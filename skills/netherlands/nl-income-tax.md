---
name: nl-income-tax
description: "Dutch resident personal income tax for 2026: box 1 tax and national insurance, general and labour credits, fiscal-partner allocation, box 2 rates, box 3 provisional deemed return and lower actual return, filing, provisional assessments, interest and penalties. Includes sole-trader and partner computations. Refers age-related credits, specialist deductions, cross-border cases and other unresolved specialist calculations to partner accountants. Trigger phrases: aangifte inkomstenbelasting, box 1 tarief, heffingskortingen, arbeidskorting, box 3 werkelijk rendement, tegenbewijsregeling, voorlopige aanslag, belastingrente."
version: 2.6
jurisdiction: NL
tax_year: 2026
last_updated: 2026-11-26
depends_on:
  - income-tax-workflow-base
category: international
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
type: computation
---

# Netherlands: personal income tax (inkomstenbelasting) 2026

## Who this applies to

This Guide covers resident individuals for the calendar year 2026. Residence depends on all the circumstances (AWR art. 4). The box 1 and credit computations below assume residence and insurance for AOW, Anw and Wlz throughout the year, and a person below AOW age throughout the year. Amounts are in euros.

The three categories are box 1 (work and home), box 2 (substantial interest) and box 3 (savings and investments), under Wet IB art. 2.3. Personal deductions reduce box 1, then box 3, then box 2, each no lower than nil; use `nl-deductions` for eligibility and remaining deductions (art. 6.2). Box 1 includes taxable business profit, wages, other work, periodic benefits and the own-home balance. Establish these amounts before computing the tax.

**Required inputs:** age and AOW month; residence and insurance periods; fiscal-partner dates; income in all three boxes; business profit and hours; personal deductions and losses; assets and debts on 1 January; actual-return records; and all filing invitations, extensions, withholding statements and assessments. For company interests, obtain direct and indirect shareholdings, partner holdings, options and other profit or voting rights; do not screen on the person's own shares alone.

**Age, insurance and additional credits.** AOW-age rates, part-year insurance, the inkomensafhankelijke combinatiekorting, ouderenkorting, alleenstaande ouderenkorting and a low-income partner's credit payment need a separate calculation (`nl-income-tax-special-groups`). Check this point with one of our partner accountants.

**Other specialist work.** Entrepreneur eligibility, startersaftrek, hours, KIA, costs, VAT and existing FOR balances: `nl-zzp-deductions`. Own-home deductions, Wet Hillen, care, gifts and alimony: `nl-deductions` and `netherlands-owner-occupied-home-tax-scheme`. Payroll: `nl-payroll-tax`; objections: `nl-tax-objection`; crypto: `netherlands-crypto-tax`; intake and assembly: `nl-freelance-intake` and `nl-return-assembly`. Check this point with one of our partner accountants.

## Rates, bands and thresholds

All figures in this table are for 2026 and the scope above. Apply the fixed statutory amounts rather than multiplying the combined headline rates across every band.

