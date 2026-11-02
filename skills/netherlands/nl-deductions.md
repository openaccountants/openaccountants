---
name: nl-deductions
description: "Dutch personal deductions (aftrekposten) a resident individual claims in the 2026 income tax return (aangifte inkomstenbelasting). Covers mortgage interest (hypotheekrenteaftrek), the eigenwoningforfait and the Wet Hillen deduction; the tariefsaanpassing that caps relief in the top band at 37.56%; partner alimony; specific care costs (specifieke zorgkosten) with the increase and the threshold; gifts (giftenaftrek: ordinary gifts with the 1%/EUR 60 floor and 10% ceiling, periodic gifts, the cultural uplift); weekend costs for severely disabled persons; the end of the study-cost deduction; the 2026 tax credits as pointers; who files and the 1 May deadline. Tax year 2026, with 2025 figures for returns still open. Trigger phrases: aftrekposten, hypotheekrenteaftrek, tariefsaanpassing, zorgkosten aftrek, giftenaftrek, ANBI, periodieke gift, partneralimentatie, studiekosten, persoonsgebonden aftrek. Out of scope: entrepreneur deductions (nl-zzp-deductions), rates and credits in full (nl-income-tax, nl-income-tax-special-groups), non-residents (nl-cross-border), objections (nl-tax-objection)."
version: 1.3
jurisdiction: NL
tax_year: 2026
last_updated: 2026-10-31
authored_by: Michael Cutajar and the OpenAccountants team
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
depends_on:
  - income-tax-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Netherlands: income tax deductions for individuals (aftrekposten) 2026

## Who this applies to

- **Resident individuals** (binnenlandse belastingplichtigen) filing the 2026 aangifte inkomstenbelasting. Tax year = calendar year 1 January to 31 December 2026. Currency euro; figures below use a comma for thousands and a point for decimals (the Belastingdienst writes them the other way round).
- **What this skill covers:** the own home in box 1 (mortgage interest, eigenwoningforfait, Wet Hillen), the tariefsaanpassing, and the persoonsgebonden aftrek of Wet IB 2001 chapter 6. Since earlier repeals, the personal deductions left in the law are exactly four (Wet IB art. 6.1(2)): maintenance obligations (alimony), specific care costs, weekend costs for severely disabled persons, and gifts. Unused personal deductions from earlier years are added (art. 6.1(1)(b)).
- **Fiscal partners** (fiscale partners) for the whole year, or for part of the year who choose to be partners all year, combine care costs, gifts and weekend costs and test the thresholds on their joint income. They may split the combined deduction any way they like, as long as the total is 100%.
- **Not here:**
  - Entrepreneur reliefs (zelfstandigenaftrek, startersaftrek, MKB-winstvrijstelling, KIA, FOR, the hours test): **nl-zzp-deductions**. Investment schemes (EIA, MIA, Vamil) and R&D relief (S&O-afdrachtvermindering, aftrek speur- en ontwikkelingswerk) are business matters; route them there or to a specialist.
  - Rates, bands, the full credit calculation and box 3 tax: **nl-income-tax**. People at AOW age and other special groups: **nl-income-tax-special-groups**.
  - The owner-occupied home in depth (bijleenregeling, kapitaalverzekering eigen woning): **netherlands-owner-occupied-home-tax-scheme**.
  - Non-residents and qualifying foreign taxpayers (Wet IB art. 7.8): **nl-cross-border**.
  - Objecting to an assessment: **nl-tax-objection**. Company tax for a BV: **nl-corporate-tax**.

## Rates, bands and thresholds

