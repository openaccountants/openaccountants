---
name: india-financial-statements
description: Use this skill when preparing, reviewing, or advising on annual financial statements for an Indian company. Trigger on phrases like "financial statements India", "MCA filing", "AOC-4", "Schedule III", "Ind AS", "Indian Accounting Standards", "Companies Act 2013", "CARO", "statutory audit India", "ROC filing", "small company India", "OPC", "balance sheet format India", or any question about preparing and filing statutory accounts under the Companies Act 2013. Covers Ind AS/AS frameworks, Schedule III formats, size thresholds, required statements, notes, MCA filing, and audit requirements.
version: 1.0
jurisdiction: IN
tax_year: 2026
last_updated: 2026-10-17
authored_by: Michael Cutajar and the OpenAccountants team
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
depends_on:
  - financial-statements-workflow-base
category: financial-statements
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# India Company Financial Statements: Framework, Formats, Audit and Filing

This Guide covers the annual financial statements of a company under the Indian Companies Act, 2013: which accounting framework applies (Ind AS or the Accounting Standards), which statements to prepare, the small company and One Person Company relaxations, the statutory audit and the CARO Order of 2020, internal audit, and filing with the Registrar of Companies. Figures are for tax year 2026. For Indian income tax this means the tax year from 1 April 2026 to 31 March 2027 under the Income-tax Act, 2025, which replaced the Income-tax Act, 1961 from 1 April 2026. For company law, the Guide states the rules in force on 17 October 2026; they apply to financial statements for the financial year ending 31 March 2027 unless a rule below says otherwise. The Corporate Laws (Amendment) Bill, 2026 is not law (see Section 3).

## Section 1: Quick Reference

