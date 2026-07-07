---
name: qc-corporate-tax-co17
description: "Use this skill whenever asked about Quebec corporate income tax. Quebec administers its own CIT (separate from federal T2) via the CO-17 return filed with Revenu Québec under the Quebec Taxation Act (Loi sur les impôts, RLRQ c. I-3). Trigger on phrases like \"Quebec CIT\", \"CO-17\", \"QC corporate tax\", \"Quebec small business deduction SBD\", \"Quebec tax credits R&D Quebec\", \"C3i credit\", \"C3I investment credit\", \"Crédit d'impôt à l'investissement et l'innovation\", \"Revenu Québec corporate\", \"déclaration de revenus des sociétés\", \"Quebec corporate instalments\", \"taxable income earned in Quebec\", \"TIEQ\", \"Quebec allocation\", \"Quebec compensation tax financial institutions\", \"Quebec CCPC rate\", or \"Quebec 5500 hour test\". Covers the 11.5% Quebec general CIT rate under Section 771 of the Quebec Taxation Act (combined with federal 15% = 26.5% combined), the Quebec Small Business Deduction (SBD) reducing the rate to 3.2% on the first $500,000 of active business income for Canadian-Controlled Private Corporations (CCPC) subject to the 5,500 paid-hours test under Section 771.1, the C3i credit (Crédit d'impôt à l'investissement et l'innovation) for qualified property at rates of 20-40% depending on territorial zone (high-economic-vitality vs. intermediate vs. low-economic-vitality regions), the Quebec R&D tax credit stack on top of federal SR&ED, and the CO-17 filing mechanics including 6-month filing deadline, 2-month payment deadline, instalment regime, and coordination with the federal T2 return. Out of scope: federal T2 corporate tax (use canada-corporate-tax-t2), Quebec personal income tax TP-1 (use qc-individual-return), Quebec QST (use qc-qst-return), Quebec compensation tax on financial institutions, mining duties under the Mining Tax Act, Quebec source deductions and employer contributions (TPZ-1015), insurance premium tax, logging tax, and specialised sector regimes (cooperatives, mutual funds, insurance corporations). ALWAYS read this skill alongside canada-formation and the federal CIT files (canada-corporate-tax-t2) — Quebec CIT is computed in parallel with, not as a substitute for, federal CIT."
jurisdiction: CA
domain: corporate-tax
tax_year: 2025
tier: 2
last_updated: 2026-07-06
---

# qc-corporate-tax-co17

## Quebec — Corporate Income Tax (CO-17) — Skill v1.0

Produced by OpenAccountants (openaccountants.com)

This skill is for informational purposes only and does not constitute tax, legal, or financial advice. All outputs must be reviewed and signed off by a qualified Quebec tax adviser (CPA auditeur or CPA with Quebec corporate tax expertise, or a tax lawyer admitted to the Barreau du Québec with corporate tax specialisation) before filing or acting upon. Quebec administers its CIT separately from the federal government — the CRA does not collect Quebec corporate tax. The latest verified version of this skill is maintained at openaccountants.com.

## Section 1 — Quick Reference

**Quick Reference table**

| Field | Value |
| --- | --- |
| Province | Quebec (Québec) |
| Tax | Corporate Income Tax — Impôt sur le revenu des sociétés |
| Currency | CAD |
| Tax authority | **Revenu Québec** (Agence du revenu du Québec — ARQ) |
| Primary legislation | **Loi sur les impôts, RLRQ c. I-3** (Quebec Taxation Act, "QTA") |
| Companion administration Act | **Loi sur l'administration fiscale, RLRQ c. A-6.002** (Tax Administration Act) |
| Federal interaction | **Separate return** — Quebec does NOT join the federal T2 collection agreement. A corporation with a permanent establishment in Quebec files both the federal T2 (with CRA) and the **CO-17** (with Revenu Québec). |
| **Quebec general CIT rate** | **11.5%** of taxable income earned in Quebec (Section 771 QTA) — combined with federal 15% net rate = **26.5% combined** general rate |
| **Quebec Small Business Deduction (SBD) rate** | **3.2%** on the first **$500,000** of active business income for CCPCs that pass the **paid-hours test** — combined with federal 9% small-business rate = **12.2% combined** small-business rate |
| **SBD paid-hours threshold (full rate)** | **≥ 5,500 paid hours** in the taxation year (or preceding year) — Section 771.1 QTA |
| **SBD paid-hours phase-out** | Linear reduction between **5,000 and 5,500** paid hours; **no SBD if < 5,000 hours** (with limited exception for primary-sector and manufacturing activities) |
| **SBD business limit** | **$500,000** — aligned with federal small-business limit; reduced if taxable capital employed in Canada is between $10M and $50M (parallel to federal grind) |
| **C3i credit rate (high-vitality zones)** | **20%** of qualified investment in qualified property (e.g., Montreal, Quebec City urban areas) |
| **C3i credit rate (intermediate zones)** | **30%** of qualified investment |
| **C3i credit rate (low-vitality / resource regions)** | **40%** of qualified investment (e.g., Gaspésie–Îles-de-la-Madeleine, Bas-Saint-Laurent, Côte-Nord, Nord-du-Québec, Saguenay–Lac-Saint-Jean designated portions) |
| **C3i credit refundability** | Fully **refundable** for CCPCs with assets ≤ $50M; partially refundable on a sliding scale up to $100M; **non-refundable** above $100M |
| **R&D credit (Quebec)** | Quebec stacks on top of the federal SR&ED ITC. Refundable for CCPCs. Multiple components: salaries (general rate up to **30%** for SMEs sliding to 14% for large), university / public research contracts, private partnership pre-competitive research, fees paid to eligible research consortia |
| **Capital gains inclusion** | 50% for gains realised on or before 24 June 2024; 66.67% thereafter — Quebec **harmonised** with the federal change announced in the 2024 federal Budget and confirmed in the Quebec 2024–25 Information Bulletins |
| **Compensation tax on financial institutions** | Separate tax under Title IV.1.1 QTA (out of scope of this skill) |
| **Allocation of taxable income** | "Taxable income earned in Quebec" (TIEQ) — based on the **two-factor formula** (50% wages + 50% gross revenue from a Quebec PE) — Section 771R QTA and Regulation 771R |
| **Annual return** | **Form CO-17 — Déclaration de revenus des sociétés** |
| **CO-17 filing deadline** | **6 months** after the end of the taxation year (parallel to federal T2 — Section 1000 QTA) |
| **Payment deadline (balance due)** | **2 months** after year-end for general corporations; **3 months** for CCPCs claiming the SBD and meeting the federal CCPC payment-extension criteria (Section 1027 QTA — harmonised with federal Section 157(1)(b) ITA) |
| **Instalments — frequency** | **Monthly** by default; **quarterly** for "eligible CCPCs" parallel to federal Section 157(1.1)–(1.5) ITA |
| **Instalment due date** | Last day of each month (or quarter) |
| **NEQ — Enterprise Number** | Quebec Enterprise Number — registration via the **Registraire des entreprises du Québec** required for all corporations with a Quebec PE |
| **Late filing penalty** | Minimum penalty regime under Sections 1045, 1049 QTA — generally 5% of unpaid tax plus 1% per month up to 12 months (parallel to federal Section 162(1)) |
| **Statute of limitations (reassessment)** | **3 years** from the original notice of assessment for CCPCs; **4 years** for other corporations (Section 1010 QTA) — extended for misrepresentation or neglect |
| Skill version | 1.0 |
| Validated by | Live status: https://openaccountants.com/skills/qc-corporate-tax-co17 |

### 1.1 Conservative Defaults (Snapshot)

**Conservative Defaults Snapshot table**

