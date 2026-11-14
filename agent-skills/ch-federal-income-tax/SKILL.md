---
name: ch-federal-income-tax
description: "Use this reference for Swiss federal income tax (direkte Bundessteuer / impot federal direct) for self-employed individuals resident in Switzerland. Trigger on phrases like \"Bundessteuer\", \"direkte Bundessteuer\", \"impot federal direct\", \"Steuererklarung Schweiz\", \"selbstandig Steuern Schweiz\", \"Swiss federal income tax\", \"self-employed tax Switzerland\", \"AHV deduction\", \"Saule 3a\", \"BVG\", \"Geschaftsaufwand\", or any question about computing or filing FEDERAL income tax for a self-employed person in Switzerland. Covers the DBG Art. 36 tariffs for tax period 2026, with 2025 as a comparison and enacted 2027 figures, Geschaftsaufwand, depreciation, AHV/IV/EO deductibility, BVG and Saule 3a deductions, and federal filing and collection. Cantonal and municipal taxes are out of scope. This Tier 2 draft supports source checking and reviewer questions; it does not authorise filing, payment or a tax position."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/ch-federal-income-tax"
  jurisdiction: "CH"
  tax_year: "2026"
  last_updated: "2026-11-14"
---

# Switzerland Federal Income Tax (Direkte Bundessteuer): Self-Employed Skill v2.4

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Who this applies to

This reference covers the direkte Bundessteuer (DBSt), the Swiss federal income tax on natural persons, for individuals resident in Switzerland who are self-employed, including those who also have employment, rental or capital income. The Act is the Bundesgesetz über die direkte Bundessteuer (DBG, SR 642.11). The currency is CHF. The tax authority is the Eidgenössische Steuerverwaltung (ESTV / AFC), which oversees the tax; the cantons assess and collect it (DBG Art. 2).

The period label is tax period (Steuerperiode) 2026, the calendar year 2026 (DBG Art. 40). The tariff for 2026 is the one set by the FDF ordinance of 10 September 2025 on cold progression. Tax period 2025 is kept as a comparison, because a 2025 return can still be in progress. Enacted 2027 figures are shown for reference only.

**This file covers FEDERAL tax only.** Cantonal and communal income tax is a separate tax under each canton's own law. It is not computed here, and federal tax alone is never the total tax burden. No cantonal statute was read. The only cantonal material read is the Zurich and Bern pages named under 'Deadlines and filing'.

### What this file is

This is a Tier 2 source-cited draft. It has no accountant sign-off: the earlier version recorded its validation as pending, and no approval carries into this text. Working paper only: nothing here is a filing position, and a Treuhänder, Steuerberater or equivalent must review every output before use. The base workflow is `income-tax-workflow-base`, read with `workflow-base`. This file fills their country slots.

Each statement carries one of these meanings:

- **Enacted:** read in the DBG or another federal Act or ordinance on Fedlex, the official publication platform of federal law.
- **ESTV practice:** read in an ESTV leaflet, form or page. It guides assessment and is not statute.
- **Cantonal page:** read on a canton's own website, for that canton only.
- **Derived:** computed or reasoned here from read text.
- **Held:** not proven. It appears on the 'Not yet confirmed:' line after the Sources table. Silence in this file is not a finding that a rule does not exist.

### Companion guides

These are the other Swiss files in this repository. Consume a companion's output where one is loaded; none of these was checked figure by figure against this file.

| Companion | Owns |
| --- | --- |
| `ch-cantonal-tax` | Cantonal and communal income tax |
| `ch-ahv-iv` | AHV/IV contribution computation; this file needs only the deduction and the headline figures |
| `ch-lump-sum` | Expenditure taxation (Aufwandbesteuerung, DBG Art. 14) |
| `ch-corporate-income-tax` | Companies; see R-CH-2 |
| `ch-company-formation` | Choice and formation of a company |
| `switzerland-vat` | MWST returns and the net or gross treatment of a supply |
| `switzerland-crypto-tax` | Crypto assets |
| `ch-tax-overview` | Orientation across Swiss taxes |

### Refusals and boundaries

The codes R-CH-1 to R-CH-5 and their messages are kept from the earlier version, with the spelling 'Treuhänder' restored. R-CH-6 and R-CH-7 give codes to its 2 hard stops. If a trigger fires, stop that work, give the message exactly and do not produce a partial classification or computation.

| Code | Trigger | Exact message |
| --- | --- | --- |
| R-CH-1 | The request is to compute, estimate or file cantonal or communal tax, or a total tax figure that includes either | 'This skill covers FEDERAL tax only. Cantonal and municipal taxes require separate cantonal skills or Treuhänder consultation. Do not estimate.' |
| R-CH-2 | The taxpayer is a corporation or other legal person, including an AG, GmbH or Verein | 'Corporate taxation is separate. Out of scope.' |
| R-CH-3 | The person lacks tax residence or stay in Switzerland (DBG Art. 3) for all or part of the period, or any of the person's income is subject to Quellensteuer (DBG Art. 83 to 101) | 'Source tax for non-residents has different rules. Escalate.' |
| R-CH-4 | The person has a business, permanent establishment or real estate in more than one canton, so an interkantonale Steuerausscheidung is in question | 'Multi-canton allocation is out of scope.' |
| R-CH-5 | The request concerns a Steuererlass or other tax relief application (DBG Art. 167 to 167g) | 'Escalate to Treuhänder.' |
| R-CH-6 | There is no bank statement and no other record of the year's receipts and payments | 'I need the bank statements or other records for the full tax year before I can classify anything.' |
| R-CH-7 | A tax computation is requested and marital or registered partnership status at the end of the period is unknown | 'Marital status determines the tariff. I need it before I can compute federal tax.' |

### Required inputs

**Minimum viable:** a bank statement for the full tax year, marital status and canton of residence.

**Recommended:** all invoices, AHV/IV/EO contribution statements, BVG certificate, Säule 3a statements (BVV 3 Art. 8 requires the provider to certify them), and the prior year Steuerveranlagung.

**Ideal:** complete business accounts, Anlageverzeichnis (asset register) and provisional tax notices.

If the minimum is missing the earlier version gave a soft warning, except for 2 hard stops: no bank statement (R-CH-6) and unknown marital status (R-CH-7). A missing canton leaves the tariff computable, but deadline, portal and every cantonal fact stay Needs Input. Evidence for the return itself is what DBG Art. 125 lists; see 'Deadlines and filing'.

## Rates, bands and thresholds

### How to read the tariff

Never compute federal tax from approximate brackets. DBG Art. 36 prints a statutory amount at each threshold and a charge for each further full CHF 100. Rates below are CHF per 100 of taxable income. The 13.20 band is above the final 11.50 because it carries the tax up to a flat 11.5% of the whole income. The statutory amount at the final threshold is set separately, so the last step does not follow from the band before it.

ESTV Form 58c for 2026 gives the 2 rounding steps, and they are ESTV practice, not words in Art. 36: amounts under CHF 100 of taxable income are ignored, and the annual tax is rounded down to the next 5 Rappen where needed. Art. 36(3) is enacted: tax amounts under CHF 25 are not levied. For example, taxable income of CHF 18,400 on the Grundtarif gives CHF 24.64, so nothing is levied.

Art. 39(2) requires the FDF to adjust tariff steps and deductions each year for the index at 30 June before the tax period, with no adjustment after negative inflation. That is why each year below has its own table. Use the table for the tax period being assessed, whichever year the return is filed.

### Grundtarif (DBG Art. 36(1)), tax period 2026

Status: Enacted.

| Taxable income from (CHF) | Tax at that figure (CHF) | CHF per further 100 | Source |
| --- | --- | --- | --- |
| Up to 15,200 | 0.00 | 0.77 | DBG Art. 36(1), https://fedlex.data.admin.ch/filestore/fedlex.data.admin.ch/eli/cc/1991/1184_1184_1184/20260101/de/html/fedlex-data-admin-ch-eli-cc-1991-1184_1184_1184-20260101-de-html-2.html |
| 33,200 | 138.60 | 0.88 | same |
| 43,500 | 229.20 | 2.64 | same |
| 58,000 | 612.00 | 2.97 | same |
| 76,200 | 1,152.50 | 5.94 | same |
| 82,100 | 1,502.95 | 6.60 | same |
| 108,900 | 3,271.75 | 8.80 | same |
| 141,500 | 6,140.55 | 11.00 | same |
| 185,100 | 10,936.55 | 13.20 | same |
| 793,900 | 91,298.15 | none, next row at 794,000 | same |
| 794,000 and above | 91,310.00 | 11.50 | same |

### Tariff for married couples and qualifying households (DBG Art. 36(2) and (2bis)), tax period 2026

Status: Enacted. Art. 36(2) applies to spouses living in a legally and factually undivided marriage. Art. 9(1bis) treats registered partners the same way. Art. 36(2bis) applies it also to widowed, separated, divorced and single persons who live in one household with children or persons in need of support and mainly bear their maintenance. Married couples and these taxpayers, where they live with children or supported persons and mainly bear their maintenance, then reduce the tax by the amount below for each child or supported person. ESTV Kreisschreiben Nr. 30 point 13.4.1 (Practice): both conditions must be met, the reduction cannot be shared between taxpayers and it cannot be combined with the Grundtarif.

| Taxable income from (CHF) | Tax at that figure (CHF) | CHF per further 100 | Source |
| --- | --- | --- | --- |
| Up to 29,700 | 0 | 1.00 | DBG Art. 36(2), https://fedlex.data.admin.ch/filestore/fedlex.data.admin.ch/eli/cc/1991/1184_1184_1184/20260101/de/html/fedlex-data-admin-ch-eli-cc-1991-1184_1184_1184-20260101-de-html-2.html |
| 53,400 | 237 | 2.00 | same |
| 61,300 | 395 | 3.00 | same |
| 79,100 | 929 | 4.00 | same |
| 94,900 | 1,561 | 5.00 | same |
| 108,700 | 2,251 | 6.00 | same |
| 120,600 | 2,965 | 7.00 | same |
| 130,500 | 3,658 | 8.00 | same |
| 138,400 | 4,290 | 9.00 | same |
| 144,300 | 4,821 | 10.00 | same |
| 148,300 | 5,221 | 11.00 | same |
| 150,400 | 5,452 | 12.00 | same |
| 152,400 | 5,692 | 13.00 | same |
| 941,300 | 108,249 | none, next row at 941,400 | same |
| 941,400 and above | 108,261 | 11.50 | same |
| Reduction per child or supported person | 263 | Art. 36(2bis) second sentence | same |

### Tax period 2025 tariffs, comparison

Status: Enacted. Same provisions, as set by the FDF ordinance of 22 August 2024.

| Grundtarif from (CHF) | Tax at that figure (CHF) | CHF per further 100 | Source |
| --- | --- | --- | --- |
| Up to 15,200 | 0.00 | 0.77 | DBG Art. 36(1), https://fedlex.data.admin.ch/filestore/fedlex.data.admin.ch/eli/cc/1991/1184_1184_1184/20250101/de/html/fedlex-data-admin-ch-eli-cc-1991-1184_1184_1184-20250101-de-html-16.html |
| 33,200 | 138.60 | 0.88 | same |
| 43,500 | 229.20 | 2.64 | same |
| 58,000 | 612.00 | 2.97 | same |
| 76,100 | 1,149.55 | 5.94 | same |
| 82,000 | 1,500.00 | 6.60 | same |
| 108,800 | 3,268.80 | 8.80 | same |
| 141,500 | 6,146.40 | 11.00 | same |
| 184,900 | 10,920.40 | 13.20 | same |
| 793,300 | 91,229.20 | none, next row at 793,400 | same |
| 793,400 and above | 91,241.00 | 11.50 | same |

| Art. 36(2) tariff from (CHF) | Tax at that figure (CHF) | CHF per further 100 | Source |
| --- | --- | --- | --- |
| Up to 29,700 | 0 | 1.00 | DBG Art. 36(2), https://fedlex.data.admin.ch/filestore/fedlex.data.admin.ch/eli/cc/1991/1184_1184_1184/20250101/de/html/fedlex-data-admin-ch-eli-cc-1991-1184_1184_1184-20250101-de-html-16.html |
| 53,400 | 237 | 2.00 | same |
| 61,300 | 395 | 3.00 | same |
| 79,100 | 929 | 4.00 | same |
| 94,900 | 1,561 | 5.00 | same |
| 108,600 | 2,246 | 6.00 | same |
| 120,500 | 2,960 | 7.00 | same |
| 130,500 | 3,660 | 8.00 | same |
| 138,300 | 4,284 | 9.00 | same |
| 144,200 | 4,815 | 10.00 | same |
| 148,200 | 5,215 | 11.00 | same |
| 150,300 | 5,446 | 12.00 | same |
| 152,300 | 5,686 | 13.00 | same |
| 940,800 | 108,191 | none, next row at 940,900 | same |
| 940,900 and above | 108,203.50 | 11.50 | same |
| Reduction per child or supported person | 263 | Art. 36(2bis) second sentence | same |

### Tax period 2027 tariffs, reference

