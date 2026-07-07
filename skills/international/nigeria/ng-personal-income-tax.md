---
name: ng-personal-income-tax
description: Use this skill whenever asked about Nigerian Personal Income Tax (PIT) for individuals and sole traders / self-employed professionals filing an annual self-assessment return. Trigger on phrases like "Nigeria PIT", "Personal Income Tax Nigeria", "annual return Nigeria", "self-employed Nigeria tax", "self-assessment Nigeria", "PITA self-employed", "NTA 2025 individuals", "Nigeria Tax Act 2025 individuals", "consolidated relief allowance Nigeria", "CRA Nigeria", "minimum tax Nigeria", "state IRS filing", "SIRS annual return", "FIRS individual return FCT", "income tax Lagos", "income tax Abuja", or "Nigerian sole trader tax return". Covers tax year 2025 under PITA (Cap P8 LFN 2004 as amended through Finance Act 2023) plus the transitional treatment of the Nigeria Tax Act 2025 (effective 1 January 2026) for forward planning, including progressive brackets (7-24%), Consolidated Relief Allowance, minimum tax floor, capital allowances under the Fifth Schedule, WHT credits, life-insurance / pension / NHF / NHIS reliefs, and annual self-assessment filing to the State Internal Revenue Service (SIRS) — with FIRS jurisdiction reserved for FCT residents, members of the armed forces and police, foreign-service officers, and non-residents earning Nigeria-source income. Out of scope — employer-side payroll PAYE mechanics, PAYE return preparation, monthly PAYE remittance and statutory deductions (see ng-paye); corporate income tax / companies (CIT) and dividend WHT (see ng-cit); petroleum profits tax; partial-year residency and treaty tie-breaker analysis. ALWAYS read this skill before touching any Nigerian PIT work for individuals.
jurisdiction: NG
domain: international
tax_year: 2025
tier: 2
last_updated: 2026-07-06
---

# ng-personal-income-tax

## Nigeria — Personal Income Tax (PIT) — Skill v1.0

Nigeria — Personal Income Tax (PIT) — Skill v1.0

## > Relationship to ng-income-tax.md.

**Relationship to `ng-income-tax.md`.** A prior skill `ng-income-tax.md` (v2.0) existed in this package covering the same self-employed PIT territory with a strong bookkeeping / bank-statement bias. This new skill is the canonical "Personal Income Tax for individuals and sole traders" reference and should be treated as the primary source going forward. The older `ng-income-tax.md` retains useful Nigerian bank-statement reading guidance and a transaction pattern library, which remain valid as a bookkeeping companion. Where the two skills overlap (CRA computation, progressive brackets, minimum tax, capital allowances, filing authority), this skill controls. Recommendation: retire `ng-income-tax.md` once the bank-statement pattern library has been re-homed into a separate `ng-bookkeeping.md` skill; until then, treat `ng-income-tax.md` as deprecated for tax-rule purposes and load it only for its bank-narration patterns.

## Verified rates & thresholds (accountant-reviewed)

> Reviewed against the cited tax authorities by **Omolola Fasasi** on 2026-06-21.
> Items flagged for further clarification are tracked separately and excluded here.
> This block is generated from verified `skill_facts` — edit the facts, not the prose.

### ng-personal-income-tax

