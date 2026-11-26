---
name: malta-financial-statements
description: Use this skill when preparing, reviewing, or advising on annual financial statements for a Maltese company. Trigger on phrases like "annual accounts Malta", "financial statements Malta", "Companies Act filing", "MBR filing", "balance sheet format", "profit and loss format", "directors' report", "audit exemption Malta", "small company Malta", "abridged accounts", "year-end adjustments", or any question about preparing statutory accounts under the Malta Companies Act (Cap. 386). Covers reporting frameworks, size thresholds, required statements, P&L and balance sheet formats, notes disclosures, filing deadlines, and audit requirements.
version: "2.1"
jurisdiction: MT
tax_year: 2026
last_updated: 2026-11-26
depends_on:
  - financial-statements-workflow-base
category: financial-statements
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: financial-statements
type: situation-rules
---

# Malta statutory financial statements: framework, size tests, audit, approval and filing with the Registrar

## Scope
This skill covers the annual accounts that a company registered in Malta under the Companies Act must prepare, have audited (or not), lay before its members and deliver to the Registrar of Companies at the Malta Business Registry (MBR). It covers:

- which accounting framework applies: IFRS as adopted by the EU, or GAPSME (the General Accounting Principles for Small and Medium-Sized Entities);
- the size tests in article 185 of the Companies Act (small company, the micro "at least two of three" audit exemption, small group) and in the GAPSME Regulations;
- the audit requirement under the Companies Act and the separate audit requirement for income tax under article 19(4)(a) of the Income Tax Management Act, as relaxed by the Audit Exemption Rules 2025;
- the directors' report, signing, laying before the general meeting, delivery to the Registrar, and the penalties for default.

**Year.** Malta companies may use any accounting reference date. Figures are for accounting periods reported in tax year 2026 (calendar 2026), using the statutory text and the period-start instruction identified below. Most companies with a 31 December year-end are now finishing their **2025** accounts: see Case 1 and "When the higher limits started".

**Not covered.** Corporate income tax computations, tax rates, refunds and the company tax return: see the **mt-corporate-tax** skill. VAT: see the **malta-vat-return** skill. Banks, financial institutions, insurers, investment companies with variable share capital (SICAVs), partnerships and corporate sustainability reporting (CSRD): Check this point with one of our partner accountants. Their specialist treatment is not decided here.

**Sources.** The operative provisions supporting this Guide were checked on 26 November 2026, with the earlier completed GAPSME size-test reading reused where unchanged. Portal fields, professional signing eligibility and specialist reporting are referred below.

Built from the law: not yet approved by an accountant.

## Ask the client first

- Is the company **private or public**? Is any of its securities admitted to trading on a regulated market, or is it a public-interest entity (PIE)? GAPSME excludes PIEs. For PIEs or listed issuers: Check this point with one of our partner accountants.
- What is the company's **accounting reference date**, and is this its first accounting period? If first, when was it registered, and how long is the period?
- For **this and the previous balance sheet date**: total assets (balance sheet total), net turnover (excluding VAT and rebates), and average number of employees (full-time weeks divided by weeks in the period, plus part-time hours divided by weeks in the period and by forty, each rounded to the nearest whole number). After the first balance sheet date, article 185 changes the relevant exemption only after two consecutive accounting periods.
- Is the company a **parent**? If so, what are the group totals, net and gross, and is the company itself a subsidiary of an EU/EEA parent that consolidates it?
- Has the **board resolved** to use IFRS as adopted by the EU instead of GAPSME? For which period?
- Is the company an **exempt company** under article 211 (at most fifty debenture holders, no corporate director, no outside control of policy, conditions written into the memorandum or articles)?
- Who are the **shareholders**, when was the company registered, and what are their education dates (MQF level 3 or higher)? This matters for the income tax start-up audit waiver.
- Is an **auditor already appointed**? When is the general meeting planned?
- Is the company registered under the **Merchant Shipping Act**, a bank, insurer, financial institution or SICAV? If yes, see "When to refuse or refer".
- Were **previous accounts or annual returns** filed late, or not at all?

## The method, step by step

