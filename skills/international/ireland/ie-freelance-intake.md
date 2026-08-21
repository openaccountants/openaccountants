---
name: ie-freelance-intake
description: ALWAYS USE THIS SKILL when a user asks for help preparing an Irish tax return AND mentions freelancing, self-employment, sole trader, LTD, contractor, or PSC in Ireland. Trigger on phrases like "Ireland tax return", "Form 11 Ireland", "Form 12 Ireland", "Irish sole trader", "Irish LTD CT1", "ROS Revenue Online Service", "self-assessment Ireland", "preliminary tax Ireland", "PRSI Class S", "USC Ireland", "Irish VAT registration", "Pillar Two QDMTT Ireland", or any similar phrasing where the user is an Irish tax resident self-employed individual, sole trader, partner, or small LTD director-shareholder. This is the REQUIRED entry point for the Irish freelance / SME workflow — every downstream skill in the stack (ie-income-tax-form11, ie-preliminary-tax, ie-prsi-class-s, ie-usc, ireland-vat-return, ie-corporation-tax, ie-paye, ie-payroll, ie-cgt, ie-cat, ie-formation, ie-return-assembly) depends on this skill running first. Uses ask_user_input_v0-style structured questions. Irish tax residents only (full-year residents under Section 819 TCA 1997, plus the 280-day combined test). ALWAYS read this skill first when starting an Irish freelance / SME tax workflow.
jurisdiction: IE
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# IE Freelance Intake

## What this file is

The intake orchestrator for Irish-resident self-employed individuals, sole traders, partners, and small LTD (private company limited by shares) director-shareholders, including personal service companies (PSCs). Every downstream Irish content skill depends on this skill producing a structured intake package first.

Job: (1) confirm the taxpayer is Irish tax resident under Section 819 TCA 1997, (2) determine domicile (resident-non-domiciled taxpayers attract the remittance basis under Section 71 TCA 1997), (3) classify the regime (sole trader / partnership → Form 11 income tax + PRSI Class S + USC; LTD → CT1 corporation tax + director Form 11; large MNE → Pillar Two top-up via QDMTT), (4) identify downstream skills to run, (5) hand off to `ie-return-assembly`. Outputs addressed to a credentialed Irish tax reviewer (a Chartered Tax Adviser (CTA) of the Irish Tax Institute, an ACA / ACCA / CPA, or an AITI-qualified agent registered on ROS). The reviewer signs off — this skill is not the preparer of record.

## Section 1 — Quick reference: regime decision tree at a glance

```
Irish tax resident (Section 819 TCA 1997)?  -> NO = REFUSE
   183 days in 2025  OR  280 days over 2024+2025 (>=30 in each)
       |
Domiciled in Ireland?
       |
       +-- NO  -> Remittance basis available (Section 71 TCA 1997) — flag for reviewer
       |
       +-- YES -> Worldwide income basis
       |
Entity?
       |
       +-- Sole trader / Partnership
       |       -> Form 11 (income tax 20% / 40%)
       |          + PRSI Class S 4.1% (>=EUR 5,000 reckonable)
       |          + USC 0.5% / 2% / 3% / 8% bands + 3% self-employed surcharge >EUR 100,000
       |          + Preliminary tax by 31 October 2025 (90% / 100% / 105% rule)
       |
       +-- LTD trading
       |       -> CT1 corporation tax 12.5% on trading income (Section 21 TCA 1997)
       |          + director-shareholder also files Form 11 for salary / dividends
       |
       +-- LTD non-trading / close-company investment
       |       -> CT1 corporation tax 25% on passive income
       |          + close-company surcharge under Section 440 TCA 1997 if undistributed
       |
       +-- Large MNE (>=EUR 750m consolidated revenue, 2 of last 4 years)
               -> Pillar Two top-up via QDMTT (Part 4A TCA 1997, Finance (No. 2) Act 2023)
                  REFUSE — out of scope; refer to Big 4 / specialist
```

Parallel routing (independent of entity):

- Turnover > EUR 85,000 goods / EUR 42,500 services (rolling 12 months) → VAT registration mandatory → route `ireland-vat-return`.
- Employees → route `ie-paye` + `ie-payroll`.
- Disposal of chargeable asset in 2025 → route `ie-cgt`.
- Received gift or inheritance in 2025 → route `ie-cat`.
- Entity unclear or formation needed → route `ie-formation`.
- Always final → `ie-return-assembly`.

## Section 2 — Workflow runbook (order of operations)

Strict order. Do not narrate steps.

1. **Opening** — one-line greeting + flow summary + reviewer reminder, then launch the refusal sweep.
2. **Refusal sweep** — single `ask_user_input_v0` call with the 5 questions in Section 5.1.
3. **Document dump** — ask user to upload everything at once (bank statements, sales invoices, purchase invoices, prior Form 11 / CT1, ROS notices of assessment, P30 / PAYE summaries, payroll registers, VAT3 returns, RCT records if construction). Do not insist on bank statements alone.
4. **Inference pass** — parse every document; extract turnover, expenses, PAYE withheld, prior preliminary tax, VAT collected / reclaimed.
5. **Regime classification** — apply Section 4 decision tree using inferred turnover + sweep answers.
6. **Confirmation** — show inferred summary + proposed regime + downstream-skill list; invite corrections.
7. **Gap filling** — `ask_user_input_v0` only for items documents cannot answer (domicile, PPSN / TRN, marital status / joint-assessment election, ROS access).
8. **Handoff** — produce Section 6 summary and invoke `ie-return-assembly`.

