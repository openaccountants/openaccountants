---
name: eg-financial-statements
description: Use this skill whenever asked about Egyptian financial statements, financial reporting, or the accounting standards an Egyptian business must follow. Trigger on phrases like "Egypt financial statements", "Egyptian Accounting Standards", "EAS", "القوائم المالية", "المعايير المحاسبية المصرية", "do I file accounts Egypt", "audit Egypt company", "audited financial statements Egypt", "balance sheet Egypt", "IFRS Egypt", "EGX listed company accounts", "FRA filing", or any request to explain who must prepare, audit, or file financial statements in Egypt — and what a self-employed person files instead. ALWAYS read this skill before advising on Egyptian financial reporting or audit.
version: 1.0
jurisdiction: EG
tax_year: 2026
last_updated: 2026-07-13
review_status: pending_review
depends_on:
  - income-tax-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# EG Financial Statements

## Egypt Financial Statements & Financial Reporting (القوائم المالية) Skill v1.0

This skill explains who must prepare formal financial statements (القوائم المالية) in Egypt, which accounting standards apply (the Egyptian Accounting Standards — EAS / المعايير المحاسبية المصرية), when an audit by a registered auditor (مراجع حسابات / محاسب قانوني) is required, and how all of this is filed.

The headline for a self-employed reader: as a sole proprietor (منشأة فردية) or professional (مهنة حرة) you do NOT file formal statutory financial statements. You keep proper accounts/records and file the annual income-tax return with supporting accounts. Companies are different — and this skill explains exactly what changes if you incorporate.

Reply to the user in their own language (English or Arabic).

Cross-references:
- eg-bookkeeping — the books, records, and mandatory ETA digital systems.
- eg-income-tax — the annual income-tax return for individuals.
- eg-sme-tax — the simplified MSME regime (Law No. 6 of 2025), which is even lighter on reporting.

## Section 1 — Quick reference & conservative defaults

**Quick reference table**

- **Country** — Egypt (جمهورية مصر العربية)
- **Who prepares formal financial statements** — **Companies** (joint-stock شركة مساهمة, LLC ش.ذ.م.م, etc.). **NOT** sole proprietors / professionals — they file the income-tax return with supporting accounts
- **Standards** — **Egyptian Accounting Standards (EAS / المعايير المحاسبية المصرية)** — IFRS-aligned with local departures. Banks/insurers/regulated entities follow sector standards set by the FRA / Central Bank
- **IFRS** — EGX-listed companies and public-interest entities apply **EAS** (which is converged with IFRS); full IFRS is used by some multinational subsidiaries for group reporting. *Verify any specific entity's basis*
- **Currency** — EGP (Egyptian Pound — ج.م)
- **Authority** — **ETA** (Egyptian Tax Authority — مصلحة الضرائب المصرية) for tax filing **+ FRA** (Financial Regulatory Authority — الهيئة العامة للرقابة المالية) for capital-market/regulated entities; GAFI (الهيئة العامة للاستثمار) / commercial registry for company records
- **Filing** — Companies: audited financial statements filed **with the corporate tax return** (within 4 months of year-end) and, for regulated/listed entities, with the FRA/EGX. Individuals: income-tax return by **31 March** with supporting accounts
- **Audit** — Mandatory for all companies **except** partnerships (شركات الأشخاص — general & limited partnerships), per Companies Law & Capital Market Law. *Verify the partnership carve-out for the specific entity*
- **Quality tier** — **Research-verified — pending sign-off by an Egyptian accountant (محاسب قانوني)**
- **Skill version** — 1.0

### Conservative defaults

When a fact is uncertain, the AI must take the safer, more compliant path and tell the user it is doing so:

- If the taxpayer is a company, assume audited EAS financial statements are required and must be filed with the tax return, unless it is clearly a partnership (and even then, confirm — practice and lender/bank requirements often force an audit anyway).
- If the taxpayer is an individual (sole proprietor or professional), assume NO formal statutory financial statements — but assume the ETA still expects proper supporting accounts (income, costs, fixed-asset/depreciation schedules) behind the return. See eg-bookkeeping.
- Do not assume an entity is on the simplified MSME regime unless turnover is confirmed within the threshold and the taxpayer has opted in. See eg-sme-tax.
- Flag, do not guess, thresholds and effective dates. Egypt is mid-reform: new SME accounting/auditing standards and a 2027 overhaul of auditing standards are in train (see Section 6). Always tell the user to verify the current rule.

## Section 2 — Sole proprietor vs company: what each actually files

This is the most important distinction for a self-employed reader. Egyptian law treats a natural person (شخص طبيعي) very differently from a company (شخص اعتباري / شركة).

### 2a. Sole proprietor (منشأة فردية) and professional (مهنة حرة)

- **Sole proprietor taxation and filing** — A self-employed individual is taxed as a natural person under Income Tax Law No. 91 of 2005. They do not prepare or file a statutory set of financial statements (no audited balance sheet filed at a registry). What they DO: - Keep proper books and records — see eg-bookkeeping. Egypt's digital ecosystem (e-invoicing منظومة الفاتورة الإلكترونية, e-receipt منظومة الإيصال الإلكتروني) is increasingly the backbone of those records. - File the annual personal income-tax return by 31 March following the fiscal year. Commercial/industrial income (نشاط تجاري وصناعي) and professional income (مهن حرة) are declared on the return with supporting accounts: a statement of revenues and deductible costs, depreciation, and net taxable profit. - There is no statutory audit requirement for the individual's accounts. A voluntary review by an accountant is common where amounts are large or a bank asks for it. - A simplified MSME taxpayer (Law No. 6 of 2025, turnover ≤ EGP 20m) is even lighter: simplified record-keeping and stand-alone simplified forms, with the small-enterprise turnover-based regime instead of full profit accounting. See eg-sme-tax. *Verify the current turnover bands and opt-in conditions.*  _(Income Tax Law No. 91 of 2005; Law No. 6 of 2025)_

Plain-language framing for the user: "As a sole proprietor in Egypt you file your income-tax return with supporting accounts — not a full audited set of financial statements. If you form a company, that changes; see below."

### 2b. Company (شركة) — what changes on incorporation

- **What changes on incorporation** — Once you incorporate (most commonly a limited liability company / ش.ذ.م.م or a joint-stock company / شركة مساهمة), you become a separate legal person and: - You must prepare annual financial statements under EAS — typically a statement of financial position (balance sheet / قائمة المركز المالي), statement of comprehensive income (قائمة الدخل الشامل), statement of cash flows (قائمة التدفقات النقدية), statement of changes in equity (قائمة التغير في حقوق الملكية), and notes (الإيضاحات المتممة). - These statements must generally be audited by a registered auditor (مراجع حسابات مقيد) — except partnerships (see Section 4). - The audited financial statements are filed with the corporate income-tax return to the ETA (corporate returns are due within 4 months of year-end). - Regulated and listed entities additionally file with the FRA and, if EGX-listed, with the Egyptian Exchange; company records are maintained at GAFI / the commercial registry (السجل التجاري).

**Sole proprietor vs Company comparison table**

|  | Sole proprietor / professional | Company |
| --- | --- | --- |
| Legal person | Natural person | Separate legal entity |
| Formal financial statements | **No** | **Yes (EAS)** |
| Statutory audit | **No** | **Yes** (except partnerships) |
| Filed with | ETA income-tax return + supporting accounts | ETA tax return + (if regulated/listed) FRA/EGX |
| Deadline | **31 March** (individual) | **Within 4 months** of year-end (corporate) |
| Standards | n/a (records only) | EAS (IFRS-aligned) |

## Section 3 — Egyptian Accounting Standards (EAS) overview + IFRS

### 3a. What EAS is