Status: Enacted by the FDF ordinance of 11 September 2026, in force on 1 January 2027 and read in the DBG consolidation of that date. ESTV's tariff page listed no Form 58c for 2027 when read.

| Grundtarif from (CHF) | Tax at that figure (CHF) | CHF per further 100 | Source |
| --- | --- | --- | --- |
| Up to 15,300 | 0.00 | 0.77 | DBG Art. 36(1), https://fedlex.data.admin.ch/filestore/fedlex.data.admin.ch/eli/cc/1991/1184_1184_1184/20270101/de/html/fedlex-data-admin-ch-eli-cc-1991-1184_1184_1184-20270101-de-html-2.html |
| 33,400 | 139.35 | 0.88 | same |
| 43,700 | 229.95 | 2.64 | same |
| 58,300 | 615.35 | 2.97 | same |
| 76,500 | 1,155.85 | 5.94 | same |
| 82,400 | 1,506.30 | 6.60 | same |
| 109,400 | 3,288.30 | 8.80 | same |
| 142,200 | 6,174.70 | 11.00 | same |
| 185,900 | 10,981.70 | 13.20 | same |
| 797,400 | 91,699.70 | none, next row at 797,500 | same |
| 797,500 and above | 91,712.50 | 11.50 | same |

| Art. 36(2) tariff from (CHF) | Tax at that figure (CHF) | CHF per further 100 | Source |
| --- | --- | --- | --- |
| Up to 29,900 | 0 | 1.00 | DBG Art. 36(2), https://fedlex.data.admin.ch/filestore/fedlex.data.admin.ch/eli/cc/1991/1184_1184_1184/20270101/de/html/fedlex-data-admin-ch-eli-cc-1991-1184_1184_1184-20270101-de-html-2.html |
| 53,700 | 238 | 2.00 | same |
| 61,600 | 396 | 3.00 | same |
| 79,500 | 933 | 4.00 | same |
| 95,400 | 1,569 | 5.00 | same |
| 109,200 | 2,259 | 6.00 | same |
| 121,200 | 2,979 | 7.00 | same |
| 131,100 | 3,672 | 8.00 | same |
| 139,100 | 4,312 | 9.00 | same |
| 145,000 | 4,843 | 10.00 | same |
| 149,000 | 5,243 | 11.00 | same |
| 151,100 | 5,474 | 12.00 | same |
| 153,100 | 5,714 | 13.00 | same |
| 945,900 | 108,778 | none, next row at 946,000 | same |
| 946,000 and above | 108,790 | 11.50 | same |
| Reduction per child or supported person | 264 | Art. 36(2bis) second sentence | same |

### Deductions and limits by year

Status: Enacted. Art. 33 and 35 are identical in the 2025 and 2026 consolidations. Between 2026 and 2027 only Art. 33(1)(j), 33(3) and 33(4) moved. The employment flat rates are in the Annex to the Berufskostenverordnung headed 'ab dem Steuerjahr 2016', as adjusted on 1 January 2026; earlier and later consolidations of that Annex were not read.

| Item | 2026 (CHF) | 2025 (CHF) | 2027 (CHF) | Source |
| --- | --- | --- | --- | --- |
| Kinderabzug, per child | 6,800 | 6,800 | 6,800 | DBG Art. 35(1)(a), https://fedlex.data.admin.ch/filestore/fedlex.data.admin.ch/eli/cc/1991/1184_1184_1184/20260101/de/html/fedlex-data-admin-ch-eli-cc-1991-1184_1184_1184-20260101-de-html-2.html; 2025 https://fedlex.data.admin.ch/filestore/fedlex.data.admin.ch/eli/cc/1991/1184_1184_1184/20250101/de/html/fedlex-data-admin-ch-eli-cc-1991-1184_1184_1184-20250101-de-html-16.html; 2027 https://fedlex.data.admin.ch/filestore/fedlex.data.admin.ch/eli/cc/1991/1184_1184_1184/20270101/de/html/fedlex-data-admin-ch-eli-cc-1991-1184_1184_1184-20270101-de-html-2.html |
| Unterstützungsabzug, per supported person | 6,800 | 6,800 | 6,800 | same, DBG Art. 35(1)(b) |
| Married couple | 2,800 | 2,800 | 2,800 | same, DBG Art. 35(1)(c) |
| Insurance and savings interest, spouses together | 3,700 | 3,700 | 3,700 | same, DBG Art. 33(1)(g)(1) |
| Insurance and savings interest, others | 1,800 | 1,800 | 1,800 | same, DBG Art. 33(1)(g)(2) |
| Insurance increase per child or supported person | 700 | 700 | 700 | same, DBG Art. 33(1bis)(b) |
| Second earner, 50% of the lower earned income, minimum | 8,600 | 8,600 | 8,600 | same, DBG Art. 33(2) |
| Second earner, maximum | 14,100 | 14,100 | 14,100 | same, DBG Art. 33(2) |
| Third-party childcare, per child under 14 | 25,800 | 25,800 | 25,900 | same, DBG Art. 33(3) |
| Vocational training | 13,000 | 13,000 | 13,100 | same, DBG Art. 33(1)(j) |
| Political party contributions | 10,600 | 10,600 | 10,600 | same, DBG Art. 33(1)(i) |
| Commuting cap, employment | 3,300 | 3,300 | 3,300 | same, DBG Art. 26(1)(a) |
| Meal costs, full flat deduction, per year | 3,200 | Held | Held | Berufskostenverordnung Annex, https://fedlex.data.admin.ch/filestore/fedlex.data.admin.ch/eli/cc/1993/1363_1363_1363/20260101/de/html/fedlex-data-admin-ch-eli-cc-1993-1363_1363_1363-20260101-de-html.html |
| Meal costs, half deduction, per year | 1,600 | Held | Held | same |
| Other employment costs, 3% of net wage, minimum | 2,000 | Held | Held | same |
| Other employment costs, maximum | 4,000 | Held | Held | same |
| Side employment, 20% of net receipts, minimum | 800 | Held | Held | same |
| Side employment, maximum | 2,400 | Held | Held | same |

Art. 33(1bis)(a) raises the Art. 33(1)(g) limits by half for a taxpayer with no contributions under Art. 33(1)(d) and (e). That gives CHF 5,550 for spouses and CHF 2,700 for others (Derived).

### Säule 3a limits

Status: Enacted (BVV 3 Art. 7(1)), with the published amounts from ESTV. The test is whether the person belongs to a pension institution under Art. 80 BVG, not whether the person is self-employed.

| Category | 2026 (CHF) | 2025 (CHF) | 2027 (CHF) | Source |
| --- | --- | --- | --- | --- |
| Member of an Art. 80 BVG institution, BVV 3 Art. 7(1)(a) | 7,258 | 7,258 | 7,373 | ESTV table, https://www.estv.admin.ch/de/zinssaetze-hoechstabzuege-saeule-3a-direkte-bundessteuer |
| Not a member, BVV 3 Art. 7(1)(b): 20% of earned income, at most | 36,288 | 36,288 | 36,864 | same |
| BVG upper limit, Art. 8(1) BVG, as set in BVV 2 Art. 5 | 90,720 | 90,720 | 92,160 | https://fedlex.data.admin.ch/filestore/fedlex.data.admin.ch/eli/cc/1984/543_543_543/20260801/de/html/fedlex-data-admin-ch-eli-cc-1984-543_543_543-20260801-de-html.html; 2027 https://fedlex.data.admin.ch/filestore/fedlex.data.admin.ch/eli/cc/1984/543_543_543/20270101/de/html/fedlex-data-admin-ch-eli-cc-1984-543_543_543-20270101-de-html.html |

ESTV adds: 'Die Höchstabzüge bilden zugleich die massgeblichen Einzahlungslimiten. Aufrundungen bei der Einzahlung sind nicht zulässig.' So the published amount is also the payment limit.

Each working spouse or registered partner claims separately if both contribute (BVV 3 Art. 7(2)). Work in the other spouse's profession or business is presumed to stay within the marital duty of support, so the helping spouse may not have a Säule 3a. To claim under Art. 7 the couple must show a working relationship that goes beyond that duty, and AHV/IV contributions on that income must be accounted for in the helping spouse's name (ESTV Kreisschreiben Nr. 18a point 5.7(a), Practice). Contributions may run until at most 5 years after reference age (Art. 7(3)). The full contribution may be made in the year activity ends (Art. 7(4)), but an ordinary contribution or buy-in must be paid whilst the person is still gainfully active, and once activity has ended providers may accept no more contributions (point 5.7(e), Practice). So the 31 December date below does not extend the time to pay after activity ends. Point 5.7(e) does not say how a payment credited on the last day of activity is treated, and that is held. A temporary break does not end the right to contribute where AHV-liable replacement income is earned (point 5.1, Practice).

A buy-in under BVV 3 Art. 7a is an additional deduction on these conditions together (Art. 7a(1)): the person did not pay the maximum in the 10 years before the buy-in; was entitled to contribute under Art. 7(1) in each year concerned; and pays the full contribution for the buy-in year. The 10-year test compares contributions allowed with contributions paid. The buy-in is limited to that gap and never exceeds 8% of the BVG upper limit (Art. 7a(2)). ESTV Kreisschreiben Nr. 18a point 5.6 (Practice) calls that limit the 'kleiner Abzug', which is the Art. 7(1)(a) amount in the table above: CHF 7,258 for 2026. Each annual gap can be bought in once, though one buy-in may cover several gaps (Art. 7a(3)). No buy-in is possible after an old age benefit has been drawn (Art. 7a(4)). The person applies in writing to the provider and confirms the listed facts, including AHV-liable income in each gap year (Art. 7b). Art. 7(2) and (3) otherwise apply (Art. 7a(5)). Gaps that arose before the amendment of 6 November 2024 came into force cannot be bought in, under its transitional provision; ESTV reads that as gaps from tax year 2025 (Kreisschreiben Nr. 18a point 5.6, Practice).

ESTV Kreisschreiben Nr. 18a of 22 December 2025 adds this for the self-employed (Practice). 3a contributions are private living costs and never go through the accounts (point 5.1). A contribution counts for a year only if it is credited to the individual 3a account or policy by 31 December, or the last day of liability; a bank debit is not enough (point 5.1). Any deduction needs AHV-liable earned income, so a loss from the activity gives none (point 5.5). Earned income for the 20% limit is the profit and loss balance after tax adjustments and personal AHV/IV/EO contributions, before 3a contributions (point 5.5). A self-employed person with a side job covered by the second pillar has only the Art. 7(1)(a) limit unless exempted from that cover (point 5.7(b)). In a year that moves between employment with a pension fund and self-employment without one, the total cannot exceed the Art. 7(1)(b) maximum, and the self-employed part needs accounts for the period (point 5.7(g)). The assessing authority requires any excess to be refunded by the provider (point 9.1).

### AHV/IV/EO for the self-employed

Status: AHV and IV rates, thresholds and the AHV scale Enacted; the EO rate and combined figures are from the official leaflet 2.02 (Stand 1 January 2026). The computation belongs to `ch-ahv-iv` and the Ausgleichskasse. The rows are for 2026. For 2025 the thresholds and AHV column are the same in AHVV Art. 21 of 1 January 2025; the other 2025 figures were not separately read and are held.

| Item | 2026 | 2027 | Source |
| --- | --- | --- | --- |
| AHV rate at full scale | 8.1% | 8.1% | AHVG Art. 8(1), https://fedlex.data.admin.ch/filestore/fedlex.data.admin.ch/eli/cc/63/837_843_843/20260101/de/html/fedlex-data-admin-ch-eli-cc-63-837_843_843-20260101-de-html-1.html; 2027 https://fedlex.data.admin.ch/filestore/fedlex.data.admin.ch/eli/cc/63/837_843_843/20270101/de/html/fedlex-data-admin-ch-eli-cc-63-837_843_843-20270101-de-html-1.html |
| IV rate | 1.4% | Held | IVG Art. 3(1), https://fedlex.data.admin.ch/filestore/fedlex.data.admin.ch/eli/cc/1959/827_857_845/20260101/de/html/fedlex-data-admin-ch-eli-cc-1959-827_857_845-20260101-de-html-8.html |
| EO rate | 0.5% | Held | Leaflet 2.02, https://www.ahv-iv.ch/p/2.02.d |
| Total at full scale | 10.0% | Held | same |
| Full rate applies from income of | CHF 60,500 | CHF 61,500 | AHVG Art. 8(1), https://fedlex.data.admin.ch/filestore/fedlex.data.admin.ch/eli/cc/63/837_843_843/20260101/de/html/fedlex-data-admin-ch-eli-cc-63-837_843_843-20260101-de-html-1.html; 2027 https://fedlex.data.admin.ch/filestore/fedlex.data.admin.ch/eli/cc/63/837_843_843/20270101/de/html/fedlex-data-admin-ch-eli-cc-63-837_843_843-20270101-de-html-1.html |
| Sliding scale starts at income of | CHF 10,100 | CHF 10,300 | same |
| Minimum contribution applies at income of, or below | CHF 10,000 | CHF 10,200 | same, AHVG Art. 8(2) |
| Minimum contribution, AHV only | CHF 435 | CHF 444 | same, AHVG Art. 8(2) |
| Minimum contribution, AHV/IV/EO | CHF 530 | Held | Leaflet 2.02, https://www.ahv-iv.ch/p/2.02.d |

