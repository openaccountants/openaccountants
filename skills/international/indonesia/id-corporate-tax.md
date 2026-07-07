---
name: id-corporate-tax
description: "Use this skill whenever asked about Indonesian corporate income tax (PPh Badan) for a resident Indonesian company (Perseroan Terbatas / PT). Trigger on phrases like \"Indonesia corporate tax\", \"PPh Badan\", \"SPT Tahunan 1771\", \"company tax Indonesia\", \"PT tax\", \"tarif PPh Badan\", \"small company facility 50%\", \"Pasal 31E\", \"PPh 25 installment\", \"tax holiday Indonesia\", \"tax allowance PP 78\", \"super deduction\", or \"transfer pricing Indonesia\". Covers the 22% standard rate (UU HPP), the Pasal 31E small-company facility (50% reduction on the slice of taxable income proportional to the first IDR 4.8 billion of turnover for companies with annual turnover ≤ IDR 50 billion), the Pasal 17(2b) listed-company 3% reduction, monthly PPh 25 installments, deductible vs non-deductible expenses under Pasal 6/9 UU PPh, fiscal reconciliation, depreciation under PMK 96/2009, tax incentives (tax holiday, tax allowance PP 78/2019, super-deduction R&D), transfer pricing documentation under PMK 213/2016 and PMK 172/2023, and SPT Tahunan 1771 filing via Coretax DJP. Out of scope: PPh Final UMKM 0.5% (use id-pph-final-umkm), employee payroll (use id-payroll-pph21), PPN/VAT (use indonesia-vat), permanent establishments / BUT, banking and insurance sector returns, oil/gas and mining contract regimes, Islamic finance, and consolidated/group returns. ALWAYS read this skill before touching any Indonesian corporate income tax work."
jurisdiction: ID
tax_year: 2025
reviewed_by: RILIA PUTRI
review_status: accountant-reviewed
tier: 1
last_updated: 2026-07-06
---

# id-corporate-tax

## Indonesia Corporate Income Tax (PPh Badan) Skill v1.0

> **Produced by OpenAccountants (openaccountants.com)**
>
> This skill is for informational purposes only and does not constitute tax, legal, or financial advice. All outputs must be reviewed and signed off by a licensed Indonesian tax consultant (Konsultan Pajak) before filing or acting upon.

## Verified rates & thresholds (accountant-reviewed)

> Reviewed against the cited tax authorities by **RILIA PUTRI** on 2026-06-03.
> Items flagged for further clarification are tracked separately and excluded here.
> This block is generated from verified `skill_facts` — edit the facts, not the prose.

### Corporate Tax (PPh Badan)

