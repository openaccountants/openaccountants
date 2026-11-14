---
name: india-transfer-pricing
description: "Use this skill whenever asked about India transfer pricing for FY 2026-27 (tax year 2026-27 under the Income-tax Act 2025), documentation, or CBDT transfer pricing compliance. Trigger on phrases like transfer pricing India, Indian TP documentation, Form No. 48, Form 3CEB, master file India, Form No. 56, local file India, CbCR India, Form No. 59, APA India, Section 92, section 161, safe harbour India, Form No. 49, specified domestic transactions, secondary adjustment, or any question about intercompany pricing for Indian entities. It covers Chapter X (sections 161 to 173), section 511, rules 77 to 124 of the Income-tax Rules 2026, associated enterprise tests, methods and the 35th to 65th percentile range, documentation, Form No. 48, master file and country-by-country thresholds, the 2026-27 safe harbour table, APAs, penalties and fees. Tier 2, not reviewed by an accountant."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/india-transfer-pricing"
  jurisdiction: "IN"
  tax_year: "2026"
  last_updated: "2026-11-14"
---

# India Transfer Pricing, FY 2026-27

> **General reference only.** This skill is general tax reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts. Do not rely on it to file, pay or take a tax position without review by a qualified professional in India.

This skill covers Indian transfer pricing: which transactions are caught, how the arm's length price is set, the documents to keep, the accountant's report, the master file, the country-by-country report, safe harbours, advance pricing agreements and the penalties and fees. Tax year: FY 2026-27, the tax year from 1 April 2026 to 31 March 2027 under the Income-tax Act 2025, which replaced the Income-tax Act 1961 from 1 April 2026. The transfer pricing rules now sit in Chapter X of the 2025 Act (sections 161 to 173), in section 511 (country-by-country report) and in rules 77 to 124 of the Income-tax Rules 2026. Section, rule and form numbers all changed. For income years up to 2025-26 (assessment year 2026-27 and earlier), the 1961 Act still applies and this skill does not cover it.

## Who this applies to

| Field | Value |
| --- | --- |
| Country | India (Republic of India) |
| Tax authority | Central Board of Direct Taxes (the Board); Assessing Officer; Transfer Pricing Officer (section 166) |
| Main law | Income-tax Act 2025 (30 of 2025), Chapter X, sections 161 to 173; section 511 (country-by-country report); penalties in sections 439, 442, 457 and 459; fees in section 428 as substituted by the Finance Act 2026 |
| Rules | Income-tax Rules 2026 (G.S.R. 198(E) of 20 March 2026, in force 1 April 2026), rules 77 to 124 |
| Accountant's report | Form No. 48 under section 172 (rule 85) |
| Documentation | Rule 84 (transaction documentation, the "local file"); rule 123 and Form No. 56 (master file) |
| Country-by-country report | Section 511; rule 124; Forms No. 58, 59 and 60 |
| Safe harbour | Section 167; rules 86 to 93 (international) and 94 to 98 (specified domestic transactions); Form No. 49 |
| Advance pricing agreement | Sections 168 and 169; rules 103 to 122; Forms No. 50, 51, 52 and 54 |
| Tax year | 1 April to 31 March; tax year 2026-27 returns are due in 2027 |
| Currency | INR |

### International transactions and specified domestic transactions

Section 161(1) of the 2025 Act says income from an international transaction or a specified domestic transaction is determined "having regard to the arm's length price". Section 161(2) applies the same rule to any allowance for an expense or interest. Section 161(4) switches the section off where the result would reduce the income chargeable or increase the loss computed from the books. So a transfer pricing adjustment can only increase income.

An international transaction (section 163(1)) is a transaction between two or more associated enterprises, "one of which is necessarily a non-resident". It includes the purchase, sale, transfer, lease or use of tangible or intangible property and the other items listed in section 163. Section 163(2) also treats a transaction with a person who is not an associated enterprise as an international transaction between associated enterprises if there is a prior agreement about it between that person and the associated enterprise, or its terms are in substance decided between them, and the enterprise or the associated enterprise or both are non-residents, whether or not the other person is a non-resident. A specified domestic transaction (section 164) covers the domestic related-party transactions listed in that section (for example transactions referred to in section 122 and transfers of goods or services referred to in section 140(9)). It applies only where their aggregate in the tax year is more than the amount in the rates table. At or below that amount, the transactions are not specified domestic transactions at all.

### Associated enterprises (section 162)

An enterprise is an associated enterprise of another if any one of the tests in section 162(1) applies. They include common participation in management, control or capital, and the numeric tests in the rates table. Section 162(1) also covers board appointments (more than half of the board, or one or more executive directors), whole dependence on the other's know-how, patents or other rights, sales influenced by the other, common control by an individual or a Hindu undivided family and their relatives, and "any relationship of mutual interest" as prescribed.

### Interaction with other skills

| Related skill | Interaction |
| --- | --- |
| `india-financial-statements` | Company accounts under the Companies Act 2013 support the documentation and the master file |
| `india-gst` | Related-party supplies also raise GST valuation questions; GST is not covered here |
| `india-income-tax` | Return due dates and fees for individuals; this skill covers the transfer pricing layer only |

No live skill in this library covers Indian corporate income tax. For company rates and the return itself, refer to a professional.

## Rates, bands and thresholds

Every figure for tax year 2026-27, with the official text on the row. Quotes come from the Gazette text of the Act and the Finance Act 2026 and from the Income-tax Rules 2026.

### Associated enterprise tests and the specified domestic transaction threshold

| Item | Value | Note | Source |
| --- | --- | --- | --- |
| Shareholding test, section 162(1)(a)(ii) and (iii): voting power held at any time in the tax year, directly or indirectly, of not less than | 26% | "shares carrying not less than 26% of the voting power in the other enterprise" | https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Loan test, section 162(1)(b): loan from the other enterprise of not less than this share of the book value of total assets | 51% | "such loan constitutes not less than 51% of the book value of the total assets" | https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Guarantee test, section 162(1)(c): guarantees not less than this share of total borrowings | 10% | "which guarantees not less than 10% of the total borrowings of the other enterprise" | https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Supply test, section 162(1)(g): this share or more of raw materials and consumables supplied by the other enterprise, with prices influenced by it | 90% | "90% or more of the raw materials and consumables required for the manufacture" | https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Firm or association test, section 162(1)(k): the other enterprise holds not less than this interest | 10% | "holds not less than 10% interest in such firm, association of persons" | https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Specified domestic transactions, section 164: caught only where the aggregate in the tax year exceeds | twenty crore rupees | "aggregate of such transactions entered into by the assessee in a tax year exceeds a sum of twenty crore rupees" | https://egazette.gov.in/WriteReadData/2025/265620.pdf |