| Ambiguity | Default |
| --- | --- |
| Quebec PE existence unclear | Assume PE exists if any employee, office, fixed place, agent with contracting authority, or substantial equipment in Quebec — Section 12 QTA |
| TIEQ allocation factors unclear | Allocate 100% to Quebec if any doubt about the second-province factor; never under-allocate to Quebec |
| SBD paid-hours unclear | Default to NO SBD (apply 11.5% general rate) until time-tracking records confirm ≥ 5,500 hours |
| CCPC status unclear | Default to non-CCPC (no SBD); confirm with federal T2 CCPC determination first |
| C3i zone classification unclear | Default to 20% high-vitality rate (lowest) until zone confirmed against Annex II of the Taxation Act regulations |
| C3i property qualification unclear | Do not claim until qualified-property test confirmed against Section 1029.8.36.166.40 et seq. QTA |
| Refundability of credits unclear | Default to non-refundable treatment until taxable-capital threshold verified |
| Quebec R&D harmonised with federal SR&ED | Quebec rules are separate — never assume federal SR&ED qualification automatically qualifies for the Quebec credit |
| Capital gains inclusion rate (transitional 2024 year) | Apply 50% pre-25-June and 66.67% post-24-June **per the federal split** unless the proposed federal deferral changes the harmonised position |

## Section 2 — Required Inputs and Refusal Catalogue

### 2.1 Required Inputs

**Minimum viable**

- Signed statutory financial statements for the taxation year (typically ASPE Part II or IFRS).
- Prior-year CO-17 and prior-year federal T2 (Schedule 5 — Provincial Allocation).
- Confirmation of Quebec permanent establishment (address, employees, fixed place of business).
- Confirmation of CCPC status (control test from federal T2).
- For SBD claim: time-tracking records establishing paid hours by employee for the year and for the preceding year.

**Recommended**

- General ledger trial balance reconciled to financial statements.
- Federal T2 Schedule 5 (allocation of taxable income to provinces) — Quebec's TIEQ should reconcile to T2 Schedule 5 Quebec column with adjustments.
- Federal Schedule 1 (reconciliation of net income for tax purposes) — Quebec adopts the federal starting point with QTA-specific add-backs.
- Capital allowance schedule (Quebec generally harmonises with federal CCA classes but watch for non-harmonised items — see Section 3.7).
- C3i investment register (asset descriptions, acquisition dates, zone, qualified-property test documentation).
- Quebec R&D documentation: payroll allocation, contract research invoices, technical reports per Quebec rules.
- Instalment-payment history (Revenu Québec online services printout).
- NEQ confirmation from the Registraire des entreprises.

**Ideal**

- Audited financial statements.
- Transfer pricing local file if associated with non-resident parties (Quebec generally relies on federal Section 247 ITA but the Minister of Revenue may reassess under Section 421 QTA).
- Allocation-formula worksheet showing two-factor calculation per province.
- Documentation of any **inter-provincial corporate income tax planning** (Quebec is aggressive on income-shifting reassessments under Section 7.4 et seq. QTA — the general anti-avoidance rule).
- Prior Revenu Québec audit / verification correspondence.
- Prior-year Form CO-1029.8.36.II ("Demande de crédit C3i") confirmations.

**HARD STOP if minimum is missing.** Without statutory accounts and the prior-year CO-17 and T2 Schedule 5, no CO-17 computation may be produced.

### 2.2 Refusal Catalogue

- **R-QC-CT-1** — Non-Quebec PE. Section 12 QTA permanent-establishment test required first. Corporations without a Quebec PE do not file CO-17. Where PE existence is contested, escalate to a Quebec tax lawyer.  _(Section 12 QTA)_
- **R-QC-CT-2** — Compensation tax on financial institutions. Banks, insurance corporations, savings and credit unions and other "financial institutions" defined under Title IV.1.1 QTA file separate compensation-tax computations. Out of scope.  _(Title IV.1.1 QTA)_
- **R-QC-CT-3** — Mining and natural-resource regimes. Quebec mining duties under the Mining Tax Act (RLRQ c. I-0.4) and logging tax under Title IV QTA are separate from CO-17 CIT — out of scope.  _(Mining Tax Act (RLRQ c. I-0.4); Title IV QTA)_
- **R-QC-CT-4** — Cooperatives and mutual insurance. Tax-exempt cooperatives under Section 985 QTA, life-insurance corporations, and mutual fund corporations have specialised computations — out of scope.  _(Section 985 QTA)_
- **R-QC-CT-5** — Inter-provincial income shifting / Quebec GAAR. Section 1079.13.1 QTA general anti-avoidance rule and Section 7.4 et seq. recharacterisation rules apply aggressively to inter-provincial allocation planning. Do NOT advise on transactions that primarily shift TIEQ out of Quebec. Escalate to Quebec corporate tax counsel.  _(Section 1079.13.1 QTA; Section 7.4 et seq. QTA)_
- **R-QC-CT-6** — Cross-skill scope. Federal T2 → canada-corporate-tax-t2. Quebec personal income tax → qc-individual-return. Quebec sales tax (QST) → qc-qst-return. Quebec source deductions / employer contributions (RREGOP, FSS, RQAP) → separate skill. GST/HST → canada-gst-hst.
- **R-QC-CT-7** — Revenu Québec verification or audit. Active Revenu Québec audit, vérification, or objection — do not draft positions without engaged Quebec tax counsel or CPA representative under power of attorney (Form MR-69 — Procuration).  _(Form MR-69)_
- **R-QC-CT-8** — Continuance or amalgamation across jurisdictions. Corporate continuance into Quebec under the Business Corporations Act (RLRQ c. S-31.1) or amalgamations involving Quebec corporations have CO-17 short-year and acquisition-of-control consequences — escalate to specialist.  _(Business Corporations Act (RLRQ c. S-31.1))_
- **R-QC-CT-9** — Foreign-affiliate / FAPI Quebec layer. Quebec generally piggy-backs on federal FAPI inclusion but with separate computational quirks under Section 580 et seq. QTA. Specialist sign-off required.  _(Section 580 et seq. QTA)_

## Section 3 — Tier 1 Rules (Standard CO-17 Computation)

### 3.1 The 11.5% General CIT Rate — Section 771 QTA

- **Quebec general CIT rate** — 11.5% percent (applied to taxable income earned in Quebec (TIEQ))  _(Section 771(1) QTA)_
- **Quebec CIT (general) formula** — Quebec CIT (general) = 11.5% × TIEQ  _(Section 771(1) QTA)_
- **Combined federal + provincial rate (general)** — Federal net rate           15.00% Quebec general rate        11.50% ------ Combined general rate      26.50%  _(Section 771 QTA)_
- **Federal provincial abatement** — The federal general rate of 15% is the post-provincial-abatement rate. Quebec corporations claim the federal 10% provincial abatement under Section 124 ITA because Quebec is a non-agreement province.  _(Section 124 ITA)_

### 3.2 Quebec Small Business Deduction (SBD) — Section 771.1 QTA

- **SBD mechanism** — A Canadian-Controlled Private Corporation (CCPC) — as defined under federal Section 125(7) ITA and incorporated by reference into the QTA — may claim a deduction reducing the Quebec CIT rate on its active business income (ABI) earned in Quebec, up to the $500,000 business limit, from 11.5% down to 3.2%.  _(Section 771.1 QTA; federal Section 125(7) ITA)_
- **Quebec CIT (SBD rate) formula** — Quebec CIT (SBD rate) = 3.2% × min(ABI in Quebec, $500,000 × SBD entitlement %)  _(Section 771.1 QTA)_
- **Combined federal + provincial rate (SBD)** — Federal small-business rate    9.00% Quebec SBD rate                3.20% ------ Combined SBD rate             12.20%  _(Section 771.1 QTA)_

#### 3.2.1 Paid-Hours Test — the Quebec-Specific Restriction

**Paid-Hours Test table**

| Paid hours in year (or preceding year) | SBD entitlement |
| --- | --- |
| **≥ 5,500 hours** | **Full SBD** — rate reduces to 3.2% |
| 5,000 — 5,500 hours | **Linear phase-down** — entitlement reduced proportionally |
| **< 5,000 hours** | **NO SBD** — full 11.5% rate applies (with primary-sector / manufacturing exception below) |

