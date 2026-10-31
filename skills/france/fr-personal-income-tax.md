---
name: fr-personal-income-tax
description: >
  French personal income tax (impôt sur le revenu, IR) for a household resident in
  France: the income of 2025, declared and taxed in 2026, under the 2026 scale set by
  the 2026 finance law (0%, 11%, 30%, 41%, 45%; bands EUR 11,600, 29,579, 84,577,
  181,917 per share). Covers the family quotient and its caps, the décote, category
  allowances, deductions, reductions and credits, the CEHR and the CDHR 20% minimum
  rate, withholding at source (rates, default grid, modulation), the flat tax on
  investment income (30% or 31.4%, depending on the income and collection date), filing deadlines by
  département, and penalties. Trigger on "impôt sur le revenu", "barème 2026",
  "quotient familial", "décote", "CEHR", "CDHR", "prélèvement à la source", "taux
  PAS", "déclaration 2042", "flat tax 31,4", "TMI". Out of scope: self-employed
  results in depth (fr-income-tax), social contributions (fr-social-contributions),
  gains on securities (fr-capital-gains), rental income (fr-rental-income), crypto
  (fr-crypto-tax), leaving France (leaving-france-exit-tax), audits (fr-tax-audit).
version: "1.10"
jurisdiction: FR
tax_year: 2026
last_updated: 2026-10-31
authored_by: Michael Cutajar and the OpenAccountants team
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# France: personal income tax for a household (impôt sur le revenu)

This skill computes French personal income tax (impôt sur le revenu, IR) for a household (foyer fiscal) resident in France. Every figure was read on an official French page on 24 October 2026, unless the Sources table says otherwise.

Two facts about the years, stated once:

- **The return filed in spring 2026 taxes the income of 2025.** The scale used for it is the one in CGI art. 197 as amended by the 2026 finance law, loi n° 2026-103 of 19 February 2026 (art. 4), which raised the bands and the linked thresholds by 0.9%. This is "the 2026 scale": it applies to the tax due in 2026 on the income of 2025 and later years, until a new finance law changes it.
- **No scale for the income of 2026 has been enacted yet.** The income of 2026 will be declared in spring 2027 under whatever the 2027 finance law sets. Until then, use the 2026 scale only as an estimate for 2026 income, and say so. The CDHR applies again under its enacted 2026 wording. The investment social-levy increase has separate commencement rules for assessed income from 2025 and payments taxed at source from 1 January 2026; see Social levies below.

Self-employed results in depth are in `fr-income-tax`; social contributions in `fr-social-contributions`; gains on securities in `fr-capital-gains`; rental income in `fr-rental-income`; crypto-assets in `fr-crypto-tax`; leaving France in `leaving-france-exit-tax`; residence and treaty questions in `fr-cross-border`; audits in `fr-tax-audit`.

## Who this applies to

- **Residents.** A person domiciled in France for tax purposes under CGI art. 4 B is taxed on worldwide income. The scale in CGI art. 197, I applies to them.
- **The household is the unit.** One return per foyer fiscal: a single person, or a married or Pacs couple taxed jointly, plus their dependants. Marital status is taken on 31 December, subject to the statutory marriage, qualifying separation/divorce/Pacs dissolution and death-year rules below. Dependants are counted on 1 January, or on 31 December if their number rose during the year.
- **Year of marriage or Pacs.** One joint return for the whole year, unless the couple opts, for that year only, for two separate returns. A couple already in a Pacs who marry stay taxed jointly and cannot opt.
- **Year of divorce, legally qualifying separation or end of a Pacs.** Under CGI art. 6(4)/(6), separate full-year returns apply on divorce/Pacs dissolution or where spouses meet one of these grounds: separate-property status and separate roofs; authorised separate residences during divorce/judicial-separation proceedings; or abandonment of the marital home with each spouse having separate income. Mere physical separation alone does not establish a ground. Each declares their own income and the supported share of common income (equal halves if not proved otherwise). The "living alone" case T/L test is judged on 31 December.
- **Year a spouse dies.** Joint taxation up to the date of death, then the survivor alone for the rest of the year.
- **Non-residents** are taxed only on French-source income, at a minimum rate (see Cross-border points). The CDHR does not apply to them.
- **Out of this skill:** part-year residents and people with two possible tax homes (refer); the IFI wealth tax; gift and inheritance duties; the PUMa health contribution.

## Rates, bands and thresholds

