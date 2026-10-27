---
name: fr-cfe
description: "French local business taxes for tax year 2026: the cotisation foncière des entreprises (CFE), the CVAE and the cap on the contribution économique territoriale (CET). Covers who is within the CFE (letting thresholds included), the N-2 rental-value base, the 2026 minimum-base bands, the creation-year exemption and the half base in the following year, the EUR 5,000 small-turnover exemption, artisan, Corsica and industrial reductions, the 1.12% chamber tax and 1% management fee, the June acompte and 15 December balance, forms 1447-C-SD and 1447-M-SD, the CVAE thresholds, rates and relief, and the CET cap (1.531% for 2026). Trigger on: CFE, cotisation foncière des entreprises, CFE micro-entrepreneur, base minimum CFE, CVAE, plafonnement CET, 1447-C, 1327-CET. Out of scope: corporate income tax (fr-corporate-tax), self-employed income tax (fr-income-tax), social contributions (fr-social-contributions), rental income tax (fr-rental-income), setting up (france-formation), booking the tax (france-bookkeeping), the IFER."
version: 0.1
jurisdiction: FR
tax_year: 2026
last_updated: 2026-10-27
authored_by: Michael Cutajar and the OpenAccountants team
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# France: the CFE, with the CVAE and the CET cap (2026)

This skill works out whether a business owes the cotisation foncière des entreprises (CFE) for 2026, on what base, how much is added to it, when it is paid, and when the cap on the contribution économique territoriale (CET, the CFE plus the CVAE) gives money back. The CFE for 2026 is assessed on the premises used and the turnover made in 2024 (year N-2). Every commune votes its own rate and its own minimum base, so no amount can be computed without them.

## Who this applies to

- **General rule.** The CFE is due where an activity is carried on in France, habitually, on a professional footing (not non-profit and not the mere management of private wealth), and not as an employee. This holds whatever the activity, tax regime or nationality. Source: https://entreprendre.service-public.gouv.fr/vosdroits/F23547 (CGI art. 1447).
- **Who pays.** Any company, any entity without legal personality (for example indivisions or funds), and any individual entrepreneur, micro-entrepreneurs included, even when working from home or at clients' sites. Employees are out. Source: https://entreprendre.service-public.gouv.fr/vosdroits/F23547.
- **The date that counts.** The CFE is due by a business carrying on its non-salaried activity habitually on 1 January of the year of assessment. Source: https://www.impots.gouv.fr/sites/default/files/media/3_Documentation/depliants/pro_fiche_cet-ifer_2026.pdf.
- **Letting premises.** Letting bare premises is within the CFE only once receipts excluding VAT are at least EUR 100,000, and bare letting for housing is never within it. Furnished letting is within the CFE once receipts are more than EUR 5,000, except a let inside the owner's main home. Source: https://entreprendre.service-public.gouv.fr/vosdroits/F23547.
- **Automatic exemptions (permanent unless stated).** Artisans and façonniers who use only apprentices under contract (spouse, PACS partner and children may help); taxi or ambulance drivers with 1 or 2 cars of up to 7 seats not run at the same time, on regulated fares (CGI art. 1453); independent home sellers (VDI) with gross pay below EUR 7,930; painters, sculptors, engravers and draughtsmen selling only their own work, and graphic designers limited to graphic works (CGI art. 1460); author-photographers, authors, composers, choreographers and translators receiving droits d'auteur, and lyric and dramatic artists; teachers teaching personally at home, at pupils' homes or in premises with no sign and no special fitting; midwives and garde-malades not under the nursing profession; sportsmen for practising a sport; occasional letting of part of one's home at a reasonable price, or furnished where it is the sub-tenant's main home (CGI art. 1459); classified tourist lets and chambres d'hôtes in the owner's home unless the commune decides otherwise. Temporary: lawyers who completed the CAPA, 2 years from the start of activity; businesses created in a BUD between 1 January 2018 and 31 December 2026, or in a ZDP between 1 January 2019 and 31 December 2027, exempt from income or corporation tax, 7 years from creation. The page lists more (cooperatives, ports, fishermen, farmers, Scop, private schools under contract, press, trade unions, HLM bodies, methanisation, social activities): check it before saying a client is liable. Source: https://entreprendre.service-public.gouv.fr/vosdroits/F23547.
- **Optional exemptions (only if the commune or EPCI decided them).** Zones ZAFR, ZAIPME, ZFRR, ZUS, QPV, ZRD, BER, the ZFA overseas, and Corsica; doctors and health auxiliaries opening a secondary practice in a medical desert, rural vets, JEI, JEC, JEU and JEII, independent record shops, labelled bookshops, live performance, caisses de crédit municipal; and a 3-year exemption for creating or extending an establishment. Requested on 1447-M-SD (with annex 1447-E, and form 1465-SD for ZAFR, ZAIPME and ZFRR). Source: https://entreprendre.service-public.gouv.fr/vosdroits/F23547. The impots.gouv.fr fiche adds, as an example, a 5-year exemption for commercial businesses in a QPV with fewer than fifty employees and turnover below EUR 10 million, unless the commune decides otherwise. Source: https://www.impots.gouv.fr/sites/default/files/media/3_Documentation/depliants/pro_fiche_cet-ifer_2026.pdf.
- **Creation year.** A business is exempt for the year it starts. Source: https://entreprendre.service-public.gouv.fr/vosdroits/F23547.

