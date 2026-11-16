---
name: eg-financial-statements
description: Use this skill whenever asked about Egyptian financial statements, financial reporting, or the accounting standards an Egyptian business must follow. Trigger on phrases like "Egypt financial statements", "Egyptian Accounting Standards", "EAS", "القوائم المالية", "المعايير المحاسبية المصرية", "do I file accounts Egypt", "audit Egypt company", "audited financial statements Egypt", "balance sheet Egypt", "IFRS Egypt", "EGX listed company accounts", "FRA filing", or any request to explain who must prepare, audit, or file financial statements in Egypt and and what a self-employed person files instead. ALWAYS read this skill before advising on Egyptian financial reporting or audit.
version: 1.2
jurisdiction: EG
tax_year: 2026
last_updated: 2026-11-16
depends_on:
  - income-tax-workflow-base
category: financial-statements
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: financial-statements
type: situation-rules
---

# EG Financial Statements v1.2

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

Loads on `income-tax-workflow-base`. It says who in Egypt prepares and files financial statements (القوائم المالية), what a self-employed person files instead, which books back the return, and which auditing standards apply. Tax year 2026, law as read on 16 November 2026. It produces a brief for a reviewer, never an audit opinion. Reply in the user's language.

**Answer first.** A sole proprietor or professional is a natural person: no statutory financial statements, but regular books under the Commercial Law from 29 July 2026 (or the Law 6 simplified set) and the annual return with all its tables before 1 April. A company files its annual return before 1 May, or within four months of its year end, and prepares statements under the Egyptian Accounting Standards (EAS). New Egyptian auditing standards apply to audits and reviews of statements for financial years starting on or after 1 January 2027.

## Who this applies to

- **Covered:** sole proprietors (منشأة فردية), professionals (مهنة حرة), limited liability companies (ش.ذ.م.م) and joint-stock companies (شركة مساهمة).
- **Out of scope:** banks (Central Bank of Egypt rules), insurers and other entities regulated by the Financial Regulatory Authority (FRA, الهيئة العامة للرقابة المالية), and group consolidation. Books in detail: `eg-bookkeeping`. Returns: `eg-income-tax`, `eg-corporate-tax`. Law 6 of 2025: `eg-sme-tax`.
- **Authorities:** the ETA (tax); the FRA (capital market, the accounting and auditing standards legislation it lists, and its register of auditors); GAFI and the commercial register (company records); the Egyptian Exchange, EGX (listed companies).
- **Natural person:** taxed under Income Tax Law 91 of 2005 and keeps books, not statutory statements. **Company:** a separate legal person whose books also follow the Companies Law 159 of 1981, which the amended Unified Tax Procedures Law art. 38 expressly takes into account (Law 150 of 2026 art. 1).

## Rates, bands and thresholds

