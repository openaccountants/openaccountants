---
name: nu-individual-return
description: "Compute a Nunavut individual's territorial income tax estimate for calendar 2026 from the federal T1 workpaper. Covers resident and non-resident scope, current territorial bands and basic personal amount, credit and multi-jurisdiction handoffs, separate refundable Nunavut credits, northern-resident and Inuit beneficiary questions, filing and completion evidence. Actual 2025 annual forms remain expressly identified as the 2025-2026 filing cycle rather than final 2026 annual fields. Use nu-tax-credits for optional credit eligibility and figures."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/nu-individual-return"
  jurisdiction: "CA-NU"
  tax_year: "2026"
  last_updated: "2026-11-14"
---

# Nunavut individual return v 2.0

## Scope

Use this method for an individual's Nunavut territorial T1 calculation, including an employee or self-employed individual. The normal resident case uses Nunavut residence at year-end. The actual 2025 instructions also cover a non-resident of Canada with employment income only in Nunavut or a business permanent establishment only there; multiple-jurisdiction business income uses T2203. Do not reject every non-resident automatically or prorate an ordinary interprovincial move by days without applying its actual residence/allocation rule. Corporations and trusts require their own returns. [CRA annual scope](https://www.canada.ca/en/revenue-agency/services/forms-publications/tax-packages-years/general-income-tax-benefit-package/nunavut/5014-pc.html).

| Quick reference | Entry |
|---|---|
| Place/currency | Nunavut, Canada; CAD |
| Current estimate | Calendar 2026 ordinary territorial bands and basic personal amount |
| Actual annual-form edition | 2025 NU428 and NU479, for the 2025-2026 filing cycle |
| Primary legislation | Income Tax Act, R.S.N.W.T.1988,c.I-1 as continued/amended for Nunavut, not the Northwest Territories' separately amended law |
| Administrator | CRA administers the territorial T1; the Government of Nunavut sets territorial rules |
| Main form jobs | Federal T1, NU428 territorial tax, NU479 separate refundable credits; applicable territorial tuition/spouse and federal special-tax schedules |
| Contributor | Open Accountants Community |