Operating principles: use `ask_user_input_v0` for multi-choice; free text only for names / PPSN / TRN. Batch up to 3 related independent questions. Never re-ask documents-visible facts. Irish terms in parentheses on first mention (e.g., "Personal Public Service Number (PPSN)"). All amounts in EUR.

## Section 3 — Required inputs

Some inferred from documents, the rest gap-filled. All mandatory before handoff.

- **Identity / registration:** legal name, PPSN (Personal Public Service Number — individuals) and / or TRN (Tax Reference Number — entities / sole-trader trade name), date of birth, marital / civil-partnership status (single / married-separate / married-joint / civil-partner), Revenue district office, ROS digital certificate active (yes / no).
- **Residence & domicile:** day count in Ireland 2025 (and 2024 if combined test relevant), domicile of origin and any domicile of choice, ordinary residence status (3 consecutive years), split-year treatment under Section 822 TCA 1997 if arrival / departure year.
- **Entity:** sole trader / partnership (general or limited) / LTD (CRO number, date of incorporation, accounting year-end) / DAC / CLG. PSC indicators: single director-shareholder, services to one principal client, IR35-style risk (Revenue eBrief 99/19, Karshan Supreme Court judgment 2023).
- **Revenue:** 2025 gross turnover, monthly / quarterly turnover detail, domestic vs intra-EU vs export mix (services to EU B2B → reverse charge VIES; goods to EU B2B → zero rate with VIES; exports outside EU → zero rate).
- **Tax history:** prior Form 11 / Form 12 / CT1 for 2022, 2023, 2024; outstanding preliminary tax / balancing payments; carried-forward losses (Section 381 / Section 382 TCA 1997); capital allowances pool (Section 284 TCA 1997).
- **Operational:** employee count (PAYE / PRSI / USC obligations under Section 985 TCA 1997), VAT registration (mandatory or elective under Section 9 VAT Consolidation Act 2010), RCT (Relevant Contracts Tax) if construction / forestry / meat processing principal (Section 530A TCA 1997), Local Property Tax (LPT) discharged.
- **Documents:** bank statements 2025, sales invoices, purchase invoices, prior Form 11 / CT1, ROS notices of assessment, P60 / employment-detail summary if also employed, payroll register if employer, VAT3 returns, eBrief / RTD annual VAT return, RCT deduction summary.

## Section 4 — Regime decision tree with thresholds and citations

All thresholds 2025-effective (Finance Act 2024, Finance (No. 2) Act 2023, Finance Act 2023).

### 4.1 Residency gate — Section 819 TCA 1997

- **Residency test** — Irish tax resident = present in Ireland for 183 days in the tax year, OR 280 days combined in the current year plus the immediately preceding year (with at least 30 days in each year). A "day" is any day on which the individual is present in the State (the historic midnight rule was abolished by Finance Act 2008; the current rule under Section 819(4) is "any part of a day"). - Full-year resident → continue. - Part-year resident with split-year relief (Section 822 TCA 1997 — arrival year for employment income, departure year for employment income; **does not apply to self-employment / trading income**) → **REFUSE** for split-year self-employment; refer to a Chartered Tax Adviser. - Non-resident → **REFUSE**.  _(Section 819 TCA 1997; Finance Act 2008)_

### 4.2 Domicile gate — Section 71 TCA 1997 + common-law domicile rules

- **Domicile / remittance basis** — Domicile is a common-law concept (domicile of origin, domicile of choice). Resident-non-domiciled individuals are taxed on Irish-source income and gains in full, but foreign income and gains only when **remitted** to Ireland (the remittance basis). The remittance basis does **not** apply to UK-source income for Irish-resident-non-domiciled persons (UK income is taxed on the arising basis under the Ireland-UK DTA / Section 73 TCA 1997). If domicile is unclear or foreign → flag for reviewer; route `ie-income-tax-form11` with `remittance_basis_election` flag. Do not assume.  _(Section 71 TCA 1997; Section 73 TCA 1997; Ireland-UK DTA)_

### 4.3 Entity gate

- **Entity classification routing** — - **Sole trader / partnership:** Form 11 self-assessment. Trading income taxed at marginal rates (20% standard band up to EUR 44,000 single / EUR 53,000 one-earner married 2025; 40% above). Partnerships file Form 1 (Partnership) plus each partner's share on their own Form 11. Route `ie-income-tax-form11`. - **LTD trading:** CT1 corporation tax. Trading income at 12.5% (Section 21 TCA 1997). Non-trading (passive) income at 25%. Close-company surcharge of 20% on undistributed investment / rental income (Section 440 TCA 1997) and 15% on undistributed service-company income (Section 441 TCA 1997). Director-shareholder also files Form 11 for own salary (Schedule E) and dividends (Schedule F). Route `ie-corporation-tax` + `ie-income-tax-form11`. - **LTD non-trading / investment holding:** CT1 at 25%; close-company surcharge likely. Route `ie-corporation-tax`. - **Entity unclear / formation needed:** route `ie-formation`. Out-of-scope refusals at this gate: - LTDs with > 50 employees → refer to in-house finance + audit firm. - Group structures with Irish parent and overseas subsidiaries → refer to specialist. - Large MNEs (consolidated revenue ≥ EUR 750m in 2 of last 4 years) caught by Pillar Two → QDMTT / IIR / UTPR under Part 4A TCA 1997 (inserted by Finance (No. 2) Act 2023, transposing Council Directive (EU) 2022/2523) → **REFUSE**; refer to Big 4 / specialist.  _(Section 21 TCA 1997; Section 440/441 TCA 1997; Part 4A TCA 1997; Finance (No. 2) Act 2023; Council Directive (EU) 2022/2523)_

