---
name: nl-income-tax
description: "Dutch personal income tax (inkomstenbelasting) for a resident individual, tax year 2026, with 2025 figures for returns still open. Covers the three boxes: box 1 bands (8.10% tax plus 27.65% national insurance in the first band, 37.56%, 49.50%) and the AOW-age rates; the tariefsaanpassing; the algemene heffingskorting and arbeidskorting with their phase-outs; the inkomensafhankelijke combinatiekorting and ouderenkorting; box 2 at 24.5% and 31%; box 3 for 2026 under the bridging law, the Hoge Raad rulings and the tegenbewijsregeling (actual return); fiscal-partner allocation; the 1 May return, extensions, voorlopige aanslag, belastingrente and penalties. Trigger phrases: aangifte inkomstenbelasting, box 1 tarief, heffingskortingen, arbeidskorting, box 3 werkelijk rendement, tegenbewijsregeling, voorlopige aanslag, belastingrente. Out of scope: entrepreneur reliefs (nl-zzp-deductions), personal and home deductions (nl-deductions), AOW-age detail (nl-income-tax-special-groups), box 2 detail (nl-box2-substantial-interest), expat scheme (nl-30-percent-ruling), payroll (nl-payroll-tax), non-residents (nl-cross-border)."
version: 2.1
jurisdiction: NL
tax_year: 2026
last_updated: 2026-10-24
authored_by: Michael Cutajar and the OpenAccountants team
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
depends_on:
  - income-tax-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Netherlands: personal income tax (inkomstenbelasting) 2026

## Who this applies to

- **Resident individuals** (binnenlandse belastingplichtigen) filing the aangifte inkomstenbelasting for 2026. Tax year = calendar year. Currency euro; figures below use a comma for thousands and a point for decimals (the Belastingdienst writes them the other way round). Where someone lives is decided on all the facts (AWR art. 4).
- **The three boxes.** Box 1: income from work and home (wages, business profit, other work, benefits, the own home). Box 2: income from a substantial interest of 5% or more in a company. Box 3: savings and investments. Each box has its own rate. Personal deductions reduce box 1 first, then box 3, then box 2, never below nil (Wet IB art. 6.2).
- **National insurance contributions** (premie volksverzekeringen: AOW, Anw, Wlz) are collected with income tax in the first box 1 band. A person who is not insured in the Netherlands for one of these schemes does not pay that contribution and does not get the matching part of each tax credit (Wfsv art. 10 and 12).
- **AOW age.** From the month a person reaches state pension (AOW) age, no AOW contribution is due (Wfsv art. 10(2)). The first band rate falls to 17.85%. The rates are below; the month-by-month table, the ouderenkorting and the AOW-age credits in full are in `nl-income-tax-special-groups`.
- **Fiscal partners** (fiscale partners) are taxed separately. They may divide common items (such as the own home, personal deductions, box 2 income, the joint box 3 base and dividend tax withheld) in any ratio they choose each year (Wet IB art. 2.17(2)). Wages and business profit stay with the person who earned them (art. 2.17(1)).
- **Not here:** entrepreneur reliefs (zelfstandigenaftrek, startersaftrek, hours test, MKB-winstvrijstelling detail, KIA, business costs and VAT in cost price) are in `nl-zzp-deductions`; the own home (eigenwoningforfait, mortgage interest, Wet Hillen), care costs, gifts and alimony are in `nl-deductions` and `netherlands-owner-occupied-home-tax-scheme`; the expat scheme in `nl-30-percent-ruling`; wage tax withholding in `nl-payroll-tax` and `netherlands-payroll`; non-residents and treaties in `nl-cross-border` and `nl-double-tax-relief`; objections in `nl-tax-objection`; crypto in `netherlands-crypto-tax`. Intake and the final return handoff use `nl-freelance-intake` and `nl-return-assembly`.

## Rates, bands and thresholds

