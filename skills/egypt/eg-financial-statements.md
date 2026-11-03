---
name: eg-financial-statements
description: Use this skill whenever asked about Egyptian financial statements, financial reporting, or the accounting standards an Egyptian business must follow. Trigger on phrases like "Egypt financial statements", "Egyptian Accounting Standards", "EAS", "القوائم المالية", "المعايير المحاسبية المصرية", "do I file accounts Egypt", "audit Egypt company", "audited financial statements Egypt", "balance sheet Egypt", "IFRS Egypt", "EGX listed company accounts", "FRA filing", or any request to explain who must prepare, audit, or file financial statements in Egypt and and what a self-employed person files instead. ALWAYS read this skill before advising on Egyptian financial reporting or audit.
version: 1.1
jurisdiction: EG
tax_year: 2026
last_updated: 2026-11-01
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
depends_on:
  - income-tax-workflow-base
category: financial-statements
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# EG Financial Statements

## What this file is

Loads on `income-tax-workflow-base`. It says who in Egypt prepares and files financial statements (القوائم المالية), what a self-employed person files instead, and which audit standards apply. It is current for tax year 2026 and the law as read on 1 November 2026. It produces a brief for a reviewer, not an audit opinion. Reply in the user's language.

## Scope statement

Covered: sole proprietors, professionals, LLCs and joint-stock companies. Out of scope: banks, insurers and other FRA or Central Bank regulated entities, and group consolidation. Books are in `eg-bookkeeping`; returns in `eg-income-tax` and `eg-corporate-tax`; Law 6 in `eg-sme-tax`.

Authorities: ETA (tax); the Financial Regulatory Authority, FRA (capital market and accounting and auditor legislation); GAFI and the commercial register (company records); EGX (listed companies).

## Filing requirements

