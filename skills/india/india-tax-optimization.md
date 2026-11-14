---
name: india-tax-optimization
description: >
  Use this Tier 2 reference when working through LEGAL tax minimization
  strategies for Indian taxpayers: salaried individuals, self-employed
  professionals and business owners. Trigger on phrases like "reduce my tax
  India", "tax planning", "80C", "80D", "old vs new regime", "HRA", "NPS",
  "Section 24", "presumptive taxation", "capital gains", "GST input credit", or
  any question about legally minimizing Indian income tax. Covers regime
  selection, deduction optimization, capital allowances, loss set-off, timing,
  GST planning, social security and red lines, each tied to its provision and
  conditions under the Income-tax Act 2025 for tax year 2026-27. Read this skill
  before giving Indian tax optimization advice. It has no accountant sign-off,
  holds payroll contribution rates and scheme terms it could not read, and does
  not authorise filing, payment or a tax position.
version: 1.3
jurisdiction: IN
tax_year: 2026
tax_year_notes: "Tax year 2026-27 (1 April 2026 to 31 March 2027) under the Income-tax Act 2025 as amended by the Finance Act 2026, read at 5 November 2026. Assessment year 2026-27 (previous year 2025-26) stays under the Income-tax Act 1961 and appears only for dates still running. GST figures are as read on the dated copies named on each row."
last_updated: 2026-11-14
category: tax-optimization
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
domain: tax-optimization
type: decision
---

# India Tax Optimization v1.3

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Who this applies to

This reference covers legal tax planning in India for resident individuals, Hindu undivided families (HUFs), professionals, firms, limited liability partnerships (LLPs) and domestic companies, in rupees (INR, ₹). The Central Board of Direct Taxes and the Income Tax Department administer income tax. GST is administered under the Central Goods and Services Tax Act 2017 (CGST Act), the Integrated Goods and Services Tax Act 2017 (IGST Act) and the State and Union territory Acts.

**Period label:** tax year 2026-27 (1 April 2026 to 31 March 2027). Income-tax Act 2025 s 3 makes the tax year the financial year, or for a new business or source the period from its start to 31 March.

### Which Act governs which year

| Period | Governing Act | Rates | Basis |
| --- | --- | --- | --- |
| Assessment year 2026-27 (previous year 2025-26, ended 31 March 2026) | Income-tax Act 1961 | Finance Act 2026 Part I-A of the First Schedule and s 115BAC(1A) | Finance Act 2026 s 2 |
| Tax year 2026-27 onward | Income-tax Act 2025 | Finance Act 2026 Part I-B and s 202(1) | Income-tax Act 2025 ss 1(3), 3 and 536; Finance Act 2026 s 3 |

The 2025 Act commenced on 1 April 2026 and repealed the 1961 Act (s 536(1)). Under s 536(2), proceedings and penalties for tax years beginning before 1 April 2026 continue under the 1961 Act, and an option or election in force before commencement is treated as made under the matching 2025 provision.

This file gives figures for tax year 2026-27. For 2025-26 returns and rates use `in-income-tax`. The 1961 Act copy read here omits s 115BAC, so 2025-26 slabs are held in this file.

Non-residents, trusts as taxpayers, charitable institutions, and farming and fishing structures are outside this file. Other figures have one home in a sibling guide: `in-income-tax`, `in-advance-tax`, `in-tax-residency`, `in-tds-freelance`, `in-pf-esi-employer`, `in-professional-tax`, `india-gst`, `india-einvoice`, `india-payroll`, `india-crypto-tax`, `india-formation`, `india-financial-statements`, `india-transfer-pricing` and `india-to-uae-singapore-nri-tax`. Where a sibling differs from this file, check the primary source before relying on either.

### What this file is

This is a Tier 2 source-cited draft, pending review, with no accountant sign-off. Earlier versions carried a reviewer entry. This version changes the content, so under template rule 11 that entry does not carry to this text, and the guide returns to Tier 2 until it is approved again. The change makes no finding about any earlier review.

Each strategy here is a rule with its conditions. It becomes advice only once a named client's facts meet those conditions. Do not tell a client a step is right for them because this file lists it. State the condition, then what the facts show.

### Workflow base

This file loads no workflow base. Earlier versions listed `bookkeeping-workflow-base`, but this file classifies no transactions, and that base must be loaded with a country bookkeeping skill. The India folder held no such skill at 5 November 2026. So a request here for a ledger, posting, adjustment or output file stops: do no classification from this file and ask for a qualified bookkeeping workflow.

- **Order.** Questions in 'Ask the client first' come before any output. What stays unanswered is Needs Input. Do not build a working paper with assumed answers first.
- **Question threshold:** ₹0. No item is filtered on amount, as no floor was set.
- **Defaults.** A default stands only where the law read fixes the result of the missing fact. Section 202(1) is such a default: it applies unless a valid opt-out exists. An unknown residence, age, salary definition, scheme entry or evidence condition is Needs Input.

### How to read the status words

- **Enacted** means the text is in the Act, Finance Act, rule or notification read.
- **Held** means not proved here. Use it only alongside the enacted position and with a reviewer.
- **Bill** and **memorandum** mean the Finance Bill 2026 and its explanatory memorandum, which are not law. No figure below rests on either, or on a Budget speech.

### Section map

The 1961 numbers are labels clients still use. The 2025 numbers govern tax year 2026-27. Several numbers in the earlier version of this file were wrong and are corrected here.

| Topic | 1961 Act | 2025 Act |
| --- | --- | --- |
| Default regime | s 115BAC | s 202 |
| Rebate | s 87A | s 156 |
| Home loan interest | s 24(b) | s 22(1)(b), (1)(c) and (2) |
| Presumptive business and profession | ss 44AD, 44ADA | s 58(2) Table |
| Clubbing | s 64 | s 99 |
| Life insurance and investment deduction | s 80C | s 123 and Schedule XV |
| NPS | s 80CCD | s 124 |
| Agniveer corpus | s 80CCH | s 125 |
| Health insurance | s 80D | s 126 |
| Disabled dependant | s 80DD | s 127 |
| Education loan interest | s 80E | s 129 |
| Donations | s 80G | s 133 |
| Rent paid | s 80GG | s 134 |
| Savings interest | ss 80TTA, 80TTB | s 153 |
| Short-term gains, listed | s 111A | s 196 |
| Long-term gains | s 112 | s 197 |
| Long-term gains, listed | s 112A | s 198 |
| House sale, bonds, other assets | ss 54, 54EC, 54F | ss 82, 85, 86 |
| GAAR | Chapter X-A | Chapter XI, ss 178 to 184 |
| Books and audit | ss 44AA, 44AB | ss 62, 63 |
| Return of income | s 139 | s 263 |
| Interest for advance tax default and deferment | ss 234B, 234C | ss 424, 425 |
| Notice on escaped income | s 148 | s 280 |
| Cash receipt limit and penalty | ss 269ST, 271DA | ss 186, 451 |
| Cash expenditure and payments to relatives | s 40A(3), (2) | s 36(4), (2) |
| Gifts | s 56(2)(x) | s 92(2)(m) and (3) |
| Partner's share | s 10(2A) | Schedule III (Table: Sl. No. 2) |

## Rates, bands and thresholds

Label: tax year 2026-27, read at 5 November 2026. Rows citing the 2025 Act link the Gazette text. Its wording as amended was read in the Income Tax Department's consolidation to the Finance Act 2026, in a copy archived on 12 June 2026, because the Department's site refused direct access. The Income-tax Rules 2026 rows use a copy archived on 20 March 2026 of the rules as notified. Amendments made after those copies were not read.

### Default regime, s 202(1)

This applies to an individual, HUF, association of persons, body of individuals or artificial juridical person unless a valid opt-out exists.

| Total income (₹) | Rate | Basis | URL |
| --- | --- | --- | --- |
| Up to 4,00,000 | Nil | Income-tax Act 2025 s 202(1) | https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Over 4,00,000 to 8,00,000 | 5% | Same | https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Over 8,00,000 to 12,00,000 | 10% | Same | https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Over 12,00,000 to 16,00,000 | 15% | Same | https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Over 16,00,000 to 20,00,000 | 20% | Same | https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Over 20,00,000 to 24,00,000 | 25% | Same | https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Over 24,00,000 | 30% | Same | https://egazette.gov.in/WriteReadData/2025/265620.pdf |

### Opt-out rates (the 'old regime')

| Person and total income (₹) | Rate | Basis | URL |
| --- | --- | --- | --- |
| Under 60: up to 2,50,000 | Nil | Finance Act 2026 Part I-B, Paragraph A | https://egazette.gov.in/WriteReadData/2026/271439.pdf |
| Under 60: over 2,50,000 to 5,00,000 | 5% | Same | https://egazette.gov.in/WriteReadData/2026/271439.pdf |
| Under 60: over 5,00,000 to 10,00,000 | ₹12,500 plus 20% of the excess over 5,00,000 | Same | https://egazette.gov.in/WriteReadData/2026/271439.pdf |
| Under 60: over 10,00,000 | ₹1,12,500 plus 30% of the excess over 10,00,000 | Same | https://egazette.gov.in/WriteReadData/2026/271439.pdf |
| Resident aged 60 to 79: up to 3,00,000 nil, then to 5,00,000 at 5%, to 10,00,000 ₹10,000 plus 20%, above ₹1,10,000 plus 30% | As stated | Same | https://egazette.gov.in/WriteReadData/2026/271439.pdf |
| Resident aged 80 or over: up to 5,00,000 nil, to 10,00,000 at 20%, above ₹1,00,000 plus 30% | As stated | Same | https://egazette.gov.in/WriteReadData/2026/271439.pdf |

An HUF on opt-out rates uses the 'under 60' bands, so its nil band is ₹2,50,000. On the default regime its nil band is ₹4,00,000.

### Rebate, standard deduction, surcharge and cess