| Field | Value |
| --- | --- |
| Country | India (Republic of India) |
| Currency | INR |
| Filing authority | Ministry of Corporate Affairs (MCA), Registrar of Companies (ROC) |
| Primary legislation | Companies Act, 2013, Chapter IX (sections 128 to 138, accounts) and Chapter X (sections 139 to 148, audit) |
| Supporting legislation | Companies (Accounts) Rules, 2014; Companies (Audit and Auditors) Rules, 2014; Companies (Indian Accounting Standards) Rules, 2015; Companies (Accounting Standards) Rules, 2021; Companies (Auditor's Report) Order, 2020, referred to in this Guide as CARO (2020) |
| Accounting standards | Ind AS (converged with IFRS) or the Accounting Standards (AS), by the tests in Section 2 |
| Financial year | Section 2(41): the period ending on 31 March every year (a company incorporated on or after 1 January may run to 31 March of the following year) |
| Statement formats | Schedule III: Division I (AS companies), Division II (Ind AS companies other than NBFCs), Division III (Ind AS NBFCs) |
| Filing form | e-Form AOC-4, AOC-4 XBRL or AOC-4 NBFC (Ind AS); consolidated statements in AOC-4 CFS (or the XBRL or NBFC version) |
| Filing deadline | Within the period after the AGM shown in the Section 9 table |
| AGM | Section 96. The deadline is not stated in this Guide (no allowed official page prints it); see Section 9 |

## Section 2: Reporting Framework

The Companies (Indian Accounting Standards) Rules, 2015 set the Ind AS roadmap. The tests use net worth. Once a company applies Ind AS, voluntarily or because it met a test, it must keep applying Ind AS in all later years even if it no longer meets the test.

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://resource.cdn.icai.org/87811bos-280825-final-ch1.pdf |
| Phase I (accounting periods beginning on or after 1 April 2016): any company, listed or unlisted, with net worth of | rupees five hundred crore or more | "companies other than those covered by sub-clause (a) above and having net worth of rupees five hundred crore or more" |
| Phase II (accounting periods beginning on or after 1 April 2017): every listed company whatever its net worth, and an unlisted company with net worth of | rupees two hundred and fifty crore or more | "having net worth of rupees two hundred and fifty crore or more but less than rupees five hundred crore" |
| Group rule | Holding, subsidiary, joint venture and associate companies of a company covered above also apply Ind AS | "holding, subsidiary, joint venture or associate companies of companies covered by sub- clause (a) and sub-clause (b)" |
| SME exchange | The roadmap does not apply to a company whose securities are listed (or being listed) on an SME exchange | "the roadmap shall not be applicable to companies whose securities are listed or are in the process of being listed on SME exchange" |
| Once in, always in | Ind AS continues in later years | "it shall be required to follow the Indian Accounting Standards (Ind AS) for all the subsequent financial statements" |

**Which framework applies**

| Entity type | Framework |
| --- | --- |
| Listed company (main board, India or abroad) | Ind AS (Phase I or Phase II) |
| Unlisted company with net worth at or above the Phase II amount in the table above | Ind AS |
| Holding, subsidiary, joint venture or associate of an Ind AS company | Ind AS |
| Company listed only on an SME exchange | AS, unless it opts into Ind AS |
| Any other company, including most small companies and One Person Companies | AS (Companies (Accounting Standards) Rules, 2021), unless it opts into Ind AS |
| NBFC | A separate NBFC roadmap in the same Rules, from accounting periods beginning on or after 1 April 2018 (first phase) or 1 April 2019 (second phase); check the NBFC net worth tests in the Rules |
| Banking company, insurance company | Not covered by this Guide. Refer (see the refusal list) |

## Section 3: Size Thresholds

### Small company (section 2(85))

A small company is a company, other than a public company, that meets BOTH limits: paid-up share capital not more than the first amount below, AND turnover (as per the profit and loss account for the immediately preceding financial year) not more than the second. The section sets a ceiling; the actual limits are in rule 2(1)(t) of the Companies (Specification of definition details) Rules, 2014, substituted by G.S.R. 880(E) of 1 December 2025, in force from its publication that day.

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://egazette.gov.in/WriteReadData/2025/268124.pdf |
| Paid-up share capital, not more than | rupees ten crores | "paid up capital and turnover of the small company shall not exceed rupees ten crores and rupees one hundred crores respectively" |
| Turnover, not more than | rupees one hundred crores | "paid up capital and turnover of the small company shall not exceed rupees ten crores and rupees one hundred crores respectively" |

Excluded from small company status whatever their size (section 2(85) proviso, reproduced in the CARO 2020 Guidance Note, https://resource.cdn.icai.org/60117aasb48979-a.pdf ): a public company; a holding company or a subsidiary company; a company registered under section 8; a company or body corporate governed by any special Act. A company that fails either limit, or falls in an excluded class, is not a small company.

**Pending, not law.** The Corporate Laws (Amendment) Bill, 2026 (Bill No. 85 of 2026, introduced in the Lok Sabha on 23 March 2026, https://egazette.gov.in/WriteReadData/2026/271201.pdf ) would raise the section 2(85) ceilings and change the section 403 additional fee. It has not been enacted. Apply the limits in the table above until an amending Act and new rules are notified.

### One Person Company (section 2(62))

Section 2(62) defines a One Person Company as "a company which has only one person as a member" (CARO 2020 Guidance Note, https://resource.cdn.icai.org/60117aasb48979-a.pdf ). The definition carries no capital or turnover limit.

### What small company or OPC status changes

| Relief | Small company | OPC | Where |
| --- | --- | --- | --- |
| Cash flow statement | Check section 2(40) and G.S.R. 583(E) | Check section 2(40) and G.S.R. 583(E) | Section 2(40) and exemption notification G.S.R. 583(E) of 13 June 2017 (Section 4) |
| CARO (2020) does not apply | Yes | Yes | CARO (2020) paragraph 1(2)(iv) (Section 10) |
| Auditor rotation under section 139(2) does not apply | Check rule 5 | Check rule 5 | Section 139(2) read with rule 5 (Section 10) |
| Auditor's report on internal financial controls not required | Check the exemption notification | Check the exemption notification | Section 143(3)(i) exemption (Section 10) |
| Abridged Board's report | Check section 134(3A) and rule 8A | Check section 134(3A) and rule 8A | Section 134(3A) and rule 8A of the Companies (Accounts) Rules, 2014 |
| Annual return in Form MGT-7A instead of MGT-7 | Yes | Yes | Rule 11 of the Companies (Management and Administration) Rules, 2014 (Section 9) |
| Statutory audit | Still required | Still required | Section 134 and section 139 (Section 10) |

## Section 4: Required Financial Statements

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

## Section 5: Year-End Adjustments Checklist

| # | Adjustment | India-specific notes |
| --- | --- | --- |
| 1 | Depreciation | Schedule II to the Companies Act prescribes useful lives; component accounting applies under Ind AS 16 |
| 2 | Provisions and contingencies | Ind AS 37 / AS 29: present obligation, probable outflow, reliable estimate |
| 3 | Employee benefits | Ind AS 19 / AS 15; gratuity and leave encashment need an actuarial valuation for defined benefit plans |
| 4 | Credit losses on receivables | Ind AS 109 expected credit loss model for Ind AS companies. AS companies do not apply Ind AS 109; follow the company's accounting policy for doubtful debts. AS 4 is not the receivables standard: it covers contingencies and events occurring after the balance sheet date |
| 5 | Inventory | Ind AS 2 / AS 2: lower of cost and net realisable value; FIFO or weighted average cost |
| 6 | Deferred tax | Ind AS 12 / AS 22. Measure with the income-tax rates for the year in the tables below; do not use a single blended rate |
| 7 | Foreign exchange | Ind AS 21 / AS 11: monetary items at the closing rate |
| 8 | Leases | Ind AS 116 (right-of-use model); AS 19 (finance and operating leases) |
| 9 | Revenue | Ind AS 115 (five-step model); AS 9 |
| 10 | Government grants | Ind AS 20 / AS 12 |
| 11 | Gratuity | From 21 November 2025 gratuity is governed by Chapter V of the Code on Social Security, 2020 (commencement notification S.O. 5319(E), https://egazette.gov.in/WriteReadData/2025/267882.pdf ); section 164(1) of the Code repeals the Payment of Gratuity Act, 1972 (https://egazette.gov.in/WriteReadData/2020/222111.pdf ). See `india-payroll` |
| 12 | CSR | Section 135: check the section 135(1) tests in the Act; provide for or disclose unspent amounts under section 135 and the CSR Rules |

**Company income-tax rates for deferred tax (tax year 2026-27, Finance Act, 2026)**

These are base rates under the Income-tax Act, 2025, before surcharge and health and education cess. The lower rate is a cliff: a company above the turnover test pays the other rate on all its income.

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://egazette.gov.in/WriteReadData/2026/271439.pdf |
| Domestic company whose total turnover or gross receipt in tax year 2024-25 did not exceed INR 400 crore | 25% | "where its total turnover or the 25% of the total gross receipt in the tax year 2024-25 income; does not exceed ₹ 400 crores" |
| Turnover test for the lower rate (tax year 2024-25 figures) | INR 400 crore | "where its total turnover or the 25% of the total gross receipt in the tax year 2024-25 income; does not exceed ₹ 400 crores" |
| Any other domestic company not opting under section 200 or 201 | 30% | "does not exceed ₹ 400 crores; (ii) other than that referred to in 30% of the total item (i) income" |
| Minimum alternate tax on book profit, section 206 (substituted for the old rate from 1 April 2026) | 14% | "for the figures and symbol “15%”, the figures and symbol “14%” shall be substituted" |

**Concessional regimes (Income-tax Act, 2025)**

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Section 200 rate, at the option of a domestic company, on income computed without the listed deductions | 22% | "the income-tax payable for a tax year shall be at the rate of 22%, at the option of a person being a domestic company" |
| Section 201 rate for a domestic company in manufacture or production that opts in, was set up and registered on or after 1 October 2019 and commenced manufacturing or production on or before 31 March 2024, on income other than the specified items | 15% | "1. A (a) 15% on the total Such domestic company" |

Section 200 and section 201 are the 2025 Act sections for these options; the section numbers changed from the 1961 Act. Which regime a company is in, and whether its MAT credit can still be used, decides the deferred tax rate. See `india-tax-optimization` for the choice of regime.

## Section 6: Statement of Profit and Loss Format

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

## Section 7: Balance Sheet Format

Outline of Schedule III, Part I. As in Section 6, check every caption against the Schedule text.

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

## Section 8: Notes to Financial Statements

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

## Section 9: Filing Requirements

The financial statements adopted at the AGM are filed with the Registrar under section 137. If they are not adopted at the AGM (or an adjourned AGM), the unadopted statements are filed within the same period and the statements adopted at the adjourned AGM within thirty days of that adjourned AGM. A company with subsidiaries files the consolidated statements too.

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://resource.cdn.icai.org/74737bos60488-m2-cp9.pdf |
| Filing period for financial statements (section 137(1)) | thirty days | "shall be filed with the Registrar within thirty days of the date of annual general meeting in such manner, with such fees or additional fees as may be prescribed" |
| XBRL filing (Form AOC-4 XBRL), rule 3(1) of the XBRL Rules, 2015: listed companies and their Indian subsidiaries, and any company with paid-up capital of | five crore rupees or above | "(ii) Companies having paid up capital of five crore rupees or above" |
| XBRL filing: any company with turnover of | one hundred crore rupees or above | "(iii) companies having turnover of one hundred crore rupees or above" |
| XBRL filing: every company that must prepare Ind AS statements, other than the classes exempted below | Ind AS companies | "(iv) All companies which are required to prepare their financial statements in accordance with Companies (Indian Accounting Standards) Rules, 2015" |
| Exempt from these rules | NBFCs, housing finance companies, banking and insurance companies | "Provided further that non-banking financial companies, housing finance companies and companies engaged in the business of banking and insurance sector are exempted from filing of financial statements under these rules" |

For a One Person Company, a proviso to section 137(1) sets a different filing period, which no allowed page reproduces as rule text; check it before advising an OPC.

Section 137(3) sets a penalty on the company and on the officers responsible when the statements are filed late. No allowed page reproduces the sub-section, so the amounts are not stated here.

Section 135(1) sets net worth, turnover and net profit tests for a CSR committee and a minimum CSR spend. No allowed page reproduces the section, so the tests are not stated here.

Once a company has started filing in XBRL it must keep filing in XBRL in later years, even if it no longer meets a test above. An NBFC that applies Ind AS files Form AOC-4 NBFC (Ind AS), and its consolidated statements in AOC-4 CFS NBFC (Ind AS). A company covered by section 135(1) files its CSR report in Form CSR-2 as an addendum to Form AOC-4, AOC-4 XBRL or AOC-4 NBFC (Ind AS) (rule 12(1B) of the Companies (Accounts) Rules, 2014).

**Annual return.** Separately from the financial statements, the annual return under section 92 is filed in Form MGT-7 (MGT-7A for an OPC or small company).

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://resource.cdn.icai.org/74735bos60488-m2-cp7.pdf |
| Filing period for the annual return (section 92(4)) | sixty days | "every company shall file with the Registrar a copy of the annual return, within sixty days from the date on which the annual general meeting is held or where no annual general meeting is held in any year within sixty days from the date on which the annual general meeting should have been held together with the statement specifying the reasons for not holding the annual general meeting" |

**AGM date (section 96).** No allowed official page prints the text of section 96, so this Guide does not state the AGM deadline, the first-AGM rule or the Registrar's power to extend. Read section 96 of the Companies Act, 2013 on the MCA website before you count the filing periods above, and check whether the Registrar granted an extension.

**Additional fee for late filing (section 403).** Section 403(1) lets a document be filed late on payment of an additional fee. The current first proviso sets that fee at not less than one hundred rupees per day (the wording the 2026 Bill proposes to replace; https://egazette.gov.in/WriteReadData/2026/271201.pdf ). The actual additional fee table is in the Companies (Registration Offices and Fees) Rules, 2014, which no allowed page prints. Check the fee on the MCA portal for each form. The section 403 additional fee is separate from the section 137(3) penalty.

## Section 10: Audit Requirements

### Statutory audit (sections 134 and 139 to 148)

Every company, including a small company and an OPC, has its financial statements audited. Section 134 attaches the auditor's report to every financial statement, and section 139 requires every company to appoint an individual or a firm as auditor at its first AGM, holding office until the conclusion of the sixth AGM after that (ICAI chapter on audit and auditors, https://resource.cdn.icai.org/74738bos60488-m2-cp10.pdf ). The Board appoints the first auditor within thirty days of registration.

**Pending, not law:** the 2026 Bill would add section 139(12), letting the government exempt prescribed classes of companies from appointing auditors. Until it is enacted and the classes are prescribed, no size-based audit exemption exists.

### CARO (2020)

The auditor of a company covered by the Companies (Auditor's Report) Order, 2020 adds the CARO matters (paragraphs 3 and 4) to the section 143 report, for financial years commencing on or after 1 April 2019. CARO does not apply to the report on consolidated financial statements, except its clause (xxi). It applies to every company, including a foreign company, EXCEPT:

1. a banking company;
2. an insurance company;
3. a company licensed under section 8;
4. a One Person Company and a small company;
5. a private limited company, not a subsidiary or holding company of a public company, that meets ALL THREE tests in the table below.

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://resource.cdn.icai.org/60117aasb48979-a.pdf |
| Paid-up capital plus reserves and surplus on the balance sheet date, not more than | one crore rupees | "having a paid-up capital and reserves and surplus not more than one crore rupees as on the balance sheet date" |
| Borrowings from any bank or financial institution, at no point in the financial year more than | one crore rupees | "which does not have total borrowings exceeding one crore rupees from any bank or financial institution at any point of time" |
| Total revenue as disclosed in Schedule III (including discontinuing operations), not more than | ten crore rupees | "exceeding ten crore rupees during the financial year as per the financial statements" |

Failing one test means CARO applies. A small company stays outside CARO even if it fails the private company tests. Status is judged at the balance sheet date. Since 1 December 2025 the small company exclusion follows the new section 2(85) limits in Section 3.

### Auditor rotation (section 139(2) and rule 5 of the Companies (Audit and Auditors) Rules, 2014)

Section 139(2) limits how long one individual or one firm may audit a listed company or a company of a class prescribed by rule 5 of the Companies (Audit and Auditors) Rules, 2014. No allowed page reproduces section 139(2) or rule 5, so this Guide does not state the classes, the capital or borrowing tests or the term limits. Read both before advising.

### Internal financial controls report (section 143(3)(i))

An exemption notification under the Act relieves some private companies of this report, on turnover, borrowing and no-default conditions. No allowed page reproduces the notification, so this Guide does not state the conditions. Read it before relying on the relief.

### Internal audit (section 138 and rule 13 of the Companies (Accounts) Rules, 2014)

Every test looks at the PRECEDING financial year. Meeting any ONE test is enough.

| Company | Must appoint an internal auditor if, in the preceding financial year, it had |
| --- | --- |
| Listed company | Always |
| Unlisted public company | Paid-up share capital of fifty crore rupees or more; OR turnover of two hundred crore rupees or more; OR outstanding loans or borrowings from banks or public financial institutions exceeding one hundred crore rupees at any point; OR outstanding deposits of twenty-five crore rupees or more at any point |
| Private company | Turnover of two hundred crore rupees or more; OR outstanding loans or borrowings from banks or public financial institutions exceeding one hundred crore rupees at any point |

Source: ICAI chapter on accounts of companies, https://resource.cdn.icai.org/74737bos60488-m2-cp9.pdf . The internal auditor is a chartered accountant or a cost accountant (in practice or not), or such other professional as the Board decides, and may be an employee. The audit committee or the Board sets the scope, frequency and method in consultation with the internal auditor.

## The method, step by step

1. Fix the financial year under section 2(41) of the Companies Act, 2013 (ending 31 March) and the status of the company on the balance sheet date: listed or unlisted, public or private, OPC, section 8, NBFC, bank or insurer, holding or subsidiary (https://resource.cdn.icai.org/74737bos60488-m2-cp9.pdf ).
2. Choose the framework with the Companies (Indian Accounting Standards) Rules, 2015 tests in Section 2: net worth, listing, group membership, earlier voluntary adoption (https://resource.cdn.icai.org/87811bos-280825-final-ch1.pdf ). This also picks Division I, II or III of Schedule III.
3. Test small company status under section 2(85) and rule 2(1)(t) as substituted by G.S.R. 880(E): paid-up capital AND preceding-year turnover, and the excluded classes (https://egazette.gov.in/WriteReadData/2025/268124.pdf and https://resource.cdn.icai.org/60117aasb48979-a.pdf ).
4. List the statements required under section 2(40) and section 129(3): cash flow exemption, statement of changes in equity, consolidated statements and Form AOC-1 (https://resource.cdn.icai.org/74737bos60488-m2-cp9.pdf ).
5. Post the year-end adjustments in Section 5, including deferred tax at the rates for tax year 2026-27 under the Finance Act, 2026 and the Income-tax Act, 2025 (https://egazette.gov.in/WriteReadData/2026/271439.pdf and https://egazette.gov.in/WriteReadData/2025/265620.pdf ).
6. Prepare the statements and notes in the Schedule III format for the Division chosen in step 2 (Divisions described at https://resource.cdn.icai.org/74737bos60488-m2-cp9.pdf ), and check each caption against the Schedule text.
7. Confirm the audit set-up: auditor appointment and rotation under section 139 and rule 5, CARO 2020 applicability, the internal financial controls report, and internal audit under section 138 and rule 13 (https://resource.cdn.icai.org/74738bos60488-m2-cp10.pdf and https://resource.cdn.icai.org/60117aasb48979-a.pdf and https://resource.cdn.icai.org/74737bos60488-m2-cp9.pdf ).
8. Board approval and signature under section 134, then the auditor's report, then the Board's report (for an OPC or small company, check section 134(3A) and rule 8A on the abridged form) (https://resource.cdn.icai.org/74737bos60488-m2-cp9.pdf ).
9. Hold the AGM within the section 96 period (check the section text and any extension) and lay the standalone and consolidated statements before it under section 129(2) and 129(3) (https://resource.cdn.icai.org/74737bos60488-m2-cp9.pdf ).
10. File under section 137 in the right form (AOC-4, AOC-4 XBRL, AOC-4 NBFC (Ind AS), with the CFS version and CSR-2 where needed) within the period in Section 9, then the annual return under section 92 in MGT-7 or MGT-7A (https://resource.cdn.icai.org/74737bos60488-m2-cp9.pdf and https://resource.cdn.icai.org/74735bos60488-m2-cp7.pdf ).

## Ask the client first

- Are any of the company's shares or debt securities listed or being listed, in India or abroad, and is that on a main board or an SME exchange?
- What were the company's paid-up share capital and net worth at the balance sheet date, and its turnover in the preceding financial year?
- Is the company a holding, subsidiary, associate or joint venture of another company, and does that company apply Ind AS?
- Has the company ever prepared Ind AS statements or filed in XBRL, voluntarily or otherwise?
- What were its borrowings from banks or financial institutions, and its public deposits, at their highest point in the year?
- Has it missed any financial statement or annual return filing in earlier years? Check whether any exemption you rely on is lost by a filing default.

## When to refuse or refer

- Banking companies, insurance companies and electricity companies: refer.
- NBFCs applying Ind AS (Division III and the NBFC roadmap): refer to an accountant with NBFC experience.
- First-time adoption of Ind AS (Ind AS 101 transition): refer.
- Government companies: refer.
- Restatement, reopening or voluntary revision of earlier accounts (sections 130 and 131): refer.
- A company that has missed filings for several years and needs condonation or a compounding application: refer to a company secretary.
- Any question that turns on the Corporate Laws (Amendment) Bill, 2026 or a proposed rule: say it is not law and refer for the position on the filing date.
- Income tax computation, tax audit and the return: outside this Guide; see `in-income-tax` for individuals and `india-transfer-pricing` for related-party pricing. Formation and post-incorporation filings: see `india-formation`.

## Sources

- Companies (Specification of definition details) Amendment Rules, 2025, G.S.R. 880(E) of 1 December 2025: https://egazette.gov.in/WriteReadData/2025/268124.pdf
- Corporate Laws (Amendment) Bill, 2026 (Bill No. 85 of 2026, pending): https://egazette.gov.in/WriteReadData/2026/271201.pdf
- Finance Act, 2026 (4 of 2026): https://egazette.gov.in/WriteReadData/2026/271439.pdf
- Income-tax Act, 2025 (30 of 2025): https://egazette.gov.in/WriteReadData/2025/265620.pdf
- Code on Social Security, 2020 (36 of 2020): https://egazette.gov.in/WriteReadData/2020/222111.pdf
- Commencement of the Code on Social Security, S.O. 5319(E) of 21 November 2025: https://egazette.gov.in/WriteReadData/2025/267882.pdf
- ICAI Guidance Note on CARO 2020 (reproduces the Order and section 2 definitions): https://resource.cdn.icai.org/60117aasb48979-a.pdf
- ICAI study material, Introduction to Ind AS (reproduces rule 4 of the Ind AS Rules): https://resource.cdn.icai.org/87811bos-280825-final-ch1.pdf
- ICAI study material, Accounts of Companies (sections 128 to 138 and the Accounts Rules): https://resource.cdn.icai.org/74737bos60488-m2-cp9.pdf
- ICAI study material, Management and Administration (section 92): https://resource.cdn.icai.org/74735bos60488-m2-cp7.pdf
- ICAI study material, Audit and Auditors (sections 139 to 148 and the Audit Rules): https://resource.cdn.icai.org/74738bos60488-m2-cp10.pdf

## Disclaimer

This Guide and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this Guide. All outputs must be reviewed and signed off by a qualified professional before filing or acting upon.

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