| Item | Rate or amount | Official source |
|---|---|---|
| Box 1 income tax | 8.10% to EUR 38,883; above EUR 38,883 to EUR 78,426: EUR 3,149 + 37.56% of the excess above EUR 38,883; above EUR 78,426: EUR 18,001 + 49.50% of the excess above EUR 78,426 | Wet IB art. 2.10(1), https://repository.officiele-overheidspublicaties.nl/bwb/BWBR0011353/2026-02-21_0/xml/BWBR0011353_2026-02-21_0.xml |
| National insurance, separate from income tax | AOW 17.90%, Anw 0.10%, Wlz 9.65%: total 27.65% of premium income, capped at EUR 38,883. Maximum EUR 10,751.15 before credits, computed. First-band headline total 35.75% = 8.10% + 27.65% | Wfsv arts. 8, 10-12, https://wetten.overheid.nl/BWBR0017745/2026-01-01 ; https://www.belastingdienst.nl/wps/wcm/connect/fisin/fisin2026/heffingskortingen |
| General credit, before the overall levy cap | EUR 3,115 less 6.398% of verzamelinkomen above EUR 29,736, floored at nil | Wet IB art. 8.10, https://repository.officiele-overheidspublicaties.nl/bwb/BWBR0011353/2026-02-21_0/xml/BWBR0011353_2026-02-21_0.xml |
| Labour credit, before the overall levy cap | Use the statutory cumulative formula below; maximum EUR 5,685, then a 6.51% reduction above EUR 45,592 | Wet IB art. 8.11, https://repository.officiele-overheidspublicaties.nl/bwb/BWBR0011353/2026-02-21_0/xml/BWBR0011353_2026-02-21_0.xml |
| Box 2 income tax | 24.5% to EUR 68,843; above it EUR 16,866 + 31% of the excess above EUR 68,843 | Wet IB art. 2.12, https://repository.officiele-overheidspublicaties.nl/bwb/BWBR0011353/2026-02-21_0/xml/BWBR0011353_2026-02-21_0.xml |
| Box 3 income tax | 36% of taxable box 3 income | Wet IB art. 2.13, https://repository.officiele-overheidspublicaties.nl/bwb/BWBR0011353/2026-02-21_0/xml/BWBR0011353_2026-02-21_0.xml |
| Box 3 deemed return percentages | Bank 1.28% and debts 2.70% are provisional for the 2026 voorlopige aanslag; other assets 6.00% is fixed. Recompute with final bank/debt rates when set after year-end | https://www.belastingdienst.nl/wps/wcm/connect/nl/box-3/content/berekening-box-3-inkomen-2026 ; Wet IB art. 10.6ter, https://repository.officiele-overheidspublicaties.nl/bwb/BWBR0011353/2026-02-21_0/xml/BWBR0011353_2026-02-21_0.xml |
| Box 3 allowance | EUR 59,357 per person; EUR 118,714 for whole-year fiscal partners | Wet IB arts. 5.5, 5.2(5), https://repository.officiele-overheidspublicaties.nl/bwb/BWBR0011353/2026-02-21_0/xml/BWBR0011353_2026-02-21_0.xml ; https://www.belastingdienst.nl/wps/wcm/connect/nl/box-3/content/berekening-box-3-inkomen-2026 |
| Box 3 debt threshold | EUR 3,800 per person; EUR 7,600 for whole-year fiscal partners | Wet IB art. 5.3(3)(f), https://repository.officiele-overheidspublicaties.nl/bwb/BWBR0011353/2026-02-21_0/xml/BWBR0011353_2026-02-21_0.xml |

## The taxable base

**Box 1.** Use the taxable amounts after applicable deductions, then the statutory tax table. For an eligible sole trader below AOW age at the start of 2026 who meets the hours test, the ordinary zelfstandigenaftrek is EUR 1,200, limited to profit unless the starter exception applies (art. 3.76). The MKB-winstvrijstelling is 12.7% of entrepreneurial profit after the ondernemersaftrek (art. 3.79a). These rules supply Example 1; other entrepreneur eligibility and reliefs need the specialist referral above.

**Tariefsaanpassing.** Add 11.94% of the lower of the listed deductions and the positive excess of box 1 income plus those deductions over EUR 78,426. Listed deductions are the ondernemersaftrek; MKB-winstvrijstelling only where profit after ondernemersaftrek is positive; terbeschikkingstellingsvrijstelling only where the joint result from the relevant activities is positive; deductible own-home costs; and personal deductions (art. 2.10(2)-(3)).

**Tax credits.** Compute the general credit on verzamelinkomen, the combined income of the three boxes excluding conserving income (arts. 2.18, 8.10). For labour income A, the statutory labour-credit formula is:

- B = min(8.324% × A, EUR 996).
- C = min(B + 31.009% × max(A − EUR 11,965, 0), EUR 5,300).
- D = min(C + 1.950% × max(A − EUR 25,845, 0), EUR 5,685).
- Credit = max(D − 6.51% × max(A − EUR 45,592, 0), 0).

If labour income is no more than EUR 45,592, the credit is at least the labour credit granted on wages under the statutory payroll tables, capped at EUR 5,685 (art. 8.11(2)). Labour income includes entrepreneurial profit **before** ondernemersaftrek and MKB-winstvrijstelling. Passive profit participations and profit-sharing creditor income do not count as entrepreneurial labour income; income from making assets available to a connected person does not count as other-work labour income. Wages and active other-work income count; a Ziektewet benefit for a period without an employment contract does not count (Fiscale informatie 2026, 21.10).

Combined credits reduce the combined income tax and national insurance, not income, and cannot exceed that combined levy after applicable double-tax relief (arts. 8.1, 8.8). Compute annual credits once and offset eligible wage tax withheld once in the final settlement (art. 9.2). Dividend-tax offsets, beneficial ownership and pension-account exclusions need separate assessment. Check this point with one of our partner accountants.