## Rates, bands and thresholds

| Item | Rate or amount | Year | Source |
|---|---|---|---|
| CFE rate | voted by each commune or EPCI; look it up in "Connaître les taux d'impositions directes locales par commune" | 2026 | https://entreprendre.service-public.gouv.fr/vosdroits/F23547 |
| Minimum base, N-2 turnover EUR 10,000 or less | EUR 250 to EUR 597 (commune chooses) | CFE due 2026 | https://entreprendre.service-public.gouv.fr/vosdroits/F23547 |
| Minimum base, EUR 10,001 to EUR 32,600 | EUR 250 to EUR 1,194 | CFE due 2026 | https://entreprendre.service-public.gouv.fr/vosdroits/F23547 |
| Minimum base, EUR 32,601 to EUR 100,000 | EUR 250 to EUR 2,509 | CFE due 2026 | https://entreprendre.service-public.gouv.fr/vosdroits/F23547 |
| Minimum base, EUR 100,001 to EUR 250,000 | EUR 250 to EUR 4,183 | CFE due 2026 | https://entreprendre.service-public.gouv.fr/vosdroits/F23547 |
| Minimum base, EUR 250,001 to EUR 500,000 | EUR 250 to EUR 5,974 | CFE due 2026 | https://entreprendre.service-public.gouv.fr/vosdroits/F23547 |
| Minimum base, EUR 500,001 or more | EUR 250 to EUR 7,769 | CFE due 2026 | https://entreprendre.service-public.gouv.fr/vosdroits/F23547 |
| Small-turnover exemption: business on the minimum base whose N-2 turnover (N-1 if created in N-1) did not exceed | EUR 5,000 | 2026 | https://entreprendre.service-public.gouv.fr/vosdroits/F23547 |
| Bare letting: within the CFE from receipts of at least | EUR 100,000 | 2026 | https://entreprendre.service-public.gouv.fr/vosdroits/F23547 |
| Furnished letting: within the CFE from receipts of more than | EUR 5,000 | 2026 | https://entreprendre.service-public.gouv.fr/vosdroits/F23547 |
| VDI exemption: gross pay below | EUR 7,930 | 2026 | https://entreprendre.service-public.gouv.fr/vosdroits/F23547 |
| Reduction, year after creation | 50% of the base | 2026 | https://entreprendre.service-public.gouv.fr/vosdroits/F23547 |
| Reduction, artisan with 1 / 2 / 3 employees (apprentices not counted), if pay for labour is more than 50% of turnover including VAT | 75% / 50% / 25% | 2026 | https://entreprendre.service-public.gouv.fr/vosdroits/F23547 |
| Reduction, establishment in Corsica | 25% | 2026 | https://entreprendre.service-public.gouv.fr/vosdroits/F23547 |
| Reduction of rental value, industrial establishments | 30% | 2026 | https://entreprendre.service-public.gouv.fr/vosdroits/F23547 |
| Taxe additionnelle (CCI), on the CFE base | 1.12% | 2026 | https://entreprendre.service-public.gouv.fr/vosdroits/F23547 |
| Frais de gestion, on CFE plus taxe additionnelle | 1% | 2026 | https://entreprendre.service-public.gouv.fr/vosdroits/F23547 |
| June acompte, where last year's CFE reached the threshold and no monthly debit | 50% of last year's CFE; threshold EUR 3,000 | 2026 | https://www.impots.gouv.fr/sites/default/files/media/3_Documentation/depliants/pro_fiche_cet-ifer_2026.pdf |
| CET cap rate, CET due for 2025 | 1.438% of value added | 2025 | https://bofip.impots.gouv.fr/bofip/2594-PGP.html |
| CET cap rate, CET due for 2026 and 2027 | 1.531% of value added | 2026 | https://bofip.impots.gouv.fr/bofip/2594-PGP.html |
| CVAE entry threshold (file 1330-CVAE above it) | turnover excluding VAT more than EUR 152,500 | 2026 | https://bofip.impots.gouv.fr/bofip/839-PGP.html |
| CVAE rate, turnover below EUR 500,000 | 0% | 2026 | https://bofip.impots.gouv.fr/bofip/839-PGP.html |
| CVAE maximum rate, turnover above EUR 50,000,000 | 0.28% (2026 and 2027); 0.19% (2025) | 2026 | https://bofip.impots.gouv.fr/bofip/839-PGP.html |
| Complementary contribution on the 2025 CVAE only | 47.4% of the 2025 CVAE | 2025 | https://bofip.impots.gouv.fr/bofip/839-PGP.html |
| CVAE flat relief, turnover below EUR 2,000,000 | EUR 188 (2026 and 2027); EUR 125 (2025) | 2026 | https://bofip.impots.gouv.fr/bofip/839-PGP.html |
| CVAE franchise: no CVAE where the annual amount does not exceed | EUR 63 | 2026 | https://bofip.impots.gouv.fr/bofip/839-PGP.html |
| CVAE acomptes on 1329-AC, 15 June and 15 September | 50% each of the N-1 CVAE; none if N-1 CVAE is EUR 1,500 or less | 2026 | https://www.impots.gouv.fr/sites/default/files/media/3_Documentation/depliants/pro_fiche_cet-ifer_2026.pdf |