- **CIT rate** — 22% of Penghasilan Kena Pajak  _(UU PPh Art. 17(1)(b); UU HPP)_
- **Eligibility** — Annual turnover ≤ IDR 50,000,000,000  _(UU PPh Art. 31E)_
- **Mechanism** — 50% reduction of the prevailing corporate income tax rate applied proportionally to taxable income attributable to gross turnover up to IDR 4.8 billion  _(UU PPh Art. 31E; SE-02/PJ/2015)_
- **Turnover ≤ IDR 4.8B** — Reduced effective rate generally equals 11% on qualifying taxable income portion under Article 31E mechanism  _(UU PPh Art. 17(1)(b); UU PPh Art. 31E as amended by UU HPP No. 7/2021)_
- **Turnover IDR 4.8B–50B** — Mixed calculation generally applies: reduced effective rate on qualifying portion and standard 22% rate on the remaining taxable income  _(UU PPh Art. 31E as amended by UU HPP No. 7/2021; SE-02/PJ/2015)_
- **Turnover > IDR 50B** — Generally subject to the standard 22% corporate income tax rate without Article 31E facility  _(UU PPh Art. 17(1)(b); UU PPh Art. 31E; note: UU PPh as amended by UU HPP No. 7/2021)_
- **Automatic?** — Article 31E facility generally applies automatically where statutory eligibility requirements are satisfied  _(UU PPh Art. 31E; SE-02/PJ/2015)_
- **Rate** — 19% (3pp reduction)  _(UU PPh Art. 17(2b); PP 30/2020; PP 55/2022)_
- **Conditions** — ≥40% listed on IDX, ≥300 parties each <5%, ≥183 days, Form X.H.1-6 filed  _(UU PPh Art. 17(2b) as amended by UU HPP No. 7/2021; PP 30/2020; PP 55/2022; PMK 40/PMK.03/2023)_
- **Group I (computers, office)** — 4 years — SL 25% / DB 50%  _(UU PPh Art. 11; PMK 96/PMK.03/2009)_
- **Group II (vehicles, furniture)** — 8 years — SL 12.5% / DB 25%  _(UU PPh Art. 11; PMK 96/PMK.03/2009)_
- **Group III (heavy machinery)** — 16 years — SL 6.25% / DB 12.5%  _(UU PPh Art. 11; PMK 96/PMK.03/2009)_
- **Group IV (construction, ships)** — 20 years — SL 5% / DB 10%  _(UU PPh Art. 11; PMK 96/PMK.03/2009)_
- **Permanent buildings** — 20 years — SL 5% only  _(UU PPh Art. 11; PMK 96/PMK.03/2009)_
- **Non-permanent buildings** — 10 years — SL 10% only  _(UU PPh Art. 11; PMK 96/PMK.03/2009)_
- **Master File & Local File** — Required if turnover > IDR 50B, or RP tangible goods > IDR 20B, or RP services/interest/royalty > IDR 5B per category  _(PMK 172/2023; UU PPh Art. 18(3))_
- **CbCR** — Consolidated group revenue > IDR 11 trillion  _(PMK 172/2023; OECD CbCR framework)_
- **SPT 1771 (calendar year)** — Due no later than 4 months after fiscal year-end (generally 30 April for calendar-year taxpayers)  _(UU KUP Art. 3(3)(c) as amended by UU HPP)_
- **PPh 29 payment** — Before SPT is filed  _(UU KUP Art. 9(2); UU KUP Art. 3(5) as amended by UU HPP)_
- **Monthly PPh 25** — 15th of following month  _(UU PPh Art. 25; UU KUP as amended by UU HPP; PMK 81/2024 as amended by PMK 1/2026)_
- **Extension** — Up to 2 months  _(UU KUP Art. 3(4) as amended by UU HPP; PMK 81/2024)_
- **Late SPT 1771 filing** — IDR 1,000,000 fine  _(UU KUP Art. 7)_
- **Late PPh 25/29 payment** — Monthly interest per MoF rate (~2%/mo, max 24 months)  _(UU KUP Art. 9(2a) as amended by UU HPP; PMK 81/2024)_
- **Incorrect SPT (negligence)** — Up to 200% of shortfall  _(UU KUP Art. 13(3))_
- **Tax evasion** — 6mo–6yr imprisonment + 2×–4× shortfall  _(UU KUP Art. 39)_
- **Record retention** — 10 years  _(UU KUP Art. 28(11))_
- **Tax holiday — PMK 130/2020** — Eligible pioneer industries may obtain corporate income tax reduction facilities ranging from 50%–100% for certain investment periods subject to prevailing investment and tax incentive regulations  _(PMK 130/PMK.010/2020 as amended by PMK 69/2024)_
- **Tax allowance — PP 78/2019** — Eligible taxpayers investing in designated business sectors and/or regions may obtain income tax facilities including 30% investment allowance over 6 years, accelerated depreciation/amortization, reduced dividend withholding tax, and extended loss carry-forward  _(UU PPh Art. 31A; PP 78/2019; PMK 11/PMK.010/2020)_
- **Super-deduction R&D** — Additional gross income deduction of up to 300% for qualifying domestic R&D activities  _(PP 45/2019; PMK 153/PMK.010/2020)_
- **Super-deduction vocational** — Additional gross income deduction of up to 200% may be granted for qualifying vocational education, apprenticeship, and competency-based training activities conducted in Indonesia  _(PP 45/2019; PMK 128/PMK.010/2019)_
- **Bribery/gratuity — deductibility** — NEW provision per PP 20/2026 Article 20A: Expenditures in the form of bribes, gratuities, and other payments related to corruption or bribery offences — including payments to foreign public officials — are NOT deductible as business expenses for corporate taxpayers. Effective 22 April 2026. Introduced pursuant to OECD anti-bribery recommendations as part of Indonesia's OECD accession process.  _(PP 20/2026 Article I items 1 and 2)_

## Section 1 — Quick Reference

**Quick Reference table**

| Field | Value |
| --- | --- |
| Country | Indonesia (Republik Indonesia) |
| Tax | Corporate Income Tax — PPh Badan (Pajak Penghasilan Badan) |
| Currency | IDR (USD bookkeeping requires DJP permission) |
| Tax year | Calendar year by default; FY permitted with DJP approval (Pasal 28 UU KUP) |
| Primary legislation | UU 36/2008 (UU PPh) as amended by UU 7/2021 (HPP) and UU 11/2020 (Cipta Kerja) |
| Supporting regulations | PP 55/2022 (UMKM revision); PMK 213/2016 (TP-Doc); PMK 172/2023 (TP implementation); PP 78/2019 (tax allowance); PMK 130/2020 (tax holiday) |
| Standard rate | **22%** of taxable income (Pasal 17(1)(b) UU PPh, as amended by UU HPP) |
| Small-company facility | 50% reduction of 22% on the slice of taxable income proportional to the first IDR 4.8B of turnover, for companies with annual turnover ≤ IDR 50B (Pasal 31E). Effective rate on slice: **11%** |
| Listed-company reduction | Extra 3% (19% rate) for public companies meeting Pasal 17(2b) (≥ 40% listed, ≥ 300 parties each < 5%, ≥ 183 days) |
| Monthly installment | PPh 25 — 1/12 of preceding year's PPh Badan liability after credits |
| Annual return | SPT Tahunan PPh Badan — **Form 1771** |
| Annual deadline | Last day of the 4th month after fiscal year-end (**30 April** for calendar-year taxpayers) — Pasal 3(3) UU KUP |
| Payment deadline | Before SPT is filed; PPh 29 (annual underpayment) due before filing |
| Monthly PPh 25 deadline | 15th of the following month (payment); 20th of the following month (reporting if required) |
| Filing portal | **Coretax DJP** (from tax year 2025); previously DJP Online / e-Filing |
| Tax authority | DJP (Direktorat Jenderal Pajak — Directorate General of Taxes), Ministry of Finance |
| Bookkeeping retention | 10 years (Pasal 28(11) UU KUP) |
| Validated by | Pending — sign-off by a licensed Konsultan Pajak (USKP) |
| Skill version | 1.0 |

