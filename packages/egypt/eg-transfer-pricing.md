---
name: eg-transfer-pricing
description: Use this skill whenever asked about Egyptian transfer pricing for tax year 2026, for resident companies, permanent establishments of non-resident companies and Egyptian-parented groups with domestic or cross-border related-party dealings. Covers the arm's length rule in Income Tax Law 91 of 2005 art. 30 and executive regulation arts. 38 to 40, the related-person definition (art. 1 as replaced by Law 30 of 2023), the master file, local file and country-by-country report under Unified Tax Procedures Law 206 of 2020 arts. 12 and 13 and its executive regulations, the 1%, 2% and 3% charges and their 3% cap, advance pricing agreements, the debt to equity limit and interest-rate cap that hit related-party loans. Trigger on "Egypt TP", "Egypt transfer pricing", "Master File Egypt", "Local File Egypt", "CbCR Egypt", "تسعير المعاملات", "الأشخاص المرتبطة", "الملف المحلى". ALWAYS read this skill before touching any Egypt TP work.
version: 0.2
jurisdiction: EG
tax_year: 2026
last_updated: 2026-11-02
depends_on:
  - transfer-pricing-workflow-base
category: transfer-pricing
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: transfer-pricing
---

# Egypt Transfer Pricing (تسعير المعاملات بين الأشخاص المرتبطة) Skill v0.2

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