| Item | Amount | Basis | URL |
| --- | --- | --- | --- |
| Rebate, any resident individual | Lesser of 100% of tax and ₹12,500, if total income does not exceed ₹5,00,000 | s 156(1) | https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Rebate, resident individual under s 202(1) | Lesser of 100% of tax and ₹60,000, if income does not exceed ₹12,00,000 | s 156(2)(a) | https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Marginal rebate, resident individual under s 202(1) | Tax in excess of (total income less ₹12,00,000), where that tax is greater | s 156(2)(b), capped by s 156(3) | https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Standard deduction, salary | ₹75,000 or the salary if less, under s 202(1); ₹50,000 or the salary if less, otherwise | s 19(1) Table, Sl. No. 2 | https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Family pension | One-third, up to ₹25,000 under s 202(1); up to ₹15,000 otherwise | s 93(1)(d) | https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Surcharge, individual or HUF, both regimes | 10% over ₹50 lakh to ₹1 crore; 15% over ₹1 crore to ₹2 crore | Finance Act 2026 Part I-B Paragraph F; s 3(4)(b) Table, Sl. No. 10 | https://egazette.gov.in/WriteReadData/2026/271439.pdf |
| Surcharge, individual or HUF under s 202 | 25% where income excluding dividends and ss 196, 197 and 198 gains exceeds ₹2 crore. No 37% band. 15% where income including them exceeds ₹2 crore and the 25% limb does not apply | Finance Act 2026 s 3(4)(b) Table, Sl. No. 10 | https://egazette.gov.in/WriteReadData/2026/271439.pdf |
| Surcharge, individual or HUF on opt-out rates | 25% over ₹2 crore to ₹5 crore and 37% over ₹5 crore, on income excluding dividends and ss 196, 197 and 198 gains; otherwise 15% over ₹2 crore | Finance Act 2026 Part I-B Paragraph F | https://egazette.gov.in/WriteReadData/2026/271439.pdf |
| Surcharge cap on dividends and ss 196, 197 and 198 gains | 15% on that part of income | Same provisions | https://egazette.gov.in/WriteReadData/2026/271439.pdf |
| Health and Education Cess | 4% of tax plus surcharge | Finance Act 2026 s 3(15) | https://egazette.gov.in/WriteReadData/2026/271439.pdf |

Marginal relief applies at ₹50 lakh, ₹1 crore and ₹2 crore under s 202 (Finance Act 2026 s 3(5) Table, Sl. No. 6), at those steps and ₹5 crore on opt-out rates, at ₹1 crore for a firm, and at ₹1 crore and ₹10 crore for a domestic company (Paragraph F Table 2). Top combined rates, computed from these rows, are 39% on the default regime (30% × 1.25 × 1.04) and 42.744% on opt-out rates (30% × 1.37 × 1.04). Below ₹50 lakh the top rate is 31.2%.

Rebate limits: s 198(7) keeps s 198 long-term gains out of the rebate. Whether s 156 reaches tax on other special-rate income was not tested, so a client relying on it for s 196 or s 197 gains needs review. The ₹12,75,000 salaried figure is ₹12,00,000 plus the ₹75,000 standard deduction and assumes salary is the only income.

### Companies and firms

| Person | Rate | Surcharge and combined rate | Basis | URL |
| --- | --- | --- | --- | --- |
| Domestic company, s 200 option | 22% | 10% surcharge, 4% cess: 25.168% | ss 200, 205; Finance Act 2026 s 3(4)(b) Table, Sl. No. 9 | https://egazette.gov.in/WriteReadData/2026/271439.pdf |
| Domestic manufacturing company, s 201 option | 15% on the qualifying income; 22% on the income in s 201 Table column C clause (b); 22% on short-term gains on an asset with no depreciation allowable (clause (c)); 30% on income deemed under s 205(4) (clause (d)) | 10% surcharge, 4% cess: 17.16% on the 15% slice. Set up and registered on or after 1 October 2019, and manufacturing begun by 31 March 2024, so a new company cannot meet it | s 201; same Sl. No. 9 | https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Other domestic company | 25% if turnover or gross receipts in 2024-25 did not exceed ₹400 crore; otherwise 30% | 7% over ₹1 crore to ₹10 crore; 12% over ₹10 crore; 4% cess | Finance Act 2026 Part I-B Paragraphs E and F | https://egazette.gov.in/WriteReadData/2026/271439.pdf |
| Firm, including LLP | 30% | 12% over ₹1 crore; 4% cess: 31.2% or 34.944% | Finance Act 2026 Part I-B Paragraphs C and F; s 2(45) | https://egazette.gov.in/WriteReadData/2026/271439.pdf |

### Deductions by regime

'Default' asks whether the item survives under s 202. Section 202(2) removes every Chapter VIII deduction except ss 124(1), 124(2), 125(2) and 146, and removes Schedule III Sl. Nos. 5, 6, 7, 8, 11 and 17, Sl. Nos. 12 and 13 other than as prescribed, s 19(1) Sl. No. 1 (professional tax), s 22(1)(b) on a s 21(6) property, and ss 33(8), 45(3)(a) to (c), 46, 47(1)(a), 48 and 49.

| Item | Limit | Default | Basis | URL |
| --- | --- | --- | --- | --- |
| Life insurance, provident fund, notified schemes, tuition, housing principal | ₹1,50,000 in aggregate, individual or HUF | No | s 123, Schedule XV | https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Own NPS contribution, Schedule XV paragraph 1(y) | Within the ₹1,50,000: 10% of salary, or 20% of gross total income for a non-employee | No | s 123, Schedule XV | https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Own NPS, additional | ₹50,000 | No | s 124(3) | https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Employer NPS | 14% of salary for the Central or a State Government; 10% for others; 14% for any employer if the employee is chargeable under s 202(1) | Yes | s 124(1), (2), (13)(b) | https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Agniveer Corpus Fund, Government's contribution | Full amount | Yes | s 125(2) | https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Agniveer, own contribution | Full amount | No | s 125(1) | https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Health insurance, self and family | ₹25,000; ₹50,000 if a senior citizen is insured | No | s 126 | https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Health insurance, parents | A further ₹25,000; ₹50,000 if a parent is a senior citizen | No | s 126 | https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Preventive health check-up | ₹5,000, inside those limits | No | s 126 | https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Medical expenditure: self or family; any parent | ₹50,000 for each group, and insurance/check-up plus medical expenditure stay within ₹50,000 for that group. Sub-sections (2)(c), (d) have no age floor. For a senior citizen, only if no health insurance was paid for that person. Non-cash payment required | No | s 126(2)(c), (d), (4), (7), (9) | https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Disabled dependant | ₹75,000; ₹1,25,000 for severe disability; resident individual or HUF | No | s 127 | https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Education loan interest | No cap; initial year plus up to 7 more, 8 years at most | No | s 129 | https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Donations | 100% or 50% by donee, some inside a 10% of adjusted gross total income ceiling | No | s 133 | https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Rent paid, no house rent allowance | Least of ₹5,000 a month, 25% of total income, and rent less 10% of total income | No | s 134 | https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Savings account interest | ₹10,000, individual under 60 or HUF | No | s 153 | https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Deposit interest, resident senior citizen | ₹50,000 | No | s 153 | https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Self-occupied home loan interest | ₹2,00,000 where acquired or constructed with capital borrowed and completed within 5 years from the end of the year of borrowing, with lender's certificate; otherwise ₹30,000 | No | s 22(1)(b), (2), (5) | https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Let-out property interest | No cap on the deduction | Yes | s 22(1)(b) | https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Leave travel concession or assistance from an employer | Amount actually incurred on travel in India, within the rule 278(1) fare limits; 2 journeys in a block of 4 calendar years from 2022, with the rule 278(3) carry-over. Not for more than 2 surviving children, except children born before 1 October 1998 and multiple births after one child (rule 278(5), (6)) | No | Schedule III Sl. No. 8; Income-tax Rules 2026 rule 278 | https://web.archive.org/web/20260320162411id_/https://www.incometaxindia.gov.in/documents/d/guest/en-notified-it-rules-2026-20-03-2026-pdf |
| House rent allowance exclusion | Least of the allowance, rent less 10% of salary, and 50% of salary (Mumbai, Kolkata, Delhi, Chennai, Hyderabad, Pune, Ahmedabad, Bengaluru) or 40% elsewhere, each for the period of occupation in the year. Salary includes dearness allowance if the terms of employment provide, and excludes other allowances and perquisites (rule 279(2)) | No | Schedule III Sl. No. 11; Income-tax Rules 2026 rule 279 | https://web.archive.org/web/20260320162411id_/https://www.incometaxindia.gov.in/documents/d/guest/en-notified-it-rules-2026-20-03-2026-pdf |

### Capital gains

| Gain | Rate or limit | Basis | URL |
| --- | --- | --- | --- |
| Short-term, equity share, equity oriented fund unit or business trust unit, where the sale is chargeable to securities transaction tax | 20% | s 196 | https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Long-term, equity share (securities transaction tax on acquisition and transfer, subject to notified exceptions in s 198(5)), or equity oriented fund or business trust unit (tax on transfer) | 12.5% over ₹1,25,000 a year | s 198 | https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Other long-term | 12.5% | s 197 | https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Long-term land or building, resident individual or HUF, acquired before 23 July 2024 | Tax above 20% of the indexed gain is ignored | s 197(3) | https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| House sale reinvestment | ₹10 crore cap on the new asset's cost (s 82(7)) and on the gain counted for the deposit (s 82(8)); 2 houses once if the gain does not exceed ₹2 crore | s 82 | https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Bond reinvestment, land or building gain | ₹50 lakh; within 6 months; 5-year hold | s 85 | https://egazette.gov.in/WriteReadData/2025/265620.pdf |

Holding periods: long-term means held over 24 months, or over 12 months for a listed security, a Unit Trust of India unit, an equity fund unit or a zero coupon bond (s 2).

### Depreciation, written down value

| Block | Rate | Basis | URL |
| --- | --- | --- | --- |
| Buildings used mainly for residence, except hotels and boarding houses | 5% | Income-tax Rules 2026 Appendix I Part A | https://web.archive.org/web/20260320162411id_/https://www.incometaxindia.gov.in/documents/d/guest/en-notified-it-rules-2026-20-03-2026-pdf |
| Other buildings, apart from the next row | 10% | Same | https://web.archive.org/web/20260320162411id_/https://www.incometaxindia.gov.in/documents/d/guest/en-notified-it-rules-2026-20-03-2026-pdf |
| Buildings for machinery and plant of a water supply or water treatment project under 1961 Act s 80-IA(4)(i), and purely temporary erections | 40% | Same | https://web.archive.org/web/20260320162411id_/https://www.incometaxindia.gov.in/documents/d/guest/en-notified-it-rules-2026-20-03-2026-pdf |
| Furniture and fittings | 10% | Same | https://web.archive.org/web/20260320162411id_/https://www.incometaxindia.gov.in/documents/d/guest/en-notified-it-rules-2026-20-03-2026-pdf |
| Machinery and plant, general | 15% | Same | https://web.archive.org/web/20260320162411id_/https://www.incometaxindia.gov.in/documents/d/guest/en-notified-it-rules-2026-20-03-2026-pdf |
| Motor cars not run on hire | 15%; 30% if acquired from 23 August 2019 to before 1 April 2020 and used before that date | Same | https://web.archive.org/web/20260320162411id_/https://www.incometaxindia.gov.in/documents/d/guest/en-notified-it-rules-2026-20-03-2026-pdf |
| Motor buses, lorries and taxis run on hire | 30%; 45% for the same 2019-20 window; 40% for a new commercial vehicle acquired 1 January to before 1 October 2009 | Same | https://web.archive.org/web/20260320162411id_/https://www.incometaxindia.gov.in/documents/d/guest/en-notified-it-rules-2026-20-03-2026-pdf |
| Computers including computer software | 40% | Same | https://web.archive.org/web/20260320162411id_/https://www.incometaxindia.gov.in/documents/d/guest/en-notified-it-rules-2026-20-03-2026-pdf |
| Know-how, patents, copyrights, trademarks, licences, franchises and similar commercial rights | 25%; no depreciation on goodwill (s 33(1)(b)) | Appendix I Part B | https://web.archive.org/web/20260320162411id_/https://www.incometaxindia.gov.in/documents/d/guest/en-notified-it-rules-2026-20-03-2026-pdf |
| Any block, for a person under s 202(1), a domestic company under a s 199, 200 or 201 option, or a resident co-operative society under a s 203 or 204 option | Capped at 40% of written down value | Income-tax Rules 2026 rule 25(2) Table | https://web.archive.org/web/20260320162411id_/https://www.incometaxindia.gov.in/documents/d/guest/en-notified-it-rules-2026-20-03-2026-pdf |
| Additional depreciation, new machinery or plant | 20% of cost; 10% if used under 180 days in the year and the other 10% the next year. Not under s 202 | s 33(8), (9), s 202(2) | https://egazette.gov.in/WriteReadData/2025/265620.pdf |

