---
name: indonesia-references
jurisdiction: ID
last_updated: 2026-11-14
version: "1.2"
description: Official-source navigation for Indonesian tax methods and the evidence to read before applying a rate, deadline or taxpayer classification in calendar 2026.
tier: 2
tax_year: 2026
category: orchestrator
type: router
---

# Indonesia source navigation v1.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

This is a source router for calendar 2026, not another rates card. Read the actual law and its amendments before calculating; a source link or old repository extraction is not proof of a current figure. Named professional approval comes from the actual skill metadata, not this bibliography.

## The method, step by step

1. Identify the taxpayer, legal entity, income or transaction, actual period, residence and specific job. Start the freelance/SME workflow with `id-freelance-intake`, then load the task's existing skill from the folder rather than guessing a missing slug.
2. For the small-business final-income-tax job, read `id-pph-final-umkm`, PP 55/2022 with PP 20/2026 and the relevant administration text. Distinguish current eligibility, connected-taxpayer aggregation, original transitional periods, monthly gross base, notices and settlements. The amendment overrides the original text where they differ.
3. For company tax, payroll, VAT, bookkeeping, formation, electronic administration or return assembly, load `id-corporate-tax`, `id-payroll-pph21`, `indonesia-vat`, `id-bookkeeping`, `id-formation`, `id-einvoice-coretax` or `id-return-assembly` respectively. `id-withholding` is an accountant-approved companion; its professional approval does not extend to this file or to every other method. Do not modify its approval metadata.
4. Find the current statutory provision and read neighbouring definitions, conditions, exceptions, commencement and transitional articles. DJP hosts primary texts as well as staff-opinion articles; a staff opinion is not the law and a catalogue heading can be wrong. If authority guidance and the enactment disagree, use the enactment and record the conflict.
5. For a calculation table, record the exact original-language source passage, article, URL, actual read date and period. Link the official URL on each applicable rate row in the owning skill. A successful HTTP response alone is not a reading, and a prior-year document does not establish a current indexed amount.
6. Recompute the example and the client's supported numbers independently. For payroll, use the statutory TER annex and current official BPJS basis instead of an old calculator. For a blocked page, try an ordinary browser or a dated official-page archive and label it. Leave unresolved facts outside usable guidance on the owning skill's Not yet confirmed line.
7. Keep tax, social contributions, filing channels and payment confirmation distinct. An official portal reference does not grant authority to log in, file or pay. Obtain the actual accepted return and payment evidence through the authorised taxpayer workflow when that separate action is instructed.

### Earlier repository research, retained as history

The earlier bibliography recorded `steevenz/id-payroll-calculator` (MIT) and `KejawenLab/PPH21` (MIT). They were research leads and software-pattern references, not primary sources for Indonesian tax. Their old bracket structure, missing later top bracket, old pension ceiling, NPWP assumptions and payroll formulas must not be used as current rates. The old star counts are removed because they are changing popularity measures with no role in this tax-source job. No calculator, spreadsheet attachment or named code repository replaces the current law, TER annex, tax authority or social-security agency.

## When to refuse or refer

- The official amount, taxpayer category, applicable period or current legal text cannot be confirmed: withhold that conclusion and name the exact missing confirmation.
- An existing approved skill conflicts with another file: preserve the approval and record the source-backed discrepancy for the approving accountant; do not infer approval of an AI rewrite.
- A route names a skill that is absent: say it is missing and record the uncovered job. Do not silently switch to another country's method or invent a successful lookup.
- Residence, treaty, specialised-sector or professional-service classification needs facts outside the supported method: refer the specific issue to a Konsultan Pajak while continuing independently supported work.

## Sources

| Official source and scope actually read | URL | Read on |
|---|---|---|
| PP 20/2026, operative amendments and relevant explanations. Read for the small-business eligibility changes, owner/spouse/minor-child aggregation, permanent exits, professional activities and transitional provisions, not an audit of unrelated taxes | https://www.pajak.go.id/id/peraturan/perubahan-atas-peraturan-pemerintah-nomor-55-tahun-2022-tentang-penyesuaian-pengaturan-0 | 2026-11-14 |
| PP 55/2022, income-tax rules. Read for arts. 56-63 and69, original utilisation periods, business gross base and final-tax settlement/certificates, with changed provisions controlled by PP 20/2026 | https://www.pajak.go.id/peraturan/penyesuaian-pengaturan-di-bidang-pajak-penghasilan | 2026-11-14 |
| PMK 164/2023. Read for arts. 5-9,14,16-19 on general-rate notices, payment/withholding, annual turnover reporting, certificate withdrawal and PKP/instalment handoffs | https://www.pajak.go.id/id/peraturan/tata-cara-pengenaan-pajak-penghasilan-atas-penghasilan-dari-usaha-yang-diterima-atau | 2026-11-14 |
| DJP consolidated tax laws through UU 6/2023. Read for KUP arts. 3,7,9,28 and the explanatory accounting-basis passage, including annual deadlines, fine exclusions, interest rules, records and retention. Not claimed to include every later amendment | https://www.pajak.go.id/sites/default/files/2023-05/SDSN%202023%207.1_0.pdf | 2026-11-14 |
| Official Coretax implementation announcement. Read for taxpayer-account access, payment facilities and prefilled withholding information; no private portal or submission tested | https://www.pajak.go.id/en/node/112032 | 2026-11-14 |

Not yet confirmed: the current complete BPJS health/employment rate and indexed-ceiling evidence, statutory TER annex rows, current billing-code/annual-form schedules and each other method's topic-specific sources. The former bibliography's employment/health rates, pension ceiling, job-expense cap and no-NPWP surcharge are not current usable figures here. Their verification belongs in the respective owning method; this navigation file does not certify the whole Indonesia pack.