| Item | Rate or amount | Year | Source |
|---|---|---|---|
| Box 1, below AOW age: first band | to EUR 38,883: 35.75% (8.10% income tax plus 27.65% national insurance: AOW 17.90%, Anw 0.10%, Wlz 9.65%) | 2026 | Wet IB art. 2.10(1), https://wetten.overheid.nl/BWBR0011353/2026-02-21 ; Wfsv art. 10-11, https://wetten.overheid.nl/BWBR0017745/2026-01-01 ; contribution rates: https://www.belastingdienst.nl/wps/wcm/connect/fisin/fisin2026/heffingskortingen |
| Box 1: second band | above EUR 38,883 to EUR 78,426: 37.56% | 2026 | Wet IB art. 2.10(1) |
| Box 1: third band | above EUR 78,426: 49.50% | 2026 | Wet IB art. 2.10(1) |
| Box 1, AOW age all year, born on or after 1 January 1946 | first band to EUR 38,883 at 17.85%; then 37.56% and 49.50% | 2026 | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/prive/inkomstenbelasting/heffingskortingen_boxen_tarieven/boxen_en_tarieven/box_1/box_1 |
| Box 1, born before 1 January 1946 | first band to EUR 41,123 at 17.85% (8.10% tax); 37.56% to EUR 78,426; 49.50% above | 2026 | Wet IB art. 2.10a(1); same Belastingdienst page |
| Box 1, AOW age reached during 2026 | first band rate by month reached: January 17.85% rising to December 34.26% | 2026 | same Belastingdienst page; Wfsv art. 10(2) |
| Tariefsaanpassing | extra 11.94% of the lower of (a) the deductions listed in art. 2.10(3) and (b) box 1 income plus those deductions above EUR 78,426; their value is capped at 37.56% | 2026 | Wet IB art. 2.10(2),(3) |
| Algemene heffingskorting (general credit), below AOW age | EUR 3,115, less 6.398% of verzamelinkomen above EUR 29,736; nil from EUR 78,426 | 2026 | Wet IB art. 8.10(2) |
| Algemene heffingskorting, AOW age all year | EUR 1,556, less 3.195% of verzamelinkomen above EUR 29,736; nil from EUR 78,426 | 2026 | https://www.belastingdienst.nl/wps/wcm/connect/fisin/fisin2026/heffingskortingen ; Wet IB art. 8.3-8.4 |
| Arbeidskorting (labour credit), below AOW age | 8.324% of labour income (max EUR 996); plus 31.009% above EUR 11,965 (total max EUR 5,300, reached at EUR 25,845); plus 1.950% above EUR 25,845 (total max EUR 5,685, reached at EUR 45,592); less 6.51% above EUR 45,592; nil from EUR 132,920 | 2026 | Wet IB art. 8.11(2) |
| Arbeidskorting, AOW age all year | 4.156% to EUR 11,965; EUR 498 + 15.483% to EUR 25,845; EUR 2,647 + 0.974% to EUR 45,592; EUR 2,840 less 3.250% above EUR 45,592; nil from EUR 132,920 | 2026 | Belastingdienst heffingskortingen 2026 (above) |
| Arbeidskorting floor | if labour income is not above EUR 45,592: at least the labour credit the employer applied in payroll, up to EUR 5,685 | 2026 | Wet IB art. 8.11(2), last sentence |
| Inkomensafhankelijke combinatiekorting | 11.45% of labour income above EUR 6,239, max EUR 3,032; a child under 12 at the start of the year in the household for at least six months; no partner, or the lower labour income of the two | 2026 | Wet IB art. 8.14a |
| Ouderenkorting; alleenstaande ouderenkorting | EUR 2,067 less 15% of verzamelinkomen above EUR 46,002; EUR 540 | 2026 | Wet IB art. 8.17, 8.18 |
| Box 2 (aanmerkelijk belang) | 24.5% to EUR 68,843; 31% above | 2026 | Wet IB art. 2.12 |
| Box 3 rate | 36% | 2026 | Wet IB art. 2.13 |
| Box 3 deemed return: other assets | 6.00%, fixed at the start of the year | 2026 | Wet IB art. 5.2(2), 10.6ter(3); https://www.belastingdienst.nl/wps/wcm/connect/nl/box-3/content/berekening-box-3-inkomen-2026 |
| Box 3 deemed return: bank balances and debts | provisional 1.28% (bank) and 2.70% (debts), used in the 2026 voorlopige aanslag; the final figures are set by ministerial regulation after the year ends, back to 1 January 2026 | 2026 | Wet IB art. 10.6ter(2),(4); same Belastingdienst page |
| Box 3 tax-free allowance (heffingvrij vermogen) | EUR 59,357 per person (EUR 118,714 for whole-year fiscal partners) | 2026 | Wet IB art. 5.5, 5.2(5) |
| Box 3 debt threshold | first EUR 3,800 of debts not counted (EUR 7,600 for whole-year partners) | 2026 | Wet IB art. 5.3(3)(f) |
| Box 3 actual return (tegenbewijsregeling) | if the actual return is lower than the deemed benefit, the actual return is taxed, never below nil | 2026 | Wet IB art. 5.25-5.30 |
| Bijdrage Zvw (income-related health contribution) on profit and other income without payroll | 4.85% up to EUR 79,409 of contribution income | 2026 | https://www.belastingdienst.nl/wps/wcm/connect/fisin/fisin2026/inkomensafhankelijke_bijdrage_zorgverzekeringswet |
| Belastingrente | 5% a year from 1 January 2026 (6.5% in 2025) | 2026 | AWR art. 30hb; https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/standaard_functies/prive/contact/rechten_en_plichten_bij_de_belastingdienst/belastingrente/overzicht_percentages_belastingrente |
| Verzuimboete, late income tax return | EUR 469; up to EUR 6,709 for repeat failure | 2026 | AWR art. 67a; https://www.belastingdienst.nl/wps/wcm/connect/nl/belastingaangifte/content/wat-gebeurt-er-als-ik-geen-aangifte-doe-of-te-laat-of-onvolledig |
| Vergrijpboete | up to 100% of the tax not levied | 2026 | AWR art. 67d, 67e |
| 2025, box 1 below AOW age | 35.82% to EUR 38,441 (8.17% tax); 37.48% to EUR 76,817; 49.50% above | 2025 | Belastingdienst box 1 page (above) |
| 2025, general credit | EUR 3,068 less 6.337% above EUR 28,406; nil from EUR 76,817 (AOW age: EUR 1,536 less 3.170%) | 2025 | https://www.belastingdienst.nl/wps/wcm/connect/fisin/fisin2025/heffingskortingen |
| 2025, labour credit | 8.053% to EUR 12,169; EUR 980 + 30.030% to EUR 26,288; EUR 5,220 + 2.258% to EUR 43,071; EUR 5,599 less 6.510% above; nil from EUR 129,078 | 2025 | same 2025 page |
| 2025, box 3 | bank 1.37%, other assets 5.88%, debts 2.70%; allowance EUR 57,684 (partners EUR 115,368) | 2025 | Wet IB art. 5.2 as changed by Stcrt. 2026, 3708; https://www.belastingdienst.nl/wps/wcm/connect/nl/box-3/content/berekening-box-3-inkomen-2025 |