### 1.1 Conservative Defaults

**Conservative Defaults table**

| Ambiguity | Default |
| --- | --- |
| Turnover band unknown | > IDR 50B (no Pasal 31E facility) |
| 3M test unclear (*mendapatkan, menagih, memelihara*) | Not deductible |
| BIK status unknown | Deductible to company; taxable to recipient (PMK 66/2023) |
| Related-party status unknown | Treat as related |
| TP documentation status unknown | Required if revenue > IDR 50B (PMK 213/2016) |
| Listed-company status unknown | Private (no 3% Pasal 17(2b) reduction) |
| PPh Final UMKM election unknown | Standard PPh Badan (see id-pph-final-umkm) |
| Fixed-asset useful life unknown | PMK 96/2009 group rates |
| Asset purpose unclear | Non-deductible (private use) |

## Section 2 — Required Inputs and Refusal Catalogue

### 2.1 Required Inputs

**Minimum viable** — Full-year financial statements (income statement, balance sheet), prior-year SPT 1771, and confirmation of (i) turnover band, (ii) listed-company status, (iii) any tax incentive elections.

**Recommended** — General ledger, fixed-asset register, related-party transactions schedule, PPh 25 payment confirmations, Bukti Potong for PPh 21/22/23/26 credits, prior-year loss carry-forward schedule.

**Ideal** — Audited statements signed by an Akuntan Publik (KAP), complete fiscal reconciliation, Master/Local File/CbCR if thresholds met, NPWP and KSWP certificates, ratified RUPS minutes.

**HARD STOP if minimum is missing.** Without financial statements and the prior-year return, no corporate computation may be produced.

### 2.2 Refusal Catalogue

- **R-ID-CT-1** — Non-resident / Permanent Establishment (BUT). Resident PTs only. BUT under tax treaty attribution rules is out of scope. Escalate to a Konsultan Pajak.
- **R-ID-CT-2** — Sector-specific regimes. Banking, insurance, oil & gas (production sharing / cost recovery), mining contract of work, plantation contracts. Out of scope.
- **R-ID-CT-3** — Group / consolidated reporting. Out of scope.
- **R-ID-CT-4** — Tax holiday / super-deduction not yet granted. Apply incentives only after KMK / BKPM Decree is in hand. Otherwise compute at standard rate and flag the pending application.
- **R-ID-CT-5** — Arrears / SKPKB enforcement. Outstanding STP, SKPKB, SKPKBT, or active pemeriksaan. Pasal 9(2a) UU KUP monthly interest applies. Escalate immediately.
- **R-ID-CT-6** — TP controversy. Related-party disputes or active MAP/APA proceedings. Out of scope.
- **R-ID-CT-7** — Cross-skill scope. Payroll → `id-payroll-pph21`. VAT → `indonesia-vat`. PPh Final UMKM 0.5% → `id-pph-final-umkm`.
- **R-ID-CT-8** — Islamic finance (syariah banking, takaful). Specific PSAK Syariah and DJP rulings apply. Out of scope.

## Section 3 — Tier 1 Rules (Standard Computation)

### 3.1 The 22% Standard Rate

- **Standard corporate income tax rate** — PPh Badan = 22% × PKP  _(Pasal 17(1)(b) UU PPh, as amended by UU 7/2021 (HPP))_
- **22% standard rate context** — Standard corporate income tax rate: 22% of Penghasilan Kena Pajak. In force from fiscal year 2022 (reduced from 25% by UU 2/2020; confirmed by UU HPP).  _(Pasal 17(1)(b) UU PPh, as amended by UU 7/2021 (HPP))_

### 3.2 The Small-Company Facility — Pasal 31E UU PPh

- **Small-company facility scope** — Companies with annual gross turnover (peredaran bruto) up to IDR 50,000,000,000 receive a 50% reduction of the 22% rate applied to the slice of taxable income proportional to the first IDR 4,800,000,000 of gross turnover. Effective rate on the facility slice: 11%.  _(Pasal 31E UU 36/2008 (unchanged by UU HPP); SE-66/PJ/2010)_
- **Pasal 31E formula** — Turnover ≤ IDR 4.8B:         PPh Badan = 11% × PKP IDR 4.8B < Turnover ≤ 50B:   Facility slice    = (4.8B / Turnover) × PKP Non-facility slice = PKP − Facility slice PPh Badan          = 11% × Facility + 22% × Non-facility Turnover > IDR 50B:           PPh Badan = 22% × PKP   (no facility)  _(Pasal 31E UU 36/2008 (unchanged by UU HPP); SE-66/PJ/2010)_
- **Important** — Pasal 31E applies automatically — not a discretionary election. Computed for each fiscal year independently. A company that exits the IDR 50B band loses the facility for that year.  _(Pasal 31E UU 36/2008 (unchanged by UU HPP); SE-66/PJ/2010)_
- **Interaction with PPh Final UMKM 0.5%** — Cannot stack — taxpayer elects one regime or the other. PPh Final UMKM is covered in `id-pph-final-umkm` and is time-limited for PTs (3 years under PP 55/2022). After expiry the PT defaults to standard PPh Badan with Pasal 31E available where eligible.  _(PP 55/2022)_