| Income from (CHF) | Below (CHF) | AHV only % | AHV/IV/EO total % | Source |
| --- | --- | --- | --- | --- |
| 10,100 | 17,600 | 4.35 | 5.371 | AHVV Art. 21(1), https://fedlex.data.admin.ch/filestore/fedlex.data.admin.ch/eli/cc/63/1185_1183_1185/20260101/de/html/fedlex-data-admin-ch-eli-cc-63-1185_1183_1185-20260101-de-html.html; total from leaflet 2.02, https://www.ahv-iv.ch/p/2.02.d |
| 17,600 | 23,000 | 4.45 | 5.494 | same |
| 23,000 | 25,500 | 4.55 | 5.617 | same |
| 25,500 | 28,000 | 4.65 | 5.741 | same |
| 28,000 | 30,500 | 4.75 | 5.864 | same |
| 30,500 | 33,000 | 4.85 | 5.987 | same |
| 33,000 | 35,500 | 5.05 | 6.235 | same |
| 35,500 | 38,000 | 5.25 | 6.481 | same |
| 38,000 | 40,500 | 5.45 | 6.728 | same |
| 40,500 | 43,000 | 5.65 | 6.976 | same |
| 43,000 | 45,500 | 5.85 | 7.222 | same |
| 45,500 | 48,000 | 6.05 | 7.469 | same |
| 48,000 | 50,500 | 6.35 | 7.840 | same |
| 50,500 | 53,000 | 6.65 | 8.209 | same |
| 53,000 | 55,500 | 6.95 | 8.580 | same |
| 55,500 | 58,000 | 7.25 | 8.951 | same |
| 58,000 | 60,500 | 7.55 | 9.321 | same |
| 60,500 and above | none | 8.10 | 10.000 | same |

Income is rounded down to the next CHF 100 (AHVG Art. 8(1)). The minimum is not owed if it was already paid on wages, and the person can then ask for the lowest scale rate (AHVG Art. 8(2)). AHVV Art. 21(2) has a separate rule for income creditable under Art. 6quater, which was not read. The 2027 scale is in AHVV Art. 21 of 1 January 2027 and is not reproduced. Secondary self-employment income of up to CHF 2,500 in a calendar year is charged only on request (AHVV Art. 19).

### Interest rates

Status: Enacted, in Annex 2 to the Zinssatzverordnung EFD (SR 631.014) of 10 September 2025; the 2027 column is from the ESTV table.

| Interest on direct federal tax | 2026 | 2025 | 2027 | Source |
| --- | --- | --- | --- | --- |
| Vergütungszins on prepayments | 0.0% | 0.75% | 0.0% | SR 631.014 Annex 2, https://fedlex.data.admin.ch/filestore/fedlex.data.admin.ch/eli/cc/2025/564/20260101/de/html/fedlex-data-admin-ch-eli-cc-2025-564-20260101-de-html.html; ESTV https://www.estv.admin.ch/de/zinssaetze-hoechstabzuege-saeule-3a-direkte-bundessteuer |
| Verzugszins on late payment | 4.0% | 4.5% | 4.0% | same |
| Rückerstattungszins on refunds | 4.0% | 4.5% | 4.0% | same |

### Other rates used on this page

| Item | Rate or limit | Source |
| --- | --- | --- |
| MWST standard rate | 8.1% | MWSTG Art. 25(1), https://fedlex.data.admin.ch/filestore/fedlex.data.admin.ch/eli/cc/2009/615/20250331/de/html/fedlex-data-admin-ch-eli-cc-2009-615-20250331-de-html-4.html |
| MWST exemption limit: turnover in Switzerland and abroad, from supplies not excluded by MWSTG Art. 21(2) | Under CHF 100,000 in a year | same, MWSTG Art. 10(2)(a) |
| Verrechnungssteuer on capital income | 35% | VStG Art. 13(1)(a), https://fedlex.data.admin.ch/filestore/fedlex.data.admin.ch/eli/cc/1966/371_385_384/20250101/de/html/fedlex-data-admin-ch-eli-cc-1966-371_385_384-20250101-de-html-11.html |

### Enactment position

| Measure | Status at 5 November 2026 | Treatment here | Source |
| --- | --- | --- | --- |
| Federal Act on Individual Taxation of 20 June 2025 | Accepted by referendum on 8 March 2026 with 54.23% yes. EFD's voting page says it enters into force at the latest in 2032 and the Federal Council may set an earlier date; ESTV lists 'Voraussichtlich 01.01.2032' | Not applied. Joint taxation under Art. 9 stands in every DBG consolidation read, to the one dated 1 January 2029 | EFD, https://www.efd.admin.ch/de/abstimmung-individualbesteurung; ESTV, https://www.estv.admin.ch/de/gesetzgebungs-und-verordnungsaenderungen-2027-2029 |
| Initiative 'Ja zu fairen Bundessteuern auch für Ehepaare' | Vote fixed for 29 November 2026 | Not applied. Outcome unknown when read | ESTV, https://www.estv.admin.ch/de/ehepaar-und-familienbesteuerung |
| Loss carryforward from 7 to 10 years | Act of 19 December 2025, in force on 1 January 2028 in the consolidation of that date (AS 2026 482). ESTV lists 'Voraussichtlich 01.01.2028*', with a note that commencement could be later | Not applied to 2026. See Losses | DBG Art. 31(1), https://fedlex.data.admin.ch/filestore/fedlex.data.admin.ch/eli/cc/1991/1184_1184_1184/20280101/de/html/fedlex-data-admin-ch-eli-cc-1991-1184_1184_1184-20280101-de-html.html |
| Abolition of Eigenmietwert | Act of 20 December 2024, in force on 1 January 2029 in the consolidation of that date (AS 2026 213). ESTV's list marks the date with a note that commencement could be later | Not applied to 2026 | DBG Art. 21, https://fedlex.data.admin.ch/filestore/fedlex.data.admin.ch/eli/cc/1991/1184_1184_1184/20290101/de/html/fedlex-data-admin-ch-eli-cc-1991-1184_1184_1184-20290101-de-html-6.html; ESTV, https://www.estv.admin.ch/de/gesetzgebungs-und-verordnungsaenderungen-2027-2029 |
| Flat employment cost deduction | Preliminary draft only; ESTV lists 'Frühestens 01.01.2028' | Not applied. No figure read | ESTV, https://www.estv.admin.ch/de/gesetzgebungs-und-verordnungsaenderungen-2027-2029 |

## The base

### Order of calculation

1. Identify the taxpayer: one person, or spouses or registered partners aggregated under DBG Art. 9(1) and (1bis), regardless of matrimonial property regime. Income of a child under parental authority is added to the parent's, except a child's earned income, on which the child is taxed separately (Art. 9(2)).
2. Total the income of each category below for the period. Self-employment uses the business year closed in the period (Art. 41(2)), and accounts must be closed in every period (Art. 41(3)).
3. Deduct costs: Art. 26 for employment, Art. 27 to 31 for business, Art. 32 for private assets.
4. Deduct the Art. 33 items below.
   - Art. 33(1)(a): private debt interest, up to the income taxable under Art. 20, 20a and 21 plus CHF 50,000. Interest on a loan from a company to a significant shareholder or close person, on terms well away from arm's length, is excluded.
   - Art. 33(1)(b): permanent charges, and the income share of annuities under Art. 22(3)(c).
   - Art. 33(1)(c): maintenance paid to a divorced or separated spouse, and to a parent for children under that parent's authority. Other family support duties do not count.
   - Art. 33(1)(d): contributions to AHV, IV and pension institutions under law, statute or regulation.
   - Art. 33(1)(e): Säule 3a, within the limits above.
   - Art. 33(1)(f): EO, unemployment and obligatory accident insurance.
   - Art. 33(1)(g) and (1bis): life, health and other accident insurance and savings interest, within the limits above.
   - Art. 33(1)(hbis): disability costs the taxpayer bears.
   - Art. 33(1)(i): contributions to a party that is in the party register under Art. 76a of the Federal Act on Political Rights, or is in a cantonal parliament, or reached at least 3% at the last election of a cantonal parliament.
   - Art. 33(1)(j): vocational training, on the conditions under Training.
   - Art. 33(2): second earner.
   - Art. 33(3): proven third-party childcare for a child under 14 in the same household as the taxpayer who maintains the child, directly caused by the taxpayer's work, training or incapacity.
   - Art. 33(4): from each taxable gambling win, 5% up to CHF 5,400; from online casino wins, stakes debited from the player account in the year up to CHF 26,800 (2026; CHF 26,900 for 2027).
5. Deduct the 2 items measured on income after Art. 26 to 33: Art. 33(1)(h) medical and accident costs borne by the taxpayer above 5% of that income; and Art. 33a voluntary gifts to exempt Swiss legal entities, the Confederation, cantons, communes and their institutions, if they reach CHF 100 in the year and up to 20% of that income.
6. Deduct Art. 35 social deductions, set by the circumstances at the end of the period or of liability (Art. 35(2)).
7. Apply the tariff, then deduct prepayments.

```text
taxable    = max(income - costs - art33_items - art33a - art35_items, 0)
rounded    = floor(taxable / 100) * 100
gross_tax  = amount_at_threshold + floor((rounded - threshold) / 100) * rate_per_100
tax        = max(gross_tax - reduction * dependants, 0)
billed     = floor(tax * 20) / 20
levied     = 0        where gross_tax is under CHF 25 or billed is 0
           = billed   where billed is CHF 25 or more
           = held     otherwise: 0 or billed, Needs Input
balance    = levied - provisional_payments
```

`dependants` is 0 under Art. 36(1), and then the held line cannot arise. The text does not say whether Art. 36(3) tests the tax before or after the Art. 36(2bis) reduction, and neither do ESTV Kreisschreiben Nr. 30, Form 58c, ESTV's dossier 'Geltende Steuern' or the Federal Council's dispatch of 20 May 2009. The order matters only where the tariff amount is CHF 25 or more and the amount after the reduction is above 0 and under CHF 25. There, report both results and do not choose. Case D in Example 4 shows the effect. For 2026 with 1 dependant the band is taxable income of CHF 54,800 to CHF 55,900.

### Period and household

The tax period is the calendar year (Art. 40(1)). Spouses living in an undivided marriage are assessed jointly for the whole period in which they marry (Art. 42(1)). On divorce or judicial or factual separation they are assessed separately for the whole period (Art. 42(2)). If a spouse dies they are assessed jointly to the date of death, and the survivor is assessed separately for the rest of the period at the tariff that then applies, and Art. 40(3) applies by analogy (Art. 42(3)). That survivor's part period goes to the reviewer. Other liability for part of a period (Art. 40(3)) falls under R-CH-3.

### Income categories

| Category | DBG | Note |
| --- | --- | --- |
| Employment | Art. 17 | Salary certificate figures |
| Self-employment | Art. 18 | Trade, industry, agriculture, forestry, liberal profession and every other self-employment; includes gains on business assets and transfers to private assets or foreign businesses (Art. 18(2)) |
| Moveable wealth | Art. 20 | Interest, dividends and more; 70% for qualifying holdings of at least 10% (Art. 20(1bis)) |
| Immovable wealth | Art. 21 | Rent, and rental value of own use (Art. 21(1)(b)) for 2026 |
| Pensions and benefits | Art. 22 | Capital benefits go to Art. 38 |
| Other income | Art. 23 | Replacement income; payments on death or for lasting harm; compensation for giving up an activity or not exercising a right; maintenance received |
| Exempt | Art. 24 | Art. 24 lists these, including inheritances, gifts and support payments; read the list for the item in hand |
| Private capital gains | Art. 16(3) | Exempt on private assets; business assets are Art. 18 |

Partners in a simple, general or limited partnership take their share (Art. 10(1)). Income from business holdings of at least 10% is taxable at 70% after attributable costs, and on a sale only after 1 year of ownership (Art. 18b). Hidden reserves realised in the last 2 business years on final cessation after age 55, or on disability, are taxed separately under Art. 37b. Capital benefits are taxed separately at one fifth of the tariffs in Art. 36(1), (2) and the first sentence of Art. 36(2bis), so without the reduction per child (Art. 38(2)), with no social deductions (Art. 38(3)), and Form 58c for 2026 says the table applies to them from 2026. Small wages under the simplified settlement carry 0.5% (Art. 37a). These all go to the reviewer.

### Business income and MWST

All self-employment income falls under Art. 18. The earlier version said an MWST-registered business reports net of MWST. That matches the arithmetic of a supply on which MWST is owed to the Federal Tax Administration (Derived), but no DBG text read says so, and the effect of a net tax rate or flat tax rate method is held. Where the method is unknown, that is Needs Input. A business under the MWSTG Art. 10(2)(a) turnover limit that is not registered has no MWST to extract. The rate on the invoice decides the split; do not assume 8.1%.

### Business expenses

Art. 27(1) allows costs justified by the business or profession. Art. 27(2) names these as included: depreciation and provisions under Art. 28 and 29; realised and booked losses on business assets; contributions to pension institutions for own personnel, where misuse is excluded; interest on business debts, and interest on holdings under Art. 18(2); vocational training of own personnel; and profit-skimming sanctions without a punitive purpose.

