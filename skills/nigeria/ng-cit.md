---
name: ng-cit
description: 'Compute ordinary Nigerian resident company income tax for 2026 under the National Assembly Nigeria Tax Act text: the dual small-company test, ordinary company rate, development levy, profit adjustments, losses, capital allowances, withholding credits and filing package. Keep 2025 historical fixtures separate. Refuse unsupported transition apportionment, specialist sectors and unresolved minimum-effective-tax currency/version issues.'
jurisdiction: NG
tax_year: 2026
last_updated: '2026-11-16'
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: corporate-tax
version: '1.1'
type: computation
category: international
---

# Nigeria company income tax v1.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Scope

Ordinary resident Nigerian companies for 2026; amounts in NGN. A Nigerian company's profits are within scope wherever earned, whether or not remitted (NTA section 6). Each company is assessed separately; a company partnership allocates each company's share separately (section 11). Individual income tax belongs to [ng-personal-income-tax](ng-personal-income-tax.md), employee withholding to [ng-payroll](ng-payroll.md), VAT to [nigeria-vat](nigeria-vat.md), disposal calculations to [ng-cgt](ng-cgt.md), and non-residents/treaty credits to [ng-non-resident-cross-border](ng-non-resident-cross-border.md). [NTA](https://nass.gov.ng/documents/download/11249).

**Which law copy?** The National Assembly download, listed on its current law index, is used throughout. The Presidential Fiscal Policy and Tax Reforms Committee's [release of the Assembly copies](https://www.fiscalreforms.ng/news/gazetted-tax-reform-acts-authorised-by-national-assembly) identifies the officially released set. The older [LIRS-hosted Gazette](https://lirs.gov.ng/assets/docs/Gazette%20-%20NIGERIA%20TAX%20ACT,%202025.pdf) differs: its small-company definition uses NGN50 million and a professional-services exclusion; its effective-tax provision uses a different currency/scope threshold and some section numbers differ. Do not combine those copies. The National Assembly definition uses NGN100 million and no professional-services exclusion. The separate NTAA VAT small-business definition does exclude professional services. This is a document reconciliation, not a claim that the discrepancy never existed.

The [government transition announcement](https://fmino.gov.ng/federal-government-issues-transition-guidelines-for-tax-acts-2025/) keeps pre-commencement liabilities under the earlier law and distinguishes the new administration of returns due after commencement. A filing date in 2026 does not by itself turn 2025 profits into a 2026 NTA computation. The complete operative transition instrument was not obtained from its issuer; a straddling period or disputed transition outcome is held rather than automatically divided by days.

## Ask the client first

Use the intake and accounts already supplied. Establish incorporation/Tax ID, residence, accounting start/end and any change or cessation; gross turnover and total fixed assets; audited or qualifying attested accounts, trial balance and prior return; asset cost, use dates, VAT/import-duty evidence and prior allowances; loss-by-trade schedule; WHT receipts and payments; foreign income/taxes; group structure and accounts; donations, R&D, financing, related parties and any incentive certificate. No accounts or no reliable profit evidence means no final computation. Missing prior schedules block the affected loss/allowance, not the creation of a clearly incomplete working paper.

## The method, step by step

### 1. Select the period and company test [NTA sections 56, 57, 59 and definitions](https://nass.gov.ng/documents/download/11249)

| Item | Amount and condition for the National Assembly NTA text | Source |
| --- | --- | --- |
| Small company | Gross annual turnover at most NGN100,000,000 AND total fixed assets at most NGN250,000,000; 0% on total profits. No professional-services exclusion in this definition. | [NTA section 56 and definition of small company](https://nass.gov.ng/documents/download/11249) |
| Any other company | 30% on total profits. The Act permits 25% only from a date determined by Presidential order; no automatic multi-year phase-down or medium-company band is given here. | [NTA section 56](https://nass.gov.ng/documents/download/11249) |
| Development levy | 4% of assessable profits; excludes small companies and non-resident companies, and is not charged on the assessable profits computed for hydrocarbon tax. It is not 2% and is not an additional levy on top of the repealed charges. | [NTA section 59](https://nass.gov.ng/documents/download/11249) |
| Minimum effective tax | 15% floor, where the section applies, on covered taxes divided by net income. The Assembly text prints an MNE group threshold of "£750 million or its equivalent" and a domestic aggregate-turnover threshold of NGN50,000,000,000 and above; it permits a higher domestic threshold by regulation. Scope affected by the currency/version discrepancy is held. | [NTA section 57](https://nass.gov.ng/documents/download/11249) |
| Related-party debt interest | Excess over 30% of EBITDA disallowed; carry-forward limited to the next 5 assessment years. Exception for a Nigerian subsidiary of a foreign company engaged in banking or insurance. | [NTA Third Schedule](https://nass.gov.ng/documents/download/11249) |
| Donation limit | Qualifying Nigerian recipients under the section, documentary evidence, total deduction no more than 10% of profit before tax. Non-cash value is the lower of market value and acquisition consideration. | [NTA section 163](https://nass.gov.ng/documents/download/11249) |
| R&D deduction limit | Actual qualifying expenditure for the period, capped at 5% of turnover; later sale/transfer proceeds are taxable. | [NTA section 164](https://nass.gov.ng/documents/download/11249) |

Covered taxes in section 57 are the listed company income, petroleum profit and hydrocarbon taxes, development levy and priority-sector tax credit. Net income is audited profit before tax excluding franked investment income and the printed "unrealistic gains or losses"; life-insurance policyholder income is separately excluded. The free-zone exception has customs-territory and MNE exceptions. Do not replace this statutory computation with an assumed OECD IIR, UTPR, safe harbour or GloBE return deadline. Implementation and the printed terminology need the applicable regulations; hold a final top-up where those affect the result.

### 2. Reconcile accounts to assessable profits [NTA sections 20 and 21](https://nass.gov.ng/documents/download/11249)

Start with accounting profit and a documented adjustment schedule. Expenses must be wholly and exclusively incurred to produce income. The section includes interest subject to the Third Schedule, business rent, employee remuneration/benefits, repairs, title costs, approved retirement contributions, proven stock loss, qualifying bad/doubtful debt, R&D, qualifying pre-commencement expenses and the other express items. Bad/doubtful debts are reduced for earlier deductions and later recoveries return to profit; a related-party bad debt fails the stated limb. Pre-commencement expense treatment is limited to the preceding six years and the statutory conditions. Foreign-currency expenses use the official CBN rate for the relevant date or period.

Add back capital/private expense, recoverable insurance sums, profit/income taxes, unapproved retirement contributions, book depreciation/impairment and unrealised exchange differences, non-qualifying reserves, non-arm's-length related-party charges, exempt-income expenses, costs already deducted against gains, fines/penalties, another person's tax and the specified securities-lending compensating payments. Check VAT due but not charged and import duty/levy unpaid: section 21(p) can deny the expense. Do not double deduct a chargeable-gain cost. Subtract exempt/final-taxed income only after establishing its provision; a bank receipt alone does not establish exemption.

Donations and R&D need the separate limits above. A donation is not confined to a copied legacy Fifth/Sixth Schedule list: section 163 states public funds, statutory bodies/institutions, qualifying religious/charitable/educational/scientific institutions in Nigeria, specified diplomatic bodies and public-emergency interventions. Keep receipts and recipient evidence. Related-party arrangements must be arm's length and reported in the prescribed manner (NTA section 191); this does not establish any unread TP documentation or CbCR threshold/deadline.

### 3. Losses and capital allowances [NTA section 27 and First Schedule Part I](https://nass.gov.ng/documents/download/11249)

Total profits include assessable profits from all sources and chargeable gains, less allowable trade losses and capital allowances. Ordinary losses stay with the trade that generated them, use the earliest succeeding year as far as possible and continue until recouped, without double deduction. Digital/virtual-asset losses are ring-fenced to that business. No generic expiry of pre-2019 losses or ownership-change percentage is assumed.

Capital allowances require qualifying expenditure, ownership and use for the trade at the period end; verify VAT/import-duty requirements. Priority-sector expenditure requires the acceptance certificate in section 27. Apportion assets partly used for taxable income, subject to the statutory exception where non-taxable income is below 10% of total income and the separate priority-activity restriction. Apply losses before the allowance against the remaining profit. Unused allowance carries forward under paragraph 22; do not import the old general two-thirds ceiling into this Part.

| Qualifying class | Annual rate; use the actual statutory asset class | Source |
| --- | --- | --- |
| Buildings, agricultural expenditure, masts, intangible assets, heavy transportation | 10% | [NTA First Schedule Part I Table I](https://nass.gov.ng/documents/download/11249) |
| Plant, agricultural equipment, furniture/fittings, mining, other equipment | 20% | same |
| Motor vehicles, software, other capital expenditure | 25% | same |

The allowance is on qualifying expenditure, not the old initial-plus-reducing-balance model. Short basis periods are prorated. The 1% statistical amount is notional and does not reduce the allowance. Residue is qualifying expenditure less allowances made. Roll forward opening residue, additions, allowances and disposals; investigate balancing/disposal treatment before claiming a benefit. For pre-commencement assets, paragraph 23 adjusts the remaining allowance periods by those already allowed, clears residue when the older years exhaust the new period, and denies a new allowance for the residual book amount where the allowance was already fully granted. Do not apply a fresh full write-off to every old asset.

### 4. Compute tax, then distinguish credits [NTA sections 56 and 59; NTAA sections 51 and 55](https://nass.gov.ng/documents/download/11250)

Compute income tax on total profits and levy on assessable profits separately. Add an applicable, resolved effective-tax top-up; never silently treat it as zero because the taxpayer is outside an assumed euro group threshold. Credit documented non-final WHT and actual income-tax payments against the correct liability. Outgoing WHT paid as an agent is not the company's own credit. A Nigerian dividend after prescribed deduction is franked income, not a second ordinary-tax charge; redistribution set-off follows NTAA section 51(4). Final tax is not also an ordinary credit. Refunds under section 55 follow audit, a written claim within six years after the assessment year, and payment within 90 days of the authority's decision, with a set-off option. Do not promise a refund within 90 days of submitting a claim.

### 5. Prepare the statutory return and payment [NTAA sections 11, 31 and 49](https://nass.gov.ng/documents/download/11250)

Prepare the prescribed self-assessment, accounts, source-by-source tax computation, capital-allowance schedule, loss schedule, payment evidence, applicable effective-tax computation and principal-officer attestation. A small company may use a taxpayer-attested statement of accounts instead of audited statements under section 11; do not assert every small company needs an ICAN-only audit. Keep WHT receipts, donations, related-party information and evidence for each position. Retain records for at least six years after the relevant assessment year. The TCC process is separate from filing; no blanket assertion that four social certificates always block every TCC is made here.

| Obligation | Deadline and condition | Source |
| --- | --- | --- |
| Established company return | Within 6 months of accounting year end for a company in business more than 18 months | [NTAA section 11](https://nass.gov.ng/documents/download/11250) |
| Newly incorporated company | Earlier of 18 months after incorporation and 6 months after the first accounting period end | same |
| Cessation return | Within 6 months after permanent cessation, including outstanding returns | same |
| Self-assessment payment | By filing due date; lump sum or instalments, with final instalment no later than that date | [NTAA section 49](https://nass.gov.ng/documents/download/11250) |
| Assessment without objection/appeal | Within 30 days of service, subject to statutory extension; undisputed amounts remain payable during a dispute | same |

Use the NRS's current prescribed form and authenticated service. The old TaxPro Max, Remita and TIN references remain historical workflow topics, not proof of today's menus, number lengths or a universal payment provider. Capture the actual assessment, official payment reference, payment receipt and separate filing acknowledgement. Do not invent a provisional-return requirement for an ordinary company from petroleum instalment rules. [ng-return-assembly](ng-return-assembly.md) owns final packaging.

### 6. Record non-compliance separately [NTAA sections 65, 66, 101, 105 and 107](https://nass.gov.ng/documents/download/11250)

Late filing/inaccurate return under section 101 attracts NGN100,000 in the first month and NGN50,000 for each continuing month. General late payment under section 65 adds 10% plus interest at MPR plus the Minister's spread for naira, or SOFR plus the spread for foreign currency; do not invent a 5-point spread. Section 66 allows remission for good cause. Failure to deduct is the separate 40% administrative penalty; failure to remit deducted tax is governed by section 107, not an extra company-income-tax credit. Do not use the old NGN25,000/5,000 filing table or generic tax-evasion fine for a 2026 breach. Assessment limitation, objections, false returns and criminal proceedings need their actual provisions and facts, not a guessed multiplier.

## Boundary and exception table

| Original boundary | Treatment |
| --- | --- |
| R-NG-CIT-1 petroleum; R-NG-CIT-2 banks, insurers, pension funds | Refer specialist computation. Ordinary-company allowances and effective-tax assumptions do not settle their sector rules. |
| R-NG-CIT-3 free zones; R-NG-CIT-4 pioneer/industrial relief | Inspect the certificate, period and transition; no automatic exemption or new application entitlement. Existing incentives and new economic-development certificates differ. |
| R-NG-CIT-5 TP dispute/APA; R-NG-CIT-8 audit, assessment, NORA or TAT dispute | Preserve notices and deadlines; accredited representation and the actual law are needed. |
| R-NG-CIT-6 non-resident/SEP | Route to ng-non-resident-cross-border; do not use the resident-company model. |
| R-NG-CIT-7 group/consolidated request | Prepare separate legal-entity computations; specialist group/foreign-parent issues remain. |
| R-NG-CIT-9 PIT or VAT request | Load the owning sibling, including where employee benefits or VAT affect company deductions. |
| Company band/assets, incentive or effective-tax scope unknown | Hold the affected final result. Do not assume the highest band or deny relief merely to avoid investigating. |
| Export manufacturing, REICs, investment allowance, donations, foreign-tax relief | Preserve each topic; apply only a sourced provision and its conditions. No blanket export-company exemption or legacy extra investment allowance is assumed. Foreign credits route to the cross-border skill. |

## Worked cases

The original named companies and numerical fixtures are retained. The first three were explicitly for calendar 2025. Their historical legal rates, bases and additional levies require the earlier Acts; the following are retained conditional arithmetic, not verified 2025 liabilities. They are not rolled into 2026 guidance.

| Historical 2025 fixture retained | Original inputs and conditional arithmetic | Correction/hold |
| --- | --- | --- |
| ABC Ltd | Turnover NGN18,000,000; accounting profit NGN4,500,000; the old case applied nil CIT/TET and 0.005% police levy = NGN225 | Whether that levy was legally due and its operative lifetime need historical primary confirmation. Do not call a statutory amount "effectively zero". |
| XYZ Ltd | Turnover NGN65,000,000; adjusted profit NGN12,000,000; allowance NGN2,000,000; no loss; WHT NGN150,000. At assumed legacy 20%, 3% education levy and NGN60 police levy: NGN2,210,060 | Historical scope and levy base held; no proof that adjusted profit equals the police levy base. |
| Big Co Plc | Turnover NGN5,400,000,000; adjusted profit NGN820,000,000; allowances NGN180,000,000; loss NGN40,000,000; WHT NGN26,000,000; not in old NITDA/NASENI sectors. Assumed legacy total profit NGN600,000,000, CIT NGN180,000,000, education levy NGN24,600,000 and police levy NGN41,000, net NGN178,641,000 | Historical legal computation held, including levy base and applicable exemptions. |

Current example A: carry the original **Big Co Plc 2026** inputs above into the NTA calculation, with the allowances and losses independently supported. It is outside section 57 under the explicit assumption that it is neither an in-scope MNE constituent nor above the domestic threshold. Ordinary tax is NGN180 million; levy on NGN820 million is NGN32.8 million; after NGN26 million of ordinary-tax WHT the combined cash schedule is NGN186.8 million. The old NGN170.4 million result used an incorrect 2% levy and an invented transitional credit.

```oa-check
name: Big Co Plc full-year 2026 corrected company tax and levy
inputs:
  assessable_profit: 820000000
  losses: 40000000
  allowances: 180000000
  wht_credit: 26000000
steps:
  - total_profit: assessable_profit - losses - allowances
  - cit: total_profit * 0.30
  - levy: assessable_profit * 0.04
  - cit_cash: cit - wht_credit
  - combined_cash: cit_cash + levy
expected:
  total_profit: 600000000
  cit: 180000000
  levy: 32800000
  cit_cash: 154000000
  combined_cash: 186800000
```

Current example B: the decision at the small-company asset boundary. A resident company has annual turnover NGN65 million, assessable profit NGN12 million and supported allowances NGN2 million. At NGN250 million of fixed assets it satisfies both tests and ordinary company tax/levy are nil. At NGN250,000,001 it fails the asset limb, so CIT is NGN3 million and levy NGN480,000. No other change in activity, period, incentive or section 57 scope is assumed.

```oa-check
name: Nigeria company fixed-asset boundary decision
inputs:
  assessable_profit: 12000000
  allowances: 2000000
steps:
  - total_profit: assessable_profit - allowances
  - qualifying_cit: total_profit * 0
  - qualifying_levy: assessable_profit * 0
  - nonqualifying_cit: total_profit * 0.30
  - nonqualifying_levy: assessable_profit * 0.04
  - difference: nonqualifying_cit + nonqualifying_levy - qualifying_cit - qualifying_levy
expected:
  total_profit: 10000000
  qualifying_cit: 0
  nonqualifying_cit: 3000000
  nonqualifying_levy: 480000
  difference: 3480000
```

## When to refuse or refer

Apply every boundary above. Unknown facts do not become an automatic 30% assessment, an expired loss, a denied exemption or an assumed MNE scope. Withhold only the unsupported final position and name the documents/provision needed. This skill prepares a working paper for a Nigerian professional; it does not submit or represent the taxpayer in a dispute.

## Sources

| Source and actual read scope | URL | Read on |
| --- | --- | --- |
| National Assembly NTA: sections 6 to 11, 20 to 28, 56 to 59, 162 to 164, 191, 195 to 198 and definitions; First Schedule Part I and Third Schedule | https://nass.gov.ng/documents/download/11249 | 2026-11-16 |
| National Assembly NTAA: sections 11, 31, 49, 51, 55, 65, 66, 101, 105 and 107 | https://nass.gov.ng/documents/download/11250 | 2026-11-16 |
| Presidential Committee announcement identifying Assembly-released gazetted Acts; announcement only | https://www.fiscalreforms.ng/news/gazetted-tax-reform-acts-authorised-by-national-assembly | 2026-11-16 |
| Older LIRS Gazette: comparison of small-company definition, sections 56 to 59 and numbering only | https://lirs.gov.ng/assets/docs/Gazette%20-%20NIGERIA%20TAX%20ACT,%202025.pdf | 2026-11-16 |
| Federal government transition announcement, complete article; not the full operative guideline | https://fmino.gov.ng/federal-government-issues-transition-guidelines-for-tax-acts-2025/ | 2026-11-16 |

Not yet confirmed: a superseding instrument resolving the official-copy differences and the printed pound/euro effective-tax test; any applicable Presidential rate-reduction order or detailed effective-tax regulation; the complete issuer-hosted transition instrument for straddling periods; live NRS portal menus and identifiers; current TP/CbCR forms, thresholds and deadlines; specific free-zone, pioneer, export, REIC and incentive entitlement. Historical source checks remain required for the retained CITA topics: small/medium/large limits of NGN25m/100m and 0%/20%/30%; 0.5% minimum tax and small/new-business/agricultural exceptions; TET 3%, NITDA 1%, NASENI 0.25%, police 0.005%; the old capital-allowance table (buildings 15%/10%, furniture 25%/20%, vehicles/plant/computers/software 50%/25%, agricultural plant and R&D 95%/nil), its two-thirds cap and balancing claims; old loss-expiry assertions; a 10% additional investment allowance; a 3-year plus possible 2-year pioneer holiday; TCC "new business" treatment and assessment limitation; historical penalty/fraud multipliers; and the original treaty-country list (UK, France, Belgium, Netherlands, Canada, Pakistan, Romania, China, South Africa). These are preserved topics, not usable 2026 instructions. No legacy levy is added to the NTA levy. No approximate phase-down, daily-apportionment default, generic OECD deadline or speculative deduction is supplied.
