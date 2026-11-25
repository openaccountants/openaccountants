---
name: india-financial-statements
description: >
  Use this skill whenever asked about Indian company annual financial statements for
  the financial year ending 31 March 2027 (FY 2026-27). Trigger on phrases like
  financial statements India, Companies Act 2013 accounts, Schedule III, Ind AS or AS,
  Ind AS applicability, statutory audit India, CARO 2020, small company India, One
  Person Company accounts, AOC-4, AOC-4 XBRL, MGT-7, MGT-7A, AGM deadline, internal
  audit section 138, deferred tax rate India, balance sheet format India, or any
  question about preparing, auditing or filing a company's accounts with the Registrar
  of Companies. It covers the Ind AS roadmap, the small company limits from 1 December
  2025, required statements, year-end adjustments with the 2026-27 company tax rates,
  Schedule III formats, audit and CARO tests, internal audit, AGM timing and ROC filing
  periods. Tier 2, not reviewed by an accountant.
version: "2.1"
jurisdiction: IN
tax_year: 2026
tax_year_notes: "FY 2026-27 (financial year ending 31 March 2027; tax year 2026-27 under the Income-tax Act 2025); law as in force on 22 November 2026"
last_updated: 2026-11-22
depends_on:
  - financial-statements-workflow-base
category: financial-statements
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: financial-statements
type: situation-rules
---

# India Company Financial Statements: Framework, Formats, Audit and Filing, FY 2026-27

> **General reference only.** This skill is general reference material for AI-assisted workflows. It has not been reviewed for any specific company's facts. Do not rely on it to prepare, sign or file accounts without review by a qualified professional (a chartered accountant or company secretary) in India.

This skill covers company financial statements for FY 2026-27 under the Companies Act, 2013 and the Income-tax Act, 2025. It uses the law in force on 22 November 2026. The Corporate Laws (Amendment) Bill, 2026 remained before Parliament at that date.

## Who this applies to