## The taxable base

**Box 1.** Add up taxable profit from a business (after the ondernemersaftrek and the MKB-winstvrijstelling, which is 12.7% of profit after the ondernemersaftrek, Wet IB art. 3.79a; method in `nl-zzp-deductions`), wages, income from other work, periodic benefits and the own-home balance (forfait minus deductible costs, in `nl-deductions`). Deduct income provisions and personal deductions. Apply art. 2.10 band by band, never one rate to the whole amount. Then apply the tariefsaanpassing if box 1 income plus the listed deductions exceeds EUR 78,426. The listed deductions are the ondernemersaftrek, the MKB-winstvrijstelling (when profit after ondernemersaftrek is positive), the terbeschikkingstellingsvrijstelling, own-home costs and the persoonsgebonden aftrek (art. 2.10(3)). No new additions to the oudedagsreserve (FOR) are possible: art. 3.67 and 3.68 lapsed on 1 January 2023.

**Tax credits.** Credits reduce income tax and national insurance together; they never reduce income (Wet IB ch. 8). Each credit has a tax part and parts for AOW, Anw and Wlz, in proportion to the first-band rates (8.10, 17.90, 0.10 and 9.65 out of 35.75). A person who is not insured for a scheme does not get that part (Wet IB art. 8.3-8.7; Wfsv art. 12).
- The general credit runs on **verzamelinkomen** (the total of the three boxes).
- The labour credit runs on **arbeidsinkomen**: wages, profit **before** the ondernemersaftrek and the MKB-winstvrijstelling, and income from other work (Wet IB art. 8.1(1)(e); Belastingdienst heffingskortingen 2026, ch. 21.10).
- Credits are capped at the combined income tax and contributions due (art. 8.8). A partner born before 1963 whose income is too low to use the general credit has it raised up to the general credit, at most the tax and contributions the other partner owes after that partner's credits, if they had the same partner for more than six months (art. 8.9). The Belastingdienst pays this part out.
- Employers apply the general and labour credits in payroll. Compute the annual entitlement once, then credit the wage tax withheld once (art. 9.2).

