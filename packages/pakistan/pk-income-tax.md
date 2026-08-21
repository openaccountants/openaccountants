---
name: pk-income-tax
description: Use this skill whenever asked about Pakistan personal income tax for resident individuals, self-employed professionals, freelancers, sole proprietors, and Associations of Persons (AOP) filing an annual return with the Federal Board of Revenue (FBR). Trigger on phrases like "Pakistan income tax", "ITO 2001", "Income Tax Ordinance 2001", "FBR IRIS", "filer ATL Pakistan", "non-filer surcharge", "salary brackets Pakistan", "non-salary brackets Pakistan", "Finance Act 2025", "self-employed Pakistan tax", "AOP Pakistan", "freelance tax Pakistan", "PSEB IT export exemption", "Section 65 Pakistan", "10% surcharge Pakistan", or "annual return Pakistan". Covers the Income Tax Ordinance 2001 as amended by Finance Act 2024 and Finance Act 2025, salary vs non-salary progressive brackets, the Active Taxpayers List (ATL) filer-vs-non-filer differential withholding, AOP separate-entity taxation, Section 65 / PSEB IT export final-tax exemption, the 10% surcharge on income above Rs 10 million, foreign income credits, and IRIS portal mechanics. Out of scope — company (corporate) returns, Tax Year July-June for super tax above thresholds, capital gains on listed securities (NCCPL), property gain regimes, NTN registration mechanics, and provincial sales tax on services. ALWAYS read this skill before touching any Pakistan personal income tax work.
version: 1.0
jurisdiction: PK
tax_year: 2025
last_updated: 2026-07-13
reviewed_by: Ibrar Ali
review_status: current
depends_on: - income-tax-workflow-base
category: international
tier: 1
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# PK Income Tax

## Pakistan — Personal Income Tax (Individuals & AOP) — Skill v1.0

## Verified rates & thresholds (accountant-reviewed)

Reviewed against the cited tax authorities by **Ibrar Ali** on 2026-06-12.
Items flagged for further clarification are tracked separately and excluded here.
This block is generated from verified `skill_facts` — edit the facts, not the prose.

### pk-income-tax