| Field | Value |
| --- | --- |
| Country | India (Republic of India) |
| Currency | INR |
| Filing authority | Ministry of Corporate Affairs (MCA), Registrar of Companies (ROC) |
| Primary legislation | Companies Act, 2013, Chapter IX (sections 128 to 138, accounts) and Chapter X (sections 139 to 148, audit) |
| Supporting legislation | Companies (Accounts) Rules, 2014; Companies (Audit and Auditors) Rules, 2014; Companies (Indian Accounting Standards) Rules, 2015; Companies (Accounting Standards) Rules, 2021; Companies (Auditor's Report) Order, 2020, referred to in this skill as CARO (2020) |
| Accounting standards | Ind AS (converged with IFRS) or the Accounting Standards (AS), by the Ind AS roadmap tests in the rates table |
| Financial year | Section 2(41): ends on 31 March. The first financial year of a company incorporated from 1 January ends on 31 March of the following calendar year. A qualifying group company may obtain approval for a different year for overseas consolidation. |
| Statement formats | Schedule III: Division I (AS companies), Division II (Ind AS companies other than NBFCs), Division III (Ind AS NBFCs) |
| Filing form | e-Form AOC-4, AOC-4 XBRL or AOC-4 NBFC (Ind AS); consolidated statements in AOC-4 CFS (or the XBRL or NBFC version) |
| Filing deadline | Thirty days after the AGM (section 137(1)); 180 days from the close of the financial year for an OPC |
| AGM | Section 96: within six months of the close of the financial year (first AGM within nine months), not more than fifteen months between AGMs; an OPC holds none |

### Which framework applies

The Companies (Indian Accounting Standards) Rules, 2015 set the Ind AS roadmap. Use audited standalone net worth and apply Ind AS from the year after the first year-end at which a company newly meets the threshold. Once a company applies Ind AS voluntarily or mandatorily, it continues applying Ind AS in subsequent years.

| Entity type | Framework |
| --- | --- |
| Listed company (main board, India or abroad) | Ind AS (Phase I or Phase II) |
| Unlisted company with net worth at or above the Phase II amount in the rates table | Ind AS |
| Holding, subsidiary, joint venture or associate of an Ind AS company | Ind AS |
| Company listed only on an SME exchange | AS, unless it opts into Ind AS |
| Any other company, including most small companies and One Person Companies | AS (Companies (Accounting Standards) Rules, 2021), unless it opts into Ind AS |
| NBFC | Separate rule 4(1)(iv) roadmap. Phase I from 1 April 2018 covers net worth of at least INR 500 crore. Phase II from 1 April 2019 covers listed or listing NBFCs below INR 500 crore and unlisted NBFCs from INR 250 crore to below INR 500 crore. The specified group entities are also covered. Outside that roadmap, check the applicable rules before using Ind AS. |
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
| Surcharge, domestic company in the ordinary regime, total income over INR 1 crore to INR 10 crore | 7% | Subject to marginal relief | https://egazette.gov.in/WriteReadData/2026/271439.pdf |
| Surcharge, same, total income over INR 10 crore | 12% | Subject to marginal relief | https://egazette.gov.in/WriteReadData/2026/271439.pdf |
| Surcharge, domestic company under s 200 or 201 | 10% ordinarily | A qualifying Schedule V special purpose vehicle under section 57(2) or (3) takes the 25% surcharge | https://egazette.gov.in/WriteReadData/2026/275521.pdf#page=6 |
| Health and Education Cess | 4% of tax plus surcharge | All companies | https://egazette.gov.in/WriteReadData/2026/271439.pdf |
| AGM, every company except an OPC (section 96(1)) | Ordinary AGM within 6 months of year-end, first AGM within 9 months of first year-end, at most 15 months between AGMs | For a special reason the Registrar may extend an AGM other than the first by at most 3 months | https://resource.cdn.icai.org/74735bos60488-m2-cp7.pdf |
| OPC financial statements filing (section 137(1) proviso) | Within 180 days from the close of the financial year | OPC need not hold an AGM | https://resource.cdn.icai.org/74737bos60488-m2-cp9.pdf |

## The base

### Required financial statements (section 2(40))

Section 2(40) lists what "financial statement" includes, as reproduced in ICAI study material (https://resource.cdn.icai.org/74737bos60488-m2-cp9.pdf ):

1. a balance sheet as at the end of the financial year;
2. a profit and loss account (or an income and expenditure account for a not-for-profit company);
3. a cash flow statement. Section 2(40) permits an OPC, small company or dormant company to omit it. G.S.R. 583(E) also covers a qualifying private start-up company that has no default in its section 92 or 137 filings.
4. a statement of changes in equity, if applicable (Ind AS companies);
5. explanatory notes forming part of any of these.

| Document | Who prepares it | Notes |
| --- | --- | --- |
| Balance sheet | Every company | Schedule III, Part I of the relevant Division |
| Statement of profit and loss | Every company | Schedule III, Part II of the relevant Division |
| Statement of changes in equity | Ind AS companies | Division II and Division III |
| Cash flow statement | Every company except those excepted by section 2(40) and G.S.R. 583(E) | See item 3 |
| Notes | Every company | Accounting policies and the Schedule III disclosures |
| Board's report (section 134) | Every company | An OPC or small company prepares the abridged report from its standalone financial statement under rule 8A. |
| Auditor's report | Every company | Section 134 attaches it to every financial statement |
| Consolidated financial statements (section 129(3)) | A company with one or more subsidiaries or associate companies | Prepared for the company and all subsidiaries, associates and joint ventures, laid before the AGM with the standalone statements; Form AOC-1 sets out the salient features of each subsidiary, associate and joint venture (rule 5) |

### What small company or OPC status changes

A small company is a company, other than a public company, that meets BOTH limits: paid-up share capital not more than the first amount in the rates table, AND turnover (as per the profit and loss account for the immediately preceding financial year) not more than the second amount there. The section sets a ceiling; the actual limits are in rule 2(1)(t) of the Companies (Specification of definition details) Rules, 2014, substituted by G.S.R. 880(E) of 1 December 2025, in force from its publication that day.

Excluded from small company status whatever their size (section 2(85) proviso, reproduced in the CARO 2020 Guidance Note, https://resource.cdn.icai.org/60117aasb48979-a.pdf ): a public company; a holding company or a subsidiary company; a company registered under section 8; a company or body corporate governed by any special Act. A company that fails either limit, or falls in an excluded class, is not a small company.

**Pending, not law.** The Corporate Laws (Amendment) Bill, 2026 (Bill No. 85 of 2026, introduced in the Lok Sabha on 23 March 2026, https://egazette.gov.in/WriteReadData/2026/271201.pdf ) would raise the section 2(85) ceilings and change the section 403 additional fee. It has not been enacted. Apply the limits in the rates table until an amending Act and new rules are notified.

| Relief | Small company | OPC | Where |
| --- | --- | --- | --- |
| Cash flow statement | May omit | May omit | Section 2(40) |
| CARO (2020) does not apply | Yes | Yes | CARO (2020) paragraph 1(2)(iv) (see Penalties and interest: audit) |
| Auditor rotation under section 139(2) does not apply | Yes | Yes | Companies (Audit and Auditors) Rules, rule 5 |
| Auditor's report on internal financial controls not required | Subject to the no-default condition | Subject to the no-default condition | G.S.R. 583(E) |
| Abridged Board's report | Required | Required | Section 134(3A) and Companies (Accounts) Rules, rule 8A |
| Annual return in Form MGT-7A instead of MGT-7 | Yes | Yes | Rule 11 of the Companies (Management and Administration) Rules, 2014 (see Deadlines and filing) |
| Statutory audit | Still required | Still required | Section 134 and section 139 (see Penalties and interest: audit) |

### Year-end adjustments checklist

| # | Adjustment | India-specific notes |
| --- | --- | --- |
| 1 | Depreciation | Schedule II to the Companies Act prescribes useful lives; component accounting applies under Ind AS 16 |
| 2 | Provisions and contingencies | Ind AS 37 / AS 29: present obligation, probable outflow, reliable estimate |
| 3 | Employee benefits | Ind AS 19 / AS 15. Classify gratuity and leave benefits and measure each under its applicable rule. Check the AS 15 measurement relief for an eligible smaller enterprise. |
| 4 | Credit losses on receivables | Ind AS 109 expected credit loss model for Ind AS companies. AS companies do not apply Ind AS 109; follow the company's accounting policy for doubtful debts. AS 4 is not the receivables standard: it covers contingencies and events occurring after the balance sheet date |
| 5 | Inventory | Ind AS 2 / AS 2: lower of cost and net realisable value. Use specific identification for non-interchangeable or segregated project inventory and FIFO or weighted average for other inventory. |
| 6 | Deferred tax | Ind AS 12 / AS 22. Use rates enacted or substantively enacted by the reporting date and applicable to the expected reversal. Include applicable surcharge and cess. The table shows the 2026-27 tax-year rates. |
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

Use Part II of the applicable Schedule III Division. Division I presents exceptional and extraordinary items, tax expense, results of continuing and discontinuing operations and earnings per equity share. Divisions II and III also present other comprehensive income, split by whether items may be reclassified to profit or loss, and total comprehensive income. Use each Division's captions and subtotals, including the separate financial and non-financial presentation for NBFCs where prescribed.

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

File the adopted statements within 30 days of the AGM. If the AGM does not adopt them, file the unadopted statements provisionally within 30 days and file the adopted statements within 30 days of the adjourned AGM. If no AGM is held, file the signed statements, attachments and reasons within 30 days of the last date on which the AGM should have been held. Include any required consolidated statements.

A One Person Company, which need not hold an AGM, files the financial statements duly adopted by its member within one hundred eighty days from the close of the financial year (section 137(1) proviso, as reproduced in the ICAI chapter on accounts of companies).

Section 135 applies if, in the immediately preceding financial year, net worth was at least INR 500 crore, turnover was at least INR 1,000 crore or net profit was at least INR 5 crore. The minimum spend is 2% of average qualifying net profits over the preceding 3 financial years, or the available preceding years for a newer company. If required spend is at most INR 50 lakh, the Board performs the CSR committee's functions.

Once a company has started filing in XBRL it must keep filing in XBRL in later years, even if it no longer meets a test in the rates table. An NBFC that applies Ind AS files Form AOC-4 NBFC (Ind AS), and its consolidated statements in AOC-4 CFS NBFC (Ind AS). A company covered by section 135(1) files its CSR report in Form CSR-2 as an addendum to Form AOC-4, AOC-4 XBRL or AOC-4 NBFC (Ind AS) (rule 12(1B) of the Companies (Accounts) Rules, 2014).

From 14 July 2025, include the applicable e-Forms Extract of Board Report and Extract of Auditor's Report with AOC-4 and its variants, including the consolidated extract when required. Also attach the signed authenticated financial statements and required documents in PDF with the XBRL form. Use e-Form AOC-1 for the group statement under rule 5.

**Annual return.** Separately from the financial statements, the annual return under section 92 is filed in Form MGT-7 (MGT-7A for an OPC or small company).

**AGM date (section 96).** For the financial year ending 31 March 2027, an ordinary AGM is generally due by 30 September 2027, subject to the 15-month interval and any permitted extension. For a first financial year ending on that date, the first AGM is due by 31 December 2027. Count the financial statement filing period from the actual AGM or the applicable statutory fallback.

**Additional fee for late filing (section 403).** The prescribed ordinary fee for late section 92 or 137 filings is INR 100 per day in addition to the standard filing fee. Check for any fee relief for the specific filing period. The additional fee and the statutory penalty are separate.

## Penalties and interest

Section 137(3) sets an INR 10,000 company penalty plus INR 100 for each day of continuing default, capped at INR 200,000. The responsible officers or directors face INR 10,000 plus INR 100 per day after the first, capped at INR 50,000. Check the reduced penalty under section 446B for an OPC, small company, recognised start-up or Producer Company.

### Audit: statutory audit (sections 134 and 139 to 148)

Companies, including an OPC or small company, require a statutory audit. Under section 139(1), the auditor appointed at the first AGM holds office from the close of that meeting to the close of the sixth AGM, counting the appointment meeting as the first. For a non-government company under section 139(6), the Board appoints the first auditor within 30 days of registration. If the Board fails to appoint, the members appoint the auditor within 90 days at an extraordinary general meeting. Government-controlled companies use the separate section 139(5) and (7) routes.

**Pending, not law:** the 2026 Bill would add section 139(12), letting the government exempt prescribed classes of companies from appointing auditors. Until it is enacted and the classes are prescribed, no size-based audit exemption exists.

### Audit: CARO (2020)

The auditor of a company covered by the Companies (Auditor's Report) Order, 2020 adds the CARO matters in paragraphs 3 and 4 to its section 143 report for financial years commencing on or after 1 April 2021. For consolidated financial statements, apply paragraph 3(xxi). The Order covers companies, including a foreign company within section 2(42), subject to these exclusions:

1. a banking company;
2. an insurance company;
3. a company licensed under section 8;
4. a One Person Company and a small company;
5. a private limited company, not a subsidiary or holding company of a public company, that meets ALL THREE tests in the rates table.

Failing one test means CARO applies. A small company stays outside CARO even if it fails the private company tests. Status is judged at the balance sheet date. Since 1 December 2025 the small company exclusion follows the new section 2(85) limits in the rates table.

### Audit: auditor rotation (section 139(2) and rule 5)

Section 139(2) allows an individual one 5-year term and a firm two consecutive 5-year terms, followed by a 5-year cooling-off period. The rule applies to listed companies and to unlisted public companies with paid-up capital of at least INR 10 crore, private limited companies with at least INR 50 crore and companies below their relevant capital threshold with qualifying bank or financial institution borrowings or public deposits of at least INR 50 crore. Rule 5 excludes OPCs and small companies.

### Audit: internal financial controls report (section 143(3)(i))

G.S.R. 583(E), as corrected, exempts a private company with no section 92 or 137 filing default if it is an OPC or small company, or if both its latest audited turnover is below INR 50 crore and its aggregate borrowings from banks, financial institutions and bodies corporate stay below INR 25 crore throughout the financial year.

### Audit: internal audit (section 138 and rule 13)

Every test looks at the PRECEDING financial year. Meeting any ONE test is enough.

| Company | Must appoint an internal auditor if, in the preceding financial year, it had |
| --- | --- |
| Listed company | Always |
| Unlisted public company | Paid-up share capital of fifty crore rupees or more; OR turnover of two hundred crore rupees or more; OR outstanding loans or borrowings from banks or public financial institutions exceeding one hundred crore rupees at any point; OR outstanding deposits of twenty-five crore rupees or more at any point |
| Private company | Turnover of two hundred crore rupees or more; OR outstanding loans or borrowings from banks or public financial institutions exceeding one hundred crore rupees at any point |

Source: ICAI chapter on accounts of companies, https://resource.cdn.icai.org/74737bos60488-m2-cp9.pdf . The internal auditor is a chartered accountant or a cost accountant (in practice or not), or such other professional as the Board decides, and may be an employee. The audit committee or the Board sets the scope, frequency and method in consultation with the internal auditor.

## Cross-border points

- Test a foreign company against section 2(42), the Chapter X audit obligation and the applicable CARO exclusions.
- A company listed abroad counts as listed for the Ind AS roadmap.
- Foreign currency monetary items are translated at the closing rate (Ind AS 21 / AS 11).
- Under Ind AS rule 4(5) and (6), an overseas group entity may prepare its standalone statements under local requirements. Test the Indian group entity under rule 4(1) for mandatory Ind AS, and use Ind AS for consolidation when applicable.
- Related-party pricing with foreign group companies: `india-transfer-pricing`.

## Worked examples

### Example 1: Is the company a small company for FY 2026-27?

An ordinary private trading company has paid-up capital of INR 8 crore and non-negative reserves and surplus at 31 March 2027. Its preceding FY 2025-26 turnover was INR 120 crore. The capital is INR 2 crore below the small company ceiling and the preceding-year turnover is INR 20 crore above its ceiling, so the company is outside the small company class and uses MGT-7. Paid-up capital plus reserves and surplus exceeds the CARO private-company limit of INR 1 crore. Assuming no other exemption applies, CARO applies. The capital is INR 3 crore above the XBRL minimum, so the company uses AOC-4 XBRL.

```oa-check
name: Small company test, capital 8 crore, preceding-year turnover 120 crore
inputs:
  paid_up: 80000000
  turnover: 1200000000
steps:
  - capital_headroom: 100000000 - paid_up
  - turnover_headroom: 1000000000 - turnover
  - weakest_headroom: min(capital_headroom, turnover_headroom)
  - xbrl_capital_margin: paid_up - 50000000
expected:
  capital_headroom: 20000000
  turnover_headroom: -200000000
  weakest_headroom: -200000000
  xbrl_capital_margin: 30000000
```

A negative weakest headroom fails the small company test. A zero or positive XBRL capital margin meets the INR 5 crore capital test.

### Example 2: Deferred tax rate, stay in the default regime or opt for section 200

An ordinary domestic company with FY 2024-25 turnover of INR 350 crore has a net taxable temporary difference of INR 10 crore at 31 March 2027. Assume that the enacted or substantively enacted rates applicable when the difference reverses are the rates illustrated here, with total income including reversals of INR 5 crore a year. Under the default regime, 25% tax, 7% surcharge and 4% cess give 27.82% and an INR 27,820,000 deferred tax liability. With a valid section 200 election and ordinary 10% surcharge, 22% tax and 4% cess give 25.168% and an INR 25,168,000 liability. Use the regime and rates expected to apply when each difference reverses.

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
5. Post the year-end adjustments. Measure deferred tax using enacted or substantively enacted rates for the expected reversal under the applicable accounting standard.
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
| Companies Act, sections 2, 92, 96, 129, 134-139, 403 and 446B | https://www.indiacode.nic.in/bitstream/123456789/2114/5/A2013-18.pdf?v=20260526072457 | 2026-11-24 |
| MCA, Schedule III amendments from April 2021 | https://www.mca.gov.in/Ministry/pdf/ScheduleIIIAmendmentNotification_13042021.pdf | 2026-11-24 |
| ICAI, Schedule III Division I, Appendix A | https://resource.cdn.icai.org/68981clcgc55147-gnd1.pdf | 2026-11-24 |
| ICAI, Schedule III Division II, Appendix A | https://resource.cdn.icai.org/68982clcgc55147-gnd2.pdf | 2026-11-24 |
| ICAI, Schedule III Division III, Appendix A | https://resource.cdn.icai.org/68983clcgc55147-gnd3.pdf | 2026-11-24 |
| Gazette, Ind AS Rules including amended rule 4 and the NBFC roadmap | https://thc.nic.in/Central%20Governmental%20Rules/Companies%20%28Indian%20Accounting%20Standards%29%20Rules%2C2015.pdf | 2026-11-24 |
| MCA, Companies Accounting Standards Rules 2021 | https://www.mca.gov.in/bin/dms/getdocument?mds=RKk43Bmg99ksfV0bUGr6XA%253D%253D&type=open | 2026-11-24 |
| India Gazette, Taxation and Other Laws (Amendment) Act 2026, section 6 | https://egazette.gov.in/WriteReadData/2026/275521.pdf#page=6 | 2026-11-24 |
| India Gazette, CARO second amendment, commencement | https://egazette.gov.in/WriteReadData/2020/223784.pdf#page=2 | 2026-11-24 |
| Companies Accounts Second Amendment Rules 2025, rules 5 and 12 | https://egazette.gov.in/WriteReadData/2025/263619.pdf | 2026-11-24 |
| XBRL amendment, signed statements in PDF | https://egazette.gov.in/WriteReadData/2025/263676.pdf | 2026-11-24 |
| MCA, Companies Registration Offices and Fees Second Amendment Rules 2018 | https://www.mca.gov.in/Ministry/pdf/CompaniesOfficesFeesRules_07052018.pdf | 2026-11-24 |
| India Code, G.S.R. 583(E) private company exemptions | https://upload.indiacode.nic.in/showfile?actid=AC_CEN_22_29_00008_201318_1517807327856&filename=Exemption+to+Private+Companies+under+section+462+of+CA%2C+2013.pdf&type=notification | 2026-11-24 |
| India Code, G.S.R. 583(E) corrigendum | https://upload.indiacode.nic.in/showfile?actid=AC_CEN_22_29_00008_201318_1517807327856&filename=Exemption+to+Private+Company%28corrigendum%29.pdf&type=notification | 2026-11-24 |
| MCA, Audit and Auditors Rules, rule 5 | https://www.mca.gov.in/Ministry/pdf/NCARules_Chapter10.pdf | 2026-11-24 |
| India Code, 2017 audit rotation threshold amendment | https://upload.indiacode.nic.in/showfile?actid=AC_CEN_22_29_00008_201318_1517807327856&filename=Companies+%28Audit+and+Auditors%29+Second+Amendment+Rules%2C+2017.pdf&type=rule | 2026-11-24 |
| India Code, abridged Board's report rule 8A | https://upload.indiacode.nic.in/showfile?actid=AC_CEN_22_29_00008_201318_1517807327856&filename=companis+Accounts+Rules_31072018.pdf&type=rule | 2026-11-24 |
| MCA, Ind AS 12 paragraph 47 | https://www.mca.gov.in/Ministry/pdf/IndAS12_2020_10112020.pdf | 2026-11-24 |

Not yet confirmed: any future fee relief for FY 2026-27 filings and the rates in force when a future temporary difference reverses. Check the applicable law at the reporting or filing date.