| Item | Amount | Tax year | Conditions | Official URL |
|---|---|---|---|---|
| Law 6 turnover tax, turnover under EGP 500,000 (in words on the page) | 0.4% of turnover | 2026 | Business asked for Law 6; turnover not above EGP 20 million (art. 10(1)); bands owned by `eg-sme-tax` | https://eta.gov.eg/sites/default/files/2025-02/law_no.6.of_.2025.pdf |
| Law 6, EGP 500,000 to under EGP 2,000,000 (in words on the page) | 0.5% | 2026 | same conditions, art. 10(2) | same |
| Law 6, EGP 2,000,000 to under EGP 3,000,000 (in words on the page) | 0.75% | 2026 | same conditions, art. 10(3) | same |
| Law 6, EGP 3,000,000 to under EGP 10,000,000 (in words on the page) | 1% | 2026 | same conditions, art. 10(4) | same |
| Law 6, EGP 10,000,000 to EGP 20,000,000 (in words on the page) | 1.5% | 2026 | same conditions, art. 10(5) | same |
| Late return and payment, up to 60 days; or a wrong return showing more tax | Fine EGP 3,000 to 50,000 (in words on the page), plus the tax and other sums due | 2026 | Unified Tax Procedures Law 206 of 2020 art. 69; both bounds are tripled on repeat | https://eta.gov.eg/sites/default/files/2024-03/law_no.206-2020.pdf |
| Return not filed for over 60 days after the deadline | Fine EGP 5,000 to 200,000 (in words on the page) | 2026 | Art. 70; doubled if repeated within three years | same |
| Breach of the books duty in art. 38 paras. 1 to 3 | Fine EGP 20,000 to 100,000 (in words on the page) | 2026 | Art. 71 first sentence (it also covers arts. 24, 28, 35 and 37) | same |
| Books and records not kept for the legal period | Fine up to EGP 50,000 (in words on the page) | 2026 | Art. 71 second sentence; the period is five years after the tax period of the return (art. 38) | same |
| New Egyptian auditing standards | Apply to audits and reviews of statements for financial years starting on or after 1 January 2027 | 2027 | Prime Minister Decree 3725 of 2025 art. 1; international standards apply where the Egyptian ones are silent; art. 2 cancels Minister of Investment Decision 166 of 2008 and its standards from that date | https://fra.gov.eg/wp-content/uploads/2025/10/3725-2025.pdf |

## The base

**What each taxpayer prepares.**