### Documentation (rule 84)

| Item | Value | Note | Source |
| --- | --- | --- | --- |
| Rule 84(2): no rule 84(1) documentation where aggregate international transactions in the tax year do not exceed | one crore rupees | "international transactions entered into by the assessee during the tax year does not exceed one crore rupees" | https://www.incometax.gov.in/iec/foportal/sites/default/files/2026-03/En-Notified-IT-Rules-2026-20-03-2026.pdf |
| Rule 84(8): retention period from the end of the relevant tax year | nine years | "kept and maintained for a period of nine years from the end of the relevant tax year" | https://www.incometax.gov.in/iec/foportal/sites/default/files/2026-03/En-Notified-IT-Rules-2026-20-03-2026.pdf |

### Accountant's report (rule 85)

| Item | Value | Note | Source |
| --- | --- | --- | --- |
| Form for the section 172 report (rule 85(1)) | Form No. 48 | "shall be in Form No. 48 and be verified in the manner indicated therein" | https://www.incometax.gov.in/iec/foportal/sites/default/files/2026-03/En-Notified-IT-Rules-2026-20-03-2026.pdf |
| Rule 85(2): furnished at least this long before the return due date under section 263(1)(c) | one month | "shall be furnished at least one month prior to the due date of furnishing return of income" | https://www.incometax.gov.in/iec/foportal/sites/default/files/2026-03/En-Notified-IT-Rules-2026-20-03-2026.pdf |

### Master file (rule 123)

| Item | Value | Note | Source |
| --- | --- | --- | --- |
| Test (a): consolidated group revenue for the accounting year exceeds | five hundred crore rupees | "consolidated financial statement of the international group for the accounting year, exceeds five hundred crore rupees" | https://www.incometax.gov.in/iec/foportal/sites/default/files/2026-03/En-Notified-IT-Rules-2026-20-03-2026.pdf |
| Test (b)(i): aggregate international transactions in the accounting year exceed | fifty crore rupees | "during the accounting year, as per the books of account, exceeds fifty crore rupees" | https://www.incometax.gov.in/iec/foportal/sites/default/files/2026-03/En-Notified-IT-Rules-2026-20-03-2026.pdf |
| Test (b)(ii), the alternative: intangible property transactions in the accounting year exceed | ten crore rupees | "use of intangible property during the accounting year, as per the books of account, exceeds ten crore rupees" | https://www.incometax.gov.in/iec/foportal/sites/default/files/2026-03/En-Notified-IT-Rules-2026-20-03-2026.pdf |
| Master file form (rule 123(2)) | Form No. 56 | "to the Joint Director referred to in rule 124(1), in Form No. 56" | https://www.incometax.gov.in/iec/foportal/sites/default/files/2026-03/En-Notified-IT-Rules-2026-20-03-2026.pdf |
| Designation of one filing entity (rule 123(4)) | Form No. 57 | "conveyed in Form No. 57 to the Joint Director referred to in rule 124(1)" | https://www.incometax.gov.in/iec/foportal/sites/default/files/2026-03/En-Notified-IT-Rules-2026-20-03-2026.pdf |

### Country-by-country report (rule 124)

| Item | Value | Note | Source |
| --- | --- | --- | --- |
| Threshold for section 511(8) (rule 124(7)) | six thousand four hundred crore rupees | "total consolidated group revenue of the international group shall be six thousand four hundred crore rupees" | https://www.incometax.gov.in/iec/foportal/sites/default/files/2026-03/En-Notified-IT-Rules-2026-20-03-2026.pdf |
| Notification form, due two months before the report due date (rule 124(2)) | Form No. 58 | "shall be made in Form No. 58 two months prior to the due date for furnishing of report" | https://www.incometax.gov.in/iec/foportal/sites/default/files/2026-03/En-Notified-IT-Rules-2026-20-03-2026.pdf |
| Report form (rule 124(3)) | Form No. 59 | "furnish the report referred to in section 511(2) in Form No. 59" | https://www.incometax.gov.in/iec/foportal/sites/default/files/2026-03/En-Notified-IT-Rules-2026-20-03-2026.pdf |
| Constituent entity filing period (rule 124(4)) | twelve months | "shall be twelve months from the end of the reporting accounting year" | https://www.incometax.gov.in/iec/foportal/sites/default/files/2026-03/En-Notified-IT-Rules-2026-20-03-2026.pdf |
| Designated constituent entity information (rule 124(6)) | Form No. 60 | "regarding the designated constituent entity shall be furnished in Form No. 60" | https://www.incometax.gov.in/iec/foportal/sites/default/files/2026-03/En-Notified-IT-Rules-2026-20-03-2026.pdf |

### Tolerance (rule 81)

| Item | Value | Note | Source |
| --- | --- | --- | --- |
| Rule 81(7)(b): ceiling on the notified tolerance, as a share of the actual price | 3% | "such percentage, not exceeding 3% of the latter, as may be notified in this behalf by the Central Government" | https://www.incometax.gov.in/iec/foportal/sites/default/files/2026-03/En-Notified-IT-Rules-2026-20-03-2026.pdf |

### Secondary adjustment (section 170)

| Item | Value | Note | Source |
| --- | --- | --- | --- |
| Section 170(1): primary adjustment that triggers a secondary adjustment | one crore rupees or more | "primary adjustment of one crore rupees or more to the transfer price" | https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Section 170(5): optional additional income-tax on excess money not repatriated | 18% | "pay additional income-tax at the rate of 18% on such excess money" | https://egazette.gov.in/WriteReadData/2025/265620.pdf |

| Item | Value | Note | Source |
| --- | --- | --- | --- |
| Finance Act 2026, section 3(6): surcharge on tax under section 170(5), for the tax year from 1 April 2026 | 12% | "calculated at the rate of 12% of such tax" | https://egazette.gov.in/WriteReadData/2026/271439.pdf |

### Return due dates (section 263(1)(c) as substituted)

| Item | Value | Note | Source |
| --- | --- | --- | --- |
| Return due date where section 172 applies (Table serial 1, including partners of such a firm) | 30 November | "partners Where the 30th November. of the firm or the spouse of such provisions of partner (if section 10 applies to section 172" (the table decodes interleaved) | https://egazette.gov.in/WriteReadData/2026/271439.pdf |
| Return due date for a company where section 172 does not apply (serial 2) | 31 October | "Company; Where the 31st October. provisions of (ii) assessee (other than a section 172 company)" (interleaved) | https://egazette.gov.in/WriteReadData/2026/271439.pdf |