- **What EAS is** — The Egyptian Accounting Standards (EAS / المعايير المحاسبية المصرية) are the mandatory reporting framework for companies in Egypt. They are based on and largely converged with IFRS, but are not identical — there are local departures and a lag behind the latest IFRS amendments. Key points (research-verified): - The current comprehensive EAS set was issued in 2015, with significant amendments in 2019 and 2023. - The 2019 update added standards mirroring IFRS 9 (financial instruments), IFRS 15 (revenue from contracts with customers), and IFRS 16 (leases). - In early 2023 a standard similar to IFRS 17 (insurance contracts) was issued, effective for periods beginning on or after 1 July 2024. - EAS includes special/simplified requirements for small and medium-sized entities (SMEs).

Caveat to surface to the user: EAS is IFRS-aligned, not IFRS itself. Recognition or measurement under EAS can differ from current IFRS (e.g., timing of newly adopted standards, certain local treatments). Never tell a user "EAS = IFRS." *Verify the specific standard.*

### 3b. EAS vs full IFRS — who uses what

- **EAS vs full IFRS applicability** — - Public interest entities (PIEs) — listed companies, public-subscription companies, securities companies, and investment funds established by banks and insurance companies — apply EAS. - EGX-listed companies report under EAS (the IFRS-converged Egyptian framework), not a separate "full IFRS" mandate. *Verify for a specific issuer, as some prepare additional IFRS group packs.* - Banks follow standards set by the Central Bank of Egypt (CBE); insurers and other non-bank financial entities follow standards/regulation set by the FRA (الهيئة العامة للرقابة المالية). - Multinational subsidiaries often also prepare full IFRS for group consolidation in addition to local EAS statutory accounts.

## Section 4 — Audit requirements (المراجعة)

### 4a. Who must be audited

- **Who must be audited** — Under the Companies Law and the Capital Market Law, all companies must prepare annual audited financial statements — except partnership companies (شركات الأشخاص) and limited partnership companies. The audit must be performed by a registered auditor (مراجع حسابات مقيد بسجل المراجعين). - Joint-stock (شركة مساهمة) and LLC (ش.ذ.م.م): audit required. - Partnerships (general / limited): statutory carve-out — but lenders, banks, partners, or the ETA may still require audited or reviewed accounts in practice. *Verify for the specific entity.* - Sole proprietor / professional: no statutory audit (natural person).  _(Companies Law; Capital Market Law)_

### 4b. Auditing standards

- **Auditing standards, quality management, and 2027 reform** — - Egypt's auditing standards are the Egyptian Standards on Auditing, Review and Other Assurance Services (ESAROAS), adopted by Ministry of Investment Decision No. 166/2008 and aligned with the International Standards on Auditing (ISA). - Quality management: ISQM 1 and ISQM 2 are being applied (reported effective from 2025 per the profession's SMO action plan). - Major reform ahead: Prime Minister Decree No. 3725 of 2025 approved new Egyptian auditing/financial-review standards that cancel the existing standards from 1 January 2027 — the first comprehensive update since 2008. *Flag this date to any user planning a 2027+ audit.*  _(Ministry of Investment Decision No. 166/2008; Prime Minister Decree No. 3725 of 2025)_

## Section 5 — Worked examples

### Example 1 — Freelance developer, sole proprietor (the common self-employed case)

Layla is a freelance software developer registered as a sole proprietor (منشأة فردية), turnover ~EGP 1.2m in 2025.

- Financial statements? No. As a natural person she files an income-tax return, not statutory audited financials.
- Audit? No statutory audit.
- What she files: annual personal income-tax return by 31 March 2026 for FY2025, with supporting accounts (revenues, deductible costs, depreciation, net taxable profit). She keeps records via the ETA digital systems (eg-bookkeeping).
- Could the MSME regime help? Her turnover is under EGP 20m, so she may qualify for the simplified regime with even lighter record-keeping — route to eg-sme-tax to confirm bands and opt-in. *Verify thresholds.*

> Reply: "You don't prepare or file formal financial statements. File your income-tax return with supporting accounts; no audit is required."

### Example 2 — The same developer incorporates an LLC (ش.ذ.م.م)

Layla converts to a single-shareholder/limited liability company to win larger contracts.