Between EUR 500,000 and EUR 50,000,000 the CVAE rate rises by the formula in the BOFiP table for the year; round to the nearest hundredth. The minimum-base figures are bases, not tax: the commune's rate is applied to them.

## The taxable base

- **Real base.** The rental value (valeur locative) of the property subject to taxe foncière that the business used for its activity in N-2. For the CFE due for 2026, the premises used in 2024. The rental value is an administrative value, not the rent paid. Source: https://entreprendre.service-public.gouv.fr/vosdroits/F23547 (CGI art. 1498 to 1498 bis).
- **Reductions.** Apply the year-after-creation, artisan, Corsica and industrial reductions in the table. Seasonal businesses (restaurants, cafés) have the rental value reduced for the inactive period; no figure is given. Ports, airports and anti-pollution installations have their own reductions: refer. Source: https://entreprendre.service-public.gouv.fr/vosdroits/F23547.
- **New establishment.** For the two years after the creation year, the base is the property at the business's disposal on 31 December of its first year. Source: https://www.impots.gouv.fr/sites/default/files/media/3_Documentation/depliants/pro_fiche_cet-ifer_2026.pdf.
- **Minimum base.** If the real base is lower than the commune's minimum base, or there are no premises, the CFE is computed on the minimum base. The band follows the N-2 turnover excluding VAT over 12 months. With several establishments, the minimum-base CFE is due at the principal establishment, which is not always the registered office. Source: https://entreprendre.service-public.gouv.fr/vosdroits/F23547 (CGI art. 1647 D).
- **What is paid.** CFE = base x the commune's rate. Then add the taxe additionnelle (1.12% of the base) and the frais de gestion (1% of CFE plus taxe additionnelle). Exempt from the taxe additionnelle: artisans in the RNE not on the chamber of commerce electoral list, agricultural cooperatives and Sica, fishermen, furnished-let operators, heads of institutions. A micro-entrepreneur pays the taxe additionnelle through www.auto-entrepreneurs.urssaf.fr, not on the CFE notice. A craft business also pays the TCMA (no rate on the pages read). Sources: https://entreprendre.service-public.gouv.fr/vosdroits/F23547, https://www.impots.gouv.fr/sites/default/files/media/3_Documentation/depliants/pro_fiche_cet-ifer_2026.pdf.
- **CET cap.** On request, relief = CFE + CVAE minus the cap rate x value added (CVAE rules, for the year or the last 12-month period closed in it). It cannot take the CET below the commune's minimum CFE. Chamber taxes are left out. Source: https://entreprendre.service-public.gouv.fr/vosdroits/F23548, https://bofip.impots.gouv.fr/bofip/2594-PGP.html.
- **Deducting the CFE from profit.** Under a régime réel, profit is computed after the taxes borne by the business and put into collection during the year (CGI art. 39, 1-4°); the CFE is not among the listed exclusions, though the page does not name it. A micro-entrepreneur gets no separate deduction: the flat allowance covers expenses. Sources: https://bofip.impots.gouv.fr/bofip/2102-PGP.html, https://entreprendre.service-public.gouv.fr/vosdroits/F23267.