- **NGN 0 - 800,000** — 0  _(NIGERIAN TAX ACT 2025)_
- **NGN 800,001 - 3,000,000** — 0.15  _(NIGERIAN TAX ACT 2025)_
- **NGN 3,000,001 - 12,000,000** — 0.18  _(NIGERIAN TAX ACT 2025)_
- **NGN 12,000,001 - 25,000,000** — 0.21  _(NIGERIAN TAX ACT 2025)_
- **NGN 25,000,00I - 50,000,000** — 0.23  _(PITA s 37, Third Schedule)_
- **Above NGN 50,000,000** — 0.25  _(NIGERIAN TAX ACT 2025)_
- **Consolidated Relief Allowance (CRA)** — #800k Tax- free threshold + rent relief (20% of rent, max #500k)  _(NIGERIAN TAX ACT 2025)_
- **Minimum tax (where computed tax < minimum)** — ABOLISHED UNDER NIGERIAN TAX 2025  _(NIGERIAN TAX ACT 2025)_
- **Employee pension contribution (PRA 2014)** — 8% of monthly emolument  _(NIGERIAN TAX ACT 2025)_
- **Employer pension contribution (PRA 2014)** — 10% of monthly emolument  _(NIGERIAN TAX ACT 2025)_
- **National Housing Fund (NHF) contribution** — 2.5% of basic monthly salary  _(NIGERIAN TAX ACT 2025)_
- **Annual PIT return filing deadline** — 31 March of the following year  _(NIGERIAN TAX ACT 2025)_
- **PAYE remittance to state tax authority** — 10th day of following month  _(NIGERIAN TAX ACT 2025)_
- **Gratuity taxability** — Gratuity is now fully taxable (unless within #50M exemption threshold  _(NIGERIAN TAX ACT 2025)_

## Section 1 — Quick Reference

**Section 1 — Quick Reference**

| Field | Value |
| --- | --- |
| Country | Federal Republic of Nigeria |
| Tax | Personal Income Tax (PIT) on individuals and sole traders |
| Currency | NGN (Nigerian Naira) only — no kobo on the return |
| Tax year | Calendar year (1 January – 31 December) |
| Primary legislation (FY 2025) | Personal Income Tax Act, Cap P8 LFN 2004, as amended by Finance Acts 2019, 2020, 2021, 2023 |
| Successor legislation | **Nigeria Tax Act 2025 (NTA 2025)** — assented June 2025; effective **1 January 2026**. **FY 2025 is the final year under PITA**. NTA 2025 figures herein are flagged "TBC under NTA 2025 implementing regulations" pending final commencement. |
| Filing authority — residents outside FCT | State Internal Revenue Service (SIRS) of the state of residence (Lagos LIRS, Rivers RIRS, Kano KIRS, etc.) |
| Filing authority — FCT residents | Federal Inland Revenue Service (FIRS) |
| Filing authority — armed forces, police, foreign-service officers, non-residents with Nigeria-source income | FIRS (PITA s 2(1)(b)) |
| Filing authority — residence test | Place where the individual has a "place of residence" available for use on the relevant day, determined as at the **1 January** of the tax year (PITA s 3 / First Schedule) |
| Annual SPT deadline | **31 March** of the following year (PITA s 41) |
| Payment deadline | Self-assessed PIT paid in instalments OR full balance by 31 March; tax due **must** be paid on or before filing (PITA s 41(3)) |
| TIN | Tax Identification Number issued by FIRS / JTB (Joint Tax Board); single national TIN since the JTB consolidation |
| Validated by | Verified by Omolola Fasasi (MB058950) on 2026-06-21 |
| Skill version | 1.0 |

### Progressive Tax Rates — PITA (Sixth Schedule, applies for FY 2025)

**Progressive Tax Rates — PITA (Sixth Schedule, applies for FY 2025)**

| Chargeable income (NGN) | Rate | Cumulative tax at top of band |
| --- | --- | --- |
| First 300,000 | 7% | 21,000 |
| Next 300,000 (300,001 – 600,000) | 11% | 54,000 |
| Next 500,000 (600,001 – 1,100,000) | 15% | 129,000 |
| Next 500,000 (1,100,001 – 1,600,000) | 19% | 224,000 |
| Next 1,600,000 (1,600,001 – 3,200,000) | 21% | 560,000 |
| Above 3,200,000 | 24% | — |

### Progressive Tax Rates — NTA 2025 (effective FY 2026 onward — forward-planning only)

**Progressive Tax Rates — NTA 2025 (effective FY 2026 onward — forward-planning only)**

| Chargeable income (NGN) — TBC | Indicative rate — TBC |
| --- | --- |
| First ~800,000 (effectively tax-free via CRA + first-band 0%) | 0% |
| Next band | 15% |
| Next band | 18% |
| Next band | 21% |
| Top band (high-income surcharge) | 25% |

The Nigeria Tax Act 2025 consolidates and re-bands the PIT structure and **substantially raises the tax-free threshold** for low earners. Indicative structure per the First Schedule to NTA 2025 (TBC under NTA 2025 implementing regulations; verify final gazetted figures before applying):

**Do not apply NTA 2025 brackets to FY 2025 returns.** They are presented for client planning and for the FY 2026 changeover only. The precise gazetted figures must be confirmed before use.

### Consolidated Relief Allowance (CRA) — FY 2025

- **CRA formula** — CRA = max(NGN 200,000, 1% × Gross Income) + (20% × Gross Income)

- Computed on **gross income** (not assessable, not chargeable).
- Introduced in its present form by Finance Act 2020; replaced the pre-2020 personal allowance / children's allowance / dependent-relative allowance entirely.
- CRA is automatic — no documentation required.

Under NTA 2025 (FY 2026 onward), CRA is replaced by a higher tax-free threshold built into the bracket table; the explicit "20% + NGN 200,000" formula is not carried forward. **TBC under NTA 2025 implementing regulations.**

### Minimum Tax (FY 2025)

**Minimum Tax (FY 2025)**

| Element | Detail |
| --- | --- |
| Trigger | Where progressive PIT (after reliefs) is less than 1% of gross income |
| Rate | **1% of gross income** (Finance Act 2020 simplification) |
| Effect | Taxpayer pays the **higher** of progressive tax or minimum tax |
| Applies to | Resident individuals with gross income below the relief-absorption floor; cannot be avoided by inflating expenses |

**NTA 2025 abolishes the 1% minimum tax for individuals earning below the gazetted tax-free threshold.** Above that threshold, a revised floor applies — TBC under implementing regulations.

### Capital Allowances — PITA Fifth Schedule (FY 2025)

**Capital Allowances — PITA Fifth Schedule (FY 2025)**

| Asset class | Initial allowance | Annual allowance |
| --- | --- | --- |
| Industrial building | 15% | 10% |
| Non-industrial building | 5% | 10% |
| Motor vehicles | 50% | 25% |
| Plant and machinery — agricultural | 95% | 0% (single-shot) |
| Plant and machinery — other | 50% | 25% |
| Furniture and fittings | 25% | 20% |
| Computer / IT equipment | 50% | 25% |
| Mining (qualifying) | 95% | 0% |

- **CA restriction and residue** — Annual allowance is on tax written-down value (reducing balance). A statutory residue of NGN 10 is retained on each asset until disposal. Capital allowances are restricted to two-thirds of assessable income in any year of assessment for individuals; unutilised capital allowances carry forward indefinitely.  _(PITA s 14, Fifth Schedule para 24)_

### Reliefs (in addition to CRA) — PITA s 33

**Reliefs (in addition to CRA) — PITA s 33**

| Relief | Treatment |
| --- | --- |
| Pension contributions to a licensed Pension Fund Administrator (PFA) under Pension Reform Act 2014 | Deductible; minimum mandatory 8% (employee) + 10% (employer) of basic + housing + transport for employed; for self-employed, contributions to a PFA under the Micro Pension Plan or voluntary RSA are deductible at actual amount paid |
| National Housing Fund (NHF) | 2.5% of basic salary — voluntary for self-employed; deductible at actual amount paid |
| Life insurance premiums (own life or spouse's life) | Deductible at actual amount paid |
| National Health Insurance Scheme (NHIS) / private health insurance | Deductible at actual premium paid |
| Annuity contributions | Deductible at actual amount paid (subject to anti-abuse review) |
| Gratuity / approved retirement benefit schemes | Treated under separate Sixth Schedule rules |

### Conservative Defaults

**Conservative Defaults (Section 1)**

| Ambiguity | Default |
| --- | --- |
| Residency not confirmed | STOP — non-resident vs resident drives the entire computation |
| State of residence not confirmed | STOP — determines filing authority (SIRS vs FIRS) |
| CRA basis ambiguous | Apply on **gross income** (not net, not assessable) |
| Capex described as "expense" | Reclassify to capital allowance schedule; do not deduct as P&L expense |
| WHT certificate missing | Do **not** credit WHT against tax due |
| Minimum tax check forgotten | Always run min(progressive tax, 1% × gross) — pay the higher |
| FCT vs state confusion | FCT (Abuja) → FIRS; everywhere else → state SIRS |
| FY 2025 vs FY 2026 | Use PITA brackets for FY 2025; flag NTA 2025 for FY 2026 planning only |
| Self-employed pension status unknown | Assume no pension relief unless PFA RSA evidence supplied |
| Spouse income | Filed separately (each spouse is a separate taxable person under PITA s 2) — there is no joint return in Nigerian PIT |

## Section 2 — Required Inputs and Refusal Catalogue

### Required Inputs

**Minimum viable** — (a) residency confirmation for the full tax year 2025; (b) state of residence as at 1 January 2025; (c) TIN; (d) one of: bank statements covering the calendar year, a profit-and-loss extract from the books, or a gross-revenue figure with a credible expense breakdown.

**Recommended** — WHT certificates from all corporate clients who deducted WHT at source (5% on contracts, 10% on professional fees); PFA contribution receipts; NHF, NHIS, and life-insurance receipts; capital-asset register with acquisition dates and costs; prior-year PIT acknowledgement / assessment notice; rent receipts (own residence and business premises distinct).

**Ideal** — complete bookkeeping pack (general ledger, trial balance, P&L, balance sheet); full bukti-style WHT certificate set; prior-year capital-allowance carry-forward computation; any FIRS / SIRS correspondence in the prior 6 years; multi-state operations breakdown if applicable.

**Refusal if minimum is missing — SOFT WARN.** No residency + no documents = hard stop. Residency confirmed but no gross-income evidence = hard stop (rate computation impossible). Gross income documented but expense detail missing = proceed with reviewer warning; defaults assume minimum tax floor likely applies.

### Refusal Catalogue

- **R-NG-PIT-1** — Residency unknown. "Cannot proceed without residency confirmation. Nigerian PIT is based on the place of residence as at 1 January 2025. Non-residents are taxed only on Nigeria-source income, generally via WHT as a final tax. Please confirm physical residence and any travel/migration during the year before continuing."
- **R-NG-PIT-2** — State of residence unknown. "The filing authority is determined by state of residence as at 1 January 2025. FCT (Abuja) residents file with FIRS; every other state has its own SIRS (LIRS, RIRS, KIRS, etc.). The forms, instalment mechanics, and payment platforms differ. Please confirm the state."
- **R-NG-PIT-3** — Pure employee with PAYE only. "Employees subject only to monthly PAYE withholding are administered by the employer. For PAYE return preparation and monthly PAYE remittance, use `ng-paye`. This skill handles the individual's own annual self-assessment for self-employed and mixed-income individuals."
- **R-NG-PIT-4** — Company / corporate (CIT) return. "Limited companies file Companies Income Tax (CIT) under CITA, not PIT. Out of scope — escalate to `ng-cit` or a Nigerian corporate tax practitioner."
- **R-NG-PIT-5** — Petroleum profits tax / upstream oil & gas. "Petroleum operations are governed by the Petroleum Profits Tax Act / Petroleum Industry Act 2021. Out of scope. Escalate."
- **R-NG-PIT-6** — Partial-year resident or dual residency. "Mid-year migration, treaty tie-breakers, and split-year computations require Nigerian double-tax treaty analysis. Out of scope — escalate to a CITN-registered tax practitioner."
- **R-NG-PIT-7** — VAT (consumption tax) return requested. "This skill covers PIT only. For Nigerian VAT use `ng-vat-return` or `nigeria-vat`."
- **R-NG-PIT-8** — Audit / tax-investigation / objection in progress. "Active enforcement (Notice of Assessment objection, Tax Appeal Tribunal proceedings, EFCC tax-fraud referral) requires representation by a CITN member with right of audience. Do not advise. Escalate immediately."
- **R-NG-PIT-9** — Pre-2020 deduction system requested. "The old personal allowance + children's allowance + dependent-relative allowance system was repealed by Finance Act 2020 with effect from year of assessment 2020. Do not apply pre-2020 reliefs to FY 2025."
- **R-NG-PIT-10** — NTA 2025 applied to FY 2025. "Nigeria Tax Act 2025 commences 1 January 2026. Do not apply NTA 2025 brackets or tax-free thresholds to FY 2025 returns. Use PITA Sixth Schedule for FY 2025."

## Section 3 — Tier 1 Rules: Computation Flow

### 3.1 Computation flow (FY 2025 under PITA)

- **Computation flow** — Gross income from all sources (worldwide for residents) = business income (sole trade / pekerjaan / professional fees) + employment income (salary + benefits-in-kind, if any) + investment income (interest, dividends gross — though most are subject to WHT as a final tax) + rental income (gross rent) + other taxable income (royalties, prizes outside the final-tax categories) – allowable business expenses (wholly, exclusively, necessarily, reasonably incurred — PITA s 20) – capital allowances (Fifth Schedule, capped at 2/3 of assessable income for the year) = Assessable income + other income (post-deduction items not in the trade) = Total income – Consolidated Relief Allowance (NGN 200,000 or 1% × gross, whichever higher; PLUS 20% × gross) – Pension (PFA RSA contributions) – NHF – Life insurance premium – NHIS / approved health insurance – Annuity / other approved reliefs = Chargeable income × Sixth Schedule progressive rates (7%, 11%, 15%, 19%, 21%, 24%) = Tax per progressive rates COMPARE WITH 1% × gross income (minimum tax floor) → Tax payable = MAX(progressive tax, minimum tax) – WHT credits (only with certificate) – Provisional / instalment payments made during the year = Final tax due (or refund)

### 3.2 T1-NG-PIT-1 — CRA is computed on GROSS income

- **T1-NG-PIT-1** — The Consolidated Relief Allowance formula uses gross income, not assessable income and not chargeable income. The 20% factor and the NGN 200,000 / 1% floor are both applied to gross. This is the single most common error in Nigerian PIT returns.

### 3.3 T1-NG-PIT-2 — Minimum tax is a hard floor

- **T1-NG-PIT-2** — Always run minimum tax (1% × gross income) and compare with progressive tax. The taxpayer pays the higher. Expenses cannot bring the liability below 1% of gross. The minimum tax is not avoided by capital allowances, CRA, or other reliefs.

### 3.4 T1-NG-PIT-3 — Capital expenditure cannot be expensed

- **T1-NG-PIT-3** — Capex on qualifying assets is never deducted as a business expense in the P&L. It is moved to the capital-allowance schedule and absorbed via initial + annual allowance, capped at two-thirds of assessable income per year. Excess capital allowance carries forward indefinitely.

### 3.5 T1-NG-PIT-4 — WHT is a credit, not an income exclusion

- **T1-NG-PIT-4** — When a corporate client deducts WHT at 5% (contracts) or 10% (professional fees), the gross fee is included in gross income for the individual's return; the WHT is then credited against tax liability. Gross-up the receipt — do not net the WHT off the income line. WHT credit requires a valid WHT certificate (credit note) from the deducting party.

### 3.6 T1-NG-PIT-5 — Filing authority follows residency

- **T1-NG-PIT-5** — FCT residents file with FIRS. All other state residents file with their respective State Internal Revenue Service (SIRS): LIRS (Lagos), RIRS (Rivers), KIRS (Kano), OYIRS (Oyo), etc. The First Schedule to PITA defines "place of residence" with priority rules for individuals with multiple residences (principal residence, then habitual abode, then place of business). Determined as at 1 January of the tax year.

### 3.7 T1-NG-PIT-6 — Spouses are separate taxpayers

- **T1-NG-PIT-6** — Nigerian PIT has no joint return. Each spouse is independently assessed, files separately, and uses separate CRA. A married individual does not get an enhanced CRA or any spouse uplift. Dependants do not increase CRA either (the pre-2020 system that gave a children's allowance was repealed).

### 3.8 T1-NG-PIT-7 — Old reliefs are abolished

- **T1-NG-PIT-7** — Do not apply the pre-2020 personal allowance (NGN 5,000 plus 20% of earned income), children's allowance, dependent-relative allowance, or alimony / disability allowances in the historic form. The Finance Act 2020 collapsed all of those into CRA.

### 3.9 T1-NG-PIT-8 — Rounding

- **T1-NG-PIT-8** — Chargeable income is computed in whole NGN. The Sixth Schedule applies to the whole NGN chargeable income figure; the final tax payable is rounded to the nearest NGN (no kobo on the return).

## Section 4 — Tier 2 Catalogue (Reviewer Judgement Required)

**Section 4 — Tier 2 Catalogue (Reviewer Judgement Required)**

| Code | Situation | Issue | Suggested treatment |
| --- | --- | --- | --- |
| T2-NG-PIT-1 | Mixed personal / business vehicle | Apportionment between business and private use | Document business-use percentage with mileage log; default conservatively to 50% if undocumented |
| T2-NG-PIT-2 | Home office costs | Proportional deduction for dedicated business area | Require floor-area ratio and a documented exclusivity test; default to 0% if not exclusive |
| T2-NG-PIT-3 | Generator fuel and maintenance | Common Nigerian cost; mixed personal/business if home-based | Apportion as for vehicle; document hours of business use |
| T2-NG-PIT-4 | Capital allowance carry-forward from prior year | Verify residue values and prior-year computation | Inspect the asset register and the prior-year capital-allowance schedule; do not assume the carry-forward figure |
| T2-NG-PIT-5 | Foreign income for a Nigerian resident | Worldwide-income principle; double-tax relief under treaty or unilaterally | Identify treaty (UK, France, Netherlands, China, South Africa, Singapore, Canada, etc.) and apply ordinary credit method — limit to the lower of Nigerian tax on the foreign income and foreign tax paid; **escalate** for treaty interpretation |
| T2-NG-PIT-6 | Multiple states of operation (e.g. Lagos resident with business in Ogun) | Risk of dual taxation; SIRS jurisdiction | Confirm place of residence as at 1 January (this controls); business may still create state-level multi-jurisdiction issues — escalate |
| T2-NG-PIT-7 | Lump-sum / large irregular receipt (e.g. one-off consultancy fee) | Whether trade income or "windfall"; whether minimum tax base inflates | Verify trade nexus; gross income for minimum tax includes the receipt; consider spread or instalment treatment under PITA only if statutorily permitted |
| T2-NG-PIT-8 | Voluntary pension contribution by self-employed exceeding statutory minimum | Deductibility cap | Allow at actual amount but flag if exceeds 20% of gross income — anti-abuse risk |
| T2-NG-PIT-9 | Gift / inheritance receipt | Generally not subject to PIT but may interact with stamp duty / capital transfer | Confirm nature; usually excluded from PIT gross income — escalate if value is material |
| T2-NG-PIT-10 | Cryptocurrency disposal gains | No clear PIT framework pre-NTA 2025; NTA 2025 introduces explicit digital-asset rules | For FY 2025, treat trading gains as business income if frequent; investment gains generally outside PIT until NTA 2025 takes effect — **flag and escalate** |
| T2-NG-PIT-11 | Director's fees | Subject to PIT in the director's hands; usually WHT 10% | Gross-up; claim WHT certificate; deductibility on company side governed by CITA, not this skill |
| T2-NG-PIT-12 | Late-year change of residence | First Schedule residency test snapshot 1 January | The 1 January snapshot controls for the year; mid-year moves do **not** redirect filing authority for that year |

## Section 5 — Foreign Income, Double-Tax Relief, and NTA 2025 Transitional

### 5.1 Worldwide income for residents

- **Worldwide income for residents** — A Nigerian-resident individual is taxable on worldwide income. Foreign-source business income, foreign employment income, foreign rental, foreign dividends, and foreign interest are all included in gross income and run through the Sixth Schedule along with Nigerian-source income.  _(PITA s 3(1)(b))_

### 5.2 Double-tax relief — treaty vs unilateral

- **Double-tax relief mechanics** — Nigeria has Double Tax Agreements in force with (non-exhaustive): United Kingdom, France, Netherlands, Belgium, Canada, China, South Africa, Pakistan, Philippines, Romania, Czech Republic, Slovakia, South Korea, Singapore, Spain, Sweden, Italy. Treaty relief is by the ordinary credit method: the credit is the lower of (a) the foreign tax actually paid and (b) the Nigerian tax attributable to the foreign-source income (computed as foreign net income / total net income × total Nigerian tax). Excess foreign tax is not carried forward. For non-treaty jurisdictions, PITA s 38 provides unilateral relief on the same ordinary-credit basis where the foreign country grants reciprocal relief. **Documentation:** require an official statement from the foreign tax authority (or an equivalent payment receipt) showing the foreign tax paid. Without it, do not allow the credit (R-NG-PIT-fallthrough — escalate).  _(PITA s 38)_

### 5.3 Non-residents earning Nigeria-source income

- **Non-residents earning Nigeria-source income** — A non-resident individual is taxed only on Nigeria-source income. For most categories (professional services rendered to Nigerian payers, royalties, certain rental income), WHT applied by the Nigerian payer is the final tax — no annual return is required from the non-resident. Exceptions: non-residents with a Nigerian fixed base of business may need to file with FIRS; escalate to a Nigerian tax practitioner in any such case.

### 5.4 NTA 2025 transitional considerations (forward planning only)

**NTA 2025 transitional considerations**

| Theme | PITA position (FY 2025) | NTA 2025 (FY 2026 onward) — TBC under implementing regulations |
| --- | --- | --- |
| Brackets | 7% / 11% / 15% / 19% / 21% / 24% | Re-banded; raised tax-free threshold (~NGN 800k indicative); top band ~25% |
| Tax-free floor | Embedded in CRA mechanics | Explicit tax-free threshold in the bracket table; CRA formula retired |
| Minimum tax (individuals) | 1% of gross income | Abolished for low-income individuals; revised floor above threshold (TBC) |
| Reliefs (pension, NHF, life, NHIS) | Each separately deductible | Consolidated under a "rationalised reliefs" framework (TBC) |
| Filing authority architecture | FIRS for FCT + non-residents; SIRS for state residents | Reaffirmed; with greater coordination via the new Nigeria Revenue Service (NRS) where FIRS is restructured (TBC) |
| Digital assets | Largely silent | Explicit rules expected (TBC) |
| Self-employed / sole trader | Treated identically to other individuals for PIT | Continues; with simplified small-business presumptive option (TBC) |
| Commencement | — | 1 January 2026 |

**Action for FY 2025 returns:** Always apply PITA. Use NTA 2025 only to flag what changes in FY 2026 for client planning. Where a question concerns FY 2026 specifically, mark every NTA 2025 figure with "TBC — verify against the gazetted NTA 2025 implementing regulations" and defer to a Nigerian tax practitioner for final confirmation.

## Section 6 — Worked Example

**Facts.**
- Taxpayer: Adaeze Okonkwo, Nigerian resident in Lagos (LIRS jurisdiction).
- Sole trader — IT consultant. No employment income. No foreign income.
- 2025 gross professional fees: NGN 12,000,000 (all from Nigerian corporate clients).
- WHT deducted by clients at 10%: NGN 1,200,000 (full WHT certificate pack obtained).
- Business expenses (allowable, properly documented, all revenue in nature): NGN 3,500,000.
- Capital asset acquired in 2025: laptop NGN 800,000 (IT equipment — initial 50%, annual 25%).
- Pension contribution to PFA (voluntary RSA): NGN 480,000.
- Life insurance premium paid: NGN 120,000.
- NHIS premium paid: NGN 60,000.
- Filing status: single — irrelevant for PIT (no joint return).

**Step 1 — Capital allowance**

| Item | Cost (NGN) | Initial allowance | Annual allowance | Year-1 total |
| --- | --- | --- | --- | --- |
| Laptop (IT) | 800,000 | 50% × 800,000 = 400,000 | 25% × (800,000 − 400,000) = 100,000 | 500,000 |

Year-1 capital allowance: NGN 500,000.

```
Gross business receipts                        12,000,000
Less: allowable expenses                       (3,500,000)
Less: capital allowance (capped at 2/3 of
       assessable income before CA — applied
       here in full as it is below the cap)      (500,000)
Assessable income                               8,000,000
```

Capital-allowance cap check: 2/3 × (12,000,000 − 3,500,000) = 5,666,667. Year-1 CA of 500,000 is well below the cap → fully utilised.

```
Gross income (for CRA base)                    12,000,000
CRA fixed component: max(200,000, 1% × 12m)
                    = max(200,000, 120,000)       200,000
CRA variable component: 20% × 12,000,000        2,400,000
CRA total                                       2,600,000
```

```
Pension (PFA RSA)                                 480,000
Life insurance premium                            120,000
NHIS                                               60,000
Total other reliefs                               660,000
```

```
Assessable income                               8,000,000
Less CRA                                       (2,600,000)
Less other reliefs                               (660,000)
Chargeable income                               4,740,000
```

**Step 6 — Progressive tax (PITA Sixth Schedule)**

| Band (NGN) | Width × Rate | Tax (NGN) |
| --- | --- | --- |
| 0 – 300,000 | 300,000 × 7% | 21,000 |
| 300,001 – 600,000 | 300,000 × 11% | 33,000 |
| 600,001 – 1,100,000 | 500,000 × 15% | 75,000 |
| 1,100,001 – 1,600,000 | 500,000 × 19% | 95,000 |
| 1,600,001 – 3,200,000 | 1,600,000 × 21% | 336,000 |
| 3,200,001 – 4,740,000 | 1,540,000 × 24% | 369,600 |
| **Total progressive tax** |  | **929,600** |

```
Minimum tax = 1% × 12,000,000 = 120,000
Progressive tax (929,600) > minimum tax (120,000) → progressive controls
```

```
Tax per progressive rates                         929,600
Less WHT credit (certificates verified)        (1,200,000)
PIT due / (refund)                              (270,400)
```

Result: **NGN 270,400 refund position**. File with **Lagos LIRS** (state of residence). Refund claim triggers LIRS audit — flag for reviewer and confirm WHT certificates are complete and matching client records before lodging the claim.

**Reviewer notes.**
- Confirm all WHT certificates are originals (or LIRS-recognised electronic credit notes via the LIRS e-Tax portal).
- Verify PFA RSA contribution is to a licensed PFA under PRA 2014.
- Year-2 capital allowance on the laptop: annual 25% × (400,000 residue − 100,000 prior) — actually 25% on TWDV of NGN 300,000 = NGN 75,000.
- If client moves to Abuja FCT on 2 January 2026, filing authority for FY 2026 is FIRS (reassessed each 1 January).

## Section 7 — Filing and Payment Mechanics

### 7.1 Filing authority — final mapping

**7.1 Filing authority — final mapping**

| Taxpayer category | Filing authority | Portal |
| --- | --- | --- |
| Resident in FCT (Abuja) | FIRS | TaxPro Max (taxpromax.firs.gov.ng) |
| Resident in any other state | State Internal Revenue Service of the state of residence | State-specific (LIRS, RIRS, KIRS, OYIRS, etc.) |
| Armed forces, police force, foreign-service officers (regardless of physical residence) | FIRS | TaxPro Max |
| Non-resident with Nigeria-source income subject to non-final treatment | FIRS | TaxPro Max |
| Itinerant worker (no fixed residence) | First Schedule deeming rules; usually FIRS | TaxPro Max |

### 7.2 Annual return — Form A (self-assessment)

- **Form A filing details** — The individual self-assessment return (commonly "Form A — Income Tax Form for Returns of Income and Claims for Allowances and Reliefs") is filed by 31 March of the year following the tax year. For FY 2025, deadline is 31 March 2026. Components: - Personal data (TIN, NIN, contact details, state of residence as at 1 January). - Statement of income from all sources (business, employment, investment, rental, other). - Capital allowance computation schedule. - CRA and other reliefs schedule. - WHT credit claim with certificates attached. - Tax computation worksheet. - Declaration and signature. Many states provide e-filing portals (LIRS e-Tax, FIRS TaxPro Max). Manual paper filing remains accepted by most SIRS.

### 7.3 Provisional / instalment payments

- **Provisional / instalment payments** — PITA s 41 contemplates payment of the assessed tax by the deadline. Many SIRS (notably LIRS) operate a provisional instalment system whereby self-employed individuals pay quarterly provisional tax based on prior-year liability, with the balance settled on filing of the annual return. Confirm with the relevant SIRS — practice varies.  _(PITA s 41)_

### 7.4 Late filing and late payment

**7.4 Late filing and late payment**

| Breach | Sanction |
| --- | --- |
| Late filing of return | NGN 50,000 first month + NGN 25,000 per subsequent month (PITA s 94 / Finance Act 2020) |
| Late payment of assessed tax | 10% penalty + interest at Central Bank of Nigeria Monetary Policy Rate (MPR) + spread, per annum (PITA s 76, 77) |
| Failure to register / obtain TIN | Administrative penalty per JTB schedule |
| Failure to keep records | NGN 50,000 fine (PITA s 81) |
| Incorrect return without fraudulent intent | Additional tax = twice the difference (PITA s 95) |
| Tax evasion (wilful) | NGN 20,000 fine and/or imprisonment up to 3 years (PITA s 96) |

### 7.5 Record keeping

- **Record keeping requirements** — Minimum retention: 6 years from the end of the year of assessment to which the records relate. Documents include invoices, receipts, bank statements, contracts, WHT certificates, capital-asset records, and pension / insurance receipts. WHT certificates should be retained permanently — they may be needed in a refund audit any time within the 6-year window.  _(PITA s 81)_

### 7.6 NTA 2025 — forward note

NTA 2025 restructures FIRS into the Nigeria Revenue Service (NRS) and reaffirms the FIRS/SIRS split for PIT. From FY 2026, expect new return forms, a central digital filing portal, and possible PAYE / self-assessment harmonisation. TBC under NTA 2025 implementing regulations. Do not rely on these structural changes for FY 2025 filings.

## Section 8 — Conservative Defaults

**Section 8 — Conservative Defaults**

| Situation | Conservative default | Rationale |
| --- | --- | --- |
| Residency unconfirmed | Stop — request residency declaration | Drives the whole return |
| State of residence ambiguous (e.g. moved late December 2024) | Apply 1 January 2025 snapshot strictly per First Schedule; flag for reviewer | Statute uses the snapshot test |
| Gross income includes a one-off large receipt | Include in full gross for the year; check minimum-tax base | No spreading without statutory authority |
| Mixed personal/business expense, no documentation | Disallow entirely | Wholly-and-exclusively test (PITA s 20) |
| Capital allowance carry-forward unverified | Disallow the carry-forward this year; flag for reviewer to verify prior-year computation | No reliance on undocumented carry |
| WHT certificate missing | Disallow credit; flag for client follow-up with payer | Anti-double-claim discipline |
| Life insurance premium for a non-spouse (e.g. adult child) | Disallow | Statute permits own-life and spouse-life only |
| Pension to an unlicensed scheme | Disallow | Pension Reform Act 2014 requires licensed PFA |
| Foreign tax credit without official certificate | Disallow | Documentation requirement |
| FY 2025 client asks about NTA 2025 bracket impact | Compute under PITA for FY 2025; provide NTA 2025 numbers only as "TBC for FY 2026 planning" | Statutory commencement is 1 January 2026 |
| Refund position (WHT > tax) | Submit refund claim only with complete certificate pack; warn client of audit likelihood | LIRS / FIRS refund process triggers verification |
| Minimum tax appears to apply | Always show both computations on the working paper | Transparency to reviewer |
| Multiple states of operation | Apply residency snapshot for filing; flag T2-NG-PIT-6 | Avoid double-state filing |
| Self-employed director's fees from own company | Include in gross PIT income; verify WHT and CITA-side treatment separately | Trans-skill coordination with `ng-cit` |

## Section 9 — Sources

### Primary legislation (FY 2025)

- **Personal Income Tax Act (PITA)** — Cap P8 LFN 2004.
- **Finance Act 2019** — repealed dependent-relative and children's allowances (partial).
- **Finance Act 2020** — introduced the present CRA formula and simplified the 1% minimum tax base; abolished pre-existing personal/children's allowances.
- **Finance Act 2021** — administrative amendments.
- **Finance Act 2023** — administrative amendments and rate housekeeping.
- **Pension Reform Act 2014** — pension contribution framework, PFA licensing, RSA / Micro Pension Plan.
- **National Housing Fund Act** — NHF contribution rate and deductibility.
- **National Health Insurance Authority Act 2022** — NHIS / health insurance framework.

### Successor legislation (FY 2026 onward — forward planning only)

- **Nigeria Tax Act 2025 (NTA 2025)** — assented mid-2025; commences 1 January 2026. Consolidates PITA, CITA, VATA, CGTA, and stamp duty into a unified statute. All figures herein flagged "TBC under NTA 2025 implementing regulations" pending final commencement orders.
- **Nigeria Tax Administration Act 2025** — companion administrative statute.
- **Nigeria Revenue Service (Establishment) Act 2025** — restructures FIRS as the Nigeria Revenue Service (NRS).

### Filing infrastructure

- **FIRS — Federal Inland Revenue Service** — https://www.firs.gov.ng
- **TaxPro Max (FIRS portal)** — https://taxpromax.firs.gov.ng
- **LIRS — Lagos State Internal Revenue Service** — https://lirs.gov.ng
- **JTB — Joint Tax Board** — https://www.jtb.gov.ng (TIN issuance and inter-state coordination)
- Other SIRS portals vary; consult the state revenue website for the state of residence.

### Cross-references within this package

- `ng-paye.md` (if present) — employer-side PAYE return mechanics and monthly remittance.
- `ng-cit.md` (if present) — Companies Income Tax for limited companies.
- `ng-income-tax.md` — legacy self-employed PIT skill; retains useful bank-narration patterns; **superseded by this skill for tax-rule purposes**.
- `ng-vat-return.md` / `nigeria-vat.md` — VAT (consumption tax) treatment.
- `foundation.md` — workflow architecture and conservative-defaults principle.
- `intake.md` — onboarding question flow.
- `references.md` — source repository and verified-link index.

## PROHIBITIONS

- NEVER apply NTA 2025 brackets or thresholds to FY 2025 returns. PITA controls FY 2025.
- NEVER compute CRA on net income, assessable income, or chargeable income. CRA is on **gross income**.
- NEVER omit the minimum-tax check. Always compare progressive tax with 1% of gross.
- NEVER deduct capital expenditure as a business expense. Move to the capital-allowance schedule.
- NEVER allow capital allowances to exceed two-thirds of assessable income in a single year.
- NEVER claim a WHT credit without a valid WHT certificate from the deducting party.
- NEVER apply pre-2020 personal allowance, children's allowance, or dependent-relative allowance to FY 2025.
- NEVER file a joint return. Each spouse is a separate Nigerian PIT taxpayer.
- NEVER route an FCT (Abuja) resident's PIT return to a SIRS, or a state resident's PIT return to FIRS.
- NEVER apply the residency snapshot to any date other than 1 January of the tax year.
- NEVER allow pension relief for contributions to an unlicensed (non-PFA) scheme.
- NEVER claim life-insurance relief for premiums on the life of a person other than the taxpayer or the taxpayer's spouse.
- NEVER claim foreign tax credit beyond the ordinary-credit cap (Nigerian tax attributable to foreign income).
- NEVER apply NTA 2025 minimum-tax abolition retroactively to FY 2025.
- NEVER invent an NTA 2025 figure. Where unknown, mark "**TBC under NTA 2025 implementing regulations**" and stop.
- NEVER file or instruct filing — this skill produces a working paper for review by a CITN-registered Chartered Tax Practitioner or an ICAN-registered accountant only.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified Nigerian tax practitioner (CITN-registered Chartered Tax Practitioner or ICAN-registered accountant) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.

## Talk to a verified accountant

This skill is a tool, not an engagement. Every taxpayer's situation is
different, and the rules in the skill may not match your specific facts.

To speak with one of the licensed accountants who verifies skills for your
jurisdiction — **no liability on either side until you and the accountant sign
a formal engagement letter** — book a free 30-minute call:

**→ [Book a call](https://calendly.com/openaccountants-info/30min)**

We'll route you to the named verifier covering your country or state. You can
also see the full list of verified accountants at
[openaccountants.com/network](https://openaccountants.com/network).