**Box 2.** Regular benefits (such as dividends) and capital gains on a substantial interest, taxed under art. 2.12. Fiscal partners can divide box 2 income as a common item. Detail in `nl-box2-substantial-interest`.

**Box 3 for 2026: what the law says.**
1. **The deemed system still applies.** The bridging rules (Overbruggingswetgeving) in Wet IB art. 5.2 tax a deemed return on assets and debts at 1 January (the peildatum). Rendement = bank balances x bank rate + other assets x 6.00% - (debts above the threshold) x debt rate, set at nil if negative. The rendementsgrondslag is assets minus counted debts. The grondslag sparen en beleggen is the rendementsgrondslag less the tax-free allowance. The benefit (voordeel) = rendement / rendementsgrondslag x grondslag sparen en beleggen (art. 5.2(1),(2)). Whole-year partners add assets, debts and allowances together and divide the joint base in any ratio (art. 5.2(5), 2.17).
2. **The Hoge Raad rulings.** On 24 December 2021 (ECLI:NL:HR:2021:1963) the Hoge Raad held that box 3 for 2017 and 2018 breached art. 1 of the First Protocol together with art. 14 ECHR, and ordered redress. On 6 June 2024 (ECLI:NL:HR:2024:705) it held that the Herstelwet system breaches the same articles and that redress means taxing the actual return. The Belastingdienst states that, under these rulings, it must tax the actual return when that is lower than the deemed return.
3. **The tegenbewijsregeling.** The law now says this itself. If the taxpayer shows that the actual return (werkelijk rendement) is lower than the deemed benefit, box 3 income is the actual return, never below nil (Wet IB art. 5.25(1),(2)). Actual return = regular benefits (interest, rent, dividends, the economic rental value of property used privately) less interest paid on debts, plus the change in value of all assets and debts over the year, adjusted for deposits and withdrawals (art. 5.26-5.30). Unrealised gains and losses count. In the actual-return calculation the debt threshold and some exemptions (art. 5.10(a),(d) and 5.13, green investments) do not apply (art. 5.26(3)). For partners, the joint actual return is allocated in the same ratio as the joint base (art. 5.25(4)). A minor child's actual return goes to the parent (art. 5.25(3)). A negative actual return counts as nil.
4. **How it is claimed.** For 2025 the Belastingdienst asks for the actual return inside the return and taxes the more favourable figure. Otherwise the claim uses the inspector's form, with six weeks to add documents (art. 5.25(6)-(8)). The 2026 voorlopige aanslag uses the deemed method only, because the actual return is known only after the year ends.

**Part-year residence.** A person who becomes resident during the year, or stops being resident other than by death, uses the base at the start of the year, time-apportioned by whole months (art. 5.2(6)). Migration cases go to `nl-cross-border`.

## Deadlines and filing

- **Annual return.** Filed online in Mijn Belastingdienst. The deadline is in the invitation letter and is at least one month after the invitation (AWR art. 9(1)). For most people it is 1 May of the following year: 1 May 2027 for 2026.
- **Who must file.** Anyone invited to file. Without a letter, for the 2025 return: file if you owe EUR 58 or more (before 14 July to avoid a penalty), and you may file for a refund of EUR 19 or more.
- **Extension (uitstel).** Ask before the date in the letter, on the paper form; it cannot be requested online. An extension gives four more months. The inspector can attach conditions (AWR art. 9(2)). Filing later than 1 May can lead to belastingrente (see below).
- **Voorlopige aanslag.** The inspector may issue a provisional assessment up to the expected final tax; a positive one is not issued before the year starts (AWR art. 13). A taxpayer can request or change one online and pay it monthly. The final assessment offsets all provisional assessments and the wage tax and dividend tax withheld (AWR art. 15; Wet IB art. 9.2).
- **Bijdrage Zvw.** Assessed separately, next to the income tax assessment (see `nl-social-contributions`).