- **Phase-out formula** — SBD entitlement % = (Paid hours − 5,000) / 500   (capped at 100%) = 0 if paid hours ≤ 5,000 = 100% if paid hours ≥ 5,500  _(Section 771.1 QTA)_
- **Counting paid hours** — Each employee's paid hours for the year (including paid leave) count. Hours of shareholder-employees count subject to a maximum 40 hours/week per shareholder (anti-abuse). Hours from sub-contractors do NOT count. Hours for the preceding taxation year may be used in lieu (so a new corporation does not lose SBD in its first year if it ramps up in year 2 — but year-1 itself defaults to no SBD unless the test is met in the year).  _(Section 771.1 paragraph c QTA)_
- **Primary-sector and manufacturing exception** — Corporations whose proportion of activities in the primary sector (agriculture, fishing, forestry) or manufacturing-and-processing exceeds 50% may claim the SBD without satisfying the paid-hours test, but at a reduced rate scaled to the sector proportion. Reviewer must verify the activity-sector classification.  _(Section 771.1(2.1) QTA)_

#### 3.2.2 Taxable-Capital Grind on the Business Limit

- **Taxable-capital grind** — Parallel to federal Section 125(5.1) ITA, the $500,000 business limit is reduced where the taxable capital employed in Canada of the CCPC (and associated corporations) is between $10 million and $50 million, with full elimination above $50M. Quebec adopts the same grind through Section 771.2.1.4 QTA cross-referencing the federal computation.  _(Section 771.2.1.4 QTA; federal Section 125(5.1) ITA)_
- **Reduced business limit formula** — Reduced business limit = $500,000 − [$500,000 × (Taxable capital − $10M) / $40M]  _(Section 771.2.1.4 QTA)_

#### 3.2.3 Associated-Corporation Allocation

- **Associated-corporation allocation** — The $500,000 business limit must be shared among associated corporations (Section 1138 et seq. QTA — associated-corporation rules — parallel to federal Section 256 ITA). A Quebec-specific allocation agreement (Form CO-771.1.3) must be filed when associated corporations share the limit.  _(Section 1138 et seq. QTA; federal Section 256 ITA)_

### 3.3 Taxable Income Earned in Quebec (TIEQ) — Section 771R QTA and Regulation 771R

- **Two-factor formula** — TIEQ = Total taxable income × Quebec allocation factor Quebec allocation factor = ½ × (Wages Quebec / Total wages) + ½ × (Gross revenue from Quebec PE / Total gross revenue)  _(Section 771R QTA and Regulation 771R)_
- **Two-factor specifics** — Wages factor: Salaries, wages, and other remuneration paid to employees of the Quebec PE during the year. Includes paid commissions but excludes payments to sub-contractors. Gross revenue factor: Gross revenue reasonably attributable to the Quebec PE — generally based on the customer location for sales of goods, location of services performed for services, and location of the borrower for interest (with specific carve-outs in Regulation 771R).  _(Regulation 771R)_
- **No-Quebec-PE-corporation** — If the corporation has no Quebec PE, TIEQ = 0 and no CO-17 is filed (subject to NEQ-registration consequences which may exist independently).
- **Single-PE corporation** — If 100% of activity is in Quebec, TIEQ = total federal taxable income (no allocation).
- **Multi-jurisdiction corporation** — Reconcile with federal T2 Schedule 5 (Allocation of Taxable Income to Provinces and Territories). Quebec uses the same two-factor formula as the federal Schedule 5 allocation but enforces its own audit standard for the Quebec figures.
- **Conservative default — allocation** — Where the allocation factors are uncertain, allocate 100% to Quebec (no under-allocation). The Quebec GAAR (Section 1079.13.1) and the Minister's broad discretion under Section 421 QTA make under-allocation a high-risk position.  _(Section 1079.13.1 QTA; Section 421 QTA)_

### 3.4 Starting Point — Federal Taxable Income with QTA Adjustments

**QTA adjustments table**

| Adjustment direction | Common items |
| --- | --- |
| Add to federal taxable income | Federal CCA exceeding Quebec CCA (limited cases of non-harmonisation); federal deductions not allowed by Quebec (e.g., portion of federal R&D ITC additions that Quebec computes differently); federal items the QTA explicitly does not adopt |
| Subtract from federal taxable income | Quebec-only deductions (e.g., the Quebec-only deduction for foreign specialists under Section 737.18.6 QTA, the deduction for foreign researchers, the IFC deduction for international financial centres — all out of scope for Tier 1) |
| Allocate via TIEQ factor | The adjusted taxable income is allocated to Quebec via the two-factor formula in 3.3 |

### 3.5 Capital Gains Inclusion — Harmonised with Federal

**Capital Gains Inclusion table**  _(Information Bulletins 2024-7, 2024-9)_

| Period | Inclusion rate |
| --- | --- |
| Gains realised on or before 24 June 2024 | **50%** |
| Gains realised after 24 June 2024 | **66.67%** |

- **Important uncertainty (2025)** — The federal government deferred and ultimately did not legislate the 66.67% rate before Parliament was prorogued. The CRA administrative position revised in early 2025 reverted to 50%. Quebec's harmonisation position is contingent on federal legislation — reviewer must verify the final harmonised position at the time of filing. Information Bulletin updates supersede this skill on this point.
- **Conservative default — capital gains** — Apply the 50% inclusion rate for all gains pending final legislative outcome, with explicit reviewer note on potential top-up.

### 3.6 Refundable Dividend Tax (RDTOH / GRIP / LRIP — Quebec Mechanics)

- **RDTOH harmonisation** — Quebec harmonises with the federal RDTOH (Refundable Dividend Tax on Hand) and dividend refund mechanics under Sections 1106–1106.11 QTA. The integration rates differ slightly because Quebec dividends are taxed at provincial individual rates, but the corporate-level mechanics mirror federal Section 129 ITA.  _(Sections 1106–1106.11 QTA; federal Section 129 ITA)_
- **Quebec dividend refund (IMRTD)** — A private corporation that pays taxable dividends receives a refund of its previously paid Quebec Part-IV-equivalent tax. Quebec does NOT have a separate Part IV tax — the federal Part IV applies — but Quebec has a parallel "impôt en main remboursable au titre de dividendes" (IMRTD) computation aligned with federal RDTOH-eligible / non-eligible split (since the federal 2018 split).  _(Section 1106 QTA)_
- **Conservative default — IMRTD** — Reconcile Quebec IMRTD beginning balance to federal RDTOH eligible/non-eligible balances; flag any discrepancy.

### 3.7 Capital Cost Allowance — Generally Harmonised

- **CCA harmonisation and non-harmonised items** — Quebec generally adopts the federal CCA classes and rates by reference in Section 130 et seq. QTA. Non-harmonised items include: Quebec-specific accelerated depreciation for certain manufacturing and IT equipment in low-vitality regions (Sections 130R and following of the Regulation). Federal Accelerated Investment Incentive (AII) — Quebec harmonised effective for property acquired after 20 March 2018; same phase-out schedule. Federal immediate expensing for CCPCs (Section 1100(0.1) ITR) — Quebec harmonised within $1.5M annual cap. Bonus depreciation interactions with the C3i credit (Section 3.8 below) require careful CCA-base reduction tracking.  _(Section 130 et seq. QTA)_

### 3.8 C3i Credit (Crédit d'impôt à l'investissement et l'innovation) — Section 1029.8.36.166.40 et seq. QTA

The C3i is the principal Quebec refundable investment credit, designed to encourage capital investment outside the Montreal–Quebec City corridor. It replaced the older "Crédit d'impôt à l'investissement" (CII) regime in 2020 and was extended (Bulletin 2024-9) to property acquired before 1 January 2030.

#### 3.8.1 Qualified Property

- **Qualified property list** — Qualified property includes: Manufacturing and processing equipment (Class 53 federally). Computer hardware and certain software (Class 50). Ore-processing equipment. Equipment used in the processing of green hydrogen, biofuels, and other clean-energy applications (added by recent Information Bulletins). Property must be new (or used but never previously used for an income-earning purpose by a Quebec-related party). Property must be used principally in Quebec in the course of carrying on a business.  _(Section 1029.8.36.166.40 et seq. QTA)_

#### 3.8.2 Credit Rates by Territorial Zone

