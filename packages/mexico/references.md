---
name: mexico-references
description: >
  Find the official primary sources used by the Mexico 2026 tax pack and the open-source
  projects the old file listed. Use when looking for the Ley del Impuesto Sobre la Renta, the
  Ley del IVA, the Resolución Miscelánea Fiscal 2026 and its Anexo 8 tariffs, the Diario Oficial
  de la Federación decrees, or SAT's article-by-article law portal. Start from the Guide that owns
  the tax job, then open its cited official text. This is a source-navigation router without tax
  rates, calculations or filing authority. Open-source CFDI libraries are tooling references,
  not tax authority evidence.
version: "2.0"
jurisdiction: MX
tax_year: 2026
last_updated: 2026-11-14
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: tax
type: router
---

# Mexico: official source index 2026 v2.0

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## The method, step by step

**Quick answer:** load the Guide that owns the job, then read the official text it cites. This router holds no rates of its own.

1. Pick the owning Guide from the [pack map](README.md): individual income tax [mx-income-tax](mx-income-tax.md), monthly provisional payments [mx-estimated-tax](mx-estimated-tax.md), companies [mx-corporate-income-tax](mx-corporate-income-tax.md), IVA [mexico-iva](mexico-iva.md), payroll withholding [mx-payroll-withholding](mx-payroll-withholding.md), IMSS and INFONAVIT [mx-social-contributions](mx-social-contributions.md) and [mx-imss](mx-imss.md), transfer pricing [mexico-transfer-pricing](mexico-transfer-pricing.md), non-residents [mx-cross-border](mx-cross-border.md), CFDI [mexico-einvoice](mexico-einvoice.md) and [mx-cfdi](mx-cfdi.md), crypto [mexico-crypto-tax](mexico-crypto-tax.md).
2. **Statute text.** SAT publishes the laws article by article on its portal (for example the Ley del IVA at https://wwwmatnp.sat.gob.mx/ordenamiento/37585/ley-del-impuesto-al-valor-agregado). The Cámara de Diputados consolidated PDFs (www.diputados.gob.mx/LeyesBiblio) are the other consolidated copy; when that site does not answer, use the SAT article page or the reform decree in the Diario Oficial de la Federación (dof.gob.mx), and say which you read.
3. **Yearly figures.** ISR tariffs are not in the statute: they are published each year in Anexo 8 of the Resolución Miscelánea Fiscal (RMF 2026, DOF 28-12-2025). Updated CFF amounts (for example Art. 32-H) are in Anexo 5 of the same publication. Do not inflate an old table by a guessed factor.
4. **Decrees with an end date.** Stimulus decrees (the northern and southern border decrees) carry a validity date; check the latest DOF extension (DOF 31-12-2025 extended them to 31 December 2026).
5. **UMA.** Amounts the law states in minimum wages are read in UMA since the 2016 de-indexation; INEGI publishes the daily, monthly and annual UMA each year.
6. Record the URL, the part read, the read date and a short quotation in the owning Guide's Sources table. A server answering is not a read.
7. **Open-source tooling (not tax authority).** The old file listed two projects, kept here as tooling pointers only: phpcfdi/cfdi-sat-scraper (MIT, PHP library to download CFDI XML from the SAT portal) and NeoRazorX/facturascripts (LGPL-3.0, PHP ERP with a Mexican CFDI module). Their licences and accuracy were not re-checked today; never cite them for a tax rule.

## When to refuse or refer

Stop the affected figure when the official text or the year's Anexo cannot be read; record it on the owning Guide's Not yet confirmed line. Refer IMMEX, consolidated groups, treaty-by-treaty withholding and state payroll taxes to their own official texts and a qualified professional. Do not treat a vendor summary, a calculator, an open-source repository or another AI as evidence of Mexican law.

## Sources

| Source and portion read | URL | Read on |
|---|---|---|
| SAT law portal, Ley del IVA index page, read for the article list and structure | https://wwwmatnp.sat.gob.mx/ordenamiento/37585/ley-del-impuesto-al-valor-agregado | 2026-11-14 |
| SAT, RMF 2026 Anexo 8, read for the structure of the 2026 tariffs (sections A, B and C) | https://www.sat.gob.mx/minisitio/NormatividadRMFyRGCE/documentos2026/rmf/anexos/Anexo-8-RMF-2026_DOF-28122025.pdf | 2026-11-14 |
| DOF 28-12-2025, RMF 2026 Anexos 4, 5, 6, 8, 15 and 25, read for Anexo 5 (updated CFF amounts) | https://dof.gob.mx/nota_detalle.php?codigo=5777219&fecha=28/12/2025 | 2026-11-14 |
| DOF 31-12-2025, border stimulus decrees extension, read for validity to 31 December 2026 | https://dof.gob.mx/nota_detalle.php?codigo=5777697&fecha=31/12/2025 | 2026-11-14 |
| INEGI, Unidad de Medida y Actualización, read for the 2025 and 2026 UMA values table | https://www.inegi.org.mx/temas/uma/ | 2026-11-14 |

Not yet confirmed: the current licences and maintenance status of the two open-source projects; the consolidated LISR and CFF texts on www.diputados.gob.mx (the site refused connections on 2026-11-14).