**Fiscal partners.** For two all-year residents with the same fiscal partner throughout the calendar year, common items are the taxable own-home balance, box 2 income before personal deductions, and personal deductions. They choose each item's allocation in their returns. Wages and entrepreneurial profit remain with the earner (art. 2.17(1)-(5)). Combine assets, counted debts and allowances for the joint box 3 computation and allocate the joint base; joint actual return follows that same allocation ratio (arts. 5.2(5), 5.25(4)-(5)). For part-year partnerships, a whole-year election or migration exceptions, check eligibility separately. Check this point with one of our partner accountants.

**Box 2 classification.** Establish substantial-interest status before using the rate table. Other share classes, partner aggregation, indirect holdings, options, profit and voting rights need review (`nl-box2-substantial-interest`). Check this point with one of our partner accountants.

**Box 3 deemed method.** Use the value of taxable box 3 assets and deductible debts on 1 January. Count debts only above the debt threshold. Rendement = max(bank × bank rate + other assets × other-assets rate − counted debts × debt rate, 0). Rendementsgrondslag = taxable assets − counted debts. Grondslag sparen en beleggen = max(rendementsgrondslag − allowance, 0). If this base is zero, the deemed benefit is zero; otherwise deemed benefit = rendement × base / rendementsgrondslag (arts. 5.2-5.3). Example 2 uses the provisional rates, not final rates for a 2026 filing.

**Lower actual return (tegenbewijsregeling).** If the taxpayer demonstrates that the complete statutory actual return is lower than the deemed benefit, substitute that actual return, floored at nil, before deducting any remaining personal deductions (art. 5.25(1)-(2)). The 2026 preliminary assessment uses only the deemed method; actual return is known after year-end. The Belastingdienst explains this obligation by reference to the Hoge Raad rulings. Use the inspector's form unless the information is requested as part of the return invitation; with the separate form, additional documents may be sent up to six weeks after sending it (art. 5.25(6)-(8)).

**Establishing actual return.** Interest, dividends, rent, debt interest, unrealised changes, deposits and withdrawals, private-use property and improvements, exemption differences, green investments and minor-child attribution require a complete calculation under arts. 5.25-5.31. Do not substitute cash receipts or the deemed allowance for that calculation. Check this point with one of our partner accountants.

**Bijdrage Zvw.** This is a separate assessment beside income tax. Establish its contribution base, rate and remaining cap after other insured income separately (`nl-social-contributions`); the examples do not compute it. Check this point with one of our partner accountants.

## Deadlines and filing

- **Annual return.** File when invited. Use the deadline in the invitation: AWR art. 9(1) requires at least one month after invitation. Do not infer an individual 2026-return deadline from the customary 1 May date. No invitation, current filing/refund thresholds, benefit-related wealth reporting and older returns: Check this point with one of our partner accountants.
- **Extension.** Ask before the invitation deadline. The inspector may extend the period and impose conditions (AWR art. 9(2)). Establish the applicable year's application route and granted date; do not carry the 2025 late-season paper-only procedure into the 2026 return. Check this point with one of our partner accountants.
- **Voorlopige aanslag.** A positive provisional assessment is not set before the tax year starts and is limited to the estimated final balance after statutory offsets (AWR art. 13). A request or change can be made online; monthly advance payments are possible. Provisional assessments and legally eligible withholding are offset in the final assessment (AWR art. 15).
- **2025 returns and prospective changes.** For 2025 rates, credits and box 3, or the effect of Belastingplan 2027 amendments on 2026 deductions and cars, establish the applicable law separately rather than using this 2026 table. Check this point with one of our partner accountants.

## Penalties and interest