This skill covers Egyptian transfer pricing (TP) for tax year 2026 (calendar year, or the company's financial year). The Egyptian Tax Authority (ETA, مصلحة الضرائب المصرية) administers it. Reply in the user's language, English or Arabic. All amounts are in EGP. It loads on top of `transfer-pricing-workflow-base`; the output is working papers and a brief for a reviewer, not a filed return.

## Who this applies to

- **The arm's length rule** (Law 91 art. 30): where related persons set conditions in their commercial or financial dealings that differ from those between independent parties, and this reduces the tax base or shifts the tax burden from a taxable to an exempt or non-taxable person, ETA may set taxable profit on the arm's length price. It applies to domestic and cross-border dealings alike.
- **Related person (الشخص المرتبط)** (Law 91 art. 1, as replaced by Law 30/2023 art. 1): anyone linked to the taxpayer by a relationship that affects the tax base directly or indirectly, through management, control or ownership, so that one can act on the directions, requests, proposals or will of the other or of a third person. Always related:
  1. husband, wife, ascendants and descendants;
  2. a partnership and its general and limited partners;
  3. a capital company and a person owning, directly or indirectly, at least 50% of its voting or management rights, profit rights or capital rights;
  4. two or more companies in which another person owns at least 50% of those rights.
  For items 2 to 4, a holding attributed to one person through a related person may not be attributed again to another related person. Being an employee or client of another does not by itself make two persons related, unless the link affects the tax base. The executive regulations of Law 206 repeat this definition (MoF decree 286/2021, definitions article).
- **Who documents** (Law 206 art. 12; ER 206 art. 14): every person with commercial or financial transactions with related persons, including permanent establishments of non-resident legal persons. Transactions include sales and purchases of goods and services, assets, expense recharges, royalties, loans of every kind including credit facilities, securities, contracts and intangibles.
- **Not here:** the corporate tax computation (`eg-corporate-tax`); withholding on payments to non-residents (`eg-withholding-tax`); residence, permanent establishment and treaty relief (`eg-cross-border`).

## Rates, bands and thresholds

| Item | Amount | Conditions | Tax year | Official URL |
|---|---|---|---|---|
| Documentation set | Master file, local file and country-by-country report or notification | Required of every person with related-party commercial or financial transactions (Law 206 art. 12 first para.) | 2026 | https://eta.gov.eg/sites/default/files/2024-03/law_no.206-2020.pdf |
| Exemption from master file and local file | Total related-party transactions in the tax period not over EGP 8,000,000 | Law 206 art. 12 fourth para.; the Minister may raise the figure by decision. Measured on gross related-party income plus expenses, not the net (ER 206 art. 14). The exemption covers only the master file and local file (art. 12 fourth para. names items (a) and (b)); the art. 30 arm's length rule, the disclosure in the return and the CbC report or notification still apply. The figure in force after any ministerial decision is on "Not yet confirmed" | 2026 | same |
| Country-by-country report, Egyptian-parented group | Consolidated group revenue of EGP 3 billion or more, and at least one foreign subsidiary | ETA TP Guidelines 2018 s. 5.5 and 5.8; the Minister or his delegate may exempt a company from the CbC report in line with international practice (Law 206 art. 12 second para.) | 2026 | https://www.eta.gov.eg/sites/default/files/2026-03/egyptian-transfer-pricing-en-guidelines-2019-view.pdf |
| Country-by-country report, foreign-parented group | Consolidated group revenue of EUR 750 million or more; report filed in the parent's country | ETA TP Guidelines 2018 s. 5.5 and 5.8; the report or notification duty on all legal persons, free zone companies and PEs is in ER 206 art. 14 | 2026 | same |
| Non-disclosure in the return | 1% of the undisclosed related-party transactions | Law 206 art. 13 last para. as replaced by Law 211/2020; due even if the transactions appear in the local or master file (ER 206 art. 16) | 2026 | https://eta.gov.eg/sites/default/files/2026-05/law_no.211-2020.pdf |
| Local file not filed | 3% of related-party transactions | Same article; base is total related-party transactions (ER 206 art. 18) | 2026 | same |
| Master file not filed | 3% of related-party transactions | Same article and base | 2026 | same |
| Country-by-country report or notification not filed | 2% of related-party transactions | Same article and base | 2026 | same |
| Cap where several failures combine | 3% of related-party transactions | Same article, last sentence | 2026 | same |
| Debt to equity limit, tax year 2026 | Interest on loans above 3 times average equity is not deductible | Law 30/2023 art. 5 (transition: 4:1 for 2023, 3:1 for 2024 to 2027, 2:1 for 2028); permanent rule is 2 times average equity (Law 91 art. 52 item 1, as replaced by Law 151/2026). Equity per Egyptian Accounting Standards financial statements. Not for banks, insurers and finance companies named by the Minister | 2026 | https://eta.gov.eg/sites/default/files/2024-03/law_no.30-2023.pdf |
| National infrastructure projects | 4 times average equity | Loans from unrelated lenders, projects named by Prime Minister decision, company's share at least 25% of its investments; ends when the term of the loans for carrying out the project's main works ends (Law 91 art. 52 item 1 second para., Law 151/2026, as corrected by the Gazette erratum of 8 Aug 2026) | From 29 Jul 2026 | https://eta.gov.eg/sites/default/files/2026-08/law.no_.151.of_.2026.pdf |
| Interest rate cap | Interest above twice the Central Bank credit and discount rate on 1 January of the year in which the tax period ends is not deductible; 2 x 20.50% = 41% for a period ending in 2026 | Law 91 art. 24 item 4 (2005 text); rate from ETA circular 1/2026 | 2026 | https://eta.gov.eg/sites/default/files/2026-03/Dawry.no_.1.of_.2026.pdf |

## The base

**Methods** (ER 91 art. 39, as replaced by MoF decree 221/2018; text as printed in the ETA Guidelines): comparable uncontrolled price (CUP), cost plus, resale price, profit split, and transactional net margin (TNMM). **Choice** (ER 91 art. 40, same decree): the taxpayer applies the method that fits the nature and conditions of the transaction; if none fits, any other method, provided documents and records support it. The Guidelines work on the most appropriate method (s. 4, p. 42), with CUP preferred for commodities and quoted-price goods (p. 44) and resale price usually suited to distributors (p. 48). The pre-2018 text gave CUP first priority; that hierarchy is gone. ETA treats the Minister's guidelines as its basic reference (art. 40).

**Scope of the check** (ER 91 art. 38, same decree): exchange of goods and services, allocation of shared expenses, royalties, interest and any other commercial or financial transaction. The Guidelines read "financial transactions" to include share transfers, loans and guarantees (p. 12, note 5).

**Comparables** (Guidelines s. 5.7.3.1, p. 65): search Egyptian comparables first, then Middle East and Africa, then global; disclose the search strategy in the local file. Differences that affect price or margin are adjusted. Where comparables leave unquantified defects, statistical tools narrow the range (p. 84). ETA audits with a specialised financial database (p. 65, note 17).

**Documents, in the four steps** (Guidelines s. 5.7): master file (group structure, business and supply chain, five largest products or services, intangibles and their owners, intra-group financing, consolidated accounts and existing APAs or rulings); local file (local business and industry, controlled transactions with contracts and amounts by country, functional analysis, method choice and reasons, comparability study, adjustments, financial calculations, segmented accounts and profitability against the range, ideally three years). Local files are entity by entity, not one file for several Egyptian companies. The Guidelines leave intangibles, intra-group services and cost contribution arrangements to separate guidance (p. 11). A filing that lacks the sections the Minister's guide prescribes does not count as filed (ER 206 art. 19).

**When nothing is filed** (Law 206 art. 12 third para.; ER 206 art. 14): ETA may set pricing rules it considers suitable from the information it has; the taxpayer may object, and then carries the burden of proof (Law 206 art. 40).

**Financial transactions.** Apply the debt to equity limit and the rate cap from the table, then test the rate itself at arm's length. Interest on loans of any kind paid to natural persons who are not taxable or are exempt is not deductible (Law 91 art. 24 item 5). Dividends, board remuneration and employees' profit share are not deductible costs of a legal person (art. 52 items 3 to 5).

## Deadlines and filing

| Step | Rule | Source |
|---|---|---|
| Disclose related-party transactions | In the annual corporate return, in the form's tables | Law 206 art. 13 last para.; ER 206 art. 16 |
| Corporate return | Before 1 May, or within four months after the financial year end | Law 206 art. 31(c) |
| Local file | Within two months after the date the annual return is filed | Law 206 art. 13(b) |
| Master file | On the parent's filing date in the parent's country; if the parent is in Egypt, or its country does not require a master file, by the local file deadline | Law 206 art. 13(a); ER 206 art. 15 |
| Country-by-country report | Within one year after the end of the tax year | Law 206 art. 13(c); first report for financial years ending 31 Dec 2018 (Guidelines s. 5.9) |
| Records | Keep books, records and documents for five years after the period the return covers | Law 206 art. 38 third para. (Law 150/2026 replaced only the first para.) |
| Information requests | Provide data and documents within 15 days of a written request; the ETA head may extend once by the same period | Law 206 art. 41 |
| Penalty demand | ETA claims the TP charge on form 3 سداد | ER 206 art. 17 |

**APA** (Law 91 art. 30 second para.; ER 91 art. 40; Guidelines Part Two): the ETA Commissioner may agree one or more methods in advance. Unilateral, bilateral and multilateral APAs exist; bilateral and multilateral ones run through the treaty mutual agreement article. Steps: written request for a pre-filing meeting at least six months before the covered period starts (form 1 APA); formal application on form 2 APA within two months of ETA's notice after that meeting; ETA review and negotiation; signature; annual compliance report. ETA puts a unilateral APA at three to six months. APA documents should ideally be in English and Arabic; English may be filed first and ETA says if an Arabic version is needed (p. 97). Term depends on the case and can be renewed; a missed critical assumption can lead to revision or cancellation and a TP audit (pp. 91 to 97). Open to all taxpayers, PEs included.

**Steps for a 2026 local file:**
1. Total related-party income and expenses for the year (gross) and test the exemption threshold.
2. Fill the related-party tables in the corporate return on the ETA portal (https://workspace.eta.gov.eg/workspace/dashboard) and file before 1 May (calendar year).
3. Build the local file on the Guidelines' four steps and the Minister's guide; file it with ETA's TP department within two months of the return.
4. Obtain the group master file and file it by its date; check whether the group meets a CbCR threshold.

## Penalties and interest

| Failure | Consequence | Source |
|---|---|---|
| TP documentation failures | 1%, 3%, 3%, 2%, capped at 3% of related-party transactions (table above) | Law 206 art. 13, Law 211/2020 |
| Other sanctions | Paying the TP charge does not stop other fines or penalties under the law (ER 206 art. 20). Breach of arts. 12 or 13 is itself an offence: fine EGP 3,000 to 50,000 on top of the tax due, tripled on repeat | ER 206 art. 20; Law 206 art. 69(d) |
| Tax from a TP adjustment paid late | Delay charge at the Central Bank rate plus 2% a year (`eg-income-tax`), capped at 100% of the principal tax | Law 91 art. 110; Law 206 art. 45 bis (Law 7/2025) |
| Assessment window | Five years from the end of the statutory return deadline; interrupted by notice of assessment, demand or referral to appeal committees | Law 206 art. 44 as replaced by Law 211/2020 (the six-year evasion limb of the 2020 text was dropped) |
| Wrong return, obstruction, evasion | Fines and prison under Law 206 arts. 69 to 72; settlement possible under arts. 75, 75 bis | Law 206; Law 7/2025 |

## Cross-border points

- Payments to non-resident related persons also carry withholding (Law 91 art. 56) and dividend tax (art. 56 bis); see `eg-withholding-tax` and `eg-cross-border`.
- Bilateral and multilateral APAs and relief from double taxation after an adjustment run through the treaty's mutual agreement article; the ETA treaty list is in `eg-cross-border`.
- Egypt is a member of the OECD Inclusive Framework on BEPS and its Guidelines endorse the OECD Transfer Pricing Guidelines' documentation principles (Guidelines p. 11).
- CbC reports of foreign-parented groups reach ETA through automatic exchange between tax administrations (Guidelines s. 5.5); Law 206 art. 78 lets ETA exchange information with treaty partners.

## Two worked examples that recompute

**Case 1. Several documentation failures in one year.** Company with EGP 50,000,000 of related-party transactions in 2026. It left EGP 10,000,000 of them out of the return and never filed the local file. Non-disclosure: 1% x 10,000,000 = 100,000. Local file: 3% x 50,000,000 = 1,500,000. Sum 1,600,000, but the cap is 3% x 50,000,000 = 1,500,000. Charge: 1,500,000.

```oa-check
name: TP charges with the 3% cap, transactions EGP 50m
inputs:
  rpt_total: 50000000
  undisclosed: 10000000
steps:
  - nondisclosure: undisclosed * 0.01
  - local_file: rpt_total * 0.03
  - uncapped: nondisclosure + local_file
  - cap: rpt_total * 0.03
  - charge: min(uncapped, cap)
expected:
  nondisclosure: 100000.00
  local_file: 1500000.00
  charge: 1500000.00
```

**Case 2. Decision: fund with a group loan or with equity.** Average equity EGP 10,000,000. Option A: group loan of 45,000,000 at 10% (interest 4,500,000; 10% is under the 41% rate cap). 2026 limit is 3 x 10,000,000 = 30,000,000, so 30/45 of the interest is deductible: 3,000,000; 1,500,000 is disallowed. Option B: inject 15,000,000 as equity and borrow 30,000,000: average equity 25,000,000 (if held all year), limit 75,000,000, interest 3,000,000 all deductible. The same loan in 2028 at 2:1 would allow only 20/45, so plan for the step-down.

```oa-check
name: Debt to equity 3:1 in 2026, loan against equity funding
inputs:
  equity_a: 10000000
  loan_a: 45000000
  equity_b: 25000000
  loan_b: 30000000
  rate: 0.10
steps:
  - interest_a: loan_a * rate
  - deductible_a: interest_a * min(1, (3 * equity_a) / loan_a)
  - disallowed_a: interest_a - deductible_a
  - interest_b: loan_b * rate
  - deductible_b: interest_b * min(1, (3 * equity_b) / loan_b)
  - deductible_a_2028: interest_a * min(1, (2 * equity_a) / loan_a)
expected:
  deductible_a: 3000000.00
  disallowed_a: 1500000.00
  deductible_b: 3000000.00
  deductible_a_2028: 2000000.00
```

Disallowing interest on the excess loan at the loan rate gives the same figure as the proportional split above when one rate applies. How equity and average loans are measured (Executive Regulations arts. 58 and 59) is set out in `eg-corporate-tax`.

## Ask the client first

1. Total related-party income and expenses for 2026, gross, and who the related persons are (which test in art. 1).
2. Financial year end and the date the corporate return was or will be filed.
3. Group structure: parent's country, consolidated revenue, whether the parent files a master file and a CbC report.
4. Related-party loans: amounts, rates, average equity, any national infrastructure project.
5. Any APA, ruling or open TP audit, and documents already filed for earlier years.

Refuse to help price transactions to shift profit, backdate documentation or hide related-party dealings. Do not present output as a filed local file or a professional sign-off.

## Sources

| Source | URL | Read on |
|---|---|---|
| Income Tax Law 91 of 2005, original text: arts. 1, 2, 24 items 4 and 5, 30, 47, 52, 54, 56 (page images read; pp. 6 to 8, 18, 30 to 35 of the Gazette) | https://eta.gov.eg/sites/default/files/2024-03/law_no.91-2005.pdf | 2026-11-02 |
| Law 30 of 2023: art. 1 (art. 1 related person, art. 4, art. 52 item 1, art. 56 third para., art. 56 bis), art. 2 (art. 4 bis), arts. 5, 6, 12 (text layer read) | https://eta.gov.eg/sites/default/files/2024-03/law_no.30-2023.pdf | 2026-11-02 |
| Law 151 of 2026, arts. 1, 2, 6, 7 (art. 52 item 1, art. 56 fourth para.; text layer read); Gazette 30 bis (a), 28 Jul 2026 | https://eta.gov.eg/sites/default/files/2026-08/law.no_.151.of_.2026.pdf | 2026-11-02 |
| Gazette erratum to Laws 149, 150 and 151 of 2026, Gazette 32 bis, 8 Aug 2026 (page images read; corrects art. 52 item 1 and art. 56 fourth para.) | https://eta.gov.eg/sites/default/files/2026-08/law.no_.149.150.151.of_.2026.retractation.pdf | 2026-11-02 |
| Law 150 of 2026 amending Law 206 (art. 38 first para., art. 27 bis; text layer read) | https://eta.gov.eg/sites/default/files/2026-08/law.no_.150.of_.2026.pdf | 2026-11-02 |
| Unified Tax Procedures Law 206 of 2020: arts. 12, 13, 31, 33, 38, 40, 41, 44, 53, 68 to 81 (page images read) | https://eta.gov.eg/sites/default/files/2024-03/law_no.206-2020.pdf | 2026-11-02 |
| Law 211 of 2020: arts. 1 to 3 (art. 13 last para., arts. 44, 70, 73, 73 bis, 74 bis; text layer read) | https://eta.gov.eg/sites/default/files/2026-05/law_no.211-2020.pdf | 2026-11-02 |
| Law 7 of 2025, whole text (arts. 45 bis, 75 bis, 75 bis 1) | https://eta.gov.eg/sites/default/files/2025-02/law_no.7.of_.2025.pdf | 2026-11-02 |
| MoF decree 286 of 2021, executive regulations of Law 206: definitions and arts. 13 to 21 (text layer read) | https://eta.gov.eg/sites/default/files/2024-03/law_no.286-2021.pdf | 2026-11-02 |
| ETA Egyptian Transfer Pricing Guidelines (2018 edition, file dated 2019): pp. 11 to 13 (law and ER arts. 30, 38 to 40, decree 221/2018 note), 42 to 48, 61 to 67, 84, 91 to 97 | https://www.eta.gov.eg/sites/default/files/2026-03/egyptian-transfer-pricing-en-guidelines-2019-view.pdf | 2026-11-02 |
| ETA circular 1 of 2026, Central Bank rates on 1 January (page image read) | https://eta.gov.eg/sites/default/files/2026-03/Dawry.no_.1.of_.2026.pdf | 2026-11-02 |
| ETA income tax laws page, read for the list of instruments ETA publishes | https://www.eta.gov.eg/ar/content/qwanyn-aldrybt-ly-aldkhl | 2026-11-02 |

Not yet confirmed: the documentation threshold in force for 2026 (the law says EGP 8,000,000 and lets the Minister raise it; MoF decisions reported as 52/2024 raising it to EGP 15,000,000 and 534/2025 of 17 Dec 2025 raising it to EGP 30,000,000 were not found on eta.gov.eg and were not read; the old skill used EGP 15,000,000). The number and date of the ministerial decree that issued the TP Guidelines (the old skill said 547/2018; the ETA file does not print it). The ETA Explanatory Instructions 78 of 2023 on TP and the Minister's documentation guide (not found on eta.gov.eg). Whether a revised return filed within 30 days of the deadline (Law 206 art. 33) moves the local file deadline. The CbC notification deadline, and whether an Egyptian subsidiary must file the CbC report locally when the parent's country does not exchange it (the old skill said it may). Whether the TP charge also carries the delay charge. Whether the 2:1 base rule in Law 151/2026 or the 3:1 transition in Law 30/2023 art. 5 governs a period straddling 29 Jul 2026 (this skill applies the transition, which Law 151 did not repeal). Whether art. 24 item 4 was amended after 2005. Corresponding adjustments: no domestic provision was found. Documentation language (the old skill said Arabic, English accepted). Safe harbours for low-value services or interest, the benefit test for intra-group services, APA roll-back and fees: none found in the texts read. The "no secret comparables" statement (from the OECD country profile, a secondary source).

> Contributed by Ahmed Hassan.