1. Identify the taxpayer: natural person or company.
2. **Natural person, general system:** behind the return, prepare revenues, deductible costs, depreciation and net profit from regular books. From 29 July 2026 every taxpayer in a commercial, industrial, craft or professional activity keeps the regular books required by Commercial Law 17 of 1999, by hand or electronically (Law 206 art. 38 first para., as replaced by [Law 150 of 2026](https://eta.gov.eg/sites/default/files/2026-08/law.no_.150.of_.2026.pdf) art. 1, in force the day after publication on 28 July 2026). Before that date the duty applied only above annual turnover of EGP 500,000 (the replaced text). Every taxpayer also keeps electronic accounts of annual revenue and costs, and the Minister may set simplified rules for classes of taxpayers (art. 38, paras. not replaced).
3. **Natural person, Law 6:** exempt from the Law 206 books; keeps the simplified set in [MoF Decision 420 of 2025](https://eta.gov.eg/sites/default/files/2025-12/mof.decision.no_.420.of_.2025.pdf) art. 3: a fixed-asset register and a raw-materials stock register; a daily sales book, a daily purchases book and a tax summary book; and the e-invoice or e-receipt as the case requires, on paper or electronically ([Law 6 of 2025](https://eta.gov.eg/sites/default/files/2025-02/law_no.6.of_.2025.pdf) art. 13). The tax is on turnover (art. 10), declared on form 20 إقرارات (MoF 420 art. 2), so no profit computation sits behind it.
4. **Company:** prepare the annual statements under EAS and file the return by the art. 31 date. Listed or FRA-regulated companies add their FRA and EGX filings.
5. **Audit or review for a financial year starting on or after 1 January 2027:** apply the Decree 3725 standards.
6. Keep everything for five years after the tax period whose return was filed (Law 206 art. 38).

**Accounting standards.** The FRA list of accounting standards legislation names Minister of Investment Decision 110 of 2015 (the Egyptian Accounting Standards), Decision 69 of 2019 amending them, and Prime Minister decrees of 2023 and 2024 amending them (listed titles read, decrees not opened). It also lists Prime Minister Decree 2115 of 2023 on the Permanent Committee for Egyptian Accounting Standards and auditing standards, amended by Decree 712 of 2026. EAS is IFRS-aligned, not IFRS: never treat the two as identical, and flag standard-specific differences for the reviewer.

**Who signs.** Only a qualified, registered Egyptian auditor (مراجع حسابات مقيد) signs an audit report. Never imply assurance or an audit opinion.

**Held positions.** These carry rules from the earlier version that were not confirmed against the law in this read. They stay visible as working defaults that always end in a referral, never as settled law; each is also on the "Not yet confirmed" line.

- If the taxpayer is a company, assume audited EAS statements are required and filed with the tax return, unless it is clearly a partnership (شركات الأشخاص), and even then confirm: lenders, banks, partners or the ETA often require audited or reviewed accounts in practice. Earlier text: under the Companies Law and the Capital Market Law all companies prepare annual audited statements except general and limited partnerships, by a registered auditor; joint-stock companies and LLCs need an audit.
- The EAS set for a company: statement of financial position (قائمة المركز المالي), statement of comprehensive income (قائمة الدخل الشامل), statement of cash flows (قائمة التدفقات النقدية), statement of changes in equity (قائمة التغير في حقوق الملكية) and notes (الإيضاحات المتممة).
- EAS history in the earlier version: a 2015 comprehensive set; amendments in 2019 adding standards mirroring IFRS 9, 15 and 16; a standard similar to IFRS 17 issued in 2023, effective for periods beginning on or after 1 July 2024; special or simplified requirements for small and medium-sized entities.
- Who uses what: public interest entities (listed companies, public subscription companies, securities companies, investment funds set up by banks and insurers) apply EAS; EGX issuers report under EAS rather than a separate full IFRS mandate, though some also prepare IFRS group packs; banks follow Central Bank standards; insurers and other non-bank financial entities follow FRA standards and rules; subsidiaries of multinationals often add full IFRS for group consolidation.
- The current standards (the Egyptian Standards on Auditing, Review and Other Assurance Services, issued by Decision 166 of 2008) were described as aligned with the International Standards on Auditing; ISQM 1 and ISQM 2 were reported as applied from 2025.
- A voluntary accountant's review of an individual's accounts is common where amounts are large or a bank asks.
- Do not assume an entity uses Law 6 unless turnover is within the ceiling and the request was filed (`eg-sme-tax`).

**Sole proprietor against company.**

| Point | Sole proprietor or professional | Company |
|---|---|---|
| Legal person | Natural person | Separate legal entity |
| Formal financial statements | No | Yes, under EAS (held position above) |
| Statutory audit | No | Yes, except partnerships (held position above) |
| Filed with | ETA income tax return with supporting accounts | ETA return; FRA and EGX if regulated or listed |
| Return deadline | Before 1 April after the year (Law 206 art. 31) | Before 1 May, or within four months of the year end (Law 206 art. 31) |
| Standards | None for statements; books under Commercial Law or the Law 6 set | EAS (IFRS-aligned, not IFRS) |

Plain-language framing for a sole proprietor: "You file your income tax return with supporting accounts from your books, not a full audited set of financial statements. If you form a company, that changes."

## Deadlines and filing

| Taxpayer | What is filed | Deadline | Source |
|---|---|---|---|
| Individual, general system | Annual return with every table; a return missing tables does not count | Before 1 April of the following year (tax year 2026: by 31 March 2027) | [Law 206 of 2020](https://eta.gov.eg/sites/default/files/2024-03/law_no.206-2020.pdf) art. 31(c) |
| Individual, Law 6 | Form 20 إقرارات | Same dates: 1 January to 31 March | [Law 6 of 2025](https://eta.gov.eg/sites/default/files/2025-02/law_no.6.of_.2025.pdf) art. 12; [MoF 420 of 2025](https://eta.gov.eg/sites/default/files/2025-12/mof.decision.no_.420.of_.2025.pdf) art. 2 |
| Company | Annual return with the statements | Before 1 May, or within four months of the financial year end | [Law 206 of 2020](https://eta.gov.eg/sites/default/files/2024-03/law_no.206-2020.pdf) art. 31(c) |
| Listed or FRA-regulated company | FRA and EGX periodic statements in addition | FRA rules (the FRA has extended some periodic filing periods by board decision) | [FRA list](https://fra.gov.eg/%d8%aa%d8%b4%d8%b1%d9%8a%d8%b9%d8%a7%d8%aa-%d9%85%d8%b9%d8%a7%d9%8a%d9%8a%d8%b1-%d8%a7%d9%84%d9%85%d8%ad%d8%a7%d8%b3%d8%a8%d8%a9-%d9%88%d9%85%d8%b1%d8%a7%d9%82%d8%a8%d9%8a-%d8%a7%d9%84%d8%ad%d8%b3-2/) |

A first return counts as notice of starting the activity, and a return is due even for exempt periods (Law 206 art. 31). Law 6 returns are examined only after five years from the request, for income tax and VAT (Law 6 art. 12).

## Penalties and interest

The fines are in the rates table: art. 69 for a return or payment up to 60 days late or a return understating tax, art. 70 for no return after 60 days, art. 71 for the books duty and for not keeping books for five years. Late payment charges and their 100% ceiling are in `eg-income-tax`. A Law 6 business that files late also breaks the art. 3 condition of the regime.

## Cross-border points

This skill has no cross-border rule of its own. Subsidiaries of foreign groups still prepare local EAS statements; any IFRS group pack is extra (held position). Treaties, withholding and transfer pricing sit in `eg-cross-border`, `eg-withholding-tax` and `eg-transfer-pricing`.

## Two worked examples that recompute

**Example 1. Freelance developer in Law 6, turnover EGP 1,200,000.** No statutory statements. Tax at 0.5%: EGP 6,000 on form 20, filed by 31 March 2027. Records: the MoF 420 set.

```oa-check
name: Developer, Law 6 tax
inputs:
  turnover: 1200000
  rate: 0.005
steps:
  - tax: turnover * rate
expected:
  tax: 6000.00
```

**Example 2. Decision: stay a sole proprietor or incorporate.** The same developer weighs an LLC. Tax under Law 6 stays EGP 6,000 if the LLC qualifies. The added yearly cost is accounts and audit at an illustrative EGP 40,000 plus EGP 10,000 for filings, EGP 50,000 in all. A contract worth more than EGP 50,000 a year in margin, open only to a company, pays for it: at EGP 80,000 of extra margin the gain is EGP 30,000. Below EGP 50,000, stay a sole proprietor.

```oa-check
name: Decision, incorporate if company-only margin exceeds added cost
inputs:
  audit_cost: 40000
  filing_cost: 10000
  extra_margin: 80000
steps:
  - added_cost: audit_cost + filing_cost
  - net_gain: extra_margin - added_cost
expected:
  added_cost: 50000.00
  net_gain: 30000.00
```

**Example 3. EGX-listed joint-stock company.** Files with the ETA, the FRA and EGX. The Decree 3725 standards apply to the audit of its statements for the financial year starting on or after 1 January 2027.

**Example 4. Layla, sole proprietor developer, turnover about EGP 1,200,000 in 2025, general system.** Financial statements: no. Audit: no statutory audit. She files the 2025 return by 31 March 2026 with supporting accounts (revenues, deductible costs, depreciation, net taxable profit). From 29 July 2026 she keeps regular books under the Commercial Law even though the old EGP 500,000 condition is gone (`eg-bookkeeping`). Her turnover is under EGP 20 million, so the Law 6 regime is worth testing in `eg-sme-tax`. Reply: "You don't prepare or file formal financial statements. File your income tax return with supporting accounts; no audit is required."

**Example 5. Layla incorporates a single-shareholder company or LLC to win larger contracts.** Financial statements: yes, under EAS. Audit: yes, by a registered auditor (held position: an LLC is not a partnership). Files: the company return before 1 May or within four months of year end, with the statements; company records at GAFI and the commercial register. Standards: EAS; full IFRS only if a group or lender requires it. Reply: "Incorporating brings EAS financial statements, which in practice are audited and filed with your company tax return: a real step up from the sole proprietor return."

## Ask the client first

1. Natural person or company, and which company form?
2. Commercial, industrial, craft or professional activity?
3. In Law 6 (request date), or on the general system?
4. Financial year end, and does it start on or after 1 January 2027 for the audit standards?
5. Listed on EGX, or regulated by the FRA or the Central Bank?
6. Does a bank, lender, partner or foreign parent require audited, reviewed or IFRS statements?

Refer to a qualified Egyptian accountant (محاسب قانوني) when: a company needs statutory statements or an audit (the auditor must be registered and sign); the entity is regulated (bank, insurer, securities firm, fund); a transaction touches a standard where EAS departs from IFRS (financial instruments, leases, revenue, insurance, deferred tax); work spans the 2027 auditing standards changeover or any new SME standards; or there is group or IFRS consolidation, transfer pricing or business combination accounting.

Self-checks before handing over: inputs trace to source documents; the taxpayer type matches its row in the deadlines table; the deadline matches Law 206 art. 31; Law 6 status is confirmed before form 20 is used; no statement that EAS equals IFRS and no audit opinion given; the referral list above has been applied.

Never: tell a sole proprietor or professional they must file statutory statements or be audited; state that EAS equals IFRS; state audit thresholds, turnover bands or effective dates as settled without the source above; sign, certify or imply an audit opinion; apply this skill to banks, insurers or other FRA or Central Bank regulated entities; or replace the qualified reviewer.

## Sources

| Source | URL | Read on |
|---|---|---|
| Law 150 of 2026, arts. 1 to 3, gazette text | https://eta.gov.eg/sites/default/files/2026-08/law.no_.150.of_.2026.pdf | 2026-11-16 |
| Correction notice for Laws 149, 150, 151 of 2026, both pages (page image read) | https://eta.gov.eg/sites/default/files/2026-08/law.no_.149.150.151.of_.2026.retractation.pdf | 2026-11-16 |
| Unified Tax Procedures Law 206 of 2020, arts. 31, 38, 68 to 71 (page images and OCR read) | https://eta.gov.eg/sites/default/files/2024-03/law_no.206-2020.pdf | 2026-11-16 |
| Law 6 of 2025, arts. 1 to 16, whole text | https://eta.gov.eg/sites/default/files/2025-02/law_no.6.of_.2025.pdf | 2026-11-16 |
| MoF Decision 420 of 2025, arts. 1 to 4 (page images read) | https://eta.gov.eg/sites/default/files/2025-12/mof.decision.no_.420.of_.2025.pdf | 2026-11-16 |
| Prime Minister Decree 3725 of 2025, arts. 1 to 3 and preamble (first pages of the gazette file read; the attached standards not read) | https://fra.gov.eg/wp-content/uploads/2025/10/3725-2025.pdf | 2026-11-16 |
| FRA, legislation on accounting standards and auditors, list page 1 titles read | https://fra.gov.eg/%d8%aa%d8%b4%d8%b1%d9%8a%d8%b9%d8%a7%d8%aa-%d9%85%d8%b9%d8%a7%d9%8a%d9%8a%d8%b1-%d8%a7%d9%84%d9%85%d8%ad%d8%a7%d8%b3%d8%a8%d8%a9-%d9%88%d9%85%d8%b1%d8%a7%d9%82%d8%a8%d9%8a-%d8%a7%d9%84%d8%ad%d8%b3-2/ | 2026-11-16 |

Not yet confirmed: the audit duty for all companies except general and limited partnerships, and the auditor registration rule (Companies Law 159 of 1981 and Capital Market Law 95 of 1992 not opened; no official text found on the GAFI or FRA pages read); the list of statements under EAS; the EAS history detail (IFRS 9, 15, 16 and 17 equivalents, the 1 July 2024 date, SME requirements), beyond the FRA list titles; who applies EAS or full IFRS, including public interest entities and EGX issuers; whether the 2008 auditing standards align with the ISA, and ISQM 1 and 2 from 2025; FRA interim reporting periods; bank-required audits of partnerships; how partnerships file.
