---
name: ph-income-tax
description: >
  Check Philippine individual income tax for calendar year 2025 using a bounded
  reference for sole proprietors and individual professionals. Use for graduated
  rates, the 8% option, optional standard deduction, itemised expenses, quarterly
  and annual returns or BIR penalties. Establish citizenship, residence, income
  source, registration and the actual annual elections before choosing a method.
  This draft preserves conditional arithmetic examples and dated guidance for the
  corresponding annual return in 2026. It does not establish complete current law,
  taxpayer entitlement, a payable balance, a complete country workflow or filing
  readiness. Refer unresolved facts, law and procedures to a qualified Philippine
  practitioner before acting.
jurisdiction: PH
category: international
tax_year: 2025
tax_year_notes: >
  Historical calendar-year 2025 reference. Includes the dated 2026 guidance for
  that annual return, including RMC 30-2026's extension of covered obligations.
  Sources read on 5 November 2026 do not establish a complete 2026 law position,
  an exhaustive amendment or extension history, or an inspected filing workflow.
last_updated: 2026-11-05
version: 1.1
tier: 1
reviewed_by: "Jonathan I. Ruiz"
reviewed_on: 2026-11-03
depends_on:
  - income-tax-workflow-base
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
domain: income-tax
---

# Philippines individual income tax reference v1.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Who this applies to

This Tier 2 draft covers selected ordinary income-tax rules for individual sole proprietors and professionals for calendar year 2025. Establish the taxpayer's citizenship, residence and income source. TRAIN's amended NIRC 24(A) covers a resident citizen's ordinary taxable income from Philippine and foreign sources, whilst its nonresident-citizen and resident-alien categories use Philippine-source income. Separate compensation, ordinary business or professional income, exempt income and income subject to final or separate capital-gains tax before applying the table. A bank account or payment address does not determine source or residence. Source: [TRAIN s 5, complete 24(A), signed physical pp 3–4](https://lawphil.net/statutes/repacts/ra2017/pdf/ra_10963_2017.pdf).

Load income-tax-workflow-base and its workflow-base dependency. Their source, period, intake, refusal, output and execution requirements remain mandatory. This reference does not fill the complete country companion contract. Its 3 fixtures are arithmetic illustrations, below the universal minimum of 5 fully worked positions. Missing required facts, law, source conditions, refusal definitions or execution capability means **Needs Input**, with no deliverable financial result.

Use PHP only for these illustrations. **Not yet confirmed:** complete amendment continuity for the covered period, current VAT threshold/indexation and recognition rules, all country slots, the actual taxpayer's eligibility and elections, losses, credits, foreign-currency treatment and full procedural compliance. No return, payment, amendment or tax position is authorised by this reference.

The inherited referral catalogue remains:

| Reference | Stop or refer condition |
| --- | --- |
| R-PH-1 | Corporation or partnership. This reference covers individual sole proprietors and professionals. Route corporations to the corporate income-tax companion. Partnership classification, including a general professional partnership (GPP) and its partners, needs separate qualification; do not assume every partnership uses the same corporate return. |
| R-PH-2 | VAT registration or a VAT transition. The 8% option is unavailable to VAT-registered taxpayers. Ordinary individual income tax may still apply, but the complete VAT, registration and filing workflow is outside this reference. Do not produce a return from this draft. |
| R-PH-3 | Mixed employment and business income. The eligible business component may have an 8% option, whilst compensation follows its own graduated treatment. The business reduction and annual-form rules differ. Obtain a qualified combined computation. |
| R-PH-4 | Nonresident alien, whether engaged or not engaged in Philippine trade or business. Outside this reference. The historical OSD texts have a scope tension; they do not resolve this taxpayer's entitlement. |