Column extraction in Appendix I was scrambled. The first Part A page was checked by eye, and later rows were matched in order against a second, unformatted extraction. An asset used under 180 days in its first year takes half the rate (s 33(4)).

### Presumptive income, s 58(2) Table

| Business | Turnover limit | Deemed profit | URL |
| --- | --- | --- | --- |
| Eligible business, Sl. No. 1: resident individual, HUF or firm other than LLP | ₹2 crore; ₹3 crore if cash received does not exceed 5% of turnover | 6% of amounts received by banking or online mode in the year or by the return due date, 8% of the rest, or more if claimed | https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Goods carriages, Sl. No. 2: 10 or fewer at any time in the year | Vehicle count | ₹1,000 per ton of gross vehicle weight or unladen weight a month for a heavy goods vehicle, ₹7,500 a month for others, or more if claimed | https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Specified profession, Sl. No. 3: resident individual or firm other than LLP | ₹50 lakh; ₹75 lakh if cash received does not exceed 5% of gross receipts | 50%, or more if claimed | https://egazette.gov.in/WriteReadData/2025/265620.pdf |

### GST

| Item | Figure | Basis | URL |
| --- | --- | --- | --- |
| Registration, general | Aggregate turnover over ₹20 lakh | CGST Act s 22(1) | https://taxinformation.cbic.gov.in/content/html/tax_repository/gst/acts/2017_CGST_act/active/chapter6/section22_v1.00.html |
| Registration, special category | Over ₹10 lakh. On a State's request the Government may raise this by notification to no more than ₹20 lakh (second proviso); no such notification was read | s 22(1) and Explanation (iii): the States in Constitution article 279A(4)(g), except Jammu and Kashmir, Arunachal Pradesh, Assam, Himachal Pradesh, Meghalaya, Sikkim and Uttarakhand. Article 279A was not read, so the States left, inferred to be Manipur, Mizoram, Nagaland and Tripura, are held | https://taxinformation.cbic.gov.in/content/html/tax_repository/gst/acts/2017_CGST_act/active/chapter6/section22_v1.00.html |
| Registration, exclusive supplier of goods | Over ₹40 lakh | Notification 10/2019-Central Tax. Not for ice cream, pan masala or tobacco, compulsory registrants under s 24, voluntary registrants, or intra-State suppliers in Arunachal Pradesh, Manipur, Meghalaya, Mizoram, Nagaland, Puducherry, Sikkim, Telangana, Tripura and Uttarakhand | https://gstcouncil.gov.in/sites/default/files/2024-05/notfctn-10-central-tax-english-2019.pdf |
| Composition limit | ₹1.5 crore in the preceding year; ₹75 lakh in Arunachal Pradesh, Manipur, Meghalaya, Mizoram, Nagaland, Sikkim, Tripura and Uttarakhand | CGST Act s 10(1); Notification 14/2019-Central Tax | https://gstcouncil.gov.in/sites/default/files/2024-05/notfctn-14-central-tax-english-2019.pdf |
| Composition central tax rate | Manufacturers 0.5% of turnover; Schedule II paragraph 6(b) restaurant-type supplies 2.5%; other eligible suppliers 0.5% of taxable supplies | CGST Rules rule 7, read in the April 2019 edition | https://cbic-gst.gov.in/pdf/23042019-CGST-Rules-2017-Part-A-Rules.pdf |
| Service supplier option | Preceding-year aggregate turnover up to ₹50 lakh; 3% central tax | CGST Act s 10(2A); rate as stated in CBIC Circular 97/16/2019-GST | https://cbic-gst.gov.in/pdf/circular-cgst-97.pdf |
| Goods rates, IGST | Schedule I 5%, II 18%, III 40%, IV 3%, V 0.25%, VI 1.5%, VII 28% | Notification 9/2025-Integrated Tax (Rate), from 22 September 2025, read in an ICAI print hosted on CBIC | https://courier.cbic.gov.in/ECCS/advisory/2025/NOTIFICATION%20NO.%209_2025-INTEGRATED%20TAX%20(RATE)%20-1759486719.pdf |
| E-invoicing limit | ₹5 crore from 1 August 2023 | Notification 10/2023-Central Tax, which substitutes that figure in Notification 13/2020 (not read) | https://einvoice6.gst.gov.in/content/wp-content/uploads/2023/05/GST-notification-10-central-tax-english-2023.pdf |

The composition rates are central tax. State or Union territory tax is charged under that Act, which was not read, so the combined 1%, 5% and 6% in the earlier version are held as twice the central rate. Schedule VII keeps 28% for pan masala, tobacco and tobacco products, so the 28% rate was not abolished. Schedule IV Sl. No. 5 carries gold at heading 7108 at 3%.

### Payroll contributions

| Item | Figure | Basis | URL |
| --- | --- | --- | --- |
| Wage ceiling, Code on Social Security 2020 Chapter III | ₹25,000 a month from 17 September 2026 | S.O. 5109(E) of 17 September 2026 | https://egazette.gov.in/WriteReadData/2026/276299.pdf |
| ESI coverage wage limit | ₹21,000 a month, pending rules | Ministry of Labour FAQ of 16 March 2026, reply 12 | https://www.labour.gov.in/static/uploads/2026/03/a4ccf4c6d97c4f1f36a6d83f8c64213d.pdf |
| Employer contribution taxable in employee's hands | Aggregate over ₹7,50,000 a year to recognised provident fund, s 124(1) scheme and approved superannuation fund | Income-tax Act 2025 s 17(1)(h) | https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Provident fund interest, taxable part | Interest on own contributions from 1 April 2021 above ₹2,50,000 a year, or ₹5,00,000 where the employer does not contribute | Schedule II Sl. Nos. 3 and 4 | https://egazette.gov.in/WriteReadData/2025/265620.pdf |

EPF, EPS and ESI contribution rates are not given here: EPFO refused access and ESIC was unreachable on 14 Nov 2026, so no rate was read in a primary source. Use `in-pf-esi-employer` and check its source before applying any rate. They are listed under Not yet confirmed.

### Reporting thresholds

| Transaction reported in the statement of financial transactions | Threshold | Basis | URL |
| --- | --- | --- | --- |
| Cash deposits and withdrawals, current account | ₹50 lakh or more in the year, tested separately for deposits and for withdrawals | Income-tax Rules 2026 rule 237 Table, Sl. No. 1(c), as notified | https://web.archive.org/web/20260320162411id_/https://www.incometaxindia.gov.in/documents/d/guest/en-notified-it-rules-2026-20-03-2026-pdf |
| Cash deposits, other accounts | ₹10 lakh or more with PAN; ₹5 lakh or more without PAN, in the year | Sl. No. 2 | https://web.archive.org/web/20260320162411id_/https://www.incometaxindia.gov.in/documents/d/guest/en-notified-it-rules-2026-20-03-2026-pdf |
| Time deposits | ₹10 lakh or more in the year | Sl. No. 3 | https://web.archive.org/web/20260320162411id_/https://www.incometaxindia.gov.in/documents/d/guest/en-notified-it-rules-2026-20-03-2026-pdf |
| Bonds and shares issued | ₹10 lakh or more in the year | Sl. Nos. 5 and 6 | https://web.archive.org/web/20260320162411id_/https://www.incometaxindia.gov.in/documents/d/guest/en-notified-it-rules-2026-20-03-2026-pdf |
| Immovable property, purchase, sale, gift or joint development agreement | ₹45 lakh or more, or stamp duty value of that amount | Sl. No. 9 | https://web.archive.org/web/20260320162411id_/https://www.incometaxindia.gov.in/documents/d/guest/en-notified-it-rules-2026-20-03-2026-pdf |
| Insurance premium received by an insurer | ₹5,00,000 or more with PAN; ₹2,50,000 or more without PAN, in the year, in one or more accounts of a person | Sl. No. 11 | https://web.archive.org/web/20260320162411id_/https://www.incometaxindia.gov.in/documents/d/guest/en-notified-it-rules-2026-20-03-2026-pdf |
| Cash sales of goods or services, audited persons | Over ₹2 lakh | Sl. No. 12 | https://web.archive.org/web/20260320162411id_/https://www.incometaxindia.gov.in/documents/d/guest/en-notified-it-rules-2026-20-03-2026-pdf |

## The base

### Regime selection

Compute both ways every year, using `Example 1` as the pattern. No fixed deduction figure decides it: the break-even moves with income. At ₹15,00,000 of salary it is ₹5,43,750 of old-regime reductions on top of the ₹50,000 standard deduction.

**Opting out (s 202(4)).** Section 202(1) applies by default.

- **No business or professional income:** the option is exercised with the return under s 263(1) for that year, so it can differ year to year. The text names s 263(1), so do not plan on making it in a belated return under s 263(4).
- **Business or professional income:** the option is exercised by the s 263(1) due date and continues to later years. It may be withdrawn only once, and after that the person cannot opt out again unless they cease to have business or professional income.

**Employer.** Other income and house property loss particulars go on Form 122 (rule 204), and evidence of claims on Form 124 (rule 205, s 392(5)(b)). The employer's certificate on Form 130 records whether the employee opts out of s 202(1). The earlier version said to inform the employer at the start of the year on Form 12BBA. That name was not found in the Rules 2026 as notified, and no form read carries the employee's intimation, so that step is held. What the employer is told affects tax deducted. The return decides the charge for a person with no business income.