The published consolidation is dated 2020 and its official landing page lists later amendments. Read the applicable amendment and commencement for a changed provision; do not describe that PDF as fully consolidated 2026 law. The territorial government's 2026 rate sheet and CRA's 2026 payroll table agree on current bands. The payroll table is evidence of 2026 amounts, not a final annual NU428. [Act catalogue](https://www.nunavutlegislation.ca/en/consolidated-law/income-tax-act-consolidation), [2026 rate sheet](https://www.gov.nu.ca/sites/default/files/documents/2026-01/January_2026_Nunavut_Tax_Rate_Sheet_-_EN.pdf), [CRA 2026 table](https://www.canada.ca/en/revenue-agency/services/forms-publications/payroll/t4032-payroll-deductions-tables/t4032nu-jan/t4032nu-january-general-information.html).

## Ask the client first

1. What year, country/territory of residence at year-end, arrival/departure dates, and business permanent-establishment allocations apply?
2. What are completed federal taxable income at line 26000 and net income at line 23600, with the underlying business, gains, northern and other deduction workpapers?
3. What spouse/dependant incomes, ages, custody, disability and support facts affect ordinary or refundable claims? Obtain the other claimant's use and actual benefit records.
4. What CPP/EI credit bases, tuition/carryforwards/transfers, medical expenses, donations, pension, dividend designations and foreign-tax records support territorial credits?
5. Do T691 AMT, T1206 split income, T2203 multiple jurisdictions, bankruptcy, death or separate returns apply? Obtain the actual schedules before finalising.
6. What northern residence/address/dwelling facts, Inuit Agreement or Indian Act issue, volunteer-service evidence, political receipts, mining/royalty or benefit facts need a specific determination?

## The method, step by step

### Rates, bands and thresholds

| Item | 2026 amount and conditions | Official source |
|---|---|---|
| First band | First CAD 55,801 at 4% | [Government 2026 rate sheet](https://www.gov.nu.ca/sites/default/files/documents/2026-01/January_2026_Nunavut_Tax_Rate_Sheet_-_EN.pdf) |
| Second band | Portion over CAD 55,801 through CAD 111,602 at 7% | [Government 2026 rate sheet](https://www.gov.nu.ca/sites/default/files/documents/2026-01/January_2026_Nunavut_Tax_Rate_Sheet_-_EN.pdf) |
| Third band | Portion over CAD 111,602 through CAD 181,439 at 9% | [Government 2026 rate sheet](https://www.gov.nu.ca/sites/default/files/documents/2026-01/January_2026_Nunavut_Tax_Rate_Sheet_-_EN.pdf) |
| Top band | Portion over CAD 181,439 at 11.5% | [Government 2026 rate sheet](https://www.gov.nu.ca/sites/default/files/documents/2026-01/January_2026_Nunavut_Tax_Rate_Sheet_-_EN.pdf) |
| Basic personal amount | CAD 19,659 ordinary full-year base; its 4% tax value is computed CAD 786.36, before eligibility/proration restrictions | [CRA 2026 Nunavut table](https://www.canada.ca/en/revenue-agency/services/forms-publications/payroll/t4032-payroll-deductions-tables/t4032nu-jan/t4032nu-january-general-information.html) |

The top percentage applies only to income above its boundary. Do not apply a single top rate to all taxable income. Keep the continuous boundaries; an amount between the printed whole-dollar endpoints is not untaxed. The examples use marginal-band portions, not the whole-dollar payroll constants to calculate an annual return. Territorial ordinary tax is additional to the separately calculated federal tax.

### Reconcile federal income and determine the territorial return

1. Complete the federal T1 workpaper and reconcile line 26000 taxable income before NU428 Part A. A northern-residents deduction reduces the federal taxable-income input when valid; it is not a second deduction from territorial tax. Transaction classification belongs in `ca-fed-t2125`, not a bank-name rule in this skill. [Actual 2025 NU428](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5014-c/5014-c-fill-25e.pdf).
2. Establish the actual province/territory selection and resident/non-resident route. A business permanent establishment outside Nunavut can require T2203. Part-year Canadian residence can restrict specified territorial credit amounts in the same manner as corresponding federal amounts; it does not establish a simple days-times-final-tax shortcut. [CRA scope and newcomer/emigrant instructions](https://www.canada.ca/en/revenue-agency/services/forms-publications/tax-packages-years/general-income-tax-benefit-package/nunavut/5014-pc.html).
3. Apply the current band's rate only to its slice. With taxable income TI, gross ordinary tax is 4% × min(TI,55801) +7% × max(0,min(TI,111602)-55801) +9% × max(0,min(TI,181439)-111602) +11.5% × max(0,TI-181439). [Government 2026 table](https://www.gov.nu.ca/sites/default/files/documents/2026-01/January_2026_Nunavut_Tax_Rate_Sheet_-_EN.pdf).

### Compute non-refundable credits and special tax separately

4. Build the permitted ordinary credit bases from actual records. The 2025 NU428 includes personal, age, spouse/eligible-dependant, infirm-dependant, young-child, CPP/QPP, EI, pension, caregiver, disability, student-loan, tuition/education/textbook and designated-transfer amounts. Use the territorial amount and calculation, not an assumed federal equivalent. The form also calculates donations separately. The fixed basic personal amount alone is not a complete client's credit calculation. [Actual 2025 NU428 PartsA-B](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5014-c/5014-c-fill-25e.pdf).
5. Confirm own-use, transfer and claimant overlap. Do not transfer an entire gross tuition/disability/spouse entitlement without the relevant territorial schedule. Newcomer/emigrant reductions, support and shared dependants require their actual facts. `nu-tax-credits` owns the optional-credit figures and current confirmation gaps; load it rather than copy a second conflicting table here. [CRA annual credit instructions](https://www.canada.ca/en/revenue-agency/services/forms-publications/tax-packages-years/general-income-tax-benefit-package/nunavut/5014-pc.html).
6. Complete the actual NU428 Part C sequence, including split income, dividend credit, minimum-tax carryover/additional minimum tax, foreign credit and volunteer credit where applicable. T691, T1206 and T2036 require their actual underlying calculations. Do not subtract every special credit from a base and multiply it by the lowest rate, or invent a final 2026 line number. This method does not contain a complete federal AMT or TOSI engine. [CRA Part C instructions](https://www.canada.ca/en/revenue-agency/services/forms-publications/tax-packages-years/general-income-tax-benefit-package/nunavut/5014-pc.html), [Actual 2025 NU428](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5014-c/5014-c-fill-25e.pdf).

### Keep refundable credits separate

7. Complete NU479 separately from territorial tax. Its cost-of-living credit is **refundable**, calculated from adjusted net income, not taxable income times the lowest territorial rate. The older first 12000-times 4% and supplementary phase-out description is wrong. The actual 2025 form uses a percentage of adjusted net income with a cap and a distinct single-parent supplement; `nu-tax-credits` owns the figures and conditions. A high-income resident does not automatically lose the basic credit, and a resident with no territorial tax is not automatically ineligible. [Actual 2025 NU479](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5014-tc/5014-tc-25e.pdf), [Act s.4.1](https://www.nunavutlegislation.ca/en/file-download/download/public/7081).
8. On the actual 2025 form, cost-of-living adjusted net income begins with line 23600, reduces the specified lines 24400/25000 and treaty-exempt foreign income, with floors. A business with an outside-territory permanent establishment instead needs the allocated net income described by CRA. Political credit has an additional limitation after cost-of-living credit; it is not automatically refundable in full merely because it appears on NU479. [Actual 2025 NU479](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5014-tc/5014-tc-25e.pdf), [CRA NU479 allocation instruction](https://www.canada.ca/en/revenue-agency/services/forms-publications/tax-packages-years/general-income-tax-benefit-package/nunavut/5014-pc.html).
9. Keep NU428 tax on the provincial/territorial-tax route and NU479 on the refundable-credit route. Their difference can illustrate these two provincial components, but is not a final T1 refund before federal tax, instalments, withholding and other credits. Nunavut child benefit is a separate monthly assessment/payment based on benefit eligibility and return information, not an NU428 line. [Actual 2025 forms](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5014-c/5014-c-fill-25e.pdf), [NU479](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5014-tc/5014-tc-25e.pdf), [CRA child-benefit instructions](https://www.canada.ca/en/revenue-agency/services/forms-publications/tax-packages-years/general-income-tax-benefit-package/nunavut/5014-pc.html).

## Boundary and exception table

| Situation, including original refusal/edge-case code | Correct action |
|---|---|
|R-NU-1, residence/year unknown or not the ordinary resident case | Confirm actual residence and any Nunavut-source non-resident or multi-jurisdiction route; do not apply the resident estimate indiscriminately |
|R-NU-2, corporation/trust | Route to the proper return; individual employment as well as self-employment is within this method |
|R-NU-3, part-year residence | Establish Canadian arrival/departure versus an interprovincial move; use actual credit restrictions/allocation rather than days-times-tax |
|R-NU-4, Indian Act or Nunavut Agreement issue | Obtain the actual taxpayer, income source and controlling provision; beneficiary/status labels alone do not prove exemption or full taxability |
|EC-NU-1, cost-of-living supplement | Apply the actual NU479 and single-parent/adjusted-income conditions; never default to a maximum or invent a phase-out |
|EC-NU-2, northern deductions | Obtain exact prescribed address/zone, qualifying residency and dwelling facts and the federal workpaper before changing line 26000 |
|EC-NU-3, Agreement distributions | Refer the actual trust/distribution/recipient issue to a specialist; do not infer a blanket exemption from an organisation's name |
|EC-NU-4, mining/resource royalties | Reconcile actual business, resource and Agreement workpapers; do not assume every royalty is ordinary T2125 sales |
|Unknown annual bracket year | Obtain the year, do not use a 2025 fallback for a 2026 question |
|Child benefit, volunteer or political claim | Load `nu-tax-credits`, obtain the actual eligibility evidence and distinguish benefit payment, direct credit and ordinary credit base |

The old claim that an Inuit beneficiary necessarily has a particular Indian Act/reserve outcome is not certified here. The northern-residents deduction also requires more than a general claim that the territory is northern: obtain the prescribed-zone and continuous-residence evidence and the actual T2222. No unsupported claim of a full-year deduction follows from a year-end address. These investigation jobs are preserved rather than converted into an automatic exemption or refusal.

## Worked cases

These preserve the original low-, mid- and high-income scenarios. The 2026 numbers below show ordinary territorial tax using **only** the full basic personal credit, no other eligible credit or special tax. They are deliberately not final returns. A client's CPP/EI or other credit base is not silently assumed zero as a factual conclusion; the example stipulates no other claim.

### Case 1: low income, current estimate and actual prior filing-cycle correction

A full-year resident has 2026 taxable income 22000. Gross tax 880 less the basic credit 786.36 gives ordinary territorial tax 93.64 before optional/special/refundable amounts. For the actual 2025 filing cycle at the same taxable and adjusted net income, the old source's ordinary tax 109.04 is correct, but its 480 cost-of-living amount is not: the actual 2025 NU479 gives 440, leaving the difference between those two territorial components at minus 330.96, not minus 370.96. Keep the actual 2025 credit edition separate from the 2026 estimate. [2026 rate sheet](https://www.gov.nu.ca/sites/default/files/documents/2026-01/January_2026_Nunavut_Tax_Rate_Sheet_-_EN.pdf), [2026 basic amount](https://www.canada.ca/en/revenue-agency/services/forms-publications/payroll/t4032-payroll-deductions-tables/t4032nu-jan/t4032nu-january-general-information.html), [2025 NU428](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5014-c/5014-c-fill-25e.pdf), [2025 NU479](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5014-tc/5014-tc-25e.pdf).

```oa-check
name: Nunavut low-income 2026 estimate and 2025 credit correction
inputs:
  income: 22000
  basic_2026: 19659
  basic_2025: 19274
steps:
  - gross_tax: income * 0.04
  - personal_credit_2026: basic_2026 * 0.04
  - ordinary_tax_2026: max(0, gross_tax - personal_credit_2026)
  - ordinary_tax_2025: max(0, gross_tax - basic_2025 * 0.04)
  - cost_of_living_2025: min(1500, income * 0.02)
  - component_difference_2025: ordinary_tax_2025 - cost_of_living_2025
expected:
  gross_tax: 880
  personal_credit_2026: 786.36
  ordinary_tax_2026: 93.64
  ordinary_tax_2025: 109.04
  cost_of_living_2025: 440
  component_difference_2025: -330.96
```

### Case 2: mid-range income is not a guessed final return

At 2026 taxable income 85000, gross tax 4275.97 less 786.36 gives 3489.61 before other/special/refundable amounts. The previous version's approximate final 2800 was unsupported. At actual 2025 taxable and adjusted net income 85000, gross 4308.79 less 770.96 gives 3537.83, and the 2025 basic cost-of-living amount reaches 1500 rather than a guessed partial supplement. With no qualifying single-parent supplement or other claim, the difference of these two 2025 territorial components is 2037.83. [2026 rates](https://www.gov.nu.ca/sites/default/files/documents/2026-01/January_2026_Nunavut_Tax_Rate_Sheet_-_EN.pdf), [2026 personal amount](https://www.canada.ca/en/revenue-agency/services/forms-publications/payroll/t4032-payroll-deductions-tables/t4032nu-jan/t4032nu-january-general-information.html), [actual 2025 NU479](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5014-tc/5014-tc-25e.pdf).

```oa-check
name: Nunavut mid-range 2026 bands and prior-cycle credit
inputs:
  income: 85000
steps:
  - gross_2026: 55801 * 0.04 + (income - 55801) * 0.07
  - ordinary_2026: gross_2026 - 19659 * 0.04
  - gross_2025: 54707 * 0.04 + (income - 54707) * 0.07
  - ordinary_2025: gross_2025 - 19274 * 0.04
  - credit_2025: min(1500, income * 0.02)
  - components_2025: ordinary_2025 - credit_2025
expected:
  gross_2026: 4275.97
  ordinary_2026: 3489.61
  gross_2025: 4308.79
  ordinary_2025: 3537.83
  credit_2025: 1500
  components_2025: 2037.83
```

### Case 3: high income does not establish a cost-of-living phase-out

At 2026 taxable income 300000, gross ordinary tax rounds to 26057.96 and the basic-only ordinary result is 25271.60. The actual 2025 gross 26223.51 and basic-only 25452.55 are retained as dated calculations. With 2025 adjusted net income 300000 and otherwise valid residence, the basic cost-of-living credit does not phase out; use the actual 2025 form's cap in the separate credit workpaper, not the old “fully phased out” assumption. [Current 2026 rates](https://www.gov.nu.ca/sites/default/files/documents/2026-01/January_2026_Nunavut_Tax_Rate_Sheet_-_EN.pdf), [2026 basic amount](https://www.canada.ca/en/revenue-agency/services/forms-publications/payroll/t4032-payroll-deductions-tables/t4032nu-jan/t4032nu-january-general-information.html), [actual 2025 forms](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5014-c/5014-c-fill-25e.pdf), [NU479](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5014-tc/5014-tc-25e.pdf).

```oa-check
name: Nunavut high-income 2026 marginal portions
inputs:
  income: 300000
steps:
  - band1: 55801 * 0.04
  - band2: (111602 - 55801) * 0.07
  - band3: (181439 - 111602) * 0.09
  - band4: (income - 181439) * 0.115
  - gross: round(band1 + band2 + band3 + band4, 2)
  - ordinary: gross - 19659 * 0.04
expected:
  band1: 2232.04
  band2: 3906.07
  band3: 6285.33
  band4: 13634.515
  gross: 26057.96
  ordinary: 25271.60
```

## When to refuse or refer

- Do not finalise tax with an unknown year/residence, unreconciled federal input or unsupported material credit. State exactly what is missing while completing supported ordinary calculations.
- Refer the actual non-resident/treaty, multiple-permanent-establishment, bankruptcy/death, AMT/TOSI, trust, mining/royalty or Agreement workpaper where required. An explicit client fact is not replaced by a conservative tax guess.
- No automatic full basic/refundable/benefit entitlement, no outdated bracket fallback, and no definitive refund from a territorial-only estimate.

## Filing and payment

For calendar 2026 the ordinary individual filing/payment date is 30 April 2027; the qualifying self-employed filing date is 15 June 2027 without extending payment, subject to the actual statutory exceptions. Use `ca-fed-t1-return` and `ca-return-assembly` for the full federal submission and `ca-fed-instalments` for instalment/payment rules. The CRA's factsheet explicitly distinguishes the self-employed filing date and payment date. [CRA 2027 deadlines](https://www.canada.ca/en/services/taxes/resources-for-small-and-medium-businesses/2026-tax-deadlines-canadian-businesses-self-employed-individuals.html).

Use the correct year's CRA-certified NETFILE software or an authorised EFILE preparer, or the required paper return. MyAccount provides account/assessment access; it is not an interchangeable return-preparation form. Complete federal steps 1-5, territorial tax and supporting schedules, then separate refundable credits. In the actual 2025 forms, NU428 goes to T1 line 42800 and NU479 to line 47900. Do not describe these as final 2026 fields before that edition is confirmed. [CRA annual instructions](https://www.canada.ca/en/revenue-agency/services/forms-publications/tax-packages-years/general-income-tax-benefit-package/nunavut/5014-pc.html), [NU428](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5014-c/5014-c-fill-25e.pdf), [NU479](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5014-tc/5014-tc-25e.pdf).

Retain the prepared return and review workpaper, authorised submission acknowledgement/acceptance, notice of assessment and actual payment reconciliation. Preparing a file is not an accepted filing and generating a payment instruction is not payment. This method does not sign in, transmit, register or pay for the taxpayer.

## Completion checklist

- Territory/year and resident/non-resident/multi-jurisdiction route established.
- Federal line 26000 reconciled after supported northern/business/other deductions.
- Current 2026 band boundaries and basic personal amount applied without a whole-income top-rate shortcut.
- Ordinary and optional credit bases, claimant/transfer limitations and special taxes documented.
- NU479 adjusted income distinguished from taxable income; refundable cost-of-living amount not capped by positive tax.
- Political limitation and any single-parent supplement separately checked; monthly child benefit not treated as an NU428 credit.
- All original northern, Agreement, resource/royalty and part-year investigation jobs retained or explicitly unresolved.
- Actual 2025 form references clearly dated; final 2026 fields not invented.
- Overall federal/T1 settlement kept separate from these territorial components and accepted-filing/payment evidence retained.

## Sources

| Source and actual read scope | Official URL | Read on |
|---|---|---|
| Read for the full personal-income table in the one-page 2026 Nunavut rate sheet; unrelated fuel/property tables do not establish this method's credits |https://www.gov.nu.ca/sites/default/files/documents/2026-01/January_2026_Nunavut_Tax_Rate_Sheet_-_EN.pdf| 2026-11-14|
| Read for 2026 territorial bands, basic personal amount and indexing; payroll-purpose limitation retained |https://www.canada.ca/en/revenue-agency/services/forms-publications/payroll/t4032-payroll-deductions-tables/t4032nu-jan/t4032nu-january-general-information.html| 2026-11-14|
| Read for actual 2025 NU428 scope, newcomer/emigrant restrictions, Part C, volunteer and NU479/child-benefit handoffs; not a 2026 annual form |https://www.canada.ca/en/revenue-agency/services/forms-publications/tax-packages-years/general-income-tax-benefit-package/nunavut/5014-pc.html| 2026-11-14|
| Read for the actual 2025 NU428 tax bands, personal amount, ordinary-credit categories and territorial-tax handoff |https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5014-c/5014-c-fill-25e.pdf| 2026-11-14|
| Read for both actual 2025 NU479 pages, adjusted income, basic/single-parent/political computation and refundable-credit handoff |https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5014-tc/5014-tc-25e.pdf| 2026-11-14|
| Read for the 2020 consolidation header, ss.2.11-2.13 and 4.1/5/6.1; not represented as a complete 2026 consolidation |https://www.nunavutlegislation.ca/en/file-download/download/public/7081| 2026-11-14|
| Read for the explicit notice of later amendments to the older consolidation; not legal verification of every later provision |https://www.nunavutlegislation.ca/en/consolidated-law/income-tax-act-consolidation| 2026-11-14|
| Read for the 2027 filing/payment dates applicable to calendar 2026; the page URL's 2026 label is not treated as its return year |https://www.canada.ca/en/services/taxes/resources-for-small-and-medium-businesses/2026-tax-deadlines-canadian-businesses-self-employed-individuals.html| 2026-11-14|

Not yet confirmed: final 2026 annual NU428, NU479, tuition/spouse and federal special-tax fields/rounding; exact 2026 optional-credit and benefit values through nu-tax-credits; the client's prescribed northern address and complete 2026 T2222 eligibility/amount; any specific Indian Act/Nunavut Agreement, trust, mining/resource or multi-jurisdiction result; the complete current amendment chain for special credits. The cited official 2025 annual cycle is the latest annual form read, not a claim that all 2026 credits were published.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified Canadian CPA familiar with Nunavut territorial tax before filing.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-14. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `nu-individual-return` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/nu-individual-return. If neither is available, confirm every figure against the official source pages cited above before relying on it.
