---
name: spain-references
jurisdiction: ES
tax_year: 2026
last_updated: 2026-11-14
version: 2.0
type: router
description: >
  Spain source-routing catalog for the 2026 tax pack. Routes a tax question to
  the Spain Guide that owns the job and to the official original (BOE,
  Agencia Tributaria, the foral haciendas through their own Guides). Keeps the
  three open-source Spanish IRPF projects the earlier catalog listed, with
  what their authors say they do and their licence identity. Contains no
  operative rate, threshold or deadline. A project's output is not evidence
  that a 2026 figure is right.
tier: 2
domain: income-tax
---

# Spain: official sources and related open-source projects, 2026 v2.0

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

**Quick answer.** For a tax result, load the owning Guide below and the official original it cites. The three projects are research aids for IRPF data and filing formats; none is an official source and none is evidence that a figure for 2026 is right.

## Choose the owning Guide and official original

| Job | Owning Guide | Official source to open |
|---|---|---|
| Personal income tax (IRPF), territorio común | `es-income-tax`, with `es-irpf-deductions` and the regional `es-irpf-deductions-*` files | [Ley 35/2006](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764), [RD 439/2007](https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820), [AEAT IRPF](https://sede.agenciatributaria.gob.es/Sede/irpf.html) |
| Self-employed (autónomo) return workflow | `es-freelance-intake` first, then `es-return-assembly` | Same as above |
| País Vasco and Navarra income tax | `es-foral-income-tax` and the `es-foral-*` files | The foral hacienda texts those Guides cite |
| VAT return | `es-vat-return` | [Ley 37/1992](https://www.boe.es/buscar/act.php?id=BOE-A-1992-28740), [RD 1624/1992](https://www.boe.es/buscar/act.php?id=BOE-A-1992-28925) |
| Corporate tax | `es-corporate-tax` | The texts that Guide cites |
| Social contributions | `es-social-contributions` | The texts that Guide cites |
| Non-residents | `es-non-resident-income-tax-irnr-and` | The texts that Guide cites |

## Related open-source projects: documented scope and limits

What follows reports what each author says in their README on 14 November 2026. No code was installed, run or audited. Star counts are left out because they change daily.

| Project | What the author documents | Licence on GitHub, 14 Nov 2026 |
|---|---|---|
| [joseconti/declaracion-renta-espana](https://github.com/joseconti/declaracion-renta-espana) | A Claude skill for the IRPF 2025 return (filed April to June 2026). The README says it condenses 3,214 pages of official material: the AEAT Manual Práctico de Renta (1,903 pages) and the manuals of the four foral haciendas (Navarra, Álava, Gipuzkoa, Bizkaia). Its deepest value is the foral territories, where OpenAccountants may be thinner. | GPL-3.0 |
| [paumrch/larenta](https://github.com/paumrch/larenta) | larenta.es: a guide to IRPF 2025 with 375 state and regional deductions as structured data, with AEAT sources, and an assistant that matches deductions to a situation. Already credited in OpenAccountants. | MIT |
| [jatorre/hacienda-cli](https://github.com/jatorre/hacienda-cli) | An unofficial CLI for the AEAT electronic office (Cl@ve or certificate): downloads fiscal data, validates Modelo 100 XML against the official XSD and uploads declarations. Useful to understand the Modelo 100 XML fields an asesor fiscal fills. The README warns it has no link to the AEAT and gives no tax advice. | MIT |

## The method, step by step

1. Fix the tax year, the territory (territorio común, a foral territory, Canarias, Ceuta or Melilla) and the job.
2. Load the owning Guide from the first table. Take every figure from that Guide and the official page it links, never from this catalog or a project.
3. Use a project only to understand data and coverage: larenta to cross-check that no regional deduction is missing from `es-irpf-deductions`; declaracion-renta-espana for where the foral manuals cover a point the `es-foral-*` Guides do not; hacienda-cli for the Modelo 100 XML structure, field codes and import process that `es-return-assembly` output can map to.
4. All three projects are for tax year 2025. Before using anything from them for 2026, confirm the rule on BOE or the AEAT page for 2026.
5. Before reusing content, read the project's actual licence file and keep attribution. GPL-3.0 and MIT content can flow into AGPL-3.0 with attribution; this catalog gives no further legal opinion.

## When to refuse or refer

- A tax figure or position asked of this catalog: route to the owning Guide.
- A request to log into the AEAT electronic office or file with a project tool for a client: refuse; filing belongs to the client or their asesor fiscal.
- A foral territory point no `es-foral-*` Guide covers: refer to an asesor fiscal in that territory.

## Sources

| Source and what was read | URL | Read on |
|---|---|---|
| Read for the AEAT IRPF landing page, the entry to the return campaign and the IRPF help | https://sede.agenciatributaria.gob.es/Sede/irpf.html | 2026-11-14 |
| Read for the Ley del IRPF consolidated text as the owning law (title and in-force text only) | https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764 | 2026-11-14 |
| Read for the declaracion-renta-espana README: scope, tax year 2025, the 3,214 and 1,903 page counts, foral manuals | https://raw.githubusercontent.com/joseconti/declaracion-renta-espana/main/README.md | 2026-11-14 |
| Read for the larenta README: IRPF 2025, 375 deductions | https://raw.githubusercontent.com/paumrch/larenta/master/README.md | 2026-11-14 |
| Read for the hacienda-cli README: unofficial warning, Modelo 100 XML and XSD validation | https://raw.githubusercontent.com/jatorre/hacienda-cli/main/README.md | 2026-11-14 |
| Read for the licence identity of each repository (GitHub repository metadata, all three) | https://api.github.com/repos/jatorre/hacienda-cli | 2026-11-14 |

Not yet confirmed: whether any of the three projects will publish a 2026 version; the correctness of any project's output; the full licence terms beyond the SPDX identity GitHub shows.