**Credit Rates by Territorial Zone table**  _(Annex II of the QTA regulations)_

| Zone | Examples | Credit rate |
| --- | --- | --- |
| **High-economic-vitality zone** | Greater Montreal CMA, Greater Quebec City CMA | **20%** |
| **Intermediate zone** | Most regions outside the two CMAs but not designated as low-vitality | **30%** |
| **Low-economic-vitality / resource zones** | Designated portions of Gaspésie–Îles-de-la-Madeleine, Bas-Saint-Laurent, Côte-Nord, Nord-du-Québec, Saguenay–Lac-Saint-Jean, designated RCMs of Outaouais, Mauricie, Abitibi-Témiscamingue | **40%** |

#### 3.8.3 Excluded Threshold and Cumulative Limit

- **Excluded threshold** — $5,000 per asset CAD (does not qualify)  _(Section 1029.8.36.166.43 QTA)_
- **Cumulative limit** — $100 million CAD (per qualified-property over any 5-year period across associated corporations)

#### 3.8.4 Refundability — Sliding Scale

**Refundability Sliding Scale table**

| Total assets (corporation + associated) | Refundability |
| --- | --- |
| ≤ $50 million | **Fully refundable** |
| $50M — $100M | **Sliding-scale refundability** (linear) |
| > $100 million | **Non-refundable** — can only be applied against Quebec CIT, with 20-year carry-forward and 3-year carry-back |

#### 3.8.5 CCA Base Reduction

- **CCA base reduction** — The C3i credit reduces the CCA base of the qualified property under Section 130R134 of the Regulation (parallel to federal Section 13(7.1) ITR for investment tax credits).  _(Section 130R134 of the Regulation; federal Section 13(7.1) ITR)_

#### 3.8.6 Filing — Form CO-1029.8.36.II

- **Filing requirement** — The C3i is claimed via Form CO-1029.8.36.II filed with the CO-17. Supporting documentation includes the qualified-property asset register, zone verification, and proof of "principal use" in Quebec.  _(Form CO-1029.8.36.II)_
- **Conservative default — C3i claim** — Do not claim C3i without (i) the property-acquisition invoice on file, (ii) zone verification against the Annex II list current at the date of acquisition, and (iii) confirmation the property is used principally (> 50%) in Quebec in the course of a business.

### 3.9 Quebec R&D Tax Credits — Stack on Top of Federal SR&ED

Quebec maintains a parallel R&D credit regime that stacks on top of the federal Scientific Research and Experimental Development (SR&ED) Investment Tax Credit. Quebec's regime is significantly more complex than the federal regime.

#### 3.9.1 Core Salary Component — Section 1029.7 et seq. QTA

**Core Salary Component table**  _(Section 1029.7 et seq. QTA)_

| Component | Rate (CCPC SMEs) | Rate (large corporations) |
| --- | --- | --- |
| In-house R&D salaries (general) | **Sliding 30% → 14%** based on assets (≤$50M → ≥$75M) | **14%** |
| Subcontracted R&D (eligible subcontractor) | Same rate as above on 50% of contract value | Same |

#### 3.9.2 University and Public Research Contracts — Section 1029.8.1 QTA

- **University / public research contract credit** — 30% (CCPC SMEs) or 14% (large corporations) percent (payments to an eligible university entity or eligible public research centre)  _(Section 1029.8.1 QTA)_

#### 3.9.3 Private Pre-Competitive Research Partnerships — Section 1029.8.6 QTA

- **Pre-competitive research partnership credit** — 30% / 14% percent (payments under a recognised pre-competitive research partnership between two or more unrelated taxpayers)  _(Section 1029.8.6 QTA)_

#### 3.9.4 Fees to Eligible Research Consortia — Section 1029.8.9 QTA

- **Research consortia fee credit** — generally 30% / 14% percent (fees paid to an eligible research consortium (e.g., MITACS, certain CRIAQ programs))  _(Section 1029.8.9 QTA)_

#### 3.9.5 Refundability and Federal Stacking

- **Refundability and stacking** — For CCPC SMEs, the Quebec R&D credit is fully refundable even if exceeding tax payable. Federal SR&ED ITC and Quebec R&D credit are both claimed — Quebec credit reduces the SR&ED expenditure base on the federal computation (Section 127(18) ITA reduces the federal ITC base by government assistance, and the Quebec credit is treated as government assistance). Net combined Quebec + federal benefit on a $100,000 R&D salary spend for a CCPC SME can approach 50%+ depending on activity classification.  _(Section 127(18) ITA)_
- **Conservative default — Quebec R&D claim** — Do not claim Quebec R&D credits without (i) federal SR&ED filing prepared and reviewed first (Quebec follows federal qualification heavily), (ii) contemporaneous technical narrative meeting both federal and Quebec audit-readiness standards, and (iii) project-by-project allocation between salary, subcontract, university, and consortium components.

### 3.10 Computation Template — CO-17 Bottom Line

**Computation Template table**

| Step | Item |
| --- | --- |
| 1 | Federal taxable income (from T2 Schedule 1) |
| 2 | Quebec-specific adjustments (Section 3.4) → Adjusted taxable income |
| 3 | TIEQ = Adjusted taxable income × Quebec allocation factor (two-factor formula, Section 3.3) |
| 4 | Apply 11.5% general rate to TIEQ |
| 5 | Compute SBD deduction (3.2% rate on first $500K of ABI in Quebec, subject to paid-hours test, taxable-capital grind, associated-corporation sharing) |
| 6 | Compute C3i credit (Form CO-1029.8.36.II) — apply zone rate to qualified investment, subject to $5K threshold and cumulative limit |
| 7 | Compute Quebec R&D credits (per component) — adjust federal SR&ED base for Quebec credit treated as government assistance |
| 8 | Apply other credits (foreign tax credit Section 772 QTA, investment tax credits carried forward, etc.) |
| 9 | Compute IMRTD beginning, additions, dividend refund — reconcile to federal RDTOH |
| 10 | Determine balance due / refund, instalment-deficiency interest (Section 1037 QTA), penalties |

## Section 4 — Deductible and Non-Deductible Expenses (Quebec-Specific)

### 4.1 General Deductibility — Section 128 QTA

- **General deductibility starting point** — Quebec generally adopts the federal "income from a business" computation under Sections 9–37 ITA via Sections 128–168 QTA. The starting point is therefore the federal Schedule 1 reconciliation.  _(Sections 128–168 QTA; federal Sections 9–37 ITA)_

### 4.2 Quebec Non-Deductible / Restricted Items

**Quebec Non-Deductible / Restricted Items table**

| Item | Reference / Notes |
| --- | --- |
| **50% of meals and entertainment** | Federal 50% applies. Quebec adds a **further restriction** capping deductibility at a percentage of gross revenue (Section 421.1 QTA — 1.25% of sales for sales below $32,500; 2% on sales $32,500–$51,999; 1.25% for $52,000+ — see Annex of Section 421.1 for the sliding scale). Reviewer must apply the additional cap. |
| **Membership dues** | Quebec generally aligns with federal restriction (Section 421 QTA) — recreational club dues non-deductible. |
| **Penalties and fines** | Non-deductible per Section 144 QTA (parallel to federal Section 67.6 ITA). |
| **Bottle-deposit and certain environmental contributions** | Treatment matches federal — generally deductible when paid. |
| **Gifts to officers / shareholders** | Distribution recharacterisation risk under Section 111 QTA (parallel to federal Section 15 / 246 ITA shareholder-benefit rules). |
| **Excessive shareholder remuneration** | Quebec applies Sections 420–422 QTA reasonableness test — parallel to federal Section 67 ITA. |

### 4.3 Quebec-Only Deductions (Out of Tier 1)

**Quebec-Only Deductions table**

| Deduction | Reference | Notes |
| --- | --- | --- |
| Foreign specialist tax holiday | Section 737.18.6 QTA | 5-year graduated deduction for foreign-specialist remuneration |
| Foreign researcher | Section 737.18.14 QTA | Similar to specialist regime |
| International Financial Centre (IFC) | Section 771.1.1 QTA | Specialised regime for qualified IFC corporations in Montreal |
| Tax holiday for large investment projects (LIP) | Section 737.18.17 et seq. QTA | Up to 15-year tax holiday for projects ≥ $100M qualifying investment |