**What a change costs.** Moving to s 202 gives up the items marked 'No' above and, for house property, any loss against other heads (s 202(2)(b)(ii)). It also bars carried-forward losses attributable to the listed deductions.

### Sole proprietor, LLP or company

Business form is a commercial and legal choice first. These are the tax rules that bear on it.

- **Sole proprietor.** Profit is taxed at the person's rates. Section 58(2) may apply: see 'Presumptive income'.
- **LLP or firm.** A firm includes an LLP (s 2(45)). It pays 30%, plus surcharge and cess, and a partner's share is excluded from the partner's income (Schedule III Sl. No. 2). Remuneration to working partners is deductible only if authorised by the deed and within s 35(e)(iii): on the first ₹6,00,000 of book profit or in a loss, the higher of ₹3,00,000 and 90% of book profit, and 60% of the balance. Interest to partners is capped at 12% simple a year (s 35(e)(iv)). The partner is taxed on what the firm deducted. Over ₹1 crore a firm's 34.944% is below an individual's top rate of 39% or 42.744%. That helps only if the facts reach those bands.
- **Private company.** Under s 200 the rate is 25.168%, and the option must be made in the prescribed manner by the s 263(1) due date. It then applies to later years and cannot be withdrawn (s 200(5), (6)). It gives up the deductions in s 200(1)(a), and carried-forward losses attributable to them. If the requirements fail, the option is invalid for that year and later years (s 200(2)). Dividends are then taxed in the shareholder's hands, so compare after both layers. Under s 200 alone, ₹100 of profit leaves ₹74.83, and a 31.2% shareholder keeps ₹51.48. A text search of the 2025 consolidation for 'distributed profits' found no distribution tax charge. The stop date of 1961 Act s 115-O was not read.

### Family structuring and clubbing

Section 99 adds the following to the individual's income:

- **Spouse's remuneration** from a concern in which the individual has a substantial interest, unless it is solely attributable to the spouse's technical or professional knowledge, experience and qualification (s 99(1)(a)(i)). Include it in the income of the spouse whose total income before inclusion is greater. Once allocated, do not switch spouses in a later year unless the Assessing Officer is satisfied after giving the other spouse an opportunity to be heard (s 99(5)(a)(i), (ii)). Substantial interest is at least 20% of qualifying voting power or profits at any time in the year, held by the individual alone or with relatives (s 99(5)(a)(iii)).
- **Income from assets transferred** to the spouse without adequate consideration, otherwise than in connection with an agreement to live apart and subject to s 25(a) (s 99(1)(a)(ii)); to a son's wife on or after 1 June 1973 (s 99(1)(b)); or to a person or association for their immediate or deferred benefit, with the pre-1 June 1973 exception for a son's wife (s 99(1)(d)). Where assets transferred to the spouse or son's wife are invested in a business or contributed as firm capital, the included amount is B × C / D: B is the income, interest or both arising to that person from the business or firm in the year, C is the value of the transferred assets invested or contributed on the year's first day and D is that person's total business investment or firm capital on that day (s 99(2), as amended by the Finance Act 2026). Establish both opening values; do not club the whole business return merely because some transferred assets were used.
- **A minor child's income** (s 99(1)(c)), except income from work done by the child, from activities applying the child's skill, talent, specialised knowledge or experience, or where the child has a s 154 disability. It goes to the parent with the greater income while the marriage subsists, and otherwise to the parent who maintains the child (s 99(5)(b)). Schedule III Sl. No. 17 excludes ₹1,500 per child, but not under s 202.
- **Income from property converted to HUF property** without adequate consideration (s 99(3)).

So paying a spouse for genuine work avoids clubbing only on the qualification limb. Reasonableness is a separate test: s 36(2) can disallow excessive payments to relatives whatever the outcome under s 99.

An **HUF** is a separate taxpayer. Its nil band is in the rate tables. Schedule XV gives it life insurance, notified provident fund and unit plan entries in members' names only. An HUF built from a member's own assets meets s 99(3).

### Deductions: conditions the table cannot carry

- **Section 123.** Insurance premium counts only up to 10%, 15% or 20% of the sum assured, depending on the policy (Schedule XV). Early exit can reverse the deduction (Schedule XV paragraphs 4 and 5).
- **Health insurance and medical expenditure.** Payment must be otherwise than in cash, except for a preventive check-up. Section 126(2)(c) and (d) allow medical expenditure on the assessee, family or a parent without an age floor, up to ₹50,000 for self/family and a separate ₹50,000 for parents. Each group's insurance/check-up and medical expenditure together cannot exceed ₹50,000 (s 126(4)); the ₹5,000 preventive check-up limit is aggregate, within the insurance/check-up limits (s 126(3)). For expenditure on a senior citizen, s 126(7) additionally requires that no health insurance was paid for that person. The 1961 Act's s 80D proviso expressly limited medical expenditure to senior citizens; do not import it into the 2025 wording. Family means spouse and dependant children (s 126(10)(b)). An HUF has its own limits (s 126(5), (6)). A lump sum premium for several years is apportioned under s 126(8)(b). The general later-amendment and professional-review holds still apply.
- **Education loan.** The borrower is an individual, for higher education of self, spouse, children or a student under their legal guardianship, from a financial or approved charitable institution (s 129).
- **Donations.** The s 133(1)(a) list of 100% donees has 24 entries and (1)(b) has 6, not restated here: check the donee's entry. Only a sum of money counts, a donation over ₹2,000 must not be in cash, and a s 133(1)(b)(ii) claim depends on the donee's own reporting (s 133(4) to (6)).
- **Rent paid.** Section 134 is barred where the person receives house rent allowance under Schedule III Sl. No. 11, and its ownership bars apply.
- **House rent allowance.** The accommodation must not be owned by the employee and rent must actually be incurred. The landlord's name, address and PAN go on Form 124 where aggregate rent exceeds ₹1,00,000 in the year (rule 205). Form 124 also asks for the relationship to the landlord.
- **Self-occupied house.** Up to 2 houses take nil annual value if the owner occupies them, or cannot actually occupy them for any reason, and they are not let and yield no other benefit (s 21(6), (7)). Combined interest is capped at ₹2,00,000 (s 22(5)). Pre-construction interest comes in 5 equal instalments (s 22(1)(c)).
- **Old-regime house loss.** Set-off against other heads is capped at ₹2,00,000 a year (s 109(1)(b)).

### Capital allowances

Depreciation is claimed on block written down value (s 33). Additional depreciation needs manufacture or production of an article or thing, or generation, transmission or distribution of power, and a new machine or plant installed and first put to use in the business. It is barred for ships, aircraft, second-hand assets, installations in office or residential premises, office appliances, road transport vehicles, and assets wholly deducted in one year (s 33(8)). The text read has no ₹25,000 cost threshold, so that figure in the earlier version is removed.

### Presumptive income

Section 58 replaces ss 26 to 54 so far as contrary. These conditions apply:

- **Business, Sl. No. 1.** The person takes no Chapter VIII-C deduction, is not in a specified profession, and earns no commission, brokerage or agency income. Only banking or online receipts take 6%. A cheque that is not account payee counts as cash (s 58(9)).
- **Specified profession (s 62(4)).** Legal, medical, engineering, architectural, accountancy, technical consultancy, interior decoration, information technology, company secretary, or notified. An HUF is not within Sl. No. 3.
- **Consequences.** No further expense or allowance is deducted (s 58(4)), and written down value is treated as if depreciation was claimed (s 58(6)). No s 63 audit applies where profits are declared under s 58(2) (s 63(2)). Advance tax for Sl. Nos. 1 and 3 falls in one instalment by 15 March (s 408(2)).
- **Lower profit.** Claiming less than the deemed profit, with income above the nil band, requires books and audit (ss 58(3), 62(2)(c), 63(1) Table Sl. No. 2).
- **Lock-out.** A person who declares under Sl. No. 1 and then declares otherwise in any of the next 5 tax years cannot use Sl. No. 1 for the 5 tax years after that year. In those years, income above the nil band requires books and audit (s 58(7), (8)). Sections 62 and 63 do not apply to Sl. No. 2 business (s 58(10)).
- **Books.** The earlier version said no books are needed. Sections 58(3) and 62(2)(c) require books on a lower-profit claim. Section 62(1)(a) requires them of any person carrying on a specified profession, with no turnover test, and s 58(1) overrides only ss 26 to 54, so a Sl. No. 3 professional keeps them. For Sl. No. 1, the text read does not expressly remove s 62(2)(a) and (d) for a person declaring the deemed profit, so that point is held. Keep records proving turnover and receipt mode whatever the answer.

### Loss set-off and carry forward

| Loss | Same-year set-off | Carry forward |
| --- | --- | --- |
| Business | Any head except salary | 8 years, business income only |
| Speculation business | Speculation income only | 4 years |
| Short-term capital | Short-term or long-term gains | 8 years |
| Long-term capital | Long-term gains only | 8 years |
| House property | Any head to ₹2,00,000 on opt-out rates; none across heads under s 202 | 8 years, house property income only |
| Unabsorbed depreciation | Available profits | No time limit (s 33(11)(b)) |

Basis: ss 108 to 121 and s 33(11). Section 121 denies carry forward under ss 111(1), 112(1), 113(2), 114(2) and 115(2) unless the return is filed under s 263(1) in time. It does not list s 110 (house property) or s 33(11) (unabsorbed depreciation). Section 120 restricts set-off against undisclosed income.

Chapter VIII deductions do not reduce ss 196, 197 or 198 gains. A resident individual or HUF may use any unused nil band against those gains (ss 196(2), 197(2), 198(3)).

### Timing