Art. 27(3) bars: bribes under Swiss criminal law; costs enabling crimes or paid in return for crimes; fines (Bussen und Geldstrafen); and punitive administrative sanctions. Art. 27(4) makes a foreign fine or punitive sanction deductible only if it offends Swiss public policy or the taxpayer credibly shows all reasonable steps were taken to comply.

Art. 34 bars the rest, in particular: household and family maintenance and status-driven private costs (lit. a); debt repayment (lit. c); acquisition, production or increase in value of assets (lit. d); and income, property gains and wealth taxes of the Confederation, cantons and communes and similar foreign taxes (lit. e). Lit. b is repealed. So other taxes, such as a business vehicle tax, are not caught by lit. e and need Art. 27(1) tested.

### Training

An owner's own vocational training is not in Art. 27(2)(e), which covers own personnel. ESTV Kreisschreiben Nr. 42 point 4.6 (Practice) gives 2 routes: own vocational training that is justified by the business is deductible in the year of the cost under Art. 27(1), and further costs the owner bears are deductible under Art. 33(1)(j). Art. 33(1)(j) is capped at CHF 13,000 for 2026 and allowed only if a first Sekundarstufe II qualification exists, or the person is 20 or over and the cost is not training up to that first qualification. It needs no link to earned income in the period and covers only costs the person bears (point 4.2). Hobby courses are excluded, and coaching and career advice are in principle not vocational training (points 4.4, 4.5). The circular gives no test for 'justified by the business', so the choice of route goes to the reviewer. For employees Art. 26(1)(c) is expressly subject to Art. 33(1)(j). Employed staff training is a business expense.

### Depreciation

Art. 28(1) allows business-justified depreciation only if it is booked or, under simplified bookkeeping (OR Art. 957(2)), shown in special tables. Art. 28(2) ties it to actual value or expected useful life. ESTV Merkblatt A/1995 gives normal rates as a percentage of book value, and rates on cost are halved (its footnote 3). It is ESTV practice. It applies only to depreciation under OR Art. 960a(3) (footnote 1), and separate leaflets cover farms, forestry, electricity works, cableways and shipping (footnote 2). The earlier version's rule of one consistent method per asset is not in the leaflet and is held.

| Asset (leaflet wording) | On book value | On cost, half |
| --- | --- | --- |
| Datenverarbeitungsanlagen, hardware and software; Büromaschinen | 40% | 20% |
| Geschäftsmobiliar, workshop and storage fittings of a furniture character | 25% | 12.5% |
| Motorfahrzeuge aller Art | 40% | 20% |
| Transportmittel other than motor vehicles | 30% | 15% |
| Apparate und Maschinen zu Produktionszwecken | 30% | 15% |
| Machines mainly on shift work or under special conditions; machines under increased chemical attack | 40% | 20% |
| Automatic control systems; safety installations; electronic measuring and test devices | 40% | 20% |
| Werkzeuge, Werkgeschirr, Maschinenwerkzeuge, Geräte, Gebinde, Gerüstmaterial, Paletten | 45% | 22.5% |
| Hotel and restaurant crockery and linen | 45% | 22.5% |
| Immaterielle Werte serving the business, including goodwill | 40% | 20% |
| Hochregallager and similar installations | 15% | 7.5% |
| Movable structures on land of others, rail sidings, industrial water pipes, tanks, containers | 20% | 10% |
| Geschäftshäuser, office and bank buildings, department stores, cinemas: building alone | 4% | 2% |
| Same: building and land in one balance sheet item | 3% | 1.5% |
| Wohnhäuser of property companies and staff housing: building alone | 2% | 1% |
| Same: building and land in one balance sheet item | 1.5% | 0.75% |
| Hotel and restaurant buildings: building alone | 6% | 3% |
| Same: building and land in one balance sheet item | 4% | 2% |
| Fabrik-, Lager- and commercial buildings: building alone | 8% | 4% |
| Same: building and land in one balance sheet item | 7% | 3.5% |

The higher building rate needs the building capitalised separately, and land itself is in principle not depreciated (footnote 4). On a combined item, depreciation stops at the value of the land (footnote 5). A building with mixed business uses takes the rates in proportion.

Energy-saving installations and environmental plant may take up to 50% of book value in each of the first 2 years, then the normal rate. Catch-up depreciation is allowed only where poor business prevented enough depreciation earlier, and the taxpayer must prove it.

### Low-value items

The earlier version allowed immediate expensing under CHF 1,000. No read text sets that figure. Merkblatt A/1995 item 4 allows special cantonal methods, such as Sofortabschreibung or Einmalerledigungsverfahren, for direct federal tax if over a longer period they reach the same result. So immediate expensing depends on the canton's practice. Treat it as Needs Input, name the canton, and otherwise capitalise under the table above. A running subscription is a period cost under Art. 27(1) and does not depend on this point.

### Losses

Art. 31(1) allows losses of the 7 business years before the tax period, so far as they could not be used in those years' income. Art. 31(2) lets contributions from third parties to clear a balance sheet deficit in a restructuring absorb older losses. From 1 January 2028 Art. 31(1) reads 10 years, and Art. 205i(2) keeps prior law for self-employed losses arising before tax period 2020. Do not apply the 10-year text to 2026.

### Home office, vehicle and phone

**Home office.** The earlier version said a home office is deductible if used predominantly for business and there are no separate business premises, split by floor area. No read text states those conditions for the self-employed, and no ESTV Kreisschreiben read does. Kreisschreiben Nr. 26 of 22 September 1995, point 4, is for employees: higher costs need proof that a room in the private home must be used mainly and regularly for the work, and occasional work at home gives no claim (Practice). Kreisschreiben Nr. 2 of 12 November 1992 covers mixed property: more than 50% business use makes the whole property a business asset (leaflet point 2.1), and for a home mainly in private use, the rental value of the business part comes off self-employment income and stays in private property income (point 3.2) (Practice). Neither text covers a rented home. For employees, Berufskostenverordnung Art. 7(1) lists a 'privates Arbeitszimmer' in the other employment costs covered by the flat rate, subject to proof of higher costs under Art. 4. Merkblatt N 1/2007 point 2 says rental value of a home in one's own house is set case by case and a fair share of rooms used for both purposes is counted. Art. 27(1) is the test for the self-employed. Flag for the reviewer.

**Vehicle.** A business and private split is required. An asset is business or private as a whole, by predominant use (DBG Art. 18(2); ESTV Kreisschreiben Nr. 2 of 12 November 1992). No circular read adds to Merkblatt N 1/2007 on the private share. For a self-employed owner this is a private share (Privatanteil), not Naturallohn. Merkblatt N 1/2007 point 5: with a logbook, split actual costs by kilometres; without one, declare 0.9% of purchase price (excluding MWST) a month, at least CHF 150 a month. The 0.9% applies from 1 January 2022. For an employee with a free company car, Berufskostenverordnung Art. 5a uses 0.9% of the purchase price a month as income from that use. Flag for the reviewer.

**Phone and internet.** Business portion only. The earlier default of 0% is replaced: the business share is Needs Input. Where all household costs for heating, power, cleaning, communications and similar items named in Merkblatt N 1/2007 point 3 went through the business, the leaflet's private share is CHF 3,540 a year for a household of 1 adult, plus CHF 900 for each further adult and CHF 600 for each child. Its amounts are averages from which clear special cases can depart.

**Private withdrawals.** Goods taken from the business are income at market value (Art. 16(2)). Merkblatt N 1/2007 point 1 sets average values for goods taken in these trades: bakeries and confectioners, grocers, dairy shops, butchers, restaurants and hotels. Its later points cover the private share of staff wages and cost deductions for staff paid in kind. Use the leaflet for those trades; they are outside this file's worked figures.

### Social contributions and pensions

Own AHV and IV contributions fall under Art. 33(1)(d), EO under Art. 33(1)(f). They are deductible under law, as Art. 33(1)(d) and (f) say. The Ausgleichskasse resolves the circular base: under AHVG Art. 9(4) deducted contributions are added back and the income grossed up to 100%, and cantonal tax authorities report income (AHVV Art. 22 and 23). Leaflet 2.02 adds administrative cost contributions of at most 5% of the contributions, and quarterly Akonto billing. Whether those costs and the Akonto timing change the deductible amount is held.

Pension contributions under Art. 33(1)(d) are deductible 'gemäss Gesetz, Statut oder Reglement'. Self-employed people are not obliged to join but may insure with the institution of their profession or their employees, or otherwise with the Auffangeinrichtung (BVG Art. 44). Art. 27(2)(c) covers contributions for own personnel, not the owner. Kreisschreiben Nr. 30 point 9.3 assumes half of ordinary contributions are already in the accounts, in a passage on the second earner deduction, and states no rule. Buy-in limits were not read. Flag for the reviewer to confirm BVG status.

### Personal deductions

Figures are under 'Deductions and limits by year'. Kinderabzug covers each minor child, or child in vocational or school training, whose maintenance the taxpayer provides; separately taxed parents split it equally if the child is under joint custody and no maintenance for the child is claimed under Art. 33(1)(c) (Art. 35(1)(a)). The extent of shared care does not change that split (ESTV Kreisschreiben Nr. 30 point 10.2, Practice). Unterstützungsabzug covers each person unable or partly unable to work to whose maintenance the taxpayer contributes at least the deduction amount; it is barred for a spouse and for children under lit. a (Art. 35(1)(b)). Art. 35(3) prorates social deductions on partial liability.

Second earner: where spouses in an undivided marriage both earn, deduct 50% of the lower earned income, minimum CHF 8,600 and maximum CHF 14,100. Earned income is taxable employment or self-employment income less Art. 26 to 31 costs and Art. 33(1)(d) to (f) deductions. Where a spouse works substantially in the other's business, or they run a business together, each is given half of the joint earned income, and the couple must prove any other split. Work is substantial if regular and of a scale for which a third party would earn at least the deduction (ESTV Kreisschreiben Nr. 30 point 9.1, Practice).

```text
lower = min(earned_a, earned_b)
second_earner = max(min(lower, clamp(50% * lower, 8,600, 14,100)), 0)
```

Where the lower earned income is under CHF 8,600 only that income is deductible, and a loss gives no deduction (ESTV Kreisschreiben Nr. 30 points 9.3 and 9.4, Practice, which print the older CHF 8,100).

### Employment costs

For the employment part of a mixed year, Art. 26(1) allows: (a) necessary commuting costs up to CHF 3,300; (b) necessary extra meal costs away from home and on shift work; and (c) other costs needed for the work, subject to Art. 33(1)(j), so that vocational training goes through that limit. Flat rates apply to (b) and (c), and proof of higher costs is open only for (c) (Art. 26(2)). Art. 26 covers each employed spouse (Berufskostenverordnung Art. 2).

Under the Berufskostenverordnung:

- Commuting is public transport, or a private vehicle per kilometre only if no public transport is available or its use is objectively unreasonable (Art. 5(2)).
- The full meal deduction applies if distance or a short meal break prevents a main meal at home, or on continuous shift or night work (Art. 6(1)). It is halved if the employer subsidises meals other than in cash or a canteen is available (Art. 6(2)). No deduction applies if meals are priced below the official valuation rates (Art. 6(3)), and it cannot be combined with the Art. 9(2) weekly stay deduction (Art. 6(6)).
- Other costs use the flat rate, or the taxpayer proves all actual costs and their necessity (Art. 4, 7). The flat rate is cut for part-year or part-time work (Art. 7(2)).
- Side employment has its own flat rate, or proof of higher costs (Art. 10).

### Withholding and prepayment

Ordinary wages of residents outside Art. 83 are not reduced by a federal tax withholding in anything read here; the tax is collected through assessment. Quellensteuer cases go to R-CH-3.

Verrechnungssteuer: capital income can arrive net of 35% (VStG Art. 13(1)(a)), so report the gross amount and record the tax beside it. A person resident in Switzerland when the income fell due can reclaim it (VStG Art. 21, 22) from the canton of residence at the end of that year (Art. 30(1)). The canton normally settles against cantonal and communal taxes and pays any surplus in cash (Art. 31(1)). It is therefore not a credit in the federal ladder above. Income left undeclared forfeits the refund, unless it was omitted negligently and is declared or added before the assessment, revision or Nachsteuer proceedings close (Art. 23).

Provisional billing: if the assessment is not ready at the due date the tax is collected provisionally on the return, the last assessment or the likely amount (Art. 162(1)). Provisional amounts count against the final tax (Art. 162(2)). Differences are charged or refunded, with interest as the FDF decides (Art. 162(3)). ESTV can authorise a canton to collect in instalments in advance; prepayment interest is then paid and no late interest is owed (SR 642.124 Art. 2).

### Currency, conversion and rounding

Work in CHF. Rounding is as shown under 'How to read the tariff'. The conversion rule for foreign currency receipts and costs in Revolut or Wise exports was not read: the rate is Needs Input.

### Conservative defaults

This file permits no factual default: the workflow base leaves that choice to the content guide, and no law read fixes the result of a missing fact here. The earlier version's defaults are mapped as follows.