- **Salary brackets (TY 2024-25 baseline — TBC under Finance Act 2025)** — 0 – 600,000 = 0; 600,001 – 1,200,000 = 1% on amount > 600,000; 1,200,001 – 2,200,000 = 11% on excess + 6,000; 2,200,001 – 3,200,000 = 23% on excess + 116,000; 3,200,001 – 4,100,000 = 30% on excess + 346,000; > 4,100,000 = 35% on excess + 616,000  _(First Schedule, Pt I, Div I)_
- **Salary table applies** — Where salary income is more than 75% of total taxable income  _(First Schedule, Pt I, Div I)_
- **Non-salary brackets — business / AOP (TY 2024-25 baseline — TBC FA 2025)** — 0 – 600,000 = 0; 600,001 – 1,200,000 = 15% on amount > 600,000; 1,200,001 – 1,600,000 = 20% on excess + 90,000; 1,600,001 – 3,200,000 = 30% on excess + 170,000; 3,200,001 – 5,600,000 = 40% on excess + 650,000; > 5,600,000 = 45% on excess + 1,610,000  _(First Schedule, Pt I, Div I)_
- **10% surcharge** — 10% for non-salaried/AOPs; reduced to 9% for salaried individuals.  _(Finance Act 2025)_
- **Minimum tax on turnover §113** — 1.25% where turnover > PKR 100,000,000 (TBC)  _(ITO 2001 §113)_
- **Default surcharge §205** — Change to: Higher of 12% per annum or KIBOR + 3%  _(ITO 2001 §205)_
- **Super tax §4C** — Separate charge above PKR 150M (out of this skill's scope)  _(ITO 2001 §4C)_
- **Resident individual** — Present in Pakistan ≥ 183 days in the tax year  _(ITO 2001 §82)_
- **Tax year** — 1 July – 30 June  _(ITO 2001 §7)_
- **Return deadline — AOP** — 30 September following close of tax year  _(ITO 2001 §118(3))_
- **Return deadline — AOP** — 30 September following close of tax year  _(ITO 2001 §118(3))_
- **Wealth statement** — Mandatory for every resident individual filing a return  _(ITO 2001 §116)_
- **Advance tax instalments** — Quarterly: 15 Sept, 15 Dec, 15 March, 15 June  _(ITO 2001 §147(5) & §147(5A))_
- **Advance tax threshold** — Latest assessed taxable income > PKR 1,000,000 (TBC)  _(ITO 2001 §147)_
- **§154A IT/ITeS export final tax (PSEB-registered)** — 0.25% of export proceeds via banking channel; excluded from bracket computation & from the PKR 10M surcharge test  _(ITO 2001 §154A)_
- **Non-PSEB IT export rate** — 1% (TBC)  _(ITO 2001 §154A)_
- **§61 charitable donation credit** — Up to 30% of taxable income (individuals & AOPs) / 20% (Companies)  _(ITO 2001 §61)_
- **§62 listed shares / sukuk credit** — Omitted  _(ITO 2001 §62)_
- **§63 voluntary pension contribution** — 20% of taxable income (age uplift available)  _(ITO 2001 §63)_
- **§103 foreign tax credit** — Lesser of foreign tax paid or Pakistan tax on that income; no carry-forward  _(ITO 2001 §103)_
- **AOP member share of profit** — Exempt at member level (AOP has already paid the tax)  _(ITO 2001 §92)_
- **ATL surcharge to regain filer status** — PKR 1,000 individual / 10,000 AOP / 20,000 company (TBC)  _(ITO 2001 (FA-set))_
- **Non-filer withholding** — Increased by 100% to 500%+ depending on the transaction code  _(ITO 2001 Tenth Schedule)_
- **Late filing penalty §182** — 0.1% per day, capped at 50% of tax payable (Minimum PKR 40,000 applies)  _(ITO 2001 §182)_
- **Business loss carry-forward** — 6 years  _(ITO 2001 §57)_

## Section 1 — Quick Reference

**Quick Reference**

| Field | Value |
| --- | --- |
| Country | Islamic Republic of Pakistan |
| Tax | Personal income tax (resident individuals and AOPs) |
| Currency | PKR (Pakistani Rupee) only |
| Tax year | 1 July to 30 June (e.g. TY 2025-26 = 1 Jul 2025 – 30 Jun 2026) |
| Primary legislation | Income Tax Ordinance 2001 ("ITO 2001"), as amended by Finance Act 2024 and Finance Act 2025 |
| Tax authority | Federal Board of Revenue (FBR), Government of Pakistan |
| Filing portal | IRIS (https://iris.fbr.gov.pk) |
| Annual return deadline — individuals | 30 September following close of tax year |
| Annual return deadline — AOP | 30 September following close of tax year |
| Payment instrument | Computerised Payment Receipt (CPR) generated from IRIS, paid at SBP / NBP / authorised bank |
| Filer status register | Active Taxpayers List (ATL), published weekly by FBR every Monday |
| NTN format | 7-digit NTN for AOP; CNIC (13-digit) functions as NTN for individuals |
| Validated by | Pending — requires sign-off by a registered Pakistan tax practitioner |
| Validation date | Verified by Ibrar Ali (8907) on 2026-06-12 |
| Skill version | 1.0 |

### Salary Brackets (TY 2024-25 baseline — likely revised by Finance Act 2025; TBC under Finance Act 2025)

**Salary Brackets Table**  _(ITO 2001 First Schedule, Part I, Division I)_

| Annual taxable salary (PKR) | Rate on excess in band | Cumulative tax at top of band (PKR) |
| --- | --- | --- |
| 0 – 600,000 | 0% | 0 |
| 600,001 – 1,200,000 | 1% on amount > 600,000 | 6,000 |
| 1,200,001 – 2,200,000 | 11% on amount > 1,200,000 + 6,000 | 116,000 |
| 2,200,001 – 3,200,000 | 23% on amount > 2,200,000 + 116,000 | 346,000 |
| 3,200,001 – 4,100,000 | 30% on amount > 3,200,000 + 346,000 | 616,000 |
| > 4,100,000 | 35% on amount > 4,100,000 + 616,000 | — |

- **Applicability** — Applies where salary income is more than 75% of total taxable income (ITO 2001 First Schedule, Part I, Division I).  _(ITO 2001 First Schedule, Part I, Division I)_

**TBC — verify under Finance Act 2025 final text.** Finance Act 2025 was widely expected to revise the lower-band rates (notably the 1% and 11% bands) downward in response to public consultation; until the final gazetted Schedule is confirmed for TY 2025-26, treat the above as the TY 2024-25 baseline and flag for reviewer.

### Non-Salary Brackets — Business, Profession, and AOP (TY 2024-25 baseline; TBC under Finance Act 2025)

**Non-Salary Brackets Table**  _(ITO 2001 First Schedule, Part I, Division I, second sub-table)_

| Annual taxable income (PKR) | Rate on excess in band | Cumulative tax at top of band (PKR) |
| --- | --- | --- |
| 0 – 600,000 | 0% | 0 |
| 600,001 – 1,200,000 | 15% on amount > 600,000 | 90,000 |
| 1,200,001 – 1,600,000 | 20% on amount > 1,200,000 + 90,000 | 170,000 |
| 1,600,001 – 3,200,000 | 30% on amount > 1,600,000 + 170,000 | 650,000 |
| 3,200,001 – 5,600,000 | 40% on amount > 3,200,000 + 650,000 | 1,610,000 |
| > 5,600,000 | 45% on amount > 5,600,000 + 1,610,000 | — |

- **Applicability** — Applies to AOPs and to individuals where salary is 75% or less of total taxable income (ITO 2001 First Schedule, Part I, Division I, second sub-table).  _(ITO 2001 First Schedule, Part I, Division I, second sub-table)_

### 10% Surcharge on High Income (Finance Act 2024 / retained Finance Act 2025)

- **10% surcharge on high income** — A 10% surcharge applies on the income tax payable where the individual's taxable income exceeds PKR 10,000,000 in the tax year. The surcharge is computed as 10% of the tax charged under the non-salary brackets (or 9% for salaried individuals) above (before withholding credits). TBC — confirm Finance Act 2025 retention and exact base.  _(Finance Act 2024 / Finance Act 2025)_

### Filer vs Non-Filer (ATL)

**Filer vs Non-Filer Table**

| Status | Definition | Effect |
| --- | --- | --- |
| Filer (on ATL) | Person whose name appears on the Active Taxpayers List for the relevant week, having filed the prior tax-year return and any required wealth statement | Standard withholding rates apply (default treatment under ITO 2001) |
| Late filer | Filed the prior year's return after due date but before being struck off ATL | Higher rates than filer, lower than non-filer for certain transactions (FA 2024 introduced a distinct "late filer" tier for some withholdings) |
| Non-filer (not on ATL) | Person whose name is not on the ATL | Withholding rates increased by 100% to 500%+ depending on the transaction code; certain transactions blocked entirely under §114B (utility disconnections, SIM blocking, banking restrictions) for persistent non-filers |

- **ATL publication and surcharge** — ATL is published every Monday by FBR. To appear on ATL for a given tax year, the taxpayer must have filed the prior year's return AND paid the ATL surcharge of PKR 1,000 (individual) / PKR 10,000 (AOP) / PKR 20,000 (company) where the return was filed after the due date. Surcharge amounts are TBC under Finance Act 2025.

### Conservative Defaults Snapshot

**Conservative Defaults Snapshot Table**

| Ambiguity | Default |
| --- | --- |
| Salary vs non-salary classification borderline (~75%) | Apply non-salary brackets (higher tax) |
| ATL status unknown | Treat as non-filer (higher withholding) |
| Finance Act 2025 bracket revision uncertain | Use TY 2024-25 brackets and flag "TBC under Finance Act 2025" |
| 10% surcharge threshold computation | Apply on tax before withholding credits, not after |
| PSEB / IT export exemption claim without registration certificate | Disallow; flag for reviewer |
| Foreign tax credit without official certificate | Disallow §103 credit |
| AOP partner — share of profit taxation | Exempt at member level under §92 (AOP pays the tax); do not re-tax in member's return |

## Section 2 — Required Inputs and Refusal Catalogue

### Required Inputs

- **Minimum viable** — Minimum viable — confirmation of (a) residency for the full tax year under §82 ITO 2001 (183-day rule), (b) classification as individual (salaried, business, or both) or AOP, (c) ATL status of the taxpayer at the time of filing, and (d) at least one of: (i) bank statements covering the tax year, (ii) ledger / books of account for business income, or (iii) salary certificate (for salaried), plus any withholding certificates (CPRs / payment proofs).
- **Recommended** — Recommended — CNIC / NTN, prior-year return acknowledgement and ATL surcharge payment proof, withholding certificates (mobile, utilities, banking, contracts), bank account profile, asset register with cost and acquisition date, wealth statement (mandatory for individuals under §116), PSEB registration certificate if claiming IT export benefits, foreign withholding tax certificates for §103 credit, AOP partnership deed and member CNICs.
- **Ideal** — Ideal — full trial balance, prior-year IRIS submission XML, complete CPR pack reconciled to bank statements, e-PRC for foreign exchange remittance receipts (for IT exporters), foreign asset disclosure schedule for residents with overseas holdings, and IRIS login confirmation.
- **Refusal if minimum is missing** — Refusal if minimum is missing — SOFT WARN. Residency unknown = hard stop (treaty / source-only taxation needs separate analysis). ATL status unknown = compute on filer basis but flag the withholding credit risk. No records at all but client insists on filing = hard stop.

### Refusal Catalogue

- **R-PK-IT-1 — Residency uncertain or non-resident** — Pakistan taxes residents on worldwide income and non-residents on Pakistan-source income only (ITO 2001 §11). Dual residency, mid-year migration, or non-resident with mixed-source income requires treaty analysis. Out of scope — escalate to a Pakistan tax practitioner.  _(ITO 2001 §11)_
- **R-PK-IT-2 — Company / corporate return** — Companies (Pvt Ltd, Public Ltd) file under the corporate return regime with separate rates (currently 29% standard / 20% small company) and super tax under §4C. Out of scope — escalate to a Pakistan corporate tax practitioner.  _(ITO 2001 §4C)_
- **R-PK-IT-3 — Capital gains on listed securities** — Capital gains on listed shares are collected by the National Clearing Company of Pakistan Limited (NCCPL) under §37A and reported separately on the IRIS return. This skill does not compute NCCPL gains; flag for reviewer and obtain the NCCPL annual certificate.  _(ITO 2001 §37A)_
- **R-PK-IT-4 — Property gain / immovable property disposal** — Capital gains on immovable property under §37(1A) and §236C/§236K advance taxes follow a separate rate schedule keyed to holding period and filer status. Out of scope — escalate.  _(ITO 2001 §37(1A), §236C, §236K)_
- **R-PK-IT-5 — Provincial sales tax on services** — Services are taxed by the four provinces and ICT (SRB / PRA / KPRA / BRA / ICT) separately from FBR income tax. This skill covers federal income tax only. Route service-tax queries to the provincial sales tax skill.
- **R-PK-IT-6 — Tax amnesty / declared foreign assets** — Historic amnesty schemes (Assets Declaration Act 2019 etc.) and current foreign-asset declarations under §116A require specialist handling. Out of scope — escalate.  _(ITO 2001 §116A)_
- **R-PK-IT-7 — Notices, audits, or appeals** — Audit (§177), amendment of assessment (§122), recovery proceedings (§137), or appeal before Commissioner Appeals / ATIR carry penalty and default surcharge implications. Do not advise — escalate immediately.  _(ITO 2001 §177, §122, §137)_
- **R-PK-IT-8 — Salary tax adjustment for employees (PAYE)** — Employee monthly withholding under §149 is computed by the employer. This skill covers the individual's annual return reconciling §149 withholding to bracket tax — not monthly PAYE computation for an employer client.  _(ITO 2001 §149)_
- **R-PK-IT-9 — Super tax under §4C** — Super tax on high earners (currently applied above PKR 150 million / PKR 500 million thresholds depending on bracket) is a separate charge from the 10% surcharge in this skill. Flag for reviewer and use a specialist computation.  _(ITO 2001 §4C)_

## Section 3 — Tier 1 Rules: Residency, Brackets, ATL Implications

### 3.1 Residency (ITO 2001 §82)

- **Residency test** — An individual is a resident for a tax year if: Present in Pakistan for 183 days or more in aggregate during the tax year (1 July – 30 June); OR an employee or official of the Federal or Provincial Government posted abroad in the tax year.  _(ITO 2001 §82)_
- **Whole-year determination** — Residence is determined for the whole tax year — Pakistan does not have a split-year regime. A person who becomes resident on day 183 is resident for the entire tax year and is taxed on worldwide income for that year (subject to §103 foreign tax credit and any treaty relief).  _(ITO 2001 §82)_
- **AOP residency (§84)** — An AOP is resident if its control and management is situated wholly or partly in Pakistan in the tax year.  _(ITO 2001 §84)_

### 3.2 Heads of income (§11(1))

- **Six heads of income** — 1. Salary (§12); 2. Income from property (§15); 3. Income from business (§18) — includes freelance / professional / sole-proprietor income; 4. Capital gains (§37 / §37A) — out of scope per refusals; 5. Income from other sources (§39) — interest, royalty, prize bonds, etc.; 6. Foreign source income (§102 / §103)  _(ITO 2001 §11(1))_
- **Freelance income classification** — Freelance and self-employed professional income is taxed under Income from Business (§18), not under "other sources", unless the activity is genuinely casual.  _(ITO 2001 §18)_

### 3.3 Salary vs non-salary classification (First Schedule)

- **75% classification rule** — The First Schedule, Part I, Division I provides two parallel rate tables. The salary table applies where salary income is more than 75% of total taxable income. Otherwise the non-salary table applies.  _(First Schedule, Part I, Division I)_

Worked test:
- Total taxable income PKR 3,000,000, of which salary PKR 2,400,000 (80%) → salary table.
- Total taxable income PKR 3,000,000, of which salary PKR 2,000,000 (66.7%) → non-salary table applies to the whole.
- A salaried person who also freelances must check the 75% test annually; the classification flips once salary drops below 75%.

- **Cliff edge flag** — The non-salary table top rate (45%) is materially higher than the salary table top rate (35%). The 75% boundary is therefore a hard cliff edge and should be flagged for any taxpayer whose salary fraction is near 75%.

### 3.4 Wealth statement (§116)

- **Wealth statement requirement** — Every resident individual filing a return is required to file a wealth statement and a wealth reconciliation showing year-on-year movement in net assets. Non-filing of the wealth statement is a separate breach from non-filing of the return. The wealth statement must reconcile to the change in net wealth, with unexplained increases potentially treated as taxable income under §111.  _(ITO 2001 §116)_

### 3.5 ATL — filer / late filer / non-filer

- **ATL differential withholding** — The Active Taxpayers List drives differential withholding under the Tenth Schedule. Effect: Withholding under §149 (salary), §151 (profit on debt), §152 (non-resident payments), §153 (services / contracts / supplies), §233 (commissions), §234/235 (motor vehicle / electricity), §236 family (mobile, banking, property, education, foreign travel) all carry filer-vs-non-filer rate differentials.  _(ITO 2001 Tenth Schedule)_
- **Non-filer rate increase** — Non-filers typically pay rates increased by 100% to 500%+ relative to the filer rate depending on the transaction code.  _(ITO 2001 Tenth Schedule)_
- **Late filer tier** — The "late filer" tier introduced by Finance Act 2024 applies an intermediate rate for certain codes (notably property transactions under §236C/§236K). TBC — verify Finance Act 2025 treatment of late filer tier.  _(Finance Act 2024)_
- **ATL entry requirement** — To be on ATL for a given tax year, the prior year's return must have been filed AND any ATL surcharge paid. ATL surcharge amounts are TBC under Finance Act 2025.

### 3.6 The 10% surcharge on income > PKR 10 million

- **10% surcharge mechanics** — Tax under First Schedule brackets (salary or non-salary) × 110%  (i.e. + 10% surcharge)  if taxable income > PKR 10,000,000 = Gross tax payable – Withholding credits (§168, etc.) – Foreign tax credit (§103) – Refundable advance taxes = Final tax payable or refundable  _(Finance Act 2025 (TBC))_
- **Surcharge base** — The surcharge is applied on the bracket tax before withholding credits — it increases the underlying tax liability, not the net cash payable per se.

## Section 4 — Tier 2: Section 65 / PSEB IT Export, Surcharges, Foreign Income

### 4.1 IT and IT-enabled services export — final tax / exemption

- **Regime overview** — Pakistan offers a long-standing concessionary regime for export of IT and IT-enabled services. The regime has migrated through several statutory homes over the past five years; the controlling provision for TY 2025-26 is TBC under Finance Act 2025 final text but historically rests in: Clause (133) of Part I of the Second Schedule (exemption on export of IT services up to 2025), and The Final Tax Regime for IT exports under §154A (introduced by FA 2022) which applies a final tax (commonly 0.25% or 1% depending on PSEB registration status) on export proceeds realised through normal banking channels.  _(Second Schedule Part I Clause (133); ITO 2001 §154A)_
- **Condition 1 — PSEB registration** — PSEB (Pakistan Software Export Board) registration. Without active PSEB registration, the concessional 0.25% final tax is unavailable; the default 1% (or higher) rate applies and ordinary withholding by the bank under §154A operates.  _(ITO 2001 §154A)_
- **Condition 2 — Banking channel** — Foreign exchange remittance through banking channel. Export receipts must be realised through a scheduled bank and supported by an e-PRC (Electronic Proceeds Realisation Certificate). Cash or undocumented receipts do not qualify.
- **Condition 3 — Filing of return** — The exporter must be on ATL and must file the annual return; failure makes the concession unavailable.
- **Condition 4 — No double-claim** — Income subjected to §154A final tax is not included in the progressive bracket computation; it is reported in IRIS under the final tax schedule and the relevant bank-deducted tax is the final liability for that income stream.  _(ITO 2001 §154A)_

Practical impact for a freelance software developer:
- If registered with PSEB and receiving USD via SWIFT through a Pakistani bank, the bank deducts 0.25% on remittance and that is the final tax on the export proceeds.
- The bracket computation (salary / non-salary tables) applies only to other income heads (local services, interest, rent, etc.).
- The 10% surcharge does not apply to income that has already borne final tax under §154A — final tax income is excluded from the "taxable income" used to test the PKR 10 million threshold. TBC — confirm exact treatment under Finance Act 2025.

### 4.2 Tax credits — Sections 61–65 family

**Tax credits table**

| Section | Credit | Cap |
| --- | --- | --- |
| §61 | Charitable donation to approved institution | 30% of taxable income for individuals & AOPs / 20% for Companies; credit at average rate of tax |
| §62 | Investment in shares of listed companies / sukuk | Lower of cost / 20% of taxable income / PKR 2,000,000 (TBC under FA 2025) |
| §63 | Voluntary pension scheme contribution | 20% of taxable income, age-uplift available; subject to §63 sub-rules |
| §65 (historic) | Investment tax credit for industrial undertakings | Largely sunset for individuals; verify if any residual applies |

- **Order of application** — Credits are applied at the average rate of tax (total tax ÷ total taxable income), not at the marginal rate. The order of credits is set out in §4(3): brackets → credits → minimum tax → surcharges → refund.  _(ITO 2001 §4(3))_

### 4.3 Foreign source income and §103 foreign tax credit

- **Worldwide taxation and gross-up** — Residents are taxed on worldwide income (§11(5)). Foreign source income is grossed up (add back foreign withholding to gross), included in the relevant head, and then §103 credit is allowed for foreign income tax paid.  _(ITO 2001 §11(5), §103)_
- **§103 credit formula** — §103 credit = lesser of: (a) foreign income tax actually paid on the foreign income, and (b) Pakistan tax otherwise payable on that foreign income = (foreign source income / total taxable income) × total Pakistan tax  _(ITO 2001 §103)_
- **Excess credit and documentation** — Excess foreign tax is not carried forward. Documentation: official certificate from the foreign tax authority or the foreign withholding agent; bank advice alone is generally insufficient.  _(ITO 2001 §103)_
- **Treaty relief** — Treaty relief (§107) overrides §103 where a DTA gives a more favourable outcome — e.g. exemption-with-progression instead of credit. TBC — confirm treaty position for the relevant country.  _(ITO 2001 §107)_

### 4.4 Other charges and minimum taxes to watch

- **Minimum tax on turnover (§113)** — 1.25% (general) on turnover applies to individuals with turnover above PKR 100,000,000 (TBC) — flag for any sole-prop with significant gross revenue.  _(ITO 2001 §113)_
- **Alternate Corporate Tax (§113C)** — corporate only, out of scope.  _(ITO 2001 §113C)_
- **Workers Welfare Fund / Workers Profit Participation Fund** — generally corporate; flag if AOP industrial.
- **Super tax under §4C** — separate from the 10% surcharge; applies to taxable income above defined thresholds (currently PKR 150M+ in brackets, TBC under Finance Act 2025). Refusal R-PK-IT-9.  _(ITO 2001 §4C)_
- **Default surcharge (§205)** — simple interest at the rate prescribed (currently higher of 12% per annum or KIBOR + 3%, TBC) on unpaid tax from the due date until paid.  _(ITO 2001 §205)_

### 4.5 AOP — separate entity taxation (§92)

- **AOP separate taxation** — An AOP is taxed as a separate person under the non-salary table (First Schedule Part I Division I). Members are NOT separately taxed on their share of AOP profit — §92(1) explicitly exempts the member's share from further tax in the member's individual return, because the AOP has already borne the tax.  _(ITO 2001 §92(1))_

Practical effect:
- The AOP files its own return (deadline 30 September) and pays bracket tax on its taxable income.
- Each member receives a share of profit which is reported in the member's individual return as "exempt" (informational only) — it does not enter the bracket computation.
- Salary or remuneration paid by an AOP to a member is not deductible at the AOP level (§21(j)) and is not separately taxable at the member level (§92(2)).
- Profit shares from AOPs are added back for rate purposes in some computations historically — TBC under current ITO 2001 wording.

## Section 5 — Worked Example: Freelance Software Developer in Karachi

Facts.
- Taxpayer: Saad, resident individual (Karachi), single, no dependents.
- Tax Year 2025-26 (1 July 2025 – 30 June 2026).
- Engaged as a freelance software developer for foreign clients.
- Gross fee receipts: PKR 5,000,000 for the year.
- Of which PKR 4,000,000 is realised through SBP-permitted banking channel against e-PRC from foreign clients (qualifies for §154A IT export final tax).
- Remaining PKR 1,000,000 is from local Pakistani clients (domestic services), no PSEB exemption.
- Saad is registered with PSEB and is on ATL for TY 2025-26.
- Bank deducted 0.25% × 4,000,000 = PKR 10,000 as final tax under §154A on the export proceeds.
- Local clients withheld §153 tax at filer rate (assume 3% on services): 3% × 1,000,000 = PKR 30,000 (creditable against bracket tax).
- Allowable business expenses (rent, internet, equipment depreciation, etc.) attributable to local revenue: PKR 200,000.
- No other income, no foreign income credit, no zakat.

**Step 1 — IT export proceeds (§154A final tax)**

| Item | PKR |
| --- | --- |
| Export receipts (PSEB-registered, e-PRC supported) | 4,000,000 |
| §154A final tax at 0.25% (bank-deducted) | (10,000) |
| Final liability on export proceeds | **Nil further tax — final** |

This stream is excluded from bracket computation and excluded from the PKR 10 million surcharge threshold test.

Step 2 — Bracket computation on non-final income.

Salary share of total non-final income: PKR 0 / PKR 1,000,000 = 0% → non-salary table applies.

**Step 2 — Bracket computation table**

| Item | PKR |
| --- | --- |
| Gross local fees | 1,000,000 |
| Less allowable expenses (§20) | (200,000) |
| Net taxable income (non-salary) | 800,000 |
| Tax on first 600,000 @ 0% | 0 |
| Tax on next 200,000 (800,000 − 600,000) @ 15% | 30,000 |
| **Bracket tax** | **30,000** |
| Less §153 withholding credit (filer rate, 3% × 1,000,000) | (30,000) |
| Tax payable on local income | **Nil** |

Step 3 — 10% surcharge test.

Taxable income for surcharge purposes: PKR 800,000 (final-tax income excluded). PKR 800,000 < PKR 10,000,000 → no surcharge applies.

Step 4 — Overall result.

- Final tax on export stream: PKR 10,000 (bank-deducted, settled).
- Tax on local stream: PKR 30,000 bracket tax fully covered by PKR 30,000 §153 withholding → nil net payable.
- Net cash payable with return: Nil.
- Refund position: nil refund (withholding exactly matched bracket tax).

Reviewer notes.
- Confirm PSEB registration certificate is current for the entire TY 2025-26; lapse mid-year reverts the affected proceeds to ordinary withholding at 1% (TBC).
- Confirm each export receipt has a matching e-PRC from the bank.
- Confirm Saad is on ATL on the date of every withholding event (filer rate applied at 3% under §153 assumed).
- File wealth statement under §116 reconciling net asset movement.
- Deadline: 30 September 2026.
- IRIS workflow: report export income in the Final Tax schedule (separate worksheet) and local income in the Business Income schedule.

Alternative scenario — what if Saad were NOT on PSEB / had no e-PRC?

The PKR 4,000,000 export stream would then be ordinary business income, included in the bracket computation:

**Alternative scenario table**

| Item | PKR |
| --- | --- |
| Total gross fees | 5,000,000 |
| Less expenses | (200,000) |
| Net taxable income (non-salary) | 4,800,000 |
| Tax on first 600,000 @ 0% | 0 |
| Tax on next 600,000 (to 1,200,000) @ 15% | 90,000 |
| Tax on next 400,000 (to 1,600,000) @ 20% | 80,000 |
| Tax on next 1,600,000 (to 3,200,000) @ 30% | 480,000 |
| Tax on next 1,600,000 (to 4,800,000) @ 40% | 640,000 |
| **Bracket tax** | **1,290,000** |

Taxable income PKR 4.8M < PKR 10M → no 10% surcharge. Cost of failing to register with PSEB: ~PKR 1.28M of additional tax for this profile. The numbers above are illustrative under the TY 2024-25 baseline non-salary brackets and TBC under Finance Act 2025.

## Section 6 — Filing and Payment Mechanics

### 6.1 IRIS portal

- **IRIS filing overview** — The annual return is filed through IRIS (https://iris.fbr.gov.pk), FBR's e-filing platform. Authentication uses CNIC (individuals) or NTN (AOP) plus password. IRIS pre-populates withholding data from the FBR Tax Asaan / Maloomat repositories pulled from the various §149/§151/§153/§236 withholding agents — reviewer must reconcile against client's CPRs.

Key IRIS workflow:
1. Login → "Declaration" → "114(1) (Return of Income for Individual)" or "114(1) — AOP" as applicable.
2. Pre-population: IRIS pulls withholding data; review and reconcile.
3. Complete heads of income — Salary, Business, Property, Other Sources, Capital Gains, Final Tax (§154A, §155, §236C etc.), Foreign Income.
4. Complete tax credits (§61–§65 family) and adjustments.
5. Complete the wealth statement (§116) — required for all resident individuals filing a return.
6. Generate the CPR (Computerised Payment Receipt) for any balance payable; pay via authorised bank channel.
7. Submit return. IRIS issues an acknowledgement.

### 6.2 Deadlines

**Deadlines table**

| Item | Deadline | Source |
| --- | --- | --- |
| Annual return — individual (§114) | 30 September following close of tax year | ITO 2001 §118(2) |
| Annual return — AOP (§114) | 30 September following close of tax year | ITO 2001 §118(3) (TBC under FA 2025) |
| Wealth statement (§116) | Filed with the return; mandatory for resident individuals | §116(2) |
| Payment of tax with return (§137) | On or before the return filing deadline | §137(1) |
| Extension request | Application to the Commissioner under §119 before the due date; extension limited and discretionary | §119 |
| Advance tax (§147) | Quarterly: 15 Sept, 15 Dec, 15 March, 15 June | §147(5) |

### 6.3 Advance tax — §147

- **Advance tax calculation** — Advance tax for the quarter = (latest assessed taxable income × current year's bracket rate / 4) – withholding tax collected during the quarter  _(ITO 2001 §147)_
- **Advance tax obligation and default** — Resident individuals and AOPs with the latest assessed taxable income above the threshold (currently PKR 1,000,000 — TBC under FA 2025) must pay advance tax in four quarterly instalments under §147. Failure to pay advance tax triggers default surcharge under §205.  _(ITO 2001 §147, §205)_

### 6.4 Late filing and late payment

**Late filing/payment table**

| Breach | Sanction |
| --- | --- |
| Late filing of return (§182) | Higher of (a) 0.1% of tax payable per day, capped at 50% of tax payable (minimum PKR 40,000), or (b) prescribed minimum penalty; **AND** removal from ATL until next list refresh after compliance |
| Late payment / short payment (§205) | Default surcharge at higher of 12% per annum or KIBOR + 3% (TBC), calculated daily |
| Failure to file wealth statement (§182A) | Separate penalty in addition to return-filing penalty |
| Concealment / wilful default (§192 / §192A) | Tax evasion penalties; potential prosecution |

Specific penalty amounts are TBC under Finance Act 2025. Default surcharge rate is set by SRO and revised periodically; verify the rate prevailing for the relevant period.

### 6.5 ATL surcharge to regain filer status

**ATL surcharge intro**

| Taxpayer type | ATL surcharge (TBC under FA 2025) |
| --- | --- |
| Individual | PKR 1,000 |
| AOP | PKR 10,000 |
| Company | PKR 20,000 |

- **Surcharge timing and consequences** — The surcharge must be paid before the name re-appears on the next weekly ATL refresh. Without ATL, the taxpayer faces the non-filer withholding multiplier on all subsequent transactions, which is typically far costlier than the ATL surcharge itself.

### 6.6 Refunds (§170)

- **Refund processing** — Refunds of excess withholding or §103 credit are claimed in the return and processed by the Commissioner. Refund processing in practice can take 6–24 months and may trigger audit selection under §177. Flag any large refund position for reviewer.  _(ITO 2001 §170, §177)_

## Section 7 — Conservative Defaults

**Conservative Defaults Table**

| Situation | Conservative default | Rationale |
| --- | --- | --- |
| Salary vs non-salary classification near the 75% boundary | Apply non-salary table | Higher top rate; cannot under-assess |
| ATL status not verified | Assume non-filer; flag client to confirm | Avoid under-recognising withholding cost |
| Finance Act 2025 bracket change uncertain | Use TY 2024-25 baseline; flag "TBC under Finance Act 2025" | Documented baseline, no speculation |
| 10% surcharge threshold computation | Apply on bracket tax before withholding credits | Aligns with §4 / First Schedule reading |
| PSEB / §154A claim — no registration certificate | Treat as ordinary business income; subject to bracket tax | Affirmative documentation required |
| Foreign tax credit — no official certificate | Disallow §103 credit | §103 documentation requirement |
| AOP member share of profit | Exempt under §92 in member's return | Statutory; do not double tax |
| Wealth statement reconciliation difference | Flag and request explanation; never plug | §111 unexplained-income risk |
| Local services with no withholding evidence | Do not claim §153 credit | Anti-double-credit |
| Carry-forward of business losses | Allow up to 6 years (§57) only if pembukuan-equivalent books exist | Statutory requirement |
| Currency of income | PKR; convert foreign currency at SBP daily rate on the date of receipt | §72 / SBP convention |
| Whether to file 1770-equivalent vs salary-only short return | Use full 114(1) individual return if any business income exists | Captures all heads properly |

## Section 8 — Sources

### Primary legislation

- Income Tax Ordinance 2001 (ITO 2001) — the principal tax statute, as amended by successive Finance Acts.
- Income Tax Rules 2002 — procedural rules under ITO 2001.
- Finance Act 2024 — amendments effective TY 2024-25 including the late-filer tier and surcharge changes.
- Finance Act 2025 — amendments effective TY 2025-26. TBC — verify final gazetted text for rate tables, surcharge retention, and threshold changes.

### Key provisions referenced

- §11 — Heads of income.
- §18 — Income from business.
- §20 — Deductions in computing business income.
- §57 — Set-off and carry-forward of business losses (6 years).
- §61–§65 — Tax credits (charitable donations, listed-shares investment, voluntary pension).
- §82 / §84 — Residence of individuals / AOPs.
- §92 — AOP separate-entity taxation; member share exemption.
- §103 — Foreign tax credit.
- §107 — Tax treaty relief.
- §111 — Unexplained income / assets.
- §113 — Minimum tax on turnover.
- §114 — Return of income.
- §116 — Wealth statement.
- §118 — Due dates for returns.
- §119 — Extension of time.
- §137 — Payment of tax.
- §147 — Advance tax payable by taxpayer.
- §149 — Salary withholding (employer).
- §151 — Profit on debt withholding.
- §153 — Payments for goods, services, contracts.
- §154A — Final tax on export of IT and IT-enabled services.
- §170 — Refunds.
- §177 — Audit.
- §182 / §182A — Late-filing penalties.
- §192 / §192A — Concealment penalties.
- §205 — Default surcharge.
- §236 family — Various advance-tax / withholding codes (mobile, banking, property, education, foreign travel).
- §4C — Super tax on high-earning persons (out of scope, see refusal R-PK-IT-9).
- First Schedule, Part I, Division I — Salary and non-salary rate tables.
- Second Schedule, Part I, Clause (133) — Historic IT export exemption (TBC residual applicability).
- Tenth Schedule — Higher withholding rates for persons not appearing on ATL.

### Filing infrastructure

- Federal Board of Revenue (FBR) — https://www.fbr.gov.pk
- IRIS portal — https://iris.fbr.gov.pk
- ATL search — https://www.fbr.gov.pk/active-taxpayer-list-atl
- PSEB (Pakistan Software Export Board) — https://www.pseb.org.pk
- State Bank of Pakistan (SBP) — exchange rate and foreign exchange remittance framework.

### Cross-references within this package

- `pakistan-sales-tax.md` — federal sales tax on goods (FED on services is provincial).
- `foundation.md` — workflow architecture and conservative-defaults principle.
- `intake.md` — onboarding question flow.
- `references.md` — source repository and verified-link index.

## PROHIBITIONS

- NEVER apply salary brackets to a taxpayer whose salary is 75% or less of taxable income — use the non-salary table.
- NEVER assume ATL / filer status without verifying against the current weekly Active Taxpayers List.
- NEVER claim §154A 0.25% concessional rate without a current PSEB registration certificate AND e-PRC documentation for every receipt.
- NEVER include §154A final-tax export income in the bracket computation, and NEVER include it in the PKR 10 million surcharge threshold test (TBC under FA 2025).
- NEVER re-tax an AOP member's share of profit at the member level — §92(1) exempts it.
- NEVER allow foreign tax credit under §103 without an official foreign tax authority certificate.
- NEVER carry forward foreign tax credit — excess foreign tax is lost.
- NEVER omit the wealth statement under §116 for a resident individual filing a return.
- NEVER plug a wealth-statement reconciliation gap — flag for §111 unexplained-income risk.
- NEVER file or instruct filing — this skill produces a working paper for review by a registered Pakistan tax practitioner only.
- NEVER apply Finance Act 2025 figures as confirmed without checking the final gazetted text — flag "TBC under Finance Act 2025" wherever in doubt.
- NEVER compute super tax under §4C in this skill — refuse and escalate (R-PK-IT-9).
- NEVER advise on audit, recovery, or appeal proceedings — escalate (R-PK-IT-7).

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a registered Pakistan tax practitioner (Income Tax Practitioner, Chartered Accountant, or equivalent licensed professional) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.

## Talk to a verified accountant

This skill is a tool, not an engagement. Every taxpayer's situation is
different, and the rules in the skill may not match your specific facts.

To speak with one of the licensed accountants who verifies skills for your
jurisdiction — no liability on either side until you and the accountant sign
a formal engagement letter — book a free 30-minute call:

→ [Book a call](https://calendly.com/openaccountants-info/30min)

We'll route you to the named verifier covering your country or state. You can
also see the full list of verified accountants at
[openaccountants.com/network](https://openaccountants.com/network).

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
