---
name: nc-ordinary-irpp-reference
description: "Conditional New Caledonia selected 2025 ordinary one-part IRPP reference. Floors independently established net taxable income to the lower thousand francs and applies the progressive raw income tax scale. Use for New Caledonian IRPP, revenu imposable, quotient familial and lower-thousand rounding questions. Requires the universal and income tax workflow bases. Fictional annual resident examples preserve exact input and separate raw tax from later reductions. Complete applicable law, household parts, upstream deductions, actual input precision, exceptional income, credits, contributions, filing, settlement and professional acceptance remain held. Source chronology is unresolved. Guide presence and component checks do not establish comprehensive jurisdiction acceptance."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/nc-ordinary-irpp-reference"
  jurisdiction: "NC"
  tax_year: "2026"
  last_updated: "2026-11-14"
---

# New Caledonia: ordinary one-part IRPP reference v0.2

> **General reference only.** This source-cited Tier 2 conditional draft illustrates a selected ordinary raw income tax component. It does not complete an income tax engagement, final assessment, withholding or payment. Guide presence, source preparation and component checks do not establish comprehensive jurisdiction acceptance.

**Answer first.** New Caledonian personal income tax (IRPP) is worked out on net taxable income rounded **down to the lower thousand francs** (article 132), divided by the household's parts, with a progressive scale per part: nothing on the first **1.000.000 F**, then **4%**, **12%**, **25%** and **40%** (article 136 I). For one part (N = 1) the raw tax on the floored income B is 4% of B between 1.000.000 and 1.800.000 F, 12% between 1.800.000 and 3.000.000 F, 25% between 3.000.000 and 4.500.000 F and 40% above. Reductions such as the redistributive relief (article 136 II) come afterwards and are not computed here. Amounts are in francs Pacifique (XPF).

**Tax year 2026.** The code read on 14 November 2026 (Juridoc, updated 14 January 2026, citing an arrêté of 18 March 2026) gives this scale, last amended in 2017. It applies to 2025 income declared in 2026 and, unless the 2026 budget laws change it, to 2026 income declared in 2027. Ryan's cases are labelled "selected 2025"; the scale and floor give the same results for 2026.

## Scope and who this is for

Load workflow-base and income-tax-workflow-base in full. Preserve all 4 universal outputs and 18 checks, all 5 income tax outputs and 12 checks, all mandatory country slots and every shared refusal. Missing applicable law, facts, tools, outputs or qualified review prevents delivery of an actual financial result.

The selected 2025 illustrations stipulate one ordinary individual fiscally domiciled in New Caledonia throughout the annual period, a legally established assessment unit with exactly one part N = 1 and complete net taxable income C independently established after every applicable upstream adjustment. Articles 46-54, 128, 131-135 and related provisions require separate scope, unit, income and household determinations. C is not gross wages, receipts, net pay or revenu brut global. Establish all relevant deductions and abatements, including any Lp. 134 bis hosted-child abatement, before accepting C. A deduction or abatement may apply even when N remains one; one part does not establish that all upstream adjustments are nil.

A marital label and absence of children do not establish N = 1. Article 133 and operative Lp. 133 bis contain family and special additional-part branches, including invalidity, veteran and dependency conditions. The separate old article 133 bis is marked abrogated; that does not repeal Lp. 133 bis. Resolve the applicable person, dependant, timing and proof rules rather than inferring parts from a label. Extra-part benefit limits are separate from the raw scale and are not implemented here. No household change, death, part-year liability, arrival/departure, special residence or treaty branch is determined.

These examples exclude unresolved exceptional, deferred or unusual income and any special computation or separate-rate income. Articles 131 and 131 bis must be resolved before treating the ordinary scale as sufficient. The stage stops before every article 136 II reduction, later credit, contribution and settlement operation. It identifies raw G even where a later relief applies; it does not assume relief is nil. Positive G and zero G both leave final tax, filing, payment and refund held.