| Ambiguity | Treatment | Why |
| --- | --- | --- |
| Unknown marital status | STOP, R-CH-7 | It determines the tariff |
| Unknown household facts for Art. 36(2bis) | Needs Input | Tariff turns on the fact, and both results differ |
| Tax after the Art. 36(2bis) reduction above 0 and under CHF 25, from a tariff amount of CHF 25 or more | Needs Input | The order of Art. 36(3) and Art. 36(2bis) is held. Show both results |
| Unknown BVG status | Needs Input | The earlier default of 'without BVG (higher limit)' is withdrawn: the cap turns on a fact and the higher figure is not safe. Show both limits. |
| Unknown business use % | Needs Input | Not counted in the working figure until established; show the amount at stake |
| Unknown expense category | Needs Input | Art. 34 bars the residual only once the cost is shown to fall outside the deduction articles; not counted until then |
| Unknown cantonal question | Stop, R-CH-1 | Federal only |

Tier 2 question threshold: CHF 0. No row is filtered on amount, as no floor was set. The workflow base ceiling of 10 grouped questions applies.

### Red flag thresholds

No cash floor is set. Always send these to the reviewer:

- Taxable income at or above the top threshold for the tariff in use, where the flat 11.5% applies.
- Any Art. 37b, Art. 38, Art. 18a or Art. 18b item, or any transfer of business assets to private assets.
- A year in which the business year does not close, or a period shorter than 12 months.
- A BVG buy-in, a Säule 3a buy-in, or a 3a contribution at or above the limit for the person's category.
- Marriage, divorce, separation or death in the period (Art. 42).
- Any tax return for a child's earned income, or a separated couple sharing a child deduction.
- Prior year losses being used.

### Transaction patterns

This is a deterministic pre-classifier. When a bank line matches a row, apply the treatment. If none match, go to 'The base'. 'Business expense' below always means subject to Art. 27(1) on the facts, with private use removed. A pattern is a lead, not proof; legal source for each row is the Article named under 'The base'.

**Income (credits)**

| Pattern | Tax line | Treatment | Notes |
| --- | --- | --- | --- |
| ZAHLUNG, UBERWEISUNG [client], HONORAR | Einkünfte selbstandige Erwerbstatigkeit | Business income | Extract net only if MWST-registered and the method is known |
| STRIPE PAYOUT, PAYPAL PAYOUT | Business income | Revenue | Platform payout |
| LOHN, GEHALT, ARBEITGEBER | Einkünfte unselbstandige Erwerbstatigkeit | NOT self-employment | Employment income, Art. 17 |
| MIETEINNAHME, MIETZINS | Einkünfte Liegenschaft | NOT self-employment | Rental income, Art. 21 |
| ZINSEN, KAPITALERTRAG, DIVIDENDE | Einkünfte Vermogen | NOT self-employment | Capital income, Art. 20; VSt 35% gross-up |
| STEUERRUCKERSTATTUNG, RUCKZAHLUNG | EXCLUDE | Not income | Refund of income tax; refund of a deducted cost needs review |

**Expenses (debits), business**

| Pattern | Category | Treatment | Notes |
| --- | --- | --- | --- |
| BÜROMIETE, GESCHÄFTSMIETE, OFFICE RENT | Raumkosten | Business expense | Dedicated premises |
| BERUFSHAFTPFLICHT, VERSICHERUNG (business) | Versicherung | Business expense | Professional insurance |
| TREUHAND, BUCHHALTER, STEUERBERATER | Beratungskosten | Business expense | Private return preparation is not business |
| RECHTSANWALT, NOTAR (business) | Rechtskosten | Business expense | |
| BÜROMATERIAL | Bürobedarf | Business expense | |
| WERBUNG, MARKETING, GOOGLE ADS | Werbekosten | Business expense | |
| COMPUTER, LAPTOP, PC, BÜROMÖBEL, FAHRZEUG, AUTO (business), MASCHINE, EQUIPMENT, GEBÄUDE (commercial) | Capital item | Depreciate, not a running expense | See Depreciation for the rate and Low-value items for small purchases |
| WEITERBILDUNG, KURS, SEMINAR | Weiterbildung | Staff: Art. 27(2)(e). Owner: Art. 27(1) if justified by the business; further costs Art. 33(1)(j), to CHF 13,000 for 2026 | See Training |
| VERBANDSBEITRAG, MITGLIEDSCHAFT | Beiträge | Business expense | Professional associations |
| BANKGEBÜHR, KONTOFÜHRUNG | Bankspesen | Business expense | Business account |
| STRIPE FEE, PAYPAL FEE | Transaktionskosten | Business expense | |
| SOFTWARE, LIZENZ, ABONNEMENT | IT-Kosten | Subscription: business expense. Purchased licence: see Depreciation and Low-value items | The earlier CHF 1,000 test is held |

**Social insurance and pensions**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| AHV, AUSGLEICHSKASSE, SVA | Deductible, Art. 33(1)(d) and (f) | Own contributions; staff contributions are a business cost |
| BVG, PENSIONSKASSE, AUFFANGEINRICHTUNG | Deductible under law, statute or regulation, Art. 33(1)(d) | Confirm the regulation; buy-in flagged |
| SÄULE 3A, VORSORGE 3A | Deductible within limits, Art. 33(1)(e), never in the accounts | CHF 7,258 or up to CHF 36,288 for 2026 and 2025; check the credit date |

**Travel**

| Pattern | Category | Treatment | Notes |
| --- | --- | --- | --- |
| FLUG, SWISS, EASYJET, RYANAIR | Reisekosten | Business expense | Business purpose needed |
| HOTEL, BOOKING.COM | Reisekosten | Business expense | Business travel |
| SBB, BLS, ZVV | Reisekosten | Business expense | Business travel |
| TAXI, UBER | Reisekosten | Business expense | Business purpose needed |
| TANKSTELLE, MIGROL, COOP PRONTO, BP | Fahrzeugkosten | Tier 2: business % only | See Vehicle |

**Not deductible**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| PRIVAT, LEBENSMITTEL, MIGROS, COOP (groceries) | NOT deductible | Lebenshaltungskosten, Art. 34(a) |
| BUSSE, ORDNUNGSBUSSE | NOT deductible | Art. 27(3)(c); foreign fine under Art. 27(4) goes to the reviewer |
| BUNDESSTEUER, KANTONSSTEUER, STEUERN | NOT deductible | Income tax, Art. 34(e). A line that is another tax needs reading |
| PRIVATBEZUG | NOT deductible | Drawings |

**Exclusions**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| EIGENÜBERWEISUNG, INTERNAL | EXCLUDE | Own-account transfer |
| DARLEHEN, KREDIT, AMORTISATION | EXCLUDE | Loan principal, Art. 34(c) |
| DARLEHENSZINS (business) | Deductible | Business loan interest, Art. 27(2)(d) |
| MWST ZAHLUNG | EXCLUDE from P&L | MWST liability |
| STEUERZAHLUNG | EXCLUDE | Tax payment |

### Bank exports

| Bank | Format | Key fields | Notes |
| --- | --- | --- | --- |
| UBS | CSV, PDF, MT940 | Buchungsdatum, Text, Betrag | E-banking export |
| PostFinance | CSV, PDF | Datum, Buchungstext, Gutschrift/Belastung | E-Finance export |
| ZKB (Zurcher Kantonalbank) | CSV, PDF | Datum, Text, Betrag | |
| Raiffeisen CH | CSV, PDF | Datum, Buchungstext, Betrag | |
| Credit Suisse (now UBS) | CSV, PDF | Datum, Beschreibung, Betrag | Legacy and post-merger formats |
| Revolut, Wise | CSV | Date, Counterparty, Amount | Multi-currency |

Format details are from the earlier version and were not tested against live exports.

| Term | English | Hint |
| --- | --- | --- |
| Gutschrift | Credit | Potential income |
| Belastung / Lastschrift | Debit | Potential expense |
| Überweisung | Transfer | Check direction |
| Dauerauftrag | Standing order | Regular expense |
| Kartenzahlung | Card payment | Expense |
| Bargeldbezug | Cash withdrawal | Ask purpose |
| Kontoführung | Account maintenance | Bank charge |
| Vergütung | Payment or remuneration | Often income |

### Reviewer catalogue

Home office, vehicle use, phone and internet, voluntary BVG contributions and the AHV sliding scale were the earlier version's Tier 2 items. They stay with the reviewer. Use the official AHV table: for 2026 and 2025, income from CHF 10,100 to under CHF 60,500 pays less than the full rate. The full 10.0% applies from CHF 60,500, not from CHF 10,100.

### Working paper template

Fill this only after 'Ask the client first' is done. An unanswered item stays Needs Input and is not a PENDING figure in a finished paper.

```text
SWITZERLAND FEDERAL INCOME TAX -- WORKING PAPER
Tax Period: 2026
Client: ___________________________
Marital Status: Single / Married / Registered partner / Art. 36(2bis) household
Canton: ___________ (for filing only -- cantonal tax is OUT OF SCOPE)

A. SELF-EMPLOYMENT INCOME
  A1. Business revenue (net of MWST, if applicable)   ___________
  A2. Other business income                           ___________
  A3. Total                                           ___________

B. GESCHÄFTSAUFWAND
  B1. Raumkosten                                      ___________
  B2. Versicherungen (business)                       ___________
  B3. Beratungskosten                                 ___________
  B4. IT / Software                                   ___________
  B5. Marketing                                       ___________
  B6. Reisekosten                                     ___________
  B7. Fahrzeugkosten (business %)                     ___________
  B8. Abschreibungen                                  ___________
  B9. Bankspesen                                      ___________
  B10. Übrige Geschäftsaufwand                        ___________
  B11. Total                                          ___________

C. NET SELF-EMPLOYMENT INCOME (A3 - B11)              ___________
C1. Other net income (employment, rental, capital)    ___________

D. DEDUCTIONS
  D1. AHV/IV/EO                                       ___________
  D2. BVG                                             ___________
  D3. Säule 3a                                        ___________
  D4. Insurance and savings interest, Art. 33(1)(g)   ___________
  D5. Second earner, Art. 33(2)                       ___________
  D6. Other Art. 33 and 33a items                     ___________
  D7. Kinderabzug, Unterstützungsabzug, Art. 35       ___________
  D8. Married couple, Art. 35(1)(c)                   ___________
  D9. Total deductions                                ___________

E. STEUERBARES EINKOMMEN (C + C1 - D9)                ___________

F. DIREKTE BUNDESSTEUER (tariff for the period)       ___________
G. Art. 36(2bis) reduction                            ___________
H. Provisional payments                               ___________
I. Balance                                            ___________

NOTE: This is FEDERAL TAX ONLY. Cantonal/municipal = separate.

REVIEWER FLAGS:
  [ ] Marital status confirmed (Grundtarif / Art. 36(2) tariff)?
  [ ] BVG status confirmed (affects Säule 3a limit)?
  [ ] Home office eligibility confirmed?
  [ ] Vehicle business % confirmed?
  [ ] AHV contribution rate confirmed (declining scale)?
```

### Prohibitions

- Never compute Swiss federal tax from approximate brackets: use Art. 36 for the period or the ESTV tariff table.
- Never apply the Grundtarif to spouses taxed together. Never apply the Art. 36(2) tariff to a single person, unless Art. 36(2bis) is met.
- Never estimate cantonal or municipal taxes: federal only.
- Never allow Säule 3a above the applicable maximum.
- Never allow income tax as a deduction.
- Never allow fines as deductions, subject to Art. 27(4) for foreign fines.
- Never allow capital expenditure directly as an expense, apart from a cantonal method accepted under Merkblatt A/1995 item 4.
- Never present federal tax as the total tax burden.
- Never present calculations as definitive.

### Known gaps

ESTV Kreisschreiben are read only to the extent in Sources. Each is ESTV practice for the cantons, not statute, and older ones print amounts since indexed. See the 'Not yet confirmed:' line.

## Deadlines and filing

**Portal.** The DBG names no federal portal. The canton of residence at the end of the period levies the tax (Art. 105(1)), its authority calls for the return (Art. 124(1)), and cantons must offer electronic procedures, with electronic confirmation in place of a signature (Art. 104a). Zurich uses ZHprivateTax. Bern uses TaxMe. For other cantons name the portal from the canton's own notice; it was not read here. That one return carries both federal and cantonal tax in every canton, as the earlier version said, was not confirmed and is held.