| Point | Rule | Official source |
|---|---|---|
| Belastingrente percentage | 5% annually from 1 January 2026. This is an interest-period rate, not a guarantee of the rate accruing in 2027 on a 2026 return | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/standaard_functies/prive/contact/rechten_en_plichten_bij_de_belastingdienst/belastingrente/overzicht_percentages_belastingrente |
| Late filing | For a living taxpayer: after the reminder and formal aanmaning, missing the demand's deadline can give a EUR 469 default penalty; repeated failures can reach EUR 6,709. No penalty where there is no fault whatsoever | https://www.belastingdienst.nl/wps/wcm/connect/nl/belastingaangifte/content/wat-gebeurt-er-als-ik-geen-aangifte-doe-of-te-laat-of-onvolledig ; https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/standaard_functies/prive/contact/rechten_en_plichten_bij_de_belastingdienst/boete |
| Under-declaration standards | Ordinary tax: 25% for gross negligence, 50% for intent. The corresponding box 3 standards are 75% and 150%. Circumstances may increase or decrease them; the statutory maxima are 100% of the ordinary statutory penalty base and 300% for the box 3 portion. Intentional failure or an incorrect/incomplete return falls under art. 67d; intent or gross negligence causing underassessment falls under art. 67e. The statutory penalty base can disregard losses and carried personal deductions | AWR arts. 67d-67e, https://wetten.overheid.nl/BWBR0002320/ ; https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/standaard_functies/prive/contact/rechten_en_plichten_bij_de_belastingdienst/boete |
| Assessment-payment default: statutory power | Invorderingswet 1990 art. 63b(1) permits a penalty up to EUR 6,709 where an assessment is unpaid, partly paid or paid outside the term(s) on the assessment. It is incorrect to say that there is no statutory power | https://repository.officiele-overheidspublicaties.nl/bwb/BWBR0004770/2026-10-01_0/xml/BWBR0004770_2026-10-01_0.xml |

For an actual interest calculation, distinguish provisional, final and additional assessments, conformity to the return/request, interest caps, refunds and conserving assessments. Check this point with one of our partner accountants.

For assessment-payment penalty policy, including when a penalty is imposed and any standard percentage/minimum, and individual penalty mitigation or objections: Check this point with one of our partner accountants.

## Cross-border points

Residence follows AWR art. 4. Non-resident status, foreign income, foreign homes and other assets, treaty/unilateral relief, expat treatment, arrival/departure apportionment and conserving assessments need a case-specific calculation (`nl-cross-border`, `nl-double-tax-relief`, `nl-30-percent-ruling`). Check this point with one of our partner accountants.

## Worked examples

**Example 1: sole trader, below AOW age, no partner (simple).** Profit before entrepreneur reliefs EUR 50,000. Resident and insured for AOW, Anw and Wlz throughout 2026; below AOW age throughout the year. Meets the hours test; not a starter. Assume no unused deductions, losses or additional credits. Zelfstandigenaftrek EUR 1,200 (art. 3.76(2), see `nl-zzp-deductions`). MKB-winstvrijstelling 12.7% of 48,800 = EUR 6,197.60. Taxable profit EUR 42,602.40; no other income or deductions. Taxable income is in the second band, so box 1 income tax by the art. 2.10 table is 3,149 + (42,602.40 - 38,883) x 37.56% = 3,149 + 1,397.01 = 4,546.01. National insurance premium: 38,883 x 27.65% = 10,751.15. Total EUR 15,297.16. General credit on verzamelinkomen 42,602.40: 3,115 - 6.398% x 12,866.40 = EUR 2,291.81. Labour credit on labour income 50,000 (profit before reliefs): 5,685 - 6.51% x 4,408 = EUR 5,398.04. Income tax and contributions due EUR 7,607.31, before the return software's rounding. No tariefsaanpassing: 42,602.40 + 1,200 + 6,197.60 = 50,000, below EUR 78,426. The bijdrage Zvw comes on top, assessed separately; its base is a separate calculation (see the Zvw referral above).

```oa-check
name: Sole trader, profit EUR 50,000 before reliefs (2026)
inputs:
  profit: 50000
  zelfstandigenaftrek: 1200
steps:
  - mkb: (profit - zelfstandigenaftrek) * 0.127
  - taxable: profit - zelfstandigenaftrek - mkb
  - income_tax: 3149 + (taxable - 38883) * 0.3756
  - premium: min(taxable, 38883) * 0.2765
  - tax_before_credits: income_tax + premium
  - ahk: max(3115 - max(taxable - 29736, 0) * 0.06398, 0)
  - ak: max(5685 - max(profit - 45592, 0) * 0.0651, 0)
  - net: max(tax_before_credits - ahk - ak, 0)
expected:
  taxable: 42602.40
  income_tax: 4546.01
  premium: 10751.15
  tax_before_credits: 15297.16
  ahk: 2291.81
  ak: 5398.04
  net: 7607.31
```