## Penalties and interest

- **Belastingrente.** Charged on an income tax assessment with tax to pay that is set more than six months after the year ends. It runs from 1 July of the next year until the day before the assessment is payable (AWR art. 30f(1),(2)). No interest if the assessment follows a return received before 1 May, or a provisional-assessment request received before 1 May (art. 30f(4)). Rate 5% from 1 January 2026. Refund interest (art. 30fa) applies when the Belastingdienst takes more than 8 weeks after a request, or 13 weeks after a return, to set a refund.
- **Late filing.** First a reminder, then a formal aanmaning. A return not filed by the date in the aanmaning gives a verzuimboete of EUR 469, up to EUR 6,709 for repeat failure (AWR art. 67a). No penalty if there is no fault at all.
- **Under-declaration.** A deliberately missing, wrong or incomplete return: a vergrijpboete of up to 100% of the tax, imposed with the assessment (AWR art. 67d). Too little tax through intent or gross negligence found later: up to 100%, imposed with the navorderingsaanslag (AWR art. 67e).

## Cross-border points

- **Residence** is decided on all the facts (AWR art. 4). Non-residents are taxed under Wet IB ch. 7 on Dutch income only and do not get the national-insurance parts of the credits if not insured here. Detail in `nl-cross-border` and `nl-double-tax-relief`.
- **Foreign income of a resident** is taxed in the boxes, with relief under a treaty or the Dutch unilateral rules (`nl-double-tax-relief`).
- **Foreign assets** count in box 3 at their value on 1 January. A foreign second home is an "other asset" (6.00%).
- **Incoming employees** may have the expat scheme (30% ruling): see `nl-30-percent-ruling` for its effect on the boxes.
- **Arrival or departure in the year:** box 3 is time-apportioned (art. 5.2(6)); everything else on migration is in `nl-cross-border`.

## Worked examples

**Example 1: sole trader, below AOW age, no partner (simple).** Profit before entrepreneur reliefs EUR 50,000. Meets the hours test; not a starter. Zelfstandigenaftrek EUR 1,200 (art. 3.76(2), see `nl-zzp-deductions`). MKB-winstvrijstelling 12.7% of 48,800 = EUR 6,197.60. Taxable profit EUR 42,602.40; no other income or deductions. Box 1: 38,883 x 35.75% = 13,900.67; (42,602.40 - 38,883) x 37.56% = 1,397.01; total EUR 15,297.68. General credit on verzamelinkomen 42,602.40: 3,115 - 6.398% x 12,866.40 = EUR 2,291.81. Labour credit on labour income 50,000 (profit before reliefs): 5,685 - 6.51% x 4,408 = EUR 5,398.04. Income tax and contributions due EUR 7,607.83, before the return software's rounding. No tariefsaanpassing: 42,602.40 + 1,200 + 6,197.60 = 50,000, below EUR 78,426. The bijdrage Zvw comes on top, assessed separately.

```oa-check
name: Sole trader, profit EUR 50,000 before reliefs (2026)
inputs:
  profit: 50000
  zelfstandigenaftrek: 1200
steps:
  - mkb: (profit - zelfstandigenaftrek) * 0.127
  - taxable: profit - zelfstandigenaftrek - mkb
  - band1: min(taxable, 38883) * 0.3575
  - band2: max(min(taxable, 78426) - 38883, 0) * 0.3756
  - band3: max(taxable - 78426, 0) * 0.495
  - tax_before_credits: band1 + band2 + band3
  - ahk: max(3115 - max(taxable - 29736, 0) * 0.06398, 0)
  - ak: max(5685 - max(profit - 45592, 0) * 0.0651, 0)
  - net: max(tax_before_credits - ahk - ak, 0)
expected:
  taxable: 42602.40
  tax_before_credits: 15297.68
  ahk: 2291.81
  ak: 5398.04
  net: 7607.83
```