- Financial statements? Yes — full EAS set (financial position, comprehensive income, cash flows, changes in equity, notes).
- Audit? Yes — by a registered auditor (LLC is not a partnership).
- What she files: corporate income-tax return within 4 months of year-end, with the audited EAS statements attached; company records at GAFI / commercial registry.
- Standards: EAS (IFRS-aligned). She does not report under full IFRS unless a group/lender requires it.

> Reply: "Incorporating triggers audited EAS financial statements filed with your corporate tax return — a significant step up in compliance from the sole proprietor return."

### Example 3 — Listed company on the EGX

A client is a joint-stock company listed on the Egyptian Exchange.

- Standards: EAS (the IFRS-converged Egyptian framework). As a public-interest entity it applies the full EAS set, audited under ESAROAS/ISA.
- Filing: audited statements filed with the ETA (tax), the FRA, and the EGX, plus periodic/interim reporting per FRA listing rules. *Verify current interim-reporting cadence with the FRA.*

> Reply: "Listed and regulated entities report under EAS and file with the ETA, the FRA, and the EGX — well beyond a self-employed person's obligations."

## Section 6 — Tier 2 escalation & references

### Escalate to a qualified Egyptian accountant (محاسب قانوني) when:

- **Escalation triggers** — - The entity is a company and needs statutory financial statements or an audit — the auditor must be registered and sign the report. - The entity is regulated (bank, insurer, securities firm, fund) — FRA/CBE sector standards apply, outside this skill's scope. - A transaction touches a standard where EAS departs from IFRS (financial instruments, leases, revenue, insurance, deferred tax). - Anything spanning the 2027 auditing-standards changeover (Decree 3725/2025) or the new SME accounting/auditing standards still being rolled out. - Group/IFRS consolidation, transfer pricing, or business-combination accounting.

### References (verify before relying)

- Income Tax Law No. 91 of 2005 — taxation of natural persons and companies.
- Unified Tax Procedures Law No. 206 of 2020 — returns, records, deadlines.
- MSME / SME tax incentives — Law No. 6 of 2025 (turnover ≤ EGP 20m; simplified accounting/forms). See eg-sme-tax.
- Companies Law and Capital Market Law — financial statements & audit.
- Egyptian Accounting Standards (EAS) — 2015 set, amended 2019 & 2023.
- ESAROAS — auditing standards, MoI Decision No. 166/2008 (ISA-aligned); Decree No. 3725 of 2025 new standards effective 1 Jan 2027.
- ETA — eta.gov.eg | FRA — fra.gov.eg | EGX — egx.com.eg | GAFI.
- Big-4 / IFRS Foundation jurisdiction profile for Egypt; PwC Tax Summaries — Egypt.

## PROHIBITIONS

- **AI prohibitions** — The AI applying this skill must NOT: - Tell a sole proprietor or professional that they must file statutory financial statements or be audited. Natural persons file the income-tax return with supporting accounts — not audited financials. - State that EAS is identical to IFRS. EAS is IFRS-aligned with local departures and an adoption lag. Flag standard-specific differences. - Assert audit thresholds, turnover bands, or effective dates as settled. Egypt is mid-reform (SME standards; 2027 auditing overhaul; MSME bands). Mark these "verify" and route to a qualified accountant. - Sign, certify, or imply audit opinion or assurance. Only a registered Egyptian auditor (مراجع حسابات مقيد) may audit and sign. - Apply this skill to banks, insurers, or other FRA/CBE-regulated entities — they follow sector standards outside scope. - Replace a credentialed reviewer. All output is research-verified and pending sign-off by a qualified Egyptian accountant.

## Disclaimer

This skill is research-verified against public sources (Egyptian Accounting Standards materials, the IFRS Foundation jurisdiction profile, the Financial Regulatory Authority, PwC, and Big-4 commentary) and is pending sign-off by a qualified Egyptian accountant (محاسب قانوني). It is general information for self-employed people and small businesses, not professional accounting, audit, or legal advice. Thresholds, standards, and filing rules change — and several Egyptian reforms are in progress for 2025–2027. Verify the current position with the ETA, the FRA, and a registered Egyptian accountant before acting. Part of the open-source tax skills at openaccountants.com.

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