### 3.3 Listed-Company Reduction — Pasal 17(2b)

- **Listed-company reduction conditions** — Public companies (perusahaan terbuka / Tbk) listed on IDX (BEI) get an additional 3% reduction (effective 19%) if all of the following are met for at least 183 days in the fiscal year: (1) ≥ 40% of paid-up shares listed and traded on IDX; (2) listed shares held by ≥ 300 parties; (3) each such party holds < 5%; (4) Form X.H.1-6 filed with OJK and DJP.  _(Pasal 17(2b) UU PPh; PP 56/2015)_
- **Stacking with Pasal 31E** — The 3% reduction stacks with Pasal 31E for the non-facility slice (19% on that slice) but does not further reduce the 11% facility slice.  _(Pasal 17(2b) UU PPh; PP 56/2015)_
- **Conservative default** — Treat as private (22%). Reviewer must confirm IDX listing and Form X.H.1-6 filing before applying 19%.  _(Pasal 17(2b) UU PPh; PP 56/2015)_

### 3.4 Taxable Income (Penghasilan Kena Pajak)

- **PKP formula** — PKP = Penghasilan Bruto − Deductible costs (Pasal 6) − Tax loss carry-forward (Pasal 6(2))  _(Pasal 6(2) UU PPh)_
- **Loss carry-forward window** — Tax losses may be carried forward 5 years from the year the loss arose; pioneer industries can get an extended period under tax holiday rules. Carry-back is not available.  _(Pasal 6(2) UU PPh)_

### 3.5 Fiscal Reconciliation (Rekonsiliasi Fiskal)

- **Fiscal reconciliation method** — PPh Badan is computed from the commercial profit per the audited financial statements, adjusted by: (+) non-deductible expenses under Pasal 9; (+) income previously excluded from book profit but taxable; (−) income subject to final tax (PPh Final, already separately taxed); (−) non-taxable income under Pasal 4(3); (±) timing differences (depreciation, provisions). Reported in SPT 1771 Lampiran I.  _(Pasal 9; Pasal 4(3) UU PPh)_

## Section 4 — Deductible vs Non-Deductible Expenses

### 4.1 The 3M Test — Pasal 6 UU PPh

- **3M test definition** — An expense is deductible only if incurred to obtain, collect, and maintain income (untuk mendapatkan, menagih, dan memelihara penghasilan — the "3M" test). Pasal 6(1) lists principal categories:  _(Pasal 6(1) UU PPh)_

**Pasal 6(1) categories table**

| Category | Reference |
| --- | --- |
| Direct/indirect business costs (raw materials, salaries, rent, utilities, interest, royalties, travel, waste) | Pasal 6(1)(a) |
| Depreciation and amortisation (Pasal 11, 11A) | Pasal 6(1)(b) |
| Pension contributions to Menkeu-approved funds | Pasal 6(1)(c) |
| Losses on disposal of business assets | Pasal 6(1)(d) |
| Forex losses | Pasal 6(1)(e) |
| Approved domestic R&D | Pasal 6(1)(f) |
| Scholarship, apprenticeship, training | Pasal 6(1)(g) |
| Bad debts meeting Pasal 6(1)(h) conditions | Pasal 6(1)(h) |
| Donations under PP 93/2010 (disaster, R&D, education, sports, social infrastructure) | Pasal 6(1)(i)–(m) |

### 4.2 Non-Deductible Expenses — Pasal 9 UU PPh

- **Non-deductible expenses intro** — The following are not deductible in computing taxable income:  _(Pasal 9 UU PPh)_

**Pasal 9(1) categories table**

