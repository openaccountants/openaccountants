---
name: id-tax-optimization
description: >
  Use this skill whenever asked about Indonesian tax planning, regime selection,
  or year-end optimization for self-employed individuals (Orang Pribadi) and
  small businesses. Trigger on phrases like "Indonesia tax planning", "PPh Final
  vs progressive Indonesia", "UMKM 0.5% break-even", "PP 55/2022", "optimize
  Indonesian tax", "PTKP planning", "Indonesian tax savings", "NPPN vs pembukuan",
  "PT Perorangan vs OP", "perencanaan pajak Indonesia", "hemat pajak", "tarif
  final UMKM". It covers regime selection, entity choice, Pasal 6 and Pasal 9
  planning, PTKP, PPh Final Pasal 4(2), BPJS and year-end timing, with filing on
  the Portal Wajib Pajak (Coretax DJP). Out of scope: aggressive avoidance, treaty
  shopping, transfer pricing, paper-PT structures and CFC planning. ALWAYS read
  this skill before advising on Indonesian tax planning. This Tier 2 draft supports source checking and
  reviewer questions; it does not authorise a tax position.
version: 1.1
jurisdiction: ID
tax_year: 2026
tax_year_notes: "Planning for tax year 2026, read at 6 November 2026, under PP 55/2022 as amended by PP 20/2026, in force 22 April 2026. No PMK implementing PP 20/2026 was found in a search that was not complete."
last_updated: 2026-11-06
depends_on: []
category: tax-optimization
tier: 1
reviewed_by: "RILIA PUTRI"
reviewed_on: 2026-11-03
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
domain: tax-optimization
---

# Indonesia Tax Optimization v1.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Who this applies to

Indonesian resident self-employed individuals (Orang Pribadi, OP) and small businesses: PT Perorangan, ordinary PT, CV, firma and koperasi. Non-residents and permanent establishments (BUT) are outside it. Every output must be reviewed and signed off by a qualified professional (Konsultan Pajak bersertifikat A/B/C, Akuntan Publik, or other Indonesian-licensed practitioner) before filing or acting upon.

### What this file is

**Coverage label: planning for tax year 2026, read at 6 November 2026, under PP 55/2022 as amended by PP 20/2026, in force 22 April 2026. No PMK implementing PP 20/2026 was found in a search that was not complete.**

Each legal statement names its rung, because the rungs differ in force: UU (statute), then PP (government regulation), then PMK (ministerial regulation), then PER or SE (DJP rule or circular), then a DJP portal or press statement. A lower rung is never used to fill a gap in a higher one without saying so. A DJP press statement is not relied on for any figure here.

This guide has no `depends_on` base. It leans on these siblings, which own their figures:

- [id-income-tax](id-income-tax.md): the personal income tax computation and return.
- [id-corporate-tax](id-corporate-tax.md): the corporate computation and the Art 31E reduction in a return.
- [id-pph-final-umkm](id-pph-final-umkm.md): the 0.5% final regime in operation.
- [id-payroll-pph21](id-payroll-pph21.md): PPh 21 and BPJS payroll, including the JP wage cap.
- [id-withholding](id-withholding.md): Unifikasi withholding.
- [indonesia-vat](indonesia-vat.md): PPN returns, PKP registration and rates.
- [id-formation](id-formation.md): forming a PT or PT Perorangan.
- [id-einvoice-coretax](id-einvoice-coretax.md): Coretax DJP use.

| Field | Value |
| --- | --- |
| Country and currency | Republic of Indonesia (Republik Indonesia), Indonesian Rupiah (IDR) |
| Tax authority | Direktorat Jenderal Pajak (DJP), Ministry of Finance (Kementerian Keuangan) |
| Tax year | Calendar year, unless the taxpayer uses a book year that differs from it (UU KUP Art 1(8)) |
| Portal | Portal Wajib Pajak (PMK 81 of 2024 Art 1(21)); the sibling id-einvoice-coretax describes it as Coretax DJP |

### Refusals

Each refusal is a full stop. Give the message and do no partial planning. Escalate to a registered Konsultan Pajak.

| Trigger | Exact message |
| --- | --- |
| R-1: treaty shopping or conduit entities (Singapore, HK, NL) for P3B benefits | I cannot plan treaty benefits or conduit structures. This needs a BEPS and beneficial owner analysis by a registered Konsultan Pajak. |
| R-2: Controlled Foreign Corporation planning (PMK 93/PMK.03/2019, UU PPh Art 18(2), PP 55/2022 Art 32(2)(a)) | I cannot plan around the CFC rules. Please take this to a registered Konsultan Pajak. |
| R-3: transfer pricing structures, intra-group services or royalty restructuring (PMK 172 of 2023, which revoked PMK 213/PMK.03/2016) | I cannot design transfer pricing or intra-group structures. Please take this to a registered Konsultan Pajak. |
| R-4: participation in a tax amnesty or voluntary disclosure. The PPS window under UU 7/2021 ran from 1 January 2022 to 30 June 2022 and has closed | I cannot advise on tax amnesty or voluntary disclosure. Please take this to a registered Konsultan Pajak. |
| R-5: a 'paper PT' with no real operations | I cannot support a company with no real operations. It is exposed to UU PPh Art 18 and PP 55/2022 Art 32, and needs a registered Konsultan Pajak. |
| R-6: aggressive split invoicing between an OP and a PT controlled by the same person, including splitting turnover to stay under IDR 4,800,000,000 | I cannot design income splitting between related persons. It is exposed to UU PPh Art 18(3) and PP 55/2022 Art 32, and needs a registered Konsultan Pajak. |
| R-7: sector regimes for mining, oil and gas, plantation or financial services | This sector has its own regime, which is outside this guide. Please take this to a registered Konsultan Pajak. |
| R-8: property developer regime under PP 34/2016 | Property developer planning is outside this guide. Please take this to a registered Konsultan Pajak. |
| R-9: e-commerce marketplace seller PPN or PPh 22 issues | Marketplace PPN and PPh 22 issues are outside this guide. Please take this to a registered Konsultan Pajak. |
| R-10: cryptocurrency mining or staking optimization. PMK 81 of 2024 Art 483 item 42 revoked PMK 68/PMK.03/2022; PMK 50 of 2025 covers crypto asset trading | Crypto planning is outside this guide. Please take this to a registered Konsultan Pajak. |
| The client is not, or may not be, an Indonesian tax resident | I cannot apply these rules until Indonesian tax residence is established. Please confirm it with a registered Konsultan Pajak. |

### Rules for every answer

1. Questions come first. Ask the facts in 'Ask the client first' before any figure or comparison. No working paper, comparison or pending-flag draft comes before those answers. Whatever stays unanswered is **Needs Input**: do not fill it with an assumed rate, status, KLU or election.
2. The question threshold is 0: no fact in 'Ask the client first' is waived for a small amount.
3. Give each strategy with its condition. A strategy with an unmet condition is not available, and an unknown condition is Needs Input.
4. A move between regimes states its conditions, its deadline and whether it can be undone. See 'Moving between regimes'.
5. Optimisation sits beside UU PPh Art 18 and PP 55/2022 Art 32. A strategy holds only on its stated facts, and a saving with no business or family reason is a red flag.
6. Every comparison states whether BPJS and PPN are in it. In this file they are not, unless a line says so.

### Red flags

- Turnover is moved to a spouse, child or new PT Perorangan to stay under the ceiling. Art 58(2) and (3) of PP 55/2022 aggregate most of these, and UU PPh Art 18(3) and PP 55/2022 Art 32 reach what they do not.
- A professional calls themself a 'business' to reach the 0.5% rate. Pekerjaan bebas services are outside it.
- The 'no substance rule in Indonesia' claim. PP 55/2022 Art 32(4) lets DJP redetermine tax on substance over form.
- A client relies on a time limit, a rate or a form from a pre-2026 summary of PP 55/2022.

### When each option wins

These are starting points, each subject to the regime conditions in 'The base'.

| Situation | Starting option | Condition |
| --- | --- | --- |
| Revenue below IDR 500,000,000 a year | UMKM 0.5%, with no tax on this band for an individual (check margin) | Income is not pekerjaan bebas. A PT Perorangan has no band |
| Revenue IDR 500,000,000 to IDR 4,800,000,000, low margin | Compare UMKM Final 0.5% on gross with pembukuan | Example 2 gives the margin at which they tie |
| Revenue IDR 500,000,000 to IDR 4,800,000,000, high-margin services | UMKM Final, compared to NPPN | Only for services that are not pekerjaan bebas |
| OP in the UMKM regime for 7 years or more | No forced exit in the body of PP 55/2022: PP 20/2026 deleted Art 59 | Stay while the Art 57 and Art 58 tests are met. See 'Enactment position' for 2027 |
| Revenue above IDR 4,800,000,000 sustained | Pembukuan; consider PT Perorangan or PT | NPPN and the final rate have closed |
| Operating losses expected | Pembukuan: the only one of the 3 regimes that gives a loss to carry | UU PPh Art 6(2), up to 5 years |
| Land or building rental income | PPh Final Pasal 4(2) 10% | Not lodging services |
| Construction services | PPh Final Pasal 4(2) per PP 9/2022 | Rate by qualification and certification |

## Rates, bands and thresholds

**UMKM final tax**

| Item | Figure | Official source | URL |
| --- | --- | --- | --- |
| Final rate on gross monthly turnover | 0.5% | PP 55/2022 Art 56(2) as amended by PP 20/2026 | https://jdih.kemenkeu.go.id/api/download/d057ff82-50e7-4127-b66b-f704a36f071d/2026pp020.pdf |
| Turnover ceiling | IDR 4,800,000,000 in 1 tax year; 'not above', so exactly IDR 4,800,000,000 passes | PP 55/2022 Art 57(1) as amended by PP 20/2026 | https://jdih.kemenkeu.go.id/api/download/d057ff82-50e7-4127-b66b-f704a36f071d/2026pp020.pdf |
| Band with no tax, individuals only | First IDR 500,000,000 of turnover in 1 tax year, cumulative from the first month | UU PPh Art 7(2a) inserted by UU 7/2021; PP 55/2022 Art 60(2) and (3) | https://jdih.kemenkeu.go.id/api/download/a9faab97-aca7-4f87-9fdc-faa8123d1454/7TAHUN2021UU.pdf |
| Band for a PH or MT couple | IDR 500,000,000 for each of husband and wife | PMK 164 of 2023 Art 6(5) | https://jdih.kemenkeu.go.id/api/download/a99b8e80-9694-46ab-8de1-63c2484aa636/2023pmkeuangan164.pdf |
| Band for a PT Perorangan, koperasi or other body | None | PMK 164 of 2023 Art 6(6) | https://jdih.kemenkeu.go.id/api/download/a99b8e80-9694-46ab-8de1-63c2484aa636/2023pmkeuangan164.pdf |

**Personal income tax, UU PPh Art 17(1)(a) as amended by UU 7/2021.** Taxable income is rounded down to a full IDR 1,000 (Art 17(4)).

| Annual taxable income (IDR) | Rate | Official source | URL |
| --- | --- | --- | --- |
| Up to 60,000,000 | 5% | UU 7/2021 Art 3, amending UU PPh Art 17(1)(a) | https://jdih.kemenkeu.go.id/api/download/a9faab97-aca7-4f87-9fdc-faa8123d1454/7TAHUN2021UU.pdf |
| Over 60,000,000 to 250,000,000 | 15% | same | same |
| Over 250,000,000 to 500,000,000 | 25% | same | same |
| Over 500,000,000 to 5,000,000,000 | 30% | same | same |
| Over 5,000,000,000 | 35% | same | same |

**PTKP.** UU PPh Art 7(1) sets minimums ('paling sedikit'). PMK 101/PMK.010/2016 Art 1 sets the same amounts from tax year 2016, and JDIH shows it in force. Codes that are not in the text are sums of its parts.