## Deadlines and filing

| Obligation | Form or channel | Due |
|---|---|---|
| Creation-year exemption and base for next year | 1447-C-SD (déclaration initiale), paper, to the SIE | by 31 December of the creation year |
| New operator after a change of operator in 2026 | 1447-C-SD | by 31 December 2026, for the CFE due in 2027 |
| Exemption request, change of surface or employees, letting threshold crossed, cessation | 1447-M-SD | before the 2nd working day after 1 May; 5 May 2026 for the CFE 2027 |
| Notice | online only, espace professionnel on impots.gouv.fr | before 15 June / 15 December |
| Acompte (last year's CFE at least EUR 3,000, not on monthly debit) | online or debit | 15 June |
| Balance | online, monthly debit or debit at due date | 15 December (next working day if a weekend or holiday) |
| Monthly debit option | ten debits January to October | sign up by 30 June; before 15 June to avoid the acompte |
| Debit at due date option | | sign up by 31 May (acompte), 30 November (balance) |
| CVAE value-added return | 1330-CVAE, electronic, if turnover above EUR 152,500 | 2nd working day after 1 May |
| CVAE final return and balance | 1329-DEF | 2nd working day after 1 May of N+1; 5 May 2026 for 2025 |
| CET cap claim | 1327-CET-SD (régime réel) or 1327S-CET-SD (micro) to the SIE | by 31 December of the year after collection; 31 December 2026 for 2025 |

Sources: https://entreprendre.service-public.gouv.fr/vosdroits/F23547, https://www.impots.gouv.fr/sites/default/files/media/3_Documentation/depliants/pro_fiche_cet-ifer_2026.pdf, https://entreprendre.service-public.gouv.fr/vosdroits/F23548. Half of the cap relief expected for N-1 may be taken off the June acompte of year N, at the taxpayer's own risk, and the relief expected for the current year may be taken off that year's balance. Source: https://entreprendre.service-public.gouv.fr/vosdroits/F23548.

The two official pages word the acompte boundary differently: the fiche says "supérieur ou égal à 3 000 €", service-public says "supérieure à 3 000 €" and gives the window "entre le 26 mai et le 16 juin". At exactly EUR 3,000, follow the avis d'acompte in the espace professionnel.

## Penalties and interest

- Payment must be by electronic means (online, monthly debit or debit at due date). Source: https://www.impots.gouv.fr/sites/default/files/media/3_Documentation/depliants/pro_fiche_cet-ifer_2026.pdf.
- Late payment of the CFE carries a surcharge. No official page read today prints its rate, and Légifrance (CGI art. 1730) refused the request, so do not quote a rate: check the notice.

## Cross-border points

- The CFE turns on an activity carried on in France, whatever the nationality. A foreign business with premises or an activity in France is within it on the same rules. Source: https://entreprendre.service-public.gouv.fr/vosdroits/F23547.
- A non-resident letting bare premises in France is within the CFE once receipts reach EUR 100,000 (housing excluded). Source: https://entreprendre.service-public.gouv.fr/vosdroits/F23547.
- Non-resident taxpayers (for example non-resident letters of bare premises) may pay by bank transfer, from a State on a list set by arrêté; the only other exception is some companies managed by the Direction des grandes entreprises. Everyone else pays electronically. Sources: https://www.impots.gouv.fr/sites/default/files/media/3_Documentation/depliants/pro_fiche_cet-ifer_2026.pdf, https://entreprendre.service-public.gouv.fr/vosdroits/F23547.
- For residence, non-resident income tax and treaty questions, use fr-cross-border.

## Worked examples

**Example 1: home-based consultant on the minimum base, 2026.** A sole trader on a régime réel works from home with no premises. Turnover excluding VAT in 2024 was EUR 25,000, so the second band applies (EUR 250 to EUR 1,194). Suppose the commune set its minimum base at EUR 800 and its rate at 22% (illustrative figures: get the real ones for the commune). The base is the minimum base, EUR 800. CFE = 800 x 22% = EUR 176. Taxe additionnelle = 800 x 1.12% = EUR 8.96. Frais de gestion = 1% x (176 + 8.96) = EUR 1.85. Total on the notice: EUR 186.81, due by 15 December 2026. Last year's CFE was below EUR 3,000, so no June acompte.

```oa-check
name: Home-based consultant, minimum base, CFE 2026
inputs:
  min_base: 800
  rate_pct: 22
  ta_pct: 1.12
  fg_pct: 1
steps:
  - cfe: min_base * rate_pct / 100
  - taxe_additionnelle: min_base * ta_pct / 100
  - frais_gestion: (cfe + taxe_additionnelle) * fg_pct / 100
  - total: cfe + taxe_additionnelle + frais_gestion
expected:
  cfe: 176.00
  taxe_additionnelle: 8.96
  frais_gestion: 1.85
  total: 186.81
```

**Example 2: CET cap held back by the minimum CFE (BOFiP example, CET 2026).** A business has turnover of EUR 400,000, so no CVAE (below EUR 500,000). Value added is EUR 15,000, CFE is EUR 600, and the commune's minimum CFE is EUR 500. The cap is 15,000 x 1.531% = EUR 229.65. Relief before the limit = 600 - 229.65 = EUR 370.35. The CET after relief cannot fall below the minimum CFE, so relief is limited to 600 - 500 = EUR 100. Claim on 1327-CET-SD by 31 December 2027. Source: https://bofip.impots.gouv.fr/bofip/2594-PGP.html.

```oa-check
name: CET cap limited by minimum CFE, 2026
inputs:
  value_added: 15000
  cfe: 600
  cvae: 0
  min_cfe: 500
  cap_rate_pct: 1.531
steps:
  - cap: value_added * cap_rate_pct / 100
  - relief_unlimited: cfe + cvae - cap
  - relief: min(relief_unlimited, cfe + cvae - min_cfe)
expected:
  cap: 229.65
  relief_unlimited: 370.35
  relief: 100.00
```

## Ask the client first

- When did the business start, and has it changed hands? Creation year exempt, next year on half base; a transfer leaves the old operator liable for the whole year.
- Which commune holds the principal establishment, and are there other premises? The commune sets the rate and the minimum base.
- Own or rented premises, or home and clients' sites only? No premises means the minimum base.
- Turnover excluding VAT in 2024, restated to 12 months if short? Picks the band and the EUR 5,000 exemption.
- What is the activity, and who works in it besides apprentices? Decides the activity exemptions and the artisan reduction.
- Was last year's CFE EUR 3,000 or more, and is the client on monthly debit? Decides the June acompte.

## Sources

| Source | URL | Read on |
|---|---|---|
| Service-public, Cotisation foncière des entreprises (CFE), vérifié le 02 avril 2026 (CGI art. 1447 to 1478 bis, 1647 D) | https://entreprendre.service-public.gouv.fr/vosdroits/F23547 | 2026-10-27 |
| Service-public, Peut-on plafonner la CET ?, vérifié le 01 janvier 2026 | https://entreprendre.service-public.gouv.fr/vosdroits/F23548 | 2026-10-27 |
| impots.gouv.fr, La contribution économique territoriale et l'IFER, fiche mars 2026 | https://www.impots.gouv.fr/sites/default/files/media/3_Documentation/depliants/pro_fiche_cet-ifer_2026.pdf | 2026-10-27 |
| BOI-IF-CFE-40-30-20-30, plafonnement de la CET, version from 29/04/2026 (CGI art. 1647 B sexies) | https://bofip.impots.gouv.fr/bofip/2594-PGP.html | 2026-10-27 |
| BOI-CVAE-LIQ-10, CVAE rate and relief, version from 19/11/2025 (CGI art. 1586 quater) | https://bofip.impots.gouv.fr/bofip/839-PGP.html | 2026-10-27 |
| BOI-BIC-CHG-40-30, taxes as business expenses (CGI art. 39, 1-4°) | https://bofip.impots.gouv.fr/bofip/2102-PGP.html | 2026-10-27 |
| Service-public, Régime fiscal de la micro-entreprise | https://entreprendre.service-public.gouv.fr/vosdroits/F23267 | 2026-10-24 |

Not yet confirmed: the late-payment surcharge rate for the CFE (CGI art. 1730; Légifrance returned 403); how the cessation relief (dégrèvement pour cessation d'activité) is claimed; the TCMA rate; the split of the real base across communes for several establishments; the seasonal reduction figure; penalties for a late 1447-C-SD, 1447-M-SD or 1330-CVAE. Two source conflicts, settled: (1) the service-public cap page (vérifié le 01 janvier 2026) applies 1.531% to the CET for 2025; that page is out of date. Loi n° 2025-127 de finances pour 2025, art. 62, kept the cap at 1.531% for the CET due for 2026 and 2027 only, and left 1.438% for 2025 (BOFiP 2594-PGP § 1 and the impots.gouv.fr fiche agree). (2) BOFiP 839-PGP's group-consolidation paragraph still prints the pre-2025 trajectory (EUR 188 for 2024, EUR 125 for 2025, EUR 63 for 2026); the rule paragraph, written after the same art. 62, gives EUR 188 for 2026 and 2027, which is the figure to use.

<!-- openaccountants-cta-block -->

---

## Talk to a verified accountant

This guide is maintained by the OpenAccountants network — accountants who put
their name behind the tax answers AI gives people. The live, always-current
version (and the professional behind it) is at
[openaccountants.com](https://www.openaccountants.com).

- Use it in your AI: https://www.openaccountants.com/connect
- Meet the accountants: https://www.openaccountants.com/network

> **General reference only.** This document does not constitute tax, legal, or
> financial advice. Verify figures against the cited primary sources or with a
> licensed professional before relying on them.