| Item | Reference |
| --- | --- |
| Profit distributions to shareholders (dividends, share of profit) | Pasal 9(1)(a) |
| Costs for personal benefit of shareholders / partners / members | Pasal 9(1)(b) |
| Reserves and provisions, except specific allowances for banks, leasing, insurance, mining reclamation | Pasal 9(1)(c) |
| Personal life/health/accident insurance premiums (subject to PMK 66/2023 BIK rules) | Pasal 9(1)(d) |
| Benefits in kind (*natura/kenikmatan*) — now generally deductible to company, taxable to recipient post-UU HPP / PMK 66/2023 | Pasal 9(1)(e) |
| Excessive payments to shareholders / related parties (TP arm's-length test) | Pasal 9(1)(f) |
| Gifts and donations except qualifying Pasal 6(1)(i)–(m) and approved zakat | Pasal 9(1)(g) |
| Income tax itself (PPh Badan, PPh 25, PPh 29) | Pasal 9(1)(h) |
| Private living expenses of taxpayer or dependents | Pasal 9(1)(i) |
| Owner salary in sole prop / non-PT entity (does not apply to PT directors) | Pasal 9(1)(j) |
| Administrative sanctions and criminal fines | Pasal 9(1)(k) |

### 4.3 Benefit-in-Kind Rules — PMK 66/2023

- **BIK treatment** — From 1 July 2023, most BIK (natura dan kenikmatan) are deductible to the employer (a reversal of pre-UU HPP) and taxable to the employee through PPh 21 (see id-payroll-pph21).  _(PMK 66/2023)_
- **Tax-free exceptions to employee** — Exceptions tax-free to the employee under PMK 66/2023: (1) food and beverages provided to all employees; (2) BIK in remote areas per Menkeu Decree; (3) BIK required by the nature of the work (safety equipment, uniforms); (4) APBN/APBD-funded BIK; (5) certain capped categories (religious/sports facilities, employee gifts up to IDR 3,000,000/employee/year).  _(PMK 66/2023)_
- **Conservative default** — Treat BIK as deductible to the employer AND taxable to the employee unless an exception clearly applies and is documented.  _(PMK 66/2023)_

### 4.4 Depreciation and Amortisation — Pasal 11 and 11A

**Tangible asset groups table**  _(PMK 96/2009 as amended)_

| Group | Useful Life | Straight-Line | Declining-Balance |
| --- | --- | --- | --- |
| I (computers, office equipment) | 4 years | 25% | 50% |
| II (light vehicles, furniture) | 8 years | 12.5% | 25% |
| III (heavy machinery) | 16 years | 6.25% | 12.5% |
| IV (construction equipment, ships) | 20 years | 5% | 10% |
| Buildings — permanent | 20 years | 5% | n/a |
| Buildings — non-permanent | 10 years | 10% | n/a |

- **Intangibles (Pasal 11A)** — Mirror the four tangible groups; amortise straight-line or declining-balance.  _(Pasal 11A)_
- **Election** — Straight-line vs declining-balance is elected per group and is binding. Land is not depreciated.  _(Pasal 11(7))_

## Section 5 — Tier 2 Catalogue (Reviewer Judgement Required)

### 5.1 Tax Holiday — PMK 130/2020

- **Available for** — Pioneer industries (industri pionir) — currently 18 sectors including basic metals, oil refining, petrochemicals, machinery, robotics, pharmaceuticals, and digital economy infrastructure.  _(PMK 130/2020)_
- **Benefit** — 100% PPh Badan reduction for 5–20 years (depending on investment scale from IDR 100 billion to over IDR 30 trillion), followed by a 50% reduction for 2 transitional years. Application via OSS coordinated with BKPM and DJP; holiday begins at commercial operation start.  _(PMK 130/2020)_
- **Conservative default** — Do not apply until the Decree of the Minister of Finance (KMK) is in hand. Reviewer must verify the KMK and commercial operation date.  _(PMK 130/2020)_

### 5.2 Tax Allowance — PP 78/2019

- **Scope and benefits** — For business fields and regions listed in PP 78/2019 attachments. Benefits: 30% investment allowance over 6 years (5%/year), accelerated depreciation, reduced WHT on dividends to foreign shareholders, extended loss carry-forward up to 10 years.  _(PP 78/2019)_
- **Conservative default** — Apply only after the BKPM Decree is issued.  _(PP 78/2019)_

### 5.3 Super-Deduction R&D — PMK 153/2020

- **Super-deduction R&D detail** — Up to 300% deduction for qualifying domestic R&D in priority sectors (food, pharma, ICT, materials, transport, defence, energy, electronics). Base 100% is allowed under Pasal 6(1)(f); the additional up to 200% super-deduction requires a KMK.  _(PMK 153/2020)_
- **Conservative default** — Apply base 100% only. Apply super-deduction only after KMK is issued.  _(PMK 153/2020)_

### 5.4 Super-Deduction Vocational Training — PMK 128/2019

- **Super-deduction vocational detail** — Additional 100% deduction (200% total) on qualifying vocational training and apprenticeship costs. Requires OSS approval.  _(PMK 128/2019)_

### 5.5 Investment Allowance for Labour-Intensive Industries — PMK 16/2020

- **Investment allowance detail** — 60% investment allowance on tangible fixed-asset investment, spread over 6 years (10%/year).  _(PMK 16/2020)_

### 5.6 KEK, Free Trade Zones, Bonded Zones

- **Special zones detail** — Special Economic Zones (KEK), Free Trade Zones (Batam, Bintan, Karimun), and Bonded Zones (Kawasan Berikat) carry sector-specific PPh, PPN, PPnBM, and customs facilities under PP 12/2020 and PP 41/2021. Flag to a specialist.  _(PP 12/2020; PP 41/2021)_

### 5.7 Director Remuneration Reasonableness

- **Director remuneration deductibility** — Director / komisaris salaries are deductible if ratified by RUPS, commercially reasonable, and subject to PPh 21 withholding. Excessive remuneration may be reclassified by DJP as a deemed dividend under Pasal 9(1)(f). Flag where remuneration is materially above market.  _(Pasal 9(1)(f))_

### 5.8 Bad Debt Write-Off — Pasal 6(1)(h)

- **Bad debt conditions** — Bad debts are deductible only if (i) recognised in the books, (ii) listed in a schedule submitted to DJP, and (iii) supported by recovery action (newspaper publication, court action, or written debtor acknowledgement). Banks and financial institutions follow separate rules.  _(Pasal 6(1)(h))_

## Section 6 — Monthly PPh 25 Installments

**Legislation:** Pasal 25 UU PPh; PMK 215/2018.

- **Basic formula** — Monthly PPh 25 = (Prior-Year PPh Badan − Prior-Year Tax Credits) / 12  _(Pasal 25 UU PPh; PMK 215/2018)_
- **Creditable prior-year items** — PPh 22 (collection by certain parties), PPh 23 (services, royalties), PPh 24 (foreign tax credit). PPh 26 (WHT on payments to non-residents) is generally not creditable to a resident PT.  _(Pasal 25 UU PPh)_
- **First-year companies** — Estimate using annualised forecast taxable income.  _(Pasal 25 UU PPh)_
- **Adjustments** — Recalculated each year after the SPT 1771 is filed (new basis from May to April of the following installment year). Mid-year reduction requires DJP approval — up to a 25% reduction is permitted without proof per PMK 215/2018; larger reductions require supporting evidence.  _(PMK 215/2018)_
- **Payment** — 15th of the following month, via SSP / billing code through Coretax. No separate monthly SPT generally required.  _(PMK 215/2018)_
- **Late payment** — 2% per month, prorated daily, capped at 24 months.  _(Pasal 9(2a) UU KUP)_
- **Conservative default** — Pay PPh 25 on time and in full. Do not advise installment reductions without confirmed DJP approval.

## Section 7 — Transfer Pricing

**Legislation:** Pasal 18 UU PPh; PMK 213/2016 (TP-Doc); PMK 22/2020 (TP general); **PMK 172/2023** (implementation of arm's-length principle and dispute resolution, effective 1 January 2024).

### 7.1 The Arm's-Length Principle — PKKU

- **PKKU definition** — Related-party transactions (hubungan istimewa, Pasal 18(4) UU PPh) must apply Prinsip Kewajaran dan Kelaziman Usaha (PKKU) — the Indonesian arm's-length principle. Five OECD methods (CUP, RPM, CPM, TNMM, Profit Split) plus valuation techniques for intangibles.  _(Pasal 18(4) UU PPh)_

### 7.2 Related-Party Definition — Pasal 18(4)

- **Special relationship definition** — A "special relationship" exists where: (1) one party owns ≥ 25% of the other directly or indirectly, or two parties share ≥ 25% common ownership; (2) one party controls the other through management or technology; (3) blood relations to the second degree or marriage to the first degree.  _(Pasal 18(4) UU PPh)_

### 7.3 Documentation Thresholds — PMK 213/2016

- **Documentation requirement trigger** — TP documentation is required if any of the following applies in the fiscal year:  _(PMK 213/2016)_

**Documentation thresholds table**  _(PMK 213/2016)_

| Document | Threshold |
| --- | --- |
| **Master File & Local File** | Prior-year gross revenue > IDR 50B; OR related-party tangible-goods transactions > IDR 20B; OR related-party services / interest / royalty / other transactions > IDR 5B per category |
| **CbCR** | Ultimate parent of a group with consolidated revenue > IDR 11 trillion (~EUR 750M) |
| Related parties in preferential regimes (tax rate < 22%) | Documentation required regardless of value |

### 7.4 PMK 172/2023 Key Updates (effective 2024)

- **PMK 172/2023 updates** — Clarifies the ex-ante pricing approach (support pricing at transaction time, not retrospectively); details guidance for intangibles, intra-group services (benefit test), financial transactions, and business restructuring; confirms MAP and APA routes; reinforces secondary adjustments where retained cash is treated as a constructive dividend.  _(PMK 172/2023)_

### 7.5 Filing Mechanics

- **Master File / Local File deadline** — Must exist within 4 months after fiscal year-end; submitted on DJP request during examination; summary statement filed with SPT 1771.  _(PMK 213/2016)_
- **CbCR filing** — Filed within 12 months of fiscal year-end via DJP's CbCR portal.  _(PMK 213/2016)_
- **TP disclosure** — SPT 1771 Lampiran Khusus 3A / 3A-1 / 3A-2 — discloses related-party transactions and methods used.
- **Conservative default** — If revenue > IDR 50B or any PMK 213/2016 threshold is crossed, flag TP documentation as mandatory. Treat undocumented related-party transactions as TP adjustment risk.  _(PMK 213/2016)_

## Section 8 — Worked Example: Small PT with Pasal 31E Facility

**Facts:** PT Sumber Makmur (resident PT, fiscal year 2025 calendar).
- Gross turnover (peredaran bruto): **IDR 6,000,000,000**.
- Commercial profit before tax: IDR 1,560,000,000.
- Fiscal adjustments: + IDR 30,000,000 non-deductible entertainment (Pasal 9); + IDR 10,000,000 non-deductible private car; − IDR 100,000,000 bank interest already taxed via PPh Final.
- Tax credits: PPh 22 IDR 15,000,000; PPh 23 IDR 25,000,000; PPh 25 paid IDR 80,000,000.

### 8.1 Taxable income (PKP):

- **PKP calculation** — 1,560,000,000 + 30,000,000 + 10,000,000 − 100,000,000 = IDR 1,500,000,000

### 8.2 Apply Pasal 31E.

- **Facility/non-facility slice calculation** — Turnover sits between IDR 4.8B and IDR 50B, so the facility applies to a proportional slice: Facility slice     = (4,800,000,000 / 6,000,000,000) × 1,500,000,000 = IDR 1,200,000,000 Non-facility slice = 1,500,000,000 − 1,200,000,000                   = IDR   300,000,000

### 8.3 PPh Badan:

- **PPh Badan total calculation** — 11% × 1,200,000,000 = IDR 132,000,000 22% ×   300,000,000 = IDR  66,000,000 Total PPh Badan      IDR 198,000,000

### 8.4 PPh 29 (annual underpayment):

- **PPh 29 calculation** — 198,000,000 − 15,000,000 − 25,000,000 − 80,000,000 = IDR 78,000,000 Pay IDR 78,000,000 before filing SPT 1771, no later than 30 April 2026.

### 8.5 2026 monthly PPh 25:

- **2026 monthly PPh 25 calculation** — (198,000,000 − 15,000,000 − 25,000,000) / 12 = IDR 13,166,667 per month Effective from the May 2026 installment (January–April 2026 continues on the 2024-based amount until the 2025 SPT is filed).

## Section 9 — Filing and Payment Mechanics

### 9.1 SPT Tahunan PPh Badan — Form 1771

**Form 1771 sections table**

| Section | Content |
| --- | --- |
| Induk SPT 1771 | Cover page; tax computation summary |
| Lampiran I | Fiscal reconciliation (commercial → taxable income) |
| Lampiran II | COGS, operating expenses, depreciation |
| Lampiran III | Tax credits (PPh 21/22/23/24/25/26) |
| Lampiran IV | Income subject to final tax / non-taxable reconciliation |
| Lampiran V | Shareholders, directors, commissioners |
| Lampiran VI | Equity investments in other companies |
| Lampiran Khusus 3A series | Related-party transactions disclosure |
| Lampiran Khusus 1A / 1B | Commercial vs fiscal depreciation/amortisation |
| Lampiran Khusus 2A | Tax loss carry-forward schedule |

### 9.2 Filing Deadlines

**Filing deadlines table**

| Item | Deadline |
| --- | --- |
| SPT 1771 (calendar year) | **30 April of the following year** |
| SPT 1771 (non-calendar FY) | Last day of the 4th month after FY-end |
| Extension request | Up to 2 months under Pasal 3(4) UU KUP, with provisional payment based on reasonable estimate |
| PPh 29 (annual underpayment) | Before SPT is filed |
| Monthly PPh 25 | 15th of the following month |

### 9.3 Filing Portal — Coretax DJP

- **Coretax DJP transition** — From tax year 2025, corporate filings transition to Coretax DJP (Core Tax Administration System), the unified DJP platform replacing DJP Online, e-Filing, and legacy e-Faktur. SPT 1771 is filed electronically via Coretax.

### 9.4 Audit and Statute of Limitations

- **Statute of limitations and audit process** — Standard statute: 5 years from the end of the tax period (Pasal 13 UU KUP); extended up to 10 years for criminal tax fraud. DJP audits (pemeriksaan) are initiated by SP2/SP3 and produce SKPKB (assessment), SKPLB (overpayment), SKPN (nil), or SKPKBT (additional assessment). Administrative interest rates are set monthly by the Menkeu under the UU HPP framework.  _(Pasal 13 UU KUP)_

### 9.5 Common Penalty Headings

**Common penalty headings table**

| Infraction | Sanction |
| --- | --- |
| Late filing of SPT 1771 | IDR 1,000,000 administrative fine (Pasal 7 UU KUP) |
| Late payment of PPh 25 / PPh 29 | Monthly interest per Menkeu rate (~2%/month, capped 24 months) — Pasal 9(2a) UU KUP |
| SKPKB underpayment | Tax due + monthly interest under UU HPP framework |
| Incorrect SPT (negligence) | Up to 200% of tax shortfall (Pasal 13(3)) |
| Tax evasion | Imprisonment 6 months–6 years + 2×–4× tax shortfall (Pasal 39 UU KUP) |

- **Conservative default** — File on time. Pay PPh 29 before filing. Do not advise on late-filing strategies.

## Section 10 — Conservative Defaults Summary

**Conservative defaults summary table**

| Item | Default |
| --- | --- |
| Turnover band unknown | > IDR 50B (no Pasal 31E facility) |
| Listed-company status unknown | Private (22%, not 19%) |
| Tax holiday / allowance unverified | Apply standard rate; flag pending application |
| Related-party status unknown | Treat as related |
| TP documentation unknown | Required if > IDR 50B revenue (PMK 213/2016) |
| BIK treatment unknown | Deductible to company; taxable to recipient (PMK 66/2023) |
| Expense purpose unclear | Non-deductible (3M test fails) |
| Asset useful life unknown | PMK 96/2009 group rates |
| Bookkeeping currency | IDR (USD requires DJP permission) |
| Tax loss carry-forward | Verify 5-year window per loss year |

## Section 11 — Cross-References

**Cross-references table**

| Topic | Skill |
| --- | --- |
| Payroll withholding (PPh 21) | `id-payroll-pph21` |
| PPN / VAT / e-Faktur / PKP | `indonesia-vat` |
| Foundation principles | `foundation` |
| Intake checklist | `intake` |
| PPh Final UMKM 0.5% (alternative regime) | `id-pph-final-umkm` |

When a topic crosses skills (e.g., a PPh 21 BIK question with PPh Badan deductibility impact), address both — load the relevant cross-skill before answering.

## Section 12 — Sources

**Primary Legislation**

- **UU 7/2021** — UU Harmonisasi Peraturan Perpajakan (HPP). Set the 22% rate; reformed BIK treatment.
- **UU 36/2008** — UU Pajak Penghasilan (UU PPh). Pasal 6 (deductions), Pasal 9 (non-deductible), Pasal 11/11A (depreciation/amortisation), Pasal 17 (rates), Pasal 17(2b) (listed-company), Pasal 18 (TP), Pasal 25 (installments), Pasal 31E (small-company facility).
- **UU 11/2020** — UU Cipta Kerja (Omnibus Law). Reformed dividend exemption and other rules.
- **UU 6/1983** as amended — UU KUP (general procedures, deadlines, penalties).
- **UU 2/2020** — Emergency law that set the rate reduction trajectory.

**Government Regulations (PP)**

- **PP 55/2022** — Implementation of UU HPP; PPh Final UMKM 0.5% revisions.
- **PP 78/2019** — Tax allowance.
- **PP 93/2010** — Donations deductibility.
- **PP 56/2015** — Listed-company rate reduction.
- **PP 12/2020** — KEK Special Economic Zones.

**Minister of Finance Regulations (PMK)**

- **PMK 213/2016** — Transfer pricing documentation (Master/Local File, CbCR thresholds).
- **PMK 172/2023** — Arm's-length principle implementation, effective 2024.
- **PMK 22/2020** — TP general guidance.
- **PMK 96/2009** as amended — Tangible-asset depreciation groups.
- **PMK 130/2020 / PMK 11/2020** — Tax holiday.
- **PMK 153/2020** — Super-deduction R&D and pioneer industry list.
- **PMK 128/2019** — Super-deduction vocational training.
- **PMK 16/2020** — Investment allowance for labour-intensive industries.
- **PMK 66/2023** — BIK treatment, effective 1 July 2023.
- **PMK 215/2018** — Monthly PPh 25 computation and adjustment.

**DJP Circulars and Platform**

- **SE-66/PJ/2010** — Pasal 31E proportional-slice formula.
- **PER-22/PJ/2013** as amended — TP documentation form and procedures.
- **Coretax DJP** — Unified DJP filing platform, replacing legacy DJP Online from tax year 2025.

## PROHIBITIONS

- NEVER apply tax holiday, tax allowance, or super-deduction without a KMK / BKPM Decree in hand.
- NEVER ignore Pasal 31E when turnover ≤ IDR 50B — the facility is automatic.
- NEVER use current-year profit as the PPh 25 basis — installments are prior-year based.
- NEVER include PPh Final income in the PPh Badan computation — reconcile it out.
- NEVER deduct income tax itself (PPh Badan, 25, 29) — Pasal 9(1)(h).
- NEVER deduct dividends — Pasal 9(1)(a).
- NEVER deduct administrative or criminal fines — Pasal 9(1)(k).
- NEVER treat related-party transactions as arm's length without supporting analysis.
- NEVER skip TP documentation when PMK 213/2016 thresholds are crossed.
- NEVER advise late filing or late payment as a strategy — 2%/month surcharge is severe.
- NEVER stack PPh Final UMKM 0.5% with Pasal 31E — they are alternative regimes.
- NEVER apply Pasal 17(2b) 19% rate without confirming the 40%/300-party/<5%/183-day conditions and the X.H.1-6 filing.
- NEVER present figures as definitive — always label as estimates pending reviewer sign-off.

## Disclaimer

This skill and its outputs are for informational and computational purposes only and do not constitute tax, legal, or financial advice. All outputs must be reviewed and signed off by a qualified Indonesian Konsultan Pajak (holding a USKP certificate) before filing or acting upon. The latest verified version is maintained at [openaccountants.com](https://openaccountants.com).

## OpenAccountants footer

*OpenAccountants — open-source accounting skills for AI*

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