These regimes require specialist sign-off — out of scope for Tier 1.

## Section 5 — Tier 2 Catalogue (Reviewer Judgement Required)

### 5.1 Allocation-Formula Audit Exposure

- **Allocation audit exposure** — Revenu Québec is historically aggressive on TIEQ allocation reassessments — particularly on the wages factor (related-party payroll arrangements, employees travelling between provinces, secondments) and on the gross-revenue factor (services rendered partly inside and outside Quebec, royalty allocation, software licensing source). Reviewer must scrutinise the federal Schedule 5 numbers against the Quebec allocation evidence.

### 5.2 Quebec GAAR — Section 1079.13.1 QTA

- **Quebec GAAR** — Quebec's general anti-avoidance rule mirrors federal Section 245 ITA but is administered with a notably broader interpretation, especially against inter-provincial income shifting. Reviewer must screen any transaction whose primary purpose is to reduce TIEQ.  _(Section 1079.13.1 QTA; federal Section 245 ITA)_

### 5.3 Acquisition-of-Control and Section 736.0.2 QTA

- **Acquisition-of-control rules** — Acquisition-of-control triggers loss-streaming and CCA-class restrictions parallel to federal Section 111(5) ITA. Quebec's separate filing requires a separate streaming computation, and short taxation years on AOC are common.  _(Section 736.0.2 QTA; federal Section 111(5) ITA)_

### 5.4 Associated-Corporation Designations — Sections 1138–1142 QTA

- **Associated-corporation designations** — The associated-corporation rules are critical for SBD limit-sharing and the C3i $100M cumulative limit. Reviewer must verify corporate structure annually because de-facto control tests (Section 1142.1 QTA — parallel to federal Section 256(5.1) ITA) are easily missed in informal structures.  _(Sections 1138–1142 QTA; Section 1142.1 QTA; federal Section 256(5.1) ITA)_

### 5.5 Foreign Tax Credit — Section 772 QTA

- **Foreign tax credit** — Quebec grants a separate foreign tax credit on the Quebec proportion of foreign-source income. The mechanics are parallel to but distinct from federal Section 126 ITA — reviewer should reconcile, not assume identity.  _(Section 772 QTA; federal Section 126 ITA)_

### 5.6 C3i Eligible Property — Borderline Cases

- **Borderline exclusions** — The qualified-property test (Section 1029.8.36.166.40 et seq.) excludes many borderline assets including: Buildings (excluded unless qualifying as M&P building, narrow category). Vehicles (most road vehicles excluded). Software developed in-house (specific exclusion — though acquired off-the-shelf software may qualify). Property leased to others (lessor-lessee rules in Section 1029.8.36.166.42 require careful analysis). Reviewer must verify each material asset against the qualified-property test.  _(Section 1029.8.36.166.40 et seq. QTA; Section 1029.8.36.166.42 QTA)_

### 5.7 Quebec Tax Holidays — LIP, Manufacturing Innovation, Tertiary R&D

Out of scope for Tier 1 — but flag for specialist engagement where the corporation appears to qualify (e.g., new project ≥ $100M, AI / quantum / aerospace cluster, designated science-park location).

## Section 6 — Worked Example

### 6.1 Montreal Tech CCPC — $2M Revenue, $400K Active Business Income

**Facts:**
- TechMTL Inc., incorporated in Quebec, head office and sole PE in Montreal.
- CCPC for federal purposes (confirmed on federal T2 Schedule 23).
- Taxation year ending 31 December 2025.
- Gross revenue: $2,000,000 (all Quebec sales).
- Net income for tax purposes (federal Schedule 1): $400,000 — all active business income.
- No non-Quebec PE; TIEQ = 100% of taxable income.
- Total wages: $700,000 paid to 8 full-time employees; total paid hours for the year: 15,200 (well above the 5,500 threshold).
- Taxable capital employed in Canada: $4M (below the $10M grind threshold — full SBD).
- No associated corporations.
- C3i: TechMTL acquired qualified manufacturing equipment costing $200,000 during the year, used principally at the Montreal facility (high-vitality zone → 20% rate). $5,000 excluded threshold applies per asset.
- Federal SR&ED qualifying expenditures: $80,000 (in-house salaries). Quebec R&D credit on the same $80,000 at 30% (CCPC SME rate, assets under $50M).

**Federal T2 (high-level reconciliation):**

```
Federal taxable income                      400,000
Federal general tax @ 38%                   152,000
Less: Federal abatement 10% × 400,000       (40,000)
Less: Federal SBD 19% × 400,000             (76,000)
                                            -------
Federal Part I tax                           36,000
Less: Federal SR&ED ITC 15% × 80,000        (12,000)
[refundable for CCPC SME]
                                            -------
Net federal CIT                              24,000
```

**Quebec CO-17 computation:**

```
Step 1 — Starting taxable income
Federal taxable income                            400,000
Quebec adjustments                                      0
                                                  -------
Adjusted taxable income                           400,000

Step 2 — TIEQ allocation
Quebec allocation factor = 100% (sole PE in QC)
TIEQ                                              400,000

Step 3 — Apply general rate
Quebec CIT @ 11.5% × 400,000                       46,000

Step 4 — Quebec SBD
Paid hours check: 15,200 ≥ 5,500    → full SBD
Active business income in Quebec:    400,000
Business limit (no grind, no
  associated corp sharing):          500,000
ABI subject to SBD:                  400,000
Rate reduction: 11.5% − 3.2% = 8.3%
SBD deduction = 8.3% × 400,000                    (33,200)
                                                  -------
Quebec CIT after SBD                               12,800
[Effective rate: 3.2% × 400,000 = 12,800 ✓]

Step 5 — C3i credit (Form CO-1029.8.36.II)
Qualified investment per asset:      200,000
Less: $5,000 exclusion threshold:     (5,000)
Eligible C3i base:                   195,000
Rate (high-vitality zone):              20%
C3i credit                                        (39,000)
[Fully refundable — TechMTL assets < $50M]

Step 6 — Quebec R&D credit
Eligible salaries:                    80,000
Adjustment: federal SR&ED ITC treated as
  government assistance reduces federal
  expenditure base (already in federal calc);
  Quebec applies its rate to the Quebec
  qualifying base — assume parallel $80,000.
Rate (CCPC SME, assets < $50M):         30%
Quebec R&D credit                                 (24,000)
[Fully refundable]
                                                  -------
Quebec CIT / (refund) before instalments         (50,200)

Combined federal + Quebec position
Federal Part I net tax                             24,000
Federal SR&ED refund          [already netted]
Quebec CIT (refund)                               (50,200)
                                                  -------
Net Canadian + Quebec tax (refund)                (26,200)
```

**Combined effective rate on $400,000 ABI before credits:**
```
Federal 9% + Quebec 3.2% = 12.2% × 400,000 = 48,800

Less credits:
  Federal SR&ED 12,000
  Quebec C3i      39,000
  Quebec R&D      24,000
                 -------
  Total credits   75,000
```

The credits exceed the combined CIT — TechMTL receives a net refund of $26,200 for the year (subject to instalment-deficiency interest if instalments were not paid on schedule; see Section 7).

**Filing:**
- Federal T2 with CRA by 30 June 2026 (6 months after FY-end).
- Quebec CO-17 with Revenu Québec by 30 June 2026 (6 months after FY-end).
- Payment of CO-17 balance: technically due 28 February 2026 (2 months after year-end) for non-SBD payment timing, or 31 March 2026 (3 months) for SBD-qualifying CCPCs — in this case TechMTL is refund-position so no payment due, but instalment reconciliation still applies.
- Form CO-1029.8.36.II (C3i) filed with the CO-17.
- Form CO-1029.7 (Quebec R&D salary credit) filed with the CO-17.