- **Section 123 and NPS.** The amount must be paid in the tax year. A payment by 31 March counts for that year. Do not move a date backwards.
- **Advance tax.** Seasonal income does not change the dates. Section 425(4) gives relief only for the items it lists: see 'Deadlines and filing'.
- **Capital gains.** Sections 82, 85 and 86 run from the transfer date. Under s 82 the capital gains, and under s 86 the net consideration, not used before filing the return go into the notified capital gains account before filing, with proof attached to the return. The deposit must be made by the due date under s 263(1) for s 82 (s 82(2)(b)), and under s 263 as s 86(2)(b) puts it.
- **Section 82.** An individual or HUF with a long-term gain on a residential house. One residential house in India, bought 1 year before or 2 years after the transfer, or built within 3 years. Selling the new house within 3 years reverses it.
- **Section 85.** Land or building long-term gain only, invested within 6 months in NHAI, REC or notified bonds, up to ₹50 lakh, and held 5 years. A loan against the bonds counts as conversion. The investment gives no s 123 deduction.
- **Section 86.** An individual or HUF with a long-term gain on an asset other than a residential house, and one residential house in India on the s 82 timing. Relief is the gain in the proportion that the new house's cost bears to the net consideration, and full if the cost is at least the net consideration. It does not apply if the person owns more than one other residential house at the transfer, or buys one within 1 year or builds one within 3 years of the transfer, and the income from that house, apart from one owned at the transfer, is chargeable as house property (s 86(5)). A further such house bought within 2 years or built within 3 years, or a sale of the new house within 3 years, brings the relieved gain back (s 86(6), (7)). The new asset's cost counts to ₹10 crore for s 86(1), and the net consideration counts to ₹10 crore for s 86(2) (s 86(8), (9)).

### GST

- **Input tax credit (CGST Act s 16).** Credit needs a tax invoice, debit note or other prescribed tax paying document (s 16(2)(a)), details furnished by the supplier and communicated under s 37 (s 16(2)(aa)), receipt, with credit on goods received in lots only at the last lot (s 16(2)(b) and first proviso), no restriction of the credit details communicated under s 38 (s 16(2)(ba)), tax actually paid, subject to s 41 (s 16(2)(c)), and a return (s 16(2)(d)). A recipient who does not pay the supplier within 180 days of the invoice repays the credit with interest, and may take it again on payment. No credit may be taken after 30 November following the end of the financial year, or after the relevant annual return if earlier (s 16(4)). Tax claimed as depreciation gives no credit (s 16(3)). The earlier version named GSTR-2B: the Act text read says ss 37 and 38, and the rule that links them to GSTR-2B was not read.
- **Reverse charge.** Tax on notified supplies is paid by the recipient (s 9(3), (4)). The notifications listing them were not read.
- **Composition.** Conditions are in s 10(2): no services beyond the s 10(1) proviso (10% of turnover or ₹5 lakh, whichever is higher), no supplies outside the Act, no inter-State outward supplies, no supplies through an operator collecting tax under s 52, not a notified manufacturer, not a casual or non-resident taxable person. All registrations on one PAN must opt. No tax is collected from the customer and no credit is taken (s 10(4)). The option lapses when turnover exceeds the limit (s 10(3)).
- **Section 10(2A) option.** Subject to s 9(3) and (4), a registered person not eligible under s 10(1) and (2), with aggregate turnover in the preceding financial year not over ₹50 lakh, may pay at a prescribed rate of no more than 3% of turnover in the State or Union territory. The person must not make supplies outside the Act, make inter-State outward supplies, supply services through an operator collecting tax under s 52, be a notified manufacturer or service supplier, or be a casual or non-resident taxable person. All registrations on one PAN must opt. Sections 10(3) and (4) apply in the same way.
- **Refund of accumulated credit.** Section 54(3) allows it on zero-rated supplies without payment of tax, and where credit accumulates because inputs are taxed above outputs, other than nil-rated or fully exempt supplies and supplies notified as excluded. Its provisos bar refund in the drawback cases they state.
- **Exports.** Exports and supplies to a Special Economic Zone developer or unit are zero-rated (IGST Act s 16(1)). The copy read is the 2017 text, which allows supply under bond or Letter of Undertaking without integrated tax, or payment and refund. Later amendments to s 16 were not read, so confirm the second route applies before relying on it.
- **Place of supply.** It is decided by law, not chosen. Inside India, a service to a registered person is supplied at that person's location, with sub-sections (3) to (14) of IGST Act s 12 as exceptions. Cross-border, the default is the recipient's location (s 13(2)). Inter-State or intra-State follows from that. Do not 'optimise' it.
- **Rates.** Service rates sit in a separate notification, not read. Nil-rated and exempt goods are not in Notification 9/2025. For a rate on a specific item, use `india-gst` and the current notification.

### Social security

- **Provident fund.** Contribution rates are held. The Ministry of Labour FAQ says the definition of wages under the Labour Codes took effect on 21 November 2025 (reply 7), and that the definition under the Code on Social Security 2020 governs ESI coverage (reply 12). That is an administrative statement, and nothing read applies it to provident fund contributions, so that step is inferred and held. Do not assume 'basic plus DA' without checking.
- **Employee contribution.** It counts under s 123 on opt-out rates only (Schedule XV paragraph 1(f)).
- **Employer contribution.** Schedule XI Part A paragraph 6 as substituted by the Finance Act 2026 from 1 April 2026 no longer contains its earlier 12% of salary limb. It now deems only interest above the notified rate. The ₹7,50,000 aggregate in s 17 still applies. Contribution duties under the Code are a separate question.
- **Voluntary provident fund.** The scheme terms were not read. For tax, the contribution uses s 123 room and counts toward the ₹2,50,000 or ₹5,00,000 interest test.
- **ESI.** It provides statutory insurance cover. The cover terms were not read.

**NPS.**

- **Employer contribution.** This is one of the few deductions that survive under s 202. Section 16(k) includes the employer's s 124 contribution in salary; it is not excluded merely because aggregate employer contributions are within ₹7,50,000. Section 17(1)(h) separately includes the aggregate excess over that limit across recognised provident fund, NPS and approved superannuation contributions; s 17(1)(i) addresses accretion related to that excess. Check that the NPS contribution shows on the employer's Form 130 certificate. Salary for the deduction limit includes dearness allowance where the terms so provide, and excludes other allowances and perquisites (s 124(13)(b)). Restructuring must be real and within the employer's terms.
- **At exit: tax.** Up to 60% of the amount payable on closure or opting out is exempt (Schedule II Sl. No. 6). The rest is taxable unless used for an annuity (s 124(6), (9)). Annuity income is taxable.
- **At exit: regulations.** Use the operative regulations substituted from 16 December 2025, not the earlier wording reproduced in their footnotes. Regulation 4(1)(a) requires at least 20% annuity for a non-government subscriber exiting after at least 15 years' subscription (or a higher scheme period), on attaining 60, or on superannuation/retirement under their employment terms. Government subscribers on superannuation/retirement use the 40% minimum in regulation 3(1)(a). That government rule also applies on superannuation/retirement to corporate subscribers of bodies under Central or State Government ownership and control, or a Government Company (regulation 4(1)(a) proviso).
- **Ordinary-exit small pots.** Under either regulation 3(1)(a) or 4(1)(a), a pot up to ₹8 lakh may be withdrawn in full or paid periodically. For a pot over ₹8 lakh and up to ₹12 lakh, up to ₹6 lakh may be withdrawn as a lump sum or periodic payout, with the balance used for systematic unit redemption for at least 6 years, annuity or another approved option. ₹12 lakh is not a universal full-withdrawal threshold. Separately, regulation 4(1)(e) allows a subscriber who joined at age 60 to before 85 to withdraw the full pot up to ₹12 lakh or another Authority-approved limit; otherwise its minimum annuity is 20%.
- **Early voluntary exit.** Before eligibility under regulation 4(1)(a), at least 80% buys an annuity, except that a pot up to ₹5 lakh or another Authority-approved limit may be withdrawn in full (regulation 4(1)(b)). Government resignation, dismissal or removal has the 80% rule and the same ₹5 lakh exception under regulation 3(1)(b). A permitted withdrawal does not enlarge the tax exemption: non-government ordinary exit and qualifying small-pot options can release cash above the exempt 60%.
- **Partial withdrawal.** Exempt up to 25% of own contributions (Schedule III Sl. No. 4).

**Salary structuring.** A higher salary under s 124(13)(b) raises the employer NPS limit, and it may raise provident fund and other wage-linked costs. Test take-home and employer cost together.

### Investments

| Instrument | Income tax rule read | Held |
| --- | --- | --- |
| PPF | Deduction under Schedule XV paragraph 1(e) if notified, on opt-out rates. Payment exempt under Schedule II Sl. No. 3 if the fund is within that entry, subject to the interest test there | ₹1,50,000 account limit, 15-year term and the 'EEE' label: Public Provident Fund scheme not read |
| ELSS | Deduction under paragraph 1(m) if a notified scheme, on opt-out rates. Gains under ss 196 and 198 if it is an equity fund | 3-year lock-in: scheme notification not read |
| NPS | See above | Scheme terms beyond the exit regulations |
| Sukanya Samriddhi | Deduction under paragraph 1(h) if notified. Payment exempt under Schedule II Sl. No. 5 | Deposit limits and account terms not read |
| NSC | Deduction under paragraph 1(i) if notified | 5-year term and treatment of accrued interest: not read |
| ULIP | Deduction under paragraph 1(a) or (k) by type. Maturity exempt under Schedule II Sl. No. 2 only if aggregate premium does not exceed ₹2,50,000 for policies from 1 February 2021, with premium to sum assured limits; death benefit exempt. Outside the exemption, gains are capital gains of the year of receipt (s 67(5)), and the scheme is an equity oriented fund only if it meets the s 198(8) test throughout the term | The prescribed s 67(5) calculation was not read |
| Other life insurance | Non-ULIP policies issued from 1 April 2023 are exempt only if aggregate premium does not exceed ₹5,00,000, with premium to sum assured limits (Schedule II Sl. No. 2). Outside the exemption, the sum above premiums not deducted is income under s 92(2)(l). Sums under s 127(4) and keyman policies are never excluded. The ₹2,50,000 and ₹5,00,000 tests do not apply to an International Financial Services Centre Insurance Office policy issued from 1 April 2025 | The prescribed s 92(2)(l) computation was not read |
| Listed equity and equity funds | Short-term 20%; long-term 12.5% over ₹1,25,000; no indexation | |
| Debt funds | Specified Mutual Fund units acquired from 1 April 2023, with over 65% in debt and money market instruments or 65% or more in such units, give short-term gains whatever the holding period (s 76) | Other debt funds follow the general capital gains rules |
| Market linked debentures and unlisted bonds | Short-term whatever the holding period (s 76), for unlisted bonds from 23 July 2024 | |
| Real estate | Over 24 months: 12.5%, or the s 197(3) ceiling. Otherwise at the person's rates | |

### Annual gains harvesting (listed equity)

Selling long-term units and rebuying can use the ₹1,25,000 limit each year. It works only if each sale meets s 198, including securities transaction tax on acquisition and transfer for shares and on transfer for units. The rebought lot restarts its holding period, so it needs over 12 months to be long-term again.

