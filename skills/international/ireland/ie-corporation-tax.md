---
name: ie-corporation-tax
description: "Use this skill whenever asked about Irish Corporation Tax for a resident Irish company or branch of a non-resident company carrying on a trade in Ireland. Trigger on phrases like \"Ireland CT\", \"Ireland corporation tax\", \"12.5% Ireland\", \"Irish trading rate\", \"Pillar Two Ireland\", \"Irish CT1 return\", \"Revenue Online Service CT\", \"ROS CT1\", \"Section 21 TCA\", \"Section 21A passive income\", \"Knowledge Development Box\", \"KDB\", \"R&D tax credit Ireland\", \"Section 766\", \"Section 110 SPV\", \"group relief Ireland\", \"preliminary CT\", \"iXBRL accounts\", \"QDMTT Ireland\", \"IIR Ireland\", or \"UTPR Ireland\". Covers the 12.5% trading rate (Section 21 TCA 1997), the 25% non-trading rate (Section 21A) on passive income, the Pillar Two 15% effective minimum tax for in-scope MNEs implemented via Finance (No. 2) Act 2023 (IIR, QDMTT, UTPR), the R&D tax credit at 30% under Section 766 TCA (as raised by FA 2024) refundable in three instalments, the Knowledge Development Box at 6.25% effective rate, Section 110 securitisation SPV rules, group relief at the 75% threshold, trading loss relief (one-year carry-back, indefinite carry-forward), preliminary tax (90% current year or 100% prior year), and final CT1 filing within 9 months of year-end (by the 23rd of that month for ROS users) with iXBRL-tagged financial statements via Revenue Online Service. Out of scope: personal income tax (use ie-income-tax-form11), USC (use ie-usc), PRSI Class S (use ie-prsi-class-s), VAT (use ireland-vat-return), preliminary income tax (use ie-preliminary-tax), partnerships and unincorporated businesses, foreign branch trading profits taxed under Section 25 attribution rules, banking and insurance sector specific regimes, life assurance Case I/IV computations, REIT (Section 705A) and IREF (Section 739K) specific returns, petroleum and mineral extraction profits, and Irish Collective Asset-management Vehicles (ICAVs). ALWAYS read this skill before touching any Irish Corporation Tax work."
jurisdiction: IE
domain: international
tax_year: 2025
tier: 2
last_updated: 2026-07-06
---

# ie-corporation-tax

## Ireland — Corporation Tax — Skill v1.0