| Code | Annual PTKP (IDR) | Official source | URL |
| --- | --- | --- | --- |
| TK/0 (single, no dependants) | 54,000,000 | PMK 101/PMK.010/2016 Art 1; UU PPh Art 7(1)(a) | https://jdih.kemenkeu.go.id/api/download/d8072adc-8f62-48d1-95e0-7d25c92b6362/101~PMK.010~2016Per.pdf |
| TK/1 | 58,500,000 | same, adding 4,500,000 for 1 dependant | same |
| TK/2 | 63,000,000 | same, adding 2 dependants | same |
| TK/3 | 67,500,000 | same, adding 3 dependants | same |
| K/0 (married, no dependants) | 58,500,000 | same, adding 4,500,000 for marriage | same |
| K/1 | 63,000,000 | same | same |
| K/2 | 67,500,000 | same | same |
| K/3 | 72,000,000 | same; UU PPh Art 7 gives this example | same |
| K/I/0 (wife's income combined with the husband's under Art 8(1), no dependants) | 112,500,000 | same, adding 54,000,000 for the wife | same |
| K/I/1 | 117,000,000 | same | same |
| K/I/2 | 121,500,000 | same | same |
| K/I/3 | 126,000,000 | same; UU PPh Art 7 gives this example | same |

**Business and final-tax rates**

| Item | Figure | Official source | URL |
| --- | --- | --- | --- |
| Corporate rate | 22% from tax year 2022 | UU PPh Art 17(1)(b) as amended by UU 7/2021; PP 55/2022 Art 64 | https://jdih.kemenkeu.go.id/api/download/a9faab97-aca7-4f87-9fdc-faa8123d1454/7TAHUN2021UU.pdf |
| Corporate reduction | 50% cut of the Art 17(1)(b) rate on taxable income from the part of turnover up to IDR 4,800,000,000, for a domestic body with turnover up to IDR 50,000,000,000 | UU PPh Art 31E(1) | https://jdih.kemenkeu.go.id/api/download/ea3c666f-a427-45c4-83ba-6823e46bc068/36TAHUN2008UU.htm |
| Dividends to a resident individual, not invested | 10% final | UU PPh Art 17(2c) and (2d) (not above 10%, set by PP); PP 19/2009 Art 1 | https://jdih.kemenkeu.go.id/api/download/58a33c40-41b9-426d-b935-64f63173fb71/19TAHUN2009PP.htm |
| Rental of land or buildings | 10% of gross | PP 34/2017 Art 4(1) | https://jdih.kemenkeu.go.id/api/download/c9be149c-4489-4d9e-b1f6-912808e416c4/34TAHUN2017PP.pdf |
| Land or building transfer | 2.5% general; 1% for RS and RSS by a developer; 0% to the government, or to a BUMN or BUMD with a special assignment, under the land procurement law for public interest projects | PP 34/2016 Art 2(1) | https://jdih.kemenkeu.go.id/api/download/59e6ec13-8112-41f7-b63b-6891cac23310/34TAHUN2016PP.pdf |
| Construction execution, small or individual with SBU or SKK | 1.75% | PP 9/2022 Art 3(1)(a), amending PP 51/2008 | https://jdih.kemenkeu.go.id/api/download/9f4b118b-2f73-43d0-9537-b07663657f60/9TAHUN2022PP.pdf |
| Construction execution, no SBU or SKK | 4% | PP 9/2022 Art 3(1)(b) | https://jdih.kemenkeu.go.id/api/download/9f4b118b-2f73-43d0-9537-b07663657f60/9TAHUN2022PP.pdf |
| Construction execution, others | 2.65% | PP 9/2022 Art 3(1)(c) | https://jdih.kemenkeu.go.id/api/download/9f4b118b-2f73-43d0-9537-b07663657f60/9TAHUN2022PP.pdf |
| Integrated construction, with SBU | 2.65% | PP 9/2022 Art 3(1)(d) | https://jdih.kemenkeu.go.id/api/download/9f4b118b-2f73-43d0-9537-b07663657f60/9TAHUN2022PP.pdf |
| Integrated construction, no SBU | 4% | PP 9/2022 Art 3(1)(e) | https://jdih.kemenkeu.go.id/api/download/9f4b118b-2f73-43d0-9537-b07663657f60/9TAHUN2022PP.pdf |
| Construction consultancy (planning or supervision), with SBU or SKK | 3.5% | PP 9/2022 Art 3(1)(f) | https://jdih.kemenkeu.go.id/api/download/9f4b118b-2f73-43d0-9537-b07663657f60/9TAHUN2022PP.pdf |
| Construction consultancy, no SBU or SKK | 6% | PP 9/2022 Art 3(1)(g) | https://jdih.kemenkeu.go.id/api/download/9f4b118b-2f73-43d0-9537-b07663657f60/9TAHUN2022PP.pdf |
| Bank interest, residents and BUT | 20% of gross in the 2000 text read. Applicability for 2026 is unverified: Needs Input until PP 123/2015 is checked | PP 131/2000 Art 2(a), before the unread amendment | https://jdih.kemenkeu.go.id/api/download/f3b4a965-cb82-4764-ad9f-1a79539e449b/131TAHUN2000PP.pdf |
| Bond interest, residents and BUT | 10% | PP 91/2021 Art 2 | https://jdih.kemenkeu.go.id/api/download/03829d02-e7a8-4dd6-a7ff-d881f854b218/91TAHUN2021PP.pdf |
| Lottery prizes | unverified: the earlier version says 25%; PP 132/2000 not obtained | none | not obtained |
| IDX share sales | unverified: the earlier version says 0.1% of gross; PP 41/1994 and PP 14/1997 not obtained | none | not obtained |

**PPN (VAT).** The sibling indonesia-vat owns the operation of these rates.

| Supply | Mechanics | Official source | URL |
| --- | --- | --- | --- |
| Statutory rate | 12% at the latest from 1 January 2025; 0% on exports; 5% to 15% range by regulation | UU PPN Art 7(1) to (3) as amended by UU 7/2021 | https://jdih.kemenkeu.go.id/api/download/a9faab97-aca7-4f87-9fdc-faa8123d1454/7TAHUN2021UU.pdf |
| Luxury goods subject to PPnBM | 12% × selling price or import value | PMK 131 of 2024 Art 2(2) and (3) | https://jdih.kemenkeu.go.id/api/download/f128868e-3cf6-4596-8407-c34eeca0e7be/2024pmkeuangan131.pdf |
| All other goods and services | 12% × nilai lain, which is 11/12 of the import value, selling price or replacement value; 11% of the price in effect | PMK 131 of 2024 Art 3(1) to (3) | https://jdih.kemenkeu.go.id/api/download/f128868e-3cf6-4596-8407-c34eeca0e7be/2024pmkeuangan131.pdf |
| PKP using nilai lain or besaran tertentu under separate rules | Outside Arts 2 and 3 of PMK 131 of 2024 | PMK 131 of 2024 Art 4 | https://jdih.kemenkeu.go.id/api/download/f128868e-3cf6-4596-8407-c34eeca0e7be/2024pmkeuangan131.pdf |
| Small business limit | IDR 4,800,000,000 in 1 book year, or calendar year for a taxpayer keeping no books | PMK 197/PMK.03/2013 Art 1 | https://jdih.kemenkeu.go.id/api/download/529df403-55d0-4df7-8a59-b55a2f17fd9d/197~PMK.03~2013Per.htm |

**NPPN deemed-profit rates.** Lampiran I of PER-17/PJ/2015 is a DJP rung and numbers its KLU rows to 1,434. Group 1 is the 10 capitals Medan, Palembang, Jakarta, Bandung, Semarang, Surabaya, Denpasar, Manado, Makassar and Pontianak. Group 2 is the other provincial capitals. Group 3 is everywhere else (Art 4(1)). Always look up the exact KLU. Lampiran II and III hold higher audit norms, which are not for self-assessment (Art 3).

| Activity and KLU | Group 1 | Group 2 | Group 3 | Official source | URL |
| --- | --- | --- | --- | --- | --- |
| Computer programming, 62010 | 50% | 50% | 50% | PER-17/PJ/2015 Lampiran I, DJP copy | https://www.pajak.go.id/sites/default/files/2019-03/Lampiran%201_PER%20-%2017.PJ_.2015.pdf |
| Legal services, 69100 | 51% | 50% | 50% | same | same |
| Other management consulting, 70209 | 50% | 50% | 50% | same | same |
| Other professional, scientific and technical services, 74909 | 32% | 31% | 29% | same | same |
| General retail, 47111 | 30% | 25% | 20% | same | same |
| Restaurants, 56101 | 25% | 20% | 20% | same | same |
| Residential building construction, 41011 (subject to the PPh Final Pasal 4(2) override) | 20% | 19% | 18% | same | same |
| Irrigation network construction, 42211 (same override) | 25% | 22.5% | 20% | same | same |

**Depreciation.** UU PPh Art 11(6) and (6a), restated in PMK 72 of 2023 Art 2, which revoked PMK 96/PMK.03/2009.

| Group | Life | Straight line | Declining balance | Official source | URL |
| --- | --- | --- | --- | --- | --- |
| I (includes office machines, laptops, computers, printers and scanners, Lampiran; check other assets there) | 4 years | 25% | 50% | PMK 72 of 2023 Art 2(3) | https://jdih.kemenkeu.go.id/api/download/46cededa-86ae-4cc9-93e5-b6bef8892074/2023pmkeuangan072.pdf |
| II | 8 years | 12.5% | 25% | same | same |
| III | 16 years | 6.25% | 12.5% | same | same |
| IV | 20 years | 5% | 10% | same | same |
| Building, permanent | 20 years | 5% | none | same | same |
| Building, non-permanent | 10 years | 10% | none | same | same |

**BPJS.** These are not income tax, and the payroll sibling owns them.

