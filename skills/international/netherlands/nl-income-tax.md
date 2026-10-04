---
name: nl-income-tax
description: Use this skill whenever asked about Netherlands income tax for self-employed individuals (zzp'ers, eenmanszaak). Trigger on phrases like "aangifte inkomstenbelasting", "income tax return Netherlands", "zelfstandigenaftrek", "startersaftrek", "MKB-winstvrijstelling", "urencriterium", "Box 1 income", "Box 3 wealth tax", "heffingskortingen", "arbeidskorting", "KIA investment deduction", "self-employed tax Netherlands", "winst uit onderneming", or any question about filing or computing income tax for a Dutch zzp'er or eenmanszaak. Also trigger when preparing or reviewing an aangifte IB, computing deductible expenses, or advising on voorlopige aanslagen. This skill covers Box 1 progressive rates, entrepreneur deductions, capital allowances, tax credits, Box 3 savings/investment income, filing deadlines, and penalties. ALWAYS read this skill before touching any Dutch income tax work.
version: 2.0
jurisdiction: NL
tax_year: 2026
last_updated: 2026-09-28
authored_by: OpenAccountants team
review_status: pending_review
trust_label: Written by the OpenAccountants team
depends_on:
  - income-tax-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Netherlands income tax for a sole proprietor — 2025 returns and 2026 estimates

## Scope and who this is for

This method prepares a traceable income-tax computation for a full-year Netherlands-resident individual with domestic sole-proprietor business income, possibly alongside wages or other personal income. Figures are for tax year 2025 or tax year 2026 as labelled. The ordinary rate/credit calculations below assume the person remains below AOW age throughout the year and is fully insured for national insurance. Age transitions and insurance exceptions require the correct separate tables. Business profit is one component of Box 1, not the whole personal return. [Tax structure](https://www.belastingdienst.nl/wps/wcm/connect/fisin/fisin2025/belastingberekening) [2026 structure](https://www.belastingdienst.nl/wps/wcm/connect/fisin/fisin2026/belastingberekening)

The method screens all boxes and preserves their inputs, but does not determine complex substantial-interest, international, migration, estate, partnership, pension or actual-return property cases. An estimate with a missing material box is incomplete. Use `nl-freelance-intake` for facts, `nl-zzp-deductions` for business relief, `nl-deductions` for personal/home deductions and `nl-return-assembly` for the final field-by-field handoff. Check the actual versions and official annual sources before relying on a dependent Guide.

## Ask the client first

- Which income year and requested output: estimate, completed computation, correction or filing handoff? Obtain the actual invitation, extension, assessments and payment notices.
- Full-year residence, date of birth, month AOW age is reached, national-insurance coverage and any foreign work/income/assets?
- Which activities qualify as enterprise, employment or income from other work? Obtain contracts and actual working facts, not only registration.
- Complete accounts, invoices, bank/processor reconciliations, opening/closing balances, asset register, private-use adjustments and business deduction history?
- Employment/pension statements, withholding, taxable benefits, other income, own-home/loan records and allowable personal deductions?
- Fiscal-partner facts and dates, children/household records, both partners' work income and relevant joint deductions/assets?
- Assets and debts by category at the statutory reference date, exemptions, ownership changes, and evidence for actual Box 3 income and value changes?
- Prior loss/deduction decisions, provisional assessments, amounts already paid/refunded and unpaid balances? Keep assessment amounts distinct from cash settlement.

Missing information stays missing. A bank statement alone is not enough to classify every transaction, prove entrepreneur relief or complete the return. [Income sources](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/wanneer_bent_u_ondernemer_voor_de_inkomstenbelasting/) [Hours evidence](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/inkomstenbelasting_voor_ondernemers/voorwaarden_urencriterium) [Tax computation](https://www.belastingdienst.nl/wps/wcm/connect/fisin/fisin2025/belastingberekening)

## The method, step by step

1. Establish the year, residence, insurance and source-of-income branches.
2. Reconcile business accounts and compute business profit and relief separately.
3. Build the complete income and deduction ledger for each box.
4. Apply the correct annual rates, deduction-rate adjustment and credits.
5. Reconcile withholding and provisional assessments; calculate Zvw separately.
6. Produce a documented computation and hold unresolved dependent outputs.

### Step 1: Establish the branches

Income-tax entrepreneurship is a factual assessment of commercial activity, independence, risk and other factors. A VAT number, registration or hours threshold is not conclusive. Assess employment per engagement from all circumstances; there is no fixed customer-share safe harbour. Income from other work can be taxable without qualifying for entrepreneur relief. [Entrepreneur assessment](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/wanneer_bent_u_ondernemer_voor_de_inkomstenbelasting/) [Employment assessment](https://www.belastingdienst.nl/wps/wcm/connect/nl/arbeidsrelaties/content/wanneer-is-sprake-van-loondienst)

Use the actual year and age/insurance position. The AOW first-band rate and, for older birth cohorts, the band limit differ; reaching AOW age during the year requires the month's table. Do not use a permanently hardcoded birth-date cutoff or an approximate rate. Cross-border or partial insurance can also affect rates and the insurance components of credits. [Box 1 tables](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/prive/inkomstenbelasting/heffingskortingen_boxen_tarieven/boxen_en_tarieven/box_1/) [Credit components](https://www.belastingdienst.nl/wps/wcm/connect/fisin/fisin2026/heffingskortingen)

### Step 2: Reconcile business profit

Reconcile sales, receivables, purchases, creditors, stock, assets, loans, private withdrawals and capital introduced. Match processor settlements to gross transactions, refunds, VAT and actual fees; never invent a fee from a bank payout. Record transfers and security deposits according to their underlying legal/economic character. A merchant or bank narration proposes a category for investigation, not a tax conclusion. [Business costs](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/inkomstenbelasting_voor_ondernemers/zakelijke_kosten)

Remove recoverable VAT from income-tax cost/asset amounts. Include irrecoverable VAT only where the underlying cost is allowable, with capitalisation and private-use restrictions. Do not strip VAT blindly from KOR or exempt-activity costs. Income-tax payments are not business costs; identify each tax refund/payment by tax type and period before deciding its accounting treatment. [Business costs](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/inkomstenbelasting_voor_ondernemers/zakelijke_kosten) [KOR effects](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/btw/hoe_werkt_de_btw/kleineondernemersregeling/wat-betekent-meedoen-met-de-kleineondernemersregeling)

Use the validated `nl-zzp-deductions` method for hours, starter lookback, carryforward, partner relief, investment deduction and MKB. Record KIA and reserve/depreciation adjustments in fiscal profit before ondernemersaftrek. The MKB exemption is 12.7% in both years after entrepreneur deductions and also reduces losses. No new FOR additions are allowed from 2023. Retain both profit before ondernemersaftrek/MKB and taxable profit after them, because the labour credit uses the former business-profit basis. [MKB](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/inkomstenbelasting_voor_ondernemers/mkb_winstvrijstelling) [FOR](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/inkomstenbelasting_voor_ondernemers/fiscale_reserves/oudedagsreserve) [Labour income definition](https://www.belastingdienst.nl/wps/wcm/connect/fisin/fisin2026/heffingskortingen)

### Step 3: Build the boxes and personal deductions

Add wages, pensions, other-work income and other relevant Box 1 items to the taxable business result, applying their own rules. Include the own-home balance, income-provision deductions and any applicable loss relief. Personal deductions are used against Box 1, then Box 3, then Box 2, without reducing the respective income below nil; remaining eligible personal deductions need a carryforward ledger. Do not confuse this with business losses or unused zelfstandigenaftrek. [Calculation and deduction order](https://www.belastingdienst.nl/wps/wcm/connect/fisin/fisin2025/belastingberekening)

Collect Box 2 interests and receipts even where specialist analysis is required. Do not silently omit them because the taxpayer mainly works as a sole proprietor. For Box 3, distinguish the statutory deemed-return method from the actual-return comparison; keep complete asset/debt classification and source-year evidence. Future announced systems are not current return rules. [Tax structure](https://www.belastingdienst.nl/wps/wcm/connect/fisin/fisin2026/belastingberekening) [Box 3 guidance](https://www.belastingdienst.nl/wps/wcm/connect/nl/box-3/content/)

Fiscal partners may allocate specified common items and dividend withholding under the applicable conditions, but not wages, enterprise profit or wage withholding. Use each person's own labour income for the labour credit. Review the combined effect of permissible allocations on credits and deductions; do not describe tax credits as freely transferable. [Fiscal partnership](https://www.belastingdienst.nl/wps/wcm/connect/fisin/fisin2026/fiscaal_partnerschap)


### Step 3a: Compute the ordinary Box 3 branch

Use the actual asset categories and statutory values on 1 January of the income year. Separate bank balances from investments/other assets; apply asset exemptions before the ordinary computation. Reduce eligible debts by the annual debt threshold, never below nil. Compute deemed return by applying each category rate to the corresponding amount and subtracting the deemed return on deductible debts. Floor the aggregate deemed return at nil before applying the taxable-base ratio; it must not generate a negative Box 3 result. [Statutory floor, article 5.2(2)](https://wetten.overheid.nl/BWBR0011353) Then compute net assets after deductible debts, and the taxable savings/investment base after the tax-free allowance, never below nil. Where net assets are positive, multiply deemed return by the taxpayer's allocated taxable base divided by net assets. Use the official return's rounding and apply remaining allowable personal deductions before tax. If the taxable base is nil, do not divide by zero. [Annual method](https://www.belastingdienst.nl/wps/wcm/connect/fisin/fisin2025/belastingberekening) [2026 provisional method](https://www.belastingdienst.nl/wps/wcm/connect/nl/box-3/content/berekening-box-3-inkomen-2026)

| Parameter | 2025 | 2026 |
| --- | --- | --- |
| Bank return percentage | 1.37% | 1.28%, provisional |
| Investment/other-asset return percentage | 5.88% | 6.00%, fixed |
| Debt return percentage | 2.70% | 2.70%, provisional |
| Debt threshold, one person | €3,800 | €3,800 |
| Tax-free allowance, one person | €57,684 | €59,357 |
| Tax-free allowance, qualifying partners together | €115,368 | €118,714 |
| Tax rate | 36% | 36% |
| Source | [2025 rates](https://www.belastingdienst.nl/wps/wcm/connect/nl/box-3/content/), [asset rules](https://www.belastingdienst.nl/wps/wcm/connect/fisin/fisin2025/bezittingen_en_schulden_box_3_), [method](https://www.belastingdienst.nl/wps/wcm/connect/fisin/fisin2025/belastingberekening) | [2026 provisional assessment](https://www.belastingdienst.nl/wps/wcm/connect/nl/box-3/content/berekening-box-3-inkomen-2026) |

For whole-year qualifying fiscal partners, use joint assets/debts and the doubled debt threshold, then document the permitted allocation of the taxable base. Do not confuse that allocation with assigning every asset arbitrarily. The 2026 bank/debt percentages are provisional and will be fixed after year-end; the provisional assessment does not use actual return. [2026 status and partner method](https://www.belastingdienst.nl/wps/wcm/connect/nl/box-3/content/berekening-box-3-inkomen-2026)

From the 2025 return, actual-return information can be supplied within the return. Compare the complete annual actual return with the deemed result; the authority uses the more favourable calculation. Actual return includes received income and value changes, including unrealised changes, over the whole relevant asset portfolio. There is no tax-free allowance in that actual-return calculation; an overall negative result is set to nil and cannot be carried to another year. Do not deduct ordinary management or maintenance costs; debt interest and specific qualifying property-investment adjustments have separate treatment. Refer property own-use, valuation changes, foreign assets and complex transactions for the current actual-return rules rather than copying the deemed-return method. [Actual-return principles](https://www.belastingdienst.nl/wps/wcm/connect/fisin/fisin2025/belastingberekening) [Comparison and return route](https://www.belastingdienst.nl/wps/wcm/connect/nl/box-3/content/)

### Step 4: Apply rates and credits

For the ordinary full-year branch, apply each Box 1 rate only to the part of taxable income within that band. A high-income deduction-rate adjustment may add tax back; it is not valid to value every deduction at the top marginal rate. Retain the adjustment as a separate line and use `nl-deductions` with the correct annual sources. [2025 computation](https://www.belastingdienst.nl/wps/wcm/connect/fisin/fisin2025/belastingberekening) [2026 computation](https://www.belastingdienst.nl/wps/wcm/connect/fisin/fisin2026/belastingberekening)

Credits reduce tax and national-insurance liability, not business profit. The general credit uses verzamelinkomen; the labour credit uses arbeidsinkomen, including enterprise profit before ondernemersaftrek and MKB. Payroll may already reflect credits through lower withholding: calculate the annual entitlement once, then credit actual withholding once. Do not deduct the payroll credit as a second annual credit. Obtain the labour credit reported by the employer as well: the authority can preserve a higher employer-calculated credit under the dedicated annual table’s conditions and maximum. [2026 employer-credit exception](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/prive/inkomstenbelasting/heffingskortingen_boxen_tarieven/heffingskortingen/arbeidskorting/tabel-arbeidskorting-2026) Special low-income partner payout conditions exist, so “credits can never be paid out” is too broad. [2025 credits](https://www.belastingdienst.nl/wps/wcm/connect/fisin/fisin2025/heffingskortingen) [2026 credits](https://www.belastingdienst.nl/wps/wcm/connect/fisin/fisin2026/heffingskortingen)

The table below gives the general and labour-credit parameters for the ordinary age/insurance branch. Apply the year-specific piecewise table, bounded at nil where appropriate, and the return's rounding. Do not extrapolate one phase-out formula across all income levels. [2025 credit tables](https://www.belastingdienst.nl/wps/wcm/connect/fisin/fisin2025/heffingskortingen) [2026 credit tables](https://www.belastingdienst.nl/wps/wcm/connect/fisin/fisin2026/heffingskortingen)

### Step 5: Separate assessment and cash settlement

Reconcile annual tax after credits to eligible withholding and provisional assessment amounts using the authority's computation, then reconcile outstanding payments/refunds separately. A provisional assessment still unpaid is not proof of tax paid; a bank payment can relate to a different year or tax. Retain both assessment reconciliation and payment ledger. The eventual assessment can differ from the return's provisional calculation. [Assessment and offset structure](https://www.belastingdienst.nl/wps/wcm/connect/fisin/fisin2025/belastingberekening)

Zvw has a separate contribution-income base and assessment. Do not calculate it from total Box 1 after mortgage/personal deductions or deduct it from the income-tax bill. Obtain wage/pension Zvw statements because income already subject to an employer levy or withheld contribution affects the remaining maximum. Use the correct annual Zvw method and current notices. [2025 Zvw calculation](https://www.belastingdienst.nl/wps/wcm/connect/fisin/fisin2025/inkomensafhankelijke_bijdrage_zorgverzekeringswet)

### Step 6: Handoff and missing-data controls

Provide the tax year; residence/insurance assumptions; profit bridge; separate Box 1/2/3 ledgers; allowable deductions and carryforwards; annual rates and credit bases; withholding/provisional assessment reconciliation; separate Zvw result or hold; and every unresolved input with its consequence. Ask for the actual filing and payment dates from the notice. Do not treat an accountant extension or a particular provisional-assessment date as universal.

The output must say which computations are complete, which are estimates, and which cannot be completed. Unknown Box 3 assets, unresolved worker status or missing deduction history must not disappear from the result. No calculation or client's factual confirmation is itself filing authorisation.

## Figures by year

### Box 1 ordinary branch

| Portion of taxable Box 1 income | 2025 | 2026 |
| --- | --- | --- |
| First band | 35.82% through €38,441 | 35.75% through €38,883 |
| Second band | 37.48% above €38,441 through €76,817 | 37.56% above €38,883 through €78,426 |
| Third band | 49.50% above €76,817 | 49.50% above €78,426 |
| Source and age/insurance exceptions | [Official tables](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/prive/inkomstenbelasting/heffingskortingen_boxen_tarieven/boxen_en_tarieven/box_1/) | [Official tables](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/prive/inkomstenbelasting/heffingskortingen_boxen_tarieven/boxen_en_tarieven/box_1/) |

### General tax credit, below AOW age throughout

| Parameter | 2025 | 2026 |
| --- | --- | --- |
| Maximum and lower threshold | €3,068 through €28,406 | €3,115 through €29,736 |
| Reduction over lower threshold | 6.337% | 6.398% |
| Nil at upper threshold | €76,817 | €78,426 |
| Source | [2025](https://www.belastingdienst.nl/wps/wcm/connect/fisin/fisin2025/heffingskortingen) | [2026](https://www.belastingdienst.nl/wps/wcm/connect/fisin/fisin2026/heffingskortingen) |

Use verzamelinkomen, not merely wages or profit. The annual table's nil branch governs at the upper endpoint.

### Labour credit, below AOW age throughout

| Year | Work-income band | Credit formula |
| --- | --- | --- |
| 2025 | Through €12,169 | 8.053% of work income |
| 2025 | Above €12,169 through €26,288 | €980 + 30.030% of excess over €12,169 |
| 2025 | Above €26,288 through €43,071 | €5,220 + 2.258% of excess over €26,288 |
| 2025 | Above €43,071 through €129,078 | €5,599 − 6.510% of excess over €43,071 |
| 2025 | Above €129,078 | Nil |
| 2026 | Through €11,965 | 8.324% of work income |
| 2026 | Above €11,965 through €25,845 | €996 + 31.009% of excess over €11,965 |
| 2026 | Above €25,845 through €45,592 | €5,300 + 1.950% of excess over €25,845 |
| 2026 | Above €45,592 through €132,920 | €5,685 − 6.510% of excess over €45,592 |
| 2026 | Above €132,920 | Nil |
| Sources | [2025](https://www.belastingdienst.nl/wps/wcm/connect/fisin/fisin2025/heffingskortingen) | [2026](https://www.belastingdienst.nl/wps/wcm/connect/fisin/fisin2026/heffingskortingen) |

At published band boundaries use the return's table and rounding; do not manufacture differences by excessive precision in rounded table constants.

## Boundaries and exceptions

| Situation | Action |
| --- | --- |
| AOW age reached during year | Select actual month-specific rate and credit treatment; ordinary table is not applicable |
| Business hours below threshold | Do not reclassify the income automatically; assess each relief separately |
| Irrecoverable VAT | May be allowable cost/asset basis; do not strip automatically |
| Work income differs from taxable business profit | Use the correct separate credit basis |
| General-credit income at upper endpoint | Nil branch, not a negative credit |
| Child/partner conditions potentially qualify for IACK | Assess actual child residence/co-parenting, age and work-income conditions; ordinary hours test is not a universal requirement |
| Missing Box 3 information | Hold complete-return result; do not assume no assets |
| 2026 provisional Box 3 percentages | Identify provisional rates and update before final annual use |
| Tax payment labelled Belastingdienst | Match assessment, year, tax and actual cash settlement |

The income-dependent combination credit has separate child, household, partner and income conditions and is not automatically available merely from having a child. Use the annual chapter for co-parenting and equal-income tie rules. Other credits, including disability, elderly and green-investment credits, also require their specific facts. [2025 credits](https://www.belastingdienst.nl/wps/wcm/connect/fisin/fisin2025/heffingskortingen) [2026 credits](https://www.belastingdienst.nl/wps/wcm/connect/fisin/fisin2026/heffingskortingen) [2026 provisional Box 3](https://www.belastingdienst.nl/wps/wcm/connect/nl/box-3/content/berekening-box-3-inkomen-2026)

## Worked cases

**Ordinary 2026 illustration:** assume a below-AOW fully insured sole proprietor, no wages or employer-credit exception, no partner or other boxes, no other deductions/credits/withholding/provisional assessments, profit before entrepreneur relief €50,000 and a verified taxable business result of €42,602.40 from the deductions method. Box 1 tax before credits is €15,297.67914. General credit uses €42,602.40 verzamelinkomen and is €2,291.807728; labour credit uses €50,000 work income and is €5,398.03920. Their difference gives €7,607.832212 before return rounding (illustratively €7,607.83 to cents). This is an income-tax/national-insurance illustration, excludes separate Zvw, and does not override statutory or software rounding. [Rates](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/prive/inkomstenbelasting/heffingskortingen_boxen_tarieven/boxen_en_tarieven/box_1/) [Credit formulas](https://www.belastingdienst.nl/wps/wcm/connect/fisin/fisin2026/heffingskortingen)

These are decision and calculation checks, not complete client tax bills.

- **Band boundary:** a below-AOW, fully insured person has 2025 taxable Box 1 income exactly €38,441. The second band has no amount. Additional income goes into the second band; do not apply its rate to the whole amount. [Rates](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/prive/inkomstenbelasting/heffingskortingen_boxen_tarieven/boxen_en_tarieven/box_1/)
- **Credit bases:** a sole proprietor has reconciled profit before entrepreneur relief and a lower taxable result after relief. Use the pre-relief enterprise profit in labour income, alongside any other qualifying work income; use the full verzamelinkomen for the general credit. [Credit bases](https://www.belastingdienst.nl/wps/wcm/connect/fisin/fisin2026/heffingskortingen)
- **Year distinction:** preparation in 2026 for tax year 2025 retains the 2025 thresholds and credit formulas. The filing date does not select the annual table. [2025](https://www.belastingdienst.nl/wps/wcm/connect/fisin/fisin2025/heffingskortingen) [2026](https://www.belastingdienst.nl/wps/wcm/connect/fisin/fisin2026/heffingskortingen)
- **Mixed VAT recovery:** an otherwise allowable business purchase supports an exempt activity with no input recovery. Keep irrecoverable VAT in the allowable cost/asset basis, subject to ordinary restrictions. Do not strip it merely because this is an income-tax computation. [Costs](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/inkomstenbelasting_voor_ondernemers/zakelijke_kosten)
- **Unknown assets:** wages and business accounts are complete but the client has not supplied private investment records. Finish the independent profit bridge and hold the complete personal return; a missing Box 3 ledger is not a zero. [Box structure](https://www.belastingdienst.nl/wps/wcm/connect/fisin/fisin2025/belastingberekening)
- **Loss:** a qualifying enterprise loss after ondernemersaftrek receives MKB treatment that reduces the loss. Do not turn MKB off or increase the loss by its percentage. Carryforward losses need separate assessed records. [MKB](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/inkomstenbelasting_voor_ondernemers/mkb_winstvrijstelling)

## When to refuse or refer

- Refer residence/insurance transitions, foreign income/assets, treaties, companies/substantial interests, partnership allocations, death, cessation, complex property/actual-return cases and disputed worker status.
- Hold dependent figures for missing source records, uncertain VAT recovery, unexplained opening balances or carryforwards. Continue independent reconciliation without describing the full tax liability as settled.
- Obtain specialist or authority clarification if official sources conflict materially. In broad annual guidance, worked examples can lag updated rate tables; use dedicated year-specific tables and record the resolution.

## Completion checklist

- [ ] Income year, residence, AOW and insurance branch recorded.
- [ ] Business source and worker status assessed from facts.
- [ ] Accounts reconciled; tax payments, private flows and assets separated from costs.
- [ ] VAT recovery, annual business relief and MKB loss treatment correct.
- [ ] All boxes and personal deductions included or explicitly held.
- [ ] General and labour credits use different correct bases; no duplicate payroll credit.
- [ ] Annual rates, adjustments, rounding and special credit conditions checked.
- [ ] Withholding/assessment reconciliation separated from cash settlement and Zvw.
- [ ] Actual notices control filing/payment actions; unresolved items remain visible.
- [ ] Final handoff makes no unsupported claim of filing readiness or submission.

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