> **Produced by OpenAccountants (openaccountants.com)**
>
> This skill is for informational purposes only and does not constitute tax, legal, or financial advice. All outputs must be reviewed and signed off by a qualified Irish tax adviser (Chartered Tax Adviser CTA, ACA, ACCA, or AITI-qualified practitioner) before filing or acting upon. The latest verified version is maintained at [openaccountants.com](https://openaccountants.com).

## Section 1 — Quick Reference

**Quick Reference table**

| Field | Value |
| --- | --- |
| Country | Ireland (Éire) |
| Tax | Corporation Tax (CT) |
| Currency | EUR (functional currency election available under Section 402 TCA 1997) |
| Tax authority | Revenue Commissioners (An Coimisiún Ioncaim) |
| Primary legislation | **Taxes Consolidation Act 1997 (TCA 1997)** as amended by annual Finance Acts |
| Recent Finance Acts | Finance Act 2023 (Pillar Two introduction); Finance Act 2024 (R&D credit raised to 30%); Finance Act 2025 (annual updates) |
| **Trading rate** | **12.5%** of trading income — **Section 21 TCA 1997** |
| **Non-trading rate** | **25%** of passive (non-trading) income — **Section 21A TCA 1997** |
| **Capital gains rate (companies)** | 33% on chargeable gains (Section 28 TCA) |
| **Close-company surcharge** | 20% on undistributed investment / rental income; 15% on undistributed professional service income (Sections 440, 441 TCA) |
| **Pillar Two — IIR / QDMTT** | Effective minimum tax **15%** for MNEs with consolidated revenue **> €750M** for at least 2 of the previous 4 financial years — Part 4A TCA 1997 (inserted by Finance (No. 2) Act 2023); effective for fiscal years beginning on or after 31 December 2023 |
| **Pillar Two — UTPR** | Undertaxed Profits Rule, effective for fiscal years beginning on or after 31 December 2024 |
| **R&D Tax Credit** | **30%** of qualifying R&D expenditure (raised from 25% by Finance Act 2024) — Section 766 TCA; refundable in 3 instalments |
| **Knowledge Development Box (KDB)** | Effective rate **6.25%** (i.e. half the 12.5% rate) on qualifying IP-derived income — Section 769G-R TCA; extended to accounting periods beginning before 1 January 2027 (FA 2024) |
| **Group relief threshold** | **75%** ownership (effective beneficial); Sections 411–429 TCA |
| **Loss relief** | Trading losses: 1-year carry-back (Section 396A); indefinite carry-forward against same trade (Section 396) |
| **Preliminary tax (large companies)** | 50% of current year OR 100% of prior year, in 2 instalments (large company = CT liability > €200,000 in preceding period) |
| **Preliminary tax (small companies)** | 90% of current year OR 100% of prior year, in 1 instalment |
| **Preliminary tax due date** | 23rd day of the month preceding the last month of the accounting period (large: also a first instalment in month 6) |
| **Annual return** | **Form CT1** filed via **Revenue Online Service (ROS)** |
| **CT1 filing deadline** | 9 months after the end of the accounting period; **must be by the 23rd day of that 9th month** to avoid surcharge (Section 959AA TCA) |
| **iXBRL accounts** | Financial statements must be filed in iXBRL format alongside CT1 (mandatory for most companies; small-company exclusion limited) |
| **Late filing surcharge** | 5% of liability (up to €12,695) if filed within 2 months late; 10% (up to €63,485) if more than 2 months late |
| **Statute of limitations** | 4 years from the end of the accounting period in which the return was filed (Section 959AA(2)); unlimited for fraud / neglect |
| Skill version | 1.0 |
| Validated by | Pending — sign-off by Irish Chartered Tax Adviser (CTA / AITI) |

### 1.1 Conservative Defaults (Snapshot)

**Conservative Defaults (Snapshot) table**

| Ambiguity | Default |
| --- | --- |
| Trading vs non-trading income unclear | Non-trading (25%) |
| Passive-income source unclear | Section 21A (25%) |
| Pillar Two scope unclear | Out of scope until consolidated revenue > €750M for 2 of last 4 FYs is confirmed |
| R&D qualification unclear | No credit until BERD test + Frascati Manual criteria documented |
| KDB qualification unclear | Do not apply 6.25%; default to 12.5% trading rate |
| Group relationship unclear | No group relief |
| Close company status unclear | Treat as close company; surcharge potentially in scope |
| Accounting period > 12 months | Split into two CT accounting periods (first 12 + remainder) — Section 27 TCA |

## Section 2 — Required Inputs and Refusal Catalogue

### 2.1 Required Inputs

- **Minimum viable inputs** — Signed statutory financial statements (Companies Act 2014 format) for the accounting period; prior-year Form CT1; confirmation of (i) trading vs non-trading income split, (ii) close-company status, (iii) group structure, (iv) any Pillar Two scope flag.
- **Recommended inputs** — General ledger trial balance; fixed-asset register with capital allowance schedule (Section 284 wear-and-tear, Section 291A intangibles); R&D expenditure schedule with Section 766 categorisation; KDB tracking-and-tracing computation if claimed; preliminary tax payment confirmations; CRO B1 annual return confirmation (separate from CT but reviewer should cross-check).
- **Ideal inputs** — Audited statements with audit report and iXBRL-tagged file; transfer pricing local file (Section 835G TCA); CbCR (Section 891H TCA) if part of a group with consolidated revenue > €750M; Pillar Two GIR (Globe Information Return) workings; intercompany agreements; Revenue eBrief alerts subscription log; prior-year Revenue audit / intervention correspondence.
- **Hard stop** — HARD STOP if minimum is missing. Without statutory accounts and the prior-year CT1, no CT computation may be produced.

### 2.2 Refusal Catalogue

- **R-IE-CT-1** — Non-resident company with no Irish branch. Section 23A residence test required first. Non-resident companies with no Irish PE / branch are outside Irish CT scope. Escalate to a cross-border specialist (see `_cross-border`).  _(Section 23A TCA)_
- **R-IE-CT-2** — Sector-specific regimes. Banking and IFSC funds (Sections 110, 246), life assurance (Part 26 TCA), REITs (Section 705A et seq.), IREFs (Section 739K et seq.), petroleum (Part 24), mining (Part 24), Islamic finance (Part 8A) — out of scope.  _(Sections 110, 246, Part 26, Section 705A, Section 739K, Part 24, Part 8A TCA)_
- **R-IE-CT-3** — Section 110 SPV bespoke computations. Flagged at Tier 2 (see Section 5.3) but bespoke profit-participating loan structures, qualifying asset definitions, and Section 110(5A) restrictions require specialist sign-off. Do not produce a Section 110 computation without explicit reviewer engagement.  _(Section 110(5A) TCA)_
- **R-IE-CT-4** — Pillar Two GIR preparation. Skill flags scope and routes data; the GloBE Information Return (GIR) and the QDMTT return itself require specialist co-pilot software (e.g., OECD GIR XML schema). Out of scope for unaided generation.
- **R-IE-CT-5** — Aggressive structuring. Will not advise on debt-push-down, IP migration timing for KDB capture, residence migration to/from Ireland, hybrid mismatch structuring (anti-hybrid rules Sections 835AG–835AY), or principal-purpose-test (PPT) avoidance positions. Section 811C general anti-avoidance rule and protective notification regime under Section 811D applies — escalate.  _(Sections 835AG–835AY, 811C, 811D TCA)_
- **R-IE-CT-6** — Revenue intervention or audit. Active audit, profile interview, level 1/2/3 intervention, or qualifying disclosure under Section 1077E TCA — do not draft positions without engaged CTA representation.  _(Section 1077E TCA)_
- **R-IE-CT-7** — Cross-skill scope. Personal tax → `ie-income-tax-form11`; USC → `ie-usc`; PRSI → `ie-prsi-class-s`; VAT → `ireland-vat-return`; preliminary income tax (individuals) → `ie-preliminary-tax`.
- **R-IE-CT-8** — Functional currency election. Section 402 TCA functional currency cases require a separate computation discipline and reviewer sign-off — do not auto-elect.  _(Section 402 TCA)_

## Section 3 — Tier 1 Rules (Standard Computation)

### 3.1 The 12.5% Trading Rate — Section 21 TCA 1997

- **Trading rate** — 12.5% percent (Case I and Case II trading income)  _(Section 21(1) TCA 1997)_
- **CT (trading) formula** — CT (trading) = 12.5% × Trading profits adjusted for tax  _(Section 21(1) TCA 1997)_
- **'Trading' defined** — Section 3 TCA — a trade is "every trade, manufacture, adventure or concern in the nature of trade". The case law (Birmingham & District Cattle By-Products v IRC; CIR v Livingston) emphasises the badges of trade. Investment-holding income is not trading.  _(Section 3 TCA)_
- **Manufacturing / IP / services** — All bona-fide trading activity qualifies at 12.5% — there is no longer a separate manufacturing relief (abolished from 31 December 2010). Mere passive holding of assets does not qualify.

### 3.2 The 25% Non-Trading Rate — Section 21A TCA 1997

- **Non-trading rate** — 25% percent  _(Section 21A TCA 1997)_

**Section 21A categories table**  _(Section 21A TCA 1997)_

| Category | Schedule D Case | Examples |
| --- | --- | --- |
| Investment income (interest, dividends from non-Irish sources) | Case III | Foreign interest, foreign dividends (subject to exemption tests under Sections 21B / 626B) |
| Rental income from Irish or foreign property | Case V (Irish) / Case III (foreign) | Net rental profits |
| Royalties (where not part of a trade) | Case III / IV | Passive licensing receipts |
| Mining, petroleum, dealing in land | Case I (specified trades) | Petroleum (Part 24); dealing in land (Section 21A(2)) |
| Other Case IV / Case V income | Various | Miscellaneous untaxed income |

- **CT (non-trading) formula** — CT (non-trading) = 25% × Non-trading profits  _(Section 21A TCA 1997)_
- **Total CT liability formula** — Total CT liability = (12.5% × Case I/II trading profits) + (25% × Case III/IV/V non-trading profits) + (33% × chargeable gains, with adjustment via Section 78 to gross up to 33% effective).  _(Section 78 TCA)_

### 3.3 Capital Gains — Section 28 TCA

- **Effective CGT rate for companies** — 33% percent  _(Section 28 TCA)_
- **Section 78 gross-up formula** — Section 78 grosses up the gain by the formula `Gain × (33/12.5)` if computed at the 12.5% rate, or `Gain × (33/25)` at the 25% rate, so the effective tax is 33%.  _(Section 78 TCA)_
- **Substantial shareholding exemption** — Disposal of shares in a qualifying subsidiary (≥ 5% held for ≥ 12 months in the past 5 years, trading subsidiary, EU/treaty country) is exempt from CT on the gain.  _(Section 626B TCA)_

### 3.4 Pillar Two — 15% Effective Minimum Tax

- **Legislation** — Part 4A TCA 1997 (inserted by Finance (No. 2) Act 2023, implementing Council Directive (EU) 2022/2523 of 14 December 2022).  _(Part 4A TCA 1997)_
- **Scope** — Multinational and large domestic groups with consolidated revenue > €750M in at least 2 of the 4 preceding financial years. Excluded entities: government, international organisations, non-profits, pension funds, ultimate parent investment funds, real estate investment vehicles.  _(Part 4A TCA 1997)_
- **Three rules — sequential application** — 1. QDMTT (Qualified Domestic Minimum Top-up Tax) — Ireland's domestic top-up applied first. Effective for fiscal years beginning on or after 31 December 2023. Calculated under Irish QDMTT computation rules aligned with the GloBE rules. Has QDMTT-safe-harbour status. 2. IIR (Income Inclusion Rule) — Parent-level top-up where a low-taxed constituent entity sits below an Irish-resident parent. Effective for fiscal years beginning on or after 31 December 2023. 3. UTPR (Undertaxed Profits Rule) — Backstop allocation rule for low-taxed entities not captured by IIR. Effective for fiscal years beginning on or after 31 December 2024.  _(Part 4A TCA 1997)_
- **ETR computation** — ETR = Adjusted Covered Taxes / GloBE Income Top-up Tax % = max(0, 15% − ETR) Top-up Tax = Top-up Tax % × Excess Profit where Excess Profit = GloBE Income − Substance-Based Income Exclusion (SBIE) SBIE (transitional) = 9.8% payroll carve-out + 7.8% tangible-asset carve-out (2024), declining to 5% + 5% by 2033  _(Part 4A TCA 1997)_
- **Filing** — Pillar Two top-up tax return ("Top-up Tax Information Return" / Irish equivalent) and the GloBE Information Return (GIR) filed via Revenue's Pillar Two portal. First GIR filings deadline: 30 June 2026 for FY 2024 (i.e., 18 months after FY-end for transition year; 15 months thereafter).
- **Transitional CbCR safe harbour** — For FYs starting before 31 December 2026, jurisdictions passing the de minimis, simplified ETR, or routine profits test under qualified CbCR may avoid full GIR computation.
- **Conservative default** — Pillar Two out of scope unless the in-scope test (€750M consolidated revenue, 2 of 4 years) is confirmed in writing with consolidated group accounts. Refuse to compute IIR / QDMTT / UTPR without specialist co-pilot software and a CTA in the loop (R-IE-CT-4).

### 3.5 Close-Company Surcharges — Sections 440, 441 TCA

- **Close company definition** — A "close company" is one under the control of 5 or fewer participators (or any number of director-participators).  _(Section 430 TCA)_
- **Section 440 surcharge** — 20% surcharge on undistributed investment and rental income (non-trading) that is not distributed within 18 months of the accounting period end. percent  _(Section 440 TCA)_
- **Section 441 surcharge** — 15% surcharge on 50% of undistributed professional service income for close service companies (e.g., dentists, solicitors operating through a company). percent  _(Section 441 TCA)_
- **De minimis relief** — Surcharge does not apply if total undistributed income is less than €2,000 (Section 440) or a small threshold (Section 441). EUR  _(Section 434 TCA)_
- **Conservative default** — Assume close-company status applies to any owner-managed company and check the dividend strategy against Section 440/441 exposure.

### 3.6 Capital Allowances — Section 284 et seq. TCA

**Capital allowances table**

| Asset class | Wear-and-tear rate | Reference |
| --- | --- | --- |
| Plant and machinery | 12.5% straight-line over 8 years | Section 284 TCA |
| Motor vehicles (CO2 categories A–C ≤ 155 g/km) | 12.5% on lower of cost / specified amount (€24,000 cap) | Section 380K |
| Motor vehicles (CO2 D–F) | Restricted / nil | Section 380K |
| Industrial buildings | 4% straight-line over 25 years (most categories) | Section 271–273 |
| Intangible assets (Section 291A specified intangibles) | Aligned with accounting amortisation OR 7% (15-year life) elected; capped at 80% of trading income (re-introduced from FA 2017) | Section 291A |
| Energy-efficient equipment | 100% accelerated allowance (Section 285A) — note: scheme ended for new claims after 31 December 2025 unless extended by FA |  |

- **Section 291A cap** — Capital allowances and related interest on specified intangibles cannot reduce trading income by more than 80% in any accounting period. Excess carries forward. percent  _(Section 291A TCA)_

### 3.7 Trading Losses — Sections 396, 396A, 396B TCA

**Trading losses relief table**

| Relief | Mechanism | Reference |
| --- | --- | --- |
| Current-year offset | Trading loss offset against other Case I / total profits of the same period | Section 396(1) |
| 1-year carry-back | Trading loss carried back 12 months against trading income of the prior period | Section 396A |
| Indefinite carry-forward | Trading loss carried forward against future trading income of the **same trade** | Section 396(1) |
| Value-basis offset | Trading losses surrendered on a "value basis" against tax on non-trading income (Section 396B) — converted at 12.5% / 25% ratio | Section 396B |
| Terminal loss relief | Final 12 months' trading loss against trading income of preceding 3 years | Section 397 |

- **Restriction (Section 396C)** — Pre-trading losses are restricted to the trade that gave rise to them. Same-trade continuity is required for carry-forward; cessation extinguishes the loss.  _(Section 396C TCA)_

### 3.8 Group Relief — Sections 411–429 TCA

- **Group definition** — Two companies are in a 75% group where one is the 75% beneficial-ownership subsidiary of the other, or both are 75% subsidiaries of a third company. The parent must be EU- or EEA-resident or treaty-jurisdiction-resident for surrender of losses (post-Marks & Spencer ECJ and Section 420C extensions).  _(Section 411 TCA)_
- **What can be surrendered** — Current-year trading losses, excess capital allowances, excess management expenses, excess Case V losses, certain charges on income.
- **Mechanism** — Loss-maker surrenders to claimant within the same group; claimant offsets against profits of the corresponding accounting period (or a corresponding portion if periods do not align). Payment for group relief can be made up to the surrendered amount and is tax-neutral.
- **Consortium relief** — Available where a company is owned 75%+ collectively by a consortium and each member holds 5%–75%.  _(Section 412 TCA)_

### 3.9 Computation Template

**Computation Template table**

| Step | Item |
| --- | --- |
| 1 | Profit per accounts (statutory accounts under Companies Act 2014 / IFRS / FRS 102) |
| 2 | Add back: non-deductible expenses (entertainment, fines, depreciation, accounting amortisation outside Section 291A) |
| 3 | Less: tax-deductible amounts not in accounts (capital allowances under Section 284, R&D under Section 766) |
| 4 | Separate income into Case I (trading), Case III (foreign investment), Case IV (other), Case V (Irish rents) |
| 5 | Apply 12.5% to Case I/II; apply 25% to Case III/IV/V; compute chargeable gains at 33% effective |
| 6 | Apply credits: R&D tax credit (Section 766), foreign tax credit (Schedule 24), KDB relief (Section 769I if elected) |
| 7 | Compute close-company surcharge (Sections 440/441) on undistributed income |
| 8 | Determine preliminary tax obligation and balance due on CT1 |

## Section 4 — Deductible and Non-Deductible Expenses

### 4.1 General Deductibility — Section 81 TCA (Schedule D Case I/II)

- **Wholly and exclusively test** — An expense is deductible only if "wholly and exclusively" incurred for the purposes of the trade or profession (Section 81(2)(a)). The deduction also requires the expense to be of a revenue (not capital) nature (Section 81(2)(f)).  _(Section 81 TCA)_
- **Common deductible items** — - Cost of goods sold, raw materials, sub-contractor labour (subject to RCT compliance — Section 530 TCA). - Employee wages, employer's PRSI, pension contributions to Revenue-approved schemes. - Rent, rates, utilities, insurance (except life insurance on employees outside Revenue-approved scheme). - Repairs and maintenance (capital improvements are not deductible — they go to the capital allowances pool). - Bad debts (specific, not general provision). - Professional fees (audit, legal — but capital legal fees on acquisitions are not deductible). - Travel and subsistence (per Revenue civil-service rates for employees; reasonable trade-purpose justification).  _(Section 530 TCA)_

### 4.2 Non-Deductible Items

**Non-deductible items table**

| Item | Reference |
| --- | --- |
| Entertainment of customers / clients | Section 840 TCA |
| Penalties, fines (criminal or regulatory) | Case law; not "wholly and exclusively" |
| Depreciation per accounts | Replaced by Section 284 capital allowances |
| Goodwill amortisation per accounts | Replaced by Section 291A specified intangibles regime |
| Capital expenditure | Section 81(2)(f) — relief via capital allowances |
| Dividends / distributions | Not a deductible expense; subject to dividend withholding tax (DWT) under Section 172A |
| Corporation tax itself | Not deductible |
| General provisions for doubtful debts | Only specific bad-debt write-offs allowed |
| Pre-trading expenditure (other than Section 82) | Section 82 allows 3-year pre-trading expenses on first day of trading |
| Excessive director remuneration | "Wholly and exclusively" test plus Section 130 distribution recharacterisation risk |
| Interest on late-paid taxes | Section 1080 interest is not deductible |

### 4.3 Anti-Hybrid Rules — Sections 835AG–835AY TCA

- **ATAD II hybrid mismatch rules** — ATAD II hybrid mismatch rules deny deductions or include income where a hybrid mismatch creates a deduction-without-inclusion (D/NI), double-deduction (DD), or imported mismatch. Applies for accounting periods beginning on or after 1 January 2020. Conservative default: Flag any cross-border interest, royalty, or service deduction to a related party as a hybrid-mismatch screening question.  _(Sections 835AG–835AY TCA)_

### 4.4 Interest Limitation Rule — Section 835AY TCA

- **Interest limitation rule** — ATAD I ILR effective from 1 January 2022. Net interest expense deduction capped at 30% of tax-EBITDA unless the de minimis threshold (€3 million) applies or the equity escape / group ratio rule provides relief. Disallowed interest carries forward. percent  _(Section 835AY TCA)_

## Section 5 — Tier 2 Catalogue (Reviewer Judgement Required)

### 5.1 R&D Tax Credit — Section 766 TCA

- **R&D credit rate (FA 2024 onwards)** — 30% of qualifying R&D expenditure (raised from 25%). Applies to accounting periods commencing on or after 1 January 2024. percent  _(Section 766 TCA)_
- **Qualifying expenditure** — - Salaries of R&D staff (apportioned to qualifying time). - Consumables used in R&D. - Plant and machinery used wholly and exclusively for R&D (capital allowances accelerated where used in R&D). - Subcontracted R&D (Section 766(1)(b)(vii)) capped at 15% of in-house R&D spend or €100,000 (whichever greater). - Outsourced to a third-level institution capped at 5% of in-house spend.  _(Section 766(1)(b)(vii) TCA)_
- **Qualifying activity** — Must satisfy the Frascati Manual definition (systematic, investigative, creative, novel, uncertain). Must be in a "field of science or technology" (Section 766(1)(a)). Software development qualifies where it meets the technological-uncertainty test (Revenue R&D Guidelines).  _(Section 766(1)(a) TCA)_
- **Refundability — Section 766C** — The credit can be (i) offset against CT of the claim period, (ii) carried forward, or (iii) paid as a cash refund in 3 instalments over 33 months: - Instalment 1: Greater of €75,000 (FA 2024 raised threshold) or 50% of the credit — payable on filing. - Instalment 2: 60% of the remaining balance — 12 months later. - Instalment 3: Final balance — 24 months later.  _(Section 766C TCA)_
- **Filing** — Form CT1 R&D section; supporting "R&D Tax Credit Claim" documentation (Section 766(7B)) must accompany the claim. Revenue has 4 years to challenge.  _(Section 766(7B) TCA)_
- **Conservative default** — Do not claim R&D credit until a contemporaneous technical report meeting the Frascati Manual criteria is on file. Engage a specialist for borderline software / process improvement claims.

### 5.2 Knowledge Development Box — Sections 769G–769R TCA

- **KDB effective rate** — 6.25% on qualifying profits from qualifying intellectual property (patents, copyrighted software, IP equivalent to a patentable invention for small companies). percent  _(Sections 769G–769R TCA)_
- **OECD modified nexus approach** — Qualifying profits are restricted by the nexus fraction = (qualifying R&D expenditure × 1.3) / total expenditure on the IP asset. The 30% uplift is the OECD-permitted "up-lift" for outsourcing or acquisition costs.
- **Mechanism** — Election made in the CT1; profits from qualifying IP are computed using a tracking-and-tracing methodology; the qualifying profit is taxed at the standard 12.5%, with a deduction equal to 50% of the qualifying profit giving an effective 6.25% rate.
- **Extension** — FA 2024 extended KDB to accounting periods beginning before 1 January 2027.
- **Conservative default** — Do not elect KDB without a documented IP asset, nexus computation, and tracking-and-tracing system in place. The compliance burden is material; benefit only arises for material qualifying IP profits.

### 5.3 Section 110 Securitisation SPVs

- **Legislation** — Section 110 TCA grants a special tax regime to "qualifying companies" holding qualifying assets (financial assets, plant and machinery, commodities). Profits are computed under Case III with deductions for profit-participating notes (PPN) interest, effectively allowing tax-neutral cash flow-through to noteholders, provided strict conditions are met: - Section 110(1): Qualifying company definition (Irish-resident, ≥ €10 million qualifying assets at inception, notification to Revenue within 8 weeks). - Section 110(4): Treats PPN interest as deductible even if profit-dependent (subject to Section 110(5A) anti-avoidance from FA 2016 onwards excluding certain Irish real estate income). - Section 110(5A): Carves out Irish land-derived income — Section 110 deduction restricted for "specified property business" profits.  _(Section 110 TCA)_
- **Common uses** — CLO / CDO structures, aircraft leasing, securitisation, structured finance.
- **Conservative default** — Section 110 deals require specialist structuring counsel. Do not compute or opine on Section 110 positions without explicit reviewer engagement (R-IE-CT-3).

### 5.4 Transfer Pricing — Part 35A TCA (Sections 835A–835HB)

- **Scope** — Irish TP rules align with the OECD Transfer Pricing Guidelines 2022 (Section 835D). Apply to associated-enterprise transactions (≥ 50% common ownership, control test).  _(Section 835D TCA)_
- **Master File threshold** — Required if consolidated group revenue ≥ €250 million. EUR  _(Section 835G TCA)_
- **Local File threshold** — Required if consolidated group revenue ≥ €50 million. EUR  _(Section 835G TCA)_
- **Documentation timing** — Documentation must be in place by the CT1 filing date; produced within 30 days of Revenue request.
- **CbCR threshold** — CbCR required for groups with consolidated revenue ≥ €750 million. EUR  _(Section 891H TCA)_
- **SME exemption** — SMEs (≤ 250 employees AND turnover ≤ €50m OR balance sheet ≤ €43m) are largely exempt from formal TP documentation but the arm's-length principle still applies.  _(Section 835E TCA)_
- **Penalties** — No documentation = restricted access to the protective notification regime; potential tax-geared penalties under Section 1077E.  _(Section 1077E TCA)_

### 5.5 Foreign Tax Credit — Schedule 24 TCA

- **Foreign tax credit mechanism** — Double-tax relief on foreign-sourced income (dividends, interest, royalties) via credit (Schedule 24) or deduction. Credit limited to the Irish tax on the same income. Pooling rules permit excess credits on dividends from EU/treaty subsidiaries to be carried back 1 year or forward indefinitely (Schedule 24 para 9I).  _(Schedule 24 TCA)_

### 5.6 Participation Exemption on Foreign Dividends (NEW — FA 2024)

- **Legislation** — Section 831B TCA (inserted by Finance Act 2024), effective for distributions received on or after 1 January 2025.  _(Section 831B TCA)_
- **Mechanism** — Election-based participation exemption for foreign dividends from EU/EEA/tax-treaty subsidiaries where the receiving company holds ≥ 5% of the share capital for ≥ 12 months and certain anti-abuse conditions are met. Removes the prior "tax-and-credit" double-tax relief mechanism for opted-in dividends, replacing it with full exemption.  _(Section 831B TCA)_
- **Conservative default** — Do not elect Section 831B exemption without checking subsidiary jurisdiction listing and the 5%/12-month holding test.

### 5.7 Outbound Payments Defensive Measure — Section 817U TCA (FA 2023)

- **Outbound payments defensive measure** — Effective 1 April 2024. Withholding tax / additional CT charge on outbound interest, royalty, and dividend payments to associated entities in zero-tax or EU non-cooperative jurisdictions. Applies to payments where the recipient is not subject to a minimum 9% headline rate (or is in a Annex I non-cooperative jurisdiction). Reviewer must screen all outbound related-party payment streams.  _(Section 817U TCA)_

### 5.8 Start-Up Relief — Section 486C TCA

- **Start-up relief** — Relief from CT for new trading companies in the first 5 accounting periods. Tax liability up to €40,000 fully relieved; partial relief between €40,000 and €60,000. Linked to employer's PRSI contributions (Section 486C(7) — up to €5,000 per employee, capped at the lesser of the PRSI paid and the relief). Extended to qualifying companies commencing trade up to 31 December 2026 (FA 2024).  _(Section 486C TCA)_

### 5.9 Three-Year Tax Holiday for Certain Start-Ups (Section 486C interaction)

Note: Section 486C is the principal start-up relief. There is no separate "tax holiday" regime equivalent to Indonesia's. Reviewer should not confuse the two.

## Section 6 — Worked Examples

### 6.1 Start-Up Trading Company — All Trading Income

**Facts:** TechCo Ltd, Irish-resident, accounting period 1 January 2025 – 31 December 2025.
- Trading profit (Case I) per accounts: €500,000.
- Depreciation (added back): €20,000.
- Capital allowances on plant: €25,000.
- R&D qualifying expenditure: €100,000 (claimed at 30%).
- No non-trading income.
- Prior-year CT liability: €0 (first year of trading) — qualifies for Section 486C start-up relief.

**Computation:**

```
Case I trading profit per accounts             500,000
Add: depreciation                               20,000
                                               -------
Adjusted profit                                520,000
Less: capital allowances (Section 284)         (25,000)
                                               -------
Taxable trading profit                         495,000

CT @ 12.5%                                      61,875
Less: R&D tax credit (Section 766)             
       30% × €100,000                          (30,000)
                                               -------
CT before start-up relief                       31,875

Section 486C start-up relief
(liability < €40,000 — fully relieved,
subject to employer's PRSI cap)               (31,875)
                                               -------
CT payable                                           0

R&D credit excess / payable                     
(if credit > tax liability, refundable
in 3 instalments per Section 766C — N/A here
because credit was fully used)                       0
```

**Preliminary tax (small company):** Because TechCo is a "small company" (CT liability ≤ €200,000), it may use the prior-year (zero) test — no preliminary tax due. The 2026 preliminary tax will be 90% of 2026 estimate or 100% of 2025 (€0), whichever is lower-risk.

**Filing:** Form CT1 via ROS by 23 September 2026 (9 months after FY-end, 23rd of that month) with iXBRL accounts.

### 6.2 Mid-Size MNE — Pillar Two In Scope

**Facts:** GlobalCo Ireland Ltd, Irish-resident, fiscal year 1 January 2025 – 31 December 2025. Wholly owned by US-headquartered group with consolidated revenue €1.2 billion for FY 2024 and FY 2023 (in scope of Pillar Two from FY 2025 since €750M threshold met for 2 of last 4 FYs).

- Trading profit (Case I): €40,000,000.
- Foreign branch dividend income (Case III, qualifying for Section 626B exemption on capital portion; passive dividend portion): €3,000,000.
- Substance: 80 Irish employees with payroll cost €8,000,000; tangible assets net book value €15,000,000.

**Computation — Ireland CT layer:**

```
Case I trading profit                        40,000,000
CT @ 12.5%                                    5,000,000

Case III foreign dividend (passive)           3,000,000
CT @ 25%                                        750,000
Less: foreign tax credit (Schedule 24)        (450,000)  [assume 15% foreign WHT]
                                              ---------
Net CT on Case III                              300,000

Total Irish CT before Pillar Two              5,300,000
```

**Pillar Two ETR test (Irish jurisdiction):**

```
GloBE Income (simplified) =                  43,000,000
Adjusted Covered Taxes =                      5,300,000
ETR = 5,300,000 / 43,000,000 =                    12.33%

Required minimum =                                15.00%
Shortfall =                                         2.67%

Substance-Based Income Exclusion (SBIE) — 2025 rates:
  9.8% × payroll  9.8% × 8,000,000 =          784,000
  7.8% × tangible 7.8% × 15,000,000 =       1,170,000
                                            ---------
  SBIE total                                1,954,000

Excess profit = 43,000,000 − 1,954,000 =   41,046,000
Top-up tax = 2.67% × 41,046,000 =           1,095,928
```

**QDMTT collects this €1,095,928 in Ireland (rather than via the parent IIR).** The QDMTT is paid alongside CT but reported via the Pillar Two return / GIR.

**Conservative default applied:** Figures illustrative only — actual QDMTT computation requires the full GloBE rules, deferred-tax adjustments, transitional safe-harbour testing, and specialist software. This skill flags the in-scope position and routes to a Pillar Two specialist (R-IE-CT-4).

### 6.3 Mixed Trading and Rental Company

**Facts:** PropTradeCo Ltd, accounting period FY 2025.
- Case I trading profit: €200,000.
- Case V Irish rental profit (net): €80,000.
- Close company; undistributed Case V income at 18-month mark.

```
CT on Case I @ 12.5% × 200,000               25,000
CT on Case V @ 25%  ×  80,000                20,000
                                             ------
Total CT                                     45,000

Close-company surcharge — Section 440
20% × undistributed Case V = 20% × 60,000*   12,000

* 80,000 net Case V less 25% CT (20,000) =
  60,000 distributable, assumed not
  distributed within 18 months
                                             ------
Total liability                              57,000
```

**Conservative default:** Discuss dividend strategy with reviewer to mitigate Section 440 surcharge.

## Section 7 — Filing and Payment Mechanics

### 7.1 Form CT1 via Revenue Online Service (ROS)

**CT1 panels table**

| Panel | Content |
| --- | --- |
| Company details | Name, CRO number, tax reference, residence status |
| Trading profits | Case I / Case II — including adjustments from accounts |
| Other income | Cases III, IV, V; chargeable gains |
| Capital allowances | Wear and tear, accelerated, Section 291A intangibles |
| Losses and reliefs | Section 396 / 396A / 396B / 397 / group relief Section 411 |
| R&D credit | Section 766 claim — qualifying expenditure, category breakdown |
| Knowledge Development Box | Section 769I election and computation |
| Foreign tax credit | Schedule 24 |
| Close company | Section 440 / 441 surcharge computation |
| Transfer pricing | Section 835G certification |
| Pillar Two | Scope confirmation (separate Pillar Two return for in-scope groups) |
| iXBRL upload | Statutory accounts in iXBRL format |

- **CT1 filing method** — The Form CT1 is the sole CT return. Filed electronically via ROS (Revenue Online Service) using ROS Digital Cert.

### 7.2 iXBRL Filing — Section 884 TCA

**iXBRL requirement table**  _(Section 884 TCA)_

| Category | Requirement |
| --- | --- |
| Large Cases Division companies | iXBRL mandatory from 1 October 2013 |
| All other CT-paying companies | iXBRL mandatory from 1 October 2014 |
| Exclusion | Very small "iXBRL-exempt" companies (turnover < €8.8m, balance sheet < €4.4m, < 50 employees — 2 of 3 tests) **may** be exempt but Revenue strongly recommends iXBRL filing |

- **Tags and upload** — Mandatory iXBRL for most companies. Tags follow the Irish FRS 101 / FRS 102 / IFRS taxonomy published by Revenue. Upload via ROS within 3 months of CT1 due date if not concurrent.  _(Section 884 TCA)_

### 7.3 Preliminary Tax (Sections 958–959 TCA)

- **Small company definition** — CT liability ≤ €200,000 in prior accounting period. EUR  _(Sections 958–959 TCA)_
- **Small company preliminary tax** — Single instalment = lower of (a) 90% of current-year CT or (b) 100% of prior-year CT. Due: 23rd day of the month preceding the last month of the accounting period (i.e., for a 31 December year-end → 23 November).  _(Sections 958–959 TCA)_
- **Large company preliminary tax** — First instalment = 50% of prior-year CT (or 45% of current-year CT) — due in month 6 (i.e., 23rd day of the 6th month of the accounting period; 23 June for a calendar-year company). Second instalment = top-up to bring total to lower of 90% of current-year or 100% of prior-year — due in month 11 (23rd day of month 11; 23 November).  _(Sections 958–959 TCA)_
- **Final balance** — Due on filing of the CT1 within 9 months of the accounting period end (23rd day of that 9th month for ROS users).  _(Sections 958–959 TCA)_

### 7.4 Filing Deadlines

**Filing deadlines table**

| Item | Deadline |
| --- | --- |
| Form CT1 | 9 months after accounting period end, **by the 23rd day of that month** (Section 959AA) |
| iXBRL accounts | Concurrent with CT1 (some categories within 3 months thereafter) |
| Preliminary tax — small company (single payment) | 23rd day of month preceding last month of AP |
| Preliminary tax — large company (instalment 1) | 23rd day of month 6 of AP |
| Preliminary tax — large company (instalment 2) | 23rd day of month 11 of AP |
| R&D credit refund instalments | Per Section 766C 3-instalment schedule |
| Pillar Two GIR (first year transitional) | 30 June 2026 for FY 2024; 18 months after FY-end |
| Pillar Two GIR (subsequent years) | 15 months after FY-end |

### 7.5 Surcharges and Penalties

**Surcharges and penalties table**

| Infraction | Penalty |
| --- | --- |
| Late filing of CT1 (≤ 2 months late) | 5% surcharge on CT liability, capped at €12,695 |
| Late filing of CT1 (> 2 months late) | 10% surcharge on CT liability, capped at €63,485 |
| Restriction of reliefs on late filing | Section 959AC TCA — losses, group relief, R&D credit restricted by 50% (capped at €158,715 / €31,740) |
| Late payment of CT | Interest at **0.0219% per day** (~8% per annum) — Section 1080 TCA |
| Failure to file iXBRL | Tax-geared penalty up to €4,000 (Section 884) plus restriction of CT1 receipt |
| Negligent return | Up to 100% of tax shortfall; reduced via qualifying disclosure under Code of Practice for Revenue Audit |
| Deliberate default | Up to 100%, publication on tax defaulters list (Section 1086) |
| Pillar Two non-compliance | Tax-geared penalties under Part 4A and §1086 publication risk |

### 7.6 Statute of Limitations — Section 959AA TCA

- **Statute of limitations** — Standard: 4 years from the end of the chargeable period in which the return was filed. Unlimited in cases of fraud or neglect (Section 956 / 1077E).  _(Section 959AA TCA)_

## Section 8 — Conservative Defaults Summary

**Conservative defaults summary table**

| Item | Default |
| --- | --- |
| Trading vs non-trading split unclear | Treat as non-trading (25%) |
| Pillar Two scope | Out of scope unless €750M revenue confirmed for 2/4 FYs |
| R&D credit | Do not claim without Frascati Manual contemporaneous record |
| KDB | Do not elect without tracking-and-tracing and nexus computation |
| Section 110 | Do not opine without specialist sign-off |
| Close-company status | Assume yes for owner-managed; flag Section 440/441 |
| Group relief | None without 75% beneficial-ownership documentation |
| TP documentation | Required if consolidated group revenue ≥ €50M (local file) or ≥ €250M (master file) |
| Functional currency | EUR unless Section 402 election documented |
| Foreign dividend exemption (Section 831B) | Do not elect without 5%/12-month confirmation |
| Outbound payments | Screen for Section 817U defensive-measure WHT |
| Preliminary tax | Pay on the safer of 100% prior-year / 90% current-year |
| Loss carry-back | Verify same-trade continuity before applying Section 396A |
| iXBRL exemption | Do not assume; default to mandatory filing |
| Late filing | Never strategise around 5%/10% surcharge — file by 23rd |

## Section 9 — Cross-References

**Cross-references table**

| Topic | Skill |
| --- | --- |
| Personal income tax / Form 11 (sole trader) | `ie-income-tax-form11` |
| Universal Social Charge | `ie-usc` |
| PRSI Class S (self-employed) | `ie-prsi-class-s` |
| VAT (VAT3 / annual RTD) | `ireland-vat-return` |
| Preliminary income tax (individuals) | `ie-preliminary-tax` |
| Foundation principles | `foundation` |
| EU VAT Directive cross-border | `eu-vat-directive` |
| Intake checklist | `intake` |

## Section 10 — Sources

**Taxes Consolidation Act 1997 (TCA 1997)** — consolidating Act for all Irish direct taxes.
  - Section 21 — 12.5% trading rate.
  - Section 21A — 25% non-trading rate.
  - Section 23A — corporate residence test.
  - Section 27 — accounting periods.
  - Section 28 — chargeable gains and Section 78 gross-up.
  - Sections 76–87 — general computational rules (Case I/II Schedule D).
  - Sections 81, 82 — wholly-and-exclusively test; pre-trading expenditure.
  - Sections 110, 110(5A) — securitisation companies.
  - Section 130 — distributions recharacterisation.
  - Section 172A — dividend withholding tax.
  - Sections 284–321 — capital allowances (plant, industrial buildings, motor vehicles).
  - Section 291A — specified intangibles.
  - Sections 396, 396A, 396B, 396C, 397 — trading losses and terminal loss.
  - Sections 411–429 — group relief.
  - Section 430 et seq. — close companies; Sections 440, 441 surcharges.
  - Section 486C — start-up relief.
  - Section 626B — substantial shareholding exemption.
  - Section 766 — R&D tax credit (30% from FA 2024).
  - Section 766C — refundable R&D credit instalments.
  - Sections 769G–769R — Knowledge Development Box.
  - Section 811C, 811D — general anti-avoidance rule and protective notification.
  - Section 817U — outbound payments defensive measure (FA 2023).
  - Section 831B — participation exemption on foreign dividends (FA 2024, effective 1 January 2025).
  - Part 35A (Sections 835A–835HB) — transfer pricing.
  - Sections 835AG–835AY — ATAD II anti-hybrid rules.
  - Section 835AY — ATAD I interest limitation rule.
  - Sections 884 — iXBRL filing.
  - Section 891H — CbCR.
  - Sections 958–959 — preliminary tax.
  - Sections 959AA–959AC — return filing, surcharges, restriction of reliefs.
  - Section 1077E — tax-geared penalties; qualifying disclosure.
  - Section 1080 — interest on overdue tax.
  - Section 1086 — publication of tax defaulters.
  - **Part 4A TCA 1997** — Pillar Two (inserted by Finance (No. 2) Act 2023).
- **Schedule 24 TCA 1997** — double taxation relief / foreign tax credit pooling.

- **Finance (No. 2) Act 2023** — introduction of Part 4A Pillar Two (IIR, QDMTT, transitional safe harbours).
- **Finance Act 2024** — UTPR effective 31 December 2024; R&D credit raised to 30%; KDB extended to 31 December 2026; Section 831B participation exemption; Section 486C start-up relief extension.
- **Finance Act 2025** — annual updates (subject to confirmation at signing).

- **Council Directive (EU) 2022/2523** of 14 December 2022 — Pillar Two minimum tax directive.
- **OECD GloBE Model Rules** (December 2021), Commentary, Administrative Guidance (multiple releases 2023–2025).
- **OECD Transfer Pricing Guidelines for Multinational Enterprises and Tax Administrations 2022**.
- **OECD Frascati Manual 2015** — definition of R&D for Section 766 purposes.

- **Tax and Duty Manual (TDM) Part 04** — Cases of Schedule D and Schedule F.
- **TDM Part 04-09** — Section 110 companies.
- **TDM Part 04-06** — KDB.
- **TDM Part 29** — R&D Tax Credit Guidelines.
- **TDM Part 35A** — Transfer Pricing.
- **TDM Part 4A** — Pillar Two compliance.
- **Code of Practice for Revenue Audit and other Compliance Interventions** (2024 edition).
- **Revenue eBriefs** — periodic updates; subscribe via Revenue.ie.
- **ROS / Revenue Online Service** — filing portal: revenue.ie/en/online-services/ros/.

- **Companies Act 2014** — statutory accounts framework.
- **FRS 102 / FRS 101 / IFRS** — applicable accounting standards.
- **CRO** — Companies Registration Office (Form B1 annual return — separate from CT, but cross-referenced for compliance).

## PROHIBITIONS

- NEVER apply the 12.5% trading rate to passive income — Section 21A imposes 25%.
- NEVER apply the Knowledge Development Box without a documented nexus computation and tracking-and-tracing system.
- NEVER claim the R&D tax credit without a Frascati Manual-compliant technical record.
- NEVER assume Pillar Two is out of scope — verify the €750M consolidated revenue 2-of-4-FY test.
- NEVER compute QDMTT / IIR / UTPR without specialist GIR software and CTA engagement (R-IE-CT-4).
- NEVER ignore the close-company surcharges (Sections 440, 441) for owner-managed companies.
- NEVER deduct depreciation per accounts — use Section 284 capital allowances.
- NEVER deduct entertainment expenses (Section 840).
- NEVER deduct corporation tax itself or penalty interest under Section 1080.
- NEVER carry forward trading losses outside the same-trade continuity rule (Section 396).
- NEVER claim group relief without 75% beneficial ownership and EU/EEA/treaty residence (Section 411 / 420C).
- NEVER ignore the Section 291A 80% trading-income cap on specified intangibles.
- NEVER assume iXBRL exemption — default to filing.
- NEVER file the CT1 after the 23rd day of the 9th month — surcharge is automatic (Section 959AA).
- NEVER advise late preliminary tax — Section 1080 interest is daily and material.
- NEVER apply Section 110 without specialist counsel — Section 110(5A) Irish-property carve-out is technical.
- NEVER assume same-period correspondence in group relief — periods must overlap for the relevant portion.
- NEVER skip transfer pricing documentation for groups ≥ €50M consolidated revenue (Section 835G).
- NEVER bypass anti-hybrid (Sections 835AG–835AY) screening on cross-border related-party flows.
- NEVER stack R&D credit and KDB on the same expenditure without confirming nexus exclusion.
- NEVER apply the Section 831B participation exemption without 5% / 12-month holding evidence.
- NEVER present figures as definitive — always label as estimates pending CTA reviewer sign-off.

## Disclaimer

This skill and its outputs are for informational and computational purposes only and do not constitute tax, legal, or financial advice. All outputs must be reviewed and signed off by a qualified Irish tax adviser (CTA, AITI, ACA or ACCA holding tax qualification, or solicitor / barrister authorised in tax) before filing or acting upon. Pillar Two computations specifically require specialist GIR software and credentialed Pillar Two practitioner sign-off. The latest verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com).

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
