---
name: sa-corporate-tax
description: "Saudi Arabia corporate income tax computation for 2026: foreign ownership in resident capital companies, non-Saudi resident business and Saudi permanent establishments. Determines taxable income, allowable expenses, financing-cost limits, losses, ownership allocation, instalments and filing workpapers. Includes natural-gas and oil rate boundaries, related-party documentation and preserved historical examples. Read before Saudi CIT calculations; use the separate Zakat and withholding skills for those liabilities. Special-sector computations, treaty opinions, incentives and disputes require their own source review."
jurisdiction: SA
tax_year: 2026
last_updated: "2026-11-16"
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: "tax"
category: "international"
tax_year_notes: "Current law read 16 November 2026; historical 2025 examples are labelled 2025-2026 filing cycle."
version: "1.1"
type: "computation"
---

# Saudi Arabia corporate income tax: 2026

> **Produced by OpenAccountants (openaccountants.com)**
>
> Computational working papers for professional review. This skill does not replace a Saudi tax opinion, an approved return or a concession-specific calculation.

## Scope

Compute ordinary Saudi corporate income tax (CIT) for resident capital companies' taxable ownership, non-Saudi resident natural persons carrying on business, and non-residents' Saudi permanent establishments (PEs). Read this skill before doing that job. The controlling provisions are Income Tax Law (ITL) arts. 2-7; a Saudi commercial registration alone does not establish which ownership share is taxable. [ITL](https://zatca.gov.sa/ar/HelpCenter/guidelines/Documents/%D9%86%D8%B8%D8%A7%D9%85%20%D8%B6%D8%B1%D9%8A%D8%A8%D8%A9%20%D8%A7%D9%84%D8%AF%D8%AE%D9%84.pdf).

**Quick reference:** establish the taxpayer, ownership, activity, fiscal period and tax-adjusted profit first. Use the rate table below. Keep CIT taxable income distinct from the Zakat base. There is no employment-salary tax computation in this skill. This is the **2026** method; the original companies and periods in the worked cases remain historical **2025-2026 filing-cycle** illustrations.

For related jobs load [Zakat](sa-zakat.md), [withholding tax](sa-withholding-tax.md), [RETT](sa-rett.md), [VAT](saudi-arabia-vat.md), [e-invoicing](saudi-einvoice.md), [intake](sa-freelance-intake.md) and [return assembly](sa-return-assembly.md). Those files own their respective rates and filing details; CIT payment is not a substitute for another liability.

## Ask the client first

1. Legal form, incorporation, actual management location, business activity and any natural-gas, oil, banking, insurance, fund, zone or RHQ status.
2. Direct and indirect owners, nationalities, relevant GCC treatment, beneficial ownership and dated ownership changes; distinguish listed-share trading from founders' holdings.
3. Fiscal-year start/end, calendar, cessation or restructuring dates; prior returns, assessments and approved loss balances.
4. Financial statements, trial balance, revenue and expense detail, depreciation pools, bad debts, provisions, financing income and costs, donations and related-party contracts.
5. For a PE: sites, agents, staff, contract negotiation/conclusion, activities, head-office charges and the treaty, if any. For a treaty claim obtain residence and entitlement evidence.
6. Previous-year CIT and withholding amounts, current instalments, credit certificates, unpaid taxes and any audit, dispute or penalty-relief application.

Missing minimum inputs mean **hold the computation**. Do not deem an unidentified owner foreign, choose an ordinary sector rate for an unidentified activity, invent a treaty outcome or estimate a missing cost allocation as if it were law.

## The method, step by step

### 1. Identify the taxable person and ownership

Apply ITL art. 2 to the taxpayer and art. 6 to its base. Resident capital companies are taxable on the relevant directly or indirectly non-Saudi-owned shares; shares of persons engaged in oil/hydrocarbon production have a separate statutory rule. Saudi/GCC treatment is conditional, not a passport-only exemption. Check the listed-share exceptions and oil-producer ownership before using an ordinary Saudi/GCC versus foreign split. Zakat Regulations arts. 1, 3 and 6 separately define the Zakat population, including relevant non-Saudi holdings in listed companies. [ITL arts. 2, 6](https://zatca.gov.sa/ar/HelpCenter/guidelines/Documents/%D9%86%D8%B8%D8%A7%D9%85%20%D8%B6%D8%B1%D9%8A%D8%A8%D8%A9%20%D8%A7%D9%84%D8%AF%D8%AE%D9%84.pdf); [Zakat Regulations arts. 1, 3, 6](https://zatca.gov.sa/en/RulesRegulations/Documents/ZAKAT%20COLLECTION.pdf).

For a mixed ordinary company, prepare a documented CIT ownership allocation and a separate Zakat workpaper. Do not apply the Zakat rate to accounting profit or the CIT rate to the Zakat base. Ownership changes require a dated reconciliation and consideration of the applicable income and loss rules; do not copy the Zakat year-end ownership rule into CIT without checking its legal basis. [ITL arts. 6, 21, 43](https://zatca.gov.sa/ar/HelpCenter/guidelines/Documents/%D9%86%D8%B8%D8%A7%D9%85%20%D8%B6%D8%B1%D9%8A%D8%A8%D8%A9%20%D8%A7%D9%84%D8%AF%D8%AE%D9%84.pdf).

Test residence under ITL art. 3 and PE under art. 4. A PE includes a fixed place through which business is wholly or partly carried on, relevant agents, construction/assembly and supervisory sites, resource-survey installations, a natural person's fixed business base and a licensed branch. Read the storage, display, delivery, processing, purchasing, information-gathering, preparatory/auxiliary and contract-preparation exclusions together with the actual activities. An applicable treaty may change the result: no universal construction or service-day threshold is supplied here. [ITL arts. 3-5](https://zatca.gov.sa/ar/HelpCenter/guidelines/Documents/%D9%86%D8%B8%D8%A7%D9%85%20%D8%B6%D8%B1%D9%8A%D8%A8%D8%A9%20%D8%A7%D9%84%D8%AF%D8%AE%D9%84.pdf); [WHT guideline pp. 11-17](https://zatca.gov.sa/en/HelpCenter/guidelines/Documents/General-Guideline-for-Withholding-Tax-In-accordance-with-the-provisions-of-the-Income-Tax-Law-and-its-Implementing-Regulations.pdf).

### 2. Select the statutory rate, after classification

| Item and conditions | Rate or boundary for 2026 | Official source |
|---|---|---|
| Ordinary taxable base of resident capital company; non-Saudi resident business individual; non-resident's Saudi PE | 20% | ITL art. 7(a), [law](https://zatca.gov.sa/ar/HelpCenter/guidelines/Documents/%D9%86%D8%B8%D8%A7%D9%85%20%D8%B6%D8%B1%D9%8A%D8%A8%D8%A9%20%D8%A7%D9%84%D8%AF%D8%AE%D9%84.pdf) |
| Natural-gas investment taxable base, separately determined | 20%; the old 30% headline is obsolete | ITL art. 7(b), amended effective 2018, [law](https://zatca.gov.sa/ar/HelpCenter/guidelines/Documents/%D9%86%D8%B8%D8%A7%D9%85%20%D8%B6%D8%B1%D9%8A%D8%A8%D8%A9%20%D8%A7%D9%84%D8%AF%D8%AE%D9%84.pdf) |
| Oil/hydrocarbon production: cumulative Saudi capital investment **over SAR 375 billion** | 50% | ITL art. 7(c)(1), capital boundary in words on the page, [law](https://zatca.gov.sa/ar/HelpCenter/guidelines/Documents/%D9%86%D8%B8%D8%A7%D9%85%20%D8%B6%D8%B1%D9%8A%D8%A8%D8%A9%20%D8%A7%D9%84%D8%AF%D8%AE%D9%84.pdf) |
| Same activity: **over SAR 300 billion and up to SAR 375 billion** | 65% | ITL art. 7(c)(2), boundaries in words on the page, [law](https://zatca.gov.sa/ar/HelpCenter/guidelines/Documents/%D9%86%D8%B8%D8%A7%D9%85%20%D8%B6%D8%B1%D9%8A%D8%A8%D8%A9%20%D8%A7%D9%84%D8%AF%D8%AE%D9%84.pdf) |
| Same activity: **over SAR 225 billion and up to SAR 300 billion** | 75% | ITL art. 7(c)(3), boundaries in words on the page, [law](https://zatca.gov.sa/ar/HelpCenter/guidelines/Documents/%D9%86%D8%B8%D8%A7%D9%85%20%D8%B6%D8%B1%D9%8A%D8%A8%D8%A9%20%D8%A7%D9%84%D8%AF%D8%AE%D9%84.pdf) |
| Same activity: **not over SAR 225 billion** | 85% | ITL art. 7(c)(4), boundary in words on the page, [law](https://zatca.gov.sa/ar/HelpCenter/guidelines/Documents/%D9%86%D8%B8%D8%A7%D9%85%20%D8%B6%D8%B1%D9%8A%D8%A8%D8%A9%20%D8%A7%D9%84%D8%AF%D8%AE%D9%84.pdf) |
| Eligible carried-forward operating loss | Annual deduction limited to 25% of annual profit under the regulation; indefinite carry-forward subject to eligibility and ownership rules | ITL art. 21; IR art. 11, [regulation](https://zatca.gov.sa/en/RulesRegulations/Taxes/Documents/Regulations_of_Income_Tax.pdf) |

The oil bands apply to the whole relevant taxable base, not marginal slices. Statutory capital investment includes the cumulative fixed and intangible amounts defined in art. 7 before depreciation/amortisation, not share capital or the accounting net-asset balance. The old skill reversed the largest-investment band. Gas and oil computations and the historical downstream transitional rule require specialist review; do not extend the expired transitional period to 2026. [ITL arts. 6-7 and amendment footnotes](https://zatca.gov.sa/ar/HelpCenter/guidelines/Documents/%D9%86%D8%B8%D8%A7%D9%85%20%D8%B6%D8%B1%D9%8A%D8%A8%D8%A9%20%D8%A7%D9%84%D8%AF%D8%AE%D9%84.pdf).

### 3. Reconcile book profit to taxable income

Start with the entity's financial statements and tax-period trial balance. Establish source and attribution under arts. 5-8; a resident company's branch operations and the specific source rules require analysis, rather than a blanket domestic-sales-only computation. Compute each taxpayer independently even when accounting statements are consolidated. [ITL arts. 5-8](https://zatca.gov.sa/ar/HelpCenter/guidelines/Documents/%D9%86%D8%B8%D8%A7%D9%85%20%D8%B6%D8%B1%D9%8A%D8%A8%D8%A9%20%D8%A7%D9%84%D8%AF%D8%AE%D9%84.pdf); [IR arts. 1, 5](https://zatca.gov.sa/en/RulesRegulations/Taxes/Documents/Regulations_of_Income_Tax.pdf).

Prepare an adjustment schedule showing the original ledger account, amount, reason, controlling article and supporting document for each item:

- Deduct actual ordinary and necessary expenditure incurred to earn taxable income in the period, paid or accrued, subject to the exclusions. Capital expenditure is not an immediate ordinary deduction. [ITL art. 12; IR art. 9(1)](https://zatca.gov.sa/en/RulesRegulations/Taxes/Documents/Regulations_of_Income_Tax.pdf).
- Add back non-business/personal and entertainment expenditure, income tax, prohibited payments, statutory fines and non-arm's-length or otherwise prohibited shareholder/relative remuneration. Contractual damages have a different rule from governmental fines; keep the contract and proof. Do not treat all related-party fees as deductible merely because WHT was paid. [ITL art. 13](https://zatca.gov.sa/ar/HelpCenter/guidelines/Documents/%D9%86%D8%B8%D8%A7%D9%85%20%D8%B6%D8%B1%D9%8A%D8%A8%D8%A9%20%D8%A7%D9%84%D8%AF%D8%AE%D9%84.pdf); [IR art. 10](https://zatca.gov.sa/en/RulesRegulations/Taxes/Documents/Regulations_of_Income_Tax.pdf).
- Test bad debts against prior revenue recognition, actual write-off, recovery evidence, the accountant certificate and the related-party restriction; include later recoveries. General provisions/reserves are not automatically deductible. Separate the specific bank/insurance rules and deductible utilisation of previously added-back provisions. [ITL arts. 14-15](https://zatca.gov.sa/ar/HelpCenter/guidelines/Documents/%D9%86%D8%B8%D8%A7%D9%85%20%D8%B6%D8%B1%D9%8A%D8%A8%D8%A9%20%D8%A7%D9%84%D8%AF%D8%AE%D9%84.pdf); [IR art. 9(3)-(6)](https://zatca.gov.sa/en/RulesRegulations/Taxes/Documents/Regulations_of_Income_Tax.pdf).
- Donations require the permitted public or licensed Saudi non-profit recipient and payment in the tax year. Research expenditure must earn taxable income; land and research equipment are not automatically expensed. [ITL arts. 11, 16](https://zatca.gov.sa/ar/HelpCenter/guidelines/Documents/%D9%86%D8%B8%D8%A7%D9%85%20%D8%B6%D8%B1%D9%8A%D8%A8%D8%A9%20%D8%A7%D9%84%D8%AF%D8%AE%D9%84.pdf).
- Reverse book depreciation and compute the statutory pools when they differ. Land is excluded; apply the asset class, additions/disposals and statutory pool mechanics, including the partial-cost rule, rather than simply deducting all book depreciation. Preserve a pool roll-forward for the return. [ITL art. 17](https://zatca.gov.sa/ar/HelpCenter/guidelines/Documents/%D9%86%D8%B8%D8%A7%D9%85%20%D8%B6%D8%B1%D9%8A%D8%A8%D8%A9%20%D8%A7%D9%84%D8%AF%D8%AE%D9%84.pdf).
- Test securities gains, non-business disposals and qualifying investment dividends separately. For the dividend exemption, the resident capital company's participation must meet the statutory minimum and holding period; do not exempt every foreign dividend. [ITL art. 10](https://zatca.gov.sa/ar/HelpCenter/guidelines/Documents/%D9%86%D8%B8%D8%A7%D9%85%20%D8%B6%D8%B1%D9%8A%D8%A8%D8%A9%20%D8%A7%D9%84%D8%AF%D8%AE%D9%84.pdf).

| Additional computation parameter | Condition | Official source |
|---|---|---|
| Dividend participation exemption | At least 10% capital participation held for at least 1 year; apply art. 10(c) to the recipient investment | ITL art. 10(c), [law](https://zatca.gov.sa/ar/HelpCenter/guidelines/Documents/%D9%86%D8%B8%D8%A7%D9%85%20%D8%B6%D8%B1%D9%8A%D8%A8%D8%A9%20%D8%A7%D9%84%D8%AF%D8%AE%D9%84.pdf) |
| Fixed buildings depreciation | 5% statutory pool rate, subject to art. 17 mechanics | ITL art. 17(b)(1), [law](https://zatca.gov.sa/ar/HelpCenter/guidelines/Documents/%D9%86%D8%B8%D8%A7%D9%85%20%D8%B6%D8%B1%D9%8A%D8%A8%D8%A9%20%D8%A7%D9%84%D8%AF%D8%AE%D9%84.pdf) |
| Movable industrial/agricultural buildings | 10% statutory pool rate | ITL art. 17(b)(2), [law](https://zatca.gov.sa/ar/HelpCenter/guidelines/Documents/%D9%86%D8%B8%D8%A7%D9%85%20%D8%B6%D8%B1%D9%8A%D8%A8%D8%A9%20%D8%A7%D9%84%D8%AF%D8%AE%D9%84.pdf) |
| Machinery, equipment, computers/software and vehicles | 25% statutory pool rate | ITL art. 17(b)(3), [law](https://zatca.gov.sa/ar/HelpCenter/guidelines/Documents/%D9%86%D8%B8%D8%A7%D9%85%20%D8%B6%D8%B1%D9%8A%D8%A8%D8%A9%20%D8%A7%D9%84%D8%AF%D8%AE%D9%84.pdf) |
| Geological survey/exploration and resource-development preparatory costs | 20% statutory pool rate | ITL art. 17(b)(4), [law](https://zatca.gov.sa/ar/HelpCenter/guidelines/Documents/%D9%86%D8%B8%D8%A7%D9%85%20%D8%B6%D8%B1%D9%8A%D8%A8%D8%A9%20%D8%A7%D9%84%D8%AF%D8%AE%D9%84.pdf) |
| Other depreciable tangible/intangible assets in residual class | 10% statutory pool rate | ITL art. 17(b)(5), [law](https://zatca.gov.sa/ar/HelpCenter/guidelines/Documents/%D9%86%D8%B8%D8%A7%D9%85%20%D8%B6%D8%B1%D9%8A%D8%A8%D8%A9%20%D8%A7%D9%84%D8%AF%D8%AE%D9%84.pdf) |

**Financing-cost limitation:** deductible loan charges are the lesser of the qualifying actual charges and **loan-charge income + 50% × (A − B)**, where A is taxable income excluding loan-charge income and B is allowable expenses excluding loan-charge expense. Thus depreciation remains in B if deductible: the rule is not 50% of EBITDA. Banks and loan charges funding capital assets that are capitalised during construction are excluded from this formula under the amended paragraph. Retain the underlying income, expense and capitalisation schedules. No automatic carry-forward of disallowed financing cost is established here. [IR art. 9(2)](https://zatca.gov.sa/en/RulesRegulations/Taxes/Documents/Regulations_of_Income_Tax.pdf), [2023 gazette amendment](https://www.uqn.gov.sa/details?p=23668).

For a foreign branch, distinguish direct evidenced services/costs from prohibited head-office royalty, financing and estimated indirect administrative allocations. The special foreign-bank exception requires its own calculation. WHT classification is a separate inquiry and does not prove CIT deductibility. [IR art. 10(10)](https://zatca.gov.sa/en/RulesRegulations/Taxes/Documents/Regulations_of_Income_Tax.pdf); [WHT guideline p. 15](https://zatca.gov.sa/en/HelpCenter/guidelines/Documents/General-Guideline-for-Withholding-Tax-In-accordance-with-the-provisions-of-the-Income-Tax-Law-and-its-Implementing-Regulations.pdf).

### 4. Apply losses, ownership and credits

Carry only eligible, substantiated tax operating losses, not book losses or losses from exempt/non-taxable activity. The carry-forward has no ordinary time limit, but annual use is capped as in the table. There is no loss carry-back method here. On a change of at least 50% of the non-Saudi ownership/control share, ITL art. 43(b) restricts pre-change losses **unless the company continues the same activity**. This statutory exception controls over the older regulation's unqualified wording. Keep separate gas and oil loss bases. [ITL arts. 21, 43](https://zatca.gov.sa/ar/HelpCenter/guidelines/Documents/%D9%86%D8%B8%D8%A7%D9%85%20%D8%B6%D8%B1%D9%8A%D8%A8%D8%A9%20%D8%A7%D9%84%D8%AF%D8%AE%D9%84.pdf); [IR art. 11](https://zatca.gov.sa/en/RulesRegulations/Taxes/Documents/Regulations_of_Income_Tax.pdf).

Apply the documented taxable ownership share consistently and compute CIT. Reconcile eligible advance payments and credit certificates to the tax payment account. An amount effectively connected with and included in a PE's tax base follows ITL art. 68(f); any WHT actually deducted from an amount included in a taxpayer's base is creditable under art. 68(g). Do not take an unsupported foreign-tax credit, claim a credit twice or assume every payment to a PE is subject to final WHT. Treaty/foreign-credit analysis not established by the facts remains open. [ITL art. 68](https://zatca.gov.sa/ar/HelpCenter/guidelines/Documents/%D9%86%D8%B8%D8%A7%D9%85%20%D8%B6%D8%B1%D9%8A%D8%A8%D8%A9%20%D8%A7%D9%84%D8%AF%D8%AE%D9%84.pdf); [WHT guideline pp. 15-17, 31](https://zatca.gov.sa/en/HelpCenter/guidelines/Documents/General-Guideline-for-Withholding-Tax-In-accordance-with-the-provisions-of-the-Income-Tax-Law-and-its-Implementing-Regulations.pdf).

### 5. Prepare related-party disclosures separately from the CIT calculation

Use the actual functions, assets, risks, terms and comparable transactions; document why the selected method fits. The bylaws provide comparable uncontrolled price, resale price, cost plus, transactional net margin and profit split methods, with conditions for another method. Disclosure is not the same test as master/local-file retention or CbCR. [TP Bylaws arts. 5-9, 14-19](https://zatca.gov.sa/ar/RulesRegulations/Taxes/Documents/Transfer%20Pricing%202019%20%D8%AA%D8%B9%D9%84%D9%8A%D9%85%D8%A7%D8%AA%20%D8%AA%D8%B3%D8%B9%D9%8A%D8%B1%20%D8%A7%D9%84%D9%85%D8%B9%D8%A7%D9%85%D9%84%D8%A7%D8%AA.pdf).

| Obligation | Test for the ordinary CIT/mixed taxpayer | Official source |
|---|---|---|
| Related-party disclosure form and licensed-accountant certificate | Disclose the required transaction, relationship, ownership, financial and method information with the return, within 120 days of year-end | TP Bylaws art. 14, [bylaws](https://zatca.gov.sa/ar/RulesRegulations/Taxes/Documents/Transfer%20Pricing%202019%20%D8%AA%D8%B9%D9%84%D9%8A%D9%85%D8%A7%D8%AA%20%D8%AA%D8%B3%D8%B9%D9%8A%D8%B1%20%D8%A7%D9%84%D9%85%D8%B9%D8%A7%D9%85%D9%84%D8%A7%D8%AA.pdf) |
| Master file and local file | Retain required content; small-enterprise documentation exception for CIT/mixed taxpayers with arm's-length related-party transactions **not exceeding SAR 6,000,000 in 12 months**, subject to ZATCA's override powers | TP Bylaws art. 1(29)(a), arts. 16-17, 19; figure read from the official scanned consolidation, [bylaws](https://zatca.gov.sa/ar/RulesRegulations/Taxes/Documents/Transfer%20Pricing%202019%20%D8%AA%D8%B9%D9%84%D9%8A%D9%85%D8%A7%D8%AA%20%D8%AA%D8%B3%D8%B9%D9%8A%D8%B1%20%D8%A7%D9%84%D9%85%D8%B9%D8%A7%D9%85%D9%84%D8%A7%D8%AA.pdf) |
| CbCR population | Multinational group consolidated revenue **over SAR 3,200,000,000 in the preceding reporting year**; apply reporting-entity and local-filing conditions | TP Bylaws art. 18(a)-(c), (g), [bylaws](https://zatca.gov.sa/ar/RulesRegulations/Taxes/Documents/Transfer%20Pricing%202019%20%D8%AA%D8%B9%D9%84%D9%8A%D9%85%D8%A7%D8%AA%20%D8%AA%D8%B3%D8%B9%D9%8A%D8%B1%20%D8%A7%D9%84%D9%85%D8%B9%D8%A7%D9%85%D9%84%D8%A7%D8%AA.pdf) |
| CbCR report versus notification | Report within 12 months after the group's reporting year; notify reporting entity and jurisdiction within 120 days of year-end | TP Bylaws art. 18(d), (f), [bylaws](https://zatca.gov.sa/ar/RulesRegulations/Taxes/Documents/Transfer%20Pricing%202019%20%D8%AA%D8%B9%D9%84%D9%8A%D9%85%D8%A7%D8%AA%20%D8%AA%D8%B3%D8%B9%D9%8A%D8%B1%20%D8%A7%D9%84%D9%85%D8%B9%D8%A7%D9%85%D9%84%D8%A7%D8%AA.pdf) |
| ZATCA documentation request where specified | Comply with the notice; the relevant minimum response period is 30 days | TP Bylaws arts. 16(b), 17(b), 19(b)-(c), [bylaws](https://zatca.gov.sa/ar/RulesRegulations/Taxes/Documents/Transfer%20Pricing%202019%20%D8%AA%D8%B9%D9%84%D9%8A%D9%85%D8%A7%D8%AA%20%D8%AA%D8%B3%D8%B9%D9%8A%D8%B1%20%D8%A7%D9%84%D9%85%D8%B9%D8%A7%D9%85%D9%84%D8%A7%D8%AA.pdf) |

A small-enterprise retention exception does not waive arm's-length pricing or the disclosure obligation. Read the exceptions for non-institutional natural persons, exempt wholly state-owned entities, investment funds and transactions within eligible consolidated Zakat groups, together with ZATCA's power to require documentation for zone/exempt-party transactions, artificial arrangements, corresponding adjustments and international obligations. Zakat-only implementation and its phased rules belong in the Zakat file, not an assumed CIT threshold. The old common SAR 750 million trigger for MF/LF/CbCR was unsupported and is not a usable test. [TP Bylaws arts. 14, 18-19](https://zatca.gov.sa/ar/RulesRegulations/Taxes/Documents/Transfer%20Pricing%202019%20%D8%AA%D8%B9%D9%84%D9%8A%D9%85%D8%A7%D8%AA%20%D8%AA%D8%B3%D8%B9%D9%8A%D8%B1%20%D8%A7%D9%84%D9%85%D8%B9%D8%A7%D9%85%D9%84%D8%A7%D8%AA.pdf).

## Boundary and exception table

| Situation | Required treatment |
|---|---|
| Ordinary Saudi/GCC-only ownership | Test the actual statutory Zakat population and route to Zakat; retain CIT ownership exceptions. |
| Banks, insurance, funds | Rate reference is not a complete sector computation. Apply R-SA-CT-2. |
| Group, share-for-share exchange, merger or asset rollover | Separate CIT taxpayers remain the default; statutory reorganisations and asset transfers require a transaction-specific opinion. Apply R-SA-CT-3. |
| RHQ, ILBZ, KAEC, Ras Al-Khair, NEOM or another incentive | Obtain the actual licence, qualifying activities, income split and applicable instrument before any incentive. Apply R-SA-CT-4. |
| Gas, oil or concessions | Identify the separate statutory base and concession terms; rate references do not establish an executable sector computation. Apply R-SA-CT-5. |
| Treaty PE, attribution, foreign tax or relief | Establish the particular treaty and facts. No treaty threshold is inferred from the country name. Apply R-SA-CT-10. |
| Pillar Two/DMTT | No enacted Saudi instrument/effective-date conclusion is established here. Do not model an expected law as current law. Apply R-SA-CT-9. |

## Worked cases

All money inputs below are **illustrative case facts**, not legal thresholds. The original names and 2025 periods are preserved. These are **2025-2026 filing-cycle** reconciliations using the cited ordinary rules, not approval of a historical return.

### 1. GlobalTech Saudi LLC: reconcile the inconsistent expense inputs

The original 100%-foreign-owned company has fiscal year **1 January-31 December 2025**, revenue **SAR 80 million**, expenses excluding interest **SAR 50 million**, financing cost **SAR 8 million**, stated EBITDA **SAR 38 million**, depreciation **SAR 4 million** and eligible losses **SAR 6 million**. These figures do not reconcile without an assumption. For this scenario the expense ledger confirms that the SAR 50 million **already includes** the SAR 4 million allowable depreciation, there is no loan-charge income, and no further adjustments apply. EBIT is therefore SAR 30 million and implied EBITDA SAR 34 million; the separately supplied SAR 38 million is rejected as unreconciled, not silently used.

IR art. 9(2) gives a financing cap of **SAR 15 million**, so the full SAR 8 million is deductible. Pre-loss income is **SAR 22 million**. The loss deduction is **SAR 5.5 million**, leaving **SAR 0.5 million** carried forward and **SAR 16.5 million** taxable. CIT is **SAR 3.3 million**. The old SAR 2.7 million result deducted depreciation twice and used the wrong base. If the expense ledger excludes depreciation instead, rebuild the workpaper; do not present this conditional result as final. [IR arts. 9, 11](https://zatca.gov.sa/en/RulesRegulations/Taxes/Documents/Regulations_of_Income_Tax.pdf); [ITL art. 7(a)](https://zatca.gov.sa/ar/HelpCenter/guidelines/Documents/%D9%86%D8%B8%D8%A7%D9%85%20%D8%B6%D8%B1%D9%8A%D8%A8%D8%A9%20%D8%A7%D9%84%D8%AF%D8%AE%D9%84.pdf).

```oa-check
name: GlobalTech Saudi LLC historical 2025 expense reconciliation
inputs:
  revenue: 80000000
  expenses_including_depreciation: 50000000
  depreciation: 4000000
  loan_income: 0
  actual_financing_cost: 8000000
  losses: 6000000
steps:
  - ebit: revenue - expenses_including_depreciation
  - implied_ebitda: ebit + depreciation
  - financing_cap: loan_income + 0.5 * (revenue - loan_income - expenses_including_depreciation)
  - allowed_financing_cost: min(actual_financing_cost, financing_cap)
  - pre_loss_income: revenue - expenses_including_depreciation - allowed_financing_cost
  - loss_used: min(losses, pre_loss_income * 0.25)
  - loss_carried_forward: losses - loss_used
  - taxable_income: pre_loss_income - loss_used
  - cit: taxable_income * 0.20
expected:
  implied_ebitda: 34000000
  financing_cap: 15000000
  loss_used: 5500000
  loss_carried_forward: 500000
  cit: 3300000
```

The ordinary return/payment deadline is **30 April 2026**, derived from ITL arts. 60(b), 69 for this year-end. An accountant certification is required under art. 60(e), since the statutory taxable-income trigger is exceeded; it is not professional approval by this skill's writer.

### 2. Riyadh Trading Co.: separate the ownership bases

Preserve the original **60% Saudi/40% foreign**, **SAR 25 million** adjusted taxable profit and **SAR 30 million** independently established Zakat base. The ordinary CIT share is **SAR 10 million** and CIT **SAR 2 million**. The Zakat workpaper receives the **SAR 18 million** Saudi share of its own base. Its original SAR 450,000 amount is valid only for the specified full-Hijri-rate scenario; a Gregorian period requires the actual-day computation in [sa-zakat](sa-zakat.md). Do not publish the old combined SAR 2.45 million as an unconditional Gregorian-year liability. [ITL arts. 6-7](https://zatca.gov.sa/ar/HelpCenter/guidelines/Documents/%D9%86%D8%B8%D8%A7%D9%85%20%D8%B6%D8%B1%D9%8A%D8%A8%D8%A9%20%D8%A7%D9%84%D8%AF%D8%AE%D9%84.pdf); [Zakat Regulations arts. 13, 15](https://zatca.gov.sa/en/RulesRegulations/Documents/ZAKAT%20COLLECTION.pdf).

```oa-check
name: Riyadh Trading Co separate CIT and Zakat workpaper bases
inputs:
  adjusted_taxable_profit: 25000000
  foreign_share: 0.40
  separately_verified_zakat_base: 30000000
  saudi_share: 0.60
steps:
  - cit_base: adjusted_taxable_profit * foreign_share
  - cit: cit_base * 0.20
  - zakat_workpaper_base: separately_verified_zakat_base * saudi_share
expected:
  cit_base: 10000000
  cit: 2000000
  zakat_workpaper_base: 18000000
```

### 3. ForeignCo SARL: decide whether the head-office charge is deductible

The original treaty-country company has an assumed established Riyadh project PE, **1 January-31 December 2025**, Saudi revenue **SAR 40 million**, local expenses **SAR 28 million** and head-office charges **SAR 5 million**. The original result was SAR 7 million profit and SAR 1.4 million CIT. That arithmetic is conditional on all charges being deductible direct expenditure. If the SAR 5 million is instead a prohibited estimated allocation of indirect head-office administration, add it back: profit is **SAR 12 million** and CIT **SAR 2.4 million**. Obtain the contracts, cost evidence and treaty attribution opinion before choosing either result. This is a genuine deductibility decision, not permission to elect the cheaper branch. [IR art. 10(10)](https://zatca.gov.sa/en/RulesRegulations/Taxes/Documents/Regulations_of_Income_Tax.pdf).

```oa-check
name: ForeignCo SARL direct service versus prohibited head-office allocation
inputs:
  pe_revenue: 40000000
  local_deductible_expenses: 28000000
  head_office_charge: 5000000
steps:
  - profit_if_direct_charge_qualifies: pe_revenue - local_deductible_expenses - head_office_charge
  - cit_if_direct_charge_qualifies: profit_if_direct_charge_qualifies * 0.20
  - profit_if_prohibited_indirect_allocation: pe_revenue - local_deductible_expenses
  - cit_if_prohibited_indirect_allocation: profit_if_prohibited_indirect_allocation * 0.20
  - tax_difference: cit_if_prohibited_indirect_allocation - cit_if_direct_charge_qualifies
expected:
  cit_if_direct_charge_qualifies: 1400000
  cit_if_prohibited_indirect_allocation: 2400000
  tax_difference: 1000000
```

Payments effectively connected with the registered PE belong in its return; retain any actual WHT certificate for the credit test. A head-office remittance or distribution needs a separate [WHT](sa-withholding-tax.md) workpaper. The assumed PE in this arithmetic example does not prove the treaty's PE threshold. The ordinary historical deadline is **30 April 2026**, subject to the actual period and applicable procedural treatment.

## When to refuse or refer

Preserve these original refusal identifiers:

- **R-SA-CT-1:** ordinary Zakat-only ownership: route to the Zakat skill after testing statutory exceptions.
- **R-SA-CT-2:** banks, insurance, mutual/investment funds or specialised sector bases: refer for the sector method.
- **R-SA-CT-3:** consolidated CIT, mergers, demergers, exchanges or rollovers: no invented group return or automatic tax neutrality.
- **R-SA-CT-4:** RHQ, ILBZ, KAEC, Ras Al-Khair, NEOM and other incentive positions: no unproven exemption.
- **R-SA-CT-5:** upstream/concession oil, hydrocarbon and specialised gas calculations: refer with the statutory-rate classification.
- **R-SA-CT-6:** active assessment, audit, objections, tax committees or appellate litigation: preserve notices and evidence; do not pre-empt the dispute.
- **R-SA-CT-7:** TP controversy, advance pricing or mutual-agreement procedures: refer with contracts and prior positions.
- **R-SA-CT-8:** another tax/job: load the named sibling, including the existing RETT skill.
- **R-SA-CT-9:** Pillar Two/DMTT with no verified enacted instrument: stop that calculation.
- **R-SA-CT-10:** treaty residence, PE, attribution or relief: no automatic treaty conclusion without the specific text and evidence.

Also stop for missing financial statements/ownership, unsubstantiated losses, conflicting expense totals, unknown sector, unsupported credits or an unverified law change. Use explicit open items; never substitute a high-rate or foreign-owner “conservative default”. All outputs remain working papers pending qualified professional sign-off.

## Filing and payment

1. Register with ZATCA before the end of the first fiscal year, subject to the separate withholding-only exception. Establish the actual tax year and the correct taxpayer registration. [ITL art. 57](https://zatca.gov.sa/ar/HelpCenter/guidelines/Documents/%D9%86%D8%B8%D8%A7%D9%85%20%D8%B6%D8%B1%D9%8A%D8%A8%D8%A9%20%D8%A7%D9%84%D8%AF%D8%AE%D9%84.pdf).
2. In the taxpayer's ZATCA account, use **Returns**, choose the applicable annual return and period, complete the approved form and reconcile its taxable-income, loss, ownership, CIT and credit/payment schedules to the workpapers. Keep financial statements, depreciation, related-party, ownership, loss and credit evidence. Submit only after professional review; this skill does not fabricate current portal box numbers. [ITL art. 60](https://zatca.gov.sa/ar/HelpCenter/guidelines/Documents/%D9%86%D8%B8%D8%A7%D9%85%20%D8%B6%D8%B1%D9%8A%D8%A8%D8%A9%20%D8%A7%D9%84%D8%AF%D8%AE%D9%84.pdf); [May 2026 guideline §§5-6](https://zatca.gov.sa/en/HelpCenter/guidelines/Documents/Simplified-Guideline-for-Income-Tax.pdf).
3. Check whether licensed-accountant certification is required: ITL art. 60(e), as detailed in IR art. 57(6), applies where taxable income **before deducting expenses** exceeds **SAR 1,000,000**; do not test only net profit. File and pay within **120 days** of year-end; cessation has a separate **60-day** return/notification rule. [ITL arts. 60, 69](https://zatca.gov.sa/ar/HelpCenter/guidelines/Documents/%D9%86%D8%B8%D8%A7%D9%85%20%D8%B6%D8%B1%D9%8A%D8%A8%D8%A9%20%D8%A7%D9%84%D8%AF%D8%AE%D9%84.pdf); [IR art. 57(6)](https://zatca.gov.sa/en/RulesRegulations/Taxes/Documents/Regulations_of_Income_Tax.pdf).
4. Compute each advance instalment as **25% × (prior-year return tax − prior-year art. 68 WHT)**. The obligation does not arise if that computed instalment is below **SAR 500,000**. Where applicable, pay by the last day of months **6, 9 and 12** of the current tax year. Request any reduction from ZATCA under art. 70(c); an estimate is not an automatic waiver. Reconcile instalments and eligible credits to the final balance, then pay through the issued **SADAD** invoice and retain the receipt. [ITL art. 70, boundaries in words on the page](https://zatca.gov.sa/ar/HelpCenter/guidelines/Documents/%D9%86%D8%B8%D8%A7%D9%85%20%D8%B6%D8%B1%D9%8A%D8%A8%D8%A9%20%D8%A7%D9%84%D8%AF%D8%AE%D9%84.pdf); [guideline §6](https://zatca.gov.sa/en/HelpCenter/guidelines/Documents/Simplified-Guideline-for-Income-Tax.pdf).
5. Retain Arabic books/supporting records under the applicable rules; WHT evidence has its own minimum retention rule in the WHT skill. Assessment is ordinarily within **5 years from the return's statutory filing deadline**, with **10 years** for non-filing or an incomplete/incorrect return intended to evade tax and written-consent exceptions. It is not ordinarily measured from the actual filing date. [ITL arts. 58, 65](https://zatca.gov.sa/ar/HelpCenter/guidelines/Documents/%D9%86%D8%B8%D8%A7%D9%85%20%D8%B6%D8%B1%D9%8A%D8%A8%D8%A9%20%D8%A7%D9%84%D8%AF%D8%AE%D9%84.pdf).

### Penalties: compute the applicable provision, not one generic percentage

| Breach and conditions | Statutory amount | Official source |
|---|---|---|
| Failure to register by the required date | Natural person SAR 1,000; joint-stock capital company SAR 10,000; other entities SAR 5,000 | IR art. 55; May 2026 guideline §7.1, [guideline](https://zatca.gov.sa/en/HelpCenter/guidelines/Documents/Simplified-Guideline-for-Income-Tax.pdf) |
| Late annual filing | Higher of 1% revenue capped at SAR 20,000 and the applicable unpaid-tax percentage below | ITL art. 76; IR art. 67, [law](https://zatca.gov.sa/ar/HelpCenter/guidelines/Documents/%D9%86%D8%B8%D8%A7%D9%85%20%D8%B6%D8%B1%D9%8A%D8%A8%D8%A9%20%D8%A7%D9%84%D8%AF%D8%AE%D9%84.pdf) |
| Unpaid-tax limb of late-filing penalty | 5% for delay up to 30 days; 10% over 30 through 90; 20% over 90 through 365; 25% over 365 | ITL art. 76(b), [law](https://zatca.gov.sa/ar/HelpCenter/guidelines/Documents/%D9%86%D8%B8%D8%A7%D9%85%20%D8%B6%D8%B1%D9%8A%D8%A8%D8%A9%20%D8%A7%D9%84%D8%AF%D8%AE%D9%84.pdf) |
| Late payment, including required WHT and advances | Additional 1% of unpaid tax per 30 days of delay from the tax due date | ITL art. 77(a), [law](https://zatca.gov.sa/ar/HelpCenter/guidelines/Documents/%D9%86%D8%B8%D8%A7%D9%85%20%D8%B6%D8%B1%D9%8A%D8%A8%D8%A9%20%D8%A7%D9%84%D8%AF%D8%AE%D9%84.pdf) |
| False information/fraud intended to evade tax | Additional 25% of the resulting tax difference, subject to the statutory conditions | ITL art. 77(b), [law](https://zatca.gov.sa/ar/HelpCenter/guidelines/Documents/%D9%86%D8%B8%D8%A7%D9%85%20%D8%B6%D8%B1%D9%8A%D8%A8%D8%A9%20%D8%A7%D9%84%D8%AF%D8%AE%D9%84.pdf) |

The old 5%-per-month/capped-at-25% CIT late-payment rule is incorrect. The current temporary penalty initiative must be assessed separately: **1 July-31 December 2026**, with registration, all required returns and principal payment or an approved adhered-to instalment plan; returns due **after 30 June 2026**, evasion penalties, previously paid fines and the listed VAT-law penalties are excluded. It does not cancel tax or make future late payment acceptable. Retain evidence of eligibility and the authority's account treatment. [ZATCA initiative guideline pp. 3-9, 11](https://zatca.gov.sa/en/HelpCenter/guidelines/Documents/Cancellation-of-Fines-Exemption%20of-Financial-Penalties.pdf).

## Completion checklist

- Taxpayer, business source, PE/activity and ownership conclusions are documented; no unknown fact became a legal presumption.
- Book-to-tax reconciliation, financing limit, depreciation pools and loss eligibility/cap recompute; no depreciation or credit is deducted twice.
- CIT and Zakat use distinct bases; WHT, related-party disclosure, MF/LF and CbCR are tested separately.
- Return schedules reconcile to the workpapers and payment account; the right deadline and advance-payment test are used.
- All original cases, refusal IDs and exceptional topics have a current destination or an explicit unresolved boundary below.

## Sources

| Official text | Actual reading on 2026-11-16 |
|---|---|
| [Income Tax Law M/1, official Arabic consolidation](https://zatca.gov.sa/ar/HelpCenter/guidelines/Documents/%D9%86%D8%B8%D8%A7%D9%85%20%D8%B6%D8%B1%D9%8A%D8%A8%D8%A9%20%D8%A7%D9%84%D8%AF%D8%AE%D9%84.pdf) | Read on 2026-11-16. Read for arts. 2-17, 21, 43, 57-60, 63-65, 68-70, 76-77 and relevant amendment footnotes: scope, source, separate bases, rates, deductions, losses/continuity, procedure, advances and penalties. Arabic controls. |
| [Income Tax Implementing Regulations, official Arabic compilation](https://zatca.gov.sa/en/RulesRegulations/Taxes/Documents/Regulations_of_Income_Tax.pdf) | Read on 2026-11-16. Read for arts. 1, 3-6, 9-11, 55, 63, 66-69 and neighboring conditions. This compilation ends with the stated historical amendments; later statutory text controls, including art. 43's same-activity loss exception. |
| [Simplified Income Tax Guideline, second version May 2026](https://zatca.gov.sa/en/HelpCenter/guidelines/Documents/Simplified-Guideline-for-Income-Tax.pdf) | Read on 2026-11-16. Read pp. 1-10; visually inspected rate and obligation diagrams on pp. 5-6. Used for ordinary rate confirmation, portal steps and penalty explanations. |
| [WHT General Guideline, second version May 2026](https://zatca.gov.sa/en/HelpCenter/guidelines/Documents/General-Guideline-for-Withholding-Tax-In-accordance-with-the-provisions-of-the-Income-Tax-Law-and-its-Implementing-Regulations.pdf) | Read on 2026-11-16. Read pp. 5-42: residence, source, PE interaction, payment classes, exemptions, records and penalty cross-checks. WHT amounts remain owned by the WHT skill. |
| [Zakat Collection Regulations 1445, decisions 1007 and 1248](https://zatca.gov.sa/en/RulesRegulations/Documents/ZAKAT%20COLLECTION.pdf) | Read on 2026-11-16. Read for arts. 1, 3-7, 13, 15, 21-29: ownership/base separation and the calendar-dependent rate boundary. |
| [TP Bylaws, official scanned consolidation amended by decision 8-2-23](https://zatca.gov.sa/ar/RulesRegulations/Taxes/Documents/Transfer%20Pricing%202019%20%D8%AA%D8%B9%D9%84%D9%8A%D9%85%D8%A7%D8%AA%20%D8%AA%D8%B3%D8%B9%D9%8A%D8%B1%20%D8%A7%D9%84%D9%85%D8%B9%D8%A7%D9%85%D9%84%D8%A7%D8%AA.pdf) | Read on 2026-11-16. Read relevant definitions, arts. 5-9, 14, 16-19 and neighboring exceptions; visually checked the small-enterprise and CbCR threshold pages (PDF pp. 7, 25-26). OCR is a reading aid, not the controlling text. |
| [Cancellation of Fines and Exemption of Financial Penalties, effective July 2026](https://zatca.gov.sa/en/HelpCenter/guidelines/Documents/Cancellation-of-Fines-Exemption%20of-Financial-Penalties.pdf) | Read on 2026-11-16. Read pp. 3-11: exact period, exclusions, required returns, principal settlement and instalment consequences. |
| [Official Gazette, regulation amendments dated 12 September 2023](https://www.uqn.gov.sa/details?p=23668) | Read on 2026-11-16. Read the old/new art. 9(2) comparison and neighboring amendments; confirms the bank and construction-capitalisation exclusions. |

**Not yet confirmed:** no executable 2026 Saudi Pillar Two/DMTT enactment or effective-date conclusion; special-zone/RHQ qualification and concession-specific oil/gas/downstream computations; bank/insurance/fund special bases; treaty PE/attribution and foreign-tax-credit entitlement for a particular taxpayer; current portal box identifiers and case-specific ownership-change allocation; automatic financing-cost carry-forward; any general loss carry-back. These original topics remain review boundaries, not usable exemptions, rates or filing instructions. The historical cases do not establish unpublished 2026 forms or a taxpayer's actual filing position. The ordinary CIT legal record-retention period beyond the separately confirmed WHT requirement must be checked for the record class before disposal.
