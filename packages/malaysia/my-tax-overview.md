---
name: my-tax-overview
description: Use this skill first for any Malaysia tax question in 2026 to route it to the right Malaysian skill. Trigger on phrases like Malaysia tax overview, Malaysian tax system, which tax applies Malaysia, LHDN or Customs, income tax or SST, Malaysian company or sole proprietor tax, payroll Malaysia, e-invoice Malaysia. It names the authorities (LHDN for income tax and e-invoicing, RMCD for sales and service tax, EPF and PERKESO for contributions, SSM for companies), the territorial basis, and which skill owns each job and each figure, so figures are read from one home. Year of assessment 2026 and calendar 2026.
version: "2.0"
jurisdiction: MY
tax_year: 2026
last_updated: 2026-11-14
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
type: router
---

# Malaysia tax overview and router, 2026

> **General reference only.** This skill routes questions to Malaysian skills. It has not been reviewed for any specific person's facts.

## The method, step by step

1. **Find the taxpayer.** Individual (employee, sole proprietor, partner), company (Sdn Bhd or Berhad), LLP, or a non-resident.
2. **Find the tax and its authority.**
   - Income tax, the Income Tax Act 1967, run by Lembaga Hasil Dalam Negeri (LHDN, IRBM). The basis is territorial: income accruing in or derived from Malaysia; foreign-source income received in Malaysia has its own rules and exemptions (refer).
   - Sales tax and service tax (SST), under the Sales Tax Act 2018 and Service Tax Act 2018, run by the Royal Malaysian Customs Department (RMCD). Malaysia has no VAT or GST; GST was repealed in 2018.
   - e-Invoicing, run by LHDN on MyInvois.
   - EPF (KWSP), SOCSO and EIS (PERKESO): contributions on wages.
   - Company law and filings: the Companies Commission of Malaysia (SSM).
3. **Load the owning skill** and take every figure from it, never from this router:

| Job | Skill |
| --- | --- |
| Individual income tax, rates, reliefs, Form B and BE | `my-income-tax` |
| Company income tax, Form C | `my-corporate-income-tax` |
| Monthly tax deduction (PCB) and CP500 instalments | `my-pcb` |
| EPF, SOCSO, EIS | `my-epf-socso` |
| Sales tax and service tax, SST-02 | `malaysia-sst` |
| e-Invoicing | `malaysia-einvoice` |
| Forming a company, SSM filings, audit exemption | `my-company-formation` |

4. **Residence first.** For individuals, residence for the basis year decides the rates (see `my-income-tax`); for companies, residence follows where management and control is exercised (see `my-corporate-income-tax`).
5. **The year.** An individual's year of assessment 2026 is calendar 2026; a company's basis period is its financial year ending in 2026.

## When to refuse or refer

| Trigger | Message |
| --- | --- |
| Real property gains tax or capital gains tax on shares | "These are separate regimes not covered by the Malaysian skills yet. Refer to a tax agent." |
| Transfer pricing, controlled transactions with related parties abroad | "Malaysia has transfer pricing rules under section 140A; no skill covers them yet. Refer." |
| Labuan entities | "Labuan has its own Act. Refer." |
| Stamp duty | "Stamp duty is under the Stamp Act 1949 and not covered yet. Refer." |
| Foreign-source income received in Malaysia | "Conditions and exemptions apply. Refer to a specialist." |

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| Read for the list of Acts LHDN administers, including the Income Tax Act 1967 as at 1 January 2026 and the Stamp Act | https://www.hasil.gov.my/en/perundangan/akta/ | 2026-11-14 |
| Read for RMCD's administration of sales tax and service tax and the MySST portal | https://mysst.customs.gov.my/faq-services-tax/ | 2026-11-14 |
| Read for LHDN's administration of e-invoicing | https://www.hasil.gov.my/en/e-invois/pelaksanaan-e-invois-di-malaysia/garis-masa-pelaksanaan-e-invois/ | 2026-11-14 |

Not yet confirmed: none. (This router carries no figures; each figure is confirmed, or listed as not confirmed, in the skill that owns it.)