**Conservative default applied:** Figures illustrative; reviewer must confirm (i) actual paid-hours documentation, (ii) C3i qualified-property classification of the specific equipment acquired, (iii) zone confirmation against Annex II current at acquisition date, (iv) Quebec R&D qualification project-by-project matching federal SR&ED, (v) any associated-corporation status affecting business-limit sharing and C3i cumulative cap.

## Section 7 — Filing and Payment Mechanics

### 7.1 Form CO-17 via Revenu Québec Online Services

The CO-17 — Déclaration de revenus des sociétés is filed electronically through Mon dossier pour les entreprises (the Revenu Québec online portal) or via certified tax-preparation software (most Canadian tax software supports CO-17 alongside T2).

**Key panels table**

| Panel | Content |
| --- | --- |
| Identification | NEQ, name, fiscal year, address of principal Quebec PE |
| Allocation of taxable income | Two-factor formula computation; reconcile to federal Schedule 5 |
| Income tax computation | Federal taxable income, Quebec adjustments, TIEQ, rate application |
| Small Business Deduction | Paid-hours test, business limit, associated-corporation allocation |
| Refundable credits | C3i (CO-1029.8.36.II), R&D (CO-1029.7 / 1029.8.1 / 1029.8.6 / 1029.8.9), other |
| Non-refundable credits | Foreign tax credit (Section 772), carry-forward credits |
| Dividend refund / IMRTD | Section 1106 reconciliation |
| Instalments | Reconciliation of instalments paid with assessed liability |
| Balance due / refund | Final position |

### 7.2 Filing Deadline — Section 1000 QTA

**Filing Deadline table**  _(Section 1000 QTA)_

| Year-end | CO-17 filing deadline |
| --- | --- |
| 31 December 2025 | 30 June 2026 |
| 30 June 2026 | 31 December 2026 |
| Short year ending 15 April 2025 | 15 October 2025 |

- **6 months filing rule** — 6 months after the end of the taxation year. Parallel to federal T2.  _(Section 1000 QTA)_

### 7.3 Payment Deadline — Section 1027 QTA

- **Balance of CIT payment deadline** — Balance of CIT is due: 2 months after year-end for general corporations. 3 months after year-end for CCPCs that: Claimed the federal SBD in the year or preceding year, AND Taxable income in the year (with associated corporations) did not exceed the business limit, AND Met the federal Section 157(1)(b) ITA payment-extension criteria. The 3-month extension is harmonised with federal but Quebec applies its own verification.  _(Section 1027 QTA; federal Section 157(1)(b) ITA)_

#### 7.4.1 Threshold for Instalments

- **Instalment threshold** — > $3,000 CAD (Quebec CIT (and certain related Quebec taxes) for the current year or the immediately preceding year)  _(Sections 1025–1028 QTA)_

#### 7.4.2 Monthly Instalments (Default)

- **Monthly instalment amount** — Each monthly instalment = lower of: 1/12 of estimated current-year Quebec CIT; 1/12 of prior-year Quebec CIT (with safe-harbour reference to "second preceding year" for the first two months). Due: Last day of each month of the taxation year.  _(Sections 1025–1028 QTA)_

#### 7.4.3 Quarterly Instalments — "Eligible CCPCs"

- **Eligibility tests** — CCPC throughout the year. Claimed federal SBD in the year or preceding year. Taxable income (current and preceding year, with associated corporations) ≤ $500,000. Taxable capital (current and preceding year, with associated corporations) ≤ $10M. Perfect compliance history (no late filings / payments in past 12 months for designated taxes — Section 1025.1 QTA).  _(federal Section 157(1.1)–(1.5) ITA; Section 1025.1 QTA)_
- **Quarterly instalment amount** — Quarterly instalment = 1/4 of the safer of estimated current-year Quebec CIT or prior-year Quebec CIT. Due: Last day of each quarter (last days of months 3, 6, 9, 12 of the taxation year).

#### 7.4.4 Instalment-Deficiency Interest — Section 1037 QTA

- **Instalment-deficiency interest** — Interest at the prescribed rate (set quarterly by the Minister; for 2025 generally 8–10% per annum range, parallel to federal) applies to the difference between instalments actually paid and the lesser of estimated current-year or prior-year requirements, computed daily.  _(Section 1037 QTA)_
- **Substantial underpayment penalty** — Additional 50% surcharge on substantial instalment underpayments (Section 1045.2 QTA) where the underpayment exceeds prescribed limits.  _(Section 1045.2 QTA)_

### 7.5 Late Filing and Payment Penalties

**Late Filing and Payment Penalties table**

| Infraction | Penalty |
| --- | --- |
| Late filing of CO-17 | **5% of unpaid Quebec CIT** at filing deadline, plus **1% per full month late**, up to **12 months** — Section 1045 QTA |
| Repeat late filing (3rd offence in 3 years) | **10% + 2% per month up to 20 months** — Section 1045 QTA |
| Late payment of CIT | Interest at the prescribed rate (~8–10% in 2025), daily compounding — Section 28 Tax Administration Act |
| Failure to file Form CO-1029.8.36.II (C3i) on time | Credit denied — strict filing-deadline rule (often within 12 months of CO-17 filing deadline, but check current Section 1029.8.36.166.45 QTA wording) |
| Failure to file Form CO-1029.7 (Quebec R&D) on time | Credit denied — strict deadline parallel to federal SR&ED 18-month claim deadline under Section 37(11) ITA |
| Negligent return | Up to **50% of tax shortfall** under Section 1049 QTA |
| False statement / gross negligence | Up to **50% of tax avoided** under Section 1049.5 QTA |
| Deliberate default | Criminal prosecution under Section 62 et seq. Tax Administration Act |

### 7.6 Reassessment Period — Section 1010 QTA

**Reassessment Period table**  _(Section 1010 QTA)_

| Corporation type | Reassessment period |
| --- | --- |
| CCPC | **3 years** from notice of assessment |
| Other corporation | **4 years** from notice of assessment |
| Misrepresentation, neglect, carelessness, wilful default, or fraud | **No limit** (Section 1010(2)(a) QTA) |
| Transactions with non-arm's-length non-residents (transfer pricing) | **7 years** (Section 1010(2)(b) QTA — parallel to federal) |
| To claim a loss / credit carry-back | Extended periods per the specific carry-back rules |

### 7.7 Power of Attorney — Form MR-69

- **Form MR-69 requirement** — To represent a corporation before Revenu Québec, a tax professional must hold a signed Form MR-69 — Procuration, procuration concernant les renseignements fiscaux. The federal RC59 / AUT-01 is not sufficient for Quebec — MR-69 is separate and required.  _(Form MR-69)_

## Section 8 — Conservative Defaults Summary

**Conservative Defaults Summary table**

| Item | Default |
| --- | --- |
| Quebec PE existence unclear | Assume PE exists if any nexus indicator (Section 12 QTA) |
| TIEQ allocation uncertain | Allocate 100% to Quebec; never under-allocate |
| Paid-hours test for SBD | No SBD until ≥ 5,500 hours documented |
| CCPC status | Default to non-CCPC until federal T2 confirmed |
| C3i zone classification | Default to 20% high-vitality rate (most conservative) |
| C3i qualified-property test | Do not claim until line-item asset register matched to qualified-property categories |
| Refundability test | Default to non-refundable until taxable capital threshold confirmed |
| Quebec R&D | Do not claim without federal SR&ED filing first prepared |
| Capital gains inclusion rate transitional year | 50% until federal legislation finalises 66.67% |
| IMRTD beginning balance | Reconcile to federal RDTOH split (eligible / non-eligible) |
| Associated-corporation status | Default to associated if any common control, ownership, or de-facto influence — Section 1142.1 QTA |
| Meals and entertainment | Apply federal 50% AND Quebec sales-based cap (Section 421.1) |
| Foreign specialist / IFC / LIP regimes | Out of scope — escalate |
| Instalments | Pay on safer of prior-year or current-year estimate |
| Late filing | Never strategise — Section 1045 penalty is automatic |
| Power of attorney | Always file MR-69 before acting on behalf of a Quebec corporation |

## Section 9 — Coordination With Federal T2