**Example 2: box 3 for fiscal partners, with a lower actual return (edge case).** Whole-year fiscal partners, both resident throughout 2026; these are their only taxable box 3 assets and debts. On 1 January 2026 they hold bank balances EUR 80,000, shares EUR 150,000 and a consumer loan of EUR 10,000. Debts counted: 10,000 - 7,600 = EUR 2,400. Rendement with the provisional 2026 rates: 80,000 x 1.28% + 150,000 x 6.00% - 2,400 x 2.70% = EUR 9,959.20. Rendementsgrondslag 230,000 - 2,400 = EUR 227,600. Grondslag sparen en beleggen 227,600 - 118,714 = EUR 108,886. Joint deemed benefit 9,959.20 x 108,886 / 227,600 = EUR 4,764.58. Assume their complete statutory actual return for 2026 is EUR 3,000, with no remaining personal deductions. This is a stipulated case input, not a return reconstructed from the opening balances; use the actual-return referral above to establish it in a real case. That is lower, so EUR 3,000 is taxed (art. 5.25). Box 3 tax 36% = EUR 1,080; split 50/50, EUR 540 each. The bank and debt rates are provisional: recompute once the final 2026 figures are set.

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

Read the case record and existing correspondence before requesting missing inputs. Obtain age/AOW month, residence and insurance periods, partner dates and allocation, all income and deductions, direct and indirect company rights, opening assets/debts, actual-return evidence and every filing/assessment letter. Confirm any withheld tax and already-paid provisional assessments before settling the balance.

## Sources

Sources support the retained rules for the stated year and eligibility. Specialist referrals require a separate assessment.

| Source | URL | Read on |
|---|---|---|
| Wet inkomstenbelasting 2001, applicable 2026 edition; arts. 2.3, 2.10, 2.12-2.13, 2.17-2.18, 3.76, 3.79a, 5.2-5.5, 5.25, 6.2, 8.1, 8.8, 8.10-8.11, 9.2, 10.6ter | https://repository.officiele-overheidspublicaties.nl/bwb/BWBR0011353/2026-02-21_0/xml/BWBR0011353_2026-02-21_0.xml | 2026-11-22; additional passages and matching official XML 2026-11-26 |
| Wet financiering sociale verzekeringen, arts. 8, 10-12 | https://wetten.overheid.nl/BWBR0017745/2026-01-01 | 2026-11-22 |
| Algemene wet inzake rijksbelastingen, arts. 4, 9, 13, 15, 67d-67e | https://wetten.overheid.nl/BWBR0002320/ | 2026-11-22 |
| Invorderingswet 1990, art. 63b | https://repository.officiele-overheidspublicaties.nl/bwb/BWBR0004770/2026-10-01_0/xml/BWBR0004770_2026-10-01_0.xml | 2026-11-22; matching official XML 2026-11-26 |
| Fiscale informatie 2026, ch. 21: credit and contribution components; labour-income definition | https://www.belastingdienst.nl/wps/wcm/connect/fisin/fisin2026/heffingskortingen | 2026-11-22 |
| Box 3 preliminary calculation 2026 | https://www.belastingdienst.nl/wps/wcm/connect/nl/box-3/content/berekening-box-3-inkomen-2026 | 2026-11-26 |
| Provisional assessments | https://www.belastingdienst.nl/wps/wcm/connect/nl/voorlopige-aanslag/content/hoge-belastingaanslag-voorlopige-aanslag | 2026-11-22 |
| Filing invitation | https://www.belastingdienst.nl/wps/wcm/connect/nl/belastingaangifte/content/moet_ik_aangifte_doen | 2026-11-22 |
| Extension | https://www.belastingdienst.nl/wps/wcm/connect/nl/belastingaangifte/content/kan-ik-nog-uitstel-aanvragen-belastingaangifte | 2026-11-22 |
| Interest percentages | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/standaard_functies/prive/contact/rechten_en_plichten_bij_de_belastingdienst/belastingrente/overzicht_percentages_belastingrente | 2026-11-22 |
| Late returns | https://www.belastingdienst.nl/wps/wcm/connect/nl/belastingaangifte/content/wat-gebeurt-er-als-ik-geen-aangifte-doe-of-te-laat-of-onvolledig | 2026-11-22 |
| Penalty standards | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/standaard_functies/prive/contact/rechten_en_plichten_bij_de_belastingdienst/boete | 2026-11-22 |

Not yet confirmed: final 2026 box 3 bank and debt rates. Do not use the provisional example as a final-return calculation. Check this point with one of our partner accountants.