- **No statutory safe harbour.** Nothing read approves or condemns a same-day or next-day repurchase. The strategy is conditional on genuine transfers at market price.
- **Stripping rules.** Section 175(8) ignores a loss on securities or units bought within 3 months before a record date and sold within 3 months after (9 months for units), up to an exempt dividend or income. Section 175(9) ignores a loss on bonus-stripping facts.
- **GAAR.** A tax benefit includes deferral (s 184(11)). Section 179(1) requires a main purpose of obtaining a tax benefit and at least one of its listed limbs for an arrangement to be impermissible, subject to the step-or-part presumption in s 179(2). Rule 128's ₹3 crore aggregate exclusion must also be tested; see 'Red lines'.
- **Not free.** Brokerage, securities transaction tax and a market move between sale and rebuy all count. The 'zero tax' claim holds only for the gain within the limit.

See `Example 3`.

## Deadlines and filing

Returns go through the Income Tax Department's e-Filing portal (incometax.gov.in). GST returns go through the GST portal (gst.gov.in).

### Return due dates, s 263(1)(c) Table

| Person | Due date for tax year 2026-27 |
| --- | --- |
| Person with a s 172 report | 30 November 2027 |
| Company, person whose accounts must be audited, partner of such a firm, and spouse of such a partner | 31 October 2027 |
| Business or profession without audit, partner of such a firm, and spouse of such a partner | 31 August 2027 |
| Any other person | 31 July 2027 |

The Finance Act 2026 moved non-audit business cases to 31 August (s 66), so '31 July' alone is out of date. Its s 5 made the same change to the 1961 Act from 1 March 2026.

For assessment year 2026-27, CBDT Circular 7/2026 of 28 September 2026 extended Sl. No. 2 returns from 31 October 2026 to 21 November 2026, and so the audit report to 21 October 2026. It names no other category and no later year. Check each year for extensions.

**Other returns.** A belated return may be filed up to 9 months after the tax year ends, or before the assessment is completed, if earlier (s 263(4)). A revised return may be filed within 12 months after the tax year ends, or before the assessment is completed, if earlier (s 263(5)), and one filed beyond 9 months carries the s 428(b) fee. An updated return may be filed within 48 months from the end of the financial year after the tax year (s 263(6)), subject to its conditions, which were not fully read.

**Audit report.** Due on the specified date, one month before the return due date (s 63(5)(a)).

### Advance tax

Payable if the year's tax is ₹10,000 or more (s 404). A resident aged 60 or over with no business or professional income need not pay (s 403(3)).

| By | Cumulative share (s 408) |
| --- | --- |
| 15 June | 15% |
| 15 September | 45% |
| 15 December | 75% |
| 15 March | 100% |

Tax paid by 31 March counts as paid in the year (s 408(3)). Section 425(4) relieves shortfalls from capital gains, s 2(49)(n) income, first-time business income, and dividends, if the tax on them is paid in the remaining instalments or by 31 March.

### Planning calendar

| When | Action |
| --- | --- |
| April | Tax year starts. Compute both regimes. Give the employer Form 122 or 124 particulars. Review salary structure, and start any scheme only if its terms fit |
| By 15 June | First advance tax instalment. Give the employer house rent, leave travel and investment declarations |
| 31 July | Return due for non-audit individuals with no business income. Late filing loses carry forward under s 121 and, for no-business persons, the s 202(4)(b) route |
| 31 August | Return due for business or profession without audit |
| By 15 September | Second instalment. Mid-year investment review |
| 30 September | Audit report, unless extended |
| 31 October | Return due for companies and audited persons. Review capital gains position |
| By 15 December | Third instalment. Review s 123 room |
| January and February | Collect rent receipts, premium receipts, medical bills and donation details. Confirm landlord PAN if rent exceeds ₹1,00,000 |
| By 15 March | Final instalment |
| By 31 March | Make s 123, s 124(3) and s 126 payments. Any harvesting sale must complete in the tax year. Give the employer proofs |

## Penalties and interest

| Provision | Rule |
| --- | --- |
| Late return interest (s 423) | 1% simple a month on tax due |
| Advance tax shortfall (s 424) | 1% simple a month from 1 April if paid under 90% of assessed tax |
| Instalment deferment (s 425) | 1% simple a month for 3 months on each of the first 3 instalments, and 1 month on the last. No interest under s 425(2) if advance tax paid is (a) 12% or more of the tax due on returned income by 15 June; (b) 36% or more of it by 15 September. The text joins the limbs with neither 'and' nor 'or', so whether each relieves only its own instalment is held |
| Late return fee (s 428(a)) | ₹1,000 if total income does not exceed ₹5,00,000; ₹5,000 otherwise |
| Under-reporting (s 439(9)) | 50% of tax on the under-reported income |
| Misreporting (s 439(10), (11)) | 200% of that tax. Cases: misrepresentation or suppression of facts; failure to record investments; expenditure claimed without evidence; false book entries; unrecorded receipts; unreported international or specified domestic transactions; income in s 195(1)(b) |
| Wilful evasion (s 478) | Simple imprisonment up to 2 years, or fine, or both, over ₹50 lakh; up to 6 months over ₹10 lakh to ₹50 lakh; fine otherwise |
| Wilful failure to file (s 479) | Same bands, with the s 479(2) exceptions |
| Cash receipt (ss 186, 451) | Penalty equal to the sum received |
| Cash expenditure (s 36(4), (5)) | Disallowance where payments to a person in a day exceed ₹10,000 otherwise than by the permitted modes; ₹35,000 for hire of goods carriages; prescribed exceptions under s 36(7) |

The s 439(8) exclusions from under-reporting and any immunity route were only partly read.

**Cash receipt limit.** No one may receive ₹2,00,000 or more in aggregate from a person in a day, for a single transaction, or for transactions on one event or occasion from a person, except by account payee cheque, account payee draft, bank electronic clearing or a prescribed electronic mode. It does not apply to Government, banks, post office savings banks or co-operative banks, s 185 transactions or notified cases (s 186). The penalty falls on the recipient.

### GAAR (Chapter XI)

Section 179(1): an arrangement is impermissible if its main purpose is a tax benefit and it also meets any one of these tests:

- it creates rights or obligations not normally created between persons at arm's length;
- it results in misuse or abuse of the Act;
- it lacks commercial substance, in whole or part, or is deemed to under s 180;
- it is entered into or carried out by means or in a manner not normally used for bona fide purposes.

Section 179(2) presumes the main purpose from a step having it. Section 180(1) deems a lack of commercial substance where the substance or effect of the whole differs significantly from the form of its steps or a part; where the arrangement involves round trip financing, an accommodating party, elements that offset or cancel each other, or a transaction through persons that disguises the value, location, source, ownership or control of funds; where the location of an asset or transaction, or a party's residence, has no substantial commercial purpose other than a tax benefit; or where it has no significant effect on a party's business risks or net cash flows apart from the tax benefit. Section 181 sets the consequences, which include denial of the benefit and recharacterisation.

Rule 128, as notified, disapplies the chapter where the aggregate tax benefit in the relevant tax year to all parties to the arrangement does not exceed ₹3 crore. Rule 128 also has limbs for certain foreign institutional investors and their investors, and for income from transferring investments made before 1 April 2017. These are not restated: read the rule if those facts arise. Without prejudice to that last limb, Chapter XI applies to any arrangement, whatever its date, for a tax benefit obtained on or after 1 April 2017 (rule 128(2)). The threshold is an exclusion and does not bless an arrangement. Specific anti-avoidance rules such as ss 36, 99 and 175 apply whatever its amount.

### Scrutiny points

These are consequences of the rules. No source read ranks them, so the earlier 'most common trigger' claim is held.

| Fact | Consequence |
| --- | --- |
| House rent allowance without genuine rent | Exclusion denied; s 439 exposure, with s 439(11)(a) or (c) possible |
| False s 123 or s 126 receipts | Deduction denied; s 439(11) and s 478 exposure |
| Transactions at the rule 237 thresholds | Reported to the Department. Rule 237(6) separately requires statements for pre-filling the return, on capital gains on listed securities and mutual fund units, dividends and interest |
| Income differing from the Annual Information Statement | Reconcile before filing. Escaped income is reached under ss 279 and 280 |
| Capital gains without advance tax | Interest under ss 424 and 425, subject to s 425(4) |
| Gifts from non-relatives over ₹50,000 in aggregate | Income under s 92(2)(m), with s 92(3) exceptions for relatives, marriage, will or inheritance and the other listed cases |
| Benami property | Prohibition of Benami Property Transactions Act 1988. Its penalty terms were not read: held |
| Transfers to spouse or minor | Clubbing under s 99 |
| Presumptive income out of line with assets or lifestyle | Possible enquiry. No specific rule read, so this is a risk note and not a threshold |

### Red lines

- Never advise fabricating rent receipts or any other evidence.
- Never advise backdating an investment or payment.
- Never advise taking ₹2,00,000 or more in cash on s 186 facts, or splitting a sum to avoid the limit.
- Never advise paying over the s 36(4) cash limit unless an exception is shown.
- Never advise structuring solely to stay under the GAAR threshold.
- Never advise ignoring Annual Information Statement differences: resolve them before filing.

## Cross-border points