| Item | Rule | Source | Status |
| --- | --- | --- | --- |
| Duty to file | The authority calls for a return by public notice, personal notice or sending the form. A person who received neither a personal notice nor a form must still file (Art. 124(1)) | DBG Art. 124 | Enacted |
| Signature | Truthful, complete, personally signed, with attachments, on time (Art. 124(2)). Spouses sign jointly; if one does not, that spouse gets a period, after which contractual representation is assumed (Art. 113(2)) | DBG Art. 124, 113 | Enacted |
| Filing date | Art. 124 sets no calendar date. The earlier '31 March' is a canton's date: use the date on the canton's notice | DBG Art. 124 | Enacted |
| Zurich | Return due by 31 March of the year after the period, so 31 March 2027 for 2026. Extension request goes to the Gemeindesteueramt before the deadline; some communes take it online | Zurich page | Cantonal page |
| Bern | The last filing date for the 2025 return was moved automatically from 15 to 30 November 2026 after a service outage. The ordinary dates for 2026 were not read | Bern page | Cantonal page |
| Other cantons | Held | | Held |
| Attachments, all | Salary certificates; certificates of pay as an organ of a legal person; lists of all securities, claims and debts (Art. 125(1)) | DBG Art. 125 | Enacted |
| Attachments, self-employed | Signed annual accounts, or under OR Art. 957(2) statements of income and expenses, assets, and private withdrawals and contributions (Art. 125(2)) | DBG Art. 125 | Enacted |
| Records | The self-employed keep business books, Art. 125(2) statements and other related records for 10 years (Art. 126(3)) | DBG Art. 126 | Enacted |
| Due date | 1 March of the year after the tax year, so 1 March 2027 for 2026 (SR 642.124 Art. 1(1)). A final or provisional invoice is prepared for that date, and a canton may skip a provisional invoice under CHF 300. It stands even if only a provisional invoice was sent or an objection was lodged (DBG Art. 161(5)) | SR 642.124; DBG Art. 161 | Enacted |
| Special due dates | Subject to Art. 161(3) and (4) (SR 642.124 Art. 1(2)). On delivery of the assessment: tax on Art. 38 capital benefits and Nachsteuer. In every case: on the day a person who means to leave the country permanently prepares to go; when a foreign taxpayer gives up a Swiss business, holding in one, establishment, real estate or claims secured on Swiss real estate; on opening of bankruptcy; on death. Art. 161(4)(b) concerns legal persons | DBG Art. 161 | Enacted |
| Payment | Within 30 days of the due date (Art. 163(1)), subject to collection by instalments under Art. 161(1). Cantons publish due dates, payment dates and payment offices (Art. 163(3)) | DBG Art. 163 | Enacted |
| Hardship | The collecting authority can extend time or allow instalments, and can waive interest, where payment on time is a serious hardship (Art. 166). It may ask for security | DBG Art. 166 | Enacted |
| Objection | 30 days from delivery, in writing (Art. 132(1)). A discretionary assessment can be challenged only for obvious error, with reasons and evidence (Art. 132(3)) | DBG Art. 132 | Enacted |
| Assessment limit | 5 years after the period ends (Art. 120(1)), subject to Art. 152 for Nachsteuer and Art. 184 for prosecution. It does not start or stands still during objection, appeal or revision proceedings, whilst the claim is secured or deferred, and whilst neither the taxpayer nor a person jointly liable has Swiss residence or stay (Art. 120(2)). It restarts on an official act directed at establishing or enforcing the tax claim, made known to the taxpayer or a person jointly liable, an express acknowledgement, a relief application, or opening of prosecution (Art. 120(3)). Absolute limit 15 years after the period (Art. 120(4)) | DBG Art. 120 | Enacted |
| Collection limit | 5 years after the assessment is final (Art. 121(1)), with the Art. 120(2) and (3) stops and restarts (Art. 121(2)). Absolute limit 10 years after the end of the year in which the tax was finally set (Art. 121(3)) | DBG Art. 121 | Enacted |
| Nachsteuer | Facts or evidence unknown to the authority that show a missing or incomplete assessment, or a failure caused by a crime or offence against the authority, open Nachsteuer: the tax is claimed with interest (Art. 151(1)). This does not apply where income was fully declared and the authority accepted the valuation (Art. 151(2)). Proceedings can open up to 10 years after the period, and the tax must be fixed within 15 years (Art. 152(1), (3)). Opening a prosecution for evasion or a tax offence also opens these proceedings (Art. 152(2)) | DBG Art. 151, 152 | Enacted |

The source for SR 642.124 is the latest Fedlex consolidation, Stand 1 January 2022. Federal form field numbers are not given, because the return is the canton's form.

## Penalties and interest

| Item | Rule | Status |
| --- | --- | --- |
| Return not filed or defective | The person is asked to make it good within a reasonable time (Art. 124(3)). After a reminder, or where records are unreliable, the authority assesses at its discretion (Art. 130(2)) | Enacted |
| Procedural breach | Intentional or negligent failure, despite a reminder, to meet a duty under the DBG or an order under it: filing the return or attachments; a certification, information or reporting duty; or inventory duties. Fine up to CHF 1,000, and up to CHF 10,000 in serious cases or on recurrence (Art. 174) | Enacted |
| Excused delay | A late return is excused if the person proves military or civil service, absence abroad, illness or other serious reasons, and made it good within 30 days after the obstacle ended (Art. 124(4)) | Enacted |
| Reach of Art. 174 | Its words cover duties under the DBG and orders under it, so it does not reach AHV, MWST or cantonal law duties. Any penalty in those laws was not read and is held | Derived |
| Late filing fee | The earlier 'reminder + fee' is not in the DBG text read. A cantonal fee is held | Held |
| Tax evasion | Intentional or negligent: as taxpayer, causing an assessment wrongly not to be made or a final assessment to be incomplete; as a person bound to withhold at source, not withholding in full; or obtaining an unlawful refund or unjustified relief (Art. 175(1)). Fine normally 1 times the evaded tax, down to 1/3 for slight fault, up to 3 times for serious fault (Art. 175(2)) | Enacted |
| First self-report | No prosecution if the evasion is unknown to any tax authority, the person fully supports the Nachsteuer and earnestly tries to pay it (Art. 175(3)). Each later self-report: fine of 1/5 of the evaded tax on those conditions (Art. 175(4)) | Enacted |
| Attempt | 2/3 of the fine for intentional completed evasion (Art. 176(2)) | Enacted |
| Inciting or assisting | Intentional incitement, help, or acting as representative in evasion: fine up to CHF 10,000, up to CHF 50,000 in serious cases or on recurrence, plus joint liability for the evaded tax (Art. 177(1) and (2)). A first self-report under Art. 175(3)(a) and (b) ends prosecution and joint liability (Art. 177(3)) | Enacted |
| Tax fraud | Using forged, altered or untrue documents, such as books, balance sheets, income statements, salary certificates or other third-party certificates, to deceive for evasion: prison up to 3 years or a monetary penalty, and a suspended sentence can carry a fine up to CHF 10,000 (Art. 186(1)). The evasion fine is reserved (Art. 186(2)). A self-report under Art. 175(3) ends prosecution of offences committed for that evasion (Art. 186(3)). Refer it out | Enacted |
| Prosecution limit | 3 years for procedural breach and 6 for attempt, after final close of the proceedings concerned; 10 years after the period, or for an unlawful refund or relief after that calendar year, for completed evasion (Art. 184(1)). It no longer runs out once the cantonal authority has issued an order in time (Art. 184(2)) | Enacted |
| Late interest | Payable on amounts not paid on time (Art. 164(1)), at the rate above. It starts 30 days after delivery of the final or provisional invoice, 30 days after the original due date in Nachsteuer cases, and 30 days after delivery of a fine or costs order (SR 642.124 Art. 3(1)). If no invoice had arrived at the due date for reasons the payer is not responsible for, it starts 30 days after delivery (DBG Art. 164(2)) | Enacted |
| Prepayment and refund interest | Vergütungszins runs on instalments and other prepayments from receipt to the original due date, and after it on credits from voluntary payments (SR 642.124 Art. 4(1)). None if repaid within 30 days of receipt (Art. 4(2)). Rückerstattungszins runs on amounts overcollected on an invoice later reduced (Art. 5) | Enacted |

The earlier word 'Ausgleichszins' does not appear in the DBG or in SR 642.124. Use the 3 terms above; a canton's use of the word is held. The rate for a calendar year applies to all interest for that year, whatever tax year or due date the tax belongs to, with narrow exceptions (ESTV Kreisschreiben Nr. 28 of 29 January 1996, point 6.1, Practice). The day count for interest is not stated in any text read. SR 642.124 Art. 3 to 5 still refer to the Zinssatzverordnung of 25 June 2021, which SR 631.014 of 10 September 2025 replaced; the rates above are from the later text.

## Cross-border points

A person is taxable by personal connection with a tax residence or stay in Switzerland. A stay means at least 30 days with gainful activity, or at least 90 days without, ignoring temporary interruption (Art. 3(3)). A foreign resident here only to study or for treatment does not qualify (Art. 3(4)).

Liability is unlimited but does not extend to foreign businesses, permanent establishments and real estate (Art. 6(1)). The rate on the taxable part uses total income (Art. 7(1)). Someone with no Swiss residence or stay who has a Swiss business, establishment, real estate or activity is taxed on economic connection (Art. 4, 5, 6(2)); those cases and any Quellensteuer case go to R-CH-3. Art. 14 expenditure taxation is open only to persons who are not Swiss citizens, who are unlimitedly liable for the first time or after a break of at least 10 years, and who do no gainful work in Switzerland; spouses must both qualify. So a person self-employed in Switzerland fails Art. 14(1)(c). It belongs to `ch-lump-sum`. No double tax treaty was read, so treaty relief is held and is Needs Input for the reviewer.

## Two worked examples that recompute

All figures use the 2026 tables unless the case says otherwise. Each is a working illustration for a reviewer, with invented facts. The workflow base minimum of an employee, a self-employed person and a mixed case are Examples 1 to 3.

### Example 1: self-employed, single, BVG member

A single resident has net business income of CHF 100,000 after expenses. AHV/IV/EO paid is CHF 10,000. Säule 3a paid is CHF 7,258 and the person belongs to an Art. 80 BVG institution. Insurance premiums are CHF 3,000, capped at CHF 1,800. Provisional tax paid is CHF 1,200. No other income or deductions.

```oa-check
name: CH self-employed single ladder 2026
inputs:
  business_income: 100000
  ahv: 10000
  saule3a: 7258
  premiums: 3000
  ins_cap: 1800
  provisional: 1200
  threshold: 76200
  at_threshold: 1152.50
  rate: 5.94
steps:
  - ins: min(premiums, ins_cap)
  - taxable: business_income - ahv - saule3a - ins
  - rounded: floor(taxable / 100) * 100
  - gross: at_threshold + floor((rounded - threshold) / 100) * rate
  - billed: floor(gross * 20) / 20
  - balance: billed - provisional
expected:
  ins: 1800
  taxable: 80942
  rounded: 80900
  gross: 1431.68
  billed: 1431.65
  balance: 231.65
```

Result: federal tax CHF 1,431.65 and a balance of CHF 231.65. If the same person were not a BVG member, Example 5 gives the different limit.

### Example 2: employee, single

A single resident has a net wage of CHF 90,000 on the salary certificate, after employee AHV and pension contributions. Public transport commuting costs CHF 1,500. Art. 6 of the Berufskostenverordnung is met in full, so CHF 3,200 for meals. Other costs use the flat 3%. Säule 3a is CHF 7,258, as a BVG member. Premiums exceed CHF 1,800. Provisional tax paid is CHF 1,000.

```oa-check
name: CH employee single ladder 2026
inputs:
  net_wage: 90000
  travel: 1500
  meals: 3200
  saule3a: 7258
  ins: 1800
  provisional: 1000
  threshold: 58000
  at_threshold: 612
  rate: 2.97
steps:
  - other: clamp(pct(net_wage, 3), 2000, 4000)
  - taxable: net_wage - min(travel, 3300) - meals - other - saule3a - ins
  - rounded: floor(taxable / 100) * 100
  - gross: at_threshold + floor((rounded - threshold) / 100) * rate
  - billed: floor(gross * 20) / 20
  - balance: billed - provisional
expected:
  other: 2700
  taxable: 73542
  rounded: 73500
  gross: 1072.35
  billed: 1072.35
  balance: 72.35
```

Result: federal tax CHF 1,072.35 and a balance of CHF 72.35.

### Example 3: mixed income, married, 2 children

This is the earlier Test 2, rebuilt. Spouse A has net business income of CHF 120,000 and AHV/IV/EO of CHF 12,000. Spouse B has a net wage of CHF 60,000. Combined income is CHF 180,000. Each pays Säule 3a of CHF 7,258 as a BVG member, together CHF 14,516. B has commuting costs of CHF 1,200 and no meal deduction; other costs take the CHF 2,000 minimum. Premiums exceed the limit. There are 2 children in the household. Provisional tax paid is CHF 1,800.

```oa-check
name: CH married mixed ladder 2026
inputs:
  income_a: 120000
  ahv_a: 12000
  net_wage_b: 60000
  saule3a_each: 7258
  travel_b: 1200
  children: 2
  provisional: 1800
  threshold: 108700
  at_threshold: 2251
  rate: 6
  reduction: 263
steps:
  - other_b: clamp(pct(net_wage_b, 3), 2000, 4000)
  - employment_b: net_wage_b - travel_b - other_b
  - earned_a: income_a - ahv_a - saule3a_each
  - earned_b: employment_b - saule3a_each
  - second_earner: max(min(min(earned_a, earned_b), clamp(pct(min(earned_a, earned_b), 50), 8600, 14100)), 0)
  - insurance: 3700 + 700 * children
  - kids: 6800 * children
  - taxable: income_a + employment_b - ahv_a - 2 * saule3a_each - insurance - second_earner - kids - 2800
  - rounded: floor(taxable / 100) * 100
  - gross: at_threshold + floor((rounded - threshold) / 100) * rate
  - tax: max(gross - reduction * children, 0)
  - billed: floor(tax * 20) / 20
  - balance: billed - provisional
expected:
  other_b: 2000
  employment_b: 56800
  earned_a: 100742
  earned_b: 49542
  second_earner: 14100
  insurance: 5100
  kids: 13600
  taxable: 114684
  rounded: 114600
  gross: 2605
  tax: 2079
  billed: 2079
  balance: 279
```