| Item | Rate or amount | Year | Source |
|---|---|---|---|
| Box 1 bands below AOW age | 8.10% income tax to EUR 38,883 (plus national insurance premiums, combined rate in nl-income-tax); 37.56% to EUR 78,426; 49.50% above | 2026 | Wet IB art. 2.10(1), https://wetten.overheid.nl/BWBR0011353/2026-01-01 ; full detail in nl-income-tax |
| Tariefsaanpassing: income threshold | income from work and home before deductions more than EUR 78,426 (2025: EUR 76,817) | 2026 | Wet IB art. 2.10(2); https://www.belastingdienst.nl/wps/wcm/connect/nl/aftrek-en-kortingen/content/afbouw-tarief-aftrekposten-bij-hoog-inkomen |
| Tariefsaanpassing: percentage | 11.94% (2025: 12.02%), so top-band relief is at most 37.56% (2025: 37.48%) | 2026 | Wet IB art. 2.10(2); same Belastingdienst page Source: https://www.belastingdienst.nl/wps/wcm/connect/nl/aftrek-en-kortingen/content/afbouw-tarief-aftrekposten-bij-hoog-inkomen (tax year 2026) (read 2026-10-31) |
| Eigenwoningforfait (WOZ value) | nil to EUR 12,500; 0.10% to EUR 25,000; 0.20% to EUR 50,000; 0.25% to EUR 75,000; 0.35% to EUR 1,350,000; above: EUR 4,725 plus 2.35% of the excess | 2026 | Wet IB art. 3.112(1) Source: https://www.belastingdienst.nl/wps/wcm/connect/nl/koopwoning/content/hoe-werkt-eigenwoningforfait (tax year 2026) (read 2026-10-31) |
| Eigenwoningforfait 2025, top bands | 0.35% to EUR 1,330,000; above: EUR 4,655 plus 2.35% | 2025 | https://www.belastingdienst.nl/wps/wcm/connect/nl/koopwoning/content/hoe-werkt-eigenwoningforfait |
| Wet Hillen share of (forfait minus home costs) | 71.867% (2025: 76.667%); ends 1 January 2041 | 2026 | Wet IB art. 3.123a(2); https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/prive/woning/eigenwoningforfait/geen_of_een_kleine_eigenwoningschuld/geen_of_een_kleine_eigenwoningschuld |
| New mortgage debt (from 2013): repayment | at least annuity (or linear), fully repaid within 360 months | 2026 | Wet IB art. 3.119a and 3.119c |
| Interest deduction period | at most 360 months; for debt existing before 1 January 2001 counted from that date | 2026 | https://www.belastingdienst.nl/wps/wcm/connect/fisin/fisin2026/eigen_woning_en_restschuld_vroegere |
| Restschuld after a sale between 29 October 2012 and 31 December 2017 | interest deductible for 15 years | 2026 | Wet IB art. 3.120a; same chapter Source: https://www.belastingdienst.nl/wps/wcm/connect/fisin/fisin2026/eigen_woning_en_restschuld_vroegere (tax year 2026) (read 2026-10-31) |
| Care costs: increase (verhoging) | 40% of costs b to h; 113% at AOW age at 1 January; only if drempelinkomen (joint with a whole-year partner) not more than EUR 41,123 (2025: EUR 40,502) | 2026 | Wet IB art. 6.19 with art. 2.10a(1) |
| Care costs: threshold, no whole-year partner | EUR 166 up to EUR 9,680; 1.65% up to EUR 51,411; above: 1.65% of EUR 51,411 (EUR 848) plus 5.75% of the excess | 2026 | Wet IB art. 6.20(1) Source: https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/prive/relatie_familie_en_gezondheid/gezondheid/aftrek_zorgkosten/hoe_berekent_u_uw_aftrek/drempelbedrag_berekenen/drempelbedrag-2026 (tax year 2026) (read 2026-10-31) |
| Care costs: threshold, whole-year partner | first band up to EUR 19,360 with EUR 332; other bands the same | 2026 | Wet IB art. 6.20(2) Source: https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/prive/relatie_familie_en_gezondheid/gezondheid/aftrek_zorgkosten/hoe_berekent_u_uw_aftrek/drempelbedrag_berekenen/drempelbedrag-2026 (tax year 2026) (read 2026-10-31) |
| Care costs: threshold 2025 | EUR 164 up to EUR 9,534; 1.65% up to EUR 50,635; EUR 835 plus 5.75% above (partners: EUR 328 up to EUR 19,068) | 2025 | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/prive/relatie_familie_en_gezondheid/gezondheid/aftrek_zorgkosten/hoe_berekent_u_uw_aftrek/drempelbedrag_berekenen/drempelbedrag-2025 |
| Care costs: travel by car (treatment and sick visits) | EUR 0.23 per km plus parking, ferry and toll, in the law as it stands; the Belastingplan 2027 bill raises it to EUR 0.25 back to 1 January 2026, and the Belastingdienst already uses EUR 0.25 | 2026 | Wet IB art. 6.17(6); Kamerstuk 37022 nr. 2, art. I part H and art. LXIII(1)(a) |
| Care costs: cannot walk 100 metres | flat EUR 925 a year | 2026 | Wet IB art. 6.17(7) |
| Care costs: extra clothing and bedding | flat EUR 330, or EUR 825 if extra spend is at least EUR 660 above normal | 2026 | https://www.belastingdienst.nl/wps/wcm/connect/fisin/fisin2026/aftrek_specifieke_zorgkosten |
| Care costs: extra household help counts above | 0% of verzamelinkomen up to EUR 39,701; 1% to EUR 59,549; 2% to EUR 79,387; 3% above | 2026 | Wet IB art. 6.17(3) |
| Tegemoetkoming specifieke zorgkosten | paid only if more than EUR 18 | 2026 | Fiscale informatie 2026 ch. 17.5 (care chapter above) Source: https://www.belastingdienst.nl/wps/wcm/connect/fisin/fisin2026/aftrek_specifieke_zorgkosten (tax year 2026) (read 2026-10-31) |
| Ordinary gifts: floor | the higher of EUR 60 and 1% of drempelinkomen | 2026 | Wet IB art. 6.39(1) |
| Ordinary gifts: ceiling | 10% of drempelinkomen, raised by the cultural uplift | 2026 | Wet IB art. 6.39(1), 6.39a(3) |
| Gifts in kind needing a valuation | above EUR 10,000 a year (whole-year partners EUR 20,000) | 2026 | Wet IB art. 6.38(2),(5) and 6.39(2),(4) |
| Periodic gifts: cap | EUR 1,500,000 a year in total (partners together) | 2026 | Wet IB art. 6.38(4),(5) Source: https://www.belastingdienst.nl/wps/wcm/connect/fisin/fisin2026/aftrek_giften (tax year 2026) (read 2026-10-31) |
| Cultural ANBI uplift | 25% of the gift, at most EUR 1,250 (partners together) | 2026 | Wet IB art. 6.39a Source: https://www.belastingdienst.nl/wps/wcm/connect/fisin/fisin2026/aftrek_giften (tax year 2026) (read 2026-10-31) |
| Volunteer car costs waived | EUR 0.23 per km in the law as it stands; the Belastingplan 2027 bill raises it to EUR 0.25 back to 1 January 2026 | 2026 | Wet IB art. 6.36(2); Kamerstuk 37022 nr. 2, art. I part I |
| Weekend costs, disabled person 21 or older | EUR 13 a day; EUR 0.23 per km by car (the Belastingdienst chapter says EUR 0.25); half each if both partners claim for the same person | 2026 | Uitvoeringsregeling IB 2001 art. 40, text in force from 17 January 2026, https://wetten.overheid.nl/BWBR0012031/2026-01-17 |
| General tax credit (algemene heffingskorting) | EUR 3,115, less 6.398% of verzamelinkomen above EUR 29,736 | 2026 | Wet IB art. 8.10(2) Source: https://www.belastingdienst.nl/wps/wcm/connect/fisin/fisin2026/heffingskortingen (tax year 2026) (read 2026-10-31) |
| Labour credit (arbeidskorting) | at most EUR 5,685, less 6.51% of work income above EUR 45,592 | 2026 | Wet IB art. 8.11 |
| IACK | 11.45% of work income above EUR 6,239, at most EUR 3,032 | 2026 | Wet IB art. 8.14a(2) Source: https://www.belastingdienst.nl/wps/wcm/connect/fisin/fisin2026/heffingskortingen (tax year 2026) (read 2026-10-31) |
| Elderly / single elderly / young disabled credit | EUR 2,067 (less 15% above EUR 46,002) / EUR 540 / EUR 923 | 2026 | Wet IB art. 8.17, 8.18, 8.16a |
| Green investment credit | 0.1% of the exempt green investments | 2026 | Wet IB art. 8.19(2) |
| Box 3 tax-free allowance | EUR 59,357 per person (2025: EUR 57,684) | 2026 | Wet IB art. 5.5; https://www.belastingdienst.nl/wps/wcm/connect/nl/box-3/content/heffingsvrij-vermogen |
| Green investments exempt in box 3 | EUR 26,715 (partners EUR 53,430) | 2026 | Wet IB art. 5.13(1) Source: https://www.belastingdienst.nl/wps/wcm/connect/fisin/fisin2026/heffingskortingen (tax year 2026) (read 2026-10-31) |
| Late-filing penalty (verzuimboete) | EUR 469 (Belastingdienst standard amount); statutory maximum EUR 6,709, used for repeat lateness | 2026 | AWR art. 67a(1) (maximum); https://www.belastingdienst.nl/wps/wcm/connect/nl/belastingaangifte/content/wat-gebeurt-er-als-ik-geen-aangifte-doe-of-te-laat-of-onvolledig |

