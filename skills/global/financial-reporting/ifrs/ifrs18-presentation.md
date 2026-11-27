---
name: ifrs18-presentation
description: IFRS 18 presentation and disclosure, IAS 1 comparative reconciliation, profit or loss classification, management-defined performance measures, expense disclosures and consequential IAS 7 cash flow amendments. Includes scope conditions, reporting controls and bounded arithmetic from the original FY2026 and FY2025 cases. Load alongside financial-reporting-workflow-base.
version: 1.0.2
jurisdiction: GLOBAL
tax_year: 2027
tax_year_notes: Effective for annual reporting periods beginning on or after 1 January 2027, applied retrospectively under IAS 8; earlier application permitted (including FY2026 early adopters).
last_updated: 2026-11-26
depends_on:
  - financial-reporting-workflow-base
category: financial-reporting
tier: 1
reviewed_by: "Talha Mehmood"
reviewed_on: 2026-11-11
sources_checked: IFRS 18 and amended IAS 7 issued texts; operative paragraphs listed in Sources, read 2026-11-26
authored_by: Talha Mehmood, ACA, FCCA
domain: financial-reporting
standard: "IFRS 18 Presentation and Disclosure in Financial Statements"
effective_date: 2027-01-01
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v2.0 (content)
---

# IFRS 18 Presentation and Disclosure in Financial Statements

## Quick reference