Result: federal tax CHF 2,079 and a balance of CHF 279. The earlier expected taxable figure of about CHF 140,084 used the stale child deduction and left out the Art. 35(1)(c) deduction, the insurance limit, second earner deduction and employment costs.

### Example 4: single parent, tariff decision

A divorced person has taxable income of CHF 80,000 and 1 child. The result depends on whether the child lives in the same household and the person mainly bears the child's maintenance. Case A meets Art. 36(2bis). Case B does not. Case C is a different person who meets Art. 36(2bis) with 2 children and taxable income of CHF 30,000, to show the floor. Case D is another who meets it with 1 child and taxable income of CHF 55,000, to show the held band.

```oa-check
name: CH Art 36(2bis) decision 2026
inputs:
  taxable: 80000
  a_threshold: 79100
  a_at: 929
  a_rate: 4
  reduction: 263
  b_threshold: 76200
  b_at: 1152.50
  b_rate: 5.94
  c_taxable: 30000
  c_children: 2
  d_taxable: 55000
steps:
  - a_gross: a_at + floor((taxable - a_threshold) / 100) * a_rate
  - a_tax: max(a_gross - reduction, 0)
  - b_gross: b_at + floor((taxable - b_threshold) / 100) * b_rate
  - b_billed: floor(b_gross * 20) / 20
  - difference: b_billed - a_tax
  - c_gross: floor((c_taxable - 29700) / 100) * 1
  - c_tax: max(c_gross - reduction * c_children, 0)
  - d_gross: 237 + floor((d_taxable - 53400) / 100) * 2
  - d_after_reduction: max(d_gross - reduction, 0)
expected:
  a_gross: 965
  a_tax: 702
  b_gross: 1378.22
  b_billed: 1378.20
  difference: 676.20
  c_gross: 3
  c_tax: 0
  d_gross: 269
  d_after_reduction: 6
```

Result: Case A owes CHF 702. Case B owes CHF 1,378.20. Only the household and maintenance facts decide between them, so an unanswered fact is Needs Input. Case C owes nothing, because the reduction exceeds the CHF 3 of tax and the tax cannot go below zero. Case D stays open. The tariff amount of CHF 269 is at least CHF 25 and the amount after the reduction is CHF 6. If Art. 36(3) tests the amount before the reduction, CHF 6 is levied; if after, nothing is. The order is held, so report both: Needs Input.

### Example 5: Säule 3a limit

This covers the earlier Tests 3 and 4. Case A is a BVG member. Case B has no BVG and earned income of CHF 200,000. Case C has no BVG and earned income of CHF 30,000.

```oa-check
name: CH Saule 3a limits 2026
inputs:
  bvg_upper: 90720
  member_limit: 7258
  earned_b: 200000
  earned_c: 30000
steps:
  - cap: pct(bvg_upper, 40)
  - case_a: member_limit
  - case_b: min(pct(earned_b, 20), cap)
  - case_c: min(pct(earned_c, 20), cap)
expected:
  cap: 36288
  case_a: 7258
  case_b: 36288
  case_c: 6000
```

Result: CHF 7,258, CHF 36,288 and CHF 6,000. In Case B, 20% is CHF 40,000 but the cap is CHF 36,288. If BVG status is unknown, Case A and Case B both stay open: Needs Input.

### Example 6: choosing the right year

The same single taxpayer with rounded taxable income of CHF 82,700 pays a different amount in each year, because the band thresholds and amounts move each year.

```oa-check
name: CH Grundtarif by year
inputs:
  rounded: 82700
  rate: 6.60
steps:
  - y2025: 1500.00 + floor((rounded - 82000) / 100) * rate
  - y2026: 1502.95 + floor((rounded - 82100) / 100) * rate
  - y2027: 1506.30 + floor((rounded - 82400) / 100) * rate
expected:
  y2025: 1546.20
  y2026: 1542.55
  y2027: 1526.10
```

Result: CHF 1,546.20 for 2025, CHF 1,542.55 for 2026 and CHF 1,526.10 for 2027.

### Example 7: private car share without a logbook

The owner has no logbook. Vehicle A cost CHF 60,000 excluding MWST and Vehicle B cost CHF 12,000. Each was used for the 12 months. Merkblatt N 1/2007 point 5(b) sets the private share at 0.9% a month, at least CHF 150 a month.

```oa-check
name: CH private car share N1 2007
inputs:
  price_a: 60000
  price_b: 12000
  months: 12
steps:
  - monthly_a: max(pct(price_a, 0.9), 150)
  - monthly_b: max(pct(price_b, 0.9), 150)
  - year_a: monthly_a * months
  - year_b: monthly_b * months
expected:
  monthly_a: 540
  monthly_b: 150
  year_a: 6480
  year_b: 1800
```

Result: CHF 6,480 and CHF 1,800, the second on the minimum. With a logbook, actual costs split by kilometres replace both figures.

### Bank line cases rechecked

These are the earlier version's 6 examples. Their dates are in 2025, the comparison year.

| Line | Input | Result |
| --- | --- | --- |
| 1 | `15.03.2025 ; UBS Gutschrift ; AGENTUR ZURICH AG ; Honorar Mrz 2025 ; +8,100.00 ; CHF` | Business income. If the invoice is gross and shows MWST at 8.1%, net CHF 7,493.06 and MWST CHF 606.94. If the business is not MWST-registered (Kleinunternehmer), CHF 8,100. If registration, invoice or method is unknown: Needs Input |
| 2 | `15.02.2025 ; PostFinance Belastung ; AUSGLEICHSKASSE ZURICH ; AHV/IV/EO ; -4,800.00 ; CHF` | Deductible under Art. 33(1)(d) and (f). Reduces taxable income. Timing of an Akonto is held |
| 3 | `30.06.2025 ; ZKB Überweisung ; CREDIT SUISSE SÄULE 3A ; Einzahlung 2025 ; -7,258.00 ; CHF` | Deductible at the maximum if a BVG member. If not a member, up to 20% of earned income, at most CHF 36,288. If status is unknown: Needs Input |
| 4 | `01.04.2025 ; UBS Lastschrift ; ADOBE INC ; Creative Cloud ; -35.90 ; CHF` | Business expense, IT, as a running subscription with business use. The CHF 1,000 test is not the reason |
| 5 | `30.09.2025 ; PostFinance ; STEUERAMT ZH ; Kantonssteuer 2025 ; -5,000.00 ; CHF` | EXCLUDE. Not deductible, Art. 34(e) |
| 6 | `03.06.2025 ; UBS Karte ; DIGITEC ; Drucker ; -890.00 ; CHF` | Capital item or immediate expense depends on the canton's method (Merkblatt A/1995 item 4). The CHF 1,000 limit is held: Needs Input |

### Earlier test cases rechecked

| Test | Earlier expected result | Finding |
| --- | --- | --- |
| 1, single, net CHF 100,000, AHV CHF 10,000, 3a CHF 7,258 | Taxable CHF 82,742, tax CHF 1,542.55 | Arithmetic kept, and correct on CHF 82,700, only where no Art. 33(1)(g) premium is claimed. With the usual claim see Example 1 |
| 2, married | About CHF 140,084 | Corrected, Example 3 |
| 3, no BVG, CHF 200,000 | Cap CHF 36,288 | Kept, Example 5 |
| 4, no BVG, CHF 30,000 | CHF 6,000 | Kept, Example 5 |
| 5, printer CHF 900 | Immediate expense | Conditioned, see Low-value items |
| 6, 'How much tax in Zurich?' | Escalate | Kept as R-CH-1 |

## Ask the client first

This is intake only. Ask these before classifying anything or building any output: `workflow-base` Step 6.5 comes before Step 7. Nothing is produced with placeholder or PENDING flags. A fact left unanswered is Needs Input, or a stop where a refusal applies. Reuse what the records already show.