Sources for the scope and 8% distinctions: [TRAIN s 5](https://lawphil.net/statutes/repacts/ra2017/ra_10963_2017.html), [RMO 23-2018 II.1–16](https://elibrary.judiciary.gov.ph/thebookshelf/showdocs/10/90318), [RA 9504 s 3](https://elibrary.judiciary.gov.ph/thebookshelf/showdocs/2/8724) and [RR 2-2010 s 3](https://elibrary.judiciary.gov.ph/thebookshelf/showdocs/10/50806). The 4 local referrals do not replace the complete refusal catalogues in the workflow bases.

## Rates, bands and thresholds

The following TRAIN table commenced on 1 January 2023. Its amounts and statutory boundaries are preserved for this historical 2025 reference. First qualify ordinary net taxable income under 24(A); turnover, compensation and a separately taxed receipt are not interchangeable bases.

| Ordinary net taxable income in PHP | Tax before qualified credits | Primary source |
| --- | --- | --- |
| Not over 250,000 | 0% | [TRAIN s 5, 24(A)(2)(a), signed physical p 4](https://lawphil.net/statutes/repacts/ra2017/pdf/ra_10963_2017.pdf). |
| Over 250,000 but not over 400,000 | 15% of the excess over 250,000 | [TRAIN s 5, 24(A)(2)(a), signed physical p 4](https://lawphil.net/statutes/repacts/ra2017/pdf/ra_10963_2017.pdf). |
| Over 400,000 but not over 800,000 | 22,500 plus 20% of the excess over 400,000 | [TRAIN s 5, 24(A)(2)(a), signed physical p 4](https://lawphil.net/statutes/repacts/ra2017/pdf/ra_10963_2017.pdf). |
| Over 800,000 but not over 2,000,000 | 102,500 plus 25% of the excess over 800,000 | [TRAIN s 5, 24(A)(2)(a), signed physical p 4](https://lawphil.net/statutes/repacts/ra2017/pdf/ra_10963_2017.pdf). |
| Over 2,000,000 but not over 8,000,000 | 402,500 plus 30% of the excess over 2,000,000 | [TRAIN s 5, 24(A)(2)(a), signed physical p 4](https://lawphil.net/statutes/repacts/ra2017/pdf/ra_10963_2017.pdf). |
| Over 8,000,000 | 2,202,500 plus 35% of the excess over 8,000,000 | [TRAIN s 5, 24(A)(2)(a), signed physical p 4](https://lawphil.net/statutes/repacts/ra2017/pdf/ra_10963_2017.pdf). |

Use the statutory 'over' and 'not over' tests. The inherited whole-peso lower labels must not create gaps for fractional amounts. The blank 1701Q contains both the earlier and 2023 schedules and separate whole-peso return instructions; those instructions do not establish every actual-year form's rounding. Sources: [TRAIN s 5](https://lawphil.net/statutes/repacts/ra2017/pdf/ra_10963_2017.pdf) and [blank 1701Q, January 2018, p 2](https://bir-cdn.bir.gov.ph/local/pdf/1701Q%20Jan%202018%20final%20rev2_copy.pdf).

| Alternative or threshold | Conditioned starting point | Primary source and qualification |
| --- | --- | --- |
| 8% option | For an eligible individual earning purely from self-employment or profession, 8% of gross sales/receipts **and other non-operating income** in excess of PHP 250,000, in lieu of the graduated income tax and NIRC 116 percentage tax. | [TRAIN s 5, 24(A)(2)(b)](https://lawphil.net/statutes/repacts/ra2017/ra_10963_2017.html); [RMO 23-2018 II.1–16](https://elibrary.judiciary.gov.ph/thebookshelf/showdocs/10/90318). Eligibility, scope and election below are essential. |
| Mixed income | Compensation follows graduated treatment. An eligible, elected 8% business component receives **no PHP 250,000 business reduction**, including no transfer of an unused compensation threshold. | [TRAIN s 5, 24(A)(2)(c)](https://lawphil.net/statutes/repacts/ra2017/ra_10963_2017.html); [RMO 23-2018 II.3 and II.11](https://elibrary.judiciary.gov.ph/thebookshelf/showdocs/10/90318). Combined execution remains referred. |
| Statutory 8% ceiling | The read RMO uses gross sales/receipts **plus other non-operating income** not exceeding PHP 3,000,000. Being non-VAT and below that number alone does not establish entitlement. | [RMO 23-2018 II.1–16](https://elibrary.judiciary.gov.ph/thebookshelf/showdocs/10/90318). **Not yet confirmed:** complete 2025 threshold/indexation and later registration chain. Verify before applying to an actual taxpayer. |

RMO 23-2018 also requires registration and a valid election. Its exclusions include VAT registration, other percentage-tax categories, GPP partner income and the specified exempt/BMBE cases. Read the complete applicable conditions and income sources; do not grant 8% merely because the receipt total is small. Books and invoices remain required under its II.13–14. The 8% regime provides no separate business-expense deduction from that base. Source: [RMO 23-2018 II.1–16](https://elibrary.judiciary.gov.ph/thebookshelf/showdocs/10/90318).

## The base

Keep the 8% regime election separate from the choice of itemised deductions or OSD under graduated taxation. Establish the actual yearly choices from registration and filed returns. Unknown election, deduction method or VAT status means Needs Input. The historical statutory fallback is not permission to invent facts or choose OSD retrospectively.

| Method | Computation and controls | Primary support |
| --- | --- | --- |
| Graduated, itemised | Reconcile legally recognised business sales/receipts, direct costs and all other ordinary taxable income. Deduct only qualifying expenses once, with the correct timing and business/private allocation. Apply the graduated table to the resulting qualified taxable income. | [NIRC 34, historical text](https://lawphil.net/statutes/repacts/ra1997/ra_8424_1997.html); [blank 1701Q pp 1–2](https://bir-cdn.bir.gov.ph/local/pdf/1701Q%20Jan%202018%20final%20rev2_copy.pdf). Complete current base and deduction rules remain unconfirmed. |
| Graduated, individual OSD | Eligible individuals may elect up to 40% of gross sales/receipts. RR 16-2008 distinguishes accrual sales from cash receipts and prevents subtracting direct costs to determine this OSD base. Do not subtract direct costs and then take OSD from the reduced amount. | [RA 9504 s 3](https://elibrary.judiciary.gov.ph/thebookshelf/showdocs/2/8724); [RR 16-2008 ss 2–3](https://elibrary.judiciary.gov.ph/thebookshelf/showdocs/10/43850). The actual deduction rate and accounting method must qualify. |
| OSD and other income | The blank 1701A applies its OSD to net business sales/receipts and adds other income separately. The individual provisions do not supply a universal deduction of 40% from every other-income receipt. Do not import the corporate gross-income base. | [Blank 1701A p 2, items 36–46](https://bir-cdn.bir.gov.ph/local/pdf/1701A%20Jan%202018%20v5%20with%20rates.pdf); [RR 16-2008 s 3](https://elibrary.judiciary.gov.ph/thebookshelf/showdocs/10/43850). Classify and qualify the actual other income. |
| OSD election and records | RR 2-2010 requires the deduction choice in the first-quarter return, annual consistency and irrevocability. Without an OSD election, including failure to file a required first-quarter return, the text supplies the itemised fallback. Financial-statement attachment relief retains records of gross sales/receipts. | [RR 2-2010 s 3, amended s 7](https://elibrary.judiciary.gov.ph/thebookshelf/showdocs/10/50806). **Not yet confirmed:** later continuity, eligibility and corrective procedures. Itemised fallback does not prove expenses. |
| NIRC 116 percentage tax | EOPT's amended 116 imposes 3% on gross quarterly **sales** of the specified non-VAT persons exempt under 109(CC), with the cooperative exception. Its temporary 1% period ended on 30 June 2023. This is not a universal charge on all non-VAT receipts or a deduction under 8%. | [EOPT s 24, signed physical p 12](https://lawphil.net/statutes/repacts/ra2024/pdf/ra_11976_2024.pdf). **Not yet confirmed:** complete 2025 recognition, transition, threshold and procedural rules. |

EOPT s 5 repeals NIRC 34(K) and renumbers the succeeding paragraph. The inherited OSD citation '34(L)' describes the older provision and must be read with that amendment. Do not reinstate the repealed general withholding prerequisite for deductions. The separate regulatory withholding condition in RR 10-2002's entertainment rule still requires reconciliation. Sources: [EOPT s 5, signed physical p 3](https://lawphil.net/statutes/repacts/ra2024/pdf/ra_11976_2024.pdf) and [RR 10-2002 s 4](https://lawphil.net/administ/bir/rr/rr10_02.pdf).

The inherited expense categories require individual qualification:

| Itemised category | Conditioned treatment or specific hold | Primary support |
| --- | --- | --- |
| Direct costs | No blanket deduction from a label. **Not yet confirmed:** applicable inventory, cost recognition and timing rules. Never deduct the same cost again as an expense or under individual OSD. | [NIRC 34(A), historical text](https://lawphil.net/statutes/repacts/ra1997/ra_8424_1997.html); [RR 16-2008 s 3](https://elibrary.judiciary.gov.ph/thebookshelf/showdocs/10/43850). |
| Salaries and wages | Reasonable compensation for services actually rendered, with the statutory fringe-benefit conditions and substantiation. A 'BIR-registered payroll' alone proves no deduction. | [NIRC 34(A)(1)(a)(i) and (b), historical text](https://lawphil.net/statutes/repacts/ra1997/ra_8424_1997.html). |
| Business rent | Reasonable required payments for continued business use or possession, subject to the statutory title/equity conditions and evidence. | [NIRC 34(A)(1)(a)(iii) and (b), historical text](https://lawphil.net/statutes/repacts/ra1997/ra_8424_1997.html). |
| Utilities | Conditional ordinary and necessary business expense; establish amount, business connection and allocation. **Not yet confirmed:** actual-year entitlement and timing. | [NIRC 34(A)(1), historical text](https://lawphil.net/statutes/repacts/ra1997/ra_8424_1997.html). |
| Professional fees | Apply the ordinary/necessary, business-connection and substantiation tests. A professional recipient or invoice description alone is insufficient. | [NIRC 34(A)(1), historical text](https://lawphil.net/statutes/repacts/ra1997/ra_8424_1997.html). |
| Depreciation | Conditional reasonable allowance for qualifying business property, with applicable method, basis and useful-life rules. **Not yet confirmed:** the asset's current allowance and amount. | [NIRC 34(F), historical text](https://lawphil.net/statutes/repacts/ra1997/ra_8424_1997.html). |
| Bad debts | Business connection, actual ascertainment of worthlessness and charge-off within the year, related-party exclusion and recovery rule apply. Write-off alone is insufficient. Securities require their separate classification. | [NIRC 34(E), historical text](https://lawphil.net/statutes/repacts/ra1997/ra_8424_1997.html); [CMEPA s 9](https://lawphil.net/statutes/repacts/ra2025/ra_12214_2025.html). **Not yet confirmed:** complete 2025 securities transition and entitlement. |
| Business interest | CREATE reduces otherwise allowable interest by 20% of **interest income subjected to final tax**, with a future-rate adjustment clause. Business-debt, timing, related-party, exclusion and capitalisation conditions remain. | [CREATE s 9](https://lawphil.net/statutes/repacts/ra2021/ra_11534_2021.html); [NIRC 34(B), historical text](https://lawphil.net/statutes/repacts/ra1997/ra_8424_1997.html). **Not yet confirmed:** current adjustment chain and the inherited categorical tax-deficiency-interest exclusion, which these read units do not establish. |
| Pension trusts | Distinguish qualifying current-liability contributions from excess contributions apportioned over 10 years and not previously deducted. No blanket immediate deduction. | [NIRC 34(J), historical text](https://lawphil.net/statutes/repacts/ra1997/ra_8424_1997.html). CMEPA's separate conditional PERA addition does not replace this trust rule; later continuity remains unconfirmed. |
| Research and development | Business connection, current-expense or qualifying deferred election, amortisation and exclusions apply. The historical deferred rule uses at least 60 months from when benefits arise. | [NIRC 34(I), historical text](https://lawphil.net/statutes/repacts/ra1997/ra_8424_1997.html). **Not yet confirmed:** authenticated election timing, later continuity and actual entitlement. |

| Former disallowance category | Corrected scope | Primary support |
| --- | --- | --- |
| Personal and family expenses | Disallowed personal/living/family costs; establish the business/private split rather than assume it. | [NIRC 36(A)(1), historical text](https://lawphil.net/statutes/repacts/ra1997/ra_8424_1997.html). |
| Capital expenditure | The specified capital, improvement and restoration amounts are not ordinary current deductions. This does not make every capital item depreciable; statutory exceptions and asset rules matter. | [NIRC 36(A)(2)–(3), historical text](https://lawphil.net/statutes/repacts/ra1997/ra_8424_1997.html). |
| Income tax | Income tax under this Title is disallowed. Foreign income taxes have separate deduction/credit-election conditions; no universal foreign-tax answer is supplied. | [NIRC 34(C), historical text](https://lawphil.net/statutes/repacts/ra1997/ra_8424_1997.html). |
| Losses linked to exempt income | The read historical 34(D)(3) specifically excludes NOLCO incurred whilst the taxpayer was exempt. **Not yet confirmed:** the broader inherited 'all losses from tax-exempt income' claim and current loss rules. | [NIRC 34(D)(3), historical text](https://lawphil.net/statutes/repacts/ra1997/ra_8424_1997.html). |
| Bribes and kickbacks | The statutory direct/indirect payments to the specified public/private recipients are disallowed. | [NIRC 34(A)(1)(c), historical text](https://lawphil.net/statutes/repacts/ra1997/ra_8424_1997.html). |
| Entertainment, amusement and recreation | Qualifying reasonable, substantiated business expenses are conditionally deductible. RR 10-2002 ceilings are 0.50% of **net sales** for goods/property and 1% of **net revenue** for services/profession, with mixed-business allocation and the regulation's exclusions and requisites. | [RR 10-2002 ss 2–5](https://lawphil.net/administ/bir/rr/rr10_02.pdf). **Not yet confirmed:** complete later continuity and reconciliation of its withholding predicate after EOPT's repeal of 34(K). Do not use the ceiling as automatic entitlement. |



**Not yet confirmed:** the inherited blanket '12% VAT instead' simplification, actual VAT rates, bases and exemptions, 2550Q/2550M applicability and the complete registration/reporting calendar. Qualify these VAT leads separately before a deliverable.

## Deadlines and filing

| Return or action | Statutory or dated position | Remaining checks and source |
| --- | --- | --- |
| 1701Q, first 3 quarters | TRAIN's amended 74(A)–(B) and the blank-form guide state 15 May, 15 August and 15 November of the current year. The annual return completes the year; do not invent a fourth 1701Q. The inherited generic '45 days' formula is incorrect. | [TRAIN s 20, signed physical p 11](https://lawphil.net/statutes/repacts/ra2017/pdf/ra_10963_2017.pdf); [1701Q instructions](https://bir-cdn.bir.gov.ph/local/pdf/1701Q%20Guide%20Jan%202018_copy.pdf). Verify actual-year non-working-day rules, eFPS rules and extensions. |
| Covered 2025 annual return, tax payment and required attachments | RMC 20-2026 initially states 15 April 2026. Later **RMC 30-2026, dated 14 April 2026, extends these covered obligations from 15 April to 15 May 2026 without penalties**. | [RMC 20-2026 p 1](https://bir-cdn.bir.gov.ph/BIR/pdf/RMC%2020-2026.pdf); [RMC 30-2026, complete p 1](https://bir-cdn.bir.gov.ph/BIR/pdf/RMC%20No.%2030-2026.pdf). Do not extrapolate this dated relief to other years, fiscal deadlines or quarterly returns. Complete later guidance and actual compliance remain unconfirmed. |
| 1701 | The dated Annex C identifies individual business/professional taxpayers, including mixed earners, and other specified taxpayer classes, subject to the actual income/regime selection. | [RMC 20-2026 Annex C Q4–5](https://bir-cdn.bir.gov.ph/BIR/pdf/RMC%2020-2026%20Annex%20C%20%283%29.pdf). Actual form fields and complete instructions remain unconfirmed. |
| 1701A | Purely business/professional income with OSD under graduated rates or the 8% option. The inherited mixed-employee eligibility is incorrect. | [Blank 1701A pp 1–2](https://bir-cdn.bir.gov.ph/local/pdf/1701A%20Jan%202018%20v5%20with%20rates.pdf); [Annex C Q5](https://bir-cdn.bir.gov.ph/BIR/pdf/RMC%2020-2026%20Annex%20C%20%283%29.pdf). No final form choice from this reference. |
| Optional 1701-MS | Annex C offers the simplified return for qualifying micro/small taxpayers, including mixed earners, with a single business-income tax rate. It is not an exclusive requirement and does not require duplicate filing after a compliant 1701/1701A submission. | [Annex C Q1–5 and Q10–11](https://bir-cdn.bir.gov.ph/BIR/pdf/RMC%2020-2026%20Annex%20C%20%283%29.pdf). Actual form, entitlement and filing completion remain unconfirmed. |
| 2551Q | EOPT's amended 128 requires the covered quarterly percentage-tax return and payment within 25 days after each taxable quarter. This includes the fourth quarter when applicable. The earlier form also has separate other-percentage-tax categories. | [EOPT s 29](https://elibrary.judiciary.gov.ph/thebookshelf/showdocs/2/96948); [2551Q instructions](https://bir-cdn.bir.gov.ph/local/pdf/2551Q_%20Jan%202018%20Guide.pdf). Verify actual liability, base, ATC, channel and any special deadline. |

The annual statutory texts need reconciliation: original NIRC 51(C)(1) states 15 April, whilst TRAIN s 20's signed 74(B) says 15 May. RMC 20 then states the earlier date for the 2025 annual return and RMC 30 provides the dated extension above. Record the textual discrepancy rather than silently treating one provision as a complete amendment history. **Not yet confirmed:** a complete legal reconciliation and all later relief. Sources: [historical NIRC 51(C)](https://lawphil.net/statutes/repacts/ra1997/ra_8424_1997.html), [signed TRAIN s 20, physical p 11](https://lawphil.net/statutes/repacts/ra2017/pdf/ra_10963_2017.pdf), [RMC 20](https://bir-cdn.bir.gov.ph/BIR/pdf/RMC%2020-2026.pdf) and [RMC 30](https://bir-cdn.bir.gov.ph/BIR/pdf/RMC%20No.%2030-2026.pdf).

The channels changed during the filing period. RMC 20 Annex C's manual 1701-MS option and then-unavailable eBIRForms/eFPS position are dated guidance. **RMC 36-2026, dated 28 April 2026, announces inclusion of 1701-MS August 2024 in Offline eBIRForms 7.9.6.0.** It does not establish eFPS availability or an inspected portal today. RMC 30 also states electronic filing/payment and manual payment at the nearest AAB notwithstanding RDO jurisdiction. Do not keep the earlier manual-only premise as current. Sources: [Annex C Q6–9](https://bir-cdn.bir.gov.ph/BIR/pdf/RMC%2020-2026%20Annex%20C%20%283%29.pdf), [RMC 36 item 1](https://bir-cdn.bir.gov.ph/BIR/pdf/RMC%20No.%2036-2026.pdf) and [RMC 30](https://bir-cdn.bir.gov.ph/BIR/pdf/RMC%20No.%2030-2026.pdf).

For the 8% election, RMO 23-2018 distinguishes new-registration forms from existing-taxpayer routes. For existing taxpayers, II.7.2 lists the 1905 route together with selecting 8% on the initial quarterly ITR, the first quarterly 2551Q and/or the standalone first quarterly 1701Q route. Annual election is required. The choice is irrevocable for that taxable year. After the specified threshold breach, its II.15 requires graduated income tax, credit for earlier 8% income-tax payments, registration update within the following month and VAT prospectively from the **first day of the following month**, with the stated earlier-period percentage-tax consequence. The inherited 'VAT from the month breached' statement is incorrect. Source: [RMO 23-2018 II.1–16 and III.A](https://elibrary.judiciary.gov.ph/thebookshelf/showdocs/10/90318). **Not yet confirmed:** complete 2025 continuity, current forms and update procedures, VAT recognition and the actual taxpayer's transition.

The blank 1701Q illustrates cumulative business income and earlier payments/credits, with compensation reported on the annual return. Its credit boxes and 2307/SAWT attachments do not establish entitlement from an unverified certificate. EOPT's amended 58(E) requires the income declaration and fact of withholding for the credit/refund claim. Obtain the evidence and reconcile it without double crediting. Sources: [1701Q pp 1–2](https://bir-cdn.bir.gov.ph/local/pdf/1701Q%20Jan%202018%20final%20rev2_copy.pdf), [1701Q instructions](https://bir-cdn.bir.gov.ph/local/pdf/1701Q%20Guide%20Jan%202018_copy.pdf) and [EOPT s 9](https://elibrary.judiciary.gov.ph/thebookshelf/showdocs/2/96948).

**Not yet confirmed:** full RR 11-2018 withholding and filing-reference scope, current certificate/SAWT requirements, all actual-year return fields and instructions, remaining RMC 20 units and annexes, acknowledgements, amendments, retention, bank cut-offs and a completed filing/payment workflow. Forms 1901, 1905 and 2303 remain registration/intake leads, not verified current blank forms or proof of eligibility. No portal, submission or payment was exercised.

## Penalties and interest

The historical penalty correction was credited to **Jonathan I. Ruiz (CPA, Philippines)**. That contribution remains acknowledged; it does not mean that he approved this v1.1 rewrite or the full current penalty position.

| Event or classification | Conditioned reference position | Primary support and limits |
| --- | --- | --- |
| Ordinary civil default | EOPT's amended 248(A) retains the 25% civil penalty for its specified filing/payment defaults. Determine the actual default, tax base and relief before computing it. | [EOPT s 41](https://elibrary.judiciary.gov.ph/thebookshelf/showdocs/2/96948). This is not an automatic surcharge for every event labelled 'late'. |
| Micro and small taxpayers | RR 6-2024 covers micro taxpayers with annual gross sales **below PHP 3,000,000** and small taxpayers from **PHP 3,000,000 to below PHP 20,000,000**. Classification is not the same question as VAT or 8% eligibility. | [RR 6-2024 ss 1–2, official filed copy](https://naro.law.upd.edu.ph/storage/01JT28JRH6YRBG857QWTQ0JJFH.pdf). Exact classification/application for the actual year remains unconfirmed. |
| Reduced civil default | For covered micro/small taxpayers, RR 6 s 3 specifies 10% for its filing/payment defaults. No penalty applies to an amendment if the initial return and tax were timely. In an audit deficiency assessment, its civil penalty applies if the audited return was late. Willful neglect and false/fraudulent returns retain the separate 50% regime. | [RR 6-2024 s 3, pp 1–2](https://naro.law.upd.edu.ph/storage/01JT28JRH6YRBG857QWTQ0JJFH.pdf). Do not infer eligibility or an automatic penalty waiver from taxpayer size. |
| Interest | TRAIN 249(A) uses twice the BSP legal rate and prohibits concurrent deficiency/delinquency interest. BIR's RR 21-2018 **digest** describes 12%; RR 6 s 4 specifies the covered micro/small reduction to 6% and a later-rate circular mechanism. | [TRAIN s 75](https://lawphil.net/statutes/repacts/ra2017/ra_10963_2017.html); [BIR RR 21-2018 digest](https://bir-cdn.bir.gov.ph/local/pdf/RR%2021-2018.pdf); [RR 6-2024 s 4](https://naro.law.upd.edu.ph/storage/01JT28JRH6YRBG857QWTQ0JJFH.pdf). **Not yet confirmed:** full RR 21, current rate continuity, bases, dates, notices and accrual periods. No flat universal 12% computation. |
| Information-return failure | Historical 250 provides PHP 1,000 per failure, capped at PHP 25,000 per calendar year, with reasonable-cause/non-willful-neglect and notice/demand conditions. RR 6 s 5 specifies PHP 500 and a PHP 12,500 annual cap for its covered taxpayers. | [NIRC 250, historical text](https://lawphil.net/statutes/repacts/ra1997/ra_8424_1997.html); [RR 6-2024 s 5](https://naro.law.upd.edu.ph/storage/01JT28JRH6YRBG857QWTQ0JJFH.pdf). This is distinct from the income-tax-return offence below. Later continuity and actual application remain unconfirmed. |
| Substantial underdeclaration or overstated deductions | Under 248(B)/RR 6 s 3, the specified amount **exceeding 30%** is prima facie evidence of a false/fraudulent return, within the provision's 50% regime. Sales/income uses the declared amount; overstated deductions uses actual deductions. | [NIRC 248(B), historical text](https://lawphil.net/statutes/repacts/ra1997/ra_8424_1997.html); [RR 6-2024 s 3](https://naro.law.upd.edu.ph/storage/01JT28JRH6YRBG857QWTQ0JJFH.pdf). The inherited bare label is insufficient to establish fraud or a computed penalty. |
| Willful neglect or false/fraudulent return | The civil provision specifies 50% with its statutory conditions. Separate criminal liability requires the applicable offence and proof; no automatic criminal conclusion from a civil label. | [NIRC 248(B), historical text](https://lawphil.net/statutes/repacts/ra1997/ra_8424_1997.html); [RR 6-2024 s 3](https://naro.law.upd.edu.ph/storage/01JT28JRH6YRBG857QWTQ0JJFH.pdf). Refer an actual allegation, audit or notice to a qualified practitioner. |
| Willful failure covered by 255 | The read historical text requires willful failure and conviction: a fine of at least PHP 10,000 **and** imprisonment from one to 10 years. It does not prescribe a maximum fine in that clause. | [NIRC 255, historical text](https://lawphil.net/statutes/repacts/ra1997/ra_8424_1997.html). **Not yet confirmed:** complete current offence/amendment and procedural position. Ordinary late filing alone does not establish conviction. |
| Unregistered business | Captured CMEPA s 24's amended 258 requires conviction and specifies PHP 5,000–20,000 **and** 6 months–2 years for the ordinary offence; excise businesses have a separate rule. The inherited 'and/or' is incorrect for that captured wording. | [CMEPA s 24](https://lawphil.net/statutes/repacts/ra2025/ra_12214_2025.html). **Not yet confirmed:** authenticated amendment/commencement, earlier-2025 wording, transitional application and actual offence. Do not apply this row universally across 2025. |
| Compromise | RR 6 s 6's reduced schedule concerns specified non-fraud offences under 113/237/238 and a valid compromise agreement, with approval conditions and the applicable schedule. It is not a unilateral election to avoid prosecution. | [RR 6-2024 s 6](https://naro.law.upd.edu.ph/storage/01JT28JRH6YRBG857QWTQ0JJFH.pdf). No actual compromise amount or agreement is established. |

RR 6's applicability is prospective and its effectivity is tied to publication. The exact publication/effectivity chain, including the inherited EOPT '22 January 2024' statement, is **not yet confirmed** here. The old 1701Q/2551Q penalty instructions predate EOPT and must not override these qualified distinctions. No unresolved surcharge, interest, compromise or criminal exposure is zero.

## Cross-border points

TRAIN's 24(A) source/residence categories above require evidence before selecting income. Foreign-source business receipts, work performed abroad, foreign tax certificates, treaties, permanent establishments and final-tax financial income require their complete applicable rules. **Not yet confirmed:** source attribution, treaty entitlement, foreign-tax deduction or credit, currency conversion and the 2025 passive-income transition for the actual individual. The ordinary table is not a universal rate for those items. Sources for the limited starting distinctions: [TRAIN s 5](https://lawphil.net/statutes/repacts/ra2017/ra_10963_2017.html) and [NIRC 34(C), historical foreign-tax election text](https://lawphil.net/statutes/repacts/ra1997/ra_8424_1997.html). Refer the unresolved cross-border position before producing a result.

## Two worked examples that recompute

The 3 inherited examples remain as **fictional, conditional arithmetic**, not taxpayer findings or an available retrospective election. Assume purely self-employed Philippine ordinary business income, PHP 2,400,000 recognised net business sales/receipts, no other or compensation income, valid registration/election for each alternative, an applicable full 40% OSD where used, and no double-counted costs. For the percentage-tax illustrations, separately stipulate a legally qualified PHP 2,400,000 sales base under 116. Assume no credits, prior payments or penalties solely for this arithmetic; an unknown real amount is not zero.

1. **8% illustration.** The eligible graphic designer has no employees and a valid yearly 8% election. Applying the qualified purely self-employed reduction gives PHP 172,000. No separate 116 percentage tax or business-expense deduction applies under that stipulated regime. Books and invoices remain required.
2. **Graduated with OSD and a decision.** The stipulated full OSD is PHP 960,000, leaving PHP 1,440,000 taxable income. Graduated income tax is PHP 262,500 and the separately stipulated percentage tax is PHP 72,000, totalling PHP 334,500. The 8% illustration is PHP 162,500 lower **on these assumptions**. Choose between legally available prospective alternatives only after eligibility and elections qualify.
3. **Graduated with itemised deductions.** The consultant's PHP 1,800,000 must be fully allowable, correctly timed expenses, not merely documented spending. With the other assumptions unchanged, taxable income is PHP 600,000, graduated tax PHP 62,500 and percentage tax PHP 72,000, totalling PHP 134,500. That illustration is PHP 37,500 below the 8% figure. This does not establish a general 'expenses over 60%' selection rule.

Sources for the rates and bases: [TRAIN s 5](https://lawphil.net/statutes/repacts/ra2017/pdf/ra_10963_2017.pdf), [RMO 23-2018 II](https://elibrary.judiciary.gov.ph/thebookshelf/showdocs/10/90318), [RR 16-2008 s 3](https://elibrary.judiciary.gov.ph/thebookshelf/showdocs/10/43850), [RR 2-2010 s 3](https://elibrary.judiciary.gov.ph/thebookshelf/showdocs/10/50806), [EOPT s 24](https://lawphil.net/statutes/repacts/ra2024/pdf/ra_11976_2024.pdf) and [historical NIRC 34](https://lawphil.net/statutes/repacts/ra1997/ra_8424_1997.html). Complete law and taxpayer qualification remain held as disclosed above.

### Case 1 arithmetic

```oa-check
name: PH2025 eligible purely self-employed eight percent illustration
inputs:
  sales: 2400000
  reduction: 250000
steps:
  - eight_percent_base: max(sales - reduction, 0)
  - income_tax: eight_percent_base * 0.08
expected:
  eight_percent_base: 2150000
  income_tax: 172000
```

### Case 2 arithmetic

```oa-check
name: PH2025 eligible OSD versus eight percent prospective decision
inputs:
  sales: 2400000
  reduction: 250000
steps:
  - osd: sales * 0.40
  - taxable_income: sales - osd
  - graduated_tax: 102500 + (taxable_income - 800000) * 0.25
  - percentage_tax: sales * 0.03
  - osd_total: graduated_tax + percentage_tax
  - eight_percent: (sales - reduction) * 0.08
  - difference: osd_total - eight_percent
expected:
  osd: 960000
  taxable_income: 1440000
  graduated_tax: 262500
  percentage_tax: 72000
  osd_total: 334500
  eight_percent: 172000
  difference: 162500
```

### Case 3 arithmetic

```oa-check
name: PH2025 qualified itemised deductions conditional comparison
inputs:
  sales: 2400000
  allowable_expenses: 1800000
  reduction: 250000
steps:
  - taxable_income: sales - allowable_expenses
  - graduated_tax: 22500 + (taxable_income - 400000) * 0.20
  - percentage_tax: sales * 0.03
  - itemised_total: graduated_tax + percentage_tax
  - eight_percent: (sales - reduction) * 0.08
  - difference: eight_percent - itemised_total
expected:
  taxable_income: 600000
  graduated_tax: 62500
  percentage_tax: 72000
  itemised_total: 134500
  eight_percent: 172000
  difference: 37500
```

These blocks check the stipulated arithmetic. The retained separate boundary oracle also checks the 6-band transitions. It supplies no return rounding, quarterly calendar, taxpayer assessment, completed workbook, filing or legal entitlement. The workflow bases' full outputs, checks and minimum worked-position requirement remain unfulfilled.

## Ask the client first

1. **Taxpayer and period:** individual status and TIN identity, citizenship, residence, calendar year, work locations, income source and any need for foreign-currency treatment.
2. **Income classes:** business/professional receipts and sales, non-operating income, employment, GPP interests, exempt or separately/finally taxed items and foreign income.
3. **Registration and threshold history:** current COR/2303, monthly books and invoices, returns/discounts/allowances, VAT status, other percentage-tax status and any threshold breach. A bank statement or total revenue alone is insufficient.
4. **Actual elections and returns:** 1901/1905 records where relevant, yearly 8% choice, first-quarter deduction choice, filed 1701Q/2551Q/annual returns and any amendments. Do not default unknown choices to OSD or non-VAT.
5. **Deductions and allocation:** purchases, direct costs, payroll, leases, business-use evidence, assets, related parties, bad debts, interest, pension/R&D elections and entertainment records. Unknown business use remains unqualified; exclude an unsupported amount from a provisional illustration without treating zero use as established fact.
6. **Payments, credits and defaults:** prior payments, 2307 certificates and reconciliations, SAWT, foreign-tax evidence, notices, filing dates and taxpayer-size facts. Missing evidence means Needs Input, not a zero payable, penalty or credit.

Retain the original controls: no 8% for an ineligible/VAT-registered or over-threshold taxpayer, no separate expense deduction under 8%, no unconfirmed yearly election, no ignored conditional 116 liability, no omitted required quarterly return and no definitive calculation without qualified review. Low, moderate or high expense labels alone do not choose a legal regime. All outputs require review and sign-off by a qualified professional before filing or acting.

## Sources

Read dates identify the actual units examined, including the expressly identified independent read-only checks. They do not certify a whole website, a complete amendment history or professional approval. Captured, extracted and unread material remain distinct. Signed TRAIN and EOPT pages control the identified HTML transcription defects.

| Source | URL | Read on | Actual read scope and limitations |
| --- | --- | --- | --- |
| TRAIN, RA 10963 | <https://lawphil.net/statutes/repacts/ra2017/ra_10963_2017.html> | 2026-11-05 | Complete 24(A), individual 51 amendment, 74(A)–(B), selected 128 amendment and complete amended 249(A)–(B). HTML is not a consolidated 2025 Code. |
| TRAIN signed text | <https://lawphil.net/statutes/repacts/ra2017/pdf/ra_10963_2017.pdf> | 2026-11-05 | Read for the 2023 rates, 8% conditions and annual-date discrepancy: Physical p 4/printed pp 6–7 table and 8%; physical p 11/printed pp 20–21 annual-date unit visually checked. Not all 54 physical pages read. |
| RMO 23-2018 | <https://elibrary.judiciary.gov.ph/thebookshelf/showdocs/10/90318> | 2026-11-05 | Read for eligibility, exclusions, annual election, records and the threshold transition: Complete II.1–16 eligibility, exclusions, records, election and breach transition; relevant III.A routes. Full later continuity and registration workflow unconfirmed. |
| RA 9504 | <https://elibrary.judiciary.gov.ph/thebookshelf/showdocs/2/8724> | 2026-11-05 | Complete s 3 individual OSD, retained-source root/independent read. Not complete later continuity. |
| RR 16-2008 | <https://elibrary.judiciary.gov.ph/thebookshelf/showdocs/10/43850> | 2026-11-05 | Complete ss 1–3 individual OSD, independent read; corporate s 4 is not an individual base. Later amendments require qualification. |
| RR 2-2010 | <https://elibrary.judiciary.gov.ph/thebookshelf/showdocs/10/50806> | 2026-11-05 | Complete s 3/amended s 7 election, consistency, fallback and records, root/independent read. Publication date and later continuity unconfirmed. |
| NIRC historical text, RA 8424 | <https://lawphil.net/statutes/repacts/ra1997/ra_8424_1997.html> | 2026-11-05 | Complete 34/36 independently read; root read 51(C), 57, 74(A)–(C), 248–250 and 255. A historical capture, not authenticated consolidated 2025 law. |
| CREATE, RA 11534 | <https://lawphil.net/statutes/repacts/ra2021/ra_11534_2021.html> | 2026-11-05 | Complete s 9 deduction amendment independently read; root read interest unit. Omitted 'x x x' provisions and later adjustments not supplied. |
| CMEPA, RA 12214 | <https://lawphil.net/statutes/repacts/ra2025/ra_12214_2025.html> | 2026-11-05 | S 9 deduction amendment independently read; root complete s 24/258. Exact registration-offence amendment/commencement and full earlier/later chain unconfirmed. |
| EOPT, RA 11976 | <https://elibrary.judiciary.gov.ph/thebookshelf/showdocs/2/96948> | 2026-11-05 | Selected classification/return/withholding amendments, complete s 5, s 9/58 credit unit, s 24/116, s 29/128 and penalty/effectivity units. HTML numeric and section-number defects identified. |
| EOPT signed text | <https://lawphil.net/statutes/repacts/ra2024/pdf/ra_11976_2024.pdf> | 2026-11-05 | Physical pp 2–3, 11–12 and 21–22 visually checked for stated classification, repeal, sales base and penalty/effectivity units. No full 22-page law or later chain claim. |
| RR 10-2002 | <https://lawphil.net/administ/bir/rr/rr10_02.pdf> | 2026-11-05 | Read for entertainment-expense definitions, conditions, allocation and ceilings: All 5 pages/8 sections on entertainment expenses. Later continuity and separate withholding-predicate reconciliation remain held. |
| RR 6-2024, official ONAR copy | <https://naro.law.upd.edu.ph/issuances/3821><br><https://naro.law.upd.edu.ph/storage/01JT28JRH6YRBG857QWTQ0JJFH.pdf> | 2026-11-05 | Read for taxpayer classification, civil penalties, interest, information failures and compromise: All 3 pages/10 sections. Filed copy, registration 24-0428, linked by UP Law registry. Application/effectivity and later continuity remain qualified. |
| BIR RR 21-2018 digest | <https://bir-cdn.bir.gov.ph/local/pdf/RR%2021-2018.pdf> | 2026-11-05 | Read for the historical interest summary and its limits: Whole one-page **digest**, not the full regulation. Full accrual/rate history remains held. A separate full-copy mirror was denied; no text accepted from it. |
| Blank 1701A, January 2018 | <https://bir-cdn.bir.gov.ph/local/pdf/1701A%20Jan%202018%20v5%20with%20rates.pdf> | 2026-11-05 | Read for pure-business form scope, OSD/8% bases, other income, credits and dated tables: Both blank pages, bases, separate other income, credits and dated tables. Not current channel or complete 2025 field authority. |
| Blank 1701Q and instructions, January 2018 | <https://bir-cdn.bir.gov.ph/local/pdf/1701Q%20Jan%202018%20final%20rev2_copy.pdf><br><https://bir-cdn.bir.gov.ph/local/pdf/1701Q%20Guide%20Jan%202018_copy.pdf> | 2026-11-05 | Read for quarterly dates, bases, cumulative treatment, elections, credits and attachments: Both blank pages and whole one-page guide. Old filing, penalty and numbering text is not adopted as current. |
| Blank 2551Q and instructions, January 2018 | <https://bir-cdn.bir.gov.ph/local/pdf/2551Q%20Jan%202018%20ENCS%20final%20rev%203_copy.pdf><br><https://bir-cdn.bir.gov.ph/local/pdf/2551Q_%20Jan%202018%20Guide.pdf> | 2026-11-05 | Read for conditional percentage-tax scope, dates, election and credit fields: Both blank pages and whole one-page guide. EOPT sales, filing and numbering amendments qualify the old text. |
| RMC 20-2026 | <https://bir-cdn.bir.gov.ph/BIR/pdf/RMC%2020-2026.pdf> | 2026-11-05 | Read for the dated annual-return, form and channel guidance: Reused qualified pp 1–2, new relevant IV form/method unit pp 4–6. Whole administrative/attachment workflow and all annexes not certified. |
| RMC 20-2026 Annex C | <https://bir-cdn.bir.gov.ph/BIR/pdf/RMC%2020-2026%20Annex%20C%20%283%29.pdf> | 2026-11-05 | Read for optional annual-form selection, dated channels, no-payment and COR questions: Whole 2-page Q1–11 FAQ; Q1–8 independently checked. Dated optional form and channel guidance; later RMC 36 changes eBIRForms availability. |
| RMC 30-2026 | <https://bir-cdn.bir.gov.ph/BIR/pdf/RMC%20No.%2030-2026.pdf> | 2026-11-05 | Read for the covered 2025 annual-return filing, payment and attachment extension: Whole single-page extension, independently read and image checked. Covered 2025 annual filing/payment/attachments only; no complete later relief or portal history. |
| RMC 36-2026 | <https://bir-cdn.bir.gov.ph/BIR/pdf/RMC%20No.%2036-2026.pdf> | 2026-11-05 | Read for the later 1701-MS eBIRForms inclusion and extension corroboration: Root whole 2 pages; independent introduction/item 1 check. 1701-MS inclusion announcement used; other changes not adopted as individual rules. |

**Not yet confirmed:** the individual gaps identified beside each topic, full RR 11-2018 and RR 21-2018, actual current registration forms and 1701-MS fields, complete law/threshold/recognition/credit and filing chains, the full country contract, required operational outputs and professional approval. A 2026 read date does not turn this historical draft into a complete current-year guide.

All outputs are informational and computational material. They do not constitute tax, legal or financial advice. Open Accountants and its contributors accept no liability for errors, omissions or outcomes arising from their use. A qualified professional must review and sign off before filing or acting. The earlier penalty contribution remains credited above; no professional approval of v1.1 is claimed.