**Example 2: box 3 for fiscal partners, with a lower actual return (edge case).** Whole-year fiscal partners. On 1 January 2026 they hold bank balances EUR 80,000, shares EUR 150,000 and a consumer loan of EUR 10,000. Debts counted: 10,000 - 7,600 = EUR 2,400. Rendement with the provisional 2026 rates: 80,000 x 1.28% + 150,000 x 6.00% - 2,400 x 2.70% = EUR 9,959.20. Rendementsgrondslag 230,000 - 2,400 = EUR 227,600. Grondslag sparen en beleggen 227,600 - 118,714 = EUR 108,886. Joint deemed benefit 9,959.20 x 108,886 / 227,600 = EUR 4,764.58. Their actual return for 2026, worked out on the Belastingdienst's form, is EUR 3,000. That is lower, so EUR 3,000 is taxed (art. 5.25). Box 3 tax 36% = EUR 1,080; split 50/50, EUR 540 each. The bank and debt rates are provisional: recompute once the final 2026 figures are set.

```oa-check
name: Box 3 partners, deemed vs actual return (2026 provisional rates)
inputs:
  bank: 80000
  shares: 150000
  debt: 10000
  actual_return: 3000
steps:
  - counted_debt: max(debt - 7600, 0)
  - rendement: max(bank * 0.0128 + shares * 0.06 - counted_debt * 0.027, 0)
  - grondslag: bank + shares - counted_debt
  - base: max(grondslag - 118714, 0)
  - deemed: rendement * base / grondslag
  - taxed: min(deemed, max(actual_return, 0))
  - tax: taxed * 0.36
  - tax_each: tax / 2
expected:
  rendement: 9959.20
  base: 108886.00
  deemed: 4764.58
  taxed: 3000.00
  tax: 1080.00
  tax_each: 540.00
```

## Ask the client first

1. Date of birth and the month AOW age is reached; resident and insured in the Netherlands all year? (Sets the rate table and the credit parts.)
2. A fiscal partner for the whole year, and how do you want to divide the common items and the box 3 base?
3. Every source of box 1 income: annual wage statements (jaaropgaaf), business accounts and hours, other-work income, the own home.
4. Every asset and debt on 1 January 2026 (including abroad and crypto), and records of income and value changes during 2026 if the actual return may be lower.
5. Any shareholding of 5% or more in a company?
6. Letters already received: invitation to file, extension, voorlopige aanslag, earlier assessments and unused deductions or losses.

## Sources