1. **Fix the period.** Take the accounting reference date. If no notice was given within nine months of registration, it is 31 December. The first accounting reference period runs from registration and lasts at least six and at most eighteen months. The directors may end any period up to seven days either side of the reference date. ([Cap. 386 art. 164](https://legislation.mt/getpdf/6a1836349844fb1e280ec744))
2. **Size the company under article 185.** Test each balance sheet date against the small-company limits and, for a private company, the micro limits. A limit is met when the company does "not exceed the limits of at least two of the three" criteria. After the first balance sheet date, changes to the relevant exemption require two consecutive accounting periods. A parent must pass the group condition, unless the article 174 exception applies. ([Cap. 386 art. 185](https://legislation.mt/getpdf/6a1836349844fb1e280ec744))
3. **Pick the framework.** An entity inside the GAPSME small or medium limits (which are different from the article 185 limits) prepares GAPSME accounts unless the board has resolved to use IFRS as adopted by the EU. Any entity outside those limits, and every PIE, uses IFRS as adopted by the EU. ([GAPSME Regulations reg. 4 and 5](https://legislation.mt/getpdf/6641e0860419230b5c3872a1))
4. **Decide the audit.** A private company inside the micro limits (at least two of three) is exempt from the Companies Act audit. For ordinary companies outside this exemption, obtain the statutory audit; specialist entities are referred below. Then apply the **separate** income tax rule: for tax, an eligible company registered in Malta under rule 6, for periods starting on or after 1 January 2025, meeting two of three can satisfy the audit-report requirement with a review report (a full audit also satisfies it), and one meeting all three needs neither. ([Cap. 386 art. 185(2)](https://legislation.mt/getpdf/6a1836349844fb1e280ec744); [Audit Exemption Rules 2025](https://legislation.mt/getpdf/688b3e0cbed0ef08a863ffa1))
5. **Prepare the accounts.** Balance sheet, profit and loss account (income statement) and notes, plus anything else the framework requires, as a composite whole showing a true and fair view. Show the company's name, registration number, legal form and registered office. ([Cap. 386 art. 167](https://legislation.mt/getpdf/6a1836349844fb1e280ec744))
6. **Prepare the directors' report** unless the company is small under article 185(1). ([Cap. 386 art. 177 and 185(1)](https://legislation.mt/getpdf/6a1836349844fb1e280ec744))
7. **Approve and sign.** The board approves the accounts; two directors sign and date the balance sheet (one, if an exempt company has only one director). The board approves the directors' report and two directors date and sign it, with the same sole-director exception. ([Cap. 386 art. 176, 178 and 211(5)](https://legislation.mt/getpdf/6a1836349844fb1e280ec744))
8. **Audit (if required),** then send copies to members and debenture holders at least fourteen days before the general meeting. ([Cap. 386 art. 179 and 180](https://legislation.mt/getpdf/6a1836349844fb1e280ec744))
9. **Lay the accounts** before the general meeting for approval: within ten months after the end of the accounting reference period for a private company, seven months for a public company, subject to article 182(3)-(4). ([Cap. 386 art. 181 and 182](https://legislation.mt/getpdf/6a1836349844fb1e280ec744))
10. **Deliver to the Registrar** within forty-two days from the end of that laying period, with any exemption declaration. File the annual return on its own cycle. ([Cap. 386 art. 183 and 184](https://legislation.mt/getpdf/6a1836349844fb1e280ec744))
11. **Hand over to tax.** The audited (or reviewed, or exempt) accounts support the company tax return. See the **mt-corporate-tax** skill.

Order matters. If you choose the framework before testing size, a company may be put on IFRS or GAPSME wrongly. If you drop the audit because of the tax rules, you may breach the Companies Act, which has its own, different test.

### Rates, bands and thresholds

| Item | Figure | Conditions | Source |
|---|---|---|---|
| Small company, periods starting on or after 20 March 2026 | Not exceeding at least two of: EUR 5,000,000 balance sheet total, EUR 10,000,000 net turnover, 50 employees | Two consecutive periods to change status; no directors' report | Cap. 386 art. 185(1): https://legislation.mt/eli/cap/386/eng/pdf |
| Small company, periods starting before 20 March 2026 (every calendar 2025 and 2026 period) | Not exceeding at least two of: EUR 4,000,000, EUR 8,000,000, 50 employees | MBR: the new limits are mandatory only for periods starting on or after 20 March 2026; no early adoption | Cap. 386 art. 185(1), consolidated 16 December 2025: https://legislation.mt/getpdf/695277d8cc8c701d50c749db |
| Start date of the higher limits | Financial reporting periods starting on or after 20 March 2026 | Early or retroactive use prohibited | MBR informative note: https://www.mbr.mt/post/informative-note-entry-into-force-of-legislation-1 |
| Micro audit exemption, private companies | Not exceeding at least two of: EUR 46,600 balance sheet total, EUR 93,000 net turnover, 2 employees | Exempt from Chapter IX, the auditors' report and the Third Schedule | Cap. 386 art. 185(2): https://legislation.mt/eli/cap/386/eng/pdf |
| Small group, from 20 March 2026 periods | EUR 5,000,000 net or EUR 6,000,000 gross; EUR 10,000,000 net or EUR 12,000,000 gross; 50 employees | Net or gross basis may be used | Cap. 386 art. 185(5): https://legislation.mt/eli/cap/386/eng/pdf |
| Small group, earlier periods | EUR 4,000,000 net or EUR 4,800,000 gross; EUR 8,000,000 net or EUR 9,600,000 gross; 50 employees | same | Cap. 386 art. 185(5), consolidated 16 December 2025: https://legislation.mt/getpdf/695277d8cc8c701d50c749db |
| GAPSME small entity | EUR 4,000,000 balance sheet total, EUR 8,000,000 revenue, 50 employees | Not raised with the Companies Act; two of three, two consecutive years | S.L. 281.05 reg. 5(1)(a): https://legislation.mt/eli/sl/281.5/eng/pdf |
| GAPSME medium-sized entity | EUR 20,000,000, EUR 40,000,000, 250 employees | Not small, and not exceeding at least two of these three; apply reg. 5 timing, PIE exclusion and non-twelve-month revenue annualisation | S.L. 281.05 reg. 5(1)(b): https://legislation.mt/eli/sl/281.5/eng/pdf |
| Tax start-up audit waiver turnover cap | EUR 80,000, pro rata for a period that is not twelve months | First two periods; sole shareholders all individuals with successful MQF level 3+ completion recognised by MQRIC who set up within three years; rule 5 shareholder-change exclusion | L.N. 139 of 2025 rule 3: https://legislation.mt/eli/ln/2025/139/eng/pdf |
| Audit cost deduction for such a company | 120% of the audit cost, capped at EUR 700 per period | First two periods, all rule 3 definitions and rule 4 conditions; no waiver used; rule 5 exclusion | L.N. 139 of 2025 rule 4: https://legislation.mt/eli/ln/2025/139/eng/pdf |
| Laying accounts | Ten months after the accounting reference period ends (private), seven months (public) | Subject to art. 182(3)-(4) | Cap. 386: https://legislation.mt/eli/cap/386/eng/pdf |
| Delivery to the Registrar | Within forty-two days from the end of the laying period | Art. 183(1); 12 December 2026 for 31 December 2025 year ends | MBR notice: https://www.mbr.mt/post/notice-to-the-public-submission-of-financial-statements-to-the-registrar |
| Penalty, accounts not delivered or defective | Up to EUR 2,329 plus EUR 46 a day | Eleventh Schedule, art. 183(6) | Cap. 386: https://legislation.mt/eli/cap/386/eng/pdf |
| Records not kept properly (offence) | Fine up to EUR 11,646 | Art. 163(6) | same |

### Apply the size tests

The Companies Act and GAPSME tests are separate. Equality meets a limit; exceeding one limit does not fail a two-of-three test.

- **Companies Act:** after the first balance sheet date, crossing or ceasing to cross two limits affects the exemption only in two consecutive accounting periods (art. 185(3)). Total assets are the GAAP balance-sheet total; turnover excludes rebates, VAT and taxes directly linked to turnover. Employee averages are full-time weeks divided by weeks in the period, and part-time hours divided by weeks in the period and by forty, each rounded to the nearest whole number (art. 185(4), (9)-(10)). [Cap. 386](https://legislation.mt/eli/cap/386/eng/pdf).
- **Parents:** apply the group test and its two-period rule, unless article 174 provides an exemption. Net figures include consolidation set-offs and adjustments; gross figures exclude them. Either basis can be used. Use each subsidiary's period ending with the parent's, otherwise its latest period ending before the parent's; if disproportionate expense or undue delay prevents obtaining those figures, use the latest available (art. 185(5)-(8)). [Cap. 386](https://legislation.mt/eli/cap/386/eng/pdf).
- **Transition:** the [MBR instruction](https://www.mbr.mt/post/informative-note-entry-into-force-of-legislation-1) applies the higher Companies Act limits only to periods starting on or after 20 March 2026, with no early or retroactive application. Calendar 2025 and 2026 periods use the previous limits. The older consolidation supplies those previous figures; do not use the current consolidated figures for an earlier period.
- **GAPSME:** medium means not small and within at least two medium limits. After the first period, changes require two consecutive financial years. In the first period use that period's figures. For a non-twelve-month period, annualise revenue by dividing it by the number of months and multiplying by twelve. Include other-source income where revenue is not relevant; PIEs are excluded (reg. 5). [S.L. 281.05](https://legislation.mt/eli/sl/281.5/eng/pdf).
- **Third Schedule medium/large categories and their group limits**, including the different pre-20-March-2026 figures: Check this point with one of our partner accountants. The GAPSME figures above do not decide that separate classification.

### Which framework applies
- The Companies Act requires accounts under "generally accepted accounting principles and practice" (GAAP). Under the Accounting and Auditing Standards Regulations, GAAP means **IFRS as adopted by the EU**, but an entity that meets the eligibility conditions may instead follow GAPSME. ([S.L. 281.02 reg. 3](https://legislation.mt/getpdf/60225987bc8272018c0f70f1))
- **GAPSME is the default for eligible entities.** An entity inside the GAPSME small or medium limits "shall" prepare GAPSME accounts "unless the Board of Directors ... has resolved to prepare financial statements in accordance with IFRS as adopted by the EU for that financial reporting period" (reg. 4). Record the board resolution if the client wants IFRS.
- **IFRS as adopted by the EU** applies to PIEs, to entities over the GAPSME medium limits, and to any entity whose board chooses it. The same framework applies to the comparatives (S.L. 281.02 reg. 3(3)).
- Article 185(2) removes the Chapter IX, audit-report and Third Schedule requirements, while the annual-account obligation in article 167 remains. Select GAPSME or IFRS under the eligibility rules above.
- **Leases and IFRS measurement or presentation details:** Check this point with one of our partner accountants.

#### What the accounts contain

| Framework and size | Statements | Source |
| --- | --- | --- |
| GAPSME, small entity | Balance sheet, income statement, notes | [GAPSME Section 4.1](https://legislation.mt/getpdf/6641e0860419230b5c3872a1) |
| GAPSME, medium-sized entity | As small, plus statement of changes in equity and statement of cash flows | [GAPSME reg. 3 and Section 4](https://legislation.mt/getpdf/6641e0860419230b5c3872a1) |
| IFRS as adopted by the EU | Check this point with one of our partner accountants for the applicable complete statement set and presentation requirements | [S.L. 281.02 reg. 3](https://legislation.mt/eli/sl/281.2/eng/pdf) |
| Every company, on top | Name, registration number, legal form, registered office; true and fair view; departures from the Act disclosed in the notes | [Cap. 386 art. 167](https://legislation.mt/getpdf/6a1836349844fb1e280ec744) |
| Medium-sized and large undertakings | Additional Third Schedule disclosures | [Cap. 386 Third Schedule](https://legislation.mt/getpdf/6a1836349844fb1e280ec744) |

- **Currency.** Accounts are presented in the currency of the share capital. If that is not the euro, state on the balance sheet the ECB (or Central Bank of Malta) rate to the euro at the balance sheet date, and use it to convert euro limits (art. 187).
- **Notes.** Disclose what GAAP requires plus what the Act requires (art. 175). The detailed note list depends on the framework: use the GAPSME Sections (for example related parties in Section 20, post balance sheet events in Section 19) or the relevant IFRS.
- **Formats:** apply the chosen framework together with the Companies Act. For a complete reporting template or uncertain presentation: Check this point with one of our partner accountants.

#### Directors' report
- **Required** for every company that is not small under article 185(1). It names the directors in the period, states the principal activities, and gives a fair, balanced review of the business, its position and its principal risks and uncertainties, with financial (and, where appropriate, non-financial) key performance indicators. It must also cover the matters in the Sixth Schedule (art. 177(3)); for the engagement-specific complete disclosure list: Check this point with one of our partner accountants.
- **Small companies are exempt** from article 177, except the sustainability-reporting obligations of small companies that are PIEs. If a small company uses the exemption, the Sixth Schedule paragraph 3 information about its acquisition of its own shares must go in the notes (art. 185(1)).
- The board approves it; two directors date and sign it, subject to the sole-director exempt-company rule in article 211(5). The copy for the Registrar is signed by a director or the company secretary (art. 178).
- Where there is an audit, the auditor reports whether the directors' report is consistent with the accounts and prepared under the law (art. 179(3)).

### Audit: Companies Act and income tax are two different tests

#### Companies Act
- Every company appoints an auditor at each general meeting where accounts are laid (art. 151), and the auditor reports on every set of annual accounts (art. 179).
- **Exemption:** a **private** company that, on its balance sheet date, stays at or under at least two of €46,600 balance sheet total, €93,000 net turnover and 2 employees is exempt from Chapter IX (Auditors, articles 151 to 162), from the auditors' report in article 179, and from the Third Schedule (art. 185(2)). The two-consecutive-years rule in article 185(3) applies.
- The Companies Act has **no review-report tier**. Under the Act, the ordinary private company either qualifies for this exemption or needs a statutory audit.
- The statutory auditor must fall within the current Accountancy Profession Act definition: a holder of a practising certificate in auditing, including an audit firm ([Cap. 281 art. 2](https://legislation.mt/eli/cap/281/eng/pdf)). S.L. 281.02 reg. 4 prescribes international auditing standards, with EU-adopted standards taking precedence and proportionate application for small undertakings. For the proposed signer's eligibility or future legislative commencement: Check this point with one of our partner accountants.
- The **Companies Act (Audit Exemption) Regulations** (S.L. 386.20), a start-up exemption for companies owned by recent graduates, are marked "Not yet in force" on legislation.mt. Do not rely on them. ([S.L. 386.20](https://legislation.mt/getpdf/602258ccbc8272018c0e3b92))

#### Income tax
- For tax, a company registered in Malta must support its records with a balance sheet and profit and loss account complying with articles 167 to 169 of the Companies Act, with "a report drawn up by a certified public auditor" attached, unless rules say otherwise (ITMA art. 19(4)(a)). A non-resident company's records are those for its Malta activities.
- The **Audit Exemption Rules 2025** (L.N. 139 of 2025) apply from accounting periods starting on or after 1 January 2024, and rule 6 from periods starting on or after 1 January 2025:
  - **Rule 6(1)(a):** a company using the article 185(2) exemption because it meets **two** of the three criteria satisfies the tax audit requirement when a **review report** has been made.
  - **Rule 6(1)(b):** a company meeting **all three** criteria needs neither audit nor review for tax.
  - Rule 6 does not apply to companies registered under the Merchant Shipping Act (rule 7 has their own test). A company that must prepare consolidated accounts keeps rule 6 only while its group is a small group (rule 6(2)). The two-year rule in article 185(3) applies (rule 8).
  - **Rule 3 (start-up waiver):** no auditor's report for the first two accounting periods of a newly registered company whose sole shareholders are individuals who successfully completed a course at MQF level 3 (or higher), recognised by MQRIC, who set up the company within three years of qualifying, and whose turnover does not exceed €80,000 (pro rata for a period that is not twelve months). ([L.N. 139 of 2025](https://legislation.mt/getpdf/688b3e0cbed0ef08a863ffa1))
  - **Rule 4:** if such a company has an audit anyway, it may deduct 120% of the audit cost, up to €700 for each accounting period. ([L.N. 139 of 2025](https://legislation.mt/getpdf/688b3e0cbed0ef08a863ffa1))
  - **Rule 5:** both reliefs end at once if a shareholder change means the shareholders are no longer all qualifying individuals.
- **Review report.** The [MTCA guidelines](https://mtca.gov.mt/docs/default-source/documents/personal-tax/legal-and-technical/guidelines/audit-exemption-rules---guidelines.pdf?sfvrsn=14aab6d_1) define a review engagement under ISRE 2400 (Revised), including subsequent amendments and interpretations issued or adopted by IAASB. The guidelines do not replace professional eligibility rules; for the proposed signer's authorisation: Check this point with one of our partner accountants.
- **Watch the mismatch.** The start-up waiver in rule 3 is a tax rule only. Unless the company also meets the article 185(2) test, the Companies Act still requires an audit.

### Year-end adjustments checklist
Use the company's chosen framework. Collect the schedules for depreciation and tax allowances separately; accruals and prepayments; provisions and contingencies; receivables impairment; inventory; current and deferred tax; foreign currency; leases; revenue cut-off; investment property; leave and bonuses; and events after the reporting period. These are preparation prompts, not recognition or measurement conclusions. For the treatment and disclosures of any such item: Check this point with one of our partner accountants. Route tax computations and elections to **mt-corporate-tax**.

## Boundary and exception table
| Situation | Rule | Source |
| --- | --- | --- |
| Parent within small-group limits | Exempt from consolidated accounts, unless a group company is listed or a PIE | [Cap. 386 art. 173](https://legislation.mt/getpdf/6a1836349844fb1e280ec744) |
| Parent that is itself a subsidiary of an overseas parent | Check this point with one of our partner accountants before applying article 174 | [Cap. 386 art. 174](https://legislation.mt/getpdf/6a1836349844fb1e280ec744) |
| Start-up waiver applies for tax but company fails art. 185(2) | Companies Act audit still required; tax deduction of 120% of the audit cost, capped at €700 | [L.N. 139 of 2025 rules 3 and 4](https://legislation.mt/getpdf/688b3e0cbed0ef08a863ffa1) |
| First period longer than twelve months | Laying period shortened by the excess days, but never below three months | [Cap. 386 art. 182(3)](https://legislation.mt/getpdf/6a1836349844fb1e280ec744) |
| Period shortened by change of reference date | Later of the normal period or three months from the notice | [Cap. 386 art. 182(4)](https://legislation.mt/getpdf/6a1836349844fb1e280ec744) |
| Issuer on a regulated market (ESEF) | Accounts go to the Registrar by an application programming interface or similar electronic means | [Cap. 386 art. 183(1) proviso](https://legislation.mt/getpdf/6a1836349844fb1e280ec744) |

## Worked cases
All amounts are illustrations. Each company is private, not a PIE, not a parent, and has a 31 December year-end unless stated.

**Case 1: micro company meeting two of three (2025 accounts).** Balance sheet total €40,000; net turnover €120,000; 1 employee; the same pattern at 31 December 2024. ([Cap. 386](https://legislation.mt/getpdf/6a1836349844fb1e280ec744))
- Article 185(2): balance sheet total is under €46,600 (met); turnover is over €93,000 (not met); employees under 2 (met). Two of three met on two consecutive dates: **exempt from the Companies Act audit**.
- Article 185(1): small, so **no directors' report**.
- GAPSME small entity limits met: GAPSME accounts (balance sheet, income statement, notes) unless the board resolved on IFRS.
- Tax: rule 6(1)(a) of L.N. 139 of 2025 applies (two of three), so the company can satisfy the tax audit-report requirement with a **review report** instead of an audit. ([L.N. 139 of 2025](https://legislation.mt/getpdf/688b3e0cbed0ef08a863ffa1))
- Deadlines: lay before the general meeting by 31 October 2026; deliver to the Registrar by 12 December 2026 (42 days after 31 October).

**Case 2: comparing the old and new article 185 limits with GAPSME.** Net turnover €9,000,000; balance sheet total €4,500,000; 30 employees, the same in 2024 and 2025. ([Cap. 386](https://legislation.mt/getpdf/6a1836349844fb1e280ec744))
- Article 185(1): turnover under €10,000,000, total assets under €5,000,000, employees under 50: **small** under the limits in force from 20 March 2026, so the higher-limit exemption is used only for a financial reporting period starting on or after that day, under MBR's instruction.
- Under the previous limits (€4,000,000 and €8,000,000), it exceeds both, so it is **not small** and must prepare and deliver a directors' report. For the calendar-year 2025 and 2026 periods, use those previous limits under MBR's period-start instruction and prepare the directors' report.
- Not micro, so a **full audit** is required.
- GAPSME: revenue over €8,000,000 and total assets over €4,000,000 for two years, so not a small entity; within €40,000,000 and €20,000,000, so a **medium-sized entity**. GAPSME accounts must include a statement of changes in equity and a statement of cash flows. ([S.L. 281.05 reg. 5](https://legislation.mt/getpdf/6641e0860419230b5c3872a1))

**Case 3: start-up waiver for tax, audit still required by the Act.** Registered 1 March 2025, first period to 31 December 2025 (ten months). Both shareholders obtained MQF level 6 degrees in 2024. Turnover €50,000; balance sheet total €60,000; 3 employees; audit fee €1,000. ([Cap. 386](https://legislation.mt/getpdf/6a1836349844fb1e280ec744))
- Article 185(2): turnover met, but balance sheet total and employees both exceed the limits. Only one of three met: **not exempt**. The Companies Act audit is required.
- Tax: the pro-rata turnover cap is €80,000 × 10 ÷ 12 = €66,666.67. Turnover of €50,000 is under it, and assume successful MQF completion is recognised by MQRIC, both remain the sole shareholders, and all rule 3 conditions are met, so for tax alone no auditor's report is needed. But the audit happens anyway, so the company does not use the waiver and claims the rule 4 deduction instead: 120% × €1,000 = €1,200, capped at €700. ([L.N. 139 of 2025](https://legislation.mt/getpdf/688b3e0cbed0ef08a863ffa1))
- The first period is ten months, so the normal laying period applies: by 31 October 2026, delivery by 12 December 2026.

**Case 4: long first period.** Registered 1 July 2024; first accounting reference date 31 December 2025 (eighteen months, the maximum).
- The period is longer than twelve months by 184 days (1 July to 31 December 2025).
- Laying period: ten months after 31 December 2025 is 31 October 2026. Reduce by 184 days: **30 April 2026**. This is later than the three-month floor (31 March 2026), so it stands.
- Delivery to the Registrar: 42 days after 30 April 2026 = **11 June 2026**. ([Cap. 386 art. 182(3) and 183(1)](https://legislation.mt/getpdf/6a1836349844fb1e280ec744))

**Case 5: late delivery.** Case 1's company misses the 12 December 2026 deadline for its 2025 accounts, and the default continues for 60 days after the day on which it occurs.
- Maximum administrative penalty under article 183(6): €2,329, due on the day the default occurs, plus €46 for each day the default continues, counted from the following day (art. 427(2)). Maximum = €2,329 + €46 × 60 = €2,329 + €2,760 = €5,089. The Registrar may impose less. The company is jointly and severally liable with its officers, and recovery lapses after five years. ([Cap. 386 art. 427 and Eleventh Schedule](https://legislation.mt/getpdf/6a1836349844fb1e280ec744))

**Case 6: parent company and the group test.** For this case only, assume a financial reporting period starting on or after 20 March 2026, so the higher limits apply; the default 2025-period assumption above does not apply. A parent's own figures are tiny. Its group, consolidated, has net turnover €11,000,000 net and €11,800,000 gross; balance sheet total €5,500,000 net and €5,900,000 gross; 40 employees. ([Cap. 386](https://legislation.mt/getpdf/6a1836349844fb1e280ec744))
- Net basis: turnover over €10,000,000 and total assets over €5,000,000: fails. Gross basis: turnover under €12,000,000, total assets under €6,000,000, employees under 50: passes. Either basis may be used, so it meets the current-date numerical **small-group** test (art. 185(5) and (7)), subject to the timing condition below.
- This is the current-date group result only. For a later balance sheet date, the prior-period pattern is also needed under article 185(6); no prior-period figures were supplied in this case. Only if the timing and article 173 conditions are met can the parent rely on the small-group consolidation exemption, including the exclusions for a group undertaking traded on a regulated or equivalent market and any group company that is a PIE.

## When to refuse or refer

- **PIEs, listed issuers and ESEF filers:** refer to a statutory auditor with PIE experience. Extra audit-report content (art. 179B) and electronic filing rules apply.
- **Banks, financial institutions, insurers and SICAVs:** sector rules override the Act (art. 168 and 169). Refer.
- **Sustainability reporting (CSRD):** large undertakings and PIEs may have sustainability reporting and assurance duties under S.L. 386.31. This skill does not cover them. Refer.
- **Merchant Shipping Act companies:** the tax audit waiver follows rule 7 of L.N. 139 of 2025 and S.L. 234.42. Refer.
- **Groups with overseas parents or subsidiaries**, including every condition of an article 174 consolidation exemption: Check this point with one of our partner accountants. Do not use this summary to claim that exemption.
- **Periods starting before 20 March 2026:** use the previous article 185 limits under the MBR instruction; do not early-adopt the higher limits. ([L.N. 61 of 2026](https://legislation.mt/getpdf/69dce8d06fe5fd3994d17860))
- **Review engagements** for tax: apply the MTCA-defined ISRE 2400 (Revised) standard. For professional signing eligibility and engagement-specific questions: Check this point with one of our partner accountants.
- **Refuse** to present accounts as exempt from audit, or to sign or date documents for directors, where the size test is not met or the records do not support it. Directors who approve non-compliant accounts face a penalty (art. 176(4)). Failing to keep proper records is a criminal offence with a fine of up to €11,646 (art. 163(6)). ([Cap. 386](https://legislation.mt/getpdf/6a1836349844fb1e280ec744))
- **Tax questions** (chargeable income, rates, refunds, the tax return deadline): route to the **mt-corporate-tax** skill. **VAT**: route to the **malta-vat-return** skill.

## Filing and payment
| Step | Deadline or rule | Source |
| --- | --- | --- |
| Send accounts, directors' report and auditors' report to members and debenture holders | At least fourteen days before the general meeting (or late, if all members entitled to attend agree); electronic copies allowed if members are told | [Cap. 386 art. 180](https://legislation.mt/getpdf/6a1836349844fb1e280ec744) |
| Lay accounts before the general meeting for approval | Private company: ten months after the accounting reference period ends. Public company: seven months; subject to art. 182(3)-(4) | [Cap. 386 art. 181 and 182](https://legislation.mt/getpdf/6a1836349844fb1e280ec744) |
| Deliver to the Registrar | Within forty-two days from the end of the laying period: accounts, auditors' report (if any), directors' report (if required) | [Cap. 386 art. 183(1)](https://legislation.mt/getpdf/6a1836349844fb1e280ec744) |
| Small company | Need not deliver the directors' report | [Cap. 386 art. 183(2)](https://legislation.mt/getpdf/6a1836349844fb1e280ec744) |
| Small private exempt company | Need not deliver the directors' report or the profit and loss account (and no auditors' report if also micro) | [Cap. 386 art. 183(2)](https://legislation.mt/getpdf/6a1836349844fb1e280ec744) |
| Using any filing exemption | Declaration on the prescribed form, signed by the directors who signed the balance sheet | [Cap. 386 art. 183(3)](https://legislation.mt/getpdf/6a1836349844fb1e280ec744) |
| Annual return | Made up to each anniversary of registration; filed within forty-two days after that date | [Cap. 386 art. 184](https://legislation.mt/getpdf/6a1836349844fb1e280ec744) |
| Annual return fee, company other than a SICAV, authorised capital up to €1,500 | €85 (paper: €100); higher bands rise with capital, up to €1,200 electronic over €2,500,000 | [S.L. 386.03 Schedule (i)](https://legislation.mt/getpdf/6022592ebc8272018c0ede95) |
| Registering annual accounts | Check this point with one of our partner accountants; no no-fee conclusion is supplied | [S.L. 386.03](https://legislation.mt/getpdf/6022592ebc8272018c0ede95) |
| Keep accounting records | Ten years (Companies Act). The nine-year income tax rule does not apply where article 163(5) applies, so a company keeps its records ten years | [Cap. 386 art. 163(5)](https://legislation.mt/getpdf/6a1836349844fb1e280ec744); [ITMA art. 19(5) proviso](https://legislation.mt/getpdf/69c65a5c7da36921dcc4f04b) |

- **How to file.** Electronic copies must be authenticated under article 82. The [MBR notice](https://www.mbr.mt/post/notice-to-the-public-submission-of-financial-statements-to-the-registrar), read 26 November 2026, confirms BAROS submission by 12 December 2026 for 31 December 2025 year ends. This does not verify every portal field or attachment.
- **Filing exemption wording or legislative commencement beyond the consolidated article 183(2) quoted here:** Check this point with one of our partner accountants. Do not substitute an uncommenced amendment for the operative text.

### Penalties (maximum administrative penalties, [Cap. 386 Eleventh Schedule](https://legislation.mt/getpdf/6a1836349844fb1e280ec744))

| Default | Penalty | Daily |
| --- | --- | --- |
| Failing to lay accounts, or laying non-compliant accounts (art. 181(3)) | €2,329 | €46 |
| Failing to deliver, or delivering defective, accounts to the Registrar (art. 183(6)) | €2,329 | €46 |
| Failing to file the annual return (art. 184(3)) | €2,329 | €46 |
| Directors approving non-compliant accounts (art. 176(4)) | €2,329 | None |
| Directors' report not compliant (art. 177(4)) | €1,164 | None |
| Failing to send accounts to members (art. 180(4)) | €1,164 | None |
| Records not kept for ten years (art. 163(7)) | €1,164 | None |
| Accounts issued or delivered unsigned (art. 176(5)) | €465 | None |

These are the maximums set by the Eleventh Schedule, which the Registrar may impose (art. 427(1)). The penalty is due on the day of default; the daily penalty runs from the next day. The company is jointly and severally liable with its officers (art. 427(4)).

**2025 year-ends (being filed now):** a private company with a 31 December 2025 year-end lays its accounts by 31 October 2026 and delivers them by 12 December 2026 (Case 1); rule 6 of L.N. 139 of 2025 applies to those accounts.

## Completion checklist
- [ ] Article 185 and GAPSME size tests run for this and the previous balance sheet date, figures kept on file, and the period-start transition applied under the MBR instruction.
- [ ] Board resolution on file if IFRS is chosen; comparatives on the same framework.
- [ ] Small-company exemption used: own-share information put in the notes.
- [ ] Audit decision recorded twice: Companies Act, and L.N. 139 of 2025 for tax (audit, review report, or none).
- [ ] Filing-exemption declaration and any translations delivered with the accounts.
- [ ] Annual return filed within forty-two days of the registration anniversary.
- [ ] Accounts handed to the tax preparer (see **mt-corporate-tax**).

## Executable checks of the worked cases

These checks verify arithmetic in Cases 3 and 5, not size-test eligibility, signing authority or whether the Registrar imposes the maximum.

```oa-check
name: Qualifying ten-month start-up turnover cap and capped audit deduction
inputs:
  months: 10
  annual_turnover_cap: 80000
  turnover: 50000
  audit_fee: 1000
steps:
  - period_cap: round(annual_turnover_cap * months / 12, 2)
  - headroom: period_cap - turnover
  - audit_deduction: min(audit_fee * 1.20, 700)
expected:
  period_cap: 66666.67
  headroom: 16666.67
  audit_deduction: 700
```

```oa-check
name: Sixty-day late accounts maximum administrative penalty
inputs:
  days: 60
  initial_maximum: 2329
  daily_maximum: 46
steps:
  - daily_component: days * daily_maximum
  - maximum: initial_maximum + daily_component
expected:
  daily_component: 2760
  maximum: 5089
```


## Sources

| Source actually read; scope | URL | Read on |
|---|---|---|
| Companies Act: arts. 151, 163-164, 167-185, 187, 211, 427; Eleventh Schedule relevant rows | https://legislation.mt/eli/cap/386/eng/pdf | 2026-11-26 |
| Previous article 185 company and group limits | https://legislation.mt/getpdf/695277d8cc8c701d50c749db | 2026-11-26 |
| MBR period-start transition instruction | https://www.mbr.mt/post/informative-note-entry-into-force-of-legislation-1 | 2026-11-26 |
| MBR 2025 calendar-year filing notice | https://www.mbr.mt/post/notice-to-the-public-submission-of-financial-statements-to-the-registrar | 2026-11-26 |
| GAPSME regs. 3-5 and para. 4.1: scope, size and statements; same-day completed bookkeeping size evidence reused | https://legislation.mt/eli/sl/281.5/eng/pdf | 2026-11-26 |
| GAAP, comparatives and auditing standards, regs. 3-4 | https://legislation.mt/eli/sl/281.2/eng/pdf | 2026-11-26 |
| Audit Exemption Rules, all rules | https://legislation.mt/eli/ln/2025/139/eng/pdf | 2026-11-26 |
| MTCA review-report definition and rule 6 examples | https://mtca.gov.mt/docs/default-source/documents/personal-tax/legal-and-technical/guidelines/audit-exemption-rules---guidelines.pdf?sfvrsn=14aab6d_1 | 2026-11-26 |
| ITMA art. 19(4)-(5) | https://legislation.mt/eli/cap/372/eng/pdf | 2026-11-26 |
| Auditor definition, art. 2 | https://legislation.mt/eli/cap/281/eng/pdf | 2026-11-26 |
| S.L. 386.20, marked not yet in force | https://legislation.mt/eli/sl/386.20/eng/pdf | 2026-11-26 |
| Annual-return fee table, Schedule (i) | https://legislation.mt/eli/sl/386.3/eng/pdf | 2026-11-26 |
