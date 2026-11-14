---
name: india-financial-statements
description: "Use this skill whenever asked about Indian company annual financial statements for the financial year ending 31 March 2027 (FY 2026-27). Trigger on phrases like financial statements India, Companies Act 2013 accounts, Schedule III, Ind AS or AS, Ind AS applicability, statutory audit India, CARO 2020, small company India, One Person Company accounts, AOC-4, AOC-4 XBRL, MGT-7, MGT-7A, AGM deadline, internal audit section 138, deferred tax rate India, balance sheet format India, or any question about preparing, auditing or filing a company's accounts with the Registrar of Companies. It covers the Ind AS roadmap, the small company limits from 1 December 2025, required statements, year-end adjustments with the 2026-27 company tax rates, Schedule III formats, audit and CARO tests, internal audit, AGM timing and ROC filing periods. Tier 2, not reviewed by an accountant."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/india-financial-statements"
  jurisdiction: "IN"
  tax_year: "2026"
  last_updated: "2026-11-14"
---

# India Company Financial Statements: Framework, Formats, Audit and Filing, FY 2026-27

> **General reference only.** This skill is general reference material for AI-assisted workflows. It has not been reviewed for any specific company's facts. Do not rely on it to prepare, sign or file accounts without review by a qualified professional (a chartered accountant or company secretary) in India.

This skill covers the annual financial statements of a company under the Indian Companies Act, 2013: which accounting framework applies (Ind AS or the Accounting Standards), which statements to prepare, the small company and One Person Company relaxations, the statutory audit and the CARO Order of 2020, internal audit, and filing with the Registrar of Companies. Tax year: FY 2026-27. For Indian income tax this means the tax year from 1 April 2026 to 31 March 2027 under the Income-tax Act, 2025, which replaced the Income-tax Act, 1961 from 1 April 2026. For company law, the skill states the rules in force on 14 November 2026; they apply to financial statements for the financial year ending 31 March 2027 unless a rule below says otherwise. The Corporate Laws (Amendment) Bill, 2026 is not law (see "Pending, not law" below).

## Who this applies to