| Item | Rate or amount | Year | Source |
|---|---|---|---|
| Scale, 0% band, per share (CGI art. 197, I-1) | Up to EUR 11,600 | Income of 2025, taxed 2026 | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000053542636/2026-10-24 |
| Scale, 11% band | EUR 11,600 to EUR 29,579 | Income of 2025 | same |
| Scale, 30% band | EUR 29,579 to EUR 84,577 | Income of 2025 | same |
| Scale, 41% band | EUR 84,577 to EUR 181,917 | Income of 2025 | same |
| Scale, 45% band | Above EUR 181,917 | Income of 2025 | same |
| Uprating of bands and linked thresholds (loi n° 2026-103, art. 4) | 0.9% | Income of 2025 | https://bofip.impots.gouv.fr/bofip/14954-PGP.html |
| Family-quotient cap, each extra half share (CGI art. 197, I-2) | EUR 1,807 (half that per quarter share) | Income of 2025 | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000053542636/2026-10-24 |
| Cap on the full share for the first child of a parent living alone (case T) | EUR 4,262 (EUR 2,131 per half share where the children are in alternating residence) | Income of 2025 | same |
| Cap on the half share of case L (and the other cases of CGI art. 195, 1-a, b, e) | EUR 1,079 | Income of 2025 | same |
| Extra tax reduction where an invalidity or veteran half share is capped | Up to EUR 1,801 per qualifying half share, limited by the cap-caused increase; EUR 900.50 for the specified shared-child quarter | Income of 2025 | same |
| Extra tax reduction, qualifying widowed person with dependants after the death year, capped extra share; limited to the increase caused by the cap | EUR 2,011 | Income of 2025 | same |
| Décote, fixed amount, single, divorced or widowed (CGI art. 197, I-4-a) | EUR 897, less 45.25% of the gross tax | Income of 2025 | same |
| Décote, fixed amount, couple taxed jointly | EUR 1,483, less 45.25% of the gross tax | Income of 2025 | same |
| Gross tax below which the décote applies | EUR 1,982 single; EUR 3,277 couple | Income of 2025 | https://bofip.impots.gouv.fr/bofip/2495-PGP.html/identifiant=BOI-IR-LIQ-20-20-30-20260407 |
| Overseas abatement on the tax (CGI art. 197, I-3) | 30%, max EUR 2,450 (Guadeloupe, Martinique, La Réunion); 40%, max EUR 4,050 (Guyane, Mayotte) | Income of 2025 | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000053542636/2026-10-24 |
| CEHR (CGI art. 223 sexies), single person | 3% on reference income EUR 250,000 to 500,000; 4% above | 2025 and 2026 | https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006069577/LEGISCTA000025049019/2026-10-24 |
| CEHR, couple taxed jointly | 3% on EUR 500,000 to 1,000,000; 4% above | 2025 and 2026 | same |
| CDHR minimum rate (CGI art. 224, III) | 20% of the CDHR reference income | Income of 2025 and of 2026 | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000053561826/2026-10-24 |
| CDHR liability threshold (CGI art. 224, I) | Above EUR 250,000 single; above EUR 500,000 couple | Income of 2025 and of 2026 | same |
| CDHR décote zone (CGI art. 224, V) | Reference income up to EUR 330,000 single, EUR 660,000 couple; factor 82.5% | Income of 2025 and of 2026 | same |
| CDHR additions to taxes already paid (CGI art. 224, III-2°) | EUR 1,500 per dependant; EUR 12,500 per couple | Income of 2025 and of 2026 | same |
| CDHR advance for the income of 2025, paid 1 to 15 December 2025 | 95% of the estimated contribution | Income of 2025 | https://www.impots.gouv.fr/actualite/contribution-differentielle-sur-les-hauts-revenus-cdhr |
| Flat tax, income tax part (CGI art. 200 A, 1-B-1°) | 12.8% | 2025 and 2026 | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000053546896/2026-10-24 |
| Social levies on general investment income collected at source under CSS art. L136-7 during 2025 (CSG 9.2%, CRDS 0.5%, solidarity levy 7.5%) | 17.2% total | Source-collected payments in 2025 | https://www.service-public.gouv.fr/particuliers/vosdroits/F2329 |
| CSG on general investment and patrimony income (CSS art. L136-8, I-2°; LFSS 2026, loi n° 2025-1403 art. 12 II) | 10.6%, so 18.6% total levies | L136-6 assessed income from 2025; L136-7 source-collected payments from 1 January 2026, subject to the statutory exceptions below | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000054336623/2026-10-24 |
| CSG kept at 9.2% (CSS art. L136-8, IV): rental income, gains on real property, and the PEL, CEL and life-insurance products covered by IV | 17.2% total | Protected categories; check the product and applicable collection rules | same, and https://www.service-public.gouv.fr/particuliers/vosdroits/F2329 |
| Flat tax on dividends and interest, total (12.8% plus levies) | 30% where the levies are 17.2%; 31.4% where they are 18.6% | For general L136-7 source-collected dividends: 30% in 2025; 31.4% from 1 January 2026. Assessed L136-6 income follows its separate commencement rule | computed from the two rows above |
| Dividend allowance, only if the household opts for the scale | 40% | 2025 | https://www.service-public.gouv.fr/particuliers/vosdroits/F2613 |
| Deductible CSG, income taxed at the scale | 6.8% | Income of 2025 | https://www.impots.gouv.fr/www2/fichiers/documentation/brochure/ir_2026/pdf_som/12-charges_ded_rev_225a236.pdf |
| Salary deduction for expenses (CGI art. 83, 3°) | 10%, min EUR 509, max EUR 14,555 per person; never more than the relevant declared remuneration | Income of 2025 | https://bofip.impots.gouv.fr/bofip/10855-PGP.html/identifiant=BOI-BAREME-000035-20260217 |
| Pension allowance (CGI art. 158, 5-a) | 10%, min EUR 454 per pensioner, max EUR 4,439 per household | Income of 2025 | https://www.impots.gouv.fr/www2/fichiers/documentation/brochure/ir_2026/pdf_som/aide_memoire.pdf |
| Micro-BIC allowance, sales | 71% (min EUR 305) | Income of 2025 | https://entreprendre.service-public.gouv.fr/vosdroits/F23267 |
| Micro-BIC allowance, services including eligible long-term furnished letting | 50% (min EUR 305) | Income of 2025 | same |
| Micro-BNC allowance | 34% (min EUR 305) | Income of 2025 | same |
| Micro allowance, classified tourist lets and chambres d'hôtes / unclassified tourist lets | 50% / 30% | Income of 2025 | same |
| Micro turnover limits, sales / services | EUR 188,700 / EUR 77,700 (income of 2025); EUR 203,100 / EUR 83,600 (income of 2026) | 2025 and 2026 | same |
| Micro limit, unclassified tourist lets | EUR 15,000 | 2025 and 2026 | same |
| Micro limit, long-term furnished lets and classified tourist lets or chambres d'hôtes (services limit) | EUR 77,700 (income of 2025); EUR 83,600 (income of 2026) | 2025 and 2026 | same |
| Micro flat payment option, household RFR of year N-2 must not exceed the stated ceiling (2.5-part example as published) | EUR 29,315 for 1 part; EUR 58,630 for 2 parts; EUR 87,945 for 3 parts; DGFiP’s 2.5-part example requires RFR below EUR 73,288 | Option for 2026; RFR of 2024 | https://www.impots.gouv.fr/professionnel/questions/en-tant-que-micro-entrepreneur-sous-quelles-conditions-puis-je-opter-pour-l |
| Micro flat payment option, following year | EUR 29,579 for 1 part; EUR 59,158 for 2 parts; EUR 88,737 for 3 parts. For 2.5 parts the exact product is EUR 73,947.50, while DGFiP’s published test is RFR below EUR 73,948 | Option for 2027; RFR of 2025 | https://www.impots.gouv.fr/professionnel/questions/en-tant-que-micro-entrepreneur-sous-quelles-conditions-puis-je-opter-pour-l |
| Micro flat payment rates | 1% sales, catering and lodging excluding furnished letting; 1.7% other eligible BIC, including classified furnished letting; 2.2% BNC | 2026 | https://entreprendre.service-public.gouv.fr/vosdroits/F23267 |
| Micro-foncier (CGI art. 32) | Gross rent up to EUR 15,000; 30% allowance | Income of 2025 | https://bofip.impots.gouv.fr/bofip/3973-PGP.html |
| Retirement savings (PER) deduction ceiling per person, subject to the dated carry-period and payment-eligibility rules below | Initial floor/cap before specified prior professional/employer pension reductions: 10% of last year's net professional income; max EUR 37,094, min EUR 4,637 (paid 2025); max EUR 37,680, min EUR 4,710 (paid 2026) | 2025 and 2026 | https://www.impots.gouv.fr/www2/fichiers/documentation/brochure/ir_2026/pdf_som/12-charges_ded_rev_225a236.pdf |
| Maintenance to an adult child, deduction limit | EUR 6,855 per child; EUR 13,710 if the payer alone supports the child's household | Income of 2025 | same |
| Gifts to bodies of general interest (reduction) | 66%, base capped at 20% of taxable income; gifts above the cap are carried to the next 5 years (aide-mémoire, note 18: "Les dons excédant ce plafond sont reportés sur les 5 années suivantes") | Income of 2025 | https://www.impots.gouv.fr/www2/fichiers/documentation/brochure/ir_2026/pdf_som/aide_memoire.pdf |
| Gifts to bodies helping people in difficulty (reduction) | 75%, base EUR 1,000 for gifts 1 Jan to 13 Oct 2025, EUR 2,000 for the year if gifts were made 14 Oct to 31 Dec 2025 | Income of 2025 | same |
| Union dues (credit) | 66%, base capped at 1% of salaries and pensions | Income of 2025 | same |
| Home help credit (CGI art. 199 sexdecies) | 50% of expenses up to EUR 12,000 (+EUR 1,500 per child, EUR 750 in alternating residence, per member over 65; overall max EUR 15,000); first year of directly employing a home worker EUR 15,000 (max EUR 18,000); EUR 20,000 where an invalidity condition is met | Income of 2025 | https://www.service-public.gouv.fr/particuliers/vosdroits/F12 |
| January advance of the home help and childcare credits | 60% of the credit received the year before; an advance that turns out too high is repaid in September (F12: "vous devrez rembourser le trop-perçu en septembre") | Paid January 2026 | same |
| Outside-home childcare credit, dependent child under 6 on 1 January of the income year (CGI art. 200 quater B) | Approved childminder or qualifying outside-home establishment. Exclude food and deduct Caf/employer care aid from expenses actually borne; credit is 50% of the net costs up to EUR 3,500 per child (EUR 1,750 in alternating residence) | Income of 2025 | https://www.service-public.gouv.fr/particuliers/vosdroits/F8 |
| Overall cap on tax advantages (CGI art. 200-0 A) | EUR 10,000, raised by EUR 8,000 for overseas investment and SOFICA reductions | Income of 2025 | https://www.impots.gouv.fr/www2/fichiers/documentation/brochure/ir_2026/pdf_som/plafonnement.pdf |
| Withholding default grid, metropolitan France and abroad (CGI art. 204 H, III-1-a) | 0% below EUR 1,635 a month, rising to 43% at EUR 55,558 and above | From 1 May 2026 | https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006069577/LEGISCTA000033779948/2026-10-24 |
| Zero withholding rate (CGI art. 204 H, II) | IR before PAS imputation nil for both last known tax years; RFR strictly below EUR 29,310 per share through 31 August 2026 (2024 reference income), then EUR 29,574 from 1 September 2026 to 31 August 2027 (2025 reference income) | Periods shown | https://bofip.impots.gouv.fr/bofip/11247-PGP.html/identifiant=BOI-IR-PAS-20-20-10-20260407 |
| Downward modulation allowed only if the estimated levy is lower by more than (CGI art. 204 J, III-1) | 5% | 2026 | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000046860839/2026-10-24 |
| Non-resident minimum rate (CGI art. 197 A) | 20% up to the top of the 11% band, 30% above (14.4% and 20% for income received in the overseas departments) | Income of 2025 | https://www.impots.gouv.fr/www2/fichiers/documentation/brochure/ir_2026/pdf_som/04-declaration_revenus_64a73.pdf |