Quebec CIT and federal CIT are computed on the same accounting starting point (financial statements → Schedule 1 reconciliation → taxable income) but filed separately with two separate authorities (Revenu Québec for CO-17; CRA for T2).

**Coordination With Federal T2 table**

| Concept | Federal (T2) | Quebec (CO-17) | Coordination point |
| --- | --- | --- | --- |
| Net income per accounts | Same | Same | Identical starting point |
| Schedule 1 adjustments | Federal Schedule 1 | CO-17 with Quebec-specific add-backs | Quebec generally adopts federal Schedule 1 by reference, with QTA-specific overrides |
| CCA / depreciation | Federal Schedule 8 | Quebec generally harmonised; some accelerated regional incentives | Reconcile any non-harmonised items |
| Taxable income | Federal Line 360 | Adjusted federal × Quebec allocation factor | Federal Schedule 5 column for Quebec ≈ TIEQ on CO-17 |
| Active business income | Federal Schedule 7 | Same definition by reference | Reconcile |
| CCPC status | Federal Schedule 23 / 49 | Same definition (Section 1117 QTA references federal 125(7) ITA) | Reconcile |
| Small business deduction | Federal 19% on first $500K → 9% net | Quebec 3.2% on first $500K subject to paid-hours test | Quebec adds paid-hours layer |
| RDTOH | Federal eligible / non-eligible RDTOH | Quebec IMRTD eligible / non-eligible | Reconcile beginning balances; track refunds separately |
| Foreign tax credit | Section 126 ITA | Section 772 QTA | Parallel but separate computations |
| R&D | Federal SR&ED ITC (Section 127.1 ITA) | Quebec R&D credits (multiple sections, see 3.9) | Both claimed; Quebec credit treated as government assistance reducing federal SR&ED base |
| Capital gains inclusion | 50% / 66.67% per federal final law | Harmonised | Confirm at filing time |
| Filing deadline | 6 months after year-end | 6 months after year-end | Same |
| Payment deadline | 2 months (3 months for SBD CCPCs) | 2 months (3 months for SBD CCPCs) | Same |
| Reassessment period | 3 years CCPC / 4 years other | 3 years CCPC / 4 years other | Parallel — Section 152(3.1) ITA / Section 1010 QTA |
| Authorisation | RC59 / AUT-01 | **MR-69 (separate)** | Cannot rely on federal authorisation |

- **Reconciliation discipline** — Reviewer must reconcile the CO-17 to the federal T2 line-by-line on (i) taxable income, (ii) the provincial allocation (Schedule 5 Quebec column), (iii) SBD computation, and (iv) any credit interaction (federal SR&ED ↔ Quebec R&D; federal ITC ↔ C3i where applicable). Discrepancies trigger Revenu Québec / CRA exchange-of-information notices under the Quebec-Canada information sharing protocol.

## Section 10 — Cross-References

**Cross-References table**

| Topic | Skill |
| --- | --- |
| Federal Corporate Income Tax (T2) | `canada-corporate-tax-t2` |
| Canadian corporate formation | `canada-formation` |
| Quebec personal income tax (TP-1) | `qc-individual-return` |
| Quebec Sales Tax (QST / TVQ) | `qc-qst-return` |
| Federal GST/HST | `canada-gst-hst` |
| Foundation principles | `foundation` |
| Intake checklist | `intake` |

## Section 11 — Sources

Primary Legislation

- **Loi sur les impôts, RLRQ c. I-3 (Quebec Taxation Act, QTA)** — Consolidating Act for Quebec direct taxes.  _(Loi sur les impôts, RLRQ c. I-3)_
- **Section 12 QTA** — Permanent establishment definition.  _(Section 12 QTA)_
- **Section 128–168 QTA** — Computation of income from a business.  _(Section 128–168 QTA)_
- **Section 130 QTA** — CCA.  _(Section 130 QTA)_
- **Section 144 QTA** — Non-deductible penalties and fines.  _(Section 144 QTA)_
- **Section 421, 421.1 QTA** — Meals and entertainment, recreational dues.  _(Section 421, 421.1 QTA)_
- **Sections 580 et seq. QTA** — Foreign affiliates.  _(Sections 580 et seq. QTA)_
- **Section 736.0.2 QTA** — Acquisition of control.  _(Section 736.0.2 QTA)_
- **Section 737.18.6, 737.18.14, 737.18.17 QTA** — Foreign specialist, foreign researcher, large investment projects tax holidays.  _(Section 737.18.6, 737.18.14, 737.18.17 QTA)_
- **Section 771 QTA** — 11.5% percent (General corporate tax rate)  _(Section 771 QTA)_
- **Section 771.1 QTA** — Small Business Deduction (SBD) and paid-hours test.  _(Section 771.1 QTA)_
- **Section 771.2.1.4 QTA** — Business-limit grind on taxable capital.  _(Section 771.2.1.4 QTA)_
- **Section 771R / Regulation 771R** — TIEQ allocation formula.  _(Section 771R / Regulation 771R)_
- **Section 771.1.1 QTA** — IFC deduction.  _(Section 771.1.1 QTA)_
- **Section 772 QTA** — Foreign tax credit.  _(Section 772 QTA)_
- **Sections 1000–1010 QTA** — Return filing and reassessment.  _(Sections 1000–1010 QTA)_
- **Section 1010 QTA** — Reassessment period.  _(Section 1010 QTA)_
- **Sections 1025–1028 QTA** — Instalments.  _(Sections 1025–1028 QTA)_
- **Section 1027 QTA** — Balance due date.  _(Section 1027 QTA)_
- **Sections 1029.7 et seq. QTA** — Quebec R&D salary credit.  _(Sections 1029.7 et seq. QTA)_
- **Sections 1029.8.1, 1029.8.6, 1029.8.9 QTA** — Quebec R&D university / partnership / consortium credits.  _(Sections 1029.8.1, 1029.8.6, 1029.8.9 QTA)_
- **Sections 1029.8.36.166.40 et seq. QTA** — C3i (Crédit d'impôt à l'investissement et l'innovation).  _(Sections 1029.8.36.166.40 et seq. QTA)_
- **Sections 1037, 1045, 1045.2, 1049, 1049.5 QTA** — Interest and penalties.  _(Sections 1037, 1045, 1045.2, 1049, 1049.5 QTA)_
- **Section 1079.13.1 QTA** — Quebec general anti-avoidance rule.  _(Section 1079.13.1 QTA)_
- **Section 1106 QTA** — Dividend refund (IMRTD).  _(Section 1106 QTA)_
- **Sections 1117 et seq. QTA** — CCPC and private corporation definitions (cross-referenced to federal).  _(Sections 1117 et seq. QTA)_
- **Sections 1138–1142.1 QTA** — Associated corporations.  _(Sections 1138–1142.1 QTA)_
- **Section 28, Loi sur l'administration fiscale, RLRQ c. A-6.002** — Interest on late payment.  _(Section 28, Loi sur l'administration fiscale, RLRQ c. A-6.002)_
- **Sections 62 et seq., Loi sur l'administration fiscale, RLRQ c. A-6.002** — Penal provisions.  _(Sections 62 et seq., Loi sur l'administration fiscale, RLRQ c. A-6.002)_
- **Regulation respecting the Taxation Act, RLRQ c. I-3, r. 1** — Quebec CCA classes, allocation regulations (especially Regulation 771R), and Annex II (territorial zones for C3i).  _(Regulation respecting the Taxation Act, RLRQ c. I-3, r. 1)_

Income Tax Act, RSC 1985, c. 1 (5th Supp.) (ITA) — incorporated by reference at multiple points.