### Penalties and fees

| Item | Value | Note | Source |
| --- | --- | --- | --- |
| Section 428(d): fee for failing to furnish the section 172 report (Form No. 48), delay up to one month | INR 50,000 | "₹ 50000 for a delay up to one month for which such failure continues" | https://egazette.gov.in/WriteReadData/2026/271439.pdf |
| Section 428(d): fee after the first month | INR 100,000 | "₹ 100000 thereafter" | https://egazette.gov.in/WriteReadData/2026/271439.pdf |

| Item | Value | Note | Source |
| --- | --- | --- | --- |
| Section 442(1): per transaction, for failing to keep the section 171(1) documents, failing to report the transaction, or maintaining or furnishing incorrect information or documents | 2% | "penalty of 2% of the value of each international transaction or specified domestic" | https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Section 442(2): failing to furnish the master file information under section 171(4) | INR 500,000 | "may impose a penalty of ₹500000 on a person, if he fails to furnish" | https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Section 457: failing to furnish information or documents required under section 171(2), for each such failure | 2% | "a penalty equal to 2 % of the value of such transaction" | https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Section 459(1)(a): reporting entity that fails to furnish the country-by-country report, per day, failure up to one month | INR 5,000 | "₹5000 for every day for which the failure continues, if the period of" | https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Section 459(1)(b): per day beyond one month | INR 15,000 | "₹15000 for every day for which the failure continues beyond the period" | https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Section 459(2): failing to produce information under section 511(7) in time, per day | INR 5,000 | "a penalty of ₹5000 for every day during which the failure continues" | https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Section 459(3): per day where the failure continues after a penalty order is served | fifty thousand rupees | "may impose penalty of fifty thousand rupees for every day for which such failure continues" | https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Section 459(4): inaccurate country-by-country report, in the cases listed | INR 500,000 | "may impose on such entity, a penalty of ₹500000, if" | https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Section 439(9): penalty on under-reported income | 50% | "shall be 50% of the tax payable on under-reported income" | https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Section 439(10): where the under-reporting results from misreporting | 200% | "shall be 200% of the tax payable on under-reported income" | https://egazette.gov.in/WriteReadData/2025/265620.pdf |

| Item | Value | Note | Source |
| --- | --- | --- | --- |
| Section 440(1)(b): additional income-tax in place of the misreporting penalty, as a share of tax payable on under-reported income | 100% | "additional income-tax amounting to 100% of the amount of tax payable on under-reported income has been paid" | https://egazette.gov.in/WriteReadData/2026/271439.pdf |

### Advance pricing agreement fees

| Item | Value | Note | Source |
| --- | --- | --- | --- |
| Application fee, rule 106(1) and (4), one fee whatever the type of agreement | twenty lakh rupees | "along with requisite fee of twenty lakh rupees for entering into an agreement" | https://www.incometax.gov.in/iec/foportal/sites/default/files/2026-03/En-Notified-IT-Rules-2026-20-03-2026.pdf |
| Additional fee for a rollback request (rule 111(5)) | INR 500,000 | "with proof of payment of an additional fee of ₹ 500000" | https://www.incometax.gov.in/iec/foportal/sites/default/files/2026-03/En-Notified-IT-Rules-2026-20-03-2026.pdf |
| Rollback years (rule 103(j)) | four tax years | "falling within the period not exceeding four tax years, preceding the first of the tax years" | https://www.incometax.gov.in/iec/foportal/sites/default/files/2026-03/En-Notified-IT-Rules-2026-20-03-2026.pdf |

### Safe harbour, block of three tax years from 2026-27 (rule 89)