## The taxable base

**The computation, in order.** Never skip a step.

1. Put each income in its category and take the category allowance: salaries and unemployment benefit (ordinary wages in lines 1AJ to 1DJ; unemployment and early-retirement benefits in lines 1AP to 1DP) take the 10% deduction or actual expenses; for the flat salary deduction use min(relevant declared remuneration, min(max(10% of that remuneration, EUR 509), EUR 14,555)) for 2025 income, so EUR 200 remuneration gives a EUR 200 deduction and zero salary net, not a negative EUR 309; pensions take the 10% pension allowance, capped per household; micro-entrepreneurs and furnished lets take the flat allowance of their micro regime; dividends taxed at the scale take the 40% allowance.
2. Add the net category incomes to get the revenu brut global.
3. Take off the deductions from global income (PER contributions, maintenance paid, deductible CSG, earlier global deficits) to get the revenu net global (RNG). Apply the dated special income allowances below to reach revenu net imposable (RNI), before dividing by shares. The PER capacity is per person after the statutory prior-contribution reductions below; the printed initial floor is not an unconditional final deduction; the three-year unused-ceiling method here applies to contributions paid in 2025. A couple can pool ceilings by ticking box 6QR. For 2026 payments and unused-ceiling vintages, apply the dated PER qualification below.
4. Count the shares (CGI art. 194 and 195): 1 for a single person, 2 for a couple taxed jointly; plus a half share for each of the first two dependent children and a full share from the third. A child in alternating residence gives a quarter share for each of the first two and a half share from the third. Case T requires actually living alone and mainly/exclusively supporting the child: the first such child gives a full share; for equally shared children each of the first two gives 0.5 share in all (ordinary 0.25 plus the case-T additional 0.25), not the sole-charge full share. Case L (living alone, no dependant, having raised a child alone for at least 5 years) gives a half share. Award invalidity/veteran half shares only to the actual CGI art. 195 populations: the specified military-invalidity/war-victim pension of at least 40% or qualifying widow pension, work-accident invalidity pension of at least 40%, qualifying CMI-invalidité card (including an eligible dependent holder), or a person older than 74 holding a combatant card or the specified military pension; this also covers a surviving spouse older than 74 of those persons or of a person holding a combatant card at death. Status labels alone are insufficient; obtain the pension/card, age and survivor evidence. A widowed taxpayer with at least one qualifying dependent or attached unmarried child without a family of their own, or a qualifying invalid dependant living under their roof, has the same share count as a married couple with those dependants. In the death year, the survivor of a couple previously taxed jointly keeps the married/Pacs status and share count for the post-death period; the separate cap treatment is in step 6.
5. Divide the RNI by the shares, apply the scale to one share, multiply back. Income taxed under the quotient system for exceptional income is added here.
6. Cap the family quotient: work out the tax again on the base shares only (1 or 2), less the cap for each extra half share. Keep the higher of the two results. For a qualifying widow after the death year, use one base share and EUR 1,807 for each extra half share. If the cap increases tax, subtract a complementary reduction equal to the smaller of EUR 2,011 and the increase from tax before the cap to tax after it. Apply that reduction before the overseas abatement, décote and other reductions. In the death year’s post-death period, cap only the half shares above two base shares and do not apply this EUR 2,011 widow reduction ([BOFiP paragraphs 180–220](https://bofip.impots.gouv.fr/bofip/2494-PGP.html/identifiant=BOI-IR-LIQ-20-20-20-20260407)). For an eligible invalidity/veteran half share under the populations in step 4, the complementary reduction is the lesser of EUR 1,801 per qualifying half share and the increase caused by the cap. Halve that limit to EUR 900.50 for the specified shared-child quarter. With a EUR 300 cap-caused increase and one eligible half share, deduct EUR 300, not EUR 1,801; no cap-caused increase means no complementary reduction. Apply before the overseas abatement/décote.
7. Apply the overseas abatement if the household lives in an overseas department on 31 December.
8. Apply the décote if the tax is below the threshold. It is the fixed amount less 45.25% of the tax, and cannot exceed the tax.
9. Take off tax reductions (they stop at zero), then tax credits (any excess is refunded). Check the overall cap on tax advantages: gifts and advantages tied to the personal situation are outside it; the home help and childcare credits, SME, FCPI, FIP, Pinel and Denormandie reductions are inside it. Pinel covers homes bought or built from 1 September 2014 to 31 December 2024, so 2025 brings only the continuing instalments of earlier investments. For the home-help credit, first deduct aid received, apply the specific service subceiling and the household ceiling for the actual claimant’s situation, then apply 50% ([F12](https://www.service-public.gouv.fr/particuliers/vosdroits/F12)); a first engagement of a service provider does not establish the higher first-direct-employment ceiling.
10. Add the flat tax (12.8%) on investment income not taxed at the scale, then the CEHR, then the CDHR.
11. Subtract withholding and tax instalments already paid, then add back any January credit advance already received, to obtain the balance or refund after the full annual credit.

**PER periods and payment eligibility.** For contributions paid in 2025, use the return brochure’s three-year unused-ceiling method. For an unused ceiling established in 2026, current [CGI art. 163 quatervicies I-2-b](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000053542827/2026-04-01) allows use during one of the following five years. The Ministry’s [1 June 2026 PER guidance](https://www.economie.gouv.fr/particuliers/gerer-mon-argent/gerer-mon-budget-et-mon-epargne/comment-fonctionne-le-plan-depargne-retraite-individuel) expressly keeps a three-year period for unused 2024 and 2025 ceilings. Track each vintage and its expiry using the annual ceiling statement. For payments from 1 January 2026, holder payments into PER plans under CMF art. L224-1 or French PEPP subaccounts under L225-1 covered by [CGI art. 163 quinvicies](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000053542708/2026-05-07) cease to qualify for this deduction from the holder’s 70th birthday. Obtain the plan type, holder’s birth date, payment dates and ceiling/vintage statement before applying the published 2026 ceiling.

**PER adjusted capacity and dated use order.** Compute the initial 10% professional-income floor/cap, then subtract the prior-year pension amounts specified by CGI art. 163 quatervicies I-2-a: qualifying compulsory employee/employer pension contributions (including the exempt employer limb), deductible non-salaried pension contributions, excluding their specified 15% fraction of profit between one and eight PASS, and the exempt retirement-plan amounts under art. 81, 18°. Use the actual correctly adjusted annual statement and do not deduct the same payment again as a voluntary global-income contribution. EUR 6,000 initial capacity less EUR 2,000 qualifying prior amounts leaves EUR 4,000; even the 2026 initial EUR 4,710 floor less those EUR 2,000 leaves EUR 2,710. For contributions paid in 2025 the brochure applies the current-year capacity first, then available older capacity starting with the oldest. Track the remaining balance/expiry by vintage. The new five-year 2026-vintage carry period does not itself prove an identical new 2026 administrative use-order instruction; retain that dated-source boundary.

**Special income allowances for 2025, declared in 2026.** Start from RNG after global deductions. Under the official worksheet’s age or invalidity rule (CGI art. 157 bis), a person born before 1 January 1961, or holding a military or work-accident invalidity pension of at least 40% or the qualifying invalidity card, receives an allowance of EUR 2,822 where household RNG does not exceed EUR 17,670, or EUR 1,411 where it is above EUR 17,670 and at most EUR 28,430. There is no allowance above EUR 28,430. Double the allowance if both spouses or Pacs partners qualify. These are the income-of-2025 amounts, not amounts established for income of 2026.

For an actually qualifying attached married or Pacs child, or a child with their own family (CGI art. 6-3 and 196 B), apply EUR 6,855 per attached person. Halve the amount attributable to a grandchild in alternating or shared residence. Establish valid requested attachment first; the attachment includes the young household’s income for the whole year and gives this income allowance instead of extra child shares in step 4. It covers the attached household as a whole and cannot be made simultaneously to both sets of parents. Subtract these special allowances from RNG to obtain RNI. See the [official calculation sheet](https://www.impots.gouv.fr/www2/fichiers/documentation/brochure/ir_2026/pdf_som/21-calcul_impot_369a382.pdf), sections 2–4, and [family instructions](https://www.impots.gouv.fr/www2/fichiers/documentation/brochure/ir_2026/pdf_som/05-situation_foyer_75a84.pdf), page 83. Obtain the claimant’s birth date, qualifying invalidity evidence and the attached household’s valid request, composition, income and custody facts. Do not copy the 2025 amounts into the 2026 income computation without its enacted figures.

**Investment income.** Dividends, interest and gains on securities are taxed by default at the flat 12.8% income tax rate (CGI art. 200 A, 1). The household can instead opt, on the return and by the filing deadline, to put all of them under the scale (CGI art. 200 A, 2). The option is global: it covers every item in the flat-tax field for that year. It brings the 40% dividend allowance and the 6.8% deductible CSG. It helps a household with no tax or a marginal rate of 11%; at 30% or more the flat rate is lower (F2613). Social levies are charged on top in both cases and are not IR.

**Exceptional and deferred income (CGI art. 163-0 A).** On request (line 0XX of form 2042 C for the 2025-income campaign), the exceptional-income quotient adds one quarter to ordinary income and multiplies the additional tax by four. Eligible non-annual income must exceed the average net taxable income of the previous three years, except the source's specified no-amount-test items such as the taxable severance component. Exclude proportionally taxed income and income already covered by its own specific quotient/spreading regime. **Deferred income is a separate branch:** receipts normally due in one or more earlier calendar years, received together because of circumstances independent of the taxpayer's will, qualify irrespective of amount. Divide their net amount by the number of actual normal due-years plus one, apply the additional tax at that fraction, then multiply it by the same coefficient. Two due-years give coefficient three; voluntary postponement is not enough, and ordinary year-end bonuses paid at the start of the next year are not automatically deferred income. A household already at 45% on its ordinary income gains nothing.

**CEHR.** Charged on the revenu fiscal de référence (RFR), counting quotient-system income at its full amount. Smoothing requires all three conditions: the current RFR is at least 1.5 times the average of the two previous years; each previous year's RFR was at or below EUR 250,000 (single) or EUR 500,000 (couple); and, in each of those two years, more than half the relevant French- and foreign-source income was passible to French income tax (CGI art. 223 sexies, II-1; BOFiP BOI-IR-CHR, paragraphs 140–170). For that last test, substantiate the French-IR-passible income and the worldwide RFR comparison, including the treatment of foreign income; the French RFR alone does not establish the test. If all three conditions hold, halve the excess over the two-year average, add that half to the average, work out the extra contribution and double it. A family-status change in the current or either previous year requires the household RFR reconstruction and claim prescribed by article II-2. The CEHR applies until the year in which the public deficit is nil (loi n° 2011-1977, art. 2, III-A).

**CDHR (contribution différentielle sur les hauts revenus).** Created by loi n° 2025-127 (art. 10) for the income of 2025 and amended by loi n° 2026-103 (art. 2) for the income of 2026 onward. It applies to households domiciled in France whose CDHR reference income passes EUR 250,000 (single) or EUR 500,000 (couple). Establish its own CGI art. 224 II reference, not unadjusted RFR: start with RFR without art. 163-0 A quotient, subtract the listed allowances (preserving the enhanced securities allowances excluded from that subtraction), exempt business profits, art. 155 B exempt products/income, the specified 10%-taxed intellectual-property result/products, gains whose art. 150-0 B ter deferral ends, and treaty-exempt income. Income exceptional both by non-annual nature and by exceeding the prior-three-year average net taxable income is counted at one quarter; apply the statutory household reconstruction if family status changed. This is distinct from the ordinary IR quotient. The contribution is the positive difference between:

- 20% of the reference income, less a décote where that income is at or below EUR 330,000 (single) or EUR 660,000 (couple). The décote is 20% of the income less 82.5% of (income less EUR 250,000 or EUR 500,000), if positive; and
- **Own adjusted tax limbs IR1 + CEHR1 + PREL1**, plus EUR 1,500 per qualifying dependant and EUR 12,500 for a couple. For IR1, count tax on the qualifying exceptional income at one quarter, without the ordinary quotient; add back the actual specified reduction/credit advantages within tax due (including arts. 199 quater B, 199 undecies B subject to its exception, 200, 238 bis, specified business/research credits and treaty credits, with the separately dated 2025-investment relief rules); subtract the specified 10%-taxed intellectual-property tax and tax on the ended art. 150-0 B ter deferral gains. CEHR1 omits its own smoothing mechanism, excludes tax attributable to the II-subtracted items and counts tax on the qualifying exceptional income at one quarter. PREL1 is the qualifying final-levy limb, not every withholding payment. Notice IR/CEHR alone need not equal these limbs.

From the income of 2026, the year of moving abroad or into France has its own rules (CGI art. 224, V bis). For the income of 2025, a liable household paid an advance of 95% of its estimate between 1 and 15 December 2025. Refer any household near the CDHR threshold: the reference income needs a full working paper. The working paper must establish the II/IV-adjusted inputs above. A stipulated valid single-household RREF EUR 300,000 gives a EUR 41,250 minimum target after décote. Net-notice IR EUR 19,500 plus a required EUR 1,500 relief addback gives IR1 EUR 21,000; with CEHR1 EUR 1,500, PREL1/other additions zero, CDHR is EUR 18,750, not EUR 20,250 from unadjusted notice IR. This declared input example does not establish relief eligibility or the unresolved 2026 advance procedure.

**Social levies.** These are not IR, but they ride on the same income. Name the income, collection route and year. Under LFSS 2026 (loi n° 2025-1403, art. 12 II), the general 18.6% total (CSG 10.6%, CRDS 0.5%, solidarity levy 7.5%) applies to L136-6 income assessed with income tax from the 2025 income year, and to L136-7 source-collected payments from 1 January 2026. General dividends actually source-collected in 2025 remain at 17.2%; a taxable 2025 securities gain assessed in 2026 falls under the 18.6% rule. Rental income, gains on real property and the PEL, CEL and life-insurance products covered by L136-8 IV retain 17.2%. Apply the historical-product exceptions in article 12 II rather than repricing all accrued products by the payment year. Loi n° 2026-534 art. 65 concerns the separate illicit-income rule, not commencement of the general 10.6% CSG rate. A resident who works in another EEA state or Switzerland and is covered by its social security pays only the 7.5% solidarity levy (F2329). Computation is in `fr-capital-gains` and `fr-rental-income`.

**Self-employed (pointer).** A micro-entrepreneur declares turnover on form 2042-C-PRO and the tax office applies the allowance in the rates table. The micro regime is lost only if a limit was exceeded in both of the two previous years (F23267). The flat payment option (versement forfaitaire libératoire) is paid with the Urssaf return and replaces IR on that turnover. It is open where the household RFR of year N-2 meets the applicable test in the rates table, with the ordinary existing-business option before 30 September of the prior year and cancellation by its own prior-year deadline. A creation during the year has a separate current-year option window: F23267 says "avant le dernier jour du 3e mois suivant celui de la création" and gives a September 2026 creation example "avant le 30 décembre 2026". Preserve those published date words rather than deny current-year entry solely because the prior September deadline has passed. Real-regime results are in `fr-income-tax`.

**Salary terminology trap.** The amount on line 1AJ is the salaire net imposable from the payslip, not the gross and not the net paid. The 10% deduction then comes off line 1AJ.

## Deadlines and filing

| Step | Date | Source |
|---|---|---|
| Online return, income of 2025, départements 01 to 19 and non-residents | Thursday 21 May 2026, 23:59 | impots.gouv.fr, modalités 2026 |
| Online return, départements 20 to 54 | Thursday 28 May 2026, 23:59 | same |
| Online return, départements 55 to 974 and 976 | Thursday 4 June 2026, 23:59 | same |
| Paper return, residents abroad included | Tuesday 19 May 2026, midnight | same |
| Online correction after the avis, for eligible online/mobile/automatic returns | 29 July to 30 November 2026 inclusive; from 1 December use a formal claim. EDI filers use EDI-Correction; paper filers use a formal claim | https://www.economie.gouv.fr/particuliers/impots-et-fiscalite/gerer-mon-impot-sur-le-revenu/impot-sur-le-revenu-corrigez-votre-declaration-en-ligne-jusquau-30-novembre-2026 |
| Ordinary claim (réclamation) concerning IR assessed by rôle, including a paper-filed return | 31 December of the second year after the rôle’s mise en recouvrement, shown on the assessment notice, subject to applicable special periods. Filing does not start this clock (LPF R196-1(a)) | https://bofip.impots.gouv.fr/bofip/597-PGP.html/identifiant=BOI-CTX-PREA-10-30-20260422 |
| Balance due up to EUR 300 | One debit in September 2026 | same, and F34009 |
| Balance due above EUR 300 | Four monthly debits, September to December 2026 | same |
| New withholding rate from the 2026 return | Applied from September 2026 | same |

**2026 correction calendar source.** The Ministry’s specific announcement of 28 August 2026 publishes 29 July–30 November inclusive, agreeing with [ServicePublic F33885](https://www.service-public.gouv.fr/particuliers/vosdroits/F33885). The [general annual DGFiP overview](https://www.impots.gouv.fr/les-modalites-de-la-declaration-de-revenus-en-2026) retains an approximate mid-August to mid-December range; use the specific operational announcement above. This is the published administrative calendar, not a record of access to a personal portal. The ordinary claim method comes from the official BOFiP and Ministry guidance; non-role and special claim periods belong in `fr-tax-audit`.

Forms: 2042 (main return), 2042 C (extra income and options), 2042 C PRO (self-employed), 2042 RICI (reductions and credits), 2047 (foreign income), 2044 (real-regime rental income). The return is compulsory every year whatever the income; a household with no change may be on the automatic return. Online filing is the rule where the home has internet access.

**Withholding at source (prélèvement à la source).** The tax of the year is collected during the year:

- **Retenue à la source** on salaries, pensions, unemployment benefit and sick pay, by the payer.
- **Acomptes** (monthly, or quarterly on option) on self-employed profits, rental income, maintenance received, annuities and qualifying foreign income within the PAS collection field, debited by the DGFiP and based on the income declared the year before. Foreign income entitled under the treaty to a credit equal to the corresponding French tax is excluded from PAS, so it is not an acompte base merely because it appears on form 2047.
- **The rate** is the household rate from the last return (CGI art. 204 H): the rate of year N-2 from January to August, of year N-1 from September. A couple taxed jointly gets individualised rates automatically, for each partner's own income; common income such as rent stays at the household rate. Either partner can opt for the household rate.
- **Default grid.** With no personal rate, the payer applies the grid in CGI art. 204 H, III (separate grids for Guadeloupe, La Réunion and Martinique, and for Guyane and Mayotte). A taxpayer may also choose the grid for salaries to keep their rate private, and then pays any shortfall themselves by the end of the following month.
- **Zero rate.** Both last known tax years must have nil IR before PAS imputation. The last known year’s RFR must be strictly below EUR 29,310 per quotient-family share for rates through 31 August 2026 (2024 reference income), then EUR 29,574 from 1 September 2026 to 31 August 2027 (2025 reference income). Apply the last-known-year conditions: the older of the two known tax years cannot precede the third year before the withholding year. The ceiling is indexed each 1 September (CGI art. 204 H, II; [BOFiP §140–180](https://bofip.impots.gouv.fr/bofip/11247-PGP.html/identifiant=BOI-IR-PAS-20-20-10-20260407)).
- **Changes.** Report a marriage, Pacs, birth or adoption, death, divorce or end of a Pacs within 60 days. Raising the rate is free. Lowering it is allowed only if the estimated levy for the year is more than 5% lower than the levy without the change (CGI art. 204 J, III-1). A change applies at the latest from the third month after the request.
- **Settlement.** The spring return computes the final tax; withholding is set against it, and the balance is collected or refunded as in the table above. Keep bank details up to date before 1 July.

## Penalties and interest

| Item | Rate | Source |
|---|---|---|
| Late return, no formal notice, or filed within 30 days of a notice (CGI art. 1728, 1-a) | 10% of the tax | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000028312309/2026-10-24 |
| Return not filed within 30 days of a formal notice (art. 1728, 1-b) | 40% | same |
| Undeclared (occult) activity discovered (art. 1728, 1-c) | 80% | same |
| Inaccuracy or omission, deliberate breach (CGI art. 1729, a) | 40% | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000020051904/2026-10-24 |
| Abuse of law (art. 1729, b) | 80% (40% if the taxpayer was neither main initiator nor main beneficiary) | same |
| Fraudulent manoeuvres or concealment (art. 1729, c) | 80% | same |
| Late payment interest (CGI art. 1727, III) | 0.20% per month | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000029355562/2026-10-24 |
| Late payment of IR on a rôle, not paid within 45 days of collection, never before 15 September for current-year tax (CGI art. 1730) | 10% | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000051219475/2026-10-24 |
| Late payment of a withholding instalment or top-up (CGI art. 1729 G, 1) | 10% of sums unpaid by the deadline. For a top-up paid at less than 70% of the amount due D, the rate instead equals half of (D − paid top-up) / D, applied to the unpaid amount | https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006069577/LEGISCTA000026890501/2026-10-24 |
| Withholding lowered by modulation (art. 1729 G, 2) | Trigger only where the last adjusted estimated levy E is strictly below 90% of the levy A recomputed on actual income. Apply the positive capped base and rate described below, with the good-faith/unforeseeable-event and no-duplication rules in paragraph 3 | same |

**Downward-modulation penalty method (CGI art. 1729 G, 2–3).** E is the last estimated levy computed under art. 204 J, III-3, increased where applicable by non-refunded payments under III-6-2°. A is the levy recomputed on actual annual income using the tax rules in force at the modulation date; U is the levy without modulation, and P is the levy actually made. First test E < 90% × A. If it passes, put C = min(A, U) and base = max(C − P, 0). With a positive base, the rate is 10%; if P < 70% × C, use half of (C − P) / C instead. No positive base means no charge under this calculation and no division by zero. Paragraph 2 does not apply where the taxpayer establishes good faith or circumstances difficult to foresee at the request date, or to sums already surcharged under paragraph 1. [Current art. 1729 G](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000036354358).

For IR, late interest starts on 1 July of the year after the income year (CGI art. 1727, IV-1). It is not due where the shortfall is no more than one twentieth of the base, save deliberate breach (art. 1727, II-4), and the 50% spontaneous-correction reduction requires filing before the administration's recovery period expires, no infringement exclusive of good faith, and payment with the rectifying declaration or, for a rôle, by the notice's payment deadline. An accepted public-accountant plan for the tax preserves that reduction in place of immediate/deadline payment (art. 1727 V). Interest stops when the art. 1730 surcharge becomes applicable (IV-2); do not extend it beyond that statutory event merely because other compatible penalties exist. In 2026 the administration may reassess the income of 2023, 2024 and 2025 (aide-mémoire); longer periods apply in some cases (see `fr-tax-audit`).

## Cross-border points

- **Non-residents.** Taxed on French-source income only, with a floor of 20% on taxable income up to the top of the 11% band and 30% above (14.4% and 20% on income received in the overseas departments). A non-resident whose average rate on worldwide income is lower may ask, on line 8TM, to be taxed at that average rate. The brochure prints the band top for the income of 2025 as EUR 29,574, five euros below the EUR 29,579 in CGI art. 197; the law wins, so use EUR 29,579 and flag the difference. Shares, décote and reductions for a non-resident, and treaty relief, are outside this skill: see `fr-cross-border`.
- **Online deadline.** Non-residents file online by the first date (21 May 2026); residents abroad filing on paper by 19 May 2026.
- **CDHR.** Applies only to households domiciled in France, subject to treaties; "Schumacker" non-residents treated as residents fall within it on French-source income only (BOFiP BOI-IR-CDHR-10). From the income of 2026 it reaches the year of departure and the year of arrival (CGI art. 224, V bis).
- **Foreign income.** Declared on form 2047, with collection determined by the actual income/treaty category. Qualifying foreign-tax-credit income can remain in the PAS field, but income entitled to a credit equal to French tax is excluded, not automatically debited by acompte (BOI-IR-PAS-20-20-10, https://bofip.impots.gouv.fr/bofip/11247-PGP.html/identifiant=BOI-IR-PAS-20-20-10-20260407). Foreign tax on dividends and interest is credited against the 12.8% flat tax within the treaty credit (CGI art. 200 A, 1-A-1°).
- **Social levies for EEA or Swiss social security members.** Only the 7.5% solidarity levy, not CSG and CRDS.
- **Leaving France.** The exit tax on shareholdings is in `leaving-france-exit-tax`.

## Worked examples

**Assessment qualification for the preserved illustrations.** The original paragraphs and executable checks below retain their raw algebra and inputs. Final IR liquidation uses whole euros under CGI art. 1724 (fractions of EUR 0.50 rounded up), not an invented intermediate per-share/levy rounding rule. Thus raw IR EUR 4,443.99 is EUR 4,444 on liquidation (with the stipulated EUR 4,000 withholding, EUR 444 rather than the raw EUR 443.99 balance); raw total IR EUR 10,873.98 is EUR 10,874; raw EUR 445.11 is EUR 445. The original examples remain fixture calculations. Source: https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000006312863

**Example 1: a single employee, simple case, income of 2025.** A single person (1 share) has EUR 42,000 on line 1AJ and no other income. The 10% deduction is EUR 4,200, inside the EUR 509 floor and the EUR 14,555 ceiling, so the net taxable income is EUR 37,800. The scale gives EUR 1,977.69 on the 11% band (EUR 17,979 at 11%) and EUR 2,466.30 on the 30% band (EUR 8,221 at 30%): EUR 4,443.99. That is above the EUR 1,982 single-person threshold, so there is no décote. EUR 4,000 was withheld in 2025, so EUR 443.99 is left to pay. That is above EUR 300, so it is taken in four debits from September to December 2026.

```oa-check
name: France 2026 return, single employee, income of 2025, salary EUR 42,000
inputs:
  salary: 42000
  withheld: 4000
steps:
  - deduction: min(max(salary * 0.10, 509), 14555)
  - rni: salary - deduction
  - band_11: (min(rni, 29579) - 11600) * 0.11
  - band_30: max(min(rni, 84577) - 29579, 0) * 0.30
  - gross_tax: band_11 + band_30
  - decote: min(max(897 - gross_tax * 0.4525, 0), gross_tax)
  - tax: gross_tax - decote
  - balance: tax - withheld
expected:
  deduction: 4200.00
  rni: 37800.00
  gross_tax: 4443.99
  decote: 0.00
  tax: 4443.99
  balance: 443.99
```

**Example 2: a couple with two children, the family-quotient cap bites, plus dividends under the flat tax.** A married couple with two dependent children (3 shares) has net taxable income of EUR 90,000 and EUR 10,000 of dividends received in 2025, with social levies collected at source under L136-7 in 2025 and left under the flat tax. With 3 shares, each share is EUR 30,000, taxed at EUR 2,103.99, so EUR 6,311.97 in all. With the 2 base shares, each share is EUR 45,000, taxed at EUR 6,603.99, so EUR 13,207.98, less two extra half shares at EUR 1,807: EUR 9,593.98. That is higher than EUR 6,311.97, so the cap applies and the tax from the scale is EUR 9,593.98. It is far above the EUR 3,277 couple threshold, so no décote. The dividends bear 12.8% income tax (EUR 1,280) and 17.2% social levies (EUR 1,720), 30% in all. The IR for the year is EUR 10,873.98. Had the same dividends been received in 2026, the levies would be 18.6% (EUR 1,860), 31.4% in all.

```oa-check
name: France 2026 return, couple with 2 children, family-quotient cap, dividends under the flat tax
inputs:
  rni: 90000
  dividends: 10000
steps:
  - per_share_3: rni / 3
  - tax_3_shares: ((min(per_share_3, 29579) - 11600) * 0.11 + max(min(per_share_3, 84577) - 29579, 0) * 0.30) * 3
  - per_share_2: rni / 2
  - tax_2_shares: ((min(per_share_2, 29579) - 11600) * 0.11 + max(min(per_share_2, 84577) - 29579, 0) * 0.30) * 2
  - capped: tax_2_shares - 2 * 1807
  - gross_tax: max(tax_3_shares, capped)
  - decote: min(max(1483 - gross_tax * 0.4525, 0), gross_tax)
  - flat_tax_ir: dividends * 0.128
  - total_ir: gross_tax - decote + flat_tax_ir
  - levies_2025: dividends * 0.172
  - levies_if_2026: dividends * 0.186
expected:
  tax_3_shares: 6311.97
  tax_2_shares: 13207.98
  gross_tax: 9593.98
  decote: 0.00
  flat_tax_ir: 1280.00
  total_ir: 10873.98
  levies_2025: 1720.00
  levies_if_2026: 1860.00
```

**Example 3: the décote, single person, income of 2025.** A single person (1 share) has net taxable income of EUR 20,000. The scale gives (20,000 - 11,600) x 11% = EUR 924. That is below the EUR 1,982 single-person threshold, so the décote is EUR 897 less 45.25% of EUR 924 (EUR 418.11): EUR 478.89. The tax after the décote is EUR 445.11 (CGI art. 197, I-4-a; BOFiP BOI-IR-LIQ-20-20-30-20260407).

```oa-check
name: France 2026 return, single person, décote, income of 2025, RNI EUR 20,000
inputs:
  rni: 20000
steps:
  - gross_tax: (min(rni, 29579) - 11600) * 0.11
  - decote: min(max(897 - gross_tax * 0.4525, 0), gross_tax)
  - tax: gross_tax - decote
expected:
  gross_tax: 924.00
  decote: 478.89
  tax: 445.11
```

### Preserved source-supported raw illustrations

### Worked example (hypothetical): single person, 1 share, net taxable income 40,000 euros

~~~
First band:  11,600 x 0                      =     0.00
Second band: (29,579 - 11,600) = 17,979 x 0.11 = 1,977.69
Third band:  (40,000 - 29,579) = 10,421 x 0.30 = 3,126.30
Tax for one share                             = 5,103.99
x 1 share                                     = 5,103.99
Gross tax is above the single-person décote threshold, so no décote.
~~~

### Worked example (hypothetical): couple, 2 children, 3 shares, net taxable income 80,000 euros

~~~
(a) With 3 shares: 80,000 / 3 = 26,666.67 per share
    (26,666.67 - 11,600) x 0.11 = 1,657.33 per share x 3 = 4,972.00
(b) With 2 base shares: 80,000 / 2 = 40,000 per share
    1,977.69 + (40,000 - 29,579) x 0.30 = 5,103.99 per share x 2 = 10,207.98
    2 extra half shares x 1,807 = 3,614.00
    10,207.98 - 3,614.00 = 6,593.98
(a) is lower than (b), so the cap applies: gross tax = 6,593.98
Above the couple décote threshold, so no décote.
~~~

**Precision of the restored illustrations.** These are raw scale/cap calculations for the stated RNI and shares, before final whole-euro liquidation: EUR 5,103.99 → EUR 5,104 and EUR 6,593.98 → EUR 6,594. In the EUR 80,000 case the displayed EUR 26,666.67 and EUR 1,657.33 are abbreviated presentation; using the unrounded quotient gives exactly EUR 4,972 before the cap. Do not round each share to cents first and infer EUR 4,971.99. The two original historical inputs/case passages and the three other current examples are retained separately.

## Ask the client first

- For the 2025 special income allowances, what are the household members’ birth dates and qualifying invalidity evidence? Is an attached child married, in a Pacs or raising their own family, and what is the valid attachment request, young household income, composition and any alternating-residence grandchild?

- For a retirement deduction, what is the plan type, the holder’s birth date, each payment date and the annual ceiling statement showing unused amounts by vintage? The 2026 carry period and payment eligibility depend on those facts.

- Were you resident in France for tax purposes for all of 2025? A non-resident is taxed only on French-source income at a minimum rate, and a part-year resident needs a referral.
- What was your situation on 31 December 2025, and did you marry, enter a Pacs, divorce, separate or lose a spouse during the year? Each changes the number of returns and of shares.
- Who depended on you, is any child in alternating residence, and do you live alone with them (case T) or live alone having raised a child for 5 years (case L)? Shares and caps differ for each.
- For an outside-home childcare claim, what is the child’s date of birth and age on 1 January of the income year, is the child dependent on your household, is the provider an approved childminder or qualifying establishment, and what care costs did you actually pay after excluding food and deducting care aid?
- Did you receive dividends, interest or gains on securities? Give the income category, year and whether the social levies were collected at source or will be assessed with income tax. Those facts set the commencement rule and rate; the option for the scale changes the whole investment computation.
- Is your reference income near EUR 250,000 (single) or EUR 500,000 (couple)? The CEHR and the CDHR then apply.
- Did you receive a one-off sum (severance pay, arrears, an exceptional bonus)? The quotient system applies only if you ask for it on the return.

Defaults while waiting for answers (OpenAccountants working practice): single, 1 share; no children; investment income under the flat tax, no option for the scale; no credit applied where eligibility is unclear; the household withholding rate on the last avis d'impôt; unemployment benefit or salary unclear, apply the 10% salary deduction either way and use the line the payer's statement names.

## Sources

| Source | URL | Read on |
|---|---|---|
| CGI art. 197 (scale, family-quotient caps, overseas abatement, décote), as amended by loi n° 2026-103 art. 4 | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000053542636/2026-10-24 | 2026-10-24 |
| CGI art. 224 (CDHR), as amended by loi n° 2026-103 art. 2 | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000053561826/2026-10-24 | 2026-10-24 |
| CGI art. 223 sexies (CEHR) | https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006069577/LEGISCTA000025049019/2026-10-24 | 2026-10-24 |
| CGI art. 200 A (flat tax 12.8%, option for the scale), as amended by loi n° 2026-103 art. 126 | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000053546896/2026-10-24 | 2026-10-24 |
| CSS art. L136-8 (CSG rates and protected categories; general-rate commencement is LFSS 2026 art. 12 II) | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000054336623/2026-10-24 | 2026-10-24 |
| CGI art. 204 A to 204 N (withholding; 204 H rates and default grid, in force 1 July 2026) | https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006069577/LEGISCTA000033779948/2026-10-24 | 2026-10-24 |
| CGI art. 204 J (modulation) | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000046860839/2026-10-24 | 2026-10-24 |
| CGI art. 1727 (late interest) | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000029355562/2026-10-24 | 2026-10-24 |
| CGI art. 1728 (late filing, as amended by loi n° 2026-103 art. 126) | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000028312309/2026-10-24 | 2026-10-24 |
| CGI art. 1729 (inaccuracies) | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000020051904/2026-10-24 | 2026-10-24 |
| CGI art. 1729 G (withholding penalties) | https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006069577/LEGISCTA000026890501/2026-10-24 | 2026-10-24 |
| CGI art. 1730 (10% late payment) | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000051219475/2026-10-24 | 2026-10-24 |
| BOFiP actualité 7 April 2026: 0.9% uprating, loi n° 2026-103 art. 4 | https://bofip.impots.gouv.fr/bofip/14954-PGP.html | 2026-10-24 |
| BOFiP BOI-IR-LIQ-20-20-20-20260407 (family-quotient caps) | https://bofip.impots.gouv.fr/bofip/2494-PGP.html/identifiant=BOI-IR-LIQ-20-20-20-20260407 | 2026-10-24 |
| BOFiP BOI-IR-LIQ-20-20-30-20260407 (décote thresholds) | https://bofip.impots.gouv.fr/bofip/2495-PGP.html/identifiant=BOI-IR-LIQ-20-20-30-20260407 | 2026-10-24 |
| BOFiP BOI-IR-CDHR-10-20260630 (CDHR scope and formula) | https://bofip.impots.gouv.fr/bofip/15095-PGP.html/identifiant=BOI-IR-CDHR-10-20260630 | 2026-10-24 |
| BOFiP BOI-IR-CHR-20170711 (CEHR) | https://bofip.impots.gouv.fr/bofip/7804-PGP.html/identifiant=BOI-IR-CHR-20170711 | 2026-10-24 |
| BOFiP BOI-BAREME-000035-20260217 (10% salary deduction amounts) | https://bofip.impots.gouv.fr/bofip/10855-PGP.html/identifiant=BOI-BAREME-000035-20260217 | 2026-10-24 |
| BOFiP BOI-BAREME-000037-20260706 (default withholding grids from 1 May 2026) | https://bofip.impots.gouv.fr/bofip/11255-PGP.html | 2026-10-24 |
| BOFiP micro-foncier (CGI art. 32) | https://bofip.impots.gouv.fr/bofip/3973-PGP.html | 2026-10-24 |
| impots.gouv.fr: les modalités de la déclaration de revenus en 2026 (site in maintenance; Internet Archive copy of 23 September 2026) | https://www.impots.gouv.fr/les-modalites-de-la-declaration-de-revenus-en-2026 | 2026-10-24 |
| impots.gouv.fr: CDHR advance (Internet Archive copy, page modified 22 December 2025) | https://www.impots.gouv.fr/actualite/contribution-differentielle-sur-les-hauts-revenus-cdhr | 2026-10-24 |
| Brochure pratique IR 2026: aide-mémoire (Internet Archive copy) | https://www.impots.gouv.fr/www2/fichiers/documentation/brochure/ir_2026/pdf_som/aide_memoire.pdf | 2026-10-24 |
| Brochure pratique IR 2026: situation de famille, pensions, charges à déduire, réductions et crédits, divers (CEHR, CDHR, quotient), déclaration (non-residents), calcul de l'impôt, plafonnement (Internet Archive copies; files 05-situation_foyer_75a84, 07-pensions_115a120, 12-charges_ded_rev_225a236, 14-RICI_2042C_257a296, 17-divers_321a336, 04-declaration_revenus_64a73, 21-calcul_impot_369a382, plafonnement) | https://www.impots.gouv.fr/www2/fichiers/documentation/brochure/ir_2026/pdf_som/ | 2026-10-24 |
| Service-public F1419: barème (checked 15 April 2026) | https://www.service-public.gouv.fr/particuliers/vosdroits/F1419 | 2026-10-24 |
| Service-public F2705: quotient familial (checked 15 April 2026) | https://www.service-public.gouv.fr/particuliers/vosdroits/F2705 | 2026-10-24 |
| Service-public F34009: prélèvement à la source (checked 15 April 2026) | https://www.service-public.gouv.fr/particuliers/vosdroits/F34009 | 2026-10-24 |
| Service-public F2613: revenus de placements, flat tax (checked 15 April 2026) | https://www.service-public.gouv.fr/particuliers/vosdroits/F2613 | 2026-10-24 |
| Service-public F2329: prélèvements sociaux (checked 30 June 2026) | https://www.service-public.gouv.fr/particuliers/vosdroits/F2329 | 2026-10-24 |
| Service-public F12: home help credit (checked 15 April 2026) | https://www.service-public.gouv.fr/particuliers/vosdroits/F12 | 2026-10-24 |
| Service-public F8: childcare credit (checked 15 April 2026) | https://www.service-public.gouv.fr/particuliers/vosdroits/F8 | 2026-10-24 |
| Entreprendre service-public F23267: micro regime (checked 13 May 2026) | https://entreprendre.service-public.gouv.fr/vosdroits/F23267 | 2026-10-24 |
| Service-public F12, selected January advance, summer balance and excess-repayment instructions reread | https://www.service-public.gouv.fr/particuliers/vosdroits/F12 | 2026-10-29 |
| DGFiP, micro flat-payment option: 2026/2024 and 2027/2025 RFR tests and published 2.5-part examples, page modified 14 October 2026 | https://www.impots.gouv.fr/professionnel/questions/en-tant-que-micro-entrepreneur-sous-quelles-conditions-puis-je-opter-pour-l | 2026-10-29 |
| CGI art. 223 sexies II: all three smoothing conditions and family-change claim; selected current provision read | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000036427364/2026-10-29 | 2026-10-29 |
| LFSS 2026, loi n° 2025-1403 art. 12 II: L136-6/L136-7 commencement and historical-product exceptions; complete operative II read | https://www.legifrance.gouv.fr/loda/article_lc/LEGIARTI000053265270/2026-10-29 | 2026-10-29 |
| CSS L136-8 I/IV and loi n° 2026-534 art. 65: selected rate/exception provisions and separate illicit-income amendment read | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000054336623/2026-10-29 and https://www.legifrance.gouv.fr/jorf/article_jo/JORFARTI000054309935 | 2026-10-29 |
| BOFiP BOI-IR-CHR paragraphs 140–200 and DGFiP aide-mémoire: selected CEHR conditions/calculation and assessed-2025 levy table reread | https://bofip.impots.gouv.fr/bofip/7804-PGP.html/identifiant=BOI-IR-CHR-20170711 and https://www.impots.gouv.fr/www2/fichiers/documentation/brochure/ir_2026/pdf_som/aide_memoire.pdf | 2026-10-29 |
| DGFiP Brochure IR 2026, official calculation sheet sections 2–4 and family instructions page 83: RNG, age/invalidity and attached-family allowances, then RNI; selected native scopes read | https://www.impots.gouv.fr/www2/fichiers/documentation/brochure/ir_2026/pdf_som/21-calcul_impot_369a382.pdf and https://www.impots.gouv.fr/www2/fichiers/documentation/brochure/ir_2026/pdf_som/05-situation_foyer_75a84.pdf | 2026-10-29 |
| Selected repair clauses: CGI art. 6(4)/(6), qualifying special shares/caps, adjusted PER/CDHR inputs, deferred-income gates, art. 1727 V payment-plan/stop rules, foreign PAS exclusion and salary lower-remuneration limit; retained official clauses personally reread, not body-wide acquisition claims | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000046197457 and https://www.impots.gouv.fr/particulier/questions/comment-puis-je-beneficier-de-la-deduction-forfaitaire-de-10 | 2026-10-31 |

**Long-term furnished letting source.** Official [F23267](https://entreprendre.service-public.gouv.fr/vosdroits/F23267) classifies long-term furnished letting as BIC services and gives the services allowance of 50%, minimum EUR 305. This is the administrative category-to-rate method for eligible micro income; keep the applicable yearly turnover limits above and use `fr-rental-income` for the detailed rental method. The earlier failed fetch of impots.gouv.fr/particulier/location-meublee is preserved in the research history; it does not negate this current official source.

Not yet confirmed: the scale for the income of 2026 (no 2027 finance law enacted on 24 October 2026); the end date of the CDHR (CGI art. 224 as read prints none, and whether loi n° 2025-127 art. 10 or loi n° 2026-103 art. 2 limit it in time was not read); the CDHR advance rule for the income of 2026; the rounding rules for the tax and the share count (CGI art. 193, not re-read); the PUMa contribution and the IFI, which this skill does not cover.

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