1. **Household:** marital or registered partner status at 31 December; children and dependants; whether they live in the household and who mainly bears their maintenance.
2. **Location:** canton and commune of residence, and any business, establishment or property in another canton or abroad.
3. **Pensions:** whether the person belongs to an Art. 80 BVG institution; Säule 3a contributions made and the date each was credited; any buy-in; whether gainful activity ended in the year, and when; for a spouse who helps in the other's business, the working relationship and whether AHV/IV is accounted for in that spouse's name.
4. **Business use:** home office, including whether it is a dedicated room and any separate business premises; vehicle use, with logbook or not; phone and internet business share.
5. **Contributions and accounts:** AHV/IV/EO paid; business year closing date; bookkeeping or simplified records; MWST registration and method.
6. **Other income and prepayment:** employment, rental and securities income; provisional tax paid; permit status if not Swiss.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| DBG, SR 642.11, Fedlex consolidation 1 January 2026, read in part; the range Art. 83 to 101 in R-CH-3 is a pointer, not fully read: Art. 2 to 10, 13, 14, 16 to 42, 83, 89, 89a, 99a, 104, 104a, 105, 113, 120, 121, 124 to 126, 130, 132, 151, 152, 161 to 167g, 174 to 177, 184 to 186, 196 | https://fedlex.data.admin.ch/filestore/fedlex.data.admin.ch/eli/cc/1991/1184_1184_1184/20260101/de/html/fedlex-data-admin-ch-eli-cc-1991-1184_1184_1184-20260101-de-html-2.html | 2026-11-05 |
| DBG, consolidation 1 January 2025, read in part: Art. 26, 31, 33, 35 and 36, compared with 2026 | https://fedlex.data.admin.ch/filestore/fedlex.data.admin.ch/eli/cc/1991/1184_1184_1184/20250101/de/html/fedlex-data-admin-ch-eli-cc-1991-1184_1184_1184-20250101-de-html-16.html | 2026-11-05 |
| DBG, consolidation 2 September 2026, read in part: compared with 1 January 2026 for tariff and deduction text | https://fedlex.data.admin.ch/filestore/fedlex.data.admin.ch/eli/cc/1991/1184_1184_1184/20260902/de/html/fedlex-data-admin-ch-eli-cc-1991-1184_1184_1184-20260902-de-html-1.html | 2026-11-05 |
| DBG, consolidation 1 January 2027, read in part: Art. 26, 33, 35 and 36 | https://fedlex.data.admin.ch/filestore/fedlex.data.admin.ch/eli/cc/1991/1184_1184_1184/20270101/de/html/fedlex-data-admin-ch-eli-cc-1991-1184_1184_1184-20270101-de-html-2.html | 2026-11-05 |
| DBG, consolidation 1 January 2028, read in part: Art. 31, 205i and their footnotes | https://fedlex.data.admin.ch/filestore/fedlex.data.admin.ch/eli/cc/1991/1184_1184_1184/20280101/de/html/fedlex-data-admin-ch-eli-cc-1991-1184_1184_1184-20280101-de-html.html | 2026-11-05 |
| DBG, consolidation 1 January 2029, read in part: Art. 9, 21 and footnotes on the 2024 Act | https://fedlex.data.admin.ch/filestore/fedlex.data.admin.ch/eli/cc/1991/1184_1184_1184/20290101/de/html/fedlex-data-admin-ch-eli-cc-1991-1184_1184_1184-20290101-de-html-6.html | 2026-11-05 |
| FDF ordinance on cold progression of 22 August 2024, read in part: tariff and deduction provisions | https://fedlex.data.admin.ch/filestore/fedlex.data.admin.ch/eli/cc/2024/479/20250101/de/html/fedlex-data-admin-ch-eli-cc-2024-479-20250101-de-html-2.html | 2026-11-05 |
| FDF ordinance on cold progression of 10 September 2025, read in part: tariff and deduction provisions | https://fedlex.data.admin.ch/filestore/fedlex.data.admin.ch/eli/cc/2025/579/20260101/de/html/fedlex-data-admin-ch-eli-cc-2025-579-20260101-de-html-1.html | 2026-11-05 |
| FDF ordinance on cold progression of 11 September 2026, read in part: tariff and deduction provisions | https://fedlex.data.admin.ch/filestore/fedlex.data.admin.ch/eli/cc/2026/486/20270101/de/html/fedlex-data-admin-ch-eli-cc-2026-486-20270101-de-html.html | 2026-11-05 |
| Berufskostenverordnung, SR 642.118.1, consolidation 1 January 2026, read in full | https://fedlex.data.admin.ch/filestore/fedlex.data.admin.ch/eli/cc/1993/1363_1363_1363/20260101/de/html/fedlex-data-admin-ch-eli-cc-1993-1363_1363_1363-20260101-de-html.html | 2026-11-05 |
| SR 642.124, FDF ordinance on due date and interest, latest consolidation 1 January 2022, read in full | https://fedlex.data.admin.ch/filestore/fedlex.data.admin.ch/eli/cc/1993/717_717_717/20220101/de/html/fedlex-data-admin-ch-eli-cc-1993-717_717_717-20220101-de-html-6.html | 2026-11-05 |
| Zinssatzverordnung EFD, SR 631.014, 1 January 2026, read in part: Art. 1, 3, 5 and Annex 2 | https://fedlex.data.admin.ch/filestore/fedlex.data.admin.ch/eli/cc/2025/564/20260101/de/html/fedlex-data-admin-ch-eli-cc-2025-564-20260101-de-html.html | 2026-11-05 |
| BVV 3, SR 831.461.3, consolidation 1 January 2025, read in part: Art. 7 to 8b and the 2024 transitional provision | https://fedlex.data.admin.ch/filestore/fedlex.data.admin.ch/eli/cc/1985/1778_1778_1778/20250101/de/html/fedlex-data-admin-ch-eli-cc-1985-1778_1778_1778-20250101-de-html-5.html | 2026-11-05 |
| BVV 2, SR 831.441.1, consolidation 1 August 2026, read in part: Art. 5 | https://fedlex.data.admin.ch/filestore/fedlex.data.admin.ch/eli/cc/1984/543_543_543/20260801/de/html/fedlex-data-admin-ch-eli-cc-1984-543_543_543-20260801-de-html.html | 2026-11-05 |
| BVV 2, consolidation 1 January 2027, read in part: Art. 5 | https://fedlex.data.admin.ch/filestore/fedlex.data.admin.ch/eli/cc/1984/543_543_543/20270101/de/html/fedlex-data-admin-ch-eli-cc-1984-543_543_543-20270101-de-html.html | 2026-11-05 |
| BVG, SR 831.40, consolidation 1 January 2025, read in part: Art. 4, 8, 44 and 45 | https://fedlex.data.admin.ch/filestore/fedlex.data.admin.ch/eli/cc/1983/797_797_797/20250101/de/html/fedlex-data-admin-ch-eli-cc-1983-797_797_797-20250101-de-html-13.html | 2026-11-05 |
| AHVG, SR 831.10, consolidation 1 January 2026, read in part: Art. 8 and 9 | https://fedlex.data.admin.ch/filestore/fedlex.data.admin.ch/eli/cc/63/837_843_843/20260101/de/html/fedlex-data-admin-ch-eli-cc-63-837_843_843-20260101-de-html-1.html | 2026-11-05 |
| AHVG, consolidation 1 January 2027, read in part: Art. 8 | https://fedlex.data.admin.ch/filestore/fedlex.data.admin.ch/eli/cc/63/837_843_843/20270101/de/html/fedlex-data-admin-ch-eli-cc-63-837_843_843-20270101-de-html-1.html | 2026-11-05 |
| AHVV, SR 831.101, consolidation 1 January 2025, read in part: Art. 21 | https://fedlex.data.admin.ch/filestore/fedlex.data.admin.ch/eli/cc/63/1185_1183_1185/20250101/de/html/fedlex-data-admin-ch-eli-cc-63-1185_1183_1185-20250101-de-html-12.html | 2026-11-05 |
| AHVV, consolidation 1 January 2026, read in part: Art. 19 to 23 | https://fedlex.data.admin.ch/filestore/fedlex.data.admin.ch/eli/cc/63/1185_1183_1185/20260101/de/html/fedlex-data-admin-ch-eli-cc-63-1185_1183_1185-20260101-de-html.html | 2026-11-05 |
| AHVV, consolidation 1 January 2027, read in part: Art. 21, not reproduced | https://fedlex.data.admin.ch/filestore/fedlex.data.admin.ch/eli/cc/63/1185_1183_1185/20270101/de/html/fedlex-data-admin-ch-eli-cc-63-1185_1183_1185-20270101-de-html-2.html | 2026-11-05 |
| IVG, SR 831.20, consolidation 1 January 2026, read in part: Art. 3 | https://fedlex.data.admin.ch/filestore/fedlex.data.admin.ch/eli/cc/1959/827_857_845/20260101/de/html/fedlex-data-admin-ch-eli-cc-1959-827_857_845-20260101-de-html-8.html | 2026-11-05 |
| MWSTG, SR 641.20, consolidation 31 March 2025, read in part: Art. 10 and 25 | https://fedlex.data.admin.ch/filestore/fedlex.data.admin.ch/eli/cc/2009/615/20250331/de/html/fedlex-data-admin-ch-eli-cc-2009-615-20250331-de-html-4.html | 2026-11-05 |
| VStG, SR 642.21, consolidation 1 January 2025, read in part: Art. 13, 21 to 23, 30 and 31 | https://fedlex.data.admin.ch/filestore/fedlex.data.admin.ch/eli/cc/1966/371_385_384/20250101/de/html/fedlex-data-admin-ch-eli-cc-1966-371_385_384-20250101-de-html-11.html | 2026-11-05 |
| Merkblatt 2.02, Beiträge der Selbstständigerwerbenden, Stand 1 January 2026, read in full; its rate column shifted in extraction and was checked against AHVV Art. 21 | https://www.ahv-iv.ch/p/2.02.d | 2026-11-05 |
| ESTV Form 58c 2026, read in part: front matter, footnotes and sample rows | https://www.estv.admin.ch/dam/de/sd-web/gnde9CmEsalK/dbst-tairfe-58c-2026-dfi.pdf | 2026-11-05 |
| ESTV Form 58c 2025, read in part: front matter and sample rows | https://www.estv.admin.ch/dam/de/sd-web/ZbaRlMm2u6u2/dbst-tarife-58c-2025-de.pdf | 2026-11-05 |
| ESTV Merkblatt A/1995, geschäftliche Betriebe, read in full | https://www.estv.admin.ch/dam/de/sd-web/Qyxr5xBfdWDp/dbst-mb-a-1995-geschbetriebe-de.pdf | 2026-11-05 |
| ESTV Merkblatt N 1/2007, read in full | https://www.estv.admin.ch/dam/de/sd-web/GZQy304UTaia/dbst-mb-n1-2007-de.pdf | 2026-11-05 |
| ESTV list of Kreisschreiben for direct federal tax, read in part: titles and files | https://www.estv.admin.ch/de/kreisschreiben-direkten-bundessteuer | 2026-11-05 |
| ESTV Kreisschreiben Nr. 42 of 30 November 2017, vocational training, read in part: points 1, 3, 4.1 to 4.6 | https://www.estv.admin.ch/dam/de/sd-web/i9TZSnch31KO/dbst-ks-2017-1-042-d-de.pdf | 2026-11-05 |
| ESTV Kreisschreiben Nr. 18a of 22 December 2025, Säule 3a, read in part: points 1 to 5.7 and 9.1 | https://www.estv.admin.ch/dam/de/sd-web/yQgKmvu80LEr/dbst-ks-2025-1-018a-dv-de.pdf | 2026-11-05 |
| ESTV Kreisschreiben Nr. 30 of 21 December 2010, married couples and families, read in part: points 9, 10.1, 10.2 and 13.4.1 | https://www.estv.admin.ch/dam/de/sd-web/2YuHXYYJMbn9/dbst-ks-2010-1-030-d-de.pdf | 2026-11-05 |
| ESTV Kreisschreiben Nr. 2 of 12 November 1992 with its leaflet on Art. 18 DBG, read in part: letter and points 1 to 3.3 | https://www.estv.admin.ch/dam/de/sd-web/VAzMNeSBnAdA/dbst-ks-w95-002-de.pdf | 2026-11-05 |
| ESTV Kreisschreiben Nr. 26 of 22 September 1995, employment costs, read in full; Nr. 42 supersedes its point 3 | https://www.estv.admin.ch/dam/de/sd-web/gaWEWbZemEqp/dbst-ks-w95-026-de.pdf | 2026-11-05 |
| ESTV Kreisschreiben Nr. 28 of 29 January 1996, collection, read in full | https://www.estv.admin.ch/dam/de/sd-web/FQ3xo-wqZh0X/dbst-ks-w95-028-de.pdf | 2026-11-05 |
| ESTV dossier 'Geltende Steuern', June 2026, read in part: direct federal tax on income, searched for the CHF 25 rule | https://www.estv2.admin.ch/stp/ds/c-geltende-steuern-de.pdf | 2026-11-05 |
| Federal Council dispatch of 20 May 2009 on tax relief for families with children, BBl 2009 4729, read in part: parent tariff passages, searched for the CHF 25 rule | https://fedlex.data.admin.ch/filestore/fedlex.data.admin.ch/eli/fga/2009/815/de/pdf-a/fedlex-data-admin-ch-eli-fga-2009-815-de-pdf-a.pdf | 2026-11-05 |
| ESTV page on interest rates and 3a maximum deductions, read in part: tables | https://www.estv.admin.ch/de/zinssaetze-hoechstabzuege-saeule-3a-direkte-bundessteuer | 2026-11-05 |
| ESTV page on tariffs, read in part: list of Form 58c files | https://www.estv.admin.ch/de/steuertarife-zur-direkten-bundessteuer | 2026-11-05 |
| ESTV page on individual taxation, read in part: result and measures | https://www.estv.admin.ch/de/individualbesteuerung | 2026-11-05 |
| ESTV page on marriage and family taxation, read in part: status of the initiative | https://www.estv.admin.ch/de/ehepaar-und-familienbesteuerung | 2026-11-05 |
| ESTV page on legislative changes 2027 to 2029, read in part: list of changes | https://www.estv.admin.ch/de/gesetzgebungs-und-verordnungsaenderungen-2027-2029 | 2026-11-05 |
| EFD voting page on individual taxation, read in part: result and commencement answers | https://www.efd.admin.ch/de/abstimmung-individualbesteurung | 2026-11-05 |
| Canton of Zurich, Steuererklärung natürliche Personen page, read in part: deadline, extension and portal sections | https://www.zh.ch/de/steuern-finanzen/steuern/steuern-natuerliche-personen/steuererklaerung-natuerliche-personen.html | 2026-11-05 |
| Canton of Bern, Fristen verlängern page, read in part: notice; ordinary dates not found in the part read | https://www.sv.fin.be.ch/de/start/themen/frist-verlaengern.html | 2026-11-05 |
| Canton of Bern, tax administration start page, reached from taxme.ch, read in part: TaxMe portal | https://www.sv.fin.be.ch/de/start.html | 2026-11-05 |
| Canton of Geneva, deadline page | https://www.ge.ch/demander-delai-rendre-declaration-impots | tried 2026-11-05: 404, not read |

Not yet confirmed: cantonal filing dates and extension practice outside the Zurich and Bern text read, including Bern's ordinary 2026 dates; cantonal portals other than ZHprivateTax and TaxMe; that one return carries federal and cantonal tax in every canton; any cantonal reminder fee; any cantonal use of 'Ausgleichszins'; any consolidation of SR 642.124 after 1 January 2022, and its cross-reference to the 2025 Zinssatzverordnung; the interest day count; the CHF 1,000 immediate expense limit and each canton's Sofortabschreibung practice; the earlier version's rule of a single method per asset; home office conditions for the self-employed, including a rented home, predominant use, separate premises and floor area split; the test for an owner's training as justified by the business under Art. 27(1); net or gross reporting of MWST by net tax rate or flat tax rate method; foreign currency conversion; timing of AHV Akonto and final contributions as a deduction, and the treatment of administrative cost contributions; owner's BVG contributions, split and buy-in limits; the order of Art. 36(3) and Art. 36(2bis), on which ESTV Kreisschreiben Nr. 30, Form 58c, ESTV's dossier 'Geltende Steuern' and the dispatch of 20 May 2009 are silent, and so the result in the band that order affects; a Säule 3a payment credited on the last day of gainful activity; commencement of the Federal Act on Individual Taxation and its tariffs; the outcome of the 29 November 2026 vote and any later commencement of the 2028 and 2029 Acts for cantons; Form 58c for 2027; 2027 IV, EO and combined AHV/IV/EO figures and 2025 and 2027 flat employment cost figures; 2025 IV, EO, combined and minimum AHV figures; any penalty under AHV, MWST or cantonal law; any ESTV Kreisschreiben not in the Sources table; later consolidations of the MWSTG and VStG than those cited; double tax treaties; and the claim that cantonal and communal tax is typically the larger share of the burden.

### Version history

| Version | Date | Change |
| --- | --- | --- |
| 2.3 | 2026-11-05 | Converted to the upstream template. Moved the file to tax period 2026 with 2025 as a comparison and enacted 2027 figures; corrected the married tariff figures, child, support and training deductions, the tariff citation, Art. 36(2bis), the AHV scale, Art. 174, depreciation rates, the BVG default and worked tests; added ESTV Kreisschreiben practice on training, Säule 3a, the second earner deduction, mixed assets and interest; held the CHF 1,000 limit and cantonal dates. |
| 2.2 | 2026-11-01 | Earlier version. Validation pending. |

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a Treuhänder or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-14. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `ch-federal-income-tax` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/ch-federal-income-tax. If neither is available, confirm every figure against the official source pages cited above before relying on it.