| Item | Value | Note | Source |
| --- | --- | --- | --- |
| Serial 1, provision of information technology services: operating profit margin on operating expense not less than | 15.5% | "operating expense incurred is not less than 15.5%, where the aggregate operating revenue" | https://www.incometax.gov.in/iec/foportal/sites/default/files/2026-03/En-Notified-IT-Rules-2026-20-03-2026.pdf |
| Serial 1: aggregate operating revenue of the transaction in the tax year not more than | two thousand crore rupees | "does not exceed a sum of two thousand crore rupees" | https://www.incometax.gov.in/iec/foportal/sites/default/files/2026-03/En-Notified-IT-Rules-2026-20-03-2026.pdf |
| Serial 2, intra-group loan in rupees: one-year State Bank of India marginal cost of funds lending rate on 1 April, plus a spread by the associated enterprise's credit rating | 175 basis points, 325 basis points, 475 basis points or 625 basis points | "(i) 175 basis points, where the associated enterprise has credit" (AAA to A; BBB-, BBB or BBB+; BB to B; C to D) | https://www.incometax.gov.in/iec/foportal/sites/default/files/2026-03/En-Notified-IT-Rules-2026-20-03-2026.pdf |
| Serial 2, no credit rating available and total rupee loans to all associated enterprises not more than one hundred crore rupees on 31 March | 425 basis points | "(v) 425 basis points, where credit rating of the associated enter- prise is not available" | https://www.incometax.gov.in/iec/foportal/sites/default/files/2026-03/En-Notified-IT-Rules-2026-20-03-2026.pdf |
| Serial 3, intra-group loan in foreign currency: reference rate on 30 September plus a spread by rating and size (total loans up to, or above, two hundred and fifty crore rupees) | 150 to 600 basis points | "(i) 150 basis points, where the associated enterprise has a credit rating of AAA" | https://www.incometax.gov.in/iec/foportal/sites/default/files/2026-03/En-Notified-IT-Rules-2026-20-03-2026.pdf |
| Serial 4, corporate guarantee: commission or fee per annum on the amount guaranteed, not less than | 1% | "at the rate not less than 1% per annum on the amount guaranteed" | https://www.incometax.gov.in/iec/foportal/sites/default/files/2026-03/En-Notified-IT-Rules-2026-20-03-2026.pdf |
| Serial 5, contract research and development for generic pharmaceutical drugs: operating profit margin not less than | 24% | "in relation to operating expense incurred is not less than 24%," | https://www.incometax.gov.in/iec/foportal/sites/default/files/2026-03/En-Notified-IT-Rules-2026-20-03-2026.pdf |
| Serial 5: aggregate operating revenue not more than | three hundred crore rupees | "where the aggregate operating revenue of such transaction does not exceed a sum of three hundred crore rupees" | https://www.incometax.gov.in/iec/foportal/sites/default/files/2026-03/En-Notified-IT-Rules-2026-20-03-2026.pdf |
| Serial 6, manufacture and export of core auto components: operating profit margin not less than | 12% | "in relation to operating expense is not less than 12%." | https://www.incometax.gov.in/iec/foportal/sites/default/files/2026-03/En-Notified-IT-Rules-2026-20-03-2026.pdf |
| Serial 7, manufacture and export of non-core auto components: operating profit margin not less than | 8.5% | "in relation to operating expense is not less than 8.5%." | https://www.incometax.gov.in/iec/foportal/sites/default/files/2026-03/En-Notified-IT-Rules-2026-20-03-2026.pdf |
| Rule 87(1)(e), auto components: original equipment manufacturer sales as a share of total turnover, at least | 90% | "where 90% or more of total turnover during the relevant tax year is in the nature of original equipment manufacturer sales" | https://www.incometax.gov.in/iec/foportal/sites/default/files/2026-03/En-Notified-IT-Rules-2026-20-03-2026.pdf |
| Serial 8, receipt of low value-adding intra-group services: maximum mark-up included in the aggregate | 5% | "including a mark-up not exceeding 5%, does not exceed a sum of ten crore rupees" | https://www.incometax.gov.in/iec/foportal/sites/default/files/2026-03/En-Notified-IT-Rules-2026-20-03-2026.pdf |
| Serial 8: aggregate amount, including the mark-up, not more than; cost pooling, exclusion of shareholder and duplicate costs and allocation keys certified by an accountant | ten crore rupees | "including a mark-up not exceeding 5%, does not exceed a sum of ten crore rupees" | https://www.incometax.gov.in/iec/foportal/sites/default/files/2026-03/En-Notified-IT-Rules-2026-20-03-2026.pdf |
| Serial 9, provision of data centre services: operating profit margin not less than | 15% | "in relation to operating expense is not less than 15%." | https://www.incometax.gov.in/iec/foportal/sites/default/files/2026-03/En-Notified-IT-Rules-2026-20-03-2026.pdf |
| Option period for information technology services (rule 91(1)) | five consecutive tax years | "shall continue to remain in force for a period of five consecutive tax years" | https://www.incometax.gov.in/iec/foportal/sites/default/files/2026-03/En-Notified-IT-Rules-2026-20-03-2026.pdf |
| Safe harbour option form (rules 90 and 91) | Form No. 49 | "the assessee shall furnish Form No. 49, complete in all respects" | https://www.incometax.gov.in/iec/foportal/sites/default/files/2026-03/En-Notified-IT-Rules-2026-20-03-2026.pdf |

### Company tax rate used in the worked examples

| Item | Rate | Condition | Source |
| --- | --- | --- | --- |
| Domestic company opting for section 200 | 22% | Income-tax Act 2025 s 200(1) | https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Surcharge, domestic company under section 200 or 201 | 10% | Finance Act 2026 s 3(4)(b) Table Sl. No. 9 | https://egazette.gov.in/WriteReadData/2026/271439.pdf |
| Health and Education Cess | 4% of tax plus surcharge | Finance Act 2026 | https://egazette.gov.in/WriteReadData/2026/271439.pdf |

## The base

### Arm's length price (section 173(a))

Section 173(a) defines the arm's length price as "a price which is applied or proposed to be applied in a transaction between persons other than associated enterprises, in uncontrolled conditions".

### Accepted methods (section 165(1), rules 78 and 79)

| Method | Accepted |
| --- | --- |
| Comparable uncontrolled price method | Yes (section 165(1)(a); rule 79(1)(a)) |
| Resale price method | Yes (section 165(1)(b)) |
| Cost plus method | Yes (section 165(1)(c)) |
| Profit split method | Yes (section 165(1)(d)) |
| Transactional net margin method | Yes (section 165(1)(e)) |
| Other method prescribed by the Board | Yes (section 165(1)(f); rule 78: any method that takes into account the price charged or paid, or that would have been charged or paid, for the same or similar uncontrolled transaction) |

### Most appropriate method (rule 80)

The most appropriate method is the one "best suited to the facts and circumstances" of the transaction that gives the most reliable measure of the arm's length price (rule 80(1)). Rule 80(2) lists the factors: nature and class of the transaction; functions, assets and risks of the enterprises; availability, coverage and reliability of data; degree of comparability; how reliably adjustments can be made; and the assumptions the method needs.

### Range, mean and tolerance (section 165(3), rule 81)

- Range: where the most appropriate method is the comparable uncontrolled price, resale price, cost plus or transactional net margin method AND the dataset has six or more entries, build a range from the 35th percentile to the 65th percentile of the dataset (rule 81(6)). A price inside the range is the arm's length price. A price outside it is adjusted to the MEDIAN of the dataset, not to the nearer end of the range.
- Otherwise (fewer than six entries, or the profit split or other method), the arm's length price is the arithmetical mean of the dataset, unless the actual price is within the notified tolerance (rule 81(7)). Rule 81(8) defines the median and the percentiles.
- Multiple-year data: for the resale price, cost plus and transactional net margin methods, comparables' data for up to the two preceding years are included in the dataset as weighted averages where the conditions in rule 81(3) to (5) are met.
- Tolerance: where one price results, or under rule 81(7), the actual price stands if it differs from the arm's length price by no more than a percentage the Central Government notifies, which cannot exceed the ceiling in the rates table (section 165(3)(a)(ii)). The percentage actually notified for tax year 2026-27 is not printed on any page this skill can cite: check the notification before relying on a tolerance.

### Secondary adjustment (section 170, rule 83)

Section 170(1) requires a secondary adjustment where a primary adjustment to the transfer price of at least the amount in the rates table is made by the assessee in the return, made by the Assessing Officer and accepted, determined by an advance pricing agreement, made under the safe harbour rules, or arises from a mutual agreement procedure. If the "excess money" is not repatriated to India within the prescribed time, it is deemed an advance to the associated enterprise and interest is imputed (section 170(2) and (4)).