- **Section 9–37 ITA** — Income from a business (starting point).  _(Section 9–37 ITA)_
- **Section 13(7.1), Regulation 1100(0.1) ITA** — Accelerated/immediate expensing.  _(Section 13(7.1), Regulation 1100(0.1) ITA)_
- **Section 67.6 ITA** — Non-deductible penalties and fines.  _(Section 67.6 ITA)_
- **Section 125 ITA** — Federal Small Business Deduction.  _(Section 125 ITA)_
- **Section 126 ITA** — Federal foreign tax credit.  _(Section 126 ITA)_
- **Section 127.1 ITA** — Federal SR&ED ITC.  _(Section 127.1 ITA)_
- **Section 127(18) ITA** — Government assistance grinding ITC base.  _(Section 127(18) ITA)_
- **Section 129 ITA** — Refundable dividend tax (federal RDTOH).  _(Section 129 ITA)_
- **Section 157(1), 157(1.1)–(1.5) ITA** — Federal instalment and CCPC quarterly option.  _(Section 157(1), 157(1.1)–(1.5) ITA)_
- **Section 162(1) ITA** — Federal late-filing penalty.  _(Section 162(1) ITA)_
- **Section 245 ITA** — Federal GAAR.  _(Section 245 ITA)_
- **Section 247 ITA** — Transfer pricing.  _(Section 247 ITA)_
- **Section 256 ITA** — Associated corporations.  _(Section 256 ITA)_

Revenu Québec Bulletins and Information

- **Information Bulletin 2024-7 (June 2024)** — Harmonisation with federal capital gains inclusion rate increase.  _(Information Bulletin 2024-7 (June 2024))_
- **Information Bulletin 2024-9 (December 2024)** — C3i extension; capital gains update.  _(Information Bulletin 2024-9 (December 2024))_

Periodic Revenu Québec updates.

- **IN-417** — General Information Concerning the QST and GST/HST (cross-reference only).  _(IN-417)_
- **Guide to the Corporation Income Tax Return — IN-417.A** — Annual guide accompanying CO-17.  _(IN-417.A)_
- **IMP. 1029.8.36.166.40 et seq.** — Revenu Québec interpretation bulletins on C3i.  _(IMP. 1029.8.36.166.40 et seq.)_
- **IMP. 1029.7 et seq.** — Revenu Québec interpretation bulletins on Quebec R&D credit.  _(IMP. 1029.7 et seq.)_

Forms

- **CO-17** — Déclaration de revenus des sociétés (Corporation Income Tax Return).  _(CO-17)_
- **CO-17.SP** — Supplementary information schedules (multiple).  _(CO-17.SP)_
- **CO-771** — SBD computation (where required separately).  _(CO-771)_
- **CO-771.1.3** — Associated corporation business-limit allocation agreement.  _(CO-771.1.3)_
- **CO-1029.8.36.II** — Demande de crédit d'impôt à l'investissement et l'innovation (C3i).  _(CO-1029.8.36.II)_
- **CO-1029.7 / CO-1029.8.1 / CO-1029.8.6 / CO-1029.8.9** — Quebec R&D credit forms by component.  _(CO-1029.7 / CO-1029.8.1 / CO-1029.8.6 / CO-1029.8.9)_
- **MR-69** — Procuration (Power of Attorney for Revenu Québec).  _(MR-69)_
- **TPZ-1015.G** — Source deductions guide (cross-reference for payroll-employer obligations).  _(TPZ-1015.G)_

Other

- **Companies Act / Business Corporations Act (Quebec), RLRQ c. S-31.1** — Corporate-law framework.  _(Companies Act / Business Corporations Act (Quebec), RLRQ c. S-31.1)_
- **Registraire des entreprises du Québec (REQ)** — NEQ registration and annual updating declaration.  _(Registraire des entreprises du Québec (REQ))_
- **Quebec-Canada Information Exchange Protocol** — Bilateral data sharing on corporate returns.  _(Quebec-Canada Information Exchange Protocol)_

## PROHIBITIONS

- **11.5% Quebec rate territorial scope** — NEVER apply the 11.5% Quebec rate to income earned outside Quebec — use the TIEQ allocation formula.
- **SBD paid-hours test confirmation** — NEVER claim the Quebec SBD without confirming the 5,500 paid-hours test (or the primary-sector / manufacturing exception with documented activity proportion).
- **CCPC vs Quebec SBD entitlement** — NEVER assume the federal CCPC determination automatically secures Quebec SBD entitlement — the paid-hours test is additional.
- **TIEQ under-allocation risk** — NEVER under-allocate TIEQ to Quebec where the allocation factors are ambiguous — Quebec audits are aggressive.
- **C3i credit conditions** — NEVER claim the C3i credit without (i) qualified-property test, (ii) zone classification against Annex II current at acquisition date, (iii) principal-use-in-Quebec confirmation.
- **C3i excluded threshold per asset** — 5,000 CAD (Excluded threshold on first $5,000 of each asset for C3i credit)  _(PROHIBITIONS section (unsure of statutory citation))_
- **C3i and federal ITC stacking** — NEVER stack C3i and federal ITC on the same expenditure without confirming the federal Section 127(18) ITA government-assistance grind.  _(Section 127(18) ITA)_
- **Quebec R&D credits sequencing** — NEVER claim Quebec R&D credits without preparing the federal SR&ED claim first.
- **Meals and entertainment sales-revenue cap** — NEVER ignore the Quebec sales-revenue cap on meals and entertainment (Section 421.1) — apply on top of the federal 50%.  _(Section 421.1 QTA)_
- **Federal CCA vs Quebec CCA** — NEVER assume federal CCA is automatically Quebec CCA — verify any non-harmonised regional incentives.
- **Quebec foreign tax credit mechanics** — NEVER apply the Quebec foreign tax credit as if identical to the federal Section 126 ITA computation — Section 772 QTA has its own mechanics.  _(Section 772 QTA; Section 126 ITA)_
- **Associated-corporation analysis and de-facto control** — NEVER bypass the Quebec associated-corporation analysis — Section 1142.1 de-facto control catches informal structures.  _(Section 1142.1 QTA)_
- **Inter-provincial income shifting and GAAR** — NEVER plan inter-provincial income shifting to reduce TIEQ without flagging Quebec GAAR risk (Section 1079.13.1).  _(Section 1079.13.1 QTA)_
- **Late filing penalty** — NEVER file late — Section 1045 penalty (5% + 1% per month up to 12 months) is automatic.  _(Section 1045 QTA)_
- **C3i and Quebec R&D claim deadlines** — NEVER miss the 12-month claim window for C3i (Form CO-1029.8.36.II) or the parallel Quebec R&D claim deadlines — late claims are denied outright.  _(Form CO-1029.8.36.II)_
- **MR-69 requirement before Revenu Québec** — NEVER act before Revenu Québec without a signed MR-69 Procuration — federal RC59 is insufficient.  _(MR-69)_
- **RDTOH and IMRTD reconciliation** — NEVER assume RDTOH and IMRTD beginning balances reconcile — verify line-by-line.
- **Quebec tax holidays specialist sign-off** — NEVER advise on Quebec tax holidays (foreign specialist, IFC, LIP) without specialist sign-off.
- **Cross-jurisdictional GAAR/transfer-pricing positions** — NEVER apply Section 110 / Section 245-equivalent / Section 247-equivalent positions cross-jurisdictionally without engaged Quebec corporate tax counsel.
- **Figures as estimates pending sign-off** — NEVER present figures as definitive — always label as estimates pending CPA / Quebec tax adviser reviewer sign-off.

## Disclaimer

This skill and its outputs are for informational and computational purposes only and do not constitute tax, legal, or financial advice. All outputs must be reviewed and signed off by a qualified Quebec tax adviser (CPA auditeur with Quebec corporate tax experience, or a tax lawyer admitted to the Barreau du Québec with corporate tax specialisation) before filing or acting upon. Quebec administers its corporate income tax separately from the federal government — a corporation with a permanent establishment in Quebec must file both the federal T2 with the CRA and the CO-17 with Revenu Québec; these returns are not interchangeable, and reliance on one does not satisfy the other. The latest verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com).

## Talk to a verified accountant

This skill is a tool, not an engagement. Every taxpayer's situation is different, and the rules in the skill may not match your specific facts.

To speak with one of the licensed accountants who verifies skills for your jurisdiction — no liability on either side until you and the accountant sign a formal engagement letter — book a free 30-minute call:

→ [Book a call](https://calendly.com/openaccountants-info/30min)

We'll route you to the named verifier covering your country or state. You can also see the full list of verified accountants at [openaccountants.com/network](https://openaccountants.com/network).