| Taxpayer | What is filed | Deadline | Source |
|---|---|---|---|
| Individual, normal basis | Annual return with its schedules; every table must be complete or the return does not count | Before 1 April | [Law 206 of 2020](https://eta.gov.eg/sites/default/files/2024-03/law_no.206-2020.pdf) Art. 31 |
| Individual, Law 6 | Form 20 (إقرارات) | Same dates | [Law 6 of 2025](https://eta.gov.eg/sites/default/files/2025-02/law_no.6.of_.2025.pdf) Art. 12; [MoF 420 of 2025](https://eta.gov.eg/sites/default/files/2025-12/mof.decision.no_.420.of_.2025.pdf) Art. 2 |
| Company | Annual return | Before 1 May, or within four months of the financial year end | [Law 206 of 2020](https://eta.gov.eg/sites/default/files/2024-03/law_no.206-2020.pdf) Art. 31 |

Books for a company follow Law 159 of 1981 as well as Article 38: the amended Article 38 applies "with regard to" that law ([Law No. 150 of 2026](https://eta.gov.eg/sites/default/files/2026-08/law.no_.150.of_.2026.pdf), Article 1). A sole proprietor keeps books, not statutory statements.

## Rates and thresholds

| Item | Amount | Tax year | Conditions | Official URL |
|---|---|---|---|---|
| Law 6 turnover tax, turnover under EGP 500,000 | 0.4% of turnover | 2026 | Business asked for Law 6; turnover not above EGP 20 million (Art. 10) | https://eta.gov.eg/sites/default/files/2025-02/law_no.6.of_.2025.pdf |
| Law 6, EGP 500,000 to under EGP 2,000,000 | 0.5% | 2026 | same conditions | same |
| Law 6, EGP 2,000,000 to under EGP 3,000,000 | 0.75% | 2026 | same conditions | same |
| Law 6, EGP 3,000,000 to under EGP 10,000,000 | 1% | 2026 | same conditions | same |
| Law 6, EGP 10,000,000 to EGP 20,000,000 | 1.5% | 2026 | same conditions | same |
| Late return, up to 60 days | Fine EGP 3,000 to 50,000, plus the tax | 2026 | Art. 69; on repeat, doubled up to three times the bounds | https://eta.gov.eg/sites/default/files/2024-03/law_no.206-2020.pdf |
| Return not filed for over 60 days | Fine EGP 5,000 to 200,000 | 2026 | Doubles if repeated within three years (Art. 70) | same |
| New Egyptian auditing standards | Apply to statements for financial years starting on or after 1 January 2027 | 2027 | Prime Minister Decree No. 3725 of 2025 | https://fra.gov.eg/%d8%aa%d8%b4%d8%b1%d9%8a%d8%b9%d8%a7%d8%aa-%d9%85%d8%b9%d8%a7%d9%8a%d9%8a%d8%b1-%d8%a7%d9%84%d9%85%d8%ad%d8%a7%d8%b3%d8%a8%d8%a9-%d9%88%d9%85%d8%b1%d8%a7%d9%82%d8%a8%d9%8a-%d8%a7%d9%84%d8%ad%d8%b3-2/ |

## Computation rules

1. Identify the taxpayer: natural person or company.
2. Natural person: prepare revenues, deductible costs, depreciation and net profit behind the return, or the Law 6 turnover figure.
3. Company: prepare the annual statements and file with the return by the Article 31 date.
4. Listed or regulated: add FRA and EGX filings.
5. Year starting on or after 1 January 2027: apply the new auditing standards.

## Edge cases and special rules

- **Law 6.** Exempt from Article 38 books, with the MoF 420 set instead; form 20 replaces profit accounts. Examination happens only after five years ([Law 6 of 2025](https://eta.gov.eg/sites/default/files/2025-02/law_no.6.of_.2025.pdf), Art. 12).
- **Incomplete return.** A return without all tables does not count for the deadline.
- **Auditing reform.** Decree 3725 of 2025 is on the FRA list "as last amended". The FRA list also holds Prime Minister Decree 2115 of 2023, amended by Decree 712 of 2026, on the Permanent Committee for Egyptian Accounting Standards and auditing standards.
- **Only a registered Egyptian auditor signs an audit.** Never imply assurance.
- **EAS is not IFRS.** Never treat them as identical.

Example 1: freelance developer, turnover EGP 1,200,000 in Law 6. No statutory statements. Tax 0.5%: EGP 6,000 on form 20 before 1 April 2027.

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

Example 2: decision, stay a sole proprietor or incorporate. The same developer weighs an LLC. Tax under Law 6 is the same EGP 6,000 if the LLC qualifies. The added yearly cost is accounts and audit at an illustrative EGP 40,000 plus EGP 10,000 for filings. A contract worth more than EGP 50,000 a year in margin, available only to a company, pays for it. Below that, stay a sole proprietor.

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

Example 3: EGX-listed joint-stock company. Files with the ETA, FRA and EGX. New auditing standards from the financial year starting on or after 1 January 2027.

**Carried from the earlier version, not checked against the law.** Kept so no working rule is lost. Any figure here is unverified, and where it differs from the tables above the tables win.

**Conservative defaults**

When a fact is uncertain, the AI must take the safer, more compliant path and tell the user it is doing so:

- If the taxpayer is a company, assume audited EAS financial statements are required and must be filed with the tax return, unless it is clearly a partnership (and even then, confirm: practice and lender/bank requirements often force an audit anyway).
- If the taxpayer is an individual (sole proprietor or professional), assume NO formal statutory financial statements: but assume the ETA still expects proper supporting accounts (income, costs, fixed-asset/depreciation schedules) behind the return. See eg-bookkeeping.
- Do not assume an entity is on the simplified MSME regime unless turnover is confirmed within the threshold and the taxpayer has opted in. See eg-sme-tax.
- Flag, do not guess, thresholds and effective dates. Egypt is mid-reform: new SME accounting/auditing standards and a 2027 overhaul of auditing standards are in train (see Section 6). Always tell the user to verify the current rule.
**2a. Sole proprietor (منشأة فردية) and professional (مهنة حرة)**

- **Sole proprietor taxation and filing**: A self-employed individual is taxed as a natural person under Income Tax Law No. 91 of 2005. They do not prepare or file a statutory set of financial statements (no audited balance sheet filed at a registry). What they DO: - Keep proper books and records: see eg-bookkeeping. Egypt's digital ecosystem (e-invoicing منظومة الفاتورة الإلكترونية, e-receipt منظومة الإيصال الإلكتروني) is increasingly the backbone of those records. - File the annual personal income-tax return by 31 March following the fiscal year. Commercial/industrial income (نشاط تجاري وصناعي) and professional income (مهن حرة) are declared on the return with supporting accounts: a statement of revenues and deductible costs, depreciation, and net taxable profit. - There is no statutory audit requirement for the individual's accounts. A voluntary review by an accountant is common where amounts are large or a bank asks for it. - A simplified MSME taxpayer (Law No. 6 of 2025, turnover ≤ EGP 20m) is even lighter: simplified record-keeping and stand-alone simplified forms, with the small-enterprise turnover-based regime instead of full profit accounting. See eg-sme-tax. *Verify the current turnover bands and opt-in conditions.*

Plain-language framing for the user: "As a sole proprietor in Egypt you file your income-tax return with supporting accounts: not a full audited set of financial statements. If you form a company, that changes; see below."

**2b. Company (شركة): what changes on incorporation**

- **What changes on incorporation**: Once you incorporate (most commonly a limited liability company / ش.ذ.م.م or a joint-stock company / شركة مساهمة), you become a separate legal person and: - You must prepare annual financial statements under EAS: typically a statement of financial position (balance sheet / قائمة المركز المالي), statement of comprehensive income (قائمة الدخل الشامل), statement of cash flows (قائمة التدفقات النقدية), statement of changes in equity (قائمة التغير في حقوق الملكية), and notes (الإيضاحات المتممة). - These statements must generally be audited by a registered auditor (مراجع حسابات مقيد): except partnerships (see Section 4). - The audited financial statements are filed with the corporate income-tax return to the ETA (corporate returns are due within 4 months of year-end). - Regulated and listed entities additionally file with the FRA and, if EGX-listed, with the Egyptian Exchange; company records are maintained at GAFI / the commercial registry (السجل التجاري).

**Sole proprietor vs Company comparison table**

|  | Sole proprietor / professional | Company |
| --- | --- | --- |
| Legal person | Natural person | Separate legal entity |
| Formal financial statements | **No** | **Yes (EAS)** |
| Statutory audit | **No** | **Yes** (except partnerships) |
| Filed with | ETA income-tax return + supporting accounts | ETA tax return + (if regulated/listed) FRA/EGX |
| unverified: Deadline | **31 March** (individual) | **Within 4 months** of year-end (corporate) |
| Standards | n/a (records only) | EAS (IFRS-aligned) |
**3a. What EAS is**

- **What EAS is**: The Egyptian Accounting Standards (EAS / المعايير المحاسبية المصرية) are the mandatory reporting framework for companies in Egypt. They are based on and largely converged with IFRS, but are not identical: there are local departures and a lag behind the latest IFRS amendments. Key points (research-verified): - The current comprehensive EAS set was issued in 2015, with significant amendments in 2019 and 2023. - The 2019 update added standards mirroring IFRS 9 (financial instruments), IFRS 15 (revenue from contracts with customers), and IFRS 16 (leases). - In early 2023 a standard similar to IFRS 17 (insurance contracts) was issued, effective for periods beginning on or after 1 July 2024. - EAS includes special/simplified requirements for small and medium-sized entities (SMEs).

Caveat to surface to the user: EAS is IFRS-aligned, not IFRS itself. Recognition or measurement under EAS can differ from current IFRS (e.g., timing of newly adopted standards, certain local treatments). Never tell a user "EAS = IFRS." *Verify the specific standard.*

**3b. EAS vs full IFRS: who uses what**

- **EAS vs full IFRS applicability**: - Public interest entities (PIEs): listed companies, public-subscription companies, securities companies, and investment funds established by banks and insurance companies: apply EAS. - EGX-listed companies report under EAS (the IFRS-converged Egyptian framework), not a separate "full IFRS" mandate. *Verify for a specific issuer, as some prepare additional IFRS group packs.* - Banks follow standards set by the Central Bank of Egypt (CBE); insurers and other non-bank financial entities follow standards/regulation set by the FRA (الهيئة العامة للرقابة المالية). - Multinational subsidiaries often also prepare full IFRS for group consolidation in addition to local EAS statutory accounts.
**4a. Who must be audited**

- **Who must be audited**: Under the Companies Law and the Capital Market Law, all companies must prepare annual audited financial statements: except partnership companies (شركات الأشخاص) and limited partnership companies. The audit must be performed by a registered auditor (مراجع حسابات مقيد بسجل المراجعين). - Joint-stock (شركة مساهمة) and LLC (ش.ذ.م.م): audit required. - Partnerships (general / limited): statutory carve-out: but lenders, banks, partners, or the ETA may still require audited or reviewed accounts in practice. *Verify for the specific entity.* - Sole proprietor / professional: no statutory audit (natural person).

**4b. Auditing standards**

- **Auditing standards, quality management, and 2027 reform**: - Egypt's auditing standards are the Egyptian Standards on Auditing, Review and Other Assurance Services (ESAROAS), adopted by Ministry of Investment Decision No. 166/2008 and aligned with the International Standards on Auditing (ISA). - Quality management: ISQM 1 and ISQM 2 are being applied (reported effective from 2025 per the profession's SMO action plan). - Major reform ahead: Prime Minister Decree No. 3725 of 2025 approved new Egyptian auditing/financial-review standards that cancel the existing standards from 1 January 2027: the first comprehensive update since 2008. *Flag this date to any user planning a 2027+ audit.*
Layla is a freelance software developer registered as a sole proprietor (منشأة فردية), turnover ~EGP 1.2m in 2025.

- Financial statements? No. As a natural person she files an income-tax return, not statutory audited financials.
- Audit? No statutory audit.
- What she files: annual personal income-tax return by 31 March 2026 for FY2025, with supporting accounts (revenues, deductible costs, depreciation, net taxable profit). She keeps records via the ETA digital systems (eg-bookkeeping).
- Could the MSME regime help? Her turnover is under EGP 20m, so she may qualify for the simplified regime with even lighter record-keeping: route to eg-sme-tax to confirm bands and opt-in. *Verify thresholds.*

Reply: "You don't prepare or file formal financial statements. File your income-tax return with supporting accounts; no audit is required."
Layla converts to a single-shareholder/limited liability company to win larger contracts.

- Financial statements? Yes: full EAS set (financial position, comprehensive income, cash flows, changes in equity, notes).
- Audit? Yes: by a registered auditor (LLC is not a partnership).
- What she files: corporate income-tax return within 4 months of year-end, with the audited EAS statements attached; company records at GAFI / commercial registry.
- Standards: EAS (IFRS-aligned). She does not report under full IFRS unless a group/lender requires it.

Reply: "Incorporating triggers audited EAS financial statements filed with your corporate tax return: a significant step up in compliance from the sole proprietor return."
**Escalate to a qualified Egyptian accountant (محاسب قانوني) when:**

- **Escalation triggers**: - The entity is a company and needs statutory financial statements or an audit: the auditor must be registered and sign the report. - The entity is regulated (bank, insurer, securities firm, fund): FRA/CBE sector standards apply, outside this skill's scope. - A transaction touches a standard where EAS departs from IFRS (financial instruments, leases, revenue, insurance, deferred tax). - Anything spanning the 2027 auditing-standards changeover (Decree 3725/2025) or the new SME accounting/auditing standards still being rolled out. - Group/IFRS consolidation, transfer pricing, or business-combination accounting.
**PROHIBITIONS**

- **AI prohibitions**: The AI applying this skill must NOT: - Tell a sole proprietor or professional that they must file statutory financial statements or be audited. Natural persons file the income-tax return with supporting accounts: not audited financials. - State that EAS is identical to IFRS. EAS is IFRS-aligned with local departures and an adoption lag. Flag standard-specific differences. - Assert audit thresholds, turnover bands, or effective dates as settled. Egypt is mid-reform (SME standards; 2027 auditing overhaul; MSME bands). Mark these "verify" and route to a qualified accountant. - Sign, certify, or imply audit opinion or assurance. Only a registered Egyptian auditor (مراجع حسابات مقيد) may audit and sign. - Apply this skill to banks, insurers, or other FRA/CBE-regulated entities: they follow sector standards outside scope. - Replace a credentialed reviewer. All output is research-verified and pending sign-off by a qualified Egyptian accountant.

## Self-checks

- Inputs trace to source documents.
- Taxpayer type matches the filing row.
- Deadline matches Article 31.
- Law 6 status confirmed before using form 20.
- No statement that EAS equals IFRS, and no audit opinion given.
- Refer when a company needs statements or an audit, when the entity is regulated, where EAS and IFRS differ, across the 2027 changeover, or for group work.

## Sources

| Source | URL | Read on |
|---|---|---|
| Law No. 150 of 2026 (Arts 1 to 3), gazette, rendered pages read | https://eta.gov.eg/sites/default/files/2026-08/law.no_.150.of_.2026.pdf | 2026-11-01 |
| Correction notice for Laws 149, 150, 151 of 2026 | https://eta.gov.eg/sites/default/files/2026-08/law.no_.149.150.151.of_.2026.retractation.pdf | 2026-11-01 |
| Unified Tax Procedures Law No. 206 of 2020, Arts 31, 38, 69 to 71, gazette text | https://eta.gov.eg/sites/default/files/2024-03/law_no.206-2020.pdf | 2026-11-01 |
| Law No. 6 of 2025, Arts 7 to 10, 12, 13 | https://eta.gov.eg/sites/default/files/2025-02/law_no.6.of_.2025.pdf | 2026-11-01 |
| MoF Decision No. 420 of 2025, Arts 1 to 4 | https://eta.gov.eg/sites/default/files/2025-12/mof.decision.no_.420.of_.2025.pdf | 2026-11-01 |
| FRA, legislation on accounting standards and auditors, list page only | https://fra.gov.eg/%d8%aa%d8%b4%d8%b1%d9%8a%d8%b9%d8%a7%d8%aa-%d9%85%d8%b9%d8%a7%d9%8a%d9%8a%d8%b1-%d8%a7%d9%84%d9%85%d8%ad%d8%a7%d8%b3%d8%a8%d8%a9-%d9%88%d9%85%d8%b1%d8%a7%d9%82%d8%a8%d9%8a-%d8%a7%d9%84%d8%ad%d8%b3-2/ | 2026-11-01 |

Not yet confirmed: the audit duty for all companies except partnerships (Companies Law 159 of 1981 and Capital Market Law text not opened); the statement list under EAS (financial position, comprehensive income, cash flows, changes in equity, notes); EAS history (2015 set; 2019 and 2023 amendments; IFRS 9, 15, 16 and 17 equivalents and the 1 July 2024 date); who applies EAS or full IFRS, including public-interest entities and EGX issuers; SME standards; Ministry of Investment Decision 166 of 2008; ISQM 1 and 2 from 2025; the claim that Decree 3725 cancels existing standards (the FRA list gives only the application date); FRA interim reporting cadence; bank-required audits of partnerships.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon. The most up-to-date version of this skill is maintained at [openaccountants.com](https://www.openaccountants.com).

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