All amounts are francs Pacifique, as identified by the DSF calculation page. No currency conversion is established. Exact fractional C values are synthetic precision tests for the floor operation, not proof that an actual statutory input may have those decimal places. Establish lawful input precision separately and preserve exact evidence. No preliminary rounding, silent zero or coercion is permitted.

## Ask the client first

1. **Which income year**, and fiscal domicile in New Caledonia for the whole year (articles 46-54).
2. **The household and its parts**: marital status, dependants, and any special part (invalidity, veteran, dependency) under article 133 and Lp. 133 bis.
3. **Complete net taxable income** after every deduction and abatement, including any Lp. 134 bis hosted-child abatement (not gross salary or gross global income).
4. **Exceptional, deferred or separate-rate income** (articles 131 and 131 bis).
5. **Gross global income of the household**, for the separate article 136 II reductions.

## The method, step by step

### Rates, bands and thresholds

| Item | Amount or rule | Source |
|---|---|---|
| Rounding of taxable income | Rounded to the lower thousand francs before division by parts | [L1, article 132](https://juridoc.gouv.nc/juridoc/jdcodes.nsf/0/050372C3F3A0E7D14B257567007545A1/%24File/Code_des_impots_Nouvelle-Caledonie_ChG_14-01-2026.pdf) |
| Scale per part | Nil to 1.000.000 F; 4% to 1.800.000 F; 12% to 3.000.000 F; 25% to 4.500.000 F; 40% above (band table below) | [L1, article 136 I(1)](https://juridoc.gouv.nc/juridoc/jdcodes.nsf/0/050372C3F3A0E7D14B257567007545A1/%24File/Code_des_impots_Nouvelle-Caledonie_ChG_14-01-2026.pdf) |
| Cap on the quotient familial benefit | 300 000 francs per half-part, or half of that per quarter-part | [L1, article 136 I(2)](https://juridoc.gouv.nc/juridoc/jdcodes.nsf/0/050372C3F3A0E7D14B257567007545A1/%24File/Code_des_impots_Nouvelle-Caledonie_ChG_14-01-2026.pdf) |
| Redistributive reduction, gross global income limit (not computed here) | 6 100 000 francs for the first part (single, widowed, divorced); 12 200 000 francs for the first two parts (joint) | [L1, article 136 II(1)](https://juridoc.gouv.nc/juridoc/jdcodes.nsf/0/050372C3F3A0E7D14B257567007545A1/%24File/Code_des_impots_Nouvelle-Caledonie_ChG_14-01-2026.pdf) |
| Currency | Francs Pacifique; the DSF simulator covers 2025, 2024 and 2023 | [L3, DSF calculation page](https://dsf.gouv.nc/particuliers-impots-et-taxes/impot-sur-le-revenu/calculer-mon-impot-sur-le-revenu) |

### Intake and component mechanics

Reuse redacted records before grouped questions. Establish the obligation, income/basis year and complete applicable source chain; fiscal domicile and liability class; annual assessment unit and any change/death; exact parts and all special-part evidence; complete income categories, losses, deductions and abatements; exceptional/deferred/unusual income; C and its lawful precision; currency; all later reductions, credits and contributions; prepayments; procedures; reviewer and tools. Present the inferred profile and wait for confirmation. Profile confirmation does not establish law. Keep identifiers, bank details and signatures with the professional.

1. **Establish the input stage.** C is complete ordinary annual net taxable income after all upstream legal adjustments and before article 132's floor. Accept a non-negative finite exact base-10 value only after branch, unit and input formation are independently established. Do not substitute gross salary or gross global income, subtract tax from C or repeat an abatement already reflected in C. _(L1 articles 46, 128, 131, 132 and Lp. 134 bis)_
2. **Preserve exact input.** Retain C and its precision separately. For documentary fixtures, an ungrouped numeral with optional decimal point and digits specifies C. Negative, missing, malformed, ambiguous, non-finite, mixed-currency or unestablished-value/precision input requires reconciliation. This transport notation is a fixture rule, not statutory precision. Do not round first to whole francs, cents or the nearest thousand.
3. **Apply the income floor.** B = 1000 x floor(C / 1000), R = C - B. Thus B is the lower multiple of 1000, C = B + R and 0 <= R < 1000. Article 132 floors income before division by parts. For this independently established N = 1 branch, per-part income is B and multiplication by N leaves the raw scale unchanged. No other N is accepted by this component. _(L1 article 132)_
4. **Allocate marginal widths.** W1 = min(max(B - 1000000, 0), 800000); W2 = min(max(B - 1800000, 0), 1200000); W3 = min(max(B - 3000000, 0), 1500000); W4 = max(B - 4500000, 0). The first 1000000 of B has no scale charge. It is a scale band, not a deduction from C or tax credit. _(L1 article 136 I(1))_
5. **Compute raw G.** G = 0.04 x W1 + 0.12 x W2 + 0.25 x W3 + 0.40 x W4. Apply each rate only to its width. Do not apply the highest reached rate to all B. There is no invented maximum input or maximum raw tax. _(L1 article 136 I(1))_
6. **Retain the stage.** Record C, N, B, R, every marginal width and G with the established premises and held later stages. B and each W are multiples of 1000, so these rational rates produce mathematically integral G. This arithmetic property is not a general tax-rounding, collection or settlement rule. No final-tax rounding is inferred.

| Selected scale band, francs per part | Marginal rate | Cumulative raw G at upper boundary for N = 1 (derived) | Source |
|---|---:|---:|---|
| B up to 1000000 | 0% | 0 | [L1, article 136 I(1)](https://juridoc.gouv.nc/juridoc/jdcodes.nsf/0/050372C3F3A0E7D14B257567007545A1/%24File/Code_des_impots_Nouvelle-Caledonie_ChG_14-01-2026.pdf) |
| B above 1000000 through 1800000 | 4% | 32000 | same |
| B above 1800000 through 3000000 | 12% | 176000 | same |
| B above 3000000 through 4500000 | 25% | 551000 | same |
| B above 4500000 | 40% | No upper boundary | same |

The rate table is L1 article 136 I(1). Its cumulative values are exact derived checks for the declared one-part branch, not final liability figures.

## Worked cases

Two of Ryan's boundary checks, as CI recomputes them (one part, XPF).

**Case 1 (NCIR09), net taxable income 1,234,567.89.** Floored to B = 1,234,000. Only the 4% band is reached: 234,000 at 4% = 9,360 raw tax.

```oa-check
name: New Caledonia IRPP, one part, income 1234567.89 F (2026 scale)
inputs:
  income: 1234567.89
steps:
  - b: floor(income / 1000) * 1000
  - w1: min(max(b - 1000000, 0), 800000)
  - w2: min(max(b - 1800000, 0), 1200000)
  - w3: min(max(b - 3000000, 0), 1500000)
  - w4: max(b - 4500000, 0)
  - tax: w1 * 0.04 + w2 * 0.12 + w3 * 0.25 + w4 * 0.40
expected:
  b: 1234000
  tax: 9360
```

**Case 2 (NCIR21), a decision: marginal bands or the top rate on everything?** Income 4,501,000. The four widths are 800,000, 1,200,000, 1,500,000 and 1,000, charged 32,000 + 144,000 + 375,000 + 400 = 551,400. Applying 40% to all of B would wrongly give 1,800,400.

```oa-check
name: New Caledonia IRPP, one part, income 4501000 F (2026 scale)
inputs:
  income: 4501000
steps:
  - b: floor(income / 1000) * 1000
  - w1: min(max(b - 1000000, 0), 800000)
  - w2: min(max(b - 1800000, 0), 1200000)
  - w3: min(max(b - 3000000, 0), 1500000)
  - w4: max(b - 4500000, 0)
  - tax: w1 * 0.04 + w2 * 0.12 + w3 * 0.25 + w4 * 0.40
  - flat_wrong: b * 0.40
expected:
  tax: 551400
  flat_wrong: 1800400
```

### Ryan's fictional selected-2025 boundary checks

Every row stipulates the complete component premises above. Fractional inputs test the floor only; actual lawful precision and operative-year applicability remain held. All G values are raw francs before reductions, credits, contributions, prepayments and settlement.

| Case | Exact C | B | R | Raw G |
|---|---:|---:|---:|---:|
| NCIR01 | 0 | 0 | 0 | 0 |
| NCIR02 | 0.001 | 0 | 0.001 | 0 |
| NCIR03 | 999.999 | 0 | 999.999 | 0 |
| NCIR04 | 1000 | 1000 | 0 | 0 |
| NCIR05 | 999999.99 | 999000 | 999.99 | 0 |
| NCIR06 | 1000000 | 1000000 | 0 | 0 |
| NCIR07 | 1000999.99 | 1000000 | 999.99 | 0 |
| NCIR08 | 1001000 | 1001000 | 0 | 40 |
| NCIR09 | 1234567.89 | 1234000 | 567.89 | 9360 |
| NCIR10 | 1799999.99 | 1799000 | 999.99 | 31960 |
| NCIR11 | 1800000 | 1800000 | 0 | 32000 |
| NCIR12 | 1800999.99 | 1800000 | 999.99 | 32000 |
| NCIR13 | 1801000 | 1801000 | 0 | 32120 |
| NCIR14 | 2999999.999 | 2999000 | 999.999 | 175880 |
| NCIR15 | 3000000 | 3000000 | 0 | 176000 |
| NCIR16 | 3000999.99 | 3000000 | 999.99 | 176000 |
| NCIR17 | 3001000 | 3001000 | 0 | 176250 |
| NCIR18 | 4499999.99 | 4499000 | 999.99 | 550750 |
| NCIR19 | 4500000 | 4500000 | 0 | 551000 |
| NCIR20 | 4500999.99 | 4500000 | 999.99 | 551000 |
| NCIR21 | 4501000 | 4501000 | 0 | 551400 |
| NCIR22 | 6000000 | 6000000 | 0 | 1151000 |
| NCIR23 | 6080000 | 6080000 | 0 | 1183000 |
| NCIR24 | 6100000 | 6100000 | 0 | 1191000 |
| NCIR25 | 100000000 | 100000000 | 0 | 38751000 |

NCIR07 preserves C = 1000999.99, B = 1000000 and G = 0. Rounding C first to 1001000 would wrongly create G = 40. NCIR09 gives W1 = 234000 and the other widths zero, so G = 9360 and R = 567.89. NCIR14 remains below the next thousand and below the next rate band; it does not become C = 3000000 through preliminary rounding.

NCIR21 gives W1 = 800000, W2 = 1200000, W3 = 1500000 and W4 = 1000. Their charges are 32000, 144000, 375000 and 400, totalling G = 551400. Applying 40% to all B would wrongly give 1800400. NCIR22-NCIR24 preserve the raw scale across amounts that resemble separate redistributive-relief boundaries; those relief rules use gross global income, not C or B. Do not use these rows to decide relief eligibility. NCIR25 illustrates an uncapped large raw input without establishing special-income eligibility or final tax.

## When to refuse or refer

Every shared refusal remains mandatory. For actual work add these stops:

- **R-NC-IR-1:** 'The applicable New Caledonian law, requested period or branch conditions are unresolved. Stop the affected calculation and obtain authoritative period-specific evidence and qualified review.'
- **R-NC-IR-2:** 'The assessment unit, one-part entitlement or complete ordinary net taxable input is not independently established. Stop and reconcile household, income, deduction, abatement and special-income evidence.'
- **R-NC-IR-3:** 'Input value, currency, lawful precision or calculation stage is unresolved. Preserve established evidence and hold delivery without preliminary rounding, coercion or a silent default.'
- **R-NC-IR-4:** 'This raw component cannot complete actual income tax, withholding, filing or payment. Hold delivery until all later stages, required outputs, checks and professional sign-off are complete.'

| Held case | Required disposition |
|---|---|
| Header or editing date treated as a complete current-law or 2025 applicability certificate | R-NC-IR-1; reconcile the January header and March note and establish the requested-period chain. |
| Metropolitan French rates, allowances, quotient rules or precision imported | R-NC-IR-1; establish New Caledonian primary law. |
| Address or profile confirmation used to establish fiscal domicile or liability | R-NC-IR-1 and R-NC-IR-2; obtain the legal and factual basis. |
| 'Single with no children' used as proof of N = 1 | R-NC-IR-2; establish all ordinary and special part branches, including operative Lp. 133 bis. |
| N other than one, unknown N, shared care, special invalidity/veteran/dependency parts or quotient cap unresolved | R-NC-IR-2; no unreviewed multiplication or general multi-part engine. |
| Death, marriage, PACS, separation, household change, arrival/departure or short-period branch unresolved | R-NC-IR-1 and R-NC-IR-2; establish unit, period and applicable timing rules. |
| Gross wages, gross global income, net pay or an estimate substituted for C | R-NC-IR-2; reconcile complete ordinary net taxable income first. |
| Deduction, loss, expense or Lp. 134 bis hosted-child abatement unresolved or assumed nil from N = 1 | R-NC-IR-2; establish each upstream adjustment independently. |
| Exceptional, deferred, unusual or separate-rate income unresolved | R-NC-IR-1 and R-NC-IR-2; apply the correct branch before any ordinary-stage delivery. |
| Negative, missing, malformed, ambiguous, non-finite or mixed-currency input | R-NC-IR-2 or R-NC-IR-3; no dropping, absolute value, conversion or zero coercion. |
| Actual input precision unestablished or synthetic fractional fixtures treated as authority | R-NC-IR-3; establish the lawful precision separately. |
| C rounded early, rounded to nearest thousand or reduced by the first band twice | R-NC-IR-3; preserve C, B and R and apply the lower-thousand floor once. |
| Highest reached marginal rate applied to all B or rate fractions confused with percentages | R-NC-IR-3; retain all widths and exact charges. |
| G reduced using C/B at a gross-global relief threshold, or relief assumed nil because G is raw | R-NC-IR-3 and R-NC-IR-4; establish the separate article 136 II base, entitlement, limits and ordering. |
| G treated as final tax, general rounding authority, PAYE, instalment, refund or balance due | R-NC-IR-3 and R-NC-IR-4; no settlement or payroll conversion inferred. |
| G = 0 treated as no filing, no tax, no separate contribution or zero balance | R-NC-IR-4; establish each obligation and later stage independently. |
| Social, solidarity, health or other separate contribution inferred from G | R-NC-IR-4; establish each programme, base, rate and period separately. |
| Required output, tool, check, procedure or qualified reviewer absent | R-NC-IR-4; component success does not complete the workflow. |

These rows document intended behaviour. Documentary and one-off fixture checks do not establish a deployed calculation engine or a completed consuming-LLM engagement.

## Completion checklist

Retain the universal working paper, reviewer brief, action list and practitioner checklist and all 5 income tax outputs: transaction classification register, computation working paper, filing/payment calendar, reviewer brief and taxpayer action list. Preserve identifiable components wherever the universal base permits combination. This reference replaces none of them.

Add a proposition ledger: exact source/version/year and chronology discrepancy; period-specific law; liability/residence/assessment unit; parts and evidence; classified income, losses, deductions and abatements including Lp. 134 bis; C and its lawful precision; N/B/R/W1/W2/W3/W4/G; every later reduction/credit and its own base; separate contributions; prepayments; procedures; refusals; tools; outputs and reviewer disposition. Mark every unresolved field held.

Run all 18 universal and 12 income tax checks. Add exact lower-thousand and marginal-boundary checks, no preliminary rounding, C = B + R, 0 <= R < 1000, width reconstruction, exact rational-rate products, no flat highest-rate computation, no invented cap, independently established N = 1, complete upstream adjustment evidence, separate later-relief bases and held-delivery checks. Raw G does not reconcile the complete income tax ladder.

The 13 universal slots are addressed only within this conditional scope: scope, source/period limits, selected figures, primary library, position rules, refusals, no unsupported defaults, material issues, fictional examples, proposition ledger, redacted intake, additional checks and revision metadata. They remain incomplete for actual work; no slot is waived.

| Mandatory income tax slot | Selected reference and remaining hold |
|---|---|
| 1. Year, basis, unit and residence | Selected 2025 ordinary full-year one-part resident illustration; actual period, unit, domicile and complete law held. |
| 2. Income categories | Independently established complete ordinary C; full classification, grossing, aggregation and special-income branches held. |
| 3. Rates and effective dates | L1 article 136 I(1) raw progressive scale; requested-period amendment, commencement and transition chain held. |
| 4. Allowances, deductions and credits | First scale band and complete upstream-adjustment premise; actual abatements, additional parts, quotient cap and later relief/credits held. |
| 5. Expenses and capital | No expense, capital or investment deduction/relief determination. |
| 6. Loss relief | Classification, offset, ordering and carry rules held before C is accepted. |
| 7. Withholding and prepayments | PAYE, instalments, credits, remittance and settlement remain held. |
| 8. Social contributions | Social, solidarity, pension, health and other separate charges held. |
| 9. Filing mechanics | Forms, portal, entries, deadlines, payment, amendments, appeals and penalties held. |
| 10. Transaction patterns | One raw component; complete receipt, expense and bank-pattern library remains required. |
| 11. Refusals and defaults | Shared plus 4 topical stops and 18 held cases; no unsupported default or live runtime qualification. |
| 12. Currency/conversion/rounding | Exact fictional francs Pacifique and lower-thousand income floor; actual base precision, conversion and final-tax/settlement precision held. |
| 13. Full worked ladders | 25 boundary/precision/raw-scale cases; complete employee/self-employed/mixed ladders through balance due remain required and unproduced. |

Optional regimes, international matters, local obligations and integrations remain incomplete. No actual income tax, payroll or comprehensive New Caledonia acceptance follows.

### Revision and disclaimer

29 October 2026, v0.1: conditional selected-2025 ordinary one-part raw IRPP component with exact lower-thousand floor, all marginal boundaries, complete upstream-input and household premises, source chronology caveat and actual-work holds. Tier 2, pending_review and verified_by pending remain.

This document is general reference material and does not constitute tax, legal or financial advice. A qualified professional in the relevant jurisdiction must establish applicable law, verify facts and complete and sign off every required output before filing, paying or relying on a result.

## Sources

| Source | Read for | URL | Read on |
|---|---|---|---|
| L1: Juridoc, Code des impôts de la Nouvelle-Calédonie (update of 14/01/2026) | Read for article 132 (lower-thousand floor), article 136 I(1) (scale), 136 I(2) (quotient cap) and 136 II(1) (redistributive limits) | https://juridoc.gouv.nc/juridoc/jdcodes.nsf/0/050372C3F3A0E7D14B257567007545A1/%24File/Code_des_impots_Nouvelle-Caledonie_ChG_14-01-2026.pdf | 2026-11-14 |
| L2: DSF, notice for the 2025 income declaration | Read for additional parts, hosted-child abatement and quotient limits (2025 context); downloaded, not re-read in full | https://dsf.gouv.nc/sites/default/files/documents/Notice%20d%C3%A9claration%20de%20revenus%20normale%202025.pdf | 2026-10-29 (read by Ryan); downloaded 2026-11-14 |
| L3: DSF, calculating income tax | Read for the currency (francs Pacifique), the reference to article 136 I and the 2025, 2024 and 2023 simulators | https://dsf.gouv.nc/particuliers-impots-et-taxes/impot-sur-le-revenu/calculer-mon-impot-sur-le-revenu | 2026-11-14 |

### Ryan's notes on each source (kept)

| Source | Selected proposition and limit | Read on |
|---|---|---|
| [L1: Juridoc, Code des impôts de la Nouvelle-Calédonie](https://juridoc.gouv.nc/juridoc/jdcodes.nsf/0/050372C3F3A0E7D14B257567007545A1/%24File/Code_des_impots_Nouvelle-Caledonie_ChG_14-01-2026.pdf) | Complete official 647-page PDF retained. Selected articles 46-54 distinguish annual income, domicile and assessment unit; 128 and 131 address input formation and special income; 132 requires the lower-thousand income floor before division by parts; 133, Lp. 133 bis, Lp. 134, Lp. 134 bis and 135 require separate household/abatement/timing treatment; 136 I gives the progressive scale and separate quotient-benefit limitation. Article 136 II begins later reductions. Selected physical pages 181, 192-194 and 196-197 were compared with originals. Complete retention is not review of every amendment or branch. | 2026-10-29 (read by Ryan) |
| [L2: DSF, notice for déclaration des revenus 2025](https://dsf.gouv.nc/sites/default/files/documents/Notice%20d%C3%A9claration%20de%20revenus%20normale%202025.pdf) | Complete official 6-page PDF retained. Original page 2 corroborates additional-part branches, family changes, hosted-child abatement, quotient limits and redistributive relief. This selected 2025 administrative context does not establish the complete law or all form procedures. | 2026-10-29 (read by Ryan) |
| [L3: DSF, calculating income tax](https://dsf.gouv.nc/particuliers-impots-et-taxes/impot-sur-le-revenu/calculer-mon-impot-sur-le-revenu) | Complete loaded public text retained on 29 October 2026. Identifies francs Pacifique, article 136 I and simulations for 2025, 2024 and 2023. The calculator is anonymous and is not a declaration. No completed simulator run or authority-endorsed result is claimed. | 2026-10-29 (read by Ryan) |

L1's filename and repeated header say 'Mise à jour le 14/01/2026', but physical page 181 cites arrêté AG-2026-DSF-0179 of 18 March 2026. Both were observed in the original. Preserve this chronology inconsistency; neither the filename nor header is accepted as an exhaustive verified law-as-at date. L2 supports a selected 2025 context, not reconciliation of every amendment, commencement or transitional provision. Actual 2025 and current-period applicability remain held until an authoritative period-specific source chain is established. An editing date does not establish operative law.

L1 article 132's editorial note directs its dependant reference to Lp. 134. Preserve the operative cross-references, including Lp. 133 bis and the upstream Lp. 134 bis abatement. Missing evidence is not evidence of no rule. No rate, exemption, deduction, deadline, rounding or filing default is imported from metropolitan France or another territory.

Not yet confirmed: any 2026 budget law changing the article 136 scale for 2026 income (no 2026 notice or simulator was published on the DSF site on 2026-11-14; the 2025 notice and the code as updated in 2026 are used, labelled for the 2025-2026 filing cycle); the code's chronology (header 14 January 2026, but it cites an arrêté of 18 March 2026); household parts other than one, the quotient cap and the article 136 II reductions (not computed); lawful input precision; filing and payment dates (not covered).

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-14. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `nc-ordinary-irpp-reference` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/nc-ordinary-irpp-reference. If neither is available, confirm every figure against the official source pages cited above before relying on it.