### 4.4 VAT registration gate — Section 6 + Section 9 VAT Consolidation Act 2010; Finance Act 2024

- **VAT registration mandatory threshold — goods** — EUR 85,000 EUR (rolling 12-month period, supplies of goods, raised from EUR 80,000 by Finance Act 2023, then to EUR 85,000 effective 1 January 2024)  _(Section 6 / Section 9 VAT Consolidation Act 2010; Finance Act 2023; Finance Act 2024)_
- **VAT registration mandatory threshold — services** — EUR 42,500 EUR (rolling 12-month period, raised from EUR 37,500 to EUR 42,500 by Finance Act 2024, effective 1 January 2025)  _(Finance Act 2024)_
- **Mixed supplies threshold rule** — Mixed supplies: the services threshold (EUR 42,500) applies if services are more than 10% of total turnover; otherwise the goods threshold applies.  _(Section 6 / Section 9 VAT Consolidation Act 2010)_
- **Distance sales into Ireland threshold** — EUR 10,000 EUR (EU-wide threshold (OSS / IOSS))  _(Section 6 / Section 9 VAT Consolidation Act 2010)_
- **Acquisitions from EU Member States by exempt/non-taxable person threshold** — EUR 41,000 EUR  _(Section 6 / Section 9 VAT Consolidation Act 2010)_
- **Below-threshold elective registration** — If above threshold → route `ireland-vat-return`. Below threshold → elective registration may still be advantageous (input VAT recovery); route only if user elects or reviewer flags.  _(Section 6 / Section 9 VAT Consolidation Act 2010)_
- **VAT standard rate 2025** — 23% percent  _(VAT Consolidation Act 2010)_
- **VAT reduced rate 13.5%** — 13.5% percent (most services, construction, restaurant food was at 9% then back to 13.5% from 1 September 2023)  _(VAT Consolidation Act 2010)_
- **VAT reduced rate 9%** — 9% percent (gas and electricity to end-October 2025 under Finance Act 2024 extension; newspapers; some e-publications)  _(Finance Act 2024)_
- **VAT livestock rate** — 4.8% percent  _(VAT Consolidation Act 2010)_
- **VAT zero rate** — 0% percent (food staples, children's clothing, exports, intra-EU B2B with VIES)  _(VAT Consolidation Act 2010)_

### 4.5 PRSI Class S gate — Social Welfare Consolidation Act 2005, Section 20A; Social Welfare Act 2023

- **PRSI Class S rate** — 4.1% percent (effective 1 October 2024; full 2025 year is at 4.1% (increased from 4.0%))  _(Social Welfare Consolidation Act 2005, Section 20A; Social Welfare Act 2023)_
- **Minimum annual reckonable income to be liable** — EUR 5,000 EUR  _(Social Welfare Consolidation Act 2005, Section 20A)_
- **Minimum annual contribution** — EUR 650 EUR  _(Social Welfare Consolidation Act 2005, Section 20A)_
- **Class S coverage** — Self-employed individuals (sole traders, partners, proprietary directors with ≥ 50% shareholding) pay PRSI Class S on reckonable income (trading income + investment income + rental income). Class S covers State Pension (Contributory), Maternity / Paternity / Adoptive Benefit, Treatment Benefit, Widow's / Widower's Pension, Invalidity Pension (added 2017), Jobseeker's Benefit Self-Employed (added November 2019). Route `ie-prsi-class-s`.  _(Social Welfare Consolidation Act 2005, Section 20A)_

### 4.6 USC gate — Part 18D TCA 1997, Sections 531AM–531AAF; Finance Act 2024

**USC 2025 rate bands**  _(Part 18D TCA 1997, Sections 531AM–531AAF; Finance Act 2024)_

| Band | Rate |
| --- | --- |
| Up to EUR 12,012 | 0.5% |
| Next EUR 15,370 (up to EUR 27,382) | 2.0% |
| Next EUR 42,662 (up to EUR 70,044) | 3.0% |
| Balance above EUR 70,044 | 8.0% |

- **Self-employed USC surcharge** — 3% percent (on non-PAYE income above EUR 100,000 under Section 531AN(2) TCA 1997 — making effective top USC rate 11% on self-employment income over EUR 100k)  _(Section 531AN(2) TCA 1997)_
- **USC full exemption threshold** — EUR 13,000 EUR (total income; medical-card holders + over-70s capped at 2%)  _(Part 18D TCA 1997)_

### 4.7 Preliminary tax gate — Section 958 TCA 1997; Section 959AN

- **Preliminary tax deadline and calculation rule** — Sole traders / partners on self-assessment must pay preliminary tax by **31 October 2025** (or the ROS extended deadline — typically mid-November — if filing **and** paying via ROS). The amount must be the **lower** of: - **90%** of the final liability for 2025 (current-year basis), OR - **100%** of the final liability for 2024 (prior-year basis), OR - **105%** of the final liability for 2023 (pre-prior-year basis) — only available where preliminary tax is paid by direct debit and the pre-prior year is not zero. Failure → interest at 0.0219% per day (~8% annualised) under Section 1080 TCA 1997 + surcharge of 5% (filed within 2 months late) or 10% (later) under Section 1084 TCA 1997. Route `ie-preliminary-tax`.  _(Section 958 TCA 1997; Section 959AN TCA 1997; Section 1080 TCA 1997; Section 1084 TCA 1997)_

### 4.8 Employer gate — Section 985 TCA 1997; PAYE Modernisation (Real-Time Reporting) from 1 January 2019

- **PAYE / employer PRSI rules** — Employees → operate PAYE / PRSI / USC in real time via ROS payroll software, file Payroll Submission Requests (PSRs) on or before each payday. Employer PRSI 8.9% Jan-Sep 2025; 9.0% from 1 Oct 2025 on weekly earnings ≤ EUR 496 / 11.05% above (Class A1 — 2025 rate increased from 11.05% to 11.15% Jan-Sep 2025; 11.25% from 1 Oct 2025 effective 1 October 2024, so full 2025 is 11.15% Jan-Sep 2025; 11.25% from 1 Oct 2025). Route `ie-paye` + `ie-payroll`.  _(Section 985 TCA 1997; PAYE Modernisation (from 1 January 2019))_

### 4.9 CGT gate — Section 28 TCA 1997 et seq.

- **Effective CGT rate for companies** — 33% percent  _(Section 28 TCA)_
- **CGT annual exemption** — EUR 1,270 EUR  _(Section 601 TCA 1997)_
- **CGT payment deadlines** — Disposals 1 January – 30 November 2025 → CGT due 15 December 2025. Disposals 1 – 31 December 2025 → CGT due 31 January 2026. Return (Form CG1 for non-Form-11 filers, or via Form 11 for self-assessed) due by 31 October 2026. Route `ie-cgt`.  _(Section 28 TCA 1997 et seq.)_

### 4.10 CAT gate — Capital Acquisitions Tax Consolidation Act 2003

- **CAT rate** — 33% percent (on the value above the relevant Group threshold (Finance Act 2024 thresholds, effective from 2 October 2024 Budget Day))  _(Capital Acquisitions Tax Consolidation Act 2003; Finance Act 2024)_

**CAT Group thresholds**  _(Capital Acquisitions Tax Consolidation Act 2003; Finance Act 2024)_

| Group | Description | Threshold |
| --- | --- | --- |
| Group A | child of disponer | EUR 400,000 (raised from EUR 335,000) |
| Group B | sibling, niece / nephew, lineal ancestor / descendant other than child | EUR 40,000 (raised from EUR 32,500) |
| Group C | all others | EUR 20,000 (raised from EUR 16,250) |

- **CAT pay-and-file deadline** — Pay-and-file by 31 October of the year following the valuation date if the valuation date falls between 1 September and 31 August. Route `ie-cat`.  _(Capital Acquisitions Tax Consolidation Act 2003)_

### 4.11 ROS digital-certificate channel

- **ROS filing channel requirement** — Form 11, CT1, VAT3, RTD, payroll PSRs, and preliminary tax are all filed through Revenue Online Service (ROS). If the user does not have an active ROS digital certificate, flag in `open_flags` — ROS onboarding takes 5–8 working days (RAN / dormant-cert reset). Without ROS access the user falls outside the ROS-extended pay-and-file deadline.

## Section 5 — Questions to ask the user

Use `ask_user_input_v0`. Batch where independent.

### 5.1 Refusal sweep (one batched `ask_user_input_v0` call, 5 single-select questions)

- **Q1 Residency 2025:** Full-year Irish resident (≥ 183 days in 2025) | Combined-test resident (280 days over 2024+2025 with ≥ 30 in each) | Part-year (arrived or left mid-2025) | Non-resident.
- **Q2 Domicile:** Irish-domiciled (born in Ireland, parents Irish-domiciled) | Foreign domicile of origin, now resident in Ireland | Acquired Irish domicile of choice | Not sure.
- **Q3 Entity:** Sole trader (own name) | Sole trader (registered business name) | Partnership (general or limited) | LTD (single director-shareholder / PSC) | LTD (multiple directors / employees) | DAC / CLG | Not sure.
- **Q4 2025 gross turnover (EUR):** ≤ EUR 42,500 | EUR 42,500 – EUR 85,000 | EUR 85,000 – EUR 500,000 | EUR 500,000 – EUR 5m | EUR 5m – EUR 50m | > EUR 50m | Not sure (infer from docs).
- **Q5 Activity mix:** Pure services | Pure goods | Mixed services + goods | Construction / forestry / meat-processing principal (RCT applies) | Financial services / investment funds (out of scope).

**Routing table**

| Answer | Action |
| --- | --- |
| Q1 full-year or combined-test | continue |
| Q1 part-year | **REFUSE** for self-employment split-year (Section 822 TCA 1997 does not cover trading income); refer to CTA |
| Q1 non-resident | **REFUSE** |
| Q2 Irish-domiciled | worldwide-income basis; continue |
| Q2 foreign domicile / not sure | flag `remittance_basis_review`; route `ie-income-tax-form11` with flag; reviewer confirms |
| Q3 sole trader / partnership | route `ie-income-tax-form11` + `ie-prsi-class-s` + `ie-usc` + `ie-preliminary-tax` |
| Q3 LTD single director (PSC) | route `ie-corporation-tax` + `ie-income-tax-form11` (director); flag IR35 / Karshan risk |
| Q3 LTD multiple directors / DAC / CLG | route `ie-corporation-tax`; if > 50 employees **REFUSE** |
| Q3 not sure | route `ie-formation` first |
| Q4 ≤ EUR 42,500 | VAT registration optional; flag below-threshold |
| Q4 EUR 42,500 – EUR 85,000 + services | VAT registration mandatory (services threshold); route `ireland-vat-return` |
| Q4 EUR 42,500 – EUR 85,000 + pure goods | VAT registration optional; flag for review |
| Q4 EUR 85,000 – EUR 5m | VAT registration mandatory; route `ireland-vat-return` |
| Q4 EUR 5m – EUR 50m | VAT mandatory; flag for reviewer (larger SME — verify scope) |
| Q4 > EUR 50m | **REFUSE** SPT prep; refer to CTA / Big 4; still load VAT for context |
| Q5 RCT principal | flag RCT obligation under Section 530A TCA 1997; reviewer registers for RCT on ROS |
| Q5 financial services / funds | **REFUSE** |

### 5.2 Secondary batched questions

- **Q6 Marital status / assessment:** Single | Married, jointly assessed | Married, separately assessed | Married, single-treatment | Civil-partnership joint | Widowed / surviving civil partner | Lone parent.
- **Q7 Employees in 2025:** None | 1–5 | 6–20 | > 20.
- **Q8 VAT registration status:** Registered (VAT number active on ROS) | Not registered (below threshold) | Not registered (above threshold — overdue) | Cancelled / deregistered in 2025 | Not sure.
- **Q9 Prior preliminary tax payment for 2024:** Paid in full by 31 October 2024 | Paid partial | Not paid | Did not file Form 11 for 2023 (first year) | Not sure.

**Routing table**

| Answer | Action |
| --- | --- |
| Q6 jointly assessed | tax bands and credits computed jointly; partner's PPSN required |
| Q6 separately assessed | each spouse files own Form 11; limited credit transfer |
| Q7 ≥ 1 employee | route `ie-paye` + `ie-payroll` |
| Q7 > 20 | flag (larger payroll — verify scope) |
| Q8 not registered + Q4 above threshold | flag **VAT registration overdue**; reviewer registers via ROS TR2 / TR1 |
| Q8 cancelled / deregistered | flag for reviewer (final VAT3 + RTD required) |
| Q9 not paid / first year | flag `preliminary_tax_2024_open`; route `ie-preliminary-tax` |

### 5.3 Capital events question

- **Q10 In 2025 did you:** Dispose of a chargeable asset (shares, second property, crypto, business) | Receive a gift or inheritance | Both | Neither | Not sure.

**Routing table**

| Answer | Action |
| --- | --- |
| Q10 disposal | route `ie-cgt`; capture disposal date for 15 December vs 31 January window |
| Q10 gift / inheritance | route `ie-cat`; capture relationship to disponer for Group A / B / C |
| Q10 both | route both |
| Q10 neither | skip |

### 5.4 Foreign income question

- **Q11 In 2025 did you have any foreign-source income, foreign bank accounts, foreign rental property, foreign pension, or foreign shares?** Yes (single item) | Yes (multiple) | No | Not sure.

Any "Yes" → flag `foreign_source_income`; reviewer confirms (a) DTA treatment (Ireland has ~75 DTAs), (b) foreign tax credit under Schedule 24 TCA 1997, (c) remittance-basis applicability if non-domiciled, (d) Form 11 Panel S (foreign income) entries.

### 5.5 ROS access

- **Q12 ROS digital certificate?** Yes (active, used in last 6 months) | Yes (dormant > 6 months — RAN required) | No (never registered) | Started but hit issues.

"No" / "dormant" / "issues" → flag in `open_flags`. ROS is the only filing channel for Form 11, CT1, VAT3, and preliminary tax. Without ROS the pay-and-file deadline is 31 October (not the ROS-extended mid-November date).

### 5.6 Onboarding fallback — no PPSN / TRN yet

If the user has no PPSN (individual) or no TRN (newly formed entity), the workflow cannot complete. Flag `no_ppsn_trn`:

- Individual without PPSN → refer to DSP (Department of Social Protection) Intreo or MyWelfare PPSN application. Cannot file Form 11 / Form 12 without PPSN.
- Entity without TRN → file Form TR1 (sole trader) / TR2 (company) via ROS or paper; TRN issues within 5 working days. Newly incorporated LTDs auto-receive a TRN on CRO registration if Form TR2 is filed concurrently with CRO Form A1.
- Director without PPSN (non-resident director of Irish LTD) → since 11 June 2023 (Companies (Corporate Enforcement Authority) Act 2021, s. 35) all directors filing with the CRO must have a PPSN, a CRO-issued IPN (Identified Person Number) via Form VIF, or an RBO PPSN-verification number. Flag `director_ppsn_required`.

## Section 6 — Intake output template

### 6.1 Human-readable confirmation (shown to user)

```
INTAKE SUMMARY — 2025 Ireland

Taxpayer: [Name] | PPSN: [seven digits + letter(s)] | TRN: [if entity]
Revenue district: [office] | Marital: [single | jointly assessed | …]
Entity: [Sole trader | Partnership | LTD trading | LTD non-trading | PSC]
ROS: [active | dormant — RAN required | onboarding needed]

RESIDENCE & DOMICILE
  - 2025 residency: full-year | combined-test (280-day)
  - Domicile: Irish | foreign-domiciled (remittance basis flagged) | unclear

REGIME: [Form 11 income tax | CT1 corporation tax | both]
  - 2025 turnover: EUR [X]
  - Activity: services | goods | mixed | RCT principal
  - VAT: registered | mandatory registration overdue | below threshold
  - PRSI Class S: applicable (4.1%) | not applicable (LTD director under PAYE)
  - USC: bands applied; 3% self-employed surcharge [if non-PAYE income > EUR 100k]
  - Preliminary tax 2025: due 31 October (or ROS-extended date)
  - Employees: [count]
  - CGT 2025: [disposal yes/no — 15 Dec or 31 Jan deadline]
  - CAT 2025: [gift/inheritance yes/no — Group A/B/C threshold]

DOWNSTREAM SKILLS:
  ie-income-tax-form11 [if sole trader / partner / director],
  ie-preliminary-tax [if sole trader / partner],
  ie-prsi-class-s [if self-employed],
  ie-usc [if self-employed or director-shareholder],
  ireland-vat-return [if VAT-registered or threshold breached],
  ie-corporation-tax [if LTD / DAC / CLG],
  ie-paye + ie-payroll [if employees],
  ie-cgt [if disposal],
  ie-cat [if gift/inheritance],
  ie-formation [if entity unclear],
  ie-return-assembly [always last].

OPEN FLAGS, REFUSALS TRIGGERED, CONSERVATIVE DEFAULTS APPLIED — listed below.

Confirm or correct anything above.
```

### 6.2 Structured intake package (internal JSON for ie-return-assembly)

```json
{
  "jurisdiction": "IE",
  "tax_year": 2025,
  "taxpayer": {
    "name": "", "ppsn": "", "trn": "",
    "revenue_district": "",
    "marital_status": "single|married_joint|married_separate|married_single_treatment|civil_partnership|widowed|lone_parent",
    "ros_certificate": "active|dormant|none|issues"
  },
  "residence_domicile": {
    "residency_2025": "full_year|combined_280_day|part_year|non_resident",
    "domicile": "irish|foreign|acquired_choice|unclear",
    "ordinary_residence": false,
    "remittance_basis_flag": false,
    "split_year_relief_applicable": false
  },
  "entity": {
    "type": "sole_trader|partnership|ltd_trading|ltd_non_trading|psc|dac|clg",
    "cro_number": "",
    "incorporation_date": "",
    "accounting_year_end": "",
    "psc_ir35_flag": false
  },
  "revenue": {
    "annual_turnover_eur": 0,
    "activity_mix": "services|goods|mixed|rct_principal",
    "rct_principal_flag": false,
    "intra_eu_b2b_supplies": 0,
    "exports_outside_eu": 0
  },
  "vat": {
    "registered": false,
    "vat_number": "",
    "mandatory_overdue_flag": false,
    "applicable_threshold_eur": 0,
    "elective_registration": false
  },
  "prsi_usc": {
    "prsi_class_s_applicable": false,
    "usc_self_employed_surcharge_applicable": false
  },
  "preliminary_tax": {
    "2024_paid_in_full": false,
    "2025_due_date": "2025-10-31",
    "ros_extended_date_available": false
  },
  "employment": {
    "has_employees": false, "employee_count": 0,
    "paye_modernisation_active": false
  },
  "capital_events": {
    "cgt_disposal_2025": false,
    "cgt_disposal_pre_dec_window": false,
    "cgt_disposal_dec_window": false,
    "cat_received_2025": false,
    "cat_group": "A|B|C|na"
  },
  "foreign_income_flag": false,
  "documents_received": [],
  "downstream_skills_to_load": [],
  "open_flags": [],
  "refusals_triggered": [],
  "conservative_defaults_applied": []
}
```

## Section 7 — Conservative defaults

When uncertain, prefer the safer (higher-tax / stricter-compliance) outcome and flag. All defaults visible to reviewer in `conservative_defaults_applied`.

**Conservative defaults table**

| Ambiguity | Conservative default |
| --- | --- |
| Residency borderline (~180 days, no combined-test data) | Assume non-resident → REFUSE; flag for day-count proof |
| Domicile unclear | Assume foreign domicile → flag `remittance_basis_review`; tax foreign income on arising basis pending reviewer call |
| Turnover near services threshold (EUR 40k–EUR 45k) | Assume above threshold → VAT registration mandatory |
| Turnover near goods threshold (EUR 80k–EUR 90k) | Assume above threshold → VAT registration mandatory |
| Activity mix near 10% services | Assume services > 10% → apply services threshold (EUR 42,500) |
| PSC vs employee unclear | Assume PSC with IR35 / Karshan risk; flag for reviewer |
| Sole trader vs partnership unclear (shared trade) | Assume partnership → Form 1 required |
| Preliminary tax base unclear | Apply 100% prior-year safe harbour (highest of available bases) |
| CGT disposal date near 30 November | Assume pre-30 November → 15 December payment window |
| CAT relationship unclear | Assume Group C (lowest threshold) |
| PRSI minimum (~EUR 5,000) | Assume above → flag Class S liability |
| Foreign income flagged but DTA unclear | Tax on arising basis with no FTC; reviewer to claim credit |
| ROS access unknown | Assume not active; flag for onboarding |
| Director PPSN status unknown (non-resident director) | Assume PPSN / IPN required under CCEA 2021 s. 35; flag |

## Section 8 — Refusal handling

Refusals fire from the refusal sweep or during inference. Protocol: stop the workflow, state the reason in one sentence, recommend a Chartered Tax Adviser (CTA, Irish Tax Institute) or AITI-qualified ROS agent, do not work around.

In-scope refusals:

- Part-year resident self-employment (Section 822 TCA 1997 does not cover trading income).
- Non-resident.
- Turnover > EUR 50m (out of small-SME scope).
- LTDs with > 50 employees.
- Group structures with Irish parent and overseas subsidiaries.
- Large MNEs in Pillar Two (QDMTT / IIR / UTPR under Part 4A TCA 1997, Finance (No. 2) Act 2023, transposing EU Directive 2022/2523) — consolidated revenue ≥ EUR 750m in 2 of last 4 years.
- Financial services / regulated investment funds.
- Charities / approved bodies under Section 207 / 208 TCA 1997 — separate compliance regime.
- Trusts and estates (Section 769 TCA 1997 et seq.).

Sample: "Stop — you arrived in Ireland in May 2025, so you are a part-year resident. Split-year relief under Section 822 TCA 1997 covers employment income only, not trading / self-employment income, so I cannot prepare your Form 11 for 2025 alone. You need a Chartered Tax Adviser (CTA) to handle the apportionment and the prior-jurisdiction interaction."

- **In-scope refusal list** — Part-year resident self-employment; Non-resident; Turnover > EUR 50m; LTDs with > 50 employees; Group structures with Irish parent and overseas subsidiaries; Large MNEs in Pillar Two (consolidated revenue ≥ EUR 750m in 2 of last 4 years); Financial services / regulated investment funds; Charities / approved bodies; Trusts and estates  _(Section 822 TCA 1997; Part 4A TCA 1997; Finance (No. 2) Act 2023; Section 207/208 TCA 1997; Section 769 TCA 1997 et seq.)_

## Section 9 — Self-checks before handoff

Run all 14 before invoking `ie-return-assembly`. Any failure → fix, do not hand off.

1. Refusal sweep used `ask_user_input_v0`, not prose.
2. Residency confirmed (full-year or combined-test); part-year → refused.
3. Domicile captured; remittance-basis flag set where appropriate.
4. Entity type set; PSC / IR35 flag set if single director-shareholder with one principal client.
5. Annual turnover recorded in EUR with bucket band.
6. VAT threshold gate applied to the correct threshold (goods EUR 85,000 vs services EUR 42,500); registration / overdue flag set.
7. PRSI Class S applicability set; minimum EUR 5,000 reckonable confirmed.
8. USC bands applied; 3% self-employed surcharge flagged if non-PAYE income > EUR 100,000.
9. Preliminary tax base selected (lower of 90% CY / 100% PY / 105% PPY).
10. Employee count set; `ie-paye` + `ie-payroll` in downstream list if > 0.
11. CGT and CAT events captured.
12. Foreign income flagged where applicable; DTA / Schedule 24 / remittance-basis review noted.
13. ROS certificate status captured; PPSN / TRN gaps flagged.
14. All conservative defaults recorded with citation; reviewer disclaimer present in opening + handoff.

## Section 10 — Final handoff to ie-return-assembly

Once gap-filling and self-checks pass, output a short handoff message naming (a) taxpayer + entity + Revenue district + ROS status, (b) regime selected with headline computation citation, (c) downstream skills in run-order, (d) skills explicitly not running and why, (e) reviewer reminder (CTA / ACA / ACCA / AITI sign-off via ROS). Then invoke `ie-return-assembly` with the Section 6.2 package.

Example (sole trader, services, VAT-registered, no employees, single):

> Intake complete. Aoife Ní Bhriain, sole trader (IT consultancy), PPSN 1234567T, Revenue district Dublin City Centre, ROS active. Full-year resident 2025, Irish-domiciled. 2025 turnover EUR 92,000 (services) → VAT-registered (above EUR 42,500 services threshold). Regime: Form 11 income tax at 20% / 40% bands + PRSI Class S 4.1% + USC 0.5% / 2% / 3% / 8% (no 3% self-employed surcharge — income below EUR 100,000). Preliminary tax due 31 October 2025 (ROS-extended mid-November); applying 100% prior-year safe harbour from 2024 Form 11. Running: ie-income-tax-form11, ie-preliminary-tax, ie-prsi-class-s, ie-usc, ireland-vat-return, ie-return-assembly. Not running: ie-corporation-tax, ie-paye, ie-payroll, ie-cgt, ie-cat, ie-formation. Needs CTA / AITI sign-off before ROS submission. Handing off now.

## Section 11 — Cross-skill references

**Inputs:** user documents (bank statements, sales / purchase invoices, prior Form 11 / CT1, ROS notices, payroll records, VAT3 returns, RCT records) + user answers. **Output:** Section 6.2 package consumed by `ie-return-assembly`.

Downstream skills (via ie-return-assembly):

- `ie-income-tax-form11` — Form 11 self-assessment income tax (Schedule D Cases I / II / III / IV / V; Schedule E; Schedule F); 20% / 40% bands; personal credits; trading-loss relief Section 381 / 382 TCA 1997.
- `ie-preliminary-tax` — 90% CY / 100% PY / 105% PPY rule under Section 958 TCA 1997.
- `ie-prsi-class-s` — Class S 4.1% on reckonable income; minimum EUR 5,000 / EUR 650.
- `ie-usc` — Universal Social Charge bands + 3% self-employed surcharge over EUR 100k.
- `ireland-vat-return` — VAT3 + RTD; rates 23% / 13.5% / 9% / 4.8% / 0%; thresholds EUR 85,000 goods / EUR 42,500 services.
- `ie-corporation-tax` — CT1 at 12.5% trading / 25% non-trading; close-company surcharge Section 440 / 441 TCA 1997.
- `ie-paye` + `ie-payroll` — PAYE Modernisation real-time reporting; employer PRSI Class A1 8.9% Jan-Sep 2025; 9.0% from 1 Oct 2025 / 11.15% Jan-Sep 2025; 11.25% from 1 Oct 2025 from 1 October 2024.
- `ie-cgt` — Section 28 TCA 1997 et seq.; 33% on gains > EUR 1,270; 15 December / 31 January split.
- `ie-cat` — Capital Acquisitions Tax Consolidation Act 2003; Group A / B / C thresholds EUR 400,000 / EUR 40,000 / EUR 20,000.
- `ie-formation` — sole trader vs partnership vs LTD; CRO + ROS TR1 / TR2 registration.
- `ie-return-assembly` — final orchestrator (Form 11 / CT1, working paper, reviewer brief, action list).

## Section 12 — Sources

Primary statutes and regulations cited (all 2025-effective; reviewer to verify Finance Act 2024 commencement orders):

- **Taxes Consolidation Act 1997 (TCA 1997)** — core income tax, corporation tax, CGT statute.
  - Section 21 — corporation tax rate 12.5% trading.
  - Section 28 et seq. — CGT charge.
  - Section 71 — remittance basis for resident-non-domiciled.
  - Section 73 — UK-source income exception.
  - Section 207 / 208 — charitable exemptions (out of scope).
  - Section 381 / 382 — trading-loss relief.
  - Section 440 / 441 — close-company surcharge.
  - Section 530A — RCT principal contractor.
  - Section 601 — CGT annual exemption EUR 1,270.
  - Section 769 et seq. — trusts (out of scope).
  - Section 819 — residence test (183 / 280 days).
  - Section 822 — split-year relief (employment income only).
  - Section 958 / 959AN — preliminary tax + self-assessment.
  - Section 985 — PAYE.
  - Section 1080 — interest on late tax.
  - Section 1084 — surcharge for late return.
  - Part 4A (inserted by Finance (No. 2) Act 2023) — Pillar Two GloBE rules (QDMTT / IIR / UTPR).
  - Part 18D (Sections 531AM–531AAF) — USC.
  - Schedule 24 — foreign tax credit.
- **Value-Added Tax Consolidation Act 2010** — VAT charge, registration, rates.
  - Section 6 / Section 9 — registration thresholds.
- **Capital Acquisitions Tax Consolidation Act 2003** — CAT.
- **Social Welfare Consolidation Act 2005**, Section 20A — PRSI Class S.
- **Finance Act 2024** — services VAT threshold EUR 42,500; CAT Group A / B / C threshold uplift; USC 4% → 3% band rate cut; 9% gas / electricity extension.
- **Finance (No. 2) Act 2023** — Pillar Two transposition (EU Directive 2022/2523).
- **Finance Act 2023** — VAT goods threshold EUR 85,000.
- **Social Welfare Act 2023** — PRSI Class S 4.0% → 4.1% from 1 October 2024.
- **Companies Act 2014** — LTD / DAC / CLG framework.
- **Companies (Corporate Enforcement Authority) Act 2021, s. 35** — director PPSN requirement from 11 June 2023.
- **Council Directive (EU) 2022/2523** — Pillar Two Directive.
- **Revenue eBrief 99/19** + **Karshan (Midlands) Ltd v Revenue Commissioners [2023] IESC 24** — employment vs self-employment / IR35-equivalent test.

## Change log

**v1.0 (May 2026):** Initial intake skill for the Irish freelance / SME workflow. Routes to ie-income-tax-form11, ie-preliminary-tax, ie-prsi-class-s, ie-usc, ireland-vat-return, ie-corporation-tax, ie-paye, ie-payroll, ie-cgt, ie-cat, ie-formation, ie-return-assembly. Reflects Finance Act 2024 (services VAT threshold EUR 42,500, CAT Group A EUR 400,000, USC 4% band cut to 3%), Social Welfare Act 2023 (PRSI Class S 4.1% from 1 October 2024), Finance (No. 2) Act 2023 (Pillar Two QDMTT / IIR / UTPR), and CCEA 2021 s. 35 (director PPSN requirement) for tax year 2025.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. OpenAccountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified Irish tax professional (a Chartered Tax Adviser (CTA) of the Irish Tax Institute, an ACA / ACCA / CPA, or an AITI-qualified agent registered on ROS) before filing with Revenue via ROS or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com).

---

*OpenAccountants — open-source accounting skills for AI*
*This output must be reviewed by a qualified professional before filing or acting upon.*
*Latest verified skills: openaccountants.com | Report errors: github.com/openaccountants/openaccountants*

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