| Field | Value |
| --- | --- |
| Country | India (Republic of India) |
| Currency | INR |
| Filing authority | Ministry of Corporate Affairs (MCA), Registrar of Companies (ROC) |
| Primary legislation | Companies Act, 2013, Chapter IX (sections 128 to 138, accounts) and Chapter X (sections 139 to 148, audit) |
| Supporting legislation | Companies (Accounts) Rules, 2014; Companies (Audit and Auditors) Rules, 2014; Companies (Indian Accounting Standards) Rules, 2015; Companies (Accounting Standards) Rules, 2021; Companies (Auditor's Report) Order, 2020, referred to in this skill as CARO (2020) |
| Accounting standards | Ind AS (converged with IFRS) or the Accounting Standards (AS), by the Ind AS roadmap tests in the rates table |
| Financial year | Section 2(41): the period ending on 31 March every year (a company incorporated on or after 1 January may run to 31 March of the following year) |
| Statement formats | Schedule III: Division I (AS companies), Division II (Ind AS companies other than NBFCs), Division III (Ind AS NBFCs) |
| Filing form | e-Form AOC-4, AOC-4 XBRL or AOC-4 NBFC (Ind AS); consolidated statements in AOC-4 CFS (or the XBRL or NBFC version) |
| Filing deadline | Thirty days after the AGM (section 137(1)); 180 days from the close of the financial year for an OPC |
| AGM | Section 96: within six months of the close of the financial year (first AGM within nine months), not more than fifteen months between AGMs; an OPC holds none |

### Which framework applies

The Companies (Indian Accounting Standards) Rules, 2015 set the Ind AS roadmap. The tests use net worth. Once a company applies Ind AS, voluntarily or because it met a test, it must keep applying Ind AS in all later years even if it no longer meets the test.

| Entity type | Framework |
| --- | --- |
| Listed company (main board, India or abroad) | Ind AS (Phase I or Phase II) |
| Unlisted company with net worth at or above the Phase II amount in the rates table | Ind AS |
| Holding, subsidiary, joint venture or associate of an Ind AS company | Ind AS |
| Company listed only on an SME exchange | AS, unless it opts into Ind AS |
| Any other company, including most small companies and One Person Companies | AS (Companies (Accounting Standards) Rules, 2021), unless it opts into Ind AS |
| NBFC | A separate NBFC roadmap in the same Rules, from accounting periods beginning on or after 1 April 2018 (first phase) or 1 April 2019 (second phase); check the NBFC net worth tests in the Rules |
| Banking company, insurance company | Not covered by this skill. Refer (see the refusal list) |

### One Person Company (section 2(62))

Section 2(62) defines a One Person Company as "a company which has only one person as a member" (CARO 2020 Guidance Note, https://resource.cdn.icai.org/60117aasb48979-a.pdf ). The definition carries no capital or turnover limit.

### Interaction with other skills

- Income tax computation, tax audit and the return: outside this skill; see `india-income-tax` for individuals and `india-transfer-pricing` for related-party pricing. Formation and post-incorporation filings: see `india-formation`. Gratuity: see `india-payroll`. Choice of company tax regime: see `india-tax-optimization`.

## Rates, bands and thresholds

### Ind AS roadmap (Companies (Indian Accounting Standards) Rules, 2015, rule 4)

| Item | Value | Note | Source |
| --- | --- | --- | --- |
| Phase I (accounting periods beginning on or after 1 April 2016): any company, listed or unlisted, with net worth of | rupees five hundred crore or more | "companies other than those covered by sub-clause (a) above and having net worth of rupees five hundred crore or more" | https://resource.cdn.icai.org/87811bos-280825-final-ch1.pdf |
| Phase II (accounting periods beginning on or after 1 April 2017): every listed company whatever its net worth, and an unlisted company with net worth of | rupees two hundred and fifty crore or more | "having net worth of rupees two hundred and fifty crore or more but less than rupees five hundred crore" | https://resource.cdn.icai.org/87811bos-280825-final-ch1.pdf |
| Group rule | Holding, subsidiary, joint venture and associate companies of a company covered above also apply Ind AS | "holding, subsidiary, joint venture or associate companies of companies covered by sub- clause (a) and sub-clause (b)" | https://resource.cdn.icai.org/87811bos-280825-final-ch1.pdf |
| SME exchange | The roadmap does not apply to a company whose securities are listed (or being listed) on an SME exchange | "the roadmap shall not be applicable to companies whose securities are listed or are in the process of being listed on SME exchange" | https://resource.cdn.icai.org/87811bos-280825-final-ch1.pdf |
| Once in, always in | Ind AS continues in later years | "it shall be required to follow the Indian Accounting Standards (Ind AS) for all the subsequent financial statements" | https://resource.cdn.icai.org/87811bos-280825-final-ch1.pdf |

### Small company limits (section 2(85), rule 2(1)(t) as substituted by G.S.R. 880(E), from 1 December 2025)

| Item | Value | Note | Source |
| --- | --- | --- | --- |
| Paid-up share capital, not more than | rupees ten crores | "paid up capital and turnover of the small company shall not exceed rupees ten crores and rupees one hundred crores respectively" | https://egazette.gov.in/WriteReadData/2025/268124.pdf |
| Turnover, not more than | rupees one hundred crores | "paid up capital and turnover of the small company shall not exceed rupees ten crores and rupees one hundred crores respectively" | https://egazette.gov.in/WriteReadData/2025/268124.pdf |

### Company income-tax rates for deferred tax, tax year 2026-27

| Item | Value | Note | Source |
| --- | --- | --- | --- |
| Domestic company whose total turnover or gross receipt in tax year 2024-25 did not exceed INR 400 crore | 25% | "where its total turnover or the 25% of the total gross receipt in the tax year 2024-25 income; does not exceed ₹ 400 crores" | https://egazette.gov.in/WriteReadData/2026/271439.pdf |
| Turnover test for the lower rate (tax year 2024-25 figures) | INR 400 crore | "where its total turnover or the 25% of the total gross receipt in the tax year 2024-25 income; does not exceed ₹ 400 crores" | https://egazette.gov.in/WriteReadData/2026/271439.pdf |
| Any other domestic company not opting under section 200 or 201 | 30% | "does not exceed ₹ 400 crores; (ii) other than that referred to in 30% of the total item (i) income" | https://egazette.gov.in/WriteReadData/2026/271439.pdf |
| Minimum alternate tax on book profit, section 206 (substituted for the old rate from 1 April 2026) | 14% | "for the figures and symbol “15%”, the figures and symbol “14%” shall be substituted" | https://egazette.gov.in/WriteReadData/2026/271439.pdf |

| Item | Value | Note | Source |
| --- | --- | --- | --- |
| Section 200 rate, at the option of a domestic company, on income computed without the listed deductions | 22% | "the income-tax payable for a tax year shall be at the rate of 22%, at the option of a person being a domestic company" | https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Section 201 rate for a domestic company in manufacture or production that opts in, was set up and registered on or after 1 October 2019 and commenced manufacturing or production on or before 31 March 2024, on income other than the specified items | 15% | "1. A (a) 15% on the total Such domestic company" | https://egazette.gov.in/WriteReadData/2025/265620.pdf |

### Filing periods and XBRL tests

| Item | Value | Note | Source |
| --- | --- | --- | --- |
| Filing period for financial statements (section 137(1)) | thirty days | "shall be filed with the Registrar within thirty days of the date of annual general meeting in such manner, with such fees or additional fees as may be prescribed" | https://resource.cdn.icai.org/74737bos60488-m2-cp9.pdf |
| XBRL filing (Form AOC-4 XBRL), rule 3(1) of the XBRL Rules, 2015: listed companies and their Indian subsidiaries, and any company with paid-up capital of | five crore rupees or above | "(ii) Companies having paid up capital of five crore rupees or above" | https://resource.cdn.icai.org/74737bos60488-m2-cp9.pdf |
| XBRL filing: any company with turnover of | one hundred crore rupees or above | "(iii) companies having turnover of one hundred crore rupees or above" | https://resource.cdn.icai.org/74737bos60488-m2-cp9.pdf |
| XBRL filing: every company that must prepare Ind AS statements, other than the classes exempted below | Ind AS companies | "(iv) All companies which are required to prepare their financial statements in accordance with Companies (Indian Accounting Standards) Rules, 2015" | https://resource.cdn.icai.org/74737bos60488-m2-cp9.pdf |
| Exempt from these rules | NBFCs, housing finance companies, banking and insurance companies | "Provided further that non-banking financial companies, housing finance companies and companies engaged in the business of banking and insurance sector are exempted from filing of financial statements under these rules" | https://resource.cdn.icai.org/74737bos60488-m2-cp9.pdf |

| Item | Value | Note | Source |
| --- | --- | --- | --- |
| Filing period for the annual return (section 92(4)) | sixty days | "every company shall file with the Registrar a copy of the annual return, within sixty days from the date on which the annual general meeting is held or where no annual general meeting is held in any year within sixty days from the date on which the annual general meeting should have been held together with the statement specifying the reasons for not holding the annual general meeting" | https://resource.cdn.icai.org/74735bos60488-m2-cp7.pdf |

### CARO 2020: private company exclusion, all three tests

| Item | Value | Note | Source |
| --- | --- | --- | --- |
| Paid-up capital plus reserves and surplus on the balance sheet date, not more than | one crore rupees | "having a paid-up capital and reserves and surplus not more than one crore rupees as on the balance sheet date" | https://resource.cdn.icai.org/60117aasb48979-a.pdf |
| Borrowings from any bank or financial institution, at no point in the financial year more than | one crore rupees | "which does not have total borrowings exceeding one crore rupees from any bank or financial institution at any point of time" | https://resource.cdn.icai.org/60117aasb48979-a.pdf |
| Total revenue as disclosed in Schedule III (including discontinuing operations), not more than | ten crore rupees | "exceeding ten crore rupees during the financial year as per the financial statements" | https://resource.cdn.icai.org/60117aasb48979-a.pdf |

### Surcharge, cess and AGM timing

| Item | Rate or period | Condition | Source |
| --- | --- | --- | --- |
| Surcharge, domestic company not under s 200 or 201, total income over 1 crore to 10 crore | 7% | Finance Act 2026 First Schedule Part I-B Paragraph F | https://egazette.gov.in/WriteReadData/2026/271439.pdf |
| Surcharge, same, total income over 10 crore | 12% | Same | https://egazette.gov.in/WriteReadData/2026/271439.pdf |
| Surcharge, domestic company under s 200 or 201 | 10% | Finance Act 2026 s 3(4)(b) Table Sl. No. 9 | https://egazette.gov.in/WriteReadData/2026/271439.pdf |
| Health and Education Cess | 4% of tax plus surcharge | All companies | https://egazette.gov.in/WriteReadData/2026/271439.pdf |
| AGM, every company except an OPC (section 96(1)) | Within 6 months from the close of the financial year; first AGM within 9 months of the close of the first financial year; gap between AGMs not more than 15 months | Registrar may extend for a special reason | https://resource.cdn.icai.org/74735bos60488-m2-cp7.pdf |
| OPC financial statements filing (section 137(1) proviso) | Within 180 days from the close of the financial year | OPC need not hold an AGM | https://resource.cdn.icai.org/74737bos60488-m2-cp9.pdf |

## The base

### Required financial statements (section 2(40))

Section 2(40) lists what "financial statement" includes, as reproduced in ICAI study material (https://resource.cdn.icai.org/74737bos60488-m2-cp9.pdf ):

1. a balance sheet as at the end of the financial year;
2. a profit and loss account (or an income and expenditure account for a not-for-profit company);
3. a cash flow statement; section 2(40) of the Companies Act 2013 and exemption notification G.S.R. 583(E) of 13 June 2017 let some companies omit it, and no allowed page reproduces either as rule text, so check both before omitting it;
4. a statement of changes in equity, if applicable (Ind AS companies);
5. explanatory notes forming part of any of these.

| Document | Who prepares it | Notes |
| --- | --- | --- |
| Balance sheet | Every company | Schedule III, Part I of the relevant Division |
| Statement of profit and loss | Every company | Schedule III, Part II of the relevant Division |
| Statement of changes in equity | Ind AS companies | Division II and Division III |
| Cash flow statement | Every company except those excepted by section 2(40) and G.S.R. 583(E) | See item 3 |
| Notes | Every company | Accounting policies and the Schedule III disclosures |
| Board's report (section 134) | Every company | For an OPC or small company, check section 134(3A) and rule 8A on the abridged form |
| Auditor's report | Every company | Section 134 attaches it to every financial statement |
| Consolidated financial statements (section 129(3)) | A company with one or more subsidiaries or associate companies | Prepared for the company and all subsidiaries, associates and joint ventures, laid before the AGM with the standalone statements; Form AOC-1 sets out the salient features of each subsidiary, associate and joint venture (rule 5) |

### What small company or OPC status changes

A small company is a company, other than a public company, that meets BOTH limits: paid-up share capital not more than the first amount in the rates table, AND turnover (as per the profit and loss account for the immediately preceding financial year) not more than the second amount there. The section sets a ceiling; the actual limits are in rule 2(1)(t) of the Companies (Specification of definition details) Rules, 2014, substituted by G.S.R. 880(E) of 1 December 2025, in force from its publication that day.

Excluded from small company status whatever their size (section 2(85) proviso, reproduced in the CARO 2020 Guidance Note, https://resource.cdn.icai.org/60117aasb48979-a.pdf ): a public company; a holding company or a subsidiary company; a company registered under section 8; a company or body corporate governed by any special Act. A company that fails either limit, or falls in an excluded class, is not a small company.

**Pending, not law.** The Corporate Laws (Amendment) Bill, 2026 (Bill No. 85 of 2026, introduced in the Lok Sabha on 23 March 2026, https://egazette.gov.in/WriteReadData/2026/271201.pdf ) would raise the section 2(85) ceilings and change the section 403 additional fee. It has not been enacted. Apply the limits in the rates table until an amending Act and new rules are notified.

| Relief | Small company | OPC | Where |
| --- | --- | --- | --- |
| Cash flow statement | Check section 2(40) and G.S.R. 583(E) | Check section 2(40) and G.S.R. 583(E) | Section 2(40) and exemption notification G.S.R. 583(E) of 13 June 2017  |
| CARO (2020) does not apply | Yes | Yes | CARO (2020) paragraph 1(2)(iv) (see Penalties and interest: audit) |
| Auditor rotation under section 139(2) does not apply | Check rule 5 | Check rule 5 | Section 139(2) read with rule 5 (see Penalties and interest: audit) |
| Auditor's report on internal financial controls not required | Check the exemption notification | Check the exemption notification | Section 143(3)(i) exemption (see Penalties and interest: audit) |
| Abridged Board's report | Check section 134(3A) and rule 8A | Check section 134(3A) and rule 8A | Section 134(3A) and rule 8A of the Companies (Accounts) Rules, 2014 |
| Annual return in Form MGT-7A instead of MGT-7 | Yes | Yes | Rule 11 of the Companies (Management and Administration) Rules, 2014 (see Deadlines and filing) |
| Statutory audit | Still required | Still required | Section 134 and section 139 (see Penalties and interest: audit) |

### Year-end adjustments checklist

| # | Adjustment | India-specific notes |
| --- | --- | --- |
| 1 | Depreciation | Schedule II to the Companies Act prescribes useful lives; component accounting applies under Ind AS 16 |
| 2 | Provisions and contingencies | Ind AS 37 / AS 29: present obligation, probable outflow, reliable estimate |
| 3 | Employee benefits | Ind AS 19 / AS 15; gratuity and leave encashment need an actuarial valuation for defined benefit plans |
| 4 | Credit losses on receivables | Ind AS 109 expected credit loss model for Ind AS companies. AS companies do not apply Ind AS 109; follow the company's accounting policy for doubtful debts. AS 4 is not the receivables standard: it covers contingencies and events occurring after the balance sheet date |
| 5 | Inventory | Ind AS 2 / AS 2: lower of cost and net realisable value; FIFO or weighted average cost |
| 6 | Deferred tax | Ind AS 12 / AS 22. Measure with the income-tax rates for the year in the rates table; do not use a single blended rate |
| 7 | Foreign exchange | Ind AS 21 / AS 11: monetary items at the closing rate |
| 8 | Leases | Ind AS 116 (right-of-use model); AS 19 (finance and operating leases) |
| 9 | Revenue | Ind AS 115 (five-step model); AS 9 |
| 10 | Government grants | Ind AS 20 / AS 12 |
| 11 | Gratuity | From 21 November 2025 gratuity is governed by Chapter V of the Code on Social Security, 2020 (commencement notification S.O. 5319(E), https://egazette.gov.in/WriteReadData/2025/267882.pdf ); section 164(1) of the Code repeals the Payment of Gratuity Act, 1972 (https://egazette.gov.in/WriteReadData/2020/222111.pdf ). See `india-payroll` |
| 12 | CSR | Section 135: check the section 135(1) tests in the Act; provide for or disclose unspent amounts under section 135 and the CSR Rules |

**Company income-tax rates for deferred tax (tax year 2026-27, Finance Act, 2026)**

These are base rates under the Income-tax Act, 2025, before surcharge and health and education cess. The lower rate is a cliff: a company above the turnover test pays the other rate on all its income.

**Concessional regimes (Income-tax Act, 2025)**

Section 200 and section 201 are the 2025 Act sections for these options; the section numbers changed from the 1961 Act. Which regime a company is in, and whether its MAT credit can still be used, decides the deferred tax rate. See `india-tax-optimization` for the choice of regime.

### Statement of profit and loss format

Schedule III has three Divisions: Division I for companies following the Companies (Accounting Standards) Rules, Division II for companies following the Companies (Indian Accounting Standards) Rules, and Division III for NBFCs that apply Ind AS. The outline below follows the line items of Part II. It is an outline, not the Schedule text: no allowed page we read prints Schedule III, so check every caption against the Schedule before you finalise.

~~~
I.    Revenue from operations
II.   Other income
III.  Total income (I + II)
IV.   Expenses:
      Cost of materials consumed
      Purchases of stock-in-trade
      Changes in inventories of finished goods, work-in-progress and stock-in-trade
      Employee benefits expense
      Finance costs
      Depreciation and amortisation expense
      Other expenses
V.    Total expenses
VI.   Profit before exceptional items and tax (III - V)
VII.  Exceptional items
VIII. Profit before tax
IX.   Tax expense: current tax; deferred tax
X.    Profit for the period
XI.   Other comprehensive income (Division II and III only):
      items that will not be reclassified to profit or loss
      items that will be reclassified to profit or loss
XII.  Total comprehensive income (Division II and III only)
~~~

The captions differ between the Divisions. Check each line in the Schedule for the Division that applies.

### Balance sheet format

Outline of Schedule III, Part I. As for the profit and loss format, check every caption against the Schedule text.

~~~
Division I (AS companies)

EQUITY AND LIABILITIES
  Shareholders' funds: share capital; reserves and surplus;
    money received against share warrants
  Share application money pending allotment
  Non-current liabilities: long-term borrowings; deferred tax
    liabilities (net); other long-term liabilities; long-term provisions
  Current liabilities: short-term borrowings; trade payables
    (micro and small enterprises, and others); other current
    liabilities; short-term provisions
  TOTAL

ASSETS
  Non-current assets: property, plant and equipment and intangible
    assets (with capital work-in-progress and intangible assets
    under development); non-current investments; deferred tax
    assets (net); long-term loans and advances; other non-current assets
  Current assets: current investments; inventories; trade
    receivables; cash and cash equivalents; short-term loans and
    advances; other current assets
  TOTAL
~~~

Division II (Ind AS companies) uses a different order and presents equity separately, with a statement of changes in equity. Check the Division II captions in the Schedule.

### Notes to financial statements

| # | Disclosure | AS companies | Ind AS companies |
| --- | --- | --- | --- |
| 1 | Significant accounting policies | AS 1 | Ind AS 1 and Ind AS 8 |
| 2 | Property, plant and equipment | Schedule III | Ind AS 16 |
| 3 | Share capital details | Required | Required |
| 4 | Borrowings (terms, security) | Required | Required |
| 5 | Trade payables (dues to micro and small enterprises) | Required (MSMED Act) | Required (MSMED Act) |
| 6 | Related party transactions | AS 18 | Ind AS 24 |
| 7 | Contingent liabilities and commitments | AS 29 | Ind AS 37 |
| 8 | Employee benefits | AS 15 | Ind AS 19 |
| 9 | Deferred tax | AS 22 | Ind AS 12 |
| 10 | Revenue | AS 9 | Ind AS 115 (including disaggregation) |
| 11 | Financial instruments | No equivalent standard | Ind AS 107 |
| 12 | Earnings per share | AS 20 (check which companies it covers in the Companies (Accounting Standards) Rules, 2021) | Ind AS 33 |
| 13 | Segment reporting | AS 17 (check which companies it covers in the 2021 Rules) | Ind AS 108 |
| 14 | CSR spending | Where section 135 applies | Where section 135 applies |

## Deadlines and filing

### Filing with the Registrar (section 137)

The financial statements adopted at the AGM are filed with the Registrar under section 137. If they are not adopted at the AGM (or an adjourned AGM), the unadopted statements are filed within the same period and the statements adopted at the adjourned AGM within thirty days of that adjourned AGM. A company with subsidiaries files the consolidated statements too.

A One Person Company, which need not hold an AGM, files the financial statements duly adopted by its member within one hundred eighty days from the close of the financial year (section 137(1) proviso, as reproduced in the ICAI chapter on accounts of companies).

Section 137(3) sets a penalty on the company and on the officers responsible when the statements are filed late. No allowed page reproduces the sub-section, so the amounts are not stated here.

Section 135(1) sets net worth, turnover and net profit tests for a CSR committee and a minimum CSR spend. No allowed page reproduces the section, so the tests are not stated here.

Once a company has started filing in XBRL it must keep filing in XBRL in later years, even if it no longer meets a test in the rates table. An NBFC that applies Ind AS files Form AOC-4 NBFC (Ind AS), and its consolidated statements in AOC-4 CFS NBFC (Ind AS). A company covered by section 135(1) files its CSR report in Form CSR-2 as an addendum to Form AOC-4, AOC-4 XBRL or AOC-4 NBFC (Ind AS) (rule 12(1B) of the Companies (Accounts) Rules, 2014).

**Annual return.** Separately from the financial statements, the annual return under section 92 is filed in Form MGT-7 (MGT-7A for an OPC or small company).

**AGM date (section 96).** Every company except an OPC holds its AGM within six months of the close of the financial year, the first AGM within nine months of the close of the first financial year, with no more than fifteen months between two AGMs (ICAI chapter on Management and Administration). For the financial year ending 31 March 2027 the AGM is due by 30 September 2027, and the financial statements by thirty days after it. Check whether the Registrar granted an extension before counting the filing periods.

**Additional fee for late filing (section 403).** Section 403(1) lets a document be filed late on payment of an additional fee. The current first proviso sets that fee at not less than one hundred rupees per day (the wording the 2026 Bill proposes to replace; https://egazette.gov.in/WriteReadData/2026/271201.pdf ). The actual additional fee table is in the Companies (Registration Offices and Fees) Rules, 2014, which no allowed page prints. Check the fee on the MCA portal for each form. The section 403 additional fee is separate from the section 137(3) penalty.

## Penalties and interest

Section 137(3) penalty and the section 403 additional fee are described under Deadlines and filing; no allowed page prints the amounts except the section 403 first proviso floor of one hundred rupees per day.

### Audit: statutory audit (sections 134 and 139 to 148)

Every company, including a small company and an OPC, has its financial statements audited. Section 134 attaches the auditor's report to every financial statement, and section 139 requires every company to appoint an individual or a firm as auditor at its first AGM, holding office until the conclusion of the sixth AGM after that (ICAI chapter on audit and auditors, https://resource.cdn.icai.org/74738bos60488-m2-cp10.pdf ). The Board appoints the first auditor within thirty days of registration.

**Pending, not law:** the 2026 Bill would add section 139(12), letting the government exempt prescribed classes of companies from appointing auditors. Until it is enacted and the classes are prescribed, no size-based audit exemption exists.

### Audit: CARO (2020)

The auditor of a company covered by the Companies (Auditor's Report) Order, 2020 adds the CARO matters (paragraphs 3 and 4) to the section 143 report, for financial years commencing on or after 1 April 2019. CARO does not apply to the report on consolidated financial statements, except its clause (xxi). It applies to every company, including a foreign company, EXCEPT:

1. a banking company;
2. an insurance company;
3. a company licensed under section 8;
4. a One Person Company and a small company;
5. a private limited company, not a subsidiary or holding company of a public company, that meets ALL THREE tests in the rates table.

Failing one test means CARO applies. A small company stays outside CARO even if it fails the private company tests. Status is judged at the balance sheet date. Since 1 December 2025 the small company exclusion follows the new section 2(85) limits in the rates table.

### Audit: auditor rotation (section 139(2) and rule 5)

Section 139(2) limits how long one individual or one firm may audit a listed company or a company of a class prescribed by rule 5 of the Companies (Audit and Auditors) Rules, 2014. No allowed page reproduces section 139(2) or rule 5, so this skill does not state the classes, the capital or borrowing tests or the term limits. Read both before advising.

### Audit: internal financial controls report (section 143(3)(i))

An exemption notification under the Act relieves some private companies of this report, on turnover, borrowing and no-default conditions. No allowed page reproduces the notification, so this skill does not state the conditions. Read it before relying on the relief.

### Audit: internal audit (section 138 and rule 13)

Every test looks at the PRECEDING financial year. Meeting any ONE test is enough.

| Company | Must appoint an internal auditor if, in the preceding financial year, it had |
| --- | --- |
| Listed company | Always |
| Unlisted public company | Paid-up share capital of fifty crore rupees or more; OR turnover of two hundred crore rupees or more; OR outstanding loans or borrowings from banks or public financial institutions exceeding one hundred crore rupees at any point; OR outstanding deposits of twenty-five crore rupees or more at any point |
| Private company | Turnover of two hundred crore rupees or more; OR outstanding loans or borrowings from banks or public financial institutions exceeding one hundred crore rupees at any point |

Source: ICAI chapter on accounts of companies, https://resource.cdn.icai.org/74737bos60488-m2-cp9.pdf . The internal auditor is a chartered accountant or a cost accountant (in practice or not), or such other professional as the Board decides, and may be an employee. The audit committee or the Board sets the scope, frequency and method in consultation with the internal auditor.

## Cross-border points

- A foreign company is within CARO 2020 (see the audit rules above); the CARO exclusions do not take a foreign company out.
- A company listed abroad counts as listed for the Ind AS roadmap.
- Foreign currency monetary items are translated at the closing rate (Ind AS 21 / AS 11).
- A foreign holding or subsidiary that applies Ind AS can bring an Indian group company into Ind AS through the group rule; IFRS use abroad alone does not.
- Related-party pricing with foreign group companies: `india-transfer-pricing`.

## Two worked examples that recompute

### Example 1: Is the company a small company for FY 2026-27?

A private company (not a holding or subsidiary, not section 8) has paid-up share capital of 8 crore rupees at 31 March 2027 and turnover of 120 crore rupees in the preceding financial year (2025-26). The capital limit leaves 2 crore of headroom, but turnover is 20 crore over the 100 crore limit. Both limits must be met, so the company is NOT a small company: CARO 2020 applies unless it meets all three private company tests (it does not: revenue is far above ten crore rupees), it files Form MGT-7, not MGT-7A, and, with turnover of 100 crore rupees or more, it files in AOC-4 XBRL.

```oa-check
name: Small company test, capital 8 crore, preceding-year turnover 120 crore
inputs:
  paid_up: 80000000
  turnover: 1200000000
steps:
  - capital_headroom: 100000000 - paid_up
  - turnover_headroom: 1000000000 - turnover
  - weakest_headroom: min(capital_headroom, turnover_headroom)
  - xbrl_turnover_margin: turnover - 1000000000
expected:
  capital_headroom: 20000000
  turnover_headroom: -200000000
  weakest_headroom: -200000000
  xbrl_turnover_margin: 200000000
```

A negative weakest headroom means the company fails a limit. An XBRL margin of zero or more means the turnover test for XBRL is met (100 crore "or above").

### Example 2: Deferred tax rate, stay in the default regime or opt for section 200

A domestic company with 2024-25 turnover of 350 crore rupees expects total income of 5 crore rupees a year and has a net taxable temporary difference of 10 crore rupees at 31 March 2027. On the default regime it pays 25% (turnover not over 400 crore), plus 7% surcharge (income over 1 crore, not over 10 crore), plus 4% cess: 27.82%, so the deferred tax liability is 2,78,20,000 rupees. If it has opted for section 200 (22%, 10% surcharge, 4% cess: 25.168%), the liability is 2,51,68,000 rupees. The rate the company will pay when the difference reverses decides which to use; the regime choice itself (MAT credit, lost deductions) is in `india-tax-optimization`.

```oa-check
name: Deferred tax on a 10 crore temporary difference, default regime against section 200
inputs:
  temp_diff: 100000000
steps:
  - default_rate: 0.25 * 1.07 * 1.04
  - s200_rate: 0.22 * 1.10 * 1.04
  - dtl_default: temp_diff * default_rate
  - dtl_s200: temp_diff * s200_rate
  - difference: dtl_default - dtl_s200
expected:
  default_rate: 0.2782
  s200_rate: 0.25168
  dtl_default: 27820000
  dtl_s200: 25168000
  difference: 2652000
```

## Ask the client first

- Are any of the company's shares or debt securities listed or being listed, in India or abroad, and is that on a main board or an SME exchange?
- What were the company's paid-up share capital and net worth at the balance sheet date, and its turnover in the preceding financial year?
- Is the company a holding, subsidiary, associate or joint venture of another company, and does that company apply Ind AS?
- Has the company ever prepared Ind AS statements or filed in XBRL, voluntarily or otherwise?
- What were its borrowings from banks or financial institutions, and its public deposits, at their highest point in the year?
- Has it missed any financial statement or annual return filing in earlier years? Check whether any exemption you rely on is lost by a filing default.

### The method, step by step

1. Fix the financial year under section 2(41) of the Companies Act, 2013 (ending 31 March) and the status of the company on the balance sheet date: listed or unlisted, public or private, OPC, section 8, NBFC, bank or insurer, holding or subsidiary (https://resource.cdn.icai.org/74737bos60488-m2-cp9.pdf ).
2. Choose the framework with the Companies (Indian Accounting Standards) Rules, 2015 tests (rates table): net worth, listing, group membership, earlier voluntary adoption (https://resource.cdn.icai.org/87811bos-280825-final-ch1.pdf ). This also picks Division I, II or III of Schedule III.
3. Test small company status under section 2(85) and rule 2(1)(t) as substituted by G.S.R. 880(E): paid-up capital AND preceding-year turnover, and the excluded classes (https://egazette.gov.in/WriteReadData/2025/268124.pdf and https://resource.cdn.icai.org/60117aasb48979-a.pdf ).
4. List the statements required under section 2(40) and section 129(3): cash flow exemption, statement of changes in equity, consolidated statements and Form AOC-1 (https://resource.cdn.icai.org/74737bos60488-m2-cp9.pdf ).
5. Post the year-end adjustments in The base, including deferred tax at the rates for tax year 2026-27 under the Finance Act, 2026 and the Income-tax Act, 2025 (https://egazette.gov.in/WriteReadData/2026/271439.pdf and https://egazette.gov.in/WriteReadData/2025/265620.pdf ).
6. Prepare the statements and notes in the Schedule III format for the Division chosen in step 2 (Divisions described at https://resource.cdn.icai.org/74737bos60488-m2-cp9.pdf ), and check each caption against the Schedule text.
7. Confirm the audit set-up: auditor appointment and rotation under section 139 and rule 5, CARO 2020 applicability, the internal financial controls report, and internal audit under section 138 and rule 13 (https://resource.cdn.icai.org/74738bos60488-m2-cp10.pdf and https://resource.cdn.icai.org/60117aasb48979-a.pdf and https://resource.cdn.icai.org/74737bos60488-m2-cp9.pdf ).
8. Board approval and signature under section 134, then the auditor's report, then the Board's report (for an OPC or small company, check section 134(3A) and rule 8A on the abridged form) (https://resource.cdn.icai.org/74737bos60488-m2-cp9.pdf ).
9. Hold the AGM within the section 96 period (check the section text and any extension) and lay the standalone and consolidated statements before it under section 129(2) and 129(3) (https://resource.cdn.icai.org/74737bos60488-m2-cp9.pdf ).
10. File under section 137 in the right form (AOC-4, AOC-4 XBRL, AOC-4 NBFC (Ind AS), with the CFS version and CSR-2 where needed) within the period in the rates table, then the annual return under section 92 in MGT-7 or MGT-7A (https://resource.cdn.icai.org/74737bos60488-m2-cp9.pdf and https://resource.cdn.icai.org/74735bos60488-m2-cp7.pdf ).

### When to refuse or refer

- Banking companies, insurance companies and electricity companies: refer.
- NBFCs applying Ind AS (Division III and the NBFC roadmap): refer to an accountant with NBFC experience.
- First-time adoption of Ind AS (Ind AS 101 transition): refer.
- Government companies: refer.
- Restatement, reopening or voluntary revision of earlier accounts (sections 130 and 131): refer.
- A company that has missed filings for several years and needs condonation or a compounding application: refer to a company secretary.
- Any question that turns on the Corporate Laws (Amendment) Bill, 2026 or a proposed rule: say it is not law and refer for the position on the filing date.
- Income tax computation, tax audit and the return: outside this skill; see `india-income-tax` for individuals and `india-transfer-pricing` for related-party pricing. Formation and post-incorporation filings: see `india-formation`.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| Read for G.S.R. 880(E) of 1 December 2025, small company limits of ten crore capital and one hundred crore turnover | https://egazette.gov.in/WriteReadData/2025/268124.pdf | 2026-11-14 |
| Read for the Corporate Laws (Amendment) Bill, 2026 (Bill No. 85 of 2026, pending): section 2(85), 139(12) and 403 proposals | https://egazette.gov.in/WriteReadData/2026/271201.pdf | 2026-11-14 |
| Read for Finance Act 2026 First Schedule Part I-B Paragraphs E and F, section 3(4)(b), and the section 206 MAT rate change to 14% | https://egazette.gov.in/WriteReadData/2026/271439.pdf | 2026-11-14 |
| Read for Income-tax Act 2025 sections 200 and 201 (concessional company rates) | https://egazette.gov.in/WriteReadData/2025/265620.pdf | 2026-11-14 |
| Read for Code on Social Security 2020 section 164(1), repeal of the Payment of Gratuity Act | https://egazette.gov.in/WriteReadData/2020/222111.pdf | 2026-11-14 |
| Read for S.O. 5319(E), commencement of the Code on 21 November 2025 | https://egazette.gov.in/WriteReadData/2025/267882.pdf | 2026-11-14 |
| Read for the ICAI Guidance Note on CARO 2020: paragraph 1(2) exclusions, the three private company tests, section 2(62) and 2(85) | https://resource.cdn.icai.org/60117aasb48979-a.pdf | 2026-11-14 |
| Read for ICAI study material, Introduction to Ind AS: rule 4 of the Ind AS Rules (roadmap, net worth tests) | https://resource.cdn.icai.org/87811bos-280825-final-ch1.pdf | 2026-11-14 |
| Read for ICAI study material, Accounts of Companies: sections 2(40), 129, 134, 137 (including the OPC 180-day proviso), 138, XBRL rule 3(1) and rule 12(1B) | https://resource.cdn.icai.org/74737bos60488-m2-cp9.pdf | 2026-11-14 |
| Read for ICAI study material, Management and Administration: section 92(4) sixty-day annual return period and section 96(1) AGM timing | https://resource.cdn.icai.org/74735bos60488-m2-cp7.pdf | 2026-11-14 |
| Read for ICAI study material, Audit and Auditors: sections 139 to 148 | https://resource.cdn.icai.org/74738bos60488-m2-cp10.pdf | 2026-11-14 |

Not yet confirmed: the section 137(3) penalty amounts; the additional fee table in the Companies (Registration Offices and Fees) Rules, 2014; the section 135(1) CSR tests; the cash flow exemption text in section 2(40) and G.S.R. 583(E); the section 139(2) and rule 5 rotation classes and terms; the section 143(3)(i) exemption conditions; the section 134(3A) and rule 8A abridged Board's report; the NBFC Ind AS net worth tests; the Schedule III captions themselves (only described, not read in the Schedule text).

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-14. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `india-financial-statements` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/india-financial-statements. If neither is available, confirm every figure against the official source pages cited above before relying on it.