| Programme | Rate or amount | Official source | URL |
| --- | --- | --- | --- |
| Kesehatan PPU | 5% of wage: 4% employer, 1% participant in the 2020 text read. Applicability for 2026 is unverified: Needs Input until Perpres 14/2021 and 59/2024 are checked | Perpres 64/2020 Art 30(1), which also deleted Perpres 82/2018 Art 31 | https://jdih.kemenkeu.go.id/api/download/179608f7-a2a0-41c0-aaec-e7d60eb36054/64TAHUN2020PERPRES.pdf |
| Kesehatan wage cap | IDR 12,000,000 a month in the 2020 text read; applicability for 2026 is unverified and held on the same amendment checks | Perpres 64/2020, amending Perpres 82/2018 Art 32 | https://jdih.kemenkeu.go.id/api/download/179608f7-a2a0-41c0-aaec-e7d60eb36054/64TAHUN2020PERPRES.pdf |
| Kesehatan PBPU (self-employed), per person, per month | IDR 35,000 class III (the participant's share, with IDR 7,000 more from central and regional government), IDR 100,000 class II, IDR 150,000 class I in the 2020 text read. Applicability for 2026 is unverified and held on the same amendment checks | Perpres 64/2020 Art 34. Perpres 14/2021 revoked part of Perpres 64/2020, and that scope was not read | https://jdih.kemenkeu.go.id/api/download/179608f7-a2a0-41c0-aaec-e7d60eb36054/64TAHUN2020PERPRES.pdf |
| JKK | 0.24%, 0.54%, 0.89%, 1.27% or 1.74% by risk grade, employer. PP 6/2025 Art 11(5) recomposes 0.14% of each to JKP, leaving JKK at 0.10%, 0.40%, 0.75%, 1.13% or 1.60%. A 50% relief reached only listed labour-intensive industries with at least 50 active workers, for JKK contributions of February to July 2025. It ended, so it is not available for tax year 2026 on the text read | PP 7/2025 Arts 3, 4 and 10; PP 6/2025 Art 11(5) | https://jdih.kemenkeu.go.id/api/download/cdb7e0ef-fa1a-43f4-953e-792cecb57321/2025PP007.pdf |
| JKM | 0.20% for JKP members after 0.10% is recomposed to JKP. So 0.30% is derived (0.20% + 0.10%); the base rate and its payer are in PP 44/2015, not obtained. See the conflict in 'Not yet confirmed' | PP 49/2023 Art 18A, JDIH DJSN copy | https://jdih.djsn.go.id/assets/file/pp%20nomor%2049%20tahun%202023.pdf |
| JHT | unverified: the earlier version says 3.7% employer and 2% employee; PP 46/2015 not obtained | none | not obtained |
| JP | unverified: the earlier version says 2% employer, 1% employee and a wage cap of IDR 11,086,300 a month from March 2026 as reported; PP 45/2015 and any BPJS circular not obtained | none | not obtained |

### Enactment position

- **PP 20/2026 is enacted.** It is in LN 2026/43, in force 22 April 2026, and JDIH shows it in force. It amends Arts 56 to 59 of PP 55/2022 and inserts Art 20A, under which bribes and gratification, including those to foreign public officials, are not deductible. Its Penjelasan says the changes prevent avoidance using the final rate.
- **Art 59 is deleted, so the body has no year limit for an individual or a PT Perorangan.** The transitional rule, Art II(1)(a), speaks only of tax years 2025 and 2026 for filers whose old window ended in 2024 or 2025. It says nothing of 2027 for them. The reading that the body governs from 2027 is held.
- **Implementing rules.** Art II(1)(g) keeps existing rules in force unless inconsistent. PMK 164 of 2023 therefore survives only where consistent; its list of CV, firma and PT as eligible is overtaken. No implementing PMK was found.
- **DJP statements.** A DJP regional press note of 7 July 2026 was read. It is the lowest rung, and no figure here rests on it.

## The base

### Moving between regimes

The 3 regimes for an individual's business or professional income are not free choices. Each has entry conditions and each move has a date.

| Regime | Rung | Mechanics |
| --- | --- | --- |
| **UMKM Final 0.5%** | PP 55/2022 as amended by PP 20/2026 | 0.5% × gross monthly turnover; no expense deduction; final. It applies unless the taxpayer notifies DJP that it chooses the general rates |
| **Progressive with NPPN** (deemed net income) | UU PPh Art 14(2); PMK 81 of 2024 Art 450; PER-17/PJ/2015 | Deemed-profit % × gross revenue, less PTKP, then the Art 17 brackets. Individuals only, turnover less than IDR 4,800,000,000, notified in the first 3 months of the tax year |
| **Progressive with Pembukuan** | UU PPh Art 14; UU KUP Art 28; PMK 81 of 2024 Art 448 | Bookkeeping; Pasal 6 deductions and Pasal 9 add-backs; PTKP; Art 17 brackets. Required where the other 2 are closed |

| Move | Conditions | Deadline | Can it be undone? |
| --- | --- | --- | --- |
| Final to general rates, by choice | Written notice to DJP through the KPP, directly, by post or courier, or electronically (PMK 164 Art 5(1) to (3)) | End of the tax year; general rates apply from the next tax year (Art 5(4), (5)). A new registrant chooses at registration (Art 5(6)) | No. Art 57(3) and (4) of PP 55/2022 bar the final rate in the following tax years |
| Final to general rates, by turnover | Turnover goes over IDR 4,800,000,000 in the current tax year. The 0.5% continues to the end of that tax year (Art 61(1)) | Automatic | Art 61(2) applies Art 17 to the following tax years, and its Penjelasan says 'dan seterusnya'. Whether a later fall below the ceiling reopens Art 58(1) is not addressed; treat as Needs Input |
| Final to general rates, through a PT Perorangan | The Art 57(2)(e) total goes over IDR 4,800,000,000 in 1 tax year | From the next tax year | No, for that individual, those companies and any they found later (Art 57(4) and its Penjelasan) |
| General rates to NPPN | Individual; business or pekerjaan bebas income; turnover of every type and place in the previous tax year less than IDR 4,800,000,000, combined for a PH or MT couple (PMK 81 of 2024 Arts 450(1), 452) | Notify in the first 3 months of the tax year. A new registrant notifies within 3 months of registration or by the end of the tax year, whichever is first (PMK 81 Art 450(2), (3)) | No notice means pembukuan for that year (UU PPh Art 14(4); Art 450(4)) |
| NPPN to pembukuan | Open to an individual who keeps books. A taxpayer on the final rate moves only under the first 3 rows, so from the next tax year at the earliest (PMK 164 Art 5(5)), unless newly registered (Art 5(6)) | For the tax year concerned, by giving no NPPN notice for it. A later change of accounting method or book year needs DJP approval (UU KUP Art 28(6)) | Back to NPPN only through the row above |

After a move to general rates, PPh 25 instalments start in the first general-rate year, treated as for a new taxpayer unless UU PPh Art 25(7)(b) or (c) applies (PMK 164 Art 16). Run the comparison on projected revenue and margin as well as actuals: no text says the choice locks when payments begin, but the opt-out above is permanent.

### Who can use the 0.5% rate

**Income outside it, whatever the taxpayer's form (Art 56(3)):** (a) an individual's income from pekerjaan bebas services; (b) foreign income taxed abroad; (c) income under a separate final tax; (d) income that is not a tax object.

**Pekerjaan bebas (Art 56(4))** has these limbs, each in the text's words, including the text's own closing limbs:

- (a) tenaga ahli: pengacara, akuntan, arsitek, dokter, konsultan, notaris, PPAT, penilai, aktuaris, 'dan tenaga ahli sejenis lainnya'. The Penjelasan treats a tenaga ahli as an individual with special expertise who supplies services on that expertise, or professional services, and is not bound by employment.
- (b) pemain musik, pembawa acara, penyanyi, pelawak, bintang film, sinetron, iklan, sutradara, kru film, foto model, peragawan or peragawati, pemain drama, penari, pemahat, pelukis, pembuat or pencipta konten online (influencer, selebgram, bloger, vloger and the text's similar makers) and other artists.
- (c) olahragawan.
- (d) penasihat, pengajar, pelatih, penceramah, penyuluh, moderator and the text's similar persons.
- (e) pengarang, peneliti, penerjemah and the text's similar persons.
- (f) agen iklan. (g) pengawas or pengelola proyek. (h) perantara, including a finder. (i) petugas penjaja barang dagangan. (j) agen asuransi. (k) MLM or direct selling distributors and the text's similar persons.

The Penjelasan's test case: a piano teacher working alone supplies pekerjaan bebas; a piano course business employing others does not. A software developer is not listed by name, so the answer depends on the facts. A sole expert selling their own expertise points to tenaga ahli; an operation selling a product or using employees points away. It is Needs Input, never assumed either way.

**Who, and for how long.** The body text is Arts 57 to 59 as amended.

| Taxpayer | Final route | Time limit |
| --- | --- | --- |
| Individual | Yes, turnover not above IDR 4,800,000,000 (Art 57(1)(a)) and not within Art 57(2)(a) or (e) | None in the body, since Art 59 was deleted. Individuals whose old 7-year window ended in tax year 2024 may use tax years 2025 and 2026 (Art II(1)(a)(1)), and those whose window ended in 2025 may use 2026 (Art II(1)(a)(2)), if the criteria are met |
| PT Perorangan founded by 1 person | Yes, same ceiling (Art 57(1)(b)), unless Art 57(2)(a), (b) or (e) applies | None in the body. A window that ended in tax year 2025 gives tax year 2026 under Art II(1)(a)(2) |
| Koperasi | Yes, same ceiling (Art 57(1)(b)) | 4 tax years from the tax year of registration (Art 57(2)(f)). A koperasi registered before PP 20/2026 whose window ends in tax years 2024 to 2029 may use tax years 2025 to 2029 (Art II(1)(b)), and its Penjelasan runs Koperasi DEF to 2029 |
| CV, firma, ordinary PT, BUMDes or BUMDes bersama | No new entry: none is in Art 57(1). One with an unexpired window may continue if the criteria are met | Until the window under old Art 59 ends: 3 tax years for a PT, 4 for a CV, firma or BUMDes (Art II(1)(e)) |
| Individual or PT Perorangan within Art 57(2)(b) or (e) that was on the final rate under the old rules | Yes, for now | Until the end of tax year 2026 (Art II(1)(f)) |
| PT Perorangan founded by an individual with special skills, supplying services similar to pekerjaan bebas | No (Art 57(2)(b)), and the Penjelasan's tax consultant company is outside | The row above applies to one already on the final rate. Otherwise none |
| Body with an Art 31A facility, a PP 94/2010 facility or its successor, or a PP 40/2021 Art 75 or 78 facility | No (Art 57(2)(c)) | None |
| BUT | No (Art 57(2)(d)) | None |

**The turnover test (Art 58).**

- Measure the last tax year before the year concerned. Count all turnover from business and pekerjaan bebas, final or non-final, domestic or foreign (Art 58(1)(a)). That includes rental and insurance agent turnover (Penjelasan examples). Employment income is not business or pekerjaan bebas turnover, so it is not in the count.
- Turnover is money or money's worth before sales discounts, cash discounts and the text's own 'potongan sejenis' limb (Art 58(1)(b)).
- **PH or MT couple:** combine husband's and wife's turnover (Art 58(2)). A minor child's turnover is included (Penjelasan to Art 58(2), which cites the income tax rules).
- **With a PT Perorangan:** for Art 57(2)(e), the individual and every PT Perorangan they founded count together. For a PH or MT couple, the husband, the wife and every PT Perorangan founded by either count together (Art 58(3)).
- A KK couple is one taxpayer under UU PPh Art 8(1), subject to the wife's sole-employer exception, so the combination follows from that. An HB couple is outside Art 58(2) and (3), which are limited to couples under UU PPh Art 8(2)(b) and (c).
- A company's turnover counts here only through the PT Perorangan limb. An ordinary PT that the client owns is not named. It remains exposed to R-6.

**Art 60 mechanics.** Tax = 0.5% × monthly turnover after the band, for all places of business. For an individual the band is used cumulatively from January, so with R = IDR 800,000,000 the tax is 0.5% × 300,000,000 = IDR 1,500,000. If a buyer appointed as withholder pays, it withholds 0.5% on a copy of the Surat Keterangan (PMK 164 Art 8; PP 55/2022 Arts 62 and 63). Art II(1)(c) and (d) continue existing letters.

**Break-even between final and general rates.** Let R = gross revenue, n = NPPN %, P = PTKP, T(·) = the Art 17 brackets, m = actual margin.

- PPh UMKM = 0.5% × max(R − 500,000,000, 0), for an individual.
- PPh NPPN = T(1,000 × floor(max(n × R − P, 0) / 1,000)).
- PPh pembukuan = T(1,000 × floor(max(m × R − P, 0) / 1,000)).

These are income tax only, for one person, with no other income. The NPPN and pembukuan formulas round positive PKP down to full IDR 1,000 under Art 17(4) before applying the brackets. Compare the resulting tax amounts: UMKM is lower only when its computed amount is strictly below the other amount, and equal amounts tie.

At n = 50% and TK/0, both NPPN and UMKM give nil at or below R = IDR 108,000,000; the PKP rounding can extend the nil result just above that revenue. With the same P and ignoring loss carry-forward, NPPN costs no more than pembukuan when m > n, and pembukuan costs no more than NPPN when m < n. They tie when both rounded taxable bases are zero and can also tie at positive bases because of rounding. Use the calculated taxes to establish any strict saving. The following margins approximate the continuous equality before the PKP rounding:

| Revenue (IDR) | Approximate equality margin, TK/0 |
| --- | --- |
| 300,000,000 | 18.00% |
| 500,000,000 | 10.80% |
| 800,000,000 | 10.50% |
| 1,200,000,000 | 9.78% |
| 2,500,000,000 | 6.43% |
| 4,800,000,000 | 4.94% |

The earlier version's single figure of about 12% describes only a revenue near IDR 450,000,000. For revenue at or below IDR 500,000,000, UMKM tax is zero: pembukuan ties it at every margin at or below P / R and can also tie just above that margin because of PKP rounding. Thus all margins up to 18.00% at IDR 300,000,000 and up to 10.80% at IDR 500,000,000 tie; pembukuan cannot cost less than zero. For revenue above IDR 500,000,000, the table is a starting estimate only. Compare both calculated tax amounts after the statutory PKP rounding: choose a lower amount only where there is a strict difference, otherwise record a tie.

### NPPN

Use is limited to the conditions in 'Moving between regimes'. The Lampiran I rate is the income measure, so expenses are not deducted and no loss arises. It is calculated separately for each business type (PER-17/PJ/2015 Art 5(1)). A taxpayer on NPPN keeps pencatatan, not books (UU PPh Art 14(3); PMK 81 Art 448(2)). A notice is deemed accepted unless an audit shows otherwise (PER-17 Art 2(2)). Exactly IDR 4,800,000,000 passes the final test but fails NPPN, because 'kurang dari' means less than. An individual whose whole turnover is final or non-object income, and not above IDR 4,800,000,000, may keep pencatatan with no NPPN notice (PMK 81 Art 451). What to record is in Art 453. Whether NPPN income is measured on receipts or on accrual is held.

### Pembukuan

It can beat UMKM or NPPN when:

- Actual margin is below the NPPN deemed margin (against NPPN) and below the tie margin above (against UMKM).
- Operating losses are expected: only pembukuan gives a loss, carried up to 5 years (UU PPh Art 6(2)).
- Capital spending is heavy: only pembukuan gives depreciation (Art 11).
- Foreign tax credits are wanted: foreign income taxed abroad is outside the final rate (PP 55/2022 Art 56(3)(b)), and Art 24 credit rules belong to id-income-tax.

Mixed business and pekerjaan bebas income does not by itself require it: NPPN is calculated separately by type.

### Entity choice: OP, PT Perorangan or PT

| Factor | OP | PT Perorangan | PT |
| --- | --- | --- | --- |
| Legislation | UU PPh; no separate entity law | UU 40/2007 Arts 153A to 153J, inserted by UU 6/2023 Art 109; PP 8/2021 | UU 40/2007 as amended by UU 6/2023 |
| Who may use it | Anyone | Micro or small business (PP 7/2021 Art 35: modal usaha up to IDR 5,000,000,000 excluding land and buildings at founding or registration; annual sales up to IDR 15,000,000,000 for support measures). 1 founder who is an Indonesian citizen aged 17 or over with capacity (PP 8/2021 Art 6). 1 such company in 1 year (Art 153E(2)). Must convert to an ordinary PT when no longer micro or small (Art 153H) | Generally 2 or more founders (UU 40/2007 Art 7) |
| Liability | Unlimited personal liability | Limited (Art 153J(1)), but not where (a) legal entity requirements are unmet, (b) the shareholder in bad faith uses the company for personal interests, (c) the shareholder joins its unlawful act, or (d) the shareholder unlawfully uses its assets so that it cannot pay its debts (Art 153J(2)) | Limited, under the general rules |
| Income tax | Personal PPh, as above | 22% with Art 31E, or UMKM Final 0.5% if eligible, with no band | 22% with Art 31E; UMKM Final only during a remaining old window |
| Setup cost | unverified: the earlier version says about IDR 0 | unverified: the earlier version says about IDR 50,000 on AHU online; UU 40/2007 Art 153I gives fee relief and the fee itself was not read | unverified: the earlier version says IDR 5,000,000 to 15,000,000 for notary, OSS and NIB |
| Minimum capital | None | Set by the founder's decision; at least 25% of authorised capital issued and paid in, with proof, within 60 days (PP 8/2021 Arts 3 and 4); sector minimums apply (Art 5) | Same PP |
| Audit | No company duty | Financial report under Art 153F. How Art 68 applies is held | UU 40/2007 Art 68(1): (a) collects or manages public funds; (b) issues debt to the public; (c) public company; (d) persero; (e) assets and/or turnover of at least IDR 50,000,000,000; (f) another law requires it |
| Monthly instalment | PPh 25 applies under UU PPh Art 25 unless final; 0.75% OPPT rate for an individual trader or service provider with a separate place of business, not pekerjaan bebas (PMK 81 Arts 1(63), 234); final payers pay monthly under PMK 164 Art 7 | Same base, or final monthly | Same base, or final monthly |
| Annual filing | SPT Tahunan individual within 3 months | SPT Tahunan body within 4 months | Same |
| Dividend tax on extraction | None | 10% final, or exempt if invested as the conditions below require | Same |
| Salary to owner | None: an OP cannot pay itself (Art 9(1)(i)) | Deductible under Art 6(1)(a) if for work done; excess over a reasonable amount through a special relationship is not (Art 9(1)(f)); PPh 21 on the owner | Same |
| Substance risk | Low | Medium: DJP may test a paper PT | Lower, on real operations |

**Decision heuristic, each line subject to the conditions above:**

- Revenue below IDR 500,000,000, low expenses, not pekerjaan bebas: OP with UMKM Final, with no tax under the individual band.
- Revenue IDR 500,000,000 to IDR 2,500,000,000, profitable, not pekerjaan bebas: OP with UMKM Final while the Art 58 total stays within IDR 4,800,000,000.
- Revenue IDR 2,500,000,000 to IDR 4,800,000,000, liability protection wanted: PT Perorangan with UMKM Final, if Art 57(2)(b) does not apply. There is no band, and Art 57(2)(e) counts the founder and every such company together. It moves to corporate rates once the ceiling is passed.
- Revenue above IDR 4,800,000,000 sustained: PT (or PT Perorangan if eligible), pembukuan, 22% with Art 31E. Plan dividends under the investment conditions below.

**Corporate tax with Art 31E.** On taxable income from the part of turnover up to IDR 4,800,000,000 the rate is 22% × 50% = 11%; the rest is at 22%. Art 31E(2) lets the turnover limit change. The split of taxable income by turnover share comes from Art 31E's wording; its Penjelasan example was not read, so check the sibling id-corporate-tax before quoting a figure.

### Dividends and the investment exemption

- A domestic dividend to a **resident individual** is exempt only if invested in Indonesia within the set period (UU PPh Art 4(3)(f)(1)(a); PP 55/2022 Arts 9 to 11). A domestic dividend to a **resident body** is exempt with no investment condition (Art 4(3)(f)(1)(b)).
- **Period:** invest by the end of the 3rd month after the tax year of receipt, and hold for at least 3 tax years from that tax year (PP 55/2022 Art 11).
- **Forms in the financial market (Art 10(2) and (3)):** debt securities, sukuk, shares, mutual fund units, asset-backed securities, DIRE units, deposits, savings, giro, futures traded on an Indonesian exchange, and other financial market instruments with OJK approval, including investment-linked insurance, finance company, pension fund and venture capital products.
- **Forms outside it (Art 10(2) and (4)):** infrastructure under KPBU; priority real sector, meaning sectors in the national medium-term development plan (Art 10(6)); property, excluding government-subsidised property (Art 10(7)); direct investment in a company in Indonesia; gold bars or ingots of 99.99% purity, produced in Indonesia and accredited and certified by BSN and/or LBMA (Art 10(8), (9)); cooperation with LPI; loans to micro and small business in Indonesia; and other lawful forms. Priority real sector and direct investment go by capital participation in a PT (Art 10(5)).
- **Transfer:** an investment may move only to another form in Art 10(2) (Art 10(10)).
- **Partial investment:** the invested part is exempt and the remainder taxed (PMK 18/PMK.03/2021 Arts 15 and 16, read for this point).
- **Evidence:** a realisation report on the Portal Wajib Pajak (PMK 81 Arts 370, 374). No text read asks for a 'commitment letter'.
- **Failure:** tax is due when the dividend was received, self-paid by the 15th of the month after that Masa Pajak, reported on SPT Masa Unifikasi, with KUP sanctions (PMK 81 Arts 372, 373).
- Combined rate if not invested: 22% + 10% × 78% = 29.8%. Investment takes it to 22%, a saving of 7.8 points, while the money stays invested. Listed-share dividends follow the same rule for a resident individual; no separate rule was read.

### PTKP planning

PTKP matters only under NPPN or pembukuan. It does nothing under UMKM Final.

**Status follows facts at the start of the tax year**, or the start of a part year (UU PPh Art 7(2)). Marriage or a new dependant counts from the next tax year if it occurs after 1 January. Report the status and dependants in the SPT Tahunan (PER-11/PJ/2025 annex). A failure to enter them does not change the law, so correct the return.

**Dependants (Art 7(1)(d)):** each family member by blood or by marriage in the straight line, and an adopted child, who is wholly maintained, up to 3 per family, each IDR 4,500,000. Parents, parents-in-law, children and stepchildren can count. Siblings are lateral, not straight line, and never count, whoever maintains them. Art 7(3) lets a PMK adjust the amounts, and PMK 101/PMK.010/2016 is that PMK. The limit of 3 is in Art 7(1)(d), not Art 7(3).

**Marital assessment (UU PPh Art 8):**

| Status | NPWP arrangement | Tax | When to use |
| --- | --- | --- | --- |
| **KK, joint (Kepala Keluarga)** | One taxpayer | The wife's income is treated as the husband's, except income solely from 1 employer with Art 21 withheld and unconnected with the husband's or family's business (Art 8(1)). PTKP is K/n, or K/I/n only if her income is combined | The default where (2) does not apply |
| **HB (Hidup Berpisah)** | Own | Lived apart by a judge's decision (Art 8(2)(a)). Tax separately | Fact, not a choice. The PTKP code for each is left to id-income-tax |
| **PH (Pisah Harta)** | Own NPWP each, with a written agreement separating assets and income (Art 8(2)(b)). 'Notarised' is not in the Act | Net incomes combined, tax split by share of **net** income (Art 8(3)) | Both have real income and assets |
| **MT (Memilih Terpisah)** | Own NPWP each; the wife chooses to run her own rights and duties (Art 8(2)(c)) | Same as PH | A simpler compromise |

Income taxed as PPh Final is settled at source or by final payment and stays out of the joint progressive calculation, since Art 4(2) taxes it separately. Its turnover still counts in the Art 58 test. A minor child's income is combined with the parents' (Art 8(4)).

### Deductible expenses, Pasal 6

These matter only under pembukuan. Under NPPN the deemed % stands in for expenses, and under UMKM Final they do not count. Each row is UU PPh Art 6(1) as amended.

| Category | Reference | Planning note and condition |
| --- | --- | --- |
| Costs of obtaining, collecting and maintaining income | Art 6(1)(a) | The general rule, which needs a direct link. It includes wages, insurance premiums and taxes except PPh. Employer premiums for staff are deductible and are income to the employee |
| Depreciation and amortisation | Art 6(1)(b); Arts 11, 11A | See 'Depreciation' |
| Contributions to a pension fund approved by the OJK | Art 6(1)(c) | The earlier version said DJP-approved; the Act says OJK. Limits on employer and employee amounts are held |
| Realised losses on disposal of property used in the business | Art 6(1)(d) | Timing a real disposal is fine |
| FX losses | Art 6(1)(e) | The rules for unrealised FX are held |
| R&D in Indonesia | Art 6(1)(f) | 100% of the cost. **Super deduction up to 300%** is for a domestic **body** only: PP 45/2019 Art 29C; PMK 81 of 2024 Art 432 (100% plus up to 200%: 50% for an Indonesian patent or plant variety registration, 25% for a foreign registration as well, 100% for commercialisation, 25% for collaboration). PMK 81 revoked PMK 153/PMK.010/2020. An individual on pembukuan does not get it. To earn the extra, work must seek a new discovery, rest on an original concept, have an uncertain result, be planned and budgeted, aim at something transferable or tradable, and fit a priority theme (Art 434(1)). Art 434(2) excludes 9 activities, including routine quality control and market research. Arts 435 to 447 hold further conditions, not read in detail |
| Scholarships, apprenticeships and training | Art 6(1)(g) | **Super deduction up to 200%** is for a domestic **body** only: PP 45/2019 Art 29B; PMK 128/PMK.010/2019 Art 2 (100% plus up to 100%). Conditions: competency-based activity, a cooperation agreement, no fiscal loss in the year of use, and a Surat Keterangan Fiskal. No 'priority sector' or 'ruling' wording was read |
| Bad debts written off | Art 6(1)(h) | All of: (1) charged to profit and loss; (2) a list given to DJP; (3) filed with a court or the government debt agency, or a written agreement, or published, or the debtor's acknowledgement. Limb (3) does not apply to small debtors. The PMK 207/2015 notification cited in the earlier version was not obtained: held |
| Donations | Art 6(1)(i) to (m); PP 93/2010 | National disaster relief, R&D, social infrastructure, education facilities and sports development. Up to 5% of prior-year fiscal net income (Art 3). Conditions: prior-year fiscal income, no loss caused, valid proof, a recipient with an NPWP unless it is a body excluded as a tax subject (Art 2), and not to a special-relationship party (Art 4). 'DJP-approved channels' is not the test |

### Non-deductibles, Pasal 9

Each row is UU PPh Art 9(1), unless stated.

| Item | Reference | Note |
| --- | --- | --- |
| Profit distributions in any name or form, including dividends, policyholder dividends from an insurer and cooperative surplus distributions | (a) | The investment exemption above concerns the recipient's income; it does not make the payer's distribution deductible |
| Personal costs of shareholders, partners or members | (b) | These costs are not deductible |
| Reserves and provisions, except the specified reserve categories: credit losses of banks, other credit distributors, finance leases, consumer finance and factoring businesses; insurance including BPJS social assistance; LPS guarantees; mine reclamation; forestry replanting; and closure and maintenance of industrial waste disposal sites | (c) | The credit-loss category uses the applicable accounting standards with limits after coordination with OJK. All exceptions must meet their requirements. No general bad-debt provision: eligibility, limits and implementing conditions are Needs Input unless evidenced |
| Insurance premiums paid by an individual on life, health, accident, endowment or scholarships | (d) | Exception: employer pays and treats the premium as employee income |
| Excess paid to a shareholder or related party for work | (f) | Arm's length test |
| Gifted property, aid, donations and inheritances within Art 4(3)(a) and (b), except Art 6(1)(i) to (m), zakat received by a collecting body formed or approved by the government, and compulsory religious contributions received by a religious body formed or approved by the government, on the implementing regulation's terms | (g) | Segregate clearly |
| PPh | (h) | Other taxes fall under Art 6(1)(a)(9). PBB fits that wording, and PB1 was not specifically read |
| Personal costs of the taxpayer or dependants | (i) | Includes an OP's pay to himself. The earlier version cited (j) |
| Salary to partners in a partnership, firma or CV with capital not divided into shares | (j) | Family pay may be deductible only for real work. It is related under Art 18(4) and tested under Art 9(1)(f). Pay to a wife in the husband's business is combined under Art 8(1), and pay to a minor child under Art 8(4), so the saving may be nil |
| Tax sanctions | (k) | Interest, fines and surcharges |
| Spending with benefit over more than 1 year | Art 9(2) | Capitalise it. The earlier version cited Art 11(8), which covers disposals |
| Bribes and gratification | PP 55/2022 Art 20A | Includes payments to foreign public officials |
| Entertainment without a Daftar Nominatif | PER-11/PJ/2025 Lampiran 3D, Bagian A | Entertainment, representation and hospitality are listed there under Art 6(1)(a). SE-27/PJ.22/1986, which the earlier version cited, was not obtained; its fields and its consequence are held. Prepare the list before claiming the cost |

### Depreciation

Tangible non-building assets may use straight line or declining balance, applied consistently ('taat asas'; Art 11(2); PMK 72 of 2023 Art 2(2)). Buildings use straight line only. Declining balance front-loads deductions.

Start is the month of **expenditure**, or the month of completion for an asset in progress (Art 11(3); PMK 72 Art 5(1)). With DJP approval the start can be the month of use or the month income begins (Art 11(4); Art 5). The earlier version's 'month of first business use' applies only with that approval. A permanent building's useful life may exceed the 20 years if that is its actual life (Art 11(6a)).

### PPh Final Pasal 4(2)

UU PPh Art 4(2) is the root for these. They apply by the nature of the income, not by election, and sit outside the progressive calculation.

**Rental (PP 34/2017).** Lodging services (rooms, dormitories, worker lodging, boarding houses) are outside it (Art 2(3)). Tax is withheld by a tenant appointed to withhold, otherwise self-paid (Art 3).

| Strategy | Detail |
| --- | --- |
| Gross-up clause in lease | State who bears the 10%, to avoid disputes |
| Service charges v rent | Art 4(2) counts maintenance, security, service and other facility charges related to the land or building **whether the contract is separate or joined**. Splitting the contract saves nothing, and the earlier version was wrong to suggest otherwise |
| Furnished rental | Whether a separate furniture hire falls outside 'other facility charges' is held. Do not plan on it |
| Sub-leasing | Art 2(1) reaches a person or body that earns rent. No sublease limb was read, so check who the landlord is. The 10% applies to gross, so rent paid out gives no relief in a final computation |

**Construction (PP 9/2022).** A valid SBU or, for an individual, SKK saves 1.35 to 2.5 points on every invoice (4% less 2.65% and 1.75%; 6% less 3.5%). Having none does not remove the duty (Art 3(1a)). The Penjelasan to Art 3(1) names the SBU issuers: a certification body formed by an accredited association and recorded by LPJK, a certification body accredited by the energy minister, or that minister. Art 10D requires an evaluation after 3 tax years, on which construction income may move to the general Art 17 rates; no result was read. The final rate on these services puts them outside the 0.5% route (PP 55/2022 Art 56(3)(c)).

**Others.** Bank interest, bond interest and land or building transfers are in the rates table. Applicability of the bank-interest rate and exclusions for 2026 is unverified until PP 123/2015 is checked: Needs Input. In the unamended 2000 text, PP 131/2000 Art 3(1) takes these out of withholding: (a) deposits and savings up to IDR 7,500,000 not split up; (b) interest to banks; (c) interest to an approved pension fund on its permitted sources; (d) savings at an appointed bank for low-cost housing. PP 34/2016 Art 6 takes these out of payment: (a) an individual below PTKP transferring under IDR 60,000,000, not split up; (b) an individual's gift to a straight line relative one degree, a religious, education or social body, a koperasi or a micro or small business person; (c) a body's gift to the same, other than a relative, in (b) and (c) with no business, work, ownership or control link and on PMK terms; (d) inheritance; (e) a body's merger or split at book value set by the Minister; (f) a building transfer under a build-operate-transfer, build-transfer-operate or state asset use agreement; and (g) a person outside the tax subject. Bond interest exclusions were not read. Lottery and IDX figures are held.

### BPJS

**Kesehatan.** In the text read, wage for the 5% is basic wage plus fixed allowances paid without regard to attendance (Perpres 82/2018 Art 33(3), (4)), with an IDR 12,000,000 monthly cap in Perpres 64/2020. These describe the texts read: applicability for 2026 is unverified until Perpres 14/2021 and 59/2024 are checked. Keep the rate, base, cap and PBPU amounts as Needs Input for a 2026 computation. Planning on the base must rest on a real pay structure, and the earlier version's bonus line is held.

**Ketenagakerjaan.** PP 6/2025 Art 11 funds JKP at 0.36%: 0.22% from the government and 0.14% from JKK recomposition. The earlier version's plan to set a founder's fixed wage just above the JP cap depends on the JP cap, which is held, and on Art 9(1)(f). A self-employed OP without staff usually pays only Kesehatan PBPU. Whether the OP has any Ketenagakerjaan duty is held.

| Payer | Income tax treatment |
| --- | --- |
| Employer PT, employer parts | Deductible under Art 6(1)(a) as wage cost and premiums, with the Penjelasan. The earlier version cited Art 6(1)(c), which is for OJK-approved pension funds. Employer-paid JKK, JKM and health premiums are employee income (PMK 168 of 2023 Art 5). Employer-paid pension and old-age contributions to the bodies Art 7 names are not (PMK 168 Art 7). The deduction route for JHT and JP is held |
| Employee parts in payroll | For a permanent employee the PPh 21 deductions are biaya jabatan, employee-paid contributions for pension and old-age programmes, and zakat or compulsory religious contributions paid through the employer (PMK 168 of 2023 Art 10(1)). The employee health contribution is not in that list; the 1% figure describes the 2020 text read and remains Needs Input for 2026 on the amendment checks above |
| OP self, PBPU | Needs Input if claimed. It is treated like Art 9(1)(d) or (i), and no text read gives a deduction |

### Year-end timing

UU KUP Art 28(5) requires books kept consistently on the accrual **or cash** basis. A change needs DJP approval (Art 28(6)). The earlier version said cash was generally not permitted, which is not the text. UMKM Final is monthly on gross turnover. Timing for advances under the final rate is held.

**Income deferral, on the accrual basis.**

| Technique | Condition |
| --- | --- |
| Genuine January completion | Under the accrual basis, use January only if performance actually completes in January. Invoicing in January does not defer income from December performance or delivery |
| Stage-based recognition | Plan project milestones around year-end only if contract terms genuinely allow. The earlier version's PSAK 72 label is held |
| Advance receipts | Deposits for future work are liabilities until performance, on accrual only. A cash-basis taxpayer has income on receipt |
| Year-end rebate or discount accruals | Must be contractual; conditional discounts only when conditions are met |

**Expense acceleration, on the accrual basis.**

| Technique | Condition |
| --- | --- |
| Prepay annual contracts in December | Only the part for the current year is a cost. Benefit over more than 1 year is spread (Art 9(2)) |
| Year-end bonus accrual | Declared and committed before year-end. PPh 21 timing belongs to id-payroll-pph21 |
| Asset purchase before year-end | The start month is the month of expenditure, so December gives 1 month |
| Bad debt write-off | All Art 6(1)(h) conditions above |
| R&D or training spend | Super deductions for domestic bodies only, on their conditions |

**Regime dates.** See 'Moving between regimes'. UMKM Final is not elected at the start of a year: it applies unless opted out. Only the NPPN notice falls in January to March.

### PPN and the regimes

The final rate does not switch off PPN. Report as a PKP when turnover goes over the small business limit, by the end of the book year in which it was exceeded (PMK 164 Art 17(3)). PMK 164 Art 24(a) revoked the older end-of-next-month rule. PPN duties and rights start in the first Masa Pajak of the next book year (Art 18). On a late report or ex officio confirmation (Art 17(7)), they start from the Masa Pajak of confirmation, and PPN that should have been collected from the next book year goes on SPT Masa PPN (Art 19). Early PKP status is possible (Art 20). Exports are 0% (UU PPN Art 7(2)). A comparison between regimes needs a separate PPN line if the client is near the limit.

### Defaults

A default stands only where the law fixes the result. Everything else is Needs Input.

| Scenario | Treatment |
| --- | --- |
| UMKM time limit uncertain | An individual has no limit in the body. For a koperasi, CV, firma or PT, Needs Input: ask the tax year of registration. Do not treat the window as expired without it |
| Continuing on the final rate when not eligible | Tax is recalculated at general rates with KUP Arts 13 and 15 consequences. Rate as in 'Penalties and interest' |
| NPPN % uncertain | Needs Input: the KLU decides it. Show candidate KLUs only labelled as candidates |
| Mixed business and employment income | Employment is taxed at the general rates, and the 0.5% only on qualifying business income. The law fixes this |
| Dependants not shown on the return | PTKP follows the facts at the start of the year. Unknown facts are Needs Input |
| Spouse's business income with no PH agreement | Needs Input until MT and HB are excluded. Then Art 8(1) joint treatment is fixed by law, subject to its exception |
| Asset purchase | Capitalise if the benefit runs over more than 1 year (Art 9(2)) |
| Entertainment without Daftar Nominatif | Do not claim it. The effect of a missing list rests on an unread circular |
| R&D super deduction without proof of the conditions | Body: 100% under Art 6(1)(f) until the PMK 81 conditions are shown. Individual: 100% only |
| Dividend investment exemption | Apply only if the investment and report conditions are met. Otherwise Needs Input, then 10% if they fail |
| OP self BPJS contributions | Needs Input. No deduction claimed without a text |
| Mixed rental contract | 10% on the full amount related to the land or building (PP 34/2017 Art 4(2)) |

## Deadlines and filing

File on the Portal Wajib Pajak (Coretax DJP). PER-11/PJ/2025 Arts 83 and 84 set single SPT Tahunan forms for individuals and bodies, with lampiran. Art 143 treats documents for tax year 2025 made through the portal as compliant. PER-11/PJ/2025 and its annex do not name the 1770, 1770S, 1770SS or 1771 forms of the earlier version, so that those forms no longer apply is an inference.

| Date | Step | Basis |
| --- | --- | --- |
| 15th of the next month | Deposit UMKM final tax for each place of business, and Art 4(2), 15, 21, 22, 23, 25 and 26 tax | PMK 164 Art 7(2); PMK 81 Art 94(2) |
| 20 days after the month end | SPT Masa Unifikasi for final tax, unless there is no income, only withheld transactions, or the band is not used up (Art 7(4)); a validated NTPN is deemed filing (Art 7(5)) | PMK 164 Art 7(3) to (5) |
| End of the next month | PPN deposit | PMK 81 Art 94(3)(e) |
| First 3 months of the tax year | NPPN notice; a new registrant has 3 months from registration or to the end of the tax year, whichever is first | UU PPh Art 14(2); PMK 81 Art 450 |
| 31 March for a calendar year | SPT Tahunan, individual: 3 months after the end of the tax year | UU KUP Art 3(3); PMK 81 Art 169(1) |
| 30 April for a calendar year | SPT Tahunan, body: 4 months after the end of the tax year | UU KUP Art 3(3); PMK 81 Art 169(2) |
| End of the 3rd month after the tax year of receipt | Invest a dividend; realisation report each year to the third year | PP 55/2022 Art 11; PMK 81 Art 374 |
| 31 December | Final opt-out notice | PMK 164 Art 5(4) |
| End of the book year in which the limit is exceeded | PKP report | PMK 164 Art 17(3) |
| 1 January | PTKP status fixed | UU PPh Art 7(2) |

Form 1721 and 1721-A1 are named in the earlier version. PMK 168 of 2023 Art 20(5) leaves the form to DJP, and the current name belongs to id-payroll-pph21. A separate 'SPT Masa PPh 25' form was not confirmed.

## Penalties and interest

All are UU KUP as amended by UU 7/2021 and UU 6/2023 Art 113, unless stated. They reach duties under the tax laws by the KUP's own terms; PMK 81 Art 373(4) applies KUP sanctions to a failed dividend investment. They are not a general sanction for a breach of the company or BPJS laws.

| Failure | Consequence | Basis |
| --- | --- | --- |
| Late SPT | IDR 500,000 SPT Masa PPN; IDR 100,000 other SPT Masa; IDR 1,000,000 SPT Tahunan body; IDR 100,000 SPT Tahunan individual | Art 7(1) |
| Late payment | Monthly interest at the Minister's rate (reference rate plus 5%, divided by 12), up to 24 months; a part month counts as full | Art 9(2a) to (2c) |
| Underpayment found on assessment (SKPKB, within 5 years) | Tax plus interest at reference plus 15%, divided by 12, up to 24 months | Art 13(1), (2), (2b) |
| No SPT after warning, or certain other cases | Interest at reference plus 20%, divided by 12, up to 24 months; 75% on PPN and on withheld tax not deposited | Art 13(3), (3b), (3c) |
| New data after assessment (SKPKBT) | Surcharge of 100% of the extra tax, unless the SKPKBT is issued on the taxpayer's own written statement before the audit for it starts | Art 15(2), (3) |
| Assessment not paid by its due date | Interest at the reference rate divided by 12, up to 24 months; a part month counts as full | Art 19(1), (4) |
| No books or records | Net income set by norm and other methods | UU PPh Art 14(5) |
| Records | Keep for 10 years, in Indonesia | UU KUP Art 28(11) |

The monthly rates themselves are published in KMK and were not read, so no number is given. The earlier version's '2%/month per Pasal 19 KUP' is not the current law.

**Anti-avoidance.** UU PPh Art 18(3) lets DJP redetermine income between related parties, and Art 18(4) defines the relationship: 25% capital, direct or indirect; control; family by blood or marriage in the straight line and/or sideways 1 degree. PP 55/2022 Art 32(1) lets the Minister prevent avoidance, Art 32(2) lists limbs (a) to (h) (CFC dividends; arm's length redetermination and debt as capital; SPV purchases; conduit share sales; employee income diverted; comparison with similar taxpayers after 5 years of commercial selling and 3 years of losses; borrowing cost limits; hybrid mismatches), Art 32(3) limits (a) to (f) to special relationships, and Art 32(4) lets DJP redetermine on substance over form. UU KUP Art 28 is a bookkeeping rule, not an anti-avoidance rule, and no Pasal 28A exists in the texts read (UU 28/2007, UU 7/2021 and UU 6/2023).

## Cross-border points

- This guide is for residents. A treaty or conduit question is refusal R-1, and PER-25/PJ/2018 (beneficial owner) was not obtained.
- Foreign turnover counts toward the Art 58 test (Art 58(1)(a)), but foreign income taxed abroad is outside the 0.5% rate (Art 56(3)(b)).
- The Art 24 credit belongs to id-income-tax.
- Exports are 0% PPN, and the export definition belongs to indonesia-vat.
- CFC and transfer pricing are refusals R-2 and R-3.

## Two worked examples that recompute

Each result is income tax only, with no BPJS or PPN, unless the example says so. Every example is conditional on its stated facts.

### Example 1: Software developer, three routes

Single OP, TK/0, Jakarta. Gross revenue IDR 1,200,000,000. Genuine expenses IDR 200,000,000, so actual margin is about 83%. KLU 62010, Group 1, NPPN 50%. Turnover last year was within the ceiling, and the NPPN notice is in time. No spouse, no PT Perorangan.

```oa-check
name: id-opt-developer
inputs:
  revenue: 1200000000
  expenses: 200000000
  nppn_pct: 0.50
  ptkp: 54000000
steps:
  - option_a: 0.005 * max(revenue - 500000000, 0)
  - pkp_b: floor(max(nppn_pct * revenue - ptkp, 0) / 1000) * 1000
  - option_b: 0.05 * min(pkp_b, 60000000) + 0.15 * max(min(pkp_b, 250000000) - 60000000, 0) + 0.25 * max(min(pkp_b, 500000000) - 250000000, 0) + 0.30 * max(min(pkp_b, 5000000000) - 500000000, 0) + 0.35 * max(pkp_b - 5000000000, 0)
  - pkp_c: floor(max(revenue - expenses - ptkp, 0) / 1000) * 1000
  - option_c: 0.05 * min(pkp_c, 60000000) + 0.15 * max(min(pkp_c, 250000000) - 60000000, 0) + 0.25 * max(min(pkp_c, 500000000) - 250000000, 0) + 0.30 * max(min(pkp_c, 5000000000) - 500000000, 0) + 0.35 * max(pkp_c - 5000000000, 0)
  - pct_a: round(100 * option_a / revenue, 2)
  - pct_b: round(100 * option_b / revenue, 2)
  - pct_c: round(100 * option_c / revenue, 2)
expected:
  option_a: 3500000.00
  pkp_b: 546000000.00
  option_b: 107800000.00
  pkp_c: 946000000.00
  option_c: 227800000.00
  pct_a: 0.29
  pct_b: 8.98
  pct_c: 18.98
```

| Regime | PPh (IDR) | Effective rate on revenue |
| --- | --- | --- |
| UMKM Final 0.5% | 3,500,000 | 0.29% |
| Progressive with NPPN | 107,800,000 | 8.98% |
| Progressive with pembukuan | 227,800,000 | 18.98% |

The result turns on one fact. **Case 1, the work is not pekerjaan bebas:** Option A is open and is IDR 104,300,000 below Option B. **Case 2, the developer is a tenaga ahli under Art 56(4)(a):** Option A does not exist, the income is outside the final rate, and the choice is B or C, with B lower by IDR 120,000,000 because actual margin is above 50%. If that fact is unknown, the answer is Needs Input, not Option A.

### Example 2: Which should I choose, final or pembukuan? Low-margin trader

Single OP, TK/0, not pekerjaan bebas, revenue IDR 1,200,000,000. Estimate the continuous equality margin using the 15% band, then compare the actual tax after statutory PKP flooring. The approximation alone does not decide the regime.

```oa-check
name: id-opt-tie-margin
inputs:
  revenue: 1200000000
  ptkp: 54000000
  margin_a: 0.097778
  margin_b: 0.09779
  margin_c: 0.0978
steps:
  - final_tax: 0.005 * max(revenue - 500000000, 0)
  - pkp_tie: 60000000 + (final_tax - 3000000) / 0.15
  - net_tie: pkp_tie + ptkp
  - tie_pct: round(100 * net_tie / revenue, 2)
  - pkp_a: 1000 * floor(max(revenue * margin_a - ptkp, 0) / 1000)
  - pkp_b: 1000 * floor(max(revenue * margin_b - ptkp, 0) / 1000)
  - pkp_c: 1000 * floor(max(revenue * margin_c - ptkp, 0) / 1000)
  - tax_a: 3000000 + (pkp_a - 60000000) * 0.15
  - tax_b: 3000000 + (pkp_b - 60000000) * 0.15
  - tax_c: 3000000 + (pkp_c - 60000000) * 0.15
  - pkp_switch_below: 63333000
  - pkp_switch_above: 63334000
  - tax_switch_below: 3000000 + (pkp_switch_below - 60000000) * 0.15
  - tax_switch_above: 3000000 + (pkp_switch_above - 60000000) * 0.15
expected:
  final_tax: 3500000.00
  pkp_tie: 63333333.33
  net_tie: 117333333.33
  tie_pct: 9.78
  pkp_a: 63333000
  pkp_b: 63348000
  pkp_c: 63360000
  tax_a: 3499950
  tax_b: 3502200
  tax_c: 3504000
  tax_switch_below: 3499950
  tax_switch_above: 3500100
```

The 9.78% is a rounded continuous approximation. At actual margins of 9.7778%, 9.779% and 9.78%, pembukuan tax is respectively IDR 3,499,950, IDR 3,502,200 and IDR 3,504,000 after PKP flooring, against IDR 3,500,000 UMKM in each case. Pembukuan is lower by IDR 50 in the first case; UMKM is lower by IDR 2,200 and IDR 4,000 in the other cases. Thus a margin below 9.78% does not by itself establish a saving with pembukuan.

In this 15% band, there is no exact tie: floored PKP of IDR 63,333,000 gives tax of IDR 3,499,950 and the next IDR 1,000 step gives IDR 3,500,100. The switch occurs when actual net income reaches IDR 117,334,000, or margin 117,334,000 / 1,200,000,000. Compare the calculated amounts rather than a rounded percentage. If the trader chooses pembukuan by opting out, the choice is permanent, so test the margin over several years before notice is given.

### Example 3: PTKP, K/2 v TK/0

OP, married, 2 children wholly maintained at 1 January, wife with no income to combine. NPPN deemed net IDR 200,000,000.

```oa-check
name: id-opt-ptkp
inputs:
  net: 200000000
  ptkp_k2: 67500000
  ptkp_tk0: 54000000
steps:
  - pkp_k2: floor(max(net - ptkp_k2, 0) / 1000) * 1000
  - tax_k2: 0.05 * min(pkp_k2, 60000000) + 0.15 * max(min(pkp_k2, 250000000) - 60000000, 0)
  - pkp_tk0: floor(max(net - ptkp_tk0, 0) / 1000) * 1000
  - tax_tk0: 0.05 * min(pkp_tk0, 60000000) + 0.15 * max(min(pkp_tk0, 250000000) - 60000000, 0)
  - difference: tax_tk0 - tax_k2
expected:
  pkp_k2: 132500000.00
  tax_k2: 13875000.00
  pkp_tk0: 146000000.00
  tax_tk0: 15900000.00
  difference: 2025000.00
```

The correct status is K/2 because of the facts at 1 January. A return filed at TK/0 overpays by IDR 2,025,000. The fix is to report the facts, not to 'register' them.

### Example 4: Crossing the ceiling

OP on the final rate, not pekerjaan bebas, last year's turnover within the ceiling. Year 1 turnover IDR 5,000,000,000, which goes over the ceiling in-year. Year 2 turnover is also IDR 5,000,000,000, with expenses IDR 833,000,000, TK/0. Year 2 is on pembukuan, because NPPN needs prior-year turnover under IDR 4,800,000,000.

```oa-check
name: id-opt-crossing
inputs:
  turnover: 5000000000
  expenses: 833000000
  ptkp: 54000000
steps:
  - year1_final: 0.005 * max(turnover - 500000000, 0)
  - net: turnover - expenses
  - pkp: floor(max(net - ptkp, 0) / 1000) * 1000
  - year2_tax: 0.05 * min(pkp, 60000000) + 0.15 * max(min(pkp, 250000000) - 60000000, 0) + 0.25 * max(min(pkp, 500000000) - 250000000, 0) + 0.30 * max(min(pkp, 5000000000) - 500000000, 0) + 0.35 * max(pkp - 5000000000, 0)
  - increase: year2_tax - year1_final
expected:
  year1_final: 22500000.00
  net: 4167000000.00
  pkp: 4113000000.00
  year2_tax: 1177900000.00
  increase: 1155400000.00
```

Year 1 stays at 0.5% to year end (Art 61(1)). The 35% bracket starts only above IDR 5,000,000,000 of taxable income, so it is not reached. Model the change before it happens. PPh 25 starts in Year 2, and a PKP report is due for Year 1.

### Example 5: Husband, wife and minor child in one test

The Penjelasan to Art 58(2) example: in tax year 2026 Tuan A, a notary, has turnover of IDR 3,000,000,000. Nyonya Y, who chose MT, has a boutique with IDR 2,000,000,000. Their minor child has singing income of IDR 500,000,000. No PT Perorangan. Assume 2025 turnover was within the ceiling, so the boutique is on the final rate in 2026.

```oa-check
name: id-opt-couple
inputs:
  husband: 3000000000
  wife: 2000000000
  minor_child: 500000000
  ceiling: 4800000000
steps:
  - combined: husband + wife + minor_child
  - over_by: max(combined - ceiling, 0)
  - wife_2026_final: 0.005 * max(wife - 500000000, 0)
expected:
  combined: 5500000000.00
  over_by: 700000000.00
  wife_2026_final: 7500000.00
```

All 3 turnovers count, including the notary's, whose own income was never on the final rate. Nyonya Y's boutique cannot use the final rate for tax year 2027. Her own IDR 2,000,000,000 being under the ceiling does not help her.

### Example 6: PPN on an IDR 100,000,000 price

A PKP sells at a price of IDR 100,000,000, once ordinary and once as a luxury good subject to PPnBM. PPnBM itself is not computed.

```oa-check
name: id-opt-ppn
inputs:
  price: 100000000
  rate: 0.12
steps:
  - nilai_lain: round(price * 11 / 12, 2)
  - ppn_ordinary: round(price * 11 / 12 * rate, 2)
  - ppn_luxury: price * rate
  - gap: ppn_luxury - ppn_ordinary
expected:
  nilai_lain: 91666666.67
  ppn_ordinary: 11000000.00
  ppn_luxury: 12000000.00
  gap: 1000000.00
```

The rate is 12% in both. Only the base differs, and the 11% is an effect, not the rate. A PKP on a besaran tertentu or other nilai lain route under separate rules is outside this (PMK 131 of 2024 Art 4).

### Example 7: Rental with a service charge

A landlord receives IDR 200,000,000 rent and IDR 15,000,000 for maintenance, security and cleaning, under 2 separate contracts for the same building. This is the Penjelasan's pattern to PP 34/2017 Art 4(2).

```oa-check
name: id-opt-rental
inputs:
  rent: 200000000
  service: 15000000
  rate: 0.10
steps:
  - gross: rent + service
  - tax: gross * rate
  - tax_on_rent_alone: rent * rate
  - no_such_saving: tax - tax_on_rent_alone
expected:
  gross: 215000000.00
  tax: 21500000.00
  tax_on_rent_alone: 20000000.00
  no_such_saving: 1500000.00
```

Tax is IDR 21,500,000 whichever way it is papered. The IDR 1,500,000 is the 'saving' that the old split advice implied, which the text does not allow.

### Example 8: Dividend through a PT, invested or not

A PT with taxable income of IDR 100,000,000 at 22% (no Art 31E) distributes all of the profit after tax to a resident individual.

```oa-check
name: id-opt-dividend
inputs:
  profit: 100000000
  corporate: 0.22
  dividend: 0.10
steps:
  - pt_tax: profit * corporate
  - paid: profit - pt_tax
  - dividend_tax: paid * dividend
  - total_pct: round(100 * (pt_tax + dividend_tax) / profit, 2)
expected:
  pt_tax: 22000000.00
  paid: 78000000.00
  dividend_tax: 7800000.00
  total_pct: 29.80
```

If the full IDR 78,000,000 is invested on the conditions above, the IDR 7,800,000 is not due and the total is 22%. If only part is invested, only the rest is taxed. If the conditions later fail, tax becomes due as above.

## Ask the client first

1. Tax residence, entity form (OP, CV or firma, PT Perorangan, PT, koperasi) and, for a body, the tax year of registration and any facility under Art 57(2)(c).
2. Gross annual turnover for the last 3 years with a current-year projection, split by business, pekerjaan bebas, rental, construction and foreign, and net margin. Include turnover of a spouse, minor children and every PT Perorangan founded by either spouse.
3. The work actually done, whether it rests on the person's own expertise, whether staff are used, and the KLU code. These decide pekerjaan bebas and NPPN %.
4. Marital status at 1 January, the NPWP arrangement (KK, PH, MT or HB), and dependants who were wholly maintained at 1 January, up to 3.
5. Regime history: years inside UMKM, any opt-out notice, any NPPN notice and its date, any Surat Keterangan, book or record keeping and accounting method, PKP status.
6. BPJS enrolment (Kesehatan and Ketenagakerjaan) and payroll, employment income, capital income, dividends received and how they were invested, and the business reason for any planned step.

## Sources

JDIH means the Ministry of Finance legal information site. Its record page gives the status and history of a regulation, and a status stated here comes from that page. 'Read in part' names the articles read. peraturan.bpk.go.id refused a scripted request and was not retried. UU PPh is read as UU 36/2008 with the amendments in UU 7/2021 and UU 6/2023, not in a consolidation.

| Source | URL | Read on |
| --- | --- | --- |
| UU 36/2008 (UU PPh), JDIH: read in part, Arts 4, 6, 7, 8, 9, 11, 14, 16, 17, 18, 25 and 31E | https://jdih.kemenkeu.go.id/api/download/ea3c666f-a427-45c4-83ba-6823e46bc068/36TAHUN2008UU.htm | 2026-11-05 |
| UU 7/2021 (UU HPP), JDIH: read in part, the amendments to UU PPh (Art 3), UU PPN Art 7 and UU KUP, and the PPS window | https://jdih.kemenkeu.go.id/api/download/a9faab97-aca7-4f87-9fdc-faa8123d1454/7TAHUN2021UU.pdf | 2026-11-05 |
| UU 6/2023 (Cipta Kerja), JDIH: read in part, Art 109 (UU 40/2007 Arts 153A to 153J), Art 111 and Art 113 (UU KUP Arts 9, 15, 19 and others) | https://jdih.kemenkeu.go.id/api/download/53aa253f-c2e0-4a7a-9f33-51606c127c3b/2023uu006.pdf | 2026-11-05 |
| UU 28/2007 (UU KUP), JDIH: read in part, Arts 1, 3, 7, 13, 15, 19 and 28 | https://jdih.kemenkeu.go.id/api/download/41f6943a-e61f-49cb-9e3f-c33de38230cf/28TAHUN2007UU.pdf | 2026-11-05 |
| UU 42/2009 (UU PPN), JDIH: read in part, Arts 7 and 8A | https://jdih.kemenkeu.go.id/api/download/7ba0c9a6-d0dd-4d7f-a8a8-b4099b3c321c/42TAHUN2009UU.pdf | 2026-11-05 |
| UU 40/2007 (companies), JDIH: read in part, Arts 7 and 68 | https://jdih.kemenkeu.go.id/api/download/c9943517-6922-4200-b7c7-4037b4dcc3a6/40TAHUN2007UU.htm | 2026-11-05 |
| PP 20/2026, JDIH: read in part, Arts 56 to 59, 20A, Art II and their Penjelasan | https://jdih.kemenkeu.go.id/api/download/d057ff82-50e7-4127-b66b-f704a36f071d/2026pp020.pdf | 2026-11-05 |
| PP 55/2022, JDIH: read in part, Arts 9 to 11, 32, 33, 35, 56 to 64 and 72, and Penjelasan to Art 61 | https://jdih.kemenkeu.go.id/api/download/cab6ec99-3dbc-47c6-adbf-ea5f0f7117d6/55TAHUN2022PP.pdf | 2026-11-05 |
| PP 19/2009, JDIH: read in full, all articles | https://jdih.kemenkeu.go.id/api/download/58a33c40-41b9-426d-b935-64f63173fb71/19TAHUN2009PP.htm | 2026-11-06 |
| PP 58/2023, JDIH: read in part, the revocation of PP 80/2010 only | https://jdih.kemenkeu.go.id/api/download/e47c3fc4-a912-4bf1-bcad-335fee3f71f8/2023pp058.pdf | 2026-11-05 |
| PP 9/2022, JDIH: read in part, Arts 3 and 10D and Penjelasan to Art 3(1) | https://jdih.kemenkeu.go.id/api/download/9f4b118b-2f73-43d0-9537-b07663657f60/9TAHUN2022PP.pdf | 2026-11-05 |
| PP 34/2017, JDIH: read in part, Arts 2 to 4 and Penjelasan to Art 4 | https://jdih.kemenkeu.go.id/api/download/c9be149c-4489-4d9e-b1f6-912808e416c4/34TAHUN2017PP.pdf | 2026-11-05 |
| PP 34/2016, JDIH: read in part, Arts 2 and 6 | https://jdih.kemenkeu.go.id/api/download/59e6ec13-8112-41f7-b63b-6891cac23310/34TAHUN2016PP.pdf | 2026-11-05 |
| PP 45/2019, JDIH: read in part, Arts 29B and 29C | https://jdih.kemenkeu.go.id/api/download/22cbb01a-a28b-4a98-9f76-fa1951392bc5/45TAHUN2019PP.pdf | 2026-11-05 |
| PP 131/2000, JDIH: read in part, Arts 2 and 3 | https://jdih.kemenkeu.go.id/api/download/f3b4a965-cb82-4764-ad9f-1a79539e449b/131TAHUN2000PP.pdf | 2026-11-05 |
| PP 93/2010, JDIH: read in part, Arts 1 to 4 | https://jdih.kemenkeu.go.id/api/download/4131c047-4770-4d66-afee-bfcd810a47c4/93TAHUN2010PP.htm | 2026-11-05 |
| PP 91/2021, JDIH: read in part, Art 2 | https://jdih.kemenkeu.go.id/api/download/03829d02-e7a8-4dd6-a7ff-d881f854b218/91TAHUN2021PP.pdf | 2026-11-05 |
| PP 8/2021, JDIH: read in part, Arts 3 to 7 | https://jdih.kemenkeu.go.id/api/download/680a952b-3f39-4e9c-86ea-4e4e1d1470e4/8TAHUN2021PP.pdf | 2026-11-05 |
| PP 7/2021, JDIH: read in part, Art 35 | https://jdih.kemenkeu.go.id/api/download/3e30c923-6c9c-4528-8101-7f9faf8f4eb3/7TAHUN2021PP.pdf | 2026-11-05 |
| PP 49/2023, JDIH DJSN: read in part, Art 18A | https://jdih.djsn.go.id/assets/file/pp%20nomor%2049%20tahun%202023.pdf | 2026-11-05 |
| PP 6/2025, JDIH: read in part, Art 11 | https://jdih.kemenkeu.go.id/api/download/909a0028-c6d2-476b-8692-97a800fafe56/2025PP006.pdf | 2026-11-05 |
| PP 7/2025, JDIH: read in part, Arts 3, 4, 10 and 11 | https://jdih.kemenkeu.go.id/api/download/cdb7e0ef-fa1a-43f4-953e-792cecb57321/2025PP007.pdf | 2026-11-05 |
| Perpres 82/2018, JDIH: read in part, Arts 30 to 34 | https://jdih.kemenkeu.go.id/api/download/282b38cb-22fc-4f40-b201-4740a595bb73/82TAHUN2018PERPRES.pdf | 2026-11-05 |
| Perpres 64/2020, JDIH: read in part, Arts 30, 31 (deleted), 32 and 34 as amended | https://jdih.kemenkeu.go.id/api/download/179608f7-a2a0-41c0-aaec-e7d60eb36054/64TAHUN2020PERPRES.pdf | 2026-11-05 |
| PMK 164 of 2023, JDIH: read in part, Arts 4 to 8, 16 to 20 and 24 | https://jdih.kemenkeu.go.id/api/download/a99b8e80-9694-46ab-8de1-63c2484aa636/2023pmkeuangan164.pdf | 2026-11-05 |
| PMK 168 of 2023, JDIH: read in part, Arts 5, 7, 10 and 20 | https://jdih.kemenkeu.go.id/api/download/e60a82e0-b218-40f5-9d18-b924aa1e11ce/2023pmkeuangan168.pdf | 2026-11-05 |
| PMK 172 of 2023, JDIH: read in part, the revocation clause only | https://jdih.kemenkeu.go.id/api/download/b0b74668-cf4d-456b-bb23-be5e1aeac2cb/2023pmkeuangan172.pdf | 2026-11-05 |
| PMK 72 of 2023, JDIH: read in part, Arts 2 and 5, the revocation clause and the Group 1 office machine line of the Lampiran | https://jdih.kemenkeu.go.id/api/download/46cededa-86ae-4cc9-93e5-b6bef8892074/2023pmkeuangan072.pdf | 2026-11-05 |
| PMK 81 of 2024, JDIH: read in part, Arts 1, 94, 169, 226, 234, 370 to 374, 432 to 434, 448 to 453 and 483, the revocation clause | https://jdih.kemenkeu.go.id/api/download/637047be-3dba-4347-aba1-98fa7fd5ab3f/2024pmkeuangan081.pdf | 2026-11-05 |
| PMK 53 of 2025, JDIH: read in part, its list of articles amended | https://jdih.kemenkeu.go.id/api/download/f5252d58-c4a6-45c3-87b7-cb3b6c3abbf9/2025pmkeuangan053.pdf | 2026-11-05 |
| PMK 54 of 2025, JDIH: read in part, its list of articles amended | https://jdih.kemenkeu.go.id/api/download/454dde57-6a75-40ef-9afe-ff66077074db/2025pmkeuangan054.pdf | 2026-11-05 |
| PMK 1 of 2026, JDIH: read in part, its list of articles amended | https://jdih.kemenkeu.go.id/api/download/b5f99bff-f689-4e4f-ae3a-7c6a9a4cfe8a/2026pmkeuangan001.pdf | 2026-11-05 |
| PMK 101/PMK.010/2016, JDIH: read in part, Art 1 | https://jdih.kemenkeu.go.id/api/download/d8072adc-8f62-48d1-95e0-7d25c92b6362/101~PMK.010~2016Per.pdf | 2026-11-05 |
| PMK 128/PMK.010/2019, JDIH: read in part, Arts 1 and 2 | https://jdih.kemenkeu.go.id/api/download/7d8167be-9bbe-4850-bc3e-62910e8f9b13/128~PMK.010~2019Per.pdf | 2026-11-05 |
| PMK 18/PMK.03/2021, JDIH: read in part, Arts 15 and 16 | https://jdih.kemenkeu.go.id/api/download/39fdb2fc-1736-4ebb-80f5-d257f75df0b5/18~PMK.03~2021Per.pdf | 2026-11-05 |
| PMK 131 of 2024, JDIH: read in part, Arts 2 to 5 | https://jdih.kemenkeu.go.id/api/download/f128868e-3cf6-4596-8407-c34eeca0e7be/2024pmkeuangan131.pdf | 2026-11-05 |
| PMK 197/PMK.03/2013, JDIH: read in part, Arts 1 and 4 | https://jdih.kemenkeu.go.id/api/download/529df403-55d0-4df7-8a59-b55a2f17fd9d/197~PMK.03~2013Per.htm | 2026-11-05 |
| PMK 50 of 2025, JDIH: read in part, title and subject | https://jdih.kemenkeu.go.id/api/download/66a7633b-9e1b-4a54-9046-5320aa96c7e1/2025pmkeuangan050.pdf | 2026-11-05 |
| PER-11/PJ/2025, JDIH: read in part, Arts 83, 84 and 143 | https://jdih.kemenkeu.go.id/api/download/a94edee5-e585-4eeb-b9e7-a76f616c92fb/PER-11_PJ_2025.pdf | 2026-11-05 |
| PER-11/PJ/2025 Lampiran, JDIH: read in part, SPT Tahunan status and dependant lines, Lampiran 3D and the Art 31E instructions | https://jdih.kemenkeu.go.id/api/download/465612a0-fca6-4f3e-8c9f-b32970ad49af/Lampiran%20PER-11%20PJ%202025.pdf | 2026-11-05 |
| PER-17/PJ/2015, DJP: read in part, Arts 1 to 5 | https://www.pajak.go.id/sites/default/files/2019-03/PER%20-%2017.PJ_.2015.pdf | 2026-11-05 |
| PER-17/PJ/2015 Lampiran I, DJP: read in part, the KLU rows in the table, checked by word position | https://www.pajak.go.id/sites/default/files/2019-03/Lampiran%201_PER%20-%2017.PJ_.2015.pdf | 2026-11-05 |
| PER-17/PJ/2015 Lampiran II, DJP: read in part, that it holds higher audit norms | https://www.pajak.go.id/sites/default/files/2019-03/Lampiran%202_PER%20-%2017.PJ_.2015.pdf | 2026-11-05 |
| PER-17/PJ/2015 Lampiran III, DJP: read in part, that it holds audit norms for bodies | https://www.pajak.go.id/sites/default/files/2019-03/Lampiran%203_PER%20-%2017.PJ_.2015.pdf | 2026-11-05 |
| DJP Kanwil Jakarta Timur press note of 7 July 2026: read in part, its statement on PP 20/2026 | https://www.pajak.go.id/id/siaran-pers/kanwil-djp-jakarta-timur-sosialisasikan-pp-nomor-20-tahun-2026-bagi-umkm | 2026-11-05 |
| JDIH record, PMK 153/PMK.010/2020: read in part, status and history | https://jdih.kemenkeu.go.id/dok/153-pmk-010-2020 | 2026-11-05 |
| JDIH record, PMK 213/PMK.03/2016: read in part, status and history | https://jdih.kemenkeu.go.id/dok/213-pmk-03-2016 | 2026-11-05 |
| JDIH record, PMK 93/PMK.03/2019: read in part, status and history | https://jdih.kemenkeu.go.id/dok/93-pmk-03-2019 | 2026-11-05 |
| JDIH record, PMK 68/PMK.03/2022: read in part, status and history | https://jdih.kemenkeu.go.id/dok/68-pmk-03-2022 | 2026-11-05 |
| JDIH record, PMK 37 of 2025: read in part, title, status and history | https://jdih.kemenkeu.go.id/dok/pmk-37-tahun-2025 | 2026-11-05 |
| JDIH record, UU 11/2020: read in part, status and history | https://jdih.kemenkeu.go.id/dok/uu-11-tahun-2020 | 2026-11-05 |
| JDIH record, UU 40/2007: read in part, status and history | https://jdih.kemenkeu.go.id/dok/uu-40-tahun-2007 | 2026-11-05 |
| JDIH record, PP 20/2026: read in part, status, date and gazette number | https://jdih.kemenkeu.go.id/dok/pp-20-tahun-2026 | 2026-11-05 |

Not yet confirmed: an implementing PMK for PP 20/2026; the position from tax year 2027 of individuals and PT Perorangan whose old window ended in 2024 or 2025; which parts of PMK 164 of 2023 stay consistent with PP 20/2026; whether a fall below the ceiling reopens the final rate after Art 61(2); PER-17/PJ/2015 status against any later KLU list, and its Lampiran 4; receipts or accrual for NPPN income; PER-25/PJ/2018; PER-37/PJ/2022 and its relation to PMK 37 of 2025; SE-27/PJ.22/1986; PMK 207/PMK.03/2015 and the bad debt list rule; pension contribution limits; unrealised FX; PMK 81 Arts 435 to 447; furnished rental; timing of advances under the final rate; PP 132/2000; PP 41/1994 and PP 14/1997; PP 123/2015, which amends PP 131/2000; PP 44, 45 and 46 of 2015, UU 24/2011 and Perpres 59/2024; the scope of Perpres 14/2021; JHT rates; JP rates and the JP wage cap; the conflict between PP 49/2023 Art 18A and PP 6/2025 Art 11 on the source of JKP funding; the bonus line for Kesehatan; any Ketenagakerjaan duty of an OP; PT Perorangan and PT setup fees; Art 68 of UU 40/2007 for a PT Perorangan; JDIH's status for UU 40/2007, which conflicts with UU 6/2023 amending it; the PSAK 72 label; KMK monthly interest rates; the current status of PMK 107/PMK.03/2017; the outcome of the PP 9/2022 Art 10D evaluation; the current names of the 1721 forms; a separate SPT Masa PPh 25 form.