| Source | URL | Read on |
|---|---|---|
| Wet inkomstenbelasting 2001, version in force from 21 February 2026 (art. 2.10, 2.10a, 2.12, 2.13, 2.17, 3.67, 3.68, 3.76, 3.79a, 5.1-5.5, 5.25-5.30, 6.2, 8.1, 8.8-8.11, 8.14a, 8.17, 8.18, 9.2, 10.6ter) | https://wetten.overheid.nl/BWBR0011353/2026-02-21 | 2026-10-24 |
| Wet inkomstenbelasting 2001, version 1 January 2026 (art. 5.2 before the retroactive 2025 change in Stcrt. 2026, 3708) | https://wetten.overheid.nl/BWBR0011353/2026-01-01 | 2026-10-24 |
| Wet financiering sociale verzekeringen, art. 9-12 | https://wetten.overheid.nl/BWBR0017745/2026-01-01 | 2026-10-24 |
| Algemene wet inzake rijksbelastingen (art. 4, 9, 13, 15, 30f, 30fa, 30hb, 67a, 67d, 67e) | https://wetten.overheid.nl/BWBR0002320/ | 2026-10-24 |
| Belastingdienst, box 1 rates 2026 and 2025, AOW-age month table | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/prive/inkomstenbelasting/heffingskortingen_boxen_tarieven/boxen_en_tarieven/box_1/box_1 | 2026-10-24 |
| Fiscale informatie 2026 ch. 21, tax credits | https://www.belastingdienst.nl/wps/wcm/connect/fisin/fisin2026/heffingskortingen | 2026-10-24 |
| Fiscale informatie 2025, tax credits | https://www.belastingdienst.nl/wps/wcm/connect/fisin/fisin2025/heffingskortingen | 2026-10-24 |
| Fiscale informatie 2026 ch. 28, bijdrage Zvw | https://www.belastingdienst.nl/wps/wcm/connect/fisin/fisin2026/inkomensafhankelijke_bijdrage_zorgverzekeringswet | 2026-10-24 |
| Belastingdienst, box 3 on the 2026 voorlopige aanslag | https://www.belastingdienst.nl/wps/wcm/connect/nl/box-3/content/berekening-box-3-inkomen-2026 | 2026-10-24 |
| Belastingdienst, box 3 for 2025 | https://www.belastingdienst.nl/wps/wcm/connect/nl/box-3/content/berekening-box-3-inkomen-2025 | 2026-10-24 |
| Belastingdienst, actual return in the 2025 return | https://www.belastingdienst.nl/wps/wcm/connect/nl/box-3/content/werkelijk-rendement-belastingaangifte | 2026-10-24 |
| Hoge Raad 24 December 2021, ECLI:NL:HR:2021:1963 | https://uitspraken.rechtspraak.nl/details?id=ECLI:NL:HR:2021:1963 | 2026-10-24 |
| Hoge Raad 6 June 2024, ECLI:NL:HR:2024:705 | https://uitspraken.rechtspraak.nl/details?id=ECLI:NL:HR:2024:705 | 2026-10-24 |
| Belastingdienst, when to file | https://www.belastingdienst.nl/wps/wcm/connect/nl/belastingaangifte/content/wanneer-moet-ik-aangifte-doen | 2026-10-24 |
| Belastingdienst, must I file (2025 thresholds) | https://www.belastingdienst.nl/wps/wcm/connect/nl/belastingaangifte/content/moet_ik_aangifte_doen | 2026-10-24 |
| Belastingdienst, extension | https://www.belastingdienst.nl/wps/wcm/connect/nl/belastingaangifte/content/kan-ik-nog-uitstel-aanvragen-belastingaangifte | 2026-10-24 |
| Belastingdienst, voorlopige aanslag | https://www.belastingdienst.nl/wps/wcm/connect/nl/voorlopige-aanslag/content/hoge-belastingaanslag-voorlopige-aanslag | 2026-10-24 |
| Belastingdienst, belastingrente percentages | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/standaard_functies/prive/contact/rechten_en_plichten_bij_de_belastingdienst/belastingrente/overzicht_percentages_belastingrente | 2026-10-24 |
| Belastingdienst, late or missing return | https://www.belastingdienst.nl/wps/wcm/connect/nl/belastingaangifte/content/wat-gebeurt-er-als-ik-geen-aangifte-doe-of-te-laat-of-onvolledig | 2026-10-24 |
| Belastingplan 2027 bill, Kamerstuk 37022 nr. 2 (art. I, art. LXIII) | https://zoek.officielebekendmakingen.nl/kst-37022-2.html | 2026-10-24 |

Pending law: the Belastingplan 2027 bill (Kamerstuk 37022, sent to the Tweede Kamer on 29 September 2026, not enacted on 24 October 2026) would apply some changes back to 1 January 2026 (art. LXIII(1)(a)): the car rate in Wet IB art. 3.15(6), 3.17(1)(b), 6.17(6) and 6.36(2) from EUR 0.23 to EUR 0.25 per km, an amendment to art. 3.76(3) (the starter's increase of the zelfstandigenaftrek) and the classic-car age rule in art. 3.20(5). See `nl-zzp-deductions` and `nl-deductions`. Its new box 1 table (first band 8.58% to EUR 39,247, second band 38.16%) and the higher labour credit take effect from 2027, not 2026.

Not yet confirmed: (1) the final 2026 box 3 bank and debt percentages (set after the year ends; 1.28% and 2.70% are provisional; the statute text currently reads 1.37% and 2.70%); (2) whether the Hoge Raad has ruled on the 2026 bridging rules as such (only the 2021 and 2024 rulings were read); (3) the late-payment penalty (betaalverzuimboete) amount for income tax and the vergrijpboete percentages in the Besluit Bestuurlijke Boeten Belastingdienst (not read); (4) the 2026 filing thresholds (EUR 58 and EUR 19 are for the 2025 return); (5) the bijdrage Zvw base for a sole trader (profit before or after the entrepreneur reliefs), left to `nl-social-contributions`; (6) the conserving assessment on emigration, left to `nl-cross-border`.

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