- **Residence** decides most of this file: see `in-tax-residency`. The rebate, the s 58 tables and the senior bands all need residence.
- **Foreign assets.** A resident, other than not ordinarily resident, must file whatever the income level if at any time in the year they hold an asset or financial interest outside India, have signing authority in an account outside India, or are a beneficiary of such an asset, unless the income from it is includible in the holder's income (s 263(1)(a)(ix), (b)). Foreign asset disclosure carries its own consequences, not covered here.
- **Foreign tax.** Relief is under s 159 (agreements) or s 160 (a resident's foreign income taxed in a country with no agreement). See `in-income-tax`.
- **Related parties.** See `india-transfer-pricing`.
- **Non-residents and returnees.** See `india-to-uae-singapore-nri-tax`. Section 124 and Schedule XV rows above are not tested for them.
- **GST.** See the place of supply and export points above.

## Two worked examples that recompute

All examples use tax year 2026-27, resident individuals under 60, income below ₹50 lakh so no surcharge and, except as Example 3 states, no other income or special-rate items. Each uses the rate tables above. Inputs are stated, not assumed for any client.

### Example 1: regime choice, salaried, ₹15,00,000

**Stated inputs.** Private employer, salary ₹15,00,000 including house rent allowance, no professional tax. On opt-out rates: rule 279 exclusion ₹2,40,000 (rent paid in the city of work, accommodation not owned), standard deduction ₹50,000, s 123 ₹1,50,000, s 124(3) ₹50,000, s 126 ₹25,000. Interest ₹2,00,000 on a house in another city that the employee cannot actually occupy, which qualifies under ss 21(6) and 22(2).

The earlier version of this example was wrong on both sides. Its default regime tax is ₹93,750, not ₹1,57,500. Its opt-out income is ₹7,85,000, not ₹8,85,000.

```oa-check
name: Regime choice at 15 lakh salary with and without housing items
inputs:
  salary: 1500000
  sd_default: 75000
  sd_optout: 50000
  hra: 240000
  s123: 150000
  s124_3: 50000
  s126: 25000
  interest: 200000
steps:
  - t_default: salary - sd_default
  - tax_default: pct(min(max(t_default - 400000, 0), 400000), 5) + pct(min(max(t_default - 800000, 0), 400000), 10) + pct(min(max(t_default - 1200000, 0), 400000), 15) + pct(min(max(t_default - 1600000, 0), 400000), 20)
  - total_default: round(tax_default * 1.04, 2)
  - t_optout: salary - hra - sd_optout - interest - s123 - s124_3 - s126
  - tax_optout: pct(min(max(t_optout - 250000, 0), 250000), 5) + pct(min(max(t_optout - 500000, 0), 500000), 20) + pct(max(t_optout - 1000000, 0), 30)
  - total_optout: round(tax_optout * 1.04, 2)
  - saving: total_default - total_optout
  - t_no_housing: salary - sd_optout - s123 - s124_3 - s126
  - tax_no_housing: pct(min(max(t_no_housing - 250000, 0), 250000), 5) + pct(min(max(t_no_housing - 500000, 0), 500000), 20) + pct(max(t_no_housing - 1000000, 0), 30)
  - total_no_housing: round(tax_no_housing * 1.04, 2)
  - cost_if_no_housing: total_no_housing - total_default
  - breakeven_income: 500000 + (tax_default - 12500) / 0.2
  - breakeven_reductions: salary - sd_optout - breakeven_income
expected:
  t_default: 1425000
  tax_default: 93750
  total_default: 97500
  t_optout: 785000
  tax_optout: 69500
  total_optout: 72280
  saving: 25220
  t_no_housing: 1225000
  total_no_housing: 187200
  cost_if_no_housing: 89700
  breakeven_reductions: 543750
```

The s 156(2)(b) marginal rebate gives nothing here: income is ₹2,25,000 over ₹12,00,000, more than the ₹93,750 tax.

**Decision point.** With both housing items, opt-out rates cost ₹25,220 less. Without them, they cost ₹89,700 more. Old-regime reductions of ₹5,43,750 at this salary is the point of indifference. If either housing item fails its conditions, rerun: the regime answer can flip.

### Example 2: employer NPS

**Stated inputs.** Private employer. Salary for the s 124(13)(b) limit stays ₹8,00,000. Before restructuring, cash salary is ₹18,00,000 with no employer NPS contribution. Afterwards, cash salary is ₹16,88,000 and the employer contributes ₹1,12,000 to NPS. Section 16(k) includes that contribution, so gross salary income stays ₹18,00,000 in both cases; the same ₹18,00,000 employer outlay is split differently. Other employer costs are unchanged. No other deductions. Aggregate employer contributions to recognised provident fund, NPS and approved superannuation stay within ₹7,50,000 after the change, with no taxable accretion on earlier excess contributions under s 17(1)(i). The employer's terms permit this genuine prospective restructuring.

The earlier version said the full ₹1,12,000 is deductible in both regimes. It is not: 14% applies to a private employer's employee only under s 202(1). On opt-out rates the limit is 10%, ₹80,000.

```oa-check
name: Employer NPS deduction by regime at 18 lakh salary income
inputs:
  income: 1800000
  salary_124: 800000
  sd_default: 75000
  sd_optout: 50000
  nps_paid: 112000
steps:
  - ded_default: pct(salary_124, 14)
  - ded_optout: pct(salary_124, 10)
  - t0_default: income - sd_default
  - t1_default: t0_default - ded_default
  - tax0_default: 60000 + pct(min(max(t0_default - 1200000, 0), 400000), 15) + pct(max(t0_default - 1600000, 0), 20)
  - tax1_default: 60000 + pct(min(max(t1_default - 1200000, 0), 400000), 15) + pct(max(t1_default - 1600000, 0), 20)
  - saving_default: round((tax0_default - tax1_default) * 1.04, 2)
  - t0_optout: income - sd_optout
  - t1_optout: t0_optout - ded_optout
  - tax0_optout: 112500 + pct(t0_optout - 1000000, 30)
  - tax1_optout: 112500 + pct(t1_optout - 1000000, 30)
  - saving_optout: round((tax0_optout - tax1_optout) * 1.04, 2)
  - cash_after: income - nps_paid
  - net0_default: income - round(tax0_default * 1.04, 2)
  - net1_default: cash_after - round(tax1_default * 1.04, 2)
  - cash_reduction_default: net0_default - net1_default
  - net0_optout: income - round(tax0_optout * 1.04, 2)
  - net1_optout: cash_after - round(tax1_optout * 1.04, 2)
  - cash_reduction_optout: net0_optout - net1_optout
expected:
  ded_default: 112000
  ded_optout: 80000
  tax0_default: 145000
  tax1_default: 122600
  saving_default: 23296
  saving_optout: 24960
  cash_after: 1688000
  net0_default: 1649200
  net1_default: 1560496
  cash_reduction_default: 88704
  net0_optout: 1449000
  net1_optout: 1361960
  cash_reduction_optout: 87040
```

**Decision point.** The default regime saves ₹23,296 at a 20.8% marginal rate, but available cash falls ₹88,704 and ₹1,12,000 moves into NPS. Opt-out rates save ₹24,960 on a smaller deduction because the marginal rate is 31.2%; available cash falls ₹87,040. Deducted amount is not the right test: compare total tax and cash under each regime and treat the NPS money as locked until an eligible exit. No additional employer contribution is assumed outside the stated cost.

### Example 3: gains harvesting

**Stated inputs.** Listed equity shares bought and sold with securities transaction tax, all held over 12 months, ₹3,00,000 of unrealised gain, flat price, no other s 198 gains, nil band already used by other income, no costs. Harvest: ₹1,25,000 in each of 2 tax years, and ₹50,000 in a third.

```oa-check
name: Long-term gain on one sale against three annual harvests
inputs:
  gain: 300000
  limit: 125000
steps:
  - tax_one: pct(max(gain - limit, 0), 12.5)
  - total_one: round(tax_one * 1.04, 2)
  - year3_gain: gain - limit - limit
  - harvest_tax: pct(max(year3_gain - limit, 0), 12.5)
  - saving: total_one - harvest_tax
expected:
  tax_one: 21875
  total_one: 22750
  year3_gain: 50000
  harvest_tax: 0
  saving: 22750
```

**Decision point.** The saving is ₹22,750, not the ₹21,875 in the earlier version, which left out cess. It falls to the extent prices rise on repurchased lots, or costs and spreads arise. A rebought lot sold within 12 months gives short-term gain at 20%. Harvesting in a year with other s 198 gains uses the same ₹1,25,000 limit.

### Example 4: presumptive income and regime choice

**Stated inputs.** Resident individual trader, turnover ₹1,50,00,000, all received by banking mode, cash payments under 5%, so s 63 audit is not triggered at ₹10 crore. Sl. No. 1 eligible. No other income. Actual profit ₹12,00,000. On opt-out rates: s 123 ₹1,50,000.

```oa-check
name: Presumptive 6 percent against actual profit by regime
inputs:
  turnover: 15000000
  actual: 1200000
  s123: 150000
steps:
  - deemed: pct(turnover, 6)
  - tax_default: pct(min(max(deemed - 400000, 0), 400000), 5) + pct(min(max(deemed - 800000, 0), 400000), 10)
  - rebate: min(tax_default, 60000)
  - total_default: round((tax_default - rebate) * 1.04, 2)
  - tax_actual: pct(min(max(actual - 400000, 0), 400000), 5) + pct(min(max(actual - 800000, 0), 400000), 10)
  - total_actual: round((tax_actual - min(tax_actual, 60000)) * 1.04, 2)
  - t_optout: deemed - s123
  - tax_optout: pct(min(max(t_optout - 250000, 0), 250000), 5) + pct(min(max(t_optout - 500000, 0), 500000), 20)
  - total_optout: round(tax_optout * 1.04, 2)
expected:
  deemed: 900000
  tax_default: 30000
  total_default: 0
  tax_actual: 60000
  total_actual: 0
  t_optout: 750000
  tax_optout: 62500
  total_optout: 65000
```

**Decision point.** Under the default regime, tax is nil on the deemed ₹9,00,000 and also on the actual ₹12,00,000, because the rebate covers both. So s 58 saves no income tax on these facts. The earlier claims of about ₹40,000 tax saved and ₹50,000 compliance saved are not supported: the first fails on these figures and the second was not sourced. Opting out would cost ₹65,000. Audit is a separate test. Declaring the ₹9,00,000 needs no s 63 audit, and the ₹10 crore limit also covers these facts if all its cash limbs are met.

### Example 5: just over ₹12,00,000

**Stated inputs.** Resident individual eligible for s 156 rebate, salary ₹13,00,000, default regime, no other income. For the NPS comparison, salary within s 124(13)(b) is ₹8,00,000. Aggregate employer contributions to recognised provident fund, NPS and approved superannuation stay within ₹7,50,000 after the change, with no taxable accretion on earlier excess contributions under s 17(1)(i).

```oa-check
name: Marginal rebate just above 12 lakh
inputs:
  salary: 1300000
  sd: 75000
  nps: 25000
steps:
  - income: salary - sd
  - tax: pct(min(max(income - 400000, 0), 400000), 5) + pct(min(max(income - 800000, 0), 400000), 10) + pct(min(max(income - 1200000, 0), 400000), 15)
  - excess: income - 1200000
  - rebate: max(tax - excess, 0)
  - total: round((tax - rebate) * 1.04, 2)
  - income_nps: income - nps
  - tax_nps: pct(min(max(income_nps - 400000, 0), 400000), 5) + pct(min(max(income_nps - 800000, 0), 400000), 10)
  - rebate_nps: min(tax_nps, 60000)
  - total_nps: round((tax_nps - rebate_nps) * 1.04, 2)
  - cash_without_nps: salary - total
  - cash_with_nps: salary - nps - total_nps
  - cash_change: cash_with_nps - cash_without_nps
expected:
  income: 1225000
  tax: 63750
  excess: 25000
  rebate: 38750
  total: 26000
  income_nps: 1200000
  tax_nps: 60000
  rebate_nps: 60000
  total_nps: 0
  cash_without_nps: 1274000
  cash_with_nps: 1275000
  cash_change: 1000
```

**Decision point.** Income ₹25,000 over the limit costs ₹26,000. If the employer's terms permit a real prospective split of the same ₹13,00,000 outlay into ₹12,75,000 cash and ₹25,000 employer NPS, gross salary stays ₹13,00,000 under s 16(k). The s 124(2) deduction, within the ₹1,12,000 limit on the stated salary, takes total income to ₹12,00,000 and tax to nil. Available cash rises ₹1,000, with ₹25,000 held in NPS until an eligible exit. Other employer costs are unchanged. An additional contribution on top of cash salary would be a different cost comparison.

## Ask the client first

Questions come before any output, and an unanswered fact stays Needs Input.

1. **Who.** Residence for the year, date of birth, marital status, children and their ages, parents' ages, disability of self or dependants, and whether the taxpayer is an individual, HUF, firm, LLP or company.
2. **Income.** Each type for the tax year and the last 2 years: salary with its breakdown, business or profession with turnover and receipts by mode, house property, capital gains, dividends, interest, foreign income, and any other.
3. **Regime position.** Any s 202(4) opt-out in force or earlier withdrawal, any carried-forward loss by type and year, and whether past returns were filed on time.
4. **Employer and contributions.** Employer type, salary as s 124(13)(b) and rule 279(2) define it, house rent allowance, rent paid and landlord PAN, city of work, employer provident fund, NPS and superannuation totals, and own contributions.
5. **Assets and transactions.** Home loan dates, completion date and lender's certificate, houses owned and their use, planned sales with cost and acquisition dates, listed holdings by lot, securities transaction tax paid, gifts, transfers to family, and cash dealings of ₹2,00,000 or more.
6. **GST and evidence.** State of supply, turnover, inter-State or e-commerce supplies, existing registrations on the PAN, and documents supporting each claim, along with the purpose of any series of transactions.

### Completion checks

- Every step cites its provision and states its condition.
- Both regimes are computed before a regime recommendation.
- Each family payment or transfer is tested against ss 36(2) and 99.
- Each step with a tax purpose is tested against s 179 and the specific rules.
- Held items are flagged, not estimated.
- A qualified reviewer signs off before any client acts.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| Income-tax Act 2025, No. 30 of 2025, Gazette text, read in part: the sections cited | https://egazette.gov.in/WriteReadData/2025/265620.pdf | 2026-11-05 |
| Income-tax Act 2025 as amended by the Finance Act 2026, Income Tax Department consolidation, archived 12 June 2026, read in part: the sections and Schedules cited | https://web.archive.org/web/20260612085646id_/https://www.incometaxindia.gov.in/documents/d/guest/income_tax_act_2025_as_amended_by_fa_act_2026-pdf | 2026-11-06 |
| Finance Act 2026, No. 4 of 2026, Gazette text, read in part: ss 1 to 3, 5, 66 and 127(a)(iii), and Parts I-A and I-B of the First Schedule | https://egazette.gov.in/WriteReadData/2026/271439.pdf | 2026-11-07 |
| Finance Bill 2026 as introduced, read in part: rates clauses, for comparison only, not relied on | https://egazette.gov.in/WriteReadData/2026/269757.pdf | 2026-11-05 |
| Income-tax Act 1961, India Code copy archived 24 March 2026, read in part: arrangement of sections, ss 64 and 115-O headings and s 80D only. The copy omits s 115BAC | https://web.archive.org/web/20260324194825id_/https://www.indiacode.nic.in/bitstream/123456789/2435/1/a1961-43.pdf | 2026-11-06 |
| Income-tax Rules 2026, G.S.R. 198(E), as notified 20 March 2026, Department copy archived that day, read in part: rules 25, 127, 128, 204, 205, 237, 278, 279, 280, Appendix I, and Forms 122, 124, 125 and 130 in part | https://web.archive.org/web/20260320162411id_/https://www.incometaxindia.gov.in/documents/d/guest/en-notified-it-rules-2026-20-03-2026-pdf | 2026-11-05 |
| CBDT Circular 7/2026 of 28 September 2026, read in full, with an extraction warning at the end of the file | https://www.incometax.gov.in/iec/foportal/sites/default/files/2026-09/Circular-7-2026.pdf | 2026-11-05 |
| PFRDA (Exits and Withdrawals under the NPS) Regulations 2015, last amended 16 December 2025, read in part: regulations 3 and 4 | https://www.pfrda.org.in/documents/33652/184762/PFRDA+(Exits+and+Withdrawals+under+the+NPS)+Regulations,+2015+%5BLast+amended+on+16+December+2025%5D.pdf | 2026-11-05 |
| S.O. 5109(E) of 17 September 2026, Ministry of Labour and Employment, read in full | https://egazette.gov.in/WriteReadData/2026/276299.pdf | 2026-11-05 |
| Ministry of Labour and Employment, additional FAQs on Labour Codes, as on 16 March 2026, read in part: replies on wages and ESI coverage | https://www.labour.gov.in/static/uploads/2026/03/a4ccf4c6d97c4f1f36a6d83f8c64213d.pdf | 2026-11-05 |
| CGST Act s 10, CBIC tax information portal, undated text, read in part: sub-sections (1) to (5) | https://taxinformation.cbic.gov.in/content/html/tax_repository/gst/acts/2017_CGST_act/active/chapter3/section10_v1.00.html | 2026-11-05 |
| CGST Act s 16, CBIC tax information portal, undated text, read in part: sub-sections (2) to (4) and the provisos to sub-section (2) | https://taxinformation.cbic.gov.in/content/html/tax_repository/gst/acts/2017_CGST_act/active/chapter5/section16_v1.00.html | 2026-11-06 |
| CGST Act s 22, CBIC tax information portal, undated text, read in part: sub-section (1), its provisos and the Explanation | https://taxinformation.cbic.gov.in/content/html/tax_repository/gst/acts/2017_CGST_act/active/chapter6/section22_v1.00.html | 2026-11-06 |
| CGST Act s 24, CBIC tax information portal, undated text, read in part: its list, to test the s 24 carve-out in Notification 10/2019 | https://taxinformation.cbic.gov.in/content/html/tax_repository/gst/acts/2017_CGST_act/active/chapter6/section24_v1.00.html | 2026-11-05 |
| CGST Act s 54, CBIC tax information portal, undated text, read in part: sub-section (3) and its provisos | https://taxinformation.cbic.gov.in/content/html/tax_repository/gst/acts/2017_CGST_act/active/chapter11/section54_v1.00.html | 2026-11-05 |
| CGST Act as on 1 January 2022, CBIC copy, read in part: s 9 only | https://cbic-gst.gov.in/pdf/CGST-Act-2017-amended-01012022.pdf | 2026-11-05 |
| CGST Rules 2017 Part A, edition of 23 April 2019, read in part: rule 7 only. Later amendments not read | https://cbic-gst.gov.in/pdf/23042019-CGST-Rules-2017-Part-A-Rules.pdf | 2026-11-05 |
| IGST Act 2017, GST Council copy of the 2017 text, read in part: ss 12(1) and (2), 13(1) and (2), and 16(1) to (3). Later amendments not read | https://gstcouncil.gov.in/sites/default/files/2024-03/annexure-5-igst-act_2017.pdf | 2026-11-05 |
| Notification 10/2019-Central Tax, read in full | https://gstcouncil.gov.in/sites/default/files/2024-05/notfctn-10-central-tax-english-2019.pdf | 2026-11-05 |
| Notification 14/2019-Central Tax, read in full | https://gstcouncil.gov.in/sites/default/files/2024-05/notfctn-14-central-tax-english-2019.pdf | 2026-11-05 |
| Notification 10/2023-Central Tax, read in full | https://einvoice6.gst.gov.in/content/wp-content/uploads/2023/05/GST-notification-10-central-tax-english-2023.pdf | 2026-11-05 |
| Notification 9/2025-Integrated Tax (Rate), ICAI print hosted on CBIC, read in part: Schedule headings, Schedules III and VII, Schedule IV Sl. No. 5 and paragraph 2 | https://courier.cbic.gov.in/ECCS/advisory/2025/NOTIFICATION%20NO.%209_2025-INTEGRATED%20TAX%20(RATE)%20-1759486719.pdf | 2026-11-05 |
| CBIC Circular 97/16/2019-GST of 5 April 2019, read in part: its first page. Notification 2/2019-Central Tax (Rate) itself was not read | https://cbic-gst.gov.in/pdf/circular-cgst-97.pdf | 2026-11-05 |

Not yet confirmed: EPF, EPS, EDLI and ESI contribution rates and any schemes or rules under the Code on Social Security 2020 (EPFO refused access and ESIC was unreachable); whether the Labour Codes' wages definition sets the provident fund contribution base; Public Provident Fund, Sukanya Samriddhi, NSC and ELSS scheme limits, terms and lock-ins; 2025-26 slabs under 1961 Act s 115BAC; old section numbers beyond the 1961 arrangement of sections read; amendments to the Income-tax Rules 2026 after 20 March 2026 (the Department's site refused direct access), including any to rules 128, 204, 205, 237 and 279; amendments to the 2025 Act after the 12 June 2026 copy; whether Form 12BBA survives under another rule; whether Sl. No. 1 declarants under s 58 need books under s 62; s 156 against special-rate income other than s 198; the prescribed calculations for life policies outside the exemption (ss 67(5), 92(2)(l)); whether each s 425(2) limb relieves only its own instalment; the s 263(6) conditions; penalty immunity routes; Prohibition of Benami Property Transactions Act 1988 terms; rule 36(4) and the GSTR-2B link; State and Union territory GST rates and combined composition rates; Notification 2/2019-Central Tax (Rate) itself; CGST Rules after April 2019; IGST Act amendments, including to s 16(3); Notification 13/2020-Central Tax; that e-invoicing generates an invoice reference number through an NIC portal or improves credit accuracy; Constitution article 279A(4)(g), the special category States it leaves, and any notification raising their ₹10 lakh limit; later amendments to Notifications 10/2019 and 14/2019-Central Tax; rate notifications after 9/2025, and service rates.

### Version history

| Version | Date | Change |
| --- | --- | --- |
| 1.2 | 2026-11-07 | Converted to the upstream template. Set the year to tax year 2026-27 under the Income-tax Act 2025 and tied each strategy to its provision and condition. Corrected section numbers, 4 worked examples, the GAAR test and citation, the filing dates, the presumptive limits, the registration, composition and rate statements for GST, the depreciation labels, the reporting thresholds and the NPS exit rule. Removed the bookkeeping base. Held payroll rates and scheme terms not read. Returned to Tier 2 under template rule 11. Repair review clarified employer NPS salary inclusion and cash effects, current exit eligibility and small-pot options, spouse allocation and business proportions, medical expenditure and GAAR. |
| 1.1 | 2026-11-01 | Previous version, in the older layout. |

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a Chartered Accountant, tax consultant, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.