## The taxable base

**Order of the calculation.** Box 1 income (work, then the own-home balance), then personal deductions, then tax per box, then the tariefsaanpassing, then credits. Personal deductions reduce box 1 income first, then box 3, then box 2, each not below nil; care costs are used first (Wet IB art. 6.2). What is left is carried to later years and fixed by the inspector in an appealable decision (art. 6.2a). Deductions count in the year paid, set off or made available (art. 6.40).

**Drempelinkomen.** The care-cost and gift tests use verzamelinkomen before personal deductions (boxes 1, 2 and 3 together); with a whole-year partner, both incomes added (art. 6.19, 6.20, 6.39).

### Own home (eigen woning)

- **Deductible:** interest on the eigenwoningschuld (debt to buy, improve or maintain the main residence, or buy off ground lease), financing costs (advice, arrangement and notary fees for the mortgage deed, NHG fee), and periodic ground-lease payments (erfpacht, opstal, beklemming) (Wet IB art. 3.120). Money borrowed for anything else is a box 3 debt. For loans taken out before 2013, arrangement fees count only up to 1.5% of the debt and EUR 3,630. Penalty interest (boeterente) paid on repaying or refinancing is deductible if the loan belongs to the eigenwoningschuld ([Fiscale informatie 2026 ch. 10](https://www.belastingdienst.nl/wps/wcm/connect/fisin/fisin2026/eigen_woning_en_restschuld_vroegere)).
- **Debt from 2013:** interest is deductible only if the loan is repaid at least annuity (linear also qualifies) within 360 months, by contract and in fact (art. 3.119a, 3.119c). Months used on an earlier repayment-bound loan come off the 360. **Debt held at 31 December 2012** keeps the old rules and needs no repayment. An increase after 2012 is new debt and must meet the test.
- **Loan from family, a BV, an employer or a foreign lender:** deductible, but the return must carry the loan data (start date, term, amount, repayment method, rate, lender's name, address and BSN or RSIN) (art. 3.119g).
- **Prepaid interest:** contractually agreed prepayment in 2026 for a period up to 1 July 2027 is deductible in 2026 in full. A longer prepayment is spread over the years it covers. A voluntary payment for 2027 counts in 2027 and is a box 3 asset on 1 January 2027.
- **Home not lived in:** a new home empty or being built stays an own home if the client expects to move in within 3 years after the end of the year. An old home empty and for sale stays an own home in the year it was left and the 3 years after; let months fall out of box 1.
- **Eigenwoningforfait:** the WOZ value for the year times the band rate (art. 3.112), added to box 1, for the period the address is the registered home.
- **Wet Hillen:** if the forfait is more than the deductible costs, 71.867% of the difference is deducted in 2026 (art. 3.123a). Prepaid or late-paid interest is allocated to the year it covers for this test. Partners are combined. With more than one own home, the income and costs of all homes are taken together ([Belastingdienst, Wet Hillen](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/prive/woning/eigenwoningforfait/geen_of_een_kleine_eigenwoningschuld/geen_of_een_kleine_eigenwoningschuld)). The Belastingdienst says the deduction can be refused where interest was prepaid or paid late, or the loan is from the employer.

### Tariefsaanpassing

If taxable box 1 income plus the "base-reducing items" is more than EUR 78,426, tax is raised by 11.94% of the lower of (a) that excess and (b) the items deducted (Wet IB art. 2.10(2)). Items: entrepreneur deduction, MKB-winstvrijstelling, the tbs exemption, own-home costs, and all personal deductions (art. 2.10(3)). Effect: top-band relief at 37.56%. The return software applies it; the assessment shows "tariefsaanpassing".

### Alimony (onderhoudsverplichtingen)

Deductible (Wet IB art. 6.3): periodic payments under a family-law duty, except to relatives in the direct line or second degree, so partner alimony to an ex-spouse or a spouse living permanently apart; lump sums buying off partner alimony paid to the **former** spouse; recovered social assistance; pension-rights and annuity settlements on divorce; old-age pension paid on as partner alimony. A lump sum is not deductible if paid before the court dissolved the marriage, or if the client lives unmarried with the ex-partner. Not deductible: child maintenance (a family-law duty to a relative in the direct line), lawyer and court costs to reduce or end partner alimony, a buy-out through an annuity whose premiums were already deducted (art. 6.4; [Fiscale informatie 2026 ch. 19](https://www.belastingdienst.nl/wps/wcm/connect/fisin/fisin2026/aftrek_betaalde_partneralimentatie)). Evidence: the arrangement (court or agreed) and proof of payment.

**Ex-partner stays in the co-owned home** under an alimony arrangement: for 2 years the home stays an own home; the client deducts interest on their share and also deducts their share of the forfait as alimony. After 2 years the share goes to box 3, but the forfait share stays deductible as alimony. Interest paid on the ex's share is deductible as alimony (Fiscale informatie 2026 ch. 19).

### Specific care costs (specifieke zorgkosten)

- **For whom (art. 6.16):** the client, the partner, children under 27, severely disabled household members aged 27 or over, and care-dependent parents, brothers or sisters living with the client.
- **What (art. 6.17):** medical and surgical help (doctor; paramedic on a doctor's prescription or a listed paramedic with a statement), travel for treatment, other transport if the client cannot walk 100 metres (EUR 925), prescribed medicines, aids used mainly by sick or disabled people, extra household help (with dated invoices naming the helper), a prescribed diet (fixed amounts from the diet list), extra clothing and bedding, and travel to visit a household member nursed more than 1 month more than 10 km away.
- **Never (art. 6.17(2), 6.18):** glasses, contact lenses and other vision aids, eye laser treatment replacing them, mobility scooters, wheelchairs, home adaptations, insurance premiums, CAK and Zvw own contributions, the own risk (eigen risico), and care covered by the basic Zvw package. Only the part the client bears after any reimbursement counts, and a reimbursement the client could get counts even if not claimed, whoever would pay it. Also never: a payment due for basic-package care from a non-contracted provider; mental-health and dyslexia care for anyone under 18; costs to prevent illness (travel vaccinations are the exception, for any kind of trip). Prism glasses that do not support vision are deductible ([Fiscale informatie 2026 ch. 17](https://www.belastingdienst.nl/wps/wcm/connect/fisin/fisin2026/aftrek_specifieke_zorgkosten)).
- **Aids and transport examples:** insoles, prostheses, assistance, signal, guide and therapy dogs; a hearing aid only for the extra price of a dearer device chosen because it works better for the client. Travel for treatment by bus or ambulance counts at the cost paid, less reimbursements ([Fiscale informatie 2026 ch. 17](https://www.belastingdienst.nl/wps/wcm/connect/fisin/fisin2026/aftrek_specifieke_zorgkosten)).
- **Increase and threshold:** see the rates table. The increase does not apply to medical help (a) or to visit travel (i).
- **Low income:** if the deduction leaves credits unused, the Belastingdienst pays a separate tegemoetkoming automatically.

### Gifts (giften)

- **Ordinary gifts (andere giften):** to an ANBI or an SBBI support foundation (art. 6.35); provable in writing; nothing received in return (buying a cookbook from a patients' association is not a gift); not cash (art. 6.37); only the part above the floor counts, up to the ceiling (art. 6.39). A gift to an SBBI itself is not deductible.
- **Periodic gifts:** fixed equal payments at least yearly for 5 or more years, to an ANBI or a qualifying association (25 or more members, full legal capacity, not liable to corporate tax, based in the EU or a listed state), under a notarial or private deed (art. 6.33, 6.34, 6.38(1)). No floor, no 10% ceiling. The deed may end the gift early on loss of status, bankruptcy, the donor's disability or unemployment, or death (art. 6.34, 6.38(6),(7)).
- **Cultural ANBI:** the gift is raised by 25%, at most EUR 1,250, and the ordinary-gift ceiling rises by the same amount (art. 6.39a).
- **Volunteers:** a waived allowance counts if the ANBI issued a statement, the volunteer had a right to it, the ANBI could pay and the volunteer was free to take it; waived actual costs count, car at EUR 0.23 per km (art. 6.36; see the rates table for the pending EUR 0.25).
- **ANBI status withdrawn with retroactive effect:** a gift made before the withdrawal stays deductible (gifts chapter). Check status with "ANBI opzoeken".

### Weekend costs for severely disabled persons

For a severely disabled child, brother or sister, or a person under the client's mentorship or curatorship, aged 21 or over, who usually lives in an institution and is cared for by the client at weekends or holidays (art. 6.25). EUR 13 a day (pick-up and drop-off days count) plus EUR 0.23 per km by car on the home-to-institution distance, per person, less reimbursements (Uitvoeringsregeling IB 2001 art. 40(1)). If both partners claim for the same person, each takes half (art. 40(2)). From the 21st birthday only. The Belastingdienst chapter uses EUR 0.25 per km; if the regulation is amended back to 1 January 2026, use EUR 0.25.

### Study costs

The deduction for study costs (afdeling 6.7) was repealed from 1 January 2022. For 2026 one remnant applies: a performance grant (prestatiebeurs) from before 1 July 2015, an extended diploma term for special reasons, and conversion of that grant to a loan in 2026, so only study years 2010/2011 to 2014/2015; then earlier blocked study costs can be claimed (Fiscale informatie 2026 ch. 18). Anything else: no deduction. A course for a self-employed client's business is a business cost: nl-zzp-deductions.

### Credits and box 3

Credits reduce tax, not income. Employers and benefits agencies already apply the general, labour, elderly and young-disabled credits; IACK and the green investment credit are claimed in the return. The figures are in the rates table; the full computation is in nl-income-tax. Box 3: debt that is not own-home debt is a box 3 debt; under the actual-return route the allowance does not apply (nl-income-tax).

## Deadlines and filing

- **Who files:** anyone who received an invitation letter (aangiftebrief) must file. Without a letter, the client checks whether a return is due and files as soon as possible if it is.
- **How:** online in Mijn Belastingdienst with DigiD. The online return computes the forfait, Hillen, thresholds, increases and the tariefsaanpassing.
- **When:** by the date in the letter, usually 1 May 2027 for the 2026 return. With an extension, the date in the confirmation letter, usually 1 September 2027.
- **2025 returns** still open: use the 2025 figures in the rates table and the 2025 Fiscale informatie for credits.

## Penalties and interest

- **Late filing:** reminder, then a demand (aanmaning) with 10 working days to file. After that a verzuimboete, normally EUR 469; the law allows up to EUR 6,709 (AWR art. 67a(1)), which the Belastingdienst uses for repeat lateness. The Belastingdienst can also stop paying allowances and the provisional refund.
- **No return at all:** an estimated assessment plus the penalty.
- **Interest:** late filing brings belastingrente; the rate is in nl-income-tax.
- **Wrong return on purpose:** a vergrijpboete, also on an additional assessment.

## Cross-border points

- A non-resident claims own-home costs and personal deductions only as a qualifying foreign taxpayer (Wet IB art. 7.8), and only to the extent they cannot be taken in the state of residence (art. 7.8(4)). For a Belgian resident who is not a qualifying foreign taxpayer, the Belastingdienst applies a pro rata to the weekend-cost deduction (Fiscale informatie 2026 ch. 20). Route these cases to nl-cross-border.
- Periodic gifts to associations in other EU states can qualify (art. 6.33(c)); gifts to foreign institutions need ANBI registration.
- Loans from a foreign bank carry the loan-data duty (art. 3.119g).

## Worked examples

**Example 1: mortgage interest with the tariefsaanpassing.** Resident, below AOW age, no partner. WOZ value EUR 400,000; interest EUR 12,000 on a qualifying annuity loan; salary EUR 95,000. Forfait 0.35% x 400,000 = EUR 1,400. Taxable box 1 income 95,000 + 1,400 - 12,000 = EUR 84,400. Test: 84,400 + 12,000 - 78,426 = EUR 17,974, positive. The adjustment applies to the lower of 12,000 and 17,974, so EUR 12,000. Extra tax 11.94% x 12,000 = EUR 1,432.80. The interest gets relief at 37.56%.

```oa-check
name: Mortgage interest with the 2026 tariefsaanpassing
inputs:
  woz: 400000
  interest: 12000
  salary: 95000
steps:
  - forfait: woz * 0.0035
  - taxable_box1: salary + forfait - interest
  - test_amount: taxable_box1 + interest - 78426
  - adj_base: min(interest, max(test_amount, 0))
  - extra_tax: adj_base * 0.1194
expected:
  forfait: 1400.00
  taxable_box1: 84400.00
  test_amount: 17974.00
  extra_tax: 1432.80
```

**Example 2: care costs and gifts together (edge: cash gift, cultural uplift, periodic gift).** Resident, below AOW age, no partner, drempelinkomen EUR 35,000. Care: prescribed medicines EUR 800 and dentist EUR 1,500, nothing reimbursable, nothing under the own risk. Gifts: EUR 600 by transfer to an ANBI, EUR 400 to a cultural ANBI, EUR 100 cash to a street collection, EUR 1,200 under a 5-year private deed to an ANBI.

Care: the income is not above EUR 41,123, so the medicines get the 40% increase (EUR 320); the dentist is medical help and gets none. Total 2,620. Threshold 1.65% x 35,000 = EUR 577.50. Deduction EUR 2,042.50. Gifts: cash is out. Uplift 25% x 400 = EUR 100. Ordinary gifts counted 600 + 400 + 100 = EUR 1,100. Floor: the higher of EUR 60 and 1% x 35,000 = EUR 350. Excess EUR 750. Ceiling 10% x 35,000 + 100 = EUR 3,600, not reached. Periodic gift EUR 1,200 in full. Gifts EUR 1,950. Total personal deductions EUR 3,992.50.

```oa-check
name: Care costs and gifts, drempelinkomen EUR 35,000 (2026)
inputs:
  drempelinkomen: 35000
  medicines: 800
  dentist: 1500
  gift_anbi: 600
  gift_cultural: 400
  gift_cash: 100
  periodic: 1200
steps:
  - increase: medicines * 0.40
  - care_total: medicines + increase + dentist
  - care_threshold: drempelinkomen * 0.0165
  - care_deduction: max(care_total - care_threshold, 0)
  - uplift: min(gift_cultural * 0.25, 1250)
  - ordinary: gift_anbi + gift_cultural + uplift
  - floor: max(60, drempelinkomen * 0.01)
  - ceiling: drempelinkomen * 0.10 + uplift
  - ordinary_deduction: min(max(ordinary - floor, 0), ceiling)
  - gift_deduction: ordinary_deduction + periodic
  - total: care_deduction + gift_deduction
expected:
  care_deduction: 2042.50
  ordinary_deduction: 750.00
  gift_deduction: 1950.00
  total: 3992.50
```

## Ask the client first

1. **Year, residence and partner.** Which year (2026 or an open 2025 return)? Resident all year? A fiscal partner all year, or part-year with the choice to be partners all year? These set the figures, the joint thresholds and the split.
2. **The home.** Main residence? WOZ value for the year; the lender's annual statement; when each loan started, any increase after 2012, annuity or linear, months used; any loan from family, a BV, an employer or abroad; moved, sold, let or separated?
3. **Income before deductions.** Is income from work and home before deductions above EUR 78,426? Is drempelinkomen at or below EUR 41,123? Did the client or partner reach AOW age by 1 January?
4. **Care costs.** What was paid, for whom, and what was or could be reimbursed? Anything under the own risk or a CAK contribution?
5. **Gifts and alimony.** Recipient's ANBI or cultural ANBI status; how paid (no cash); a deed for periodic gifts; alimony to an ex-partner or to children, periodic or lump sum, and the written arrangement.
6. **Business income.** If the client is self-employed, run nl-zzp-deductions first.

## Sources

| Source | URL | Read on |
|---|---|---|
| Wet inkomstenbelasting 2001, version 1 January 2026 (art. 2.10, 2.10a, 3.112, 3.119a-3.123a, 5.5, 5.13, 6.1-6.40, 7.8, 8.10-8.19) | https://wetten.overheid.nl/BWBR0011353/2026-01-01 | 2026-10-24 |
| Wet inkomstenbelasting 2001, version in force from 21 February 2026 (art. 6.17(6) checked) | https://wetten.overheid.nl/BWBR0011353/2026-02-21 | 2026-10-24 |
| Uitvoeringsregeling inkomstenbelasting 2001, art. 40 (weekend costs), text in force from 17 January 2026 | https://wetten.overheid.nl/BWBR0012031/2026-01-17 | 2026-10-24 |
| Wet inkomstenbelasting 2001, art. 6.17 change history (pending bill 37022 listed) | https://wetten.overheid.nl/BWBR0011353/2026-02-21/0/Hoofdstuk6/Afdeling6.5/Artikel6.17/informatie | 2026-10-24 |
| Belastingplan 2027 bill, Kamerstuk 37022 nr. 2 (art. I parts H and I, art. II part G, art. LXIII) | https://zoek.officielebekendmakingen.nl/kst-37022-2.html | 2026-10-24 |
| Algemene wet inzake rijksbelastingen, art. 67a | https://wetten.overheid.nl/BWBR0002320/2026-01-01 | 2026-10-24 |
| Belastingdienst, tariefsaanpassing aftrekposten | https://www.belastingdienst.nl/wps/wcm/connect/nl/aftrek-en-kortingen/content/afbouw-tarief-aftrekposten-bij-hoog-inkomen | 2026-10-31 |
| Belastingdienst, eigenwoningforfait 2026 and 2025 | https://www.belastingdienst.nl/wps/wcm/connect/nl/koopwoning/content/hoe-werkt-eigenwoningforfait | 2026-10-31 |
| Belastingdienst, Wet Hillen | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/prive/woning/eigenwoningforfait/geen_of_een_kleine_eigenwoningschuld/geen_of_een_kleine_eigenwoningschuld | 2026-10-24 |
| Fiscale informatie 2026 ch. 10, own home and restschuld | https://www.belastingdienst.nl/wps/wcm/connect/fisin/fisin2026/eigen_woning_en_restschuld_vroegere | 2026-10-31 |
| Fiscale informatie 2026 ch. 16, gifts | https://www.belastingdienst.nl/wps/wcm/connect/fisin/fisin2026/aftrek_giften | 2026-10-31 |
| Fiscale informatie 2026 ch. 17, specific care costs | https://www.belastingdienst.nl/wps/wcm/connect/fisin/fisin2026/aftrek_specifieke_zorgkosten | 2026-10-31 |
| Belastingdienst, care-cost threshold 2026 | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/prive/relatie_familie_en_gezondheid/gezondheid/aftrek_zorgkosten/hoe_berekent_u_uw_aftrek/drempelbedrag_berekenen/drempelbedrag-2026 | 2026-10-31 |
| Belastingdienst, care-cost threshold 2025 | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/prive/relatie_familie_en_gezondheid/gezondheid/aftrek_zorgkosten/hoe_berekent_u_uw_aftrek/drempelbedrag_berekenen/drempelbedrag-2025 | 2026-10-24 |
| Fiscale informatie 2025 ch. 17, care costs (2025 increase limit) | https://www.belastingdienst.nl/wps/wcm/connect/fisin/fisin2025/aftrek_specifieke_zorgkosten | 2026-10-24 |
| Fiscale informatie 2026 ch. 18, study costs | https://www.belastingdienst.nl/wps/wcm/connect/fisin/fisin2026/aftrek_studiekosten | 2026-10-24 |
| Fiscale informatie 2026 ch. 19, partner alimony | https://www.belastingdienst.nl/wps/wcm/connect/fisin/fisin2026/aftrek_betaalde_partneralimentatie | 2026-10-24 |
| Fiscale informatie 2026 ch. 20, weekend costs for severely disabled persons | https://www.belastingdienst.nl/wps/wcm/connect/fisin/fisin2026/aftrek_voor_tijdelijk_verblijf_thuis | 2026-10-24 |
| Fiscale informatie 2026 ch. 21, tax credits | https://www.belastingdienst.nl/wps/wcm/connect/fisin/fisin2026/heffingskortingen | 2026-10-31 |
| Belastingdienst, box 3 tax-free allowance | https://www.belastingdienst.nl/wps/wcm/connect/nl/box-3/content/heffingsvrij-vermogen | 2026-10-24 |
| Belastingdienst, late or missing return | https://www.belastingdienst.nl/wps/wcm/connect/nl/belastingaangifte/content/wat-gebeurt-er-als-ik-geen-aangifte-doe-of-te-laat-of-onvolledig | 2026-10-24 |

Pending law: the Belastingplan 2027 bill (Kamerstuk 37022, sent to the Tweede Kamer on 29 September 2026, not yet enacted on 24 October 2026) raises the car rate in Wet IB art. 6.17(6) and 6.36(2) from EUR 0.23 to EUR 0.25 with effect back to 1 January 2026 (art. I parts H and I, art. LXIII(1)(a)), and repeals the specific care-cost deduction (afdeling 6.5) from 1 January 2028 (art. II part G). The "repeal without commencement date" notes on wetten.overheid.nl for art. 6.17 to 6.20 refer to this bill. Recheck the car rates once the Staatsblad text is published.

Not yet confirmed: (0) the older version said a lump-sum buy-out of ground lease and building insurance are not own-home costs, and that a diet not on the diet list gives no deduction; the Belastingdienst chapters read on 27 October 2026 did not state these in words, so they are left out of the rules; (1) whether the Uitvoeringsregeling IB 2001 art. 40 weekend-cost km rate will also be raised to EUR 0.25 for 2026 (the Belastingdienst already says so; the regulation in force says EUR 0.23); (2) a STAP-budget or other non-tax successor to the study-cost deduction: no official page read, so not stated; (3) the belastingrente rate for income tax: left to nl-income-tax.

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