- Rule 83(1): repatriate within ninety days from the date in its Table (for example the return due date for a self-made adjustment, or the date of the order where an Assessing Officer's adjustment is accepted).
- Rule 83(2): imputed interest on money not repatriated is the State Bank of India one-year marginal cost of funds lending rate on 1 April of the tax year plus 325 basis points for a rupee transaction, or the rule 89(3) reference rate on 30 September plus 300 basis points for a foreign currency transaction.
- Section 170(5): instead, the assessee may pay additional income-tax at the rate in the rates table on the excess money. Section 3(6) of the Finance Act 2026 increases that tax by a surcharge at the rate in the rates table. Once paid, no secondary adjustment or further interest is needed from the date of payment (section 170(8)), and no credit or deduction is allowed for it (section 170(6) and (7)).

### Transaction documentation under rule 84 (the "local file")

Section 171(1) requires every person who has entered into an international transaction or a specified domestic transaction to keep the prescribed documents. Rule 84(1) lists them: ownership structure, group profile, business description, the nature, terms and value of each transaction, a functions, assets and risks analysis, a record of uncontrolled transactions, the comparability evaluation, the methods considered and why the most appropriate method was chosen, the actual working, the assumptions and price negotiations, and any adjustments made to align prices with arm's length prices. Rule 84(5) requires supporting documents (official publications, market studies, price publications, published accounts, agreements and correspondence).

- Rule 84(2): the rule 84(1) list does not apply to an international transaction where the aggregate value, as recorded in the books, of all international transactions in the tax year does not exceed the amount in the rates table. This is a cliff, it is tested on the aggregate, and it covers international transactions only. Rule 84(3) still requires the person to substantiate, from the material available, that the income was computed under section 161.
- Specified domestic transactions have no such exemption in rule 84(2). A person within the safe harbour for specified domestic transactions keeps the shorter list in rule 84(4) instead.
- Rule 84(6): the documents should, as far as possible, be contemporaneous and must exist on the "specified date". Section 173(d) defines that as one month before the return due date under section 263(1).
- Rule 84(7): a transaction that continues beyond one tax year needs fresh documentation only where its nature or terms, the underlying assumptions or another pricing factor change significantly.
- Rule 84(8): keep the documents for the period in the rates table, counted from the end of the relevant tax year.
- Section 171(2) and (3): the Assessing Officer or the Commissioner (Appeals) may require the documents during any proceeding. They must be furnished within ten days of receiving the notice. On application, the period can be extended by a further period of not more than thirty days.

### Safe harbours (section 167, rules 86 to 93)

Under section 167 and rule 89(1), the tax authorities accept the transfer price an eligible assessee declares for an eligible international transaction if the option is valid and the price meets the circumstance in the rates table. Rule 89(4) applies the table for a block of three tax years starting with tax year 2026-27.

Conditions that apply to every row:

- The other party is an associated enterprise, one of the two is a non-resident (rule 88).
- Not available for transactions with an associated enterprise in a territory notified under section 176, or in a no tax or low tax country or territory (rule 92).
- No comparability adjustment or tolerance is allowed on a price accepted under the safe harbour (rule 89(5)).
- Sections 171 and 172 still apply: keep the documents and file Form No. 48 (rule 89(6)).
- No mutual agreement procedure once the safe harbour price is accepted (rule 93).
- Information technology services include software development, IT enabled services, knowledge process outsourcing and contract research and development wholly or partly relating to software development, for a non-resident associated enterprise, "with insignificant risk" (rule 87(1)(a)); rule 87(2) lists the factors used to judge insignificant risk.
- A corporate guarantee is an explicit guarantee by a company to its wholly owned non-resident subsidiary for a short-term or long-term borrowing. Letters of comfort, implicit guarantees and performance guarantees are excluded (rule 86(d)). It is eligible where the amount guaranteed does not exceed one hundred crore rupees, or exceeds it and the associated enterprise's SEBI-registered agency rating is "adequate to highest safety" (rule 88(c)).
- An intra-group loan is a loan advanced to an associated enterprise that is a non-resident. It does not include a loan advanced by a financial company, including a bank, a financial institution or an enterprise that lends or borrows in the normal course of business, or a credit line or other loan facility with no fixed term for repayment (rule 86). Rows 2 and 3 therefore cover loans the Indian assessee makes, not loans it receives.
- Low value-adding intra-group services are support services that are not part of the group's core business, are not shareholder or duplicate services, neither use nor create unique and valuable intangibles, involve no significant risk for the provider, and have no reliable external comparables. The definition excludes research and development, manufacturing and production, software development, knowledge process outsourcing, business process outsourcing, purchasing of raw materials, sales, marketing and distribution, financial transactions, extraction, exploration or processing of natural resources, and insurance and reinsurance (rule 86(k)).
- Auto components: the assessee qualifies only where the share of total turnover in the rates table or more is original equipment manufacturer sales (rule 87(1)(e)).
- Data centre services qualify only where provided to a foreign company (rule 87(1)(g)).

Procedure:

- Information technology services (rule 91): Form No. 49 to the Director General of Income-tax (Systems) by the return due date for the first year. A valid option runs for five consecutive tax years. The revenue ceiling is tested in the first year only. Withdrawal is possible by declaration, but not after six months from the end of the first tax year, and the assessee cannot opt again until the five years end. In each of the next four years file a statement of the eligible transactions by the return due date. Form No. 49 is certified by the chief executive officer or chairman and managing director.
- All other safe harbour transactions (rule 90): Form No. 49 to the Assessing Officer on or before the return due date, AND the return must be filed on or before the date the Form No. 49 is furnished. The Assessing Officer may refer doubts to the Transfer Pricing Officer, but not after two months from the end of the month in which Form No. 49 is received; objections to an invalidity order go to the Commissioner within fifteen days. If the officers miss their time limits, the option is treated as valid (rule 90(10)).

The reference rate for foreign currency loans is defined in rule 89(3)(a): for example 6-month Term SOFR plus 45 basis points for US dollars, 6-month EURIBOR for euro, 6-month Term SONIA plus 30 basis points for sterling. Where an associated enterprise has more than one rating, the lowest counts (rule 89(3)(b)). Specified domestic transactions have their own safe harbour in rules 94 to 98 (government companies in the electricity business and co-operative societies buying milk from their members); this skill does not cover it.

## Deadlines and filing

### Accountant's report: Form No. 48 (section 172)

Every person who has entered into an international transaction or a specified domestic transaction during a tax year must obtain a report from an accountant and furnish it in the prescribed form (section 172). There is no value threshold for the report: one transaction is enough. Rule 85(1) prescribes Form No. 48. Rule 85(2) says it must be furnished at least one month before the return due date under section 263(1)(c). Under the 1961 Act, for assessment year 2026-27 and earlier, this report was Form 3CEB under section 92E; the e-filing portal's company page still describes that older form (Form 3CEB, a report from a chartered accountant under section 92E). Use Form No. 48 for tax year 2026-27.

### Master file: Form No. 56 (section 171(4), rule 123)

A constituent entity of an international group must keep and furnish the master file where BOTH tests are met for the accounting year: (a) the consolidated group revenue in the group's consolidated financial statement exceeds the first amount in the rates table, AND (b) the entity's aggregate international transactions, as per the books, exceed the second amount OR its international transactions for the purchase, sale, transfer, lease or use of intangible property exceed the third amount. The content list is in rule 123(1)(A) to (N).

- Form No. 56 is furnished to the Joint Director designated under rule 124(1), on or before the return due date under section 263(1)(c) (rule 123(2)).
- Every constituent entity files Part A of Form No. 56 even if the thresholds are not met (rule 123(3)).
- Where several Indian constituent entities must file, one designated entity may file Form No. 56 for all, if the group has designated it and this is conveyed in Form No. 57 thirty days before the Form No. 56 due date (rule 123(4)).
- Keep the records for nine years from the end of the relevant tax year (rule 123(5)).
- Group revenue in foreign currency is converted at the telegraphic transfer buying rate on the last day of the accounting year (rule 123(6)).

### Country-by-country report (section 511, rule 124)

Section 511 does not apply to an international group for an accounting year if its total consolidated group revenue, per the consolidated financial statement for the PRECEDING accounting year, does not exceed the amount in the rates table (section 511(8), rule 124(7)). Revenue in foreign currency is converted at the telegraphic transfer buying rate on the last day of that preceding accounting year (rule 124(8)).

- Notification (section 511(1)): every Indian constituent entity of a group whose parent is not resident in India notifies whether it is the alternate reporting entity, or the details of the parent or alternate reporting entity. Form No. 58, two months before the report due date (rule 124(2)).
- Report (section 511(2)): a parent entity or alternate reporting entity resident in India furnishes the report in Form No. 59 within twelve months from the end of the reporting accounting year (rule 124(3)).
- Local filing (section 511(4)): an Indian constituent entity files the report itself if the parent is not obliged to file, its country has no agreement with India to exchange the report, or there is a systemic failure that has been intimated. The period is twelve months from the end of the reporting accounting year (rule 124(4)); after an intimated systemic failure it is six months from the end of the month of intimation (rule 124(5)). Section 511(6) switches this off where an alternate reporting entity has filed abroad and every condition in that subsection is met.
- Designated entity (section 511(5)): the information on a designated Indian constituent entity goes in Form No. 60 (rule 124(6)).
- Accuracy notice (section 511(7)): the authority may require information within thirty days of receiving the notice, extendable by up to thirty more days on application.
- Corrections to Form No. 59 are made by intimation to the Director General of Income-tax (Systems) (rule 124(9)).

### Filing obligations

| Obligation | Detail |
| --- | --- |
| Accountant's report, Form No. 48 (section 172, rule 85) | Every person with an international transaction or a specified domestic transaction in the tax year; at least one month before the return due date |
| Transaction documentation (section 171(1), rule 84) | Keep; not filed. Produce within ten days of a notice under section 171(2), extendable by up to thirty days |
| Master file, Form No. 56 (section 171(4), rule 123) | Full form where both rule 123(1) tests are met; Part A by every constituent entity of an international group; by the return due date |
| Designation for the master file, Form No. 57 | Thirty days before the Form No. 56 due date, where one entity files for several |
| Country-by-country notification, Form No. 58 | Two months before the report due date |
| Country-by-country report, Form No. 59 | Twelve months after the end of the reporting accounting year |
| Safe harbour option, Form No. 49 | By the return due date; see Safe harbours under The base |
| Return of income | 30 November of the financial year after the tax year where section 172 applies (see Deadlines) |

### Deadlines

Section 263(1)(c), as substituted by section 66 of the Finance Act 2026, gives due dates in "the financial year succeeding the relevant tax year". So for tax year 2026-27 the dates in the rates table fall in 2027.

| Item | Deadline |
| --- | --- |
| Form No. 48 | At least one month before the return due date (rule 85(2)) |
| Transaction documentation in place | On the specified date: one month before the return due date (section 173(d)) |
| Form No. 56 (master file) | On or before the return due date (rule 123(2)) |
| Form No. 57 | Thirty days before the Form No. 56 due date (rule 123(4)) |
| Form No. 58 | Two months before the Form No. 59 due date (rule 124(2)) |
| Form No. 59 | Twelve months after the end of the reporting accounting year (section 511(2); rule 124(4) for constituent entities) |
| Form No. 49 (safe harbour) | On or before the return due date (rules 90(1) and 91(3)) |
| Form No. 52 (APA annual compliance report) | Within thirty days of the return due date or within ninety days of entering into the agreement, whichever is later (rule 113(3)) |
| Modified return after an APA | Three months from the end of the month in which the agreement was entered into (section 169(1) as substituted by the Finance Act 2026) |

### Advance pricing agreements (APA)

| Item | Detail |
| --- | --- |
| Law | Section 168 (agreement), section 169 (effect on returns); rules 103 to 122 |
| Who may apply | A person who has undertaken, or is contemplating, an international transaction (rule 104). Section 168(1)(b) also covers income of a non-resident attributable to operations in India |
| Types | Unilateral (to the Principal Chief Commissioner of Income-tax (International Taxation)); bilateral or multilateral (to the competent authority of India) (rule 106(2)) |
| Pre-filing consultation | Form No. 50 (rule 105); not binding on either side |
| Application | Form No. 51 with the fee in the rates table (rule 106) |
| When to apply | Before the first day of the first tax year covered, for continuing transactions; before undertaking the transaction, for others (rule 106(3)) |
| Fee on withdrawal | Not refunded (rule 107(2)) |
| Term | Not more than five consecutive tax years (section 168(4)) |
| Rollback | Up to four tax years before the first covered year, on request in Form No. 51 with an additional fee (rule 103(j), rule 111) |
| Annual compliance report | Form No. 52 (rule 113) |
| Renewal | New application in Form No. 54, without a pre-filing consultation (rule 119) |
| Effect while pending | Filing an application does not stop Chapter X applying until the agreement is entered into (rule 120(1)) |
| Not binding | If the law or facts that bear on the agreement change (section 168(6)) |

Rollback conditions (rule 111(2) and (3)): the same international transaction as the main agreement; the return for the rollback year and the accountant's report were furnished on time; rollback is requested for every rollback year in which the transaction took place. Rollback is refused for a year where the Appellate Tribunal has already disposed of an appeal on that transaction's arm's length price, or where rollback would reduce the income or increase the loss declared in that year's return.

## Penalties and interest

The 2025 Act as enacted had a flat penalty in section 447 for not furnishing the section 172 report. Section 102 of the Finance Act 2026 omitted section 447. The default is now a FEE under section 428(d), as substituted by section 96 of the Finance Act 2026, in the rates table.

- Section 459(4) applies where the entity knew of the inaccuracy when it filed and did not inform the authority, or discovered it later and did not inform the authority and file a correct report within fifteen days, or gave inaccurate information in reply to a section 511(7) notice.
- Section 439(11)(f) makes "failure to report any international transaction or any transaction deemed to be an international transaction or any specified domestic transaction" a case of misreporting (the higher rate).
- Section 439(8)(d) excludes from under-reported income an addition made in conformity with the arm's length price set by the Transfer Pricing Officer, where the assessee kept the prescribed documents, declared the international transaction under Chapter X, and disclosed all the material facts. All three conditions must hold.
- Section 440, as substituted by section 99 of the Finance Act 2026: the assessee may apply to the Assessing Officer, within one month from the end of the month in which the order is received, for waiver of the section 439 penalty and immunity from prosecution under section 478 or 479. ALL of these must hold: the tax and interest demanded are paid within the period in the notice of demand; for misreporting under section 439(11)(a) to (f), additional income-tax at the rate in the rates table is paid in place of the penalty; and no appeal is filed. No waiver is granted if any proceeding has been initiated under Chapter XXII.

## Cross-border points

- Every international transaction has at least one non-resident party (section 163(1)); a deemed international transaction under section 163(2) catches a third party whose terms are in substance set with the associated enterprise.
- Safe harbour is not available for transactions with an associated enterprise in a territory notified under section 176 or in a no tax or low tax territory (rule 92), and no mutual agreement procedure is available once a safe harbour price is accepted (rule 93).
- A bilateral or multilateral APA goes to the competent authority of India (rule 106(2)).
- Country-by-country reporting depends on where the parent is resident and whether its country exchanges reports with India (section 511(4)).
- Excess money from a primary adjustment must come back to India within ninety days or be deemed an advance with imputed interest (section 170, rule 83).

### Recent developments

| Date | Development |
| --- | --- |
| 1 April 2026 | Income-tax Act 2025 in force; the transfer pricing rules move from sections 92 to 92F of the 1961 Act to Chapter X of the 2025 Act; the country-by-country report moves to section 511 |
| 1 April 2026 | Income-tax Rules 2026 in force (notified 20 March 2026): new form numbers (Form No. 48 for the accountant's report, Form No. 49 for safe harbour, Forms No. 50 to 54 for APAs, Forms No. 56 to 60 for master file and country-by-country reporting) |
| Tax year 2026-27 | New safe harbour table (rule 89) for a block of three tax years starting with tax year 2026-27, with rows for information technology services, loans, corporate guarantees, pharmaceutical contract research, auto components, low value-adding intra-group services and data centre services |
| Finance Act 2026 (assent 30 March 2026) | Section 447 penalty for not furnishing the accountant's report omitted; replaced by the section 428(d) fee. Section 169(1) substituted: modified return after an APA within three months from the end of the month of the agreement. Section 166(7) substituted (time limit for the Transfer Pricing Officer's order) |

## Two worked examples that recompute

### Example 1: IT services subsidiary, safe harbour or benchmark

An Indian captive provides software development to its US parent with insignificant risk. Operating expense for tax year 2026-27 is 50 crore rupees (5,00,00,000) and its actual operating margin is 13% (6,50,00,000 of profit, a price of 56,50,00,000). Revenue is well under the two thousand crore rupee ceiling, so serial 1 of the rule 89 table is open. To be inside the safe harbour the margin must be at least 15.5%, so the declared price must rise to give 7,75,00,000 of margin: a primary adjustment of 1,25,00,000 rupees. At the section 200 company rate (22%, 10% surcharge, 4% cess: 25.168%) that costs 31,46,000 rupees of tax. The adjustment is one crore rupees or more, so section 170 also bites: repatriate the 1,25,00,000 within ninety days or pay the section 170(5) additional tax of 18% plus the 12% surcharge, 25,20,000 rupees (whether cess applies to it was not tested). The decision: opting in buys certainty for five years (rule 91) at about 31,46,000 of tax a year at this margin, against a benchmark under rule 81 that might support 13% but brings documentation, a possible Transfer Pricing Officer reference and penalty risk.

```oa-check
name: IT services safe harbour, opex 50 crore, actual margin 13% against 15.5%
inputs:
  opex: 500000000
  actual_margin: 0.13
  safe_margin: 0.155
  company_rate: 0.25168
steps:
  - required_profit: opex * safe_margin
  - actual_profit: opex * actual_margin
  - primary_adjustment: required_profit - actual_profit
  - tax_on_adjustment: primary_adjustment * company_rate
  - secondary_trigger: primary_adjustment - 10000000
  - s170_5_tax: primary_adjustment * 0.18 * 1.12
expected:
  primary_adjustment: 12500000
  tax_on_adjustment: 3146000
  secondary_trigger: 2500000
  s170_5_tax: 2520000
```

### Example 2: Unreported loan to a foreign subsidiary, penalty or the section 440 route

A company failed to report an 8 crore rupee loan to its foreign subsidiary in Form No. 48. The Transfer Pricing Officer adds 2 crore rupees of interest income. Tax on that under-reported income at 25.168% is 50,33,600 rupees. Failure to report an international transaction is misreporting (section 439(11)(f)), so the penalty is 200% of that tax: 1,00,67,200 rupees. Separately, section 442(1) can charge 2% of the transaction value for failing to report it: 16,00,000 rupees. Under section 440 as substituted, the company can instead pay the tax and interest demanded and additional income-tax of 100% of the tax on under-reported income (50,33,600 rupees), not appeal, and apply within one month from the end of the month the order is received for waiver of the section 439 penalty and immunity from prosecution. Taking the section 440 route saves 50,33,600 rupees against the full misreporting penalty, at the price of giving up the appeal.

```oa-check
name: Misreporting penalty against section 440 additional tax, 2 crore addition
inputs:
  under_reported: 20000000
  company_rate: 0.25168
  loan_value: 80000000
steps:
  - tax_on_ur: under_reported * company_rate
  - misreporting_penalty: tax_on_ur * 2
  - s440_additional_tax: tax_on_ur * 1
  - saving_s440: misreporting_penalty - s440_additional_tax
  - s442_penalty: loan_value * 0.02
expected:
  tax_on_ur: 5033600
  misreporting_penalty: 10067200
  saving_s440: 5033600
  s442_penalty: 1600000
```

## Ask the client first

- Who are the counterparties, where is each resident, and which section 162 test links them (shareholding, loans, guarantees, board, supply, control)?
- What is the total book value of international transactions for the tax year, and is there any domestic related-party transaction of the kinds listed in section 164?
- Is the Indian entity part of a group that prepares consolidated financial statements? What was consolidated revenue for this accounting year and the preceding one, and where is the parent resident?
- Does any transaction fit a safe harbour row (IT services, loans, a guarantee to a wholly owned foreign subsidiary, pharma research, auto components, low value-adding services, data centres), and is the counterparty in a notified or low tax territory?
- Is there an APA in force or pending, or a past Transfer Pricing Officer adjustment, mutual agreement case or appeal on the same transactions?
- Was any primary adjustment made last year that still needs repatriation or the section 170(5) tax?

### The method, step by step

1. Map the relationships. Test each counterparty against section 162(1) of the Income-tax Act 2025 (rates table): https://egazette.gov.in/WriteReadData/2025/265620.pdf
2. Classify each transaction. An international transaction under section 163 (one party necessarily a non-resident), or a specified domestic transaction under section 164, which exists only if the aggregate of the listed domestic transactions exceeds the section 164 amount: https://egazette.gov.in/WriteReadData/2025/265620.pdf
3. Check the safe harbour first. If a transaction fits a rule 89 row and none of the rule 92 exclusions applies, decide whether to opt in with Form No. 49 by the return due date (rules 90 and 91): https://www.incometax.gov.in/iec/foportal/sites/default/files/2026-03/En-Notified-IT-Rules-2026-20-03-2026.pdf
4. Otherwise select the most appropriate method (section 165 and rule 80), build the dataset, and apply the range or mean under rule 81. Adjust to the median if the price falls outside the range: https://www.incometax.gov.in/iec/foportal/sites/default/files/2026-03/En-Notified-IT-Rules-2026-20-03-2026.pdf
5. Prepare the rule 84 documentation by the specified date (one month before the return due date), unless the rule 84(2) exemption applies to the international transactions: https://www.incometax.gov.in/iec/foportal/sites/default/files/2026-03/En-Notified-IT-Rules-2026-20-03-2026.pdf
6. Obtain the accountant's report in Form No. 48 and furnish it at least one month before the return due date (section 172, rule 85): https://www.incometax.gov.in/iec/foportal/sites/default/files/2026-03/En-Notified-IT-Rules-2026-20-03-2026.pdf
7. File the return by the section 263(1)(c) date (30 November of the next financial year where section 172 applies): https://egazette.gov.in/WriteReadData/2026/271439.pdf
8. For a group: file Part A of Form No. 56 in every case, and the full master file if both rule 123(1) tests are met; check the section 511 country-by-country report against the preceding year's consolidated revenue, and file Form No. 58 and, where due, Form No. 59 (rules 123 and 124): https://www.incometax.gov.in/iec/foportal/sites/default/files/2026-03/En-Notified-IT-Rules-2026-20-03-2026.pdf
9. If a primary adjustment of one crore rupees or more arises, repatriate the excess money within ninety days or pay the section 170(5) additional tax (section 170, rule 83): https://egazette.gov.in/WriteReadData/2025/265620.pdf
10. Keep everything for nine years from the end of the tax year (rules 84(8) and 123(5)) and diary the section 171(2) ten-day response period for any notice: https://egazette.gov.in/WriteReadData/2025/265620.pdf

### When to refuse or refer

- Any year before tax year 2026-27 (assessment year 2026-27 and earlier). Those years are under the 1961 Act, with different sections, forms and penalties. Refer.
- Preparing or signing Form No. 48. Only an accountant as defined in section 515(3)(b) can give the report. This skill helps prepare; it does not certify.
- Building a benchmarking dataset or choosing comparables from paid databases. Refer to a transfer pricing specialist.
- Negotiating an APA, a mutual agreement procedure, a Transfer Pricing Officer reference under section 166 or an appeal. Refer.
- Specified domestic transaction safe harbour (rules 94 to 98) and the safe harbour for income attribution (rules 99 to 102). Not covered here.
- Business restructurings, intangibles valuations, profit attribution to a permanent establishment, and any question that depends on the notified tolerance percentage for tax year 2026-27. Refer.
- Any rule the client wants applied "as proposed" in a Bill or a press release. Only enacted law and notified rules are covered.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| Read for Income-tax Act 2025 sections 161 to 173, 176, 263, 439, 440, 442, 457, 459, 511 and 515 as enacted (Gazette, Act 30 of 2025) | https://egazette.gov.in/WriteReadData/2025/265620.pdf | 2026-11-14 |
| Read for Finance Act 2026 sections 3(4), 3(6), 66 (section 263 substituted), 96 (section 428), 99 (section 440), 102 (section 447 omitted) and the section 166(7) and 169(1) substitutions | https://egazette.gov.in/WriteReadData/2026/271439.pdf | 2026-11-14 |
| Read for Income-tax Rules 2026 rules 77 to 124 (methods, range, documentation, Form No. 48, safe harbour, APA, master file, country-by-country report) | https://www.incometax.gov.in/iec/foportal/sites/default/files/2026-03/En-Notified-IT-Rules-2026-20-03-2026.pdf | 2026-11-14 |
| Read for the e-filing portal company page describing the 1961 Act Form 3CEB under section 92E (assessment year 2026-27 and earlier) | https://www.incometax.gov.in/iec/foportal/help/company/return-applicable | 2026-11-14 |

Not yet confirmed: the tolerance percentage notified under section 165(3) for tax year 2026-27 (the rule only caps it at 3%); whether the 4% Health and Education Cess applies to the section 170(5) additional income-tax; how the section 428(d) fee counts a delay of more than one month (whether 1,00,000 replaces or adds to 50,000); the specified domestic transaction and income attribution safe harbours (rules 94 to 102), not read for this skill.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-14. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `india-transfer-pricing` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/india-transfer-pricing. If neither is available, confirm every figure against the official source pages cited above before relying on it.