Apply IFRS 18 for annual periods beginning on or after **1 January 2027**; earlier application requires disclosure. Apply its IAS 7 amendments at the same time. A FY2026 exercise is an **early-adoption** exercise, not a mandatory FY2026 restatement. [IFRS 18.C1](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html#IFRS18_C1); [IAS 7.64](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ias7.html#IAS07_64).

Classify profit or loss into operating, investing, financing, income taxes and discontinued operations. Operating is residual, including volatile or non-recurring items. Assess specified main business activities before using the general classification rules below. [IFRS 18.47–52](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html#IFRS18_47).

Present operating profit or loss, profit or loss before financing and income taxes (subject to the customer-financing policy exception below), and profit or loss. Additional subtotals are subject to the statement-structure, consistency and prominence requirements; there is no blanket prohibition on an adjusted subtotal. [IFRS 18.24, 69–74](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html#IFRS18_69).

**Approval boundary:** The original author and approval metadata are retained. This correction awaits the approving accountant; those historical fields do not establish approval of these amendments.

## Scope

Use this Guide for presentation and disclosure in financial statements prepared under IFRS Accounting Standards. Recognition and measurement of particular transactions remain governed by the applicable other Standards. Profit-oriented terminology can be adapted by entities with not-for-profit activities. [IFRS 18.2–6](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html#IFRS18_2).

For condensed IAS 34 interim statements, IFRS 18 generally does not apply, but its aggregation/disaggregation requirements in paragraphs 41–45 and MPM requirements in paragraphs 117–125 do apply. First-year transition rules below also matter. [IFRS 18.5](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html#IFRS18_5).

Use the [financial reporting workflow base](../financial-reporting-workflow-base.md) for the output contract. This Guide's working-paper controls supplement the accounting requirements; they do not create new requirements of the Standard. Do not infer local endorsement, statutory filing requirements, recognition amounts or tax deductibility from this global presentation Guide.

## Ask the client first

Read the available financial statements, notes and records before requesting missing information. Obtain:

- Reporting entity, consolidated/separate/individual basis, current and comparative periods, and evidence of the early-adoption decision where applicable.
- Detailed components of other income/expenses, finance costs/income, gains/losses and net FX; asset and liability roll-forwards; cash flow schedules and accounting policies.
- Evidence about investing in assets and providing financing to customers as main business activities, at the reporting-entity level.
- Derivative designation, identified risks and supporting hedge documentation; held-for-sale/discontinued-operation facts.
- Operating expense presentation and nature breakdowns; public performance communications for the reporting period; actual tax effects and NCI interests for each MPM adjustment.
- Whether IFRS 19 is elected, a measurement election is proposed on transition, or local tax/US GAAP conclusions are also requested. Use the referral boundaries below for those points.

Do not invent note splits, tax rates, ownership percentages or a balancing figure. Mark missing client evidence as a delivery hold.

## The method, step by step

### Transition and reporting period

Apply IFRS 18 retrospectively under IAS 8. The exemption is from the quantitative information specified in **IAS 8.28(f)**; it is not limited in IFRS 18.C2 to current-period information. [IFRS 18.C2](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html#IFRS18_C2).

In the first annual statements applying IFRS 18, disclose a reconciliation for **each profit or loss line item** for the immediately preceding comparative period between the restated IFRS 18 amounts and the previously presented IAS 1 amounts. Reconciliations for the current or earlier comparative periods are optional. [IFRS 18.C3, C6](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html#IFRS18_C3).

In condensed IAS 34 statements during the first year, present each heading expected under IFRS 18 and the subtotals required by paragraphs 69–74. Do not revert to IAS 34.10's headings/subtotals rule until the first IFRS 18 annual statements have been issued. [IFRS 18.C4](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html#IFRS18_C4).

For IAS 34 interim statements in that first year, disclose line-item reconciliations for the immediately preceding comparative current and cumulative periods under IAS 34.16A(a); IFRS 19 users instead use its paragraph 246(a). [IFRS 18.C5](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html#IFRS18_C5).

### Component classification: Rules A2.1–A2.6

For an entity without specified main business activities, apply the following at component level. Apply the FX, derivative and held-for-sale rules separately rather than forcing such items through an unqualified liability/asset rule.

| Component | Treatment and conditions | Official source |
|---|---|---|
| Discontinued operations (A2.1) | Classify the income and expenses required by IFRS 5 in discontinued operations. They are outside the other four classification categories. | [IFRS 18.68, B29](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html#IFRS18_68) |
| Income taxes (A2.2) | Tax expense/income included in profit or loss applying IAS 12 and related FX differences belong in income taxes. This is not a rule that every statutory levy is an income tax. | [IFRS 18.67](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html#IFRS18_67) |
| Liabilities arising only from raising finance (A2.3) | Use the originating transaction: receipt of finance and its later return, as described in B50. Subject to the special rules below, measurement/derecognition income and expenses and incremental issue/extinguishment expenses are financing. Examples include borrowing interest, debt transaction-cost amortisation, liability fair-value changes, dividends on liability-classified shares and extinguishment gains/losses. | [IFRS 18.59–60, B50–B52](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html#IFRS18_59) |
| Other liabilities (A2.4) | Financing contains interest income/expense and effects of interest-rate changes **only when identified for applying other IFRS requirements**, subject to the special rules below. Examples include lease interest, net defined-benefit liability/asset interest, provision discount unwinding/rate changes, and identified financing components on payables or contract liabilities. | [IFRS 18.61, B53–B54](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html#IFRS18_61) |
| Remaining amounts on other liabilities | Purchased goods/services expense, current/past service cost and fair-value remeasurements of business-combination contingent consideration are operating under the specified examples. Do not classify all contingent-consideration changes as financing. | [IFRS 18.B55](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html#IFRS18_B55) |
| Investing assets (A2.5) | Subject to specified-main-business exceptions, the assets are associates/JVs/unconsolidated subsidiaries, cash/cash equivalents, and other assets generating returns individually and largely independently of other resources. Debt/equity investments and investment property typically meet the last test. Only amounts included in profit or loss are classified here; do not pull FVOCI amounts out of OCI. | [IFRS 18.53, B43–B46](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html#IFRS18_53) |
| Specified investing income/expenses | For those assets, investing includes income generated; initial/subsequent measurement and derecognition amounts; and incremental acquisition/disposal expenses. This covers the applicable interest, dividends, rental income, depreciation, impairment, fair-value and disposal amounts. | [IFRS 18.54, B47](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html#IFRS18_54) |
| Investment property repairs, maintenance and management services | Do **not** move every related expense into investing. Apply the paragraph 54 list to the expense itself. Ongoing service expenses outside that list remain operating under the residual rule. | [IFRS 18.52–54](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html#IFRS18_52) |
| Assets used with other resources | Income/expenses from assets used together to produce/supply goods or services are operating, including depreciation/amortisation, impairment and disposal gains/losses. This covers operating PP&E, ROU assets, intangibles, goodwill, inventories, trade receivables and contract assets as applicable. | [IFRS 18.B48–B49](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html#IFRS18_B48) |
| Residual operating (A2.6) | All profit or loss income/expenses outside the other four categories are operating, including volatile/non-recurring items. Apply this to the actual components of revenue, cost of sales, distribution/administration/R&D, trade ECL, grants for operating costs, operating insurance recoveries, litigation/restructuring charges and bank service charges; a caption such as “finance costs” does not determine the result. | [IFRS 18.52, B42](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html#IFRS18_52) |

### FX overlay: Rule A2.7

Classify IAS 21 profit or loss exchange differences with the income/expenses from the underlying item. Thus trade-balance FX is operating and borrowing FX is financing under the general rules; apply the specified-main-business exceptions where relevant. [IFRS 18.B65–B66](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html#IFRS18_B65).

Where an other-liability transaction produces income/expenses in more than one category, judge whether its exchange difference relates to financing or the other category. Do not allocate that liability's FX between categories; treat similar liabilities consistently. [IFRS 18.B67](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html#IFRS18_B67).

If following the underlying item would involve undue cost or effort, classify the **affected** differences in operating. Assess this for each item; the same assessment may be applied to items with the same facts/circumstances. It is not a general permission to leave an available note split unexplained. [IFRS 18.B68](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html#IFRS18_B68).

### Derivative overlay: Rule A2.8

For a financial instrument designated as a hedging instrument applying IFRS 9, classify profit or loss gains/losses with income/expenses affected by the managed risks. If that requires grossing up gains/losses, put all such gains/losses in operating. **B70 does not give designated instruments an undue-cost-or-effort exception.** [IFRS 18.B70](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html#IFRS18_B70).

Undesignated components of a designated instrument follow its designated component; ineffective portions follow effective portions. [IFRS 18.B71](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html#IFRS18_B71).

An undesignated derivative used to manage identified risks follows B70, but grossing up **or undue cost or effort** puts all its gains/losses in operating. A raw-material risk derivative and a borrowing-interest risk derivative therefore need different underlying-risk analyses. [IFRS 18.B72](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html#IFRS18_B72).

For a derivative not managing identified risks, gains/losses are financing only if it relates to a transaction involving only raising finance, subject to the customer-financing B59 exception; otherwise they are operating. These rules classify categories, not the particular line item, and do not override other Standards. [IFRS 18.B73–B76](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html#IFRS18_B73).

### Specified main business activities: Rule A2.9

Assess investing in particular assets and/or providing financing to customers **from evidence, for the reporting entity as a whole**; a group and a subsidiary can reach different conclusions. Disclose the specified main activity. [IFRS 18.49–51, B30–B40](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html#IFRS18_49).

A change in that assessment applies **prospectively from the change date**, not by revising the previous assessment. Disclose the change/date and the before/after amounts and classifications required by 51(c), unless impracticable; disclose impracticability. [IFRS 18.51(c), B41](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html#IFRS18_B41).

For investing as a main activity, paragraph 54 returns from the relevant assets move into operating, **except equity-method investments remain investing**. The non-equity-method exception is not confined to FVTPL: paragraph 55(b) covers assets not accounted for using the equity method. [IFRS 18.55, 58](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html#IFRS18_55).

Cash/cash-equivalent income/expenses are operating if investing in financial assets within 53(c) is a main activity. Otherwise, for a customer-financing main activity, related cash returns are operating; unrelated returns have an operating/investing policy choice linked to the liability choice in 65(a)(ii). If related/unrelated cash cannot be distinguished, classify all its returns in operating. [IFRS 18.56–57](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html#IFRS18_56).

For customer financing as a main activity, income/expenses on finance-raising liabilities related to that activity are operating. Unrelated liabilities have an operating/financing policy choice linked to 56(b)(ii); if they cannot be distinguished, all those liabilities' income/expenses go to operating. Other liabilities' paragraph 61 amounts remain financing, with remaining amounts operating. [IFRS 18.65–66](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html#IFRS18_65).

### Held-for-sale/discontinued overlay: Rule A2.10

For a single asset, derecognition, held-for-sale classification and subsequent held-for-sale measurement income/expenses follow the category used immediately before derecognition/classification. Operating PP&E disposal gains are operating; disposal of investment property not invested in as a main activity is investing. A group of assets/liabilities requires B63–B64's separate analysis, rather than blindly following one asset. [IFRS 18.B60–B64](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html#IFRS18_B60). For a mixed disposal group or subsidiary disposal, use the referral boundary below. Discontinued-operation classification takes priority where IFRS 5 requires it.

### Statement structure, aggregation and expense disclosures: Rules A3.1–A3.7

Operating profit is the total of operating items; profit before financing and income taxes is operating plus investing; profit or loss includes all categories. **Do not present the second subtotal when applying 65(a)(ii)'s policy of putting unrelated finance-raising liability income/expenses in operating.** An additional operating-plus-investing subtotal then cannot be labelled as excluding financing. [IFRS 18.69–74](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html#IFRS18_69).

Additional line items/subtotals are required when necessary for a useful structured summary. They must comprise IFRS-recognised/measured amounts, fit the required statement structure, be consistent over time, and have no greater prominence than required totals/subtotals. Labels must faithfully describe the amounts. A qualifying adjusted subtotal may also be an MPM; presentation on the face does not eliminate the MPM note. [IFRS 18.24, 43, B118](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html#IFRS18_24).

Aggregate shared characteristics and disaggregate differing characteristics when needed for useful summaries/material information. Use “other” only when no more informative label can be found; disclose the information needed to resolve whether a large aggregate of immaterial items hides material information. [IFRS 18.41–43, B25–B26](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html#IFRS18_41).

Present operating expenses by nature, function or both, selecting the most useful structured summary. Each individual line uses only one characteristic. Consider profitability drivers, internal reporting, industry practice and whether allocations would be arbitrary. [IFRS 18.78–81, B80–B83](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html#IFRS18_78).

If any operating line uses function, give a qualitative description of the expenses in each function. Present cost of sales separately **if the functions include a cost-of-sales function**, including the IAS 2.38 inventory expense total. A function line does not automatically imply that every entity has a cost-of-sales function. [IFRS 18.82](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html#IFRS18_82).

If one or more operating lines use function, disclose in a **single note** totals for depreciation (IAS 16/IAS 40/IFRS 16), amortisation (IAS 38), employee benefits (IAS 19 plus employee services under IFRS 2), IAS 36 impairment losses/reversals and IAS 2 inventory write-downs/reversals. For each total disclose the amount related to **each operating line item**, and list any lines outside operating containing related amounts. This is not a requirement for a full matrix of every expense nature and every function. [IFRS 18.83–85](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html#IFRS18_83).

Amounts by nature can include amounts capitalised in assets. If disclosed amounts are not period expenses, explain that fact qualitatively and identify the assets. If such amounts are presented on the face, also present the affected asset carrying-amount change. Do not force a costs-incurred note to equal recognised expense lines without its inventory/capitalisation bridge. [IFRS 18.B84](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html#IFRS18_B84).

Goodwill and intangible assets are separate listed balance-sheet lines in **103(d) and 103(c)**, respectively. Apply the useful-structured-summary exception in paragraph 23 rather than declaring every combined immaterial caption an automatic failure. [IFRS 18.23, 103](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html#IFRS18_103).

### Cash flow statement: Rules A4.1–A4.3

With the indirect method, adjust **operating profit or loss** for non-cash items, accrual/working-capital changes, operating profit or loss amounts whose cash flows are investing/financing, and operating cash flows whose related income/expenses are outside operating profit or loss. Do not assume all old adjustments disappear. [IAS 7.18(b), 20](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ias7.html#IAS07_18).

Do **not** copy IFRS 18 profit or loss categories into IAS 7 automatically. In particular, classifying investment-property rental income as investing in profit or loss does not itself move the rental cash receipts to investing cash flows. Assess receipts/payments under IAS 7's own activity definitions and requirements. [IAS 7.6, 14, 16](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ias7.html#IAS07_14).

Dividends paid are financing cash flows. [IAS 7.33A](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ias7.html#IAS07_33A).

For an entity outside IAS 7.34B's specified-main-business population, **all interest paid**, including capitalised interest, is financing; interest and dividends received are investing. Present each separately and consistently. [IAS 7.31–32, 34A](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ias7.html#IAS07_34A).

For an entity within 34B, classify each total of interest paid, interest received and dividends received in a **single** cash flow category. If the corresponding profit or loss amount is wholly in one category, use the associated cash flow activity. If it spans categories, choose one of the associated activities as an accounting policy for that cash flow total. [IAS 7.34B–34D](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ias7.html#IAS07_34B).

Present income-tax cash flows separately in operating unless specifically identifiable with investing/financing activities. A profit or loss income-taxes category does not imply a separate tax category in cash flows. [IAS 7.35](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ias7.html#IAS07_35).

### Management-defined performance measures: Rules A5.1–A5.3

An MPM is a subtotal of income and expenses used in public communications outside the financial statements to communicate management's view of an aspect of whole-entity financial performance, and is neither listed in 118 nor specifically required by IFRS. Public use creates a presumption of management's view; rebuttal needs reasonable, supportable evidence. Oral communications, their written transcripts and social-media posts are excluded from the public-communications definition. [IFRS 18.117–120, B119](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html#IFRS18_117).

The 118 exclusions are gross profit and similar subtotals; operating profit before depreciation, amortisation and IAS 36 impairments; operating profit plus all equity-method investment income/expenses; the operating-plus-investing subtotal for a 73 entity; profit before income taxes; and continuing-operations profit. A label such as “EBITDA” is not enough to establish an exclusion. Ratios, free cash flow, net debt, revenue-only and non-financial measures are not themselves MPMs, but an income/expense subtotal used as a ratio's numerator/denominator can qualify. [IFRS 18.118, B116–B117, B123](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html#IFRS18_118).

Disclose all qualifying MPMs in a **single note**, explaining management's view, usefulness and calculation, and that similarly labelled measures of other entities may not be comparable. Label/describe each measure clearly without misleading users. [IFRS 18.122–123(a)–(b)](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html#IFRS18_122).

Reconcile each MPM to the most directly comparable 118 subtotal or IFRS-required total/subtotal. Disclose tax and NCI effects **for each reconciling item**, and describe how tax effects were determined. Do not invent an ownership allocation from a headline rate; use the affected entity, tax effects and actual NCI rights. [IFRS 18.123(c)–(e)](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html#IFRS18_123).

Determine tax effects from the underlying transactions using the applicable jurisdictional statutory rates, a reasonable pro-rata allocation of current/deferred tax, or another method producing a more appropriate allocation. When methods differ by item, disclose how each was determined. This is not authority for a universal tax percentage or local deductibility conclusion. [IFRS 18.B141–B142](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html#IFRS18_B141).

Changes to MPM calculations, additions/cessations or changes to reconciling-item tax methodology require explanation, reasons and restated comparatives unless impracticable; disclose impracticability. [IFRS 18.124–125](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html#IFRS18_124).

### Working-paper controls and delivery

For a **pure presentation** exercise, compare original and restated profit, continuing-operations profit, owners'/NCI allocations, OCI/comprehensive income, EPS, balance-sheet totals and total cash movement/closing cash. Show both numbers and investigate differences. A separate measurement election, error correction or other accounting change needs its own bridge; these controls do not prove that every possible transition change is presentation-only.

Keep one component ledger with original caption, note reference, both periods' amounts, final line/category, rule, function/nature and judgement. Build both periods' allocation matrices, prevent omissions/double counting, and tie rows/columns to original totals. Produce balanced **presentation** reclassification entries; do not post recognition/measurement journals merely to change captions.

Reconcile depreciation, amortisation, impairment, interest, lease/EOSB/provision movements, investments, grants, tax and inventory amounts to their underlying schedules. A residual is a corroboration, not proof of its cause: check omitted acquisitions/disposals, FX, OCI and other movements. Deliver primary statements, required notes, the comparative reconciliation, quantified judgements and a reviewer brief. Show mathematical checks and unresolved delivery holds; do not report a failed check as PASS. These replace the repeated Class A/B/C checklists as working-paper controls.

## Worked cases

These bounded recomputations retain original FY2026/FY2025 inputs; they do not certify the separate full-case financial statements. For the original early-adoption scenario, obtain evidence of FY2026 adoption and disclosure before using IFRS 18 presentation.

### Original FX components, FY2026 and FY2025

For the original industrial group without specified main activities, the supplied trade-balance and borrowing FX components sum to SAR -7,800 thousand for FY2026 and SAR +2,400 thousand for FY2025. Keep the underlying operating/financing split rather than classifying the net caption as one item. The component treatment follows [IFRS 18.B65–B66](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html#IFRS18_B65); figures are hypothetical original case inputs, not statutory amounts.

```oa-check
name: Original FX components FY2026 and FY2025, SAR thousands
inputs:
  trade_fx_2026: 1600
  borrowing_fx_2026: -9400
  trade_fx_2025: -1500
  borrowing_fx_2025: 3900
steps:
  - net_fx_2026: trade_fx_2026 + borrowing_fx_2026
  - net_fx_2025: trade_fx_2025 + borrowing_fx_2025
expected:
  net_fx_2026: -7800
  net_fx_2025: 2400
```

### Original operating-profit bridges: reconciliation hold

Using the original IAS 1 operating-profit inputs of SAR 360,400 thousand (FY2026) and SAR 291,100 thousand (FY2025), the supplied component adjustments give SAR 332,900 thousand and **SAR 264,300 thousand**, respectively. The separate full-case illustration's SAR 265,500 thousand FY2025 subtotal differs by SAR 1,200 thousand. Do not change the original input to SAR 292,300 thousand to make that subtotal fit. This arithmetic identifies a hold, not a corrected whole-case statement or a conclusion about Zakat treatment.

```oa-check
name: Original operating-profit inputs and adjustments, SAR thousands
inputs:
  ias1_op_2026: 360400
  ias1_op_2025: 291100
  rental_adjustment_2026: -14200
  commodity_adjustment_2026: -3600
  ppe_adjustment_2026: 6900
  intangible_adjustment_2026: 0
  trade_fx_adjustment_2026: 1600
  levy_adjustment_2026: -18200
  rental_adjustment_2025: -12800
  commodity_adjustment_2025: 1400
  ppe_adjustment_2025: 4200
  intangible_adjustment_2025: -2500
  trade_fx_adjustment_2025: -1500
  levy_adjustment_2025: -15600
  displayed_op_2025: 265500
steps:
  - supplied_adjustments_2026: rental_adjustment_2026 + commodity_adjustment_2026 + ppe_adjustment_2026 + intangible_adjustment_2026 + trade_fx_adjustment_2026 + levy_adjustment_2026
  - supplied_adjustments_2025: rental_adjustment_2025 + commodity_adjustment_2025 + ppe_adjustment_2025 + intangible_adjustment_2025 + trade_fx_adjustment_2025 + levy_adjustment_2025
  - computed_bridge_2026: ias1_op_2026 + supplied_adjustments_2026
  - computed_bridge_2025: ias1_op_2025 + supplied_adjustments_2025
  - unreconciled_difference_2025: displayed_op_2025 - computed_bridge_2025
expected:
  supplied_adjustments_2026: -27500
  supplied_adjustments_2025: -26800
  computed_bridge_2026: 332900
  computed_bridge_2025: 264300
  unreconciled_difference_2025: 1200
```

## When to refuse or refer

- **IFRS 19:** Eligibility, election and the reduced disclosure set are not established by this general IFRS 18 note template. Check this point with one of our partner accountants.
- **IAS 28 transition election:** Changing investment measurement from equity method to FVTPL under IFRS 18.C7, including eligibility, retrospective effects and separate statements, is outside this pure-presentation procedure. Check this point with one of our partner accountants.
- **Special contracts:** Insurance finance, issued investment contracts with participation features, hybrid liabilities/separated embedded derivatives and retained IAS 39 hedge accounting require their applicable special requirements; do not apply the simple liability table unconditionally. Check this point with one of our partner accountants.
- **Mixed disposal groups/subsidiary disposals:** Apply the required group-level analysis before using a category. Check this point with one of our partner accountants.
- **Zakat/local levies and supplier finance:** Establish local levy scope/deductibility and the derecognition facts and subsequent charges of a supplier-finance arrangement before classifying. The global Guide does not establish Saudi tax treatment or a general rule for all supplier fees. Check this point with one of our partner accountants.
- **US GAAP/SEC comparison:** The prior comparison topics—income-statement categories/subtotals, equity-method returns, pension/provision costs, non-GAAP measures, expense disaggregation, cash flow starting points and interest/dividends, goodwill and transition—need a separately sourced US GAAP analysis for dual reporters. Check this point with one of our partner accountants.
- **Original full cases:** [ifrs18-presentation-worked-examples](ifrs18-presentation-worked-examples.md) retains the original full restatement and MPM/nature-matrix cases. Their whole-case conclusions are **non-usable pending reconciliation**, including the FY2025 bridge, NCI effects and rental cash-flow analysis. This correction does not approve that sibling's outcomes or replace its original numeric inputs/years. Check this point with one of our partner accountants.

Original author attribution: **Talha Mehmood, ACA, FCCA**. This Guide supports working papers; obtain professional approval of the amended statements/disclosures before publication or filing.

## Sources

- [IASB, IFRS 18, issued 2026 text](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html). Read **2026-11-26**: paragraphs 1–6, 11, 19–24, 30–31, 37, 41–45, 47–85, 86–88, 96, 103–104, 117–125; B9, B25–B26, B29–B64, B65–B76, B80–B85, B113–B142 and C1–C7. Operative rules, exceptions and adjacent conditions were read; this is not a claim to have read every paragraph of the Standard.
- [IASB, IAS 7, issued 2026 text incorporating IFRS 18 amendments](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ias7.html). Read **2026-11-26**: paragraphs 6, 10, 12, 14, 16–20, 31–32, 33A, 34A–34D, 35 and 64. The amended requirements apply when IFRS 18 is applied, not automatically to every FY2026 reporter.

Not yet confirmed: IFRS 19-specific disclosures, IAS 28 election implementation, special contracts, mixed disposal groups, local levy/supplier-finance facts and US GAAP conclusions are referred above and excluded from usable conclusions here. The sibling's full-case outcomes remain on an explicit non-usable hold. Client-specific missing evidence also blocks delivery; it is not replaced by assumptions.
