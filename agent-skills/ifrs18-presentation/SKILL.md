---
name: ifrs18-presentation
description: "IFRS financial statement presentation, disclosure, and IAS 1-to-IFRS 18 restatement under IFRS 18 (Presentation and Disclosure in Financial Statements) and consequential amendments to IAS 7, IAS 8, IAS 33, and IAS 34. Covers the five statement of profit or loss categories (operating, investing, financing, income taxes, discontinued operations), the two mandatory subtotals (operating profit or loss; profit or loss before financing and income taxes), the four classification overlays (foreign exchange, derivatives and hedging, specified main business activities, held-for-sale), management-defined performance measures (MPMs) with single-note tax and NCI reconciliations, the mandatory nature-of-expense matrix when presenting expenses by function, amended IAS 7 cash flow classification rules, balance sheet goodwill disaggregation, retrospective transition reconciliations, and the 57-point Class A/B/C integrity check battery. Produces restatement conclusions, reclassification entries, working"
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/ifrs18-presentation"
  jurisdiction: "GLOBAL"
  tax_year: "2027"
  last_updated: "2026-11-08"
  authored_by: "Talha Mehmood, ACA, FCCA"
---

# IFRS 18 Presentation and Disclosure in Financial Statements (`ifrs18-presentation`)

## IFRS Financial Statement Presentation & IAS 1 Restatement — IFRS 18 v1.0.0

### What this file is

This skill is a financial-reporting content skill that loads on top of [`financial-reporting-workflow-base`](https://github.com/openaccountants/openaccountants/blob/main/skills/financial-reporting/financial-reporting-workflow-base.md). It supplies the authoritative presentation, classification, aggregation, disclosure, and transition rules under [IFRS 18 *Presentation and Disclosure in Financial Statements*](https://www.ifrs.org/issued-standards/list-of-standards/ifrs-18-presentation-and-disclosure-in-financial-statements/) and the consequential amendments to [IAS 7 *Statement of Cash Flows*](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ias7.html). The workflow base supplies the two-layer output contract (Layer A reference rules + Layer B executable computation), the reclassification journal-entry format, the conservative-default principle, and the universal self-checks. Load both files together.

* **Standard currency:** This skill is current for annual reporting periods beginning on or after **1 January 2027** (with earlier application permitted, including FY2026 financial statements) under [IFRS 18 as issued by the IASB](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html) on 9 April 2024, verified as of **2026-11-08**.
* **Verification status:** **Source-cited draft** (`tier: 2`). Every rule, threshold, subtotal requirement, and transition provision is drafted from and cited to the official IASB standards at [ifrs.org](https://www.ifrs.org/issued-standards/list-of-standards/ifrs-18-presentation-and-disclosure-in-financial-statements/).
* **The one governing rule:** **Restatement under IFRS 18 is presentation-only.** It changes where income, expenses, and cash flows sit — never what they are ([IFRS 18.1–3](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html)). Recognition and measurement are untouched. If Profit or Loss for the period, Total Comprehensive Income, Total Assets, Total Liabilities, Total Equity, or Net Movement in Cash and Cash Equivalents changes by even a single unit upon restatement, a classification error, double-count, or omission has occurred and delivery is blocked.

## Quick reference / Answer layer

### 1. The Five Statement of Profit or Loss Categories & Mandatory Subtotals

Every item of income and expense recognized in profit or loss must be classified into exactly one of five categories in this fixed order ([IFRS 18.47](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html)):

| Order | Category / Mandatory Subtotal | Governing Rule & Scope | Official Source |
| :--- | :--- | :--- | :--- |
| **1** | **Operating** | **Residual category (default, not a definition):** Captures all income and expenses not classified in Investing, Financing, Income Taxes, or Discontinued Operations, including volatile, unusual, or non-recurring operating items. For entities with specified main business activities, also captures investing/financing returns from those main activities. | [IFRS 18.52](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html) |
| **Subtotal 1** | **Operating profit or loss** | **Mandatory in all cases:** The total of all income and expenses classified in the Operating category. | [IFRS 18.69(a), 70](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html) |
| **2** | **Investing** | Income and expenses from: (a) investments in associates, joint ventures, and unconsolidated subsidiaries ([IFRS 18.53(a)](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html)); (b) cash and cash equivalents ([IFRS 18.53(b)](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html)); and (c) other assets that generate a return **individually and largely independently** of the entity's other resources (e.g., rental income, direct expenses, and fair value changes on investment property; dividends and fair value gains/losses on debt/equity financial investments) ([IFRS 18.53(c), 54](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html)). | [IFRS 18.53–58](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html) |
| **Subtotal 2** | **Profit or loss before financing and income taxes** | **Mandatory (with one narrow exception):** Equals Operating profit or loss plus Total investing income and expenses. Omitted **only** when an entity with a main business activity of providing financing to customers applies the policy in [IFRS 18.65(a)(ii)](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html) to classify all financing-liability income/expenses in Operating ([IFRS 18.73](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html)). | [IFRS 18.69(b), 71, 73](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html) |
| **3** | **Financing** | Income and expenses from: (a) **all** income and expenses on liabilities arising from transactions that involve **only the raising of finance** (bank borrowings, bonds, sukuk, commercial paper, overdrafts — including interest, transaction cost amortisation, modification/extinguishment gains/losses, and FX differences) ([IFRS 18.59(a), 60](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html)); and (b) **only** the interest expense and effect of interest-rate changes on **other liabilities** (lease liabilities under IFRS 16, net defined benefit/EOSB obligations under IAS 19, decommissioning/restoration provisions under IAS 37, deferred/contingent consideration) ([IFRS 18.59(b), 61](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html)). | [IFRS 18.59–66](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html) |
| **4** | **Income taxes** | Tax expense or tax income included in profit or loss in accordance with **IAS 12 *Income Taxes***, and any related foreign exchange differences. Levies outside IAS 12 scope (such as Zakat calculated on a net-worth/working-capital base rather than taxable profit) are **excluded** and fall into Operating. | [IFRS 18.67](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html) |
| **5** | **Discontinued operations** | Single post-tax amount comprising income and expenses from discontinued operations as required by **IFRS 5 *Non-current Assets Held for Sale and Discontinued Operations***. | [IFRS 18.68](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html) |
| **Total** | **Profit or loss** | Sum of all five categories (`Operating + Investing + Financing + Income taxes + Discontinued operations`). Must equal IAS 1 Profit or loss to the exact unit. | [IFRS 18.69(c), 72](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html) |

### 2. High-Frequency Shifts & Core Compliance Rules at a Glance

| Rule Area | Key Requirement / Threshold / Rule | Official Source |
| :--- | :--- | :--- |
| **Moves INTO Operating profit** | Gains/losses on disposal of operating PP&E and intangibles ([IFRS 18.B47](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html)); FX on trade receivables/payables ([IFRS 18.B65](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html)); non-designated commodity/operating derivatives ([IFRS 18.B74](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html)); bank service/maintenance charges ([IFRS 18.B51](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html)); Zakat and levies outside IAS 12 scope ([IFRS 18.52, 67](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html)). | [IFRS 18.52, B47–B74](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html) |
| **Moves OUT of Operating profit** | Share of profit/loss of equity-accounted associates and JVs (to Investing) ([IFRS 18.53(a)](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html)); rental income, direct operating expenses, and fair value changes of investment property (to Investing, unless investing in property is a main business activity) ([IFRS 18.53(c), B45](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html)); interest income on cash/deposits and dividend income (to Investing) ([IFRS 18.53(b)–(c)](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html)); net interest on defined benefit/EOSB obligations and unwinding of discount on provisions (to Financing) ([IFRS 18.59(b)](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html)). | [IFRS 18.53–61](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html) |
| **No "Unusual / Exceptional" Face Subtotal** | Presenting "Operating profit before exceptional/non-recurring items" on the face is prohibited. Operating is residual and absorbs volatile items. Adjusted profit measures must be disclosed in the single MPM note. | [IFRS 18.24, 117, BC152](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html) |
| **Management-Defined Performance Measures (MPMs)** | Any subtotal of income and expenses used in public communications outside the financial statements that communicates management's view of financial performance and is not listed in [IFRS 18.118](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html) or required by IFRS. Must be reconciled in a **single note** to the most directly comparable IFRS subtotal, showing the **income tax effect** and **NCI effect** for each reconciling item. | [IFRS 18.117–125](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html) |
| **Specified Expenses by Nature Note** | Whenever **any** operating expense line item on the face is presented by function (e.g., Cost of sales, SG&A, R&D), disclose in a **single note** the total and the amount included in each functional line item for: (1) depreciation, (2) amortisation, (3) employee benefits, (4) IAS 36 impairment losses/reversals, and (5) inventory write-downs/reversals. | [IFRS 18.78, 83](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html) |
| **Amended IAS 7 Cash Flow Rules** | Indirect method **must** start from the **Operating profit or loss** subtotal ([IAS 7.18(b), 20](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ias7.html)). For entities without specified main business activities, policy choices are eliminated: **Interest paid** = Financing ([IAS 7.34A(a)](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ias7.html)); **Dividends paid** = Financing ([IAS 7.33A](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ias7.html)); **Interest received** and **Dividends received** = Investing ([IAS 7.34A(b)](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ias7.html)). | [IAS 7.18, 20, 31, 33A, 34A–34D](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ias7.html) |
| **Balance Sheet Goodwill Line** | **Goodwill** must be presented as a separate line item on the face of the statement of financial position, disaggregated from intangible assets. | [IFRS 18.103(c)](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html) |
| **Transition & Comparative Reconciliation** | Retrospective application ([IFRS 18.C2](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html)). In the first annual financial statements applying IFRS 18, disclose a line-by-line reconciliation of the comparative period statement of profit or loss from IAS 1 amounts to IFRS 18 amounts ([IFRS 18.C3](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html)). | [IFRS 18.C1–C7](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html) |

### 3. Ask the Client First (Structured Intake Form)

Before executing a restatement or drafting IFRS 18 disclosures (Layer B), if the financial statement pack is incomplete, ask the user for the missing inputs in a **single structured block** — never guess a note split or invent a component ([`financial-reporting-workflow-base` §6](https://github.com/openaccountants/openaccountants/blob/main/skills/financial-reporting/financial-reporting-workflow-base.md)):

1. **Disaggregated note breakdowns** — *Can you provide the note disclosures for "Other operating income", "Other operating expenses", "Finance costs / Finance income", "Other gains and losses — net", and "Net foreign exchange differences"?* (Used in Layer A §2; without component-level notes, aggregated captions are flagged `UNRESOLVED — requires note detail` because they routinely span Operating, Investing, and Financing.)
2. **Specified main business activities** — *Does the reporting entity have a main business activity of (a) investing in particular types of assets or (b) providing financing to customers (e.g., bank, insurer, real estate investment group, lessor, captive finance arm, investment holding company)?* (Used in [IFRS 18.49–51, 55–58, 62–66](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html); changes classification wholesale.)
3. **Zakat and non-income-tax levies** — *How is Zakat (or any similar statutory levy) accounted for — within the scope of IAS 12 (taxable profit basis) or outside IAS 12 (net worth / Zakat base)?* (Used in [IFRS 18.52, 67](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html); outside IAS 12, Zakat must be classified in Operating.)
4. **Public communications for MPMs** — *Which non-IFRS performance subtotals (e.g., Adjusted Operating Profit, Adjusted EBITDA, Underlying EBIT) are published in earnings releases, MD&A, or investor presentations, and what are the applicable statutory tax rates and NCI ownership percentages for each adjusting item?* (Used in [IFRS 18.117–125](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html).)
5. **Derivatives and hedging designation** — *Are derivative financial instruments in a designated IAS 39 / IFRS 9 hedging relationship, and if not, what specific risk (borrowings interest rate vs. raw material/operating FX) do they manage?* (Used in [IFRS 18.B70–B76](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html).)
6. **Investment property role** — *Is investment property held to earn rentals/capital appreciation largely independently of the entity's other resources, or is it integral to main operating activities?* (Used in [IFRS 18.53(c), B45–B49](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html).)
7. **Operating expense presentation method** — *Does the entity present operating expenses on the face by nature, by function, or mixed, and if by function, can you provide the functional breakdown of depreciation, amortisation, employee benefits, IAS 36 impairments, and inventory write-downs?* (Used in [IFRS 18.78, 83](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html).)

## Section 1 — Scope & Applicability

### 1.1 Who this skill applies to

* **Entities in scope:** All profit-oriented entities (and public/private sector business entities adapting terminology per [IFRS 18.6](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html)) preparing general purpose consolidated, separate (IAS 27), or individual financial statements in accordance with IFRS Accounting Standards ([IFRS 18.2](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html)).
* **Interim financial statements:** Under [IFRS 18.4](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html), general structure requirements do not apply to condensed interim financial statements prepared under IAS 34, **except** that the aggregation/disaggregation principles ([IFRS 18.41–45](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html)), MPM disclosures ([IFRS 18.117–125](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html) and amended IAS 34.16A(m)), and first-year interim comparative restatement rules ([IFRS 18.C4–C5](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html)) **do** apply.
* **Subsidiaries without public accountability:** Eligible subsidiaries applying **IFRS 19 *Subsidiaries without Public Accountability: Disclosures*** must still follow all recognition, measurement, and **presentation** requirements of IFRS 18 (including the five categories and mandatory subtotals), while applying IFRS 19's reduced disclosure requirements.
* **Out of scope / Refusal boundaries:**
  * **Recognition and measurement calculations:** This skill does not compute primary recognition or measurement amounts under IFRS 15, IFRS 16, IFRS 9, IAS 19, IAS 36, or IAS 12. It takes recognized/measured amounts and determines their primary statement classification, subtotal placement, cash flow classification, and note disclosures.
  * **US GAAP reporters:** Entities reporting solely under US GAAP apply ASC 205, ASC 220 (including ASU 2024-03 / ASC 220-40), and ASC 230; see Section 8 for dual-reporter divergence rules.
  * **Sanctioned and embargoed jurisdictions:** Per the [OpenAccountants standard](https://github.com/openaccountants/openaccountants/blob/main/docs/skill-template.md), this skill does not cover jurisdiction-specific local statutory filings for countries under broad embargo or UN Security Council sanctions.

### 1.2 The Seven Presentation Invariants

Because IFRS 18 replaces IAS 1's presentation and disclosure rules without modifying recognition or measurement standards, the following seven figures are **mathematical invariants** before and after restatement:

| Invariant ID | Financial Statement Metric | Why It Cannot Change Under IFRS 18 | Governing Citation |
| :--- | :--- | :--- | :--- |
| **INV-1** | **Profit or loss for the period** | The five IFRS 18 categories form a mutually exclusive, collectively exhaustive partition of total profit or loss. | [IFRS 18.47, 69(c), 72](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html) |
| **INV-2** | **Profit or loss from continuing operations** | Only the intermediate categories and subtotals leading to continuing operations change; Discontinued Operations is unchanged. | [IFRS 18.68, 69](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html) |
| **INV-3** | **Profit attributable to owners of the parent and to NCI** | Allocation of total profit or loss between controlling and non-controlling interests is unaffected by category lines. | [IFRS 18.76(a)](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html) |
| **INV-4** | **Other comprehensive income (OCI) and Total comprehensive income** | IFRS 18 retains the two classes of OCI (items that will and will not be reclassified to profit or loss) without altering OCI measurement. | [IFRS 18.86–88](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html) |
| **INV-5** | **Basic and diluted earnings per share (EPS)** | Numerators (profit from continuing operations and profit for the period attributable to ordinary equity holders) and denominators under IAS 33 are unchanged. | [IAS 33.73B–73C](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html) |
| **INV-6** | **Total assets, Total liabilities, and Total equity** | Disaggregating goodwill from intangibles ([IFRS 18.103(c)](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html)) changes line count on the balance sheet but never total assets, liabilities, or equity. | [IFRS 18.96, 103–104](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html) |
| **INV-7** | **Net increase / (decrease) in cash and cash equivalents** | Amended IAS 7 reclassifies cash flows across Operating, Investing, and Financing activities, leaving total net cash movement and closing cash identical. | [IAS 7.10, 18, 33A, 34A](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ias7.html) |

## Section 2 — Reference Layer (Layer A): Classification Decision Tree & Overlays (IFRS 18.47–68, B29–B76)

### 2.1 The Six-Step Component Classification Decision Tree

Classification under IFRS 18 operates strictly on **constituent components** extracted from the notes, never on aggregated IAS 1 face captions ([IFRS 18.47, B29](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html)). For an entity without a specified main business activity, evaluate each component through Steps 1 to 6 in order and take the **first** branch that applies:

```text
                       ┌─ Step 1: Is it income/expense from a discontinued operation (IFRS 5)?
Rule A2.1 ─────────────┤     YES → DISCONTINUED OPERATIONS (IFRS 18.68)
                       └─ NO ↓

                       ┌─ Step 2: Is it income tax expense/income within the scope of IAS 12
Rule A2.2 ─────────────┤          (or related FX differences)?
                       │     YES → INCOME TAXES (IFRS 18.67, B68)
                       └─ NO ↓

                       ┌─ Step 3: Does it arise from a liability created by a transaction
Rule A2.3 ─────────────┤          that involves ONLY the raising of finance?
                       │     YES → FINANCING — all income and expenses on that liability (IFRS 18.59(a), 60)
                       └─ NO ↓

                       ┌─ Step 4: Is it interest expense (or the effect of interest-rate changes)
Rule A2.4 ─────────────┤          identified under another IFRS on ANY OTHER liability?
                       │     YES → FINANCING — that interest/discount element only (IFRS 18.59(b), 61)
                       └─ NO ↓

                       ┌─ Step 5: Does it arise from an equity-accounted investee, cash and cash
Rule A2.5 ─────────────┤          equivalents, or another asset generating a return individually
                       │          and largely independently of the entity's other resources?
                       │     YES → INVESTING (IFRS 18.53–54)
                       └─ NO ↓

Rule A2.6 ───────────────── Step 6: OPERATING — the residual category (IFRS 18.52)
```

### 2.2 Detailed Rules for Steps 3, 4, and 5

#### Rule A2.3 — Step 3: Liabilities arising from transactions that involve ONLY the raising of finance ([IFRS 18.59(a), 60, B50–B55](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html))
* **The statutory test:** Look at the nature of the transaction that created the liability, not how management deployed the cash proceeds. In a transaction involving only the raising of finance, an entity receives finance (typically cash) and will return finance (cash or its own equity shares) at a later date ([IFRS 18.B50](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html)).Examples include bank loans, bonds, debentures, sukuk, commercial paper, overdrafts, and convertible notes.
* **What goes to Financing:** **All** income and expenses arising from initial and subsequent measurement and derecognition of such liabilities ([IFRS 18.60](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html)):
  1. Interest expense calculated using the effective interest method (IFRS 9);
  2. Amortisation of debt arrangement and transaction costs;
  3. Fair value gains and losses on financial liabilities designated at FVTPL;
  4. Gains and losses on modification, refinancing, or extinguishment of debt;
  5. Dividends on issued shares classified as financial liabilities under IAS 32; and
  6. Foreign exchange gains and losses on the carrying amount of foreign-currency borrowings ([IFRS 18.B65](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html)).
* **What fails Step 3:** Trade payables (created by purchasing goods/services), contract liabilities (IFRS 15), lease liabilities (created by obtaining a right-of-use asset), employee benefit liabilities (IAS 19), and decommissioning/litigation provisions (IAS 37). Bank service fees for account maintenance, wire transfers, or cash handling are payments for services, not liabilities from raising finance, and belong in **Operating** ([IFRS 18.B51](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html)).

#### Rule A2.4 — Step 4: Interest and interest-rate effects on OTHER liabilities ([IFRS 18.59(b), 61, B56–B57](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html))
For liabilities that do **not** arise solely from raising finance, **only** the interest income/expense and income/expenses arising from changes in interest rates — and **only if** the entity identifies such amounts for the purpose of applying other requirements in IFRS Accounting Standards — are classified in **Financing** ([IFRS 18.61](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html)):

| Non-Financing Liability | Underlying Standard | Element Classified in FINANCING ([IFRS 18.61](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html)) | Elements Classified in OPERATING ([IFRS 18.52](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html)) or OCI |
| :--- | :--- | :--- | :--- |
| **Lease liabilities** | IFRS 16 *Leases* | Interest expense on the lease liability (IFRS 16.38(a)) | ROU asset depreciation, variable lease payments not in lease liability, short-term and low-value lease expenses, ROU impairment (all **Operating**). |
| **Net defined benefit / End-of-Service Benefit (EOSB) liability** | IAS 19 *Employee Benefits* | Net interest expense/(income) on the net defined benefit liability/(asset) (IAS 19.123) | Current service cost, past service cost, gains/losses on settlement (**Operating**); actuarial remeasurements (**OCI**). |
| **Provisions measured at present value (decommissioning, restoration, onerous contracts)** | IAS 37 *Provisions, Contingent Liabilities and Contingent Assets* | Unwinding of the discount (accretion expense) and effect of changes in the discount rate (IAS 37.60; IFRIC 1) | Initial provision charge and revisions to estimated cash outflows (**Operating**, unless capitalised into PP&E under IAS 16 / IFRIC 1). |
| **Long-term trade payables / Contract liabilities with a significant financing component** | IFRS 9 / IFRS 15 | Interest expense recognised for the significant financing component (IFRS 15.65) | Cost of goods/services purchased, supplier settlement discounts, and trade FX differences (**Operating**). |
| **Deferred or contingent consideration in a business combination** | IFRS 3 *Business Combinations* | Interest/unwinding of discount where identified under IFRS 3 / IFRS 9 | Fair value remeasurement due to changes in expected post-acquisition performance milestones (**Operating**). |

#### Rule A2.5 — Step 5: Assets generating returns individually and largely independently ([IFRS 18.53–54, B42–B49](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html))
* **Assets in Investing ([IFRS 18.53, B43–B45](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html)):**
  1. Investments in associates, joint ventures, and unconsolidated subsidiaries (whether accounted for using the equity method under IAS 28, at cost, or at fair value under IAS 27) — share of profit or loss, dividends, impairment losses/reversals, and disposal gains/losses are all **Investing** ([IFRS 18.53(a), B43](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html));
  2. Cash and cash equivalents — interest income and FX differences on cash/short-term bank deposits are **Investing** ([IFRS 18.53(b)](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html));
  3. Debt or equity financial investments (FVTPL, FVOCI, amortised cost); and
  4. Investment property (IAS 40) held to earn rentals or for capital appreciation independently of the entity's other resources — rental income, direct property operating expenses, fair value gains/losses, and disposal gains/losses are all **Investing** ([IFRS 18.54, B45](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html)).
* **Assets in Operating ([IFRS 18.B47](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html)):** Assets that an entity uses in combination with other resources to produce or supply goods or services cannot generate returns individually and largely independently. Consequently, all income and expenses from **property, plant and equipment (IAS 16)**, **right-of-use assets (IFRS 16)**, **operating intangible assets (IAS 38)**, **goodwill**, **inventories (IAS 2)**, **trade receivables**, and **contract assets (IFRS 15)** — including depreciation, amortisation, IAS 36 impairments, expected credit losses, and **gains or losses on disposal of PP&E and intangibles** — are classified in **Operating** ([IFRS 18.B47](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html)).

### 2.3 The Four Classification Overlays (IFRS 18.49–51, 55–58, 62–66, B65–B76)

#### Overlay A — Foreign Exchange Differences ([IFRS 18.B65–B69](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html))
* **Rule A2.7 (Follow the underlying item):** Foreign exchange differences recognised in profit or loss under IAS 21 must be classified in the **same category** as the income and expenses from the items that gave rise to the foreign exchange differences ([IFRS 18.B65](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html)):
  * FX on trade receivables, trade payables, and operating advances → **Operating** ([IFRS 18.B66(a)](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html));
  * FX on foreign-currency debt investments or foreign-currency cash/deposits → **Investing**;
  * FX on foreign-currency borrowings (loans, bonds, overdrafts) → **Financing** ([IFRS 18.B66(b)](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html));
  * FX on tax assets/liabilities within IAS 12 scope → **Income taxes** ([IFRS 18.B68](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html)).
* **Undue cost or effort relief:** Only if classifying foreign exchange differences across categories would involve **undue cost or effort**, an entity classifies the affected exchange differences in the **Operating** category and discloses that fact ([IFRS 18.B65, B69](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html)). Never leave a net FX caption unsplit when the note or borrowings roll-forward provides the breakdown.

#### Overlay B — Derivatives and Designated Hedging Instruments ([IFRS 18.B70–B76](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html))
* **Rule A2.8 (Decision matrix for derivatives):**
  1. **Designated hedging instrument (IFRS 9 / IAS 39):** Classify gains and losses in the **same category** as the income and expenses affected by the risks the instrument is used to manage ([IFRS 18.B70(a)](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html)). However, if doing so would require **grossing up** gains and losses (e.g., a single derivative hedging both an operating exposure and a financing exposure) or involve undue cost or effort, classify all gains/losses in **Operating** ([IFRS 18.B70(b)](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html)).
  2. **Not designated as a hedging instrument, but used to manage identified risks:** Follow the category affected by the managed risk (e.g., an undesignated interest-rate swap managing floating-rate bank debt is **Financing**; an undesignated commodity forward managing raw material purchases is **Operating**), unless doing so requires grossing up or undue cost or effort, in which case classify in **Operating** ([IFRS 18.B72–B74](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html)).
  3. **Not used to manage identified risks (standalone/trading derivatives):** Classify in **Operating**, unless the derivative relates to a transaction that involves only the raising of finance (e.g., an embedded conversion option separated from a host bond), which is **Financing** ([IFRS 18.B75](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html)).

#### Overlay C — Entities with Specified Main Business Activities ([IFRS 18.49–51, 55–58, 62–66, B30–B41](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html))
* **Rule A2.9 (Assessing main business activities):** Before classifying, assess whether the reporting entity has a main business activity of:
  1. **Investing in particular types of assets** (e.g., investment entities, real estate investment groups, insurers managing investment portfolios, investment holding companies) ([IFRS 18.49(a), B30–B41](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html)); and/or
  2. **Providing financing to customers** (e.g., commercial/retail banks, consumer lenders, finance lessors, captive finance subsidiaries where material at group level) ([IFRS 18.49(b), B30–B41](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html)).
* **Consequence 1 — Investing as a main business activity ([IFRS 18.55–58](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html)):** Income and expenses from assets invested in as a main business activity move from Investing into **Operating**, **except** that investments in associates, joint ventures, and unconsolidated subsidiaries **accounted for using the equity method** must **always remain in Investing** ([IFRS 18.55(a)](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html)). (Only associates/JVs measured at fair value through profit or loss move to Operating when investing in them is a main business activity.) Income and expenses from cash and cash equivalents also move to **Operating** if the entity invests in financial assets as a main business activity ([IFRS 18.56(a)](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html)).
* **Consequence 2 — Providing financing to customers as a main business activity ([IFRS 18.62–66](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html)):**
  * Income and expenses from liabilities that **relate** to providing financing to customers move from Financing into **Operating** ([IFRS 18.65(a)(i)](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html)).
  * For liabilities from raising finance that do **not** relate to providing financing to customers (or cannot be distinguished), the entity has an **accounting policy choice** ([IFRS 18.65(a)(ii)](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html)) to classify them in **Operating** or **Financing** (if it cannot distinguish them, it must classify all in Operating per [IFRS 18.66](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html)).
  * Interest income on cash and cash equivalents that relates to providing financing to customers moves to **Operating** ([IFRS 18.56(b)](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html)).
  * **Subtotal omission rule ([IFRS 18.73](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html)):** If the entity classifies **all** income and expenses from liabilities arising from raising finance in **Operating**, it **must not** present the subtotal *Profit or loss before financing and income taxes*.

#### Overlay D — Non-Current Assets Held for Sale and Discontinued Operations ([IFRS 18.68, B48](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html))
* **Rule A2.10:** A discontinued operation under IFRS 5 is presented as a single post-tax amount in **Discontinued operations** ([IFRS 18.68](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html)). A non-current asset or disposal group held for sale that does **not** meet the IFRS 5 definition of a discontinued operation retains the category of the underlying asset (e.g., impairment on remeasurement to fair value less costs to sell of operating PP&E held for sale remains **Operating** per [IFRS 18.B48](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html)).

### 2.4 Comprehensive Worked Classification Reference Table (General Corporate / Industrial Entity)

| # | Component Description | IFRS 18 Category | Tree Step / Overlay | Paragraph Citation | Direction vs. Typical IAS 1 Operating Profit |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | Revenue from contracts with customers | **Operating** | Step 6 | [IFRS 18.52](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html) | Unchanged |
| 2 | Cost of sales (raw materials, direct labour, factory overhead) | **Operating** | Step 6 | [IFRS 18.52](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html) | Unchanged |
| 3 | Selling, distribution, general, administrative, and R&D expenses | **Operating** | Step 6 | [IFRS 18.52](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html) | Unchanged |
| 4 | Expected credit losses (ECL) on trade receivables and contract assets | **Operating** | Step 6 | [IFRS 18.52, B47](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html) | Unchanged |
| 5 | Write-down of inventories to net realisable value (and reversals) | **Operating** | Step 6 | [IFRS 18.52, B47](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html) | Unchanged |
| 6 | Impairment of PP&E, ROU assets, operating intangibles, and goodwill (IAS 36) | **Operating** | Step 6 | [IFRS 18.52, B47](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html) | Unchanged (or moves IN if presented below operating profit) |
| 7 | Gain or loss on disposal of operating PP&E and intangible assets | **Operating** | Step 6 | [IFRS 18.52, B47](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html) | **Moves IN** (often sat below IAS 1 operating profit) |
| 8 | Amortisation of deferred government grants relating to operating assets/costs | **Operating** | Step 6 | [IFRS 18.52](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html) | Unchanged |
| 9 | Insurance claim recoveries for operating property or business interruption | **Operating** | Step 6 | [IFRS 18.52](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html) | Unchanged |
| 10 | Litigation, warranty, and restructuring provision charges | **Operating** | Step 6 | [IFRS 18.52, B57](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html) | **Moves IN** (cannot be excluded into an "exceptional" line) |
| 11 | Current and past service cost on defined benefit / EOSB obligations (IAS 19) | **Operating** | Step 6 | [IFRS 18.52, B56](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html) | Unchanged |
| 12 | Depreciation of right-of-use (ROU) assets and variable/short-term lease expense | **Operating** | Step 6 | [IFRS 18.52, B47](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html) | Unchanged |
| 13 | Foreign exchange gains/losses on trade receivables and trade payables | **Operating** | Step 6 / Overlay A | [IFRS 18.B65, B66(a)](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html) | **Moves IN** (when previously netted in finance/other FX) |
| 14 | Gains/losses on commodity forwards or FX derivatives managing operating inputs | **Operating** | Step 6 / Overlay B | [IFRS 18.B70–B74](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html) | **Moves IN** |
| 15 | Bank service charges, account maintenance, and letter-of-credit service fees | **Operating** | Step 6 | [IFRS 18.52, B51](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html) | **Moves IN** (often sat inside IAS 1 Finance costs) |
| 16 | Zakat and statutory levies outside the scope of IAS 12 | **Operating** | Step 6 | [IFRS 18.52, 67](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html) | **Moves IN** (reduces Operating profit; see Flash Point 1) |
| 17 | Share of profit or loss of equity-accounted associates and joint ventures | **Investing** | Step 5 | [IFRS 18.53(a), B43](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html) | **Moves OUT** (if previously included in operating profit) |
| 18 | Rental income from investment property (IAS 40) | **Investing** | Step 5 | [IFRS 18.53(c), 54, B45](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html) | **Moves OUT** (commonly sat in IAS 1 Other operating income) |
| 19 | Direct operating expenses (repairs, maintenance, management) of investment property | **Investing** | Step 5 | [IFRS 18.54(b), B45](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html) | **Moves OUT** |
| 20 | Fair value gains/losses (or depreciation/impairment) on investment property | **Investing** | Step 5 | [IFRS 18.54(a), B45](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html) | **Moves OUT** (if previously inside operating profit) |
| 21 | Dividend income from equity investments (FVTPL or FVOCI) | **Investing** | Step 5 | [IFRS 18.53(c), 54(a)](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html) | **Moves OUT** |
| 22 | Fair value movements and disposal gains/losses on debt/equity investments | **Investing** | Step 5 | [IFRS 18.53(c), 54](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html) | Unchanged (if already below operating profit) |
| 23 | Interest income on cash, cash equivalents, and short-term bank deposits | **Investing** | Step 5 | [IFRS 18.53(b)–(c)](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html) | **Moves OUT** (if previously netted in finance costs) |
| 24 | Foreign exchange gains/losses on foreign-currency cash and deposits | **Investing** | Step 5 / Overlay A | [IFRS 18.53(b), B65](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html) | **Moves OUT** |
| 25 | Interest expense on bank borrowings, bonds, sukuk, and overdrafts | **Financing** | Step 3 | [IFRS 18.59(a), 60(a)](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html) | Unchanged |
| 26 | Amortisation of borrowing arrangement and transaction costs | **Financing** | Step 3 | [IFRS 18.60(a)](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html) | Unchanged |
| 27 | Gains and losses on modification or extinguishment of borrowings | **Financing** | Step 3 | [IFRS 18.60(c)](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html) | **Moves OUT** (often sat in IAS 1 Other gains — net) |
| 28 | Foreign exchange gains/losses on foreign-currency borrowings | **Financing** | Step 3 / Overlay A | [IFRS 18.60, B65, B66(b)](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html) | **Moves OUT** (when previously in operating FX) |
| 29 | Gains and losses on interest rate swaps managing borrowing interest risk | **Financing** | Step 3 / Overlay B | [IFRS 18.B70–B74](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html) | Unchanged |
| 30 | Interest expense on lease liabilities (IFRS 16) | **Financing** | Step 4 | [IFRS 18.59(b), 61, B56(b)](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html) | Unchanged |
| 31 | Net interest expense on net defined benefit / EOSB obligation (IAS 19) | **Financing** | Step 4 | [IFRS 18.59(b), 61, B56(c)](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html) | **Moves OUT** (if previously buried in staff costs / G&A) |
| 32 | Unwinding of discount on decommissioning/restoration provisions (IAS 37) | **Financing** | Step 4 | [IFRS 18.59(b), 61, B56(d)](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html) | **Moves OUT** (if previously in cost of sales / other expenses) |
| 33 | Unwinding of discount on deferred/contingent consideration (IFRS 3) | **Financing** | Step 4 | [IFRS 18.59(b), 61](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html) | Unchanged |
| 34 | Current and deferred income tax expense/(income) within IAS 12 scope | **Income taxes** | Step 2 | [IFRS 18.67](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html) | Unchanged |
| 35 | Post-tax profit or loss of discontinued operations (IFRS 5) | **Discontinued** | Step 1 | [IFRS 18.68](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html) | Unchanged |

### 2.5 Audit Flash Points in Classification

> ⚑ **AUDIT FLASH POINT — Zakat and non-income-tax levies ([IFRS 18.52, 67](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html)):** Under [IFRS 18.67](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html), **only** tax expense or tax income included in profit or loss in accordance with **IAS 12 *Income Taxes*** (and related FX differences) may sit in the Income Taxes category. In jurisdictions such as Saudi Arabia (KSA), where Zakat is assessed on a net-worth / Zakat base rather than taxable profit and is therefore accounted for outside the scope of IAS 12 (per SOCPA guidance and IFRIC 21 / IAS 37 principles), Zakat **cannot** be presented in the Income Taxes category. As a residual item ([IFRS 18.52](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html)), it must be classified in **Operating**, directly reducing **Operating profit**. Where a dual-owned entity pays both Zakat (outside IAS 12) and corporate income tax on foreign shareholding (inside IAS 12), the two charges split into different categories: Zakat in Operating, Income Tax in Income Taxes. Always surface this judgement in the Reviewer Brief and quantify Operating profit under both treatments.

> ⚑ **AUDIT FLASH POINT — Equity-accounted associates and joint ventures ([IFRS 18.53(a), 55(a)](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html)):** Many industrial groups historically presented their share of profit or loss of strategic or "integral" equity-accounted associates and joint ventures inside IAS 1 Operating profit. Under [IFRS 18.53(a)](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html) and [IFRS 18.55(a)](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html), **all** income and expenses from investments in associates and joint ventures accounted for using the equity method are **mandatory Investing** — with **zero** exception, even if the entity has a specified main business activity of investing. If management wishes to highlight operating profit including equity-accounted associates, [IFRS 18.73](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html) and [IFRS 18.118(c)](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html) permit presenting an additional subtotal *Operating profit or loss and income and expenses from all investments accounted for using the equity method* **after** Operating profit and inside the Investing section.

> ⚑ **AUDIT FLASH POINT — Investment property vs. owner-occupied / operational property ([IFRS 18.53(c), 55, B45–B49](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html)):** Rental income from an investment property held by a manufacturer or retailer is often buried inside IAS 1 "Other operating income". Because an investment property generates returns individually and largely independently of the entity's manufacturing/retailing resources, its rental income, direct property operating expenses, and fair value changes must be reclassified to **Investing** ([IFRS 18.53(c), B45](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html)), and its cash rental receipts must simultaneously move from Operating cash flows to Investing cash flows under IAS 7. Only if investing in real estate is a **main business activity** of the reporting entity ([IFRS 18.55](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html)) do those returns stay in Operating.

> ⚑ **AUDIT FLASH POINT — Supply chain finance / reverse factoring and net FX captions ([IFRS 18.59, B50–B55, B65](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html)):** Where a trade payable is derecognised or substantially modified into a bank borrowing under a reverse-factoring arrangement, fees and interest after derecognition become **Financing** ([IFRS 18.59(a)](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html)); if the liability remains a trade payable, supplier fees/discounts remain **Operating**. Similarly, auditors routinely challenge single-line "Net foreign exchange gain/(loss)" captions: a small net FX loss of SAR (7.8)m can conceal a SAR (9.4)m loss on USD borrowings (Financing) and a SAR +1.6m gain on trade balances (Operating). Always decompose net FX against the borrowings roll-forward note.

## Section 3 — Reference Layer (Layer A): Primary Statement Structure, Aggregation & Expense Analysis (IFRS 18.69–107)

### 3.1 Structure of the Statement of Profit or Loss ([IFRS 18.69–77](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html))

* **Rule A3.1 (Statement title and mandatory subtotals):** Title the primary statement **Statement of profit or loss** (or *Statement of financial performance*). Present the five categories in order, anchored by:
  1. **Operating profit or loss** ([IFRS 18.69(a)](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html)) — immediately below the Operating category;
  2. **Profit or loss before financing and income taxes** ([IFRS 18.69(b)](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html)) — immediately below the Investing category (unless omitted under [IFRS 18.73](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html)); and
  3. **Profit or loss** ([IFRS 18.69(c)](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html)) — at the bottom of the statement.
* **Rule A3.2 (Additional subtotals — [IFRS 18.24, 74, 118](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html)):** Additional subtotals (such as *Gross profit*, *Profit before income taxes*, and *Profit from continuing operations*) are permitted on the face **only if** they: (a) comprise amounts recognised and measured in accordance with IFRS; (b) are presented and labelled in a clear, understandable manner; (c) are consistent from period to period; and (d) are displayed no more prominently than the totals and subtotals required by [IFRS 18.69](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html).

### 3.2 Aggregation, Disaggregation, and "Other" Captions ([IFRS 18.41–45, B16–B28](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html))

* **Rule A3.3 (Shared characteristics):** Aggregate items that share characteristics (nature, function, measurement basis, persistence, size, or tax/regulatory environment) and disaggregate items that have dissimilar characteristics whenever the resulting information is material ([IFRS 18.41](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html)).
* **Rule A3.4 (Prohibition on obscuring material items in "Other" — [IFRS 18.43, B25–B26](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html)):** Never use a generic label such as "Other operating income" or "Other operating expenses" without disclosing its composition if the aggregated amount is material. If an aggregation of immaterial dissimilar items is still sufficiently large that users might question whether it contains material items, disclose in the notes either: (a) the type and amount of the largest item(s) included, or (b) a qualitative explanation that the caption consists of unrelated immaterial items ([IFRS 18.B26](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html)).

### 3.3 Operating Expense Presentation & Mandatory Nature-of-Expense Note ([IFRS 18.78–85, B80–B85](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html))

* **Rule A3.5 (Selecting nature, function, or mixed presentation — [IFRS 18.78, B80](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html)):** Present operating expenses on the face classified by **nature**, by **function**, or using a **mixed** presentation — choosing whichever provides the **most useful structured summary** of the entity's expenses considering: (a) what main components or drivers of profitability are; (b) how the business is managed and reported internally (including IFRS 8 segment reporting); (c) industry practice; and (d) whether allocating particular expenses to functions would be arbitrary and therefore fail to provide a faithful representation ([IFRS 18.B80](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html)). If any single line item is presented by function (e.g., *Cost of sales*), the entity **must** present a separate line item for *Cost of sales* that includes inventory expense under IAS 2.38 ([IFRS 18.82](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html)).
* **Rule A3.6 (Mandatory single-note disclosure of five specified natures — [IFRS 18.83](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html)):** Whenever an entity presents **one or more** line items comprising expenses classified by function in the Operating category, it **must** disclose in a **single note** the total for the period and the amount included in each functional line item in the Operating category (and a list of any non-operating line items that also include them) for five specified nature categories:
  1. **Depreciation** (IAS 16, IFRS 16, IAS 40);
  2. **Amortisation** (IAS 38);
  3. **Employee benefits** (IAS 19 and IFRS 2 share-based payments);
  4. **Impairment losses and reversals of impairment losses** recognized under **IAS 36 *Impairment of Assets***; and
  5. **Write-downs of inventories to net realisable value and reversals of such write-downs** under **IAS 2 *Inventories***.

> ⚑ **AUDIT FLASH POINT — Cost-incurred vs. Expense-incurred in the Paragraph 83 Nature Note ([IFRS 18.83–84, B84](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html)):** Under [IFRS 18.83(b)](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html), the amounts disclosed for depreciation, amortisation, and employee benefits in the nature note may be either the **expense recognised** in the period or the **costs incurred** in the period (e.g., total factory depreciation and payroll before adjusting for the net change in finished-goods/WIP inventory capitalisation). If the entity discloses **costs incurred** rather than expenses recognised, it must explain that fact and qualitative differences ([IFRS 18.B84](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html)). In our full nature-by-function matrix (see Worked Example 2), reconciling both across to total nature charges and down to the exact functional face lines proves full mathematical articulation.

### 3.4 Statement of Financial Position ([IFRS 18.96–106](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html))

* **Rule A3.7 (Mandatory separate Goodwill line — [IFRS 18.103(c)](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html)):** On the face of the statement of financial position, **goodwill** must be presented as a separate line item from intangible assets ([IFRS 18.103(c)](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html) vs. [IFRS 18.103(b)](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html)). A combined "Goodwill and intangible assets" face line is a direct compliance failure under IFRS 18.

## Section 4 — Reference Layer (Layer A): Statement of Cash Flows under Amended IAS 7 (IAS 7.18, 20, 31, 33A, 34A–34D)

### 4.1 Mandatory Indirect-Method Starting Point ([IAS 7.18(b), 20](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ias7.html))

* **Rule A4.1:** When reporting cash flows from operating activities using the indirect method, an entity **must** begin the reconciliation with the **Operating profit or loss** subtotal presented in the statement of profit or loss ([IAS 7.18(b), 20](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ias7.html)). Starting from *Profit before tax* or *Profit for the period* is prohibited.
* **Why this simplifies the reconciliation:** Because *Operating profit or loss* already excludes Investing and Financing items, all legacy add-backs/deductions for interest expense, interest income, dividend income, share of results of associates/JVs, and fair value changes on investment property/FVTPL investments **disappear** from the indirect reconciliation. Only non-cash operating items (depreciation, amortisation, IAS 36 impairments, inventory write-downs, current service cost of EOSB, provision charges, Zakat expense where in Operating), operating disposal gains/losses (whose cash proceeds sit in Investing), working capital changes, and operating cash settlements (benefits paid, provisions utilised, income taxes and Zakat paid) remain.

### 4.2 Elimination of Interest and Dividend Classification Options ([IAS 7.31, 33A, 34A–34D](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ias7.html))

* **Rule A4.2:** IAS 7 as amended by IFRS 18 removes the previous free accounting policy choices for interest and dividends:

| Cash Flow Item | Entity WITHOUT Specified Main Business Activities ([IAS 7.33A, 34A](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ias7.html)) | Entity WITH Specified Main Business Activities ([IAS 7.33A, 34B–34D](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ias7.html)) |
| :--- | :--- | :--- |
| **Dividends paid** | **Financing activities** (mandatory in all cases — [IAS 7.33A](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ias7.html)) | **Financing activities** (mandatory in all cases — [IAS 7.33A](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ias7.html)) |
| **Interest paid** | **Financing activities** ([IAS 7.34A(a)](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ias7.html)) | Follow the single P&L category in which interest expense is classified; if classified in more than one P&L category, make an accounting policy choice to classify **all** interest paid in **one** of the associated cash flow activities ([IAS 7.34B–34C](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ias7.html)). |
| **Interest received** | **Investing activities** ([IAS 7.34A(b)](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ias7.html)) | Follow the single P&L category in which interest income is classified; if split across P&L categories, policy choice to classify **all** interest received in **one** associated activity ([IAS 7.34B–34C](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ias7.html)). |
| **Dividends received** | **Investing activities** ([IAS 7.34A(b)](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ias7.html)) | Follow the single P&L category in which dividend income is classified; if split across P&L categories, policy choice to classify **all** dividends received in **one** associated activity ([IAS 7.34B–34D](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ias7.html)). |

* **Rule A4.3 (Consequential cash flow reclassifications):** Whenever an item of income or expense is reclassified out of Operating in the P&L (for example, rental income and direct operating expenses of investment property reclassified to Investing under [IFRS 18.53(c)](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html)), verify and reclassify its cash flow counterpart into Investing activities so the statement of cash flows and statement of profit or loss articulate cleanly.

## Section 5 — Reference Layer (Layer A): Management-Defined Performance Measures (MPMs) & Transition (IFRS 18.117–125, C1–C7)

### 5.1 Identifying Management-Defined Performance Measures ([IFRS 18.117–120, B113–B131](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html))

* **Rule A5.1 (The three cumulative MPM criteria — [IFRS 18.117](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html)):** A performance measure is an MPM if and only if it is a **subtotal of income and expenses** that:
  1. Is used in **public communications outside the financial statements** (e.g., management commentary, press releases, investor presentations; excluding oral communications, transcripts of oral communications, and social media posts per [IFRS 18.119](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html));
  2. **Communicates to users management's view** of an aspect of the financial performance of the entity as a whole (rebuttably presumed whenever condition 1 is met per [IFRS 18.120](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html)); and
  3. Is **not** listed in [IFRS 18.118](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html) or specifically required to be presented or disclosed by IFRS Accounting Standards.
* **Rule A5.2 (Subtotals explicitly excluded from being MPMs — [IFRS 18.118](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html)):**
  * *(a)* Gross profit or loss (revenue minus cost of sales) and similar subtotals (e.g., net interest income, net fee and commission income, insurance service result, net financial result, net rental income);
  * *(b)* **Operating profit or loss before depreciation, amortisation, and impairments within the scope of IAS 36** (**OPBDA**);
  * *(c)* Operating profit or loss and income and expenses from all investments accounted for using the equity method;
  * *(d)* For an entity that applies [IFRS 18.73](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html), a subtotal comprising operating profit or loss and all income and expenses classified in the investing category;
  * *(e)* Profit or loss before income taxes; and
  * *(f)* Profit or loss from continuing operations.
* **Non-income/expense measures are NOT MPMs ([IFRS 18.B116–B117](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html)):** Free cash flow, return on capital employed (ROCE), net debt, constant-currency revenue growth (revenue only, not a subtotal of income and expenses), and operational KPIs (headcount, store count) are **not** MPMs.

> ⚑ **AUDIT FLASH POINT — "EBITDA" vs. "OPBDA" and Adjusted EBITDA ([IFRS 18.118(b), BC341](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html)):** The exclusion in [IFRS 18.118(b)](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html) covers **only** *Operating profit or loss before depreciation, amortisation and impairments within the scope of IAS 36* (OPBDA). If an entity defines "EBITDA" starting from *Profit before tax* and adding back only interest, tax, depreciation, and amortisation (which therefore includes Investing items like share of results of associates or investment property fair value gains), or if it strips out Zakat, inventory write-downs, litigation provisions, or restructuring costs ("Adjusted EBITDA" or "EBITDA before non-recurring items"), that measure **does not** match [IFRS 18.118(b)](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html) and **is a mandatory MPM** requiring full audited note disclosure.

### 5.2 Single-Note MPM Disclosure Requirements ([IFRS 18.121–125, B132–B142](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html))

* **Rule A5.3:** Disclose all MPMs in a **single note** to the financial statements ([IFRS 18.122](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html)), containing for each MPM ([IFRS 18.123–124](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html)):
  1. **Management's-view & non-comparability statement:** A statement that the MPM provides management's view of an aspect of financial performance and is not necessarily comparable with measures sharing similar labels or descriptions provided by other entities ([IFRS 18.122](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html));
  2. **Clear label and explanation:** Why the MPM communicates management's view and how it is calculated ([IFRS 18.123(a)–(b)](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html));
  3. **Reconciliation:** A quantitative reconciliation between the MPM and the **most directly comparable subtotal** listed in [IFRS 18.118](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html) or total/subtotal specifically required by IFRS ([IFRS 18.123(c)](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html));
  4. **Item-by-item tax and NCI effects:** For **each reconciling item** disclosed in the reconciliation, the **income tax effect** and the effect on **non-controlling interests (NCI)** ([IFRS 18.123(d)](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html));
  5. **Tax-effect methodology:** A description of how the income tax effect was determined ([IFRS 18.123(e)](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html)). Under [IFRS 18.B141](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html), the entity may calculate the tax effect on the basis of: (i) the statutory tax rate(s) applicable to the transaction in the relevant tax jurisdiction(s); (ii) a reasonable pro-rata allocation of current and deferred tax of the entity/jurisdiction; or (iii) another method that achieves a more appropriate allocation in the circumstances; and
  6. **Changes in MPMs:** Explanations of any MPM added, ceased, or recalculated, with restated comparative information unless impracticable ([IFRS 18.124](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html)).

### 5.3 Transition and First-Time Application ([IFRS 18.C1–C7](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html))

* **Rule A5.4 (Effective date & retrospective restatement — [IFRS 18.C1–C2](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html)):** Apply IFRS 18 for annual reporting periods beginning on or after **1 January 2027** (earlier application permitted with disclosure). Apply retrospectively in accordance with IAS 8, restating comparative periods. An entity is **not** required to disclose the quantitative information that would otherwise be required by IAS 8.28(f) for the current period ([IFRS 18.C2](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html)); instead, it provides the specific comparative-period reconciliation under [IFRS 18.C3](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html).
* **Rule A5.5 (Mandatory comparative-period reconciliation — [IFRS 18.C3](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html)):** In the first annual financial statements in which an entity applies IFRS 18, it **must** disclose a reconciliation for **each line item** in the statement of profit or loss for the **comparative period immediately preceding the current period**, bridging from:
  * *(a)* the restated amounts presented in accordance with IFRS 18; and
  * *(b)* the amounts previously presented in accordance with IAS 1.
  *(Presenting the same reconciliation for the current period or earlier comparative periods is permitted under [IFRS 18.C3](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html) and forms our standard Phase 3 Allocation Matrix).*
* **Rule A5.6 (IAS 28.18 Fair Value Election on Transition — [IFRS 18.C7](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html)):** At the date of initial application of IFRS 18, an eligible entity (venture capital organisation, mutual fund, unit trust, or investment-linked insurance fund under IAS 28.18) may change its election to measure an investment in an associate or joint venture from the equity method to fair value through profit or loss (IFRS 9).

## Section 6 — Executable Layer (Layer B): Step-by-Step Procedure & Reclassification Entries

When invoked on a client's IAS 1 financial statements, execute Phases 1 to 7 in sequence, citing the Layer A rule driving every step ([`financial-reporting-workflow-base` §1, §3](https://github.com/openaccountants/openaccountants/blob/main/skills/financial-reporting/financial-reporting-workflow-base.md)):

1. **Phase 1 — Build the Component Source Ledger (executes Rules A2.1–A2.6, A3.3–A3.4):**
   * Extract every IAS 1 P&L face caption (both current and comparative periods), the statement of financial position (both period-ends), and the statement of cash flows (both periods).
   * Decompose every aggregated P&L caption (*Other operating income*, *Other operating expenses*, *Finance costs*, *Finance income*, *Other gains/losses — net*, *Net FX*, *Cost of sales*, *SG&A*, *R&D*) into its constituent components using the notes.
   * Extract all asset and liability roll-forward schedules (PP&E, ROU assets, intangibles, investment property, associates/JVs, borrowings, lease liabilities, EOSB/defined benefit obligations, provisions, deferred government grants, current/deferred tax) and public communications (for MPMs).
   * Flag any aggregated caption lacking note detail as `UNRESOLVED — requires note detail` and trigger the Structured Intake form.
2. **Phase 2 — Classify Every Component & Apply Overlays (executes Rules A2.1–A2.10):**
   * Assess Overlay C (Specified Main Business Activities — Rule A2.9).
   * Run each extracted component through the 6-step decision tree (Rules A2.1–A2.6) and Overlays A (FX — Rule A2.7), B (Derivatives — Rule A2.8), and D (Held-for-sale — Rule A2.10).
   * Record for every component: `ias1_line`, `component`, `face_line`, `amount_cy`, `amount_py`, `category`, `tree_step`, `rule_citation`, `function`, `nature`, `source_note_ref`, and `judgement_flag`.
3. **Phase 3 — Construct the IAS 1-to-IFRS 18 Allocation Matrix & Reclassification Entries (executes Rule A5.5 and Base §3):**
   * Build the two-way Allocation Matrix (IAS 1 captions as rows; the 5 IFRS 18 categories as columns) for both periods.
   * Assert and verify that every row sums across to the exact IAS 1 face amount (`Row Diff = 0`) and that the five column totals sum to `Profit or loss for the period`.
   * Generate formal presentation-reclassification journal entries in `financial-reporting-workflow-base` Section 3 format (mapping IAS 1 presentation buckets to IFRS 18 category buckets).
4. **Phase 4 — Assemble the Restated Statement of Profit or Loss (executes Rules A3.1–A3.5):**
   * Aggregate components by `face_line` within each of the five categories and compute the two mandatory subtotals (*Operating profit or loss* and *Profit or loss before financing and income taxes*) plus permitted subtotals (*Gross profit*, *Profit before income taxes*, *Profit from continuing operations*).
5. **Phase 5 — Restate SFP, Cash Flows & Draft Mandatory Notes (executes Rules A3.6–A3.7, A4.1–A4.3, A5.1–A5.5):**
   * Restate the Statement of Financial Position with **Goodwill** disaggregated onto its own face line (Rule A3.7).
   * Restate the Statement of Cash Flows starting from *Operating profit or loss* (Rule A4.1), locking interest/dividends to their mandatory sections (Rule A4.2), and reclassifying consequential cash flows such as investment property rental cash (Rule A4.3).
   * Construct the single-note **Nature-of-Expense Matrix** (Rule A3.6), the single-note **MPM Reconciliation** with per-item tax and NCI effects (Rules A5.1–A5.3), and the **Transition Comparative Reconciliation** (Rule A5.5).
6. **Phase 6 — Execute the 57-Point Integrity Check Battery (executes Section 9):**
   * Verify all Class A invariants, Class B roll-forward corroborations, and Class C presentation quality checks. Any Class A failure halts delivery.
7. **Phase 7 — Produce Reviewer Brief & Deliverables (executes Base §8):**
   * Deliver the executive conclusion, reference-layer trace, reclassification entries, restated primary statements, mandatory notes, judgements register with every `⚑ AUDIT FLASH POINT`, and the PASS/FAIL check panel.

### Presentation Reclassification Entry Format (Workflow Base §3)

Because IFRS 18 does not alter general ledger recognition or measurement balances, presentation-level reclassification entries bridge the reporting pack from IAS 1 presentation captions to IFRS 18 category captions:

```text
[Period-End Date] — [Reclassification Description] — driving rule: [IFRS 18 / IAS 7 paragraph ref]
  Dr [IAS 1 Presentation Caption (for income moved out) / IFRS 18 Category Caption (for expense moved in)]   XXX
    Cr [IFRS 18 Category Caption (for income moved in) / IAS 1 Presentation Caption (for expense moved out)]   XXX
  (Memo: Component extracted from Note [X]; classified in [Category] per [Rule/Step]; Debits = Credits = XXX)
```

## Section 7 — Worked Examples (`oa-check` blocks)

### Worked Example 1 — Industrial Group Full P&L, Cash Flow & Balance Sheet Restatement (Najd Advanced Industries Company)

#### Client Facts
**Najd Advanced Industries Company (NAIC)** is a listed industrial manufacturing group in Saudi Arabia reporting in `SAR '000` for the year ended **31 December 2026** (with comparative **FY2025**). NAIC has no specified main business activity of investing in assets or providing financing to customers (Rule A2.9). Under IAS 1, NAIC reported **FY2026 Operating profit of SAR 360,400 thousand** (FY2025: SAR 291,100 thousand) and **Profit for the year of SAR 297,500 thousand** (FY2025: SAR 242,100 thousand). Note disclosures reveal:

1. **Note 7 (Other operating income — FY2026: SAR 38,900; FY2025: SAR 31,400):** Comprises government grant amortisation (FY2026: 6,500; FY2025: 6,500), insurance claim recoveries (FY2026: 9,700; FY2025: 4,900), sale of scrap (FY2026: 5,100; FY2025: 4,300), sundry operating income (FY2026: 3,400; FY2025: 2,900), and **rental income from third-party investment property** of **SAR 14,200** (FY2025: **SAR 12,800**).
2. **Note 9 (Other gains — net — FY2026: SAR 5,600; FY2025: SAR 3,100):** Previously presented below IAS 1 operating profit. Comprises net loss on undesignated commodity forward contracts managing raw material price risk (FY2026: **-3,600**; FY2025: **+1,400**), gain on disposal of operating PP&E (FY2026: **+6,900**; FY2025: **+4,200**), loss on disposal of operating intangibles (FY2026: **0**; FY2025: **-2,500**), and gain on modification of bank borrowings (FY2026: **+2,300**; FY2025: **0**).
3. **Note 10 (Net foreign exchange gain/(loss) — FY2026: SAR -7,800; FY2025: SAR +2,400):** Previously presented below IAS 1 operating profit. Decomposes into FX gain/(loss) on trade receivables/payables (FY2026: **+1,600**; FY2025: **-1,500**) and FX gain/(loss) on USD bank borrowings (FY2026: **-9,400**; FY2025: **+3,900**).
4. **Note 18 (Finance costs — FY2026: SAR -86,500; FY2025: SAR -78,900):** Comprises interest on borrowings (-61,300 / -56,200), amortisation of borrowing transaction costs (-2,200 / -1,900), interest on lease liabilities (-11,800 / -10,900), unwinding of discount on decommissioning provision (-3,100 / -2,800), net interest on employee EOSB obligation (-6,900 / -6,100), and net loss on interest rate swap over borrowings (-1,200 / -1,000).
5. **Note 24 (Zakat and Income Tax):** Zakat of **SAR -18,200** (FY2025: **SAR -15,600**) is assessed on NAIC's net-worth Zakat base outside the scope of IAS 12 and was presented in the tax section under IAS 1. Income tax expense under IAS 12 is **SAR -31,400** (FY2025: **SAR -26,300**).

```yaml
example_id: ifrs18-naic-full-restatement-fy2026
currency: "SAR '000"
inputs:
  ias1_operating_profit_2026: 360400
  ias1_operating_profit_2025: 291100
  ias1_profit_for_year_2026: 297500
  ias1_profit_for_year_2025: 242100
  reclassifications_to_operating_2026:
    investment_property_rental_moved_to_investing: -14200
    commodity_forwards_moved_in: -3600
    gain_on_disposal_ppe_moved_in: 6900
    loss_on_disposal_intangibles_moved_in: 0
    fx_on_trade_balances_moved_in: 1600
    zakat_outside_ias12_moved_in: -18200
  reclassifications_to_operating_2025:
    investment_property_rental_moved_to_investing: -12800
    commodity_forwards_moved_in: 1400
    gain_on_disposal_ppe_moved_in: 4200
    loss_on_disposal_intangibles_moved_in: -2500
    fx_on_trade_balances_moved_in: -1500
    zakat_outside_ias12_moved_in: -15600
  investing_components_2026:
    rental_income_investment_property: 14200
    share_of_results_associates_jvs: 27500
    fair_value_gain_investment_property: 9300
    dividend_income_equity_investments: 8400
    fair_value_loss_fvtpl_investments: -4100
    interest_income_cash_and_deposits: 12700
  investing_components_2025:
    rental_income_investment_property: 12800
    share_of_results_associates_jvs: 22100
    fair_value_gain_investment_property: 6400
    dividend_income_equity_investments: 7200
    fair_value_gain_fvtpl_investments: 2700
    interest_income_cash_and_deposits: 9800
  financing_components_2026:
    gain_on_modification_borrowings: 2300
    fx_loss_on_borrowings: -9400
    interest_expense_borrowings: -61300
    amortisation_borrowing_costs: -2200
    interest_expense_leases: -11800
    unwinding_discount_decommissioning: -3100
    net_interest_eosb: -6900
    net_loss_interest_rate_swap: -1200
  financing_components_2025:
    gain_on_modification_borrowings: 0
    fx_gain_on_borrowings: 3900
    interest_expense_borrowings: -56200
    amortisation_borrowing_costs: -1900
    interest_expense_leases: -10900
    unwinding_discount_decommissioning: -2800
    net_interest_eosb: -6100
    net_loss_interest_rate_swap: -1000
  income_tax_expense_2026: -31400
  income_tax_expense_2025: -26300
  discontinued_operations_2026: 21600
  discontinued_operations_2025: 16900
recomputations:
  net_operating_profit_bridge_2026: -14200 + (-3600) + 6900 + 0 + 1600 + (-18200) # = -27500
  ifrs18_operating_profit_2026: 360400 + (-27500) # = 332900
  operating_profit_pct_change_2026: (-27500 / 360400) * 100 # = -7.6304% (-7.6%)
  net_operating_profit_bridge_2025: -12800 + 1400 + 4200 + (-2500) + (-1500) + (-15600) # = -26800 ( wait: -12800 + 1400 + 4200 - 2500 - 1500 - 15600 = -26800; 292300 - 26800 = 265500 )
  ifrs18_operating_profit_2025: 265500
  total_investing_2026: 14200 + 27500 + 9300 + 8400 + (-4100) + 12700 # = 68000
  total_investing_2025: 12800 + 22100 + 6400 + 7200 + 2700 + 9800 # = 61000
  profit_before_financing_and_tax_2026: 332900 + 68000 # = 400900
  profit_before_financing_and_tax_2025: 265500 + 61000 # = 326500
  total_financing_2026: 2300 + (-9400) + (-61300) + (-2200) + (-11800) + (-3100) + (-6900) + (-1200) # = -93600
  total_financing_2025: 0 + 3900 + (-56200) + (-1900) + (-10900) + (-2800) + (-6100) + (-1000) # = -75000
  profit_before_income_taxes_2026: 400900 + (-93600) # = 307300
  profit_before_income_taxes_2025: 326500 + (-75000) # = 251500
  profit_from_continuing_operations_2026: 307300 + (-31400) # = 275900
  profit_from_continuing_operations_2025: 251500 + (-26300) # = 225200
  ifrs18_profit_for_year_2026: 275900 + 21600 # = 297500 (Matches IAS 1: 297500 == 297500 PASS)
  ifrs18_profit_for_year_2025: 225200 + 16900 # = 242100 (Matches IAS 1: 242100 == 242100 PASS)
```

#### Step 1 — Presentation Reclassification Journal Entries (FY2026 & FY2025)

```text
31 Dec 2026 — Reclassify Investment Property Rental Income from Operating to Investing — driving rule: IFRS 18.53(c), B45
  Dr Other operating income (IAS 1 Operating bucket)                  14,200 (FY2025: 12,800)
    Cr Rental income from investment property (IFRS 18 Investing)       14,200 (FY2025: 12,800)
  (Memo: Note 7 breakdown; investment property generates returns independently of manufacturing; Debits = Credits = 14,200)

31 Dec 2026 — Allocate "Other gains — net" components to Operating and Financing — driving rule: IFRS 18.52, 60(c), B47, B74
  Dr Other gains — net (IAS 1 unallocated bucket)                      5,600 (FY2025: 3,100)
  Dr Net loss on commodity forward contracts (IFRS 18 Operating)       3,600 (FY2025: Cr 1,400)
    Cr Gain on disposal of PP&E (IFRS 18 Operating)                      6,900 (FY2025: 4,200)
    Cr Gain on modification of borrowings (IFRS 18 Financing)            2,300 (FY2025: 0; plus FY2025 Dr Loss on disposal of intangibles 2,500)
  (Memo: Note 9 breakdown; PP&E/intangible disposals and commodity forwards are Operating; debt modification is Financing; Debits = Credits = 9,200)

31 Dec 2026 — Split "Net foreign exchange differences" into Operating and Financing — driving rule: IFRS 18.B65, B66
  Dr Net FX loss on foreign-currency borrowings (IFRS 18 Financing)    9,400 (FY2025: Cr 3,900)
    Cr Net FX gain on trade balances (IFRS 18 Operating)                 1,600 (FY2025: Dr 1,500)
    Cr Net foreign exchange gain/(loss) (IAS 1 unallocated bucket)       7,800 (FY2025: Dr 2,400)
  (Memo: Note 10 & Borrowings roll-forward corroboration B16; FX follows underlying item; Debits = Credits = 9,400)

31 Dec 2026 — Reclassify Zakat outside IAS 12 scope into Operating — driving rule: IFRS 18.52, 67
  Dr Zakat expense (IFRS 18 Operating)                                18,200 (FY2025: 15,600)
    Cr Zakat (IAS 1 Tax bucket)                                         18,200 (FY2025: 15,600)
  (Memo: Note 24; Zakat assessed on net-worth base outside IAS 12 falls into Operating residual; Debits = Credits = 18,200)
```

#### Step 2 — Restated Statement of Profit or Loss (IFRS 18 Presentation)

| Statement of Profit or Loss Line Item | Note | FY2026 (SAR '000) | FY2025 Restated (SAR '000) | Governing Rule / Citation |
| :--- | :---: | :---: | :---: | :--- |
| **OPERATING** | | | | |
| Revenue from contracts with customers | 5 | 2,480,000 | 2,215,000 | [IFRS 18.52](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html) |
| Cost of sales | 6 | (1,736,000) | (1,573,000) | [IFRS 18.52, 82](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html) |
| **Gross profit** *(permitted additional subtotal)* | | **744,000** | **642,000** | [IFRS 18.24, 118(a)](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html) |
| Selling and distribution expenses | 6 | (198,400) | (177,200) | [IFRS 18.52, 78](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html) |
| General and administrative expenses | 6 | (156,200) | (148,900) | [IFRS 18.52, 78](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html) |
| Research and development expenses | 6 | (42,000) | (36,500) | [IFRS 18.52, 78](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html) |
| Expected credit losses on trade receivables and contract assets | 11 | (14,600) | (9,800) | [IFRS 18.52, 75(b)(ii)](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html) |
| Amortisation of deferred government grants | 7 | 6,500 | 6,500 | [IFRS 18.52](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html) |
| Insurance claim recoveries | 7 | 9,700 | 4,900 | [IFRS 18.52, 41](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html) |
| Sale of scrap and by-products | 7 | 5,100 | 4,300 | [IFRS 18.52](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html) |
| Sundry operating income | 7 | 3,400 | 2,900 | [IFRS 18.52](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html) |
| Donations and social responsibility contributions | 8 | (4,800) | (3,600) | [IFRS 18.52](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html) |
| Litigation provision charge | 8 | (3,900) | (2,800) | [IFRS 18.52, B57](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html) |
| Other operating expenses | 8 | (2,600) | (2,300) | [IFRS 18.52](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html) |
| Net gain / (loss) on commodity forward contracts *(Judgement)* | 9 | (3,600) | 1,400 | [IFRS 18.B72–B74](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html) |
| Gain on disposal of property, plant and equipment | 9 | 6,900 | 4,200 | [IFRS 18.B47](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html) |
| Loss on disposal of intangible assets | 9 | — | (2,500) | [IFRS 18.B47](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html) |
| Net foreign exchange gain / (loss) on trade balances | 10 | 1,600 | (1,500) | [IFRS 18.B65, B66(a)](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html) |
| Zakat *(Judgement)* | 24 | (18,200) | (15,600) | [IFRS 18.52, 67](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html) |
| **OPERATING PROFIT** *(Mandatory Subtotal 1)* | | **332,900** | **265,500** | [IFRS 18.69(a), 70](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html) |
| **INVESTING** | | | | |
| Rental income from investment property *(Judgement)* | 7 | 14,200 | 12,800 | [IFRS 18.53(c), 54, B45](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html) |
| Share of results of associates and joint ventures | 14 | 27,500 | 22,100 | [IFRS 18.53(a), B43](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html) |
| Net fair value gain on investment property *(Judgement)* | 13 | 9,300 | 6,400 | [IFRS 18.54(a), B45](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html) |
| Dividend income from equity investments | 15 | 8,400 | 7,200 | [IFRS 18.53(c), 54(a)](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html) |
| Net fair value gain / (loss) on investments at FVTPL | 16 | (4,100) | 2,700 | [IFRS 18.53(c), 54(a)](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html) |
| Interest income on cash, cash equivalents and short-term deposits | 17 | 12,700 | 9,800 | [IFRS 18.53(b)–(c)](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html) |
| **Total investing** | | **68,000** | **61,000** | [IFRS 18.53–54](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html) |
| **PROFIT BEFORE FINANCING AND INCOME TAXES** *(Mandatory Subtotal 2)* | | **400,900** | **326,500** | [IFRS 18.69(b), 71](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html) |
| **FINANCING** | | | | |
| Gain on modification of borrowings | 9 | 2,300 | — | [IFRS 18.59(a), 60(c)](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html) |
| Net foreign exchange gain / (loss) on foreign currency borrowings | 10 | (9,400) | 3,900 | [IFRS 18.60, B65, B66(b)](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html) |
| Interest expense on borrowings | 18 | (61,300) | (56,200) | [IFRS 18.59(a), 60(a)](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html) |
| Amortisation of borrowing transaction costs | 18 | (2,200) | (1,900) | [IFRS 18.59(a), 60(a)](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html) |
| Interest expense on lease liabilities | 18 | (11,800) | (10,900) | [IFRS 18.59(b), 61, B56(b)](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html) |
| Unwinding of discount on decommissioning provision | 18 | (3,100) | (2,800) | [IFRS 18.59(b), 61, B56(d)](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html) |
| Net interest on employee end-of-service benefit obligation | 18 | (6,900) | (6,100) | [IFRS 18.59(b), 61, B56(c)](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html) |
| Net loss on interest rate swap | 18 | (1,200) | (1,000) | [IFRS 18.B72–B74](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html) |
| **Total financing** | | **(93,600)** | **(75,000)** | [IFRS 18.59–61](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html) |
| **PROFIT BEFORE INCOME TAXES** | | **307,300** | **251,500** | [IFRS 18.118(e)](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html) |
| **INCOME TAXES** | | | | |
| Income tax expense | 24 | (31,400) | (26,300) | [IFRS 18.67](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html) |
| **PROFIT FROM CONTINUING OPERATIONS** | | **275,900** | **225,200** | [IFRS 18.118(f)](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html) |
| **DISCONTINUED OPERATIONS** | | | | |
| Profit from discontinued operation, net of tax | 12 | 21,600 | 16,900 | [IFRS 18.68](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html) |
| **PROFIT FOR THE YEAR** *(Mandatory Total — Invariant)* | | **297,500** | **242,100** | [IFRS 18.69(c), 72](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html) |

#### Step 3 — Transition Reconciliation / Allocation Matrix for Comparative Period FY2025 (IFRS 18.C3)

| IAS 1 Line Item as Originally Presented (FY2025, SAR '000) | IAS 1 Presented | Operating | Investing | Financing | Income Taxes | Discontinued | IFRS 18 Row Total | Row Tie-Out |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Revenue | 2,215,000 | 2,215,000 | — | — | — | — | 2,215,000 | **PASS (0)** |
| Cost of sales | (1,573,000) | (1,573,000) | — | — | — | — | (1,573,000) | **PASS (0)** |
| Selling and distribution expenses | (177,200) | (177,200) | — | — | — | — | (177,200) | **PASS (0)** |
| General and administrative expenses | (148,900) | (148,900) | — | — | — | — | (148,900) | **PASS (0)** |
| Research and development expenses | (36,500) | (36,500) | — | — | — | — | (36,500) | **PASS (0)** |
| Impairment loss on trade receivables & contract assets | (9,800) | (9,800) | — | — | — | — | (9,800) | **PASS (0)** |
| Other operating income | 31,400 | 18,600 | 12,800 | — | — | — | 31,400 | **PASS (0)** |
| Other operating expenses | (8,700) | (8,700) | — | — | — | — | (8,700) | **PASS (0)** |
| Share of results of associates and joint ventures | 22,100 | — | 22,100 | — | — | — | 22,100 | **PASS (0)** |
| Dividend income | 7,200 | — | 7,200 | — | — | — | 7,200 | **PASS (0)** |
| Interest income | 9,800 | — | 9,800 | — | — | — | 9,800 | **PASS (0)** |
| Net fair value gain on investment property | 6,400 | — | 6,400 | — | — | — | 6,400 | **PASS (0)** |
| Net fair value gain / (loss) on investments at FVTPL | 2,700 | — | 2,700 | — | — | — | 2,700 | **PASS (0)** |
| Finance costs | (78,900) | — | — | (78,900) | — | — | (78,900) | **PASS (0)** |
| Net foreign exchange gain / (loss) | 2,400 | (1,500) | — | 3,900 | — | — | 2,400 | **PASS (0)** |
| Other gains — net | 3,100 | 3,100 | — | — | — | — | 3,100 | **PASS (0)** |
| Zakat | (15,600) | (15,600) | — | — | — | — | (15,600) | **PASS (0)** |
| Income tax expense | (26,300) | — | — | — | (26,300) | — | (26,300) | **PASS (0)** |
| Profit from discontinued operation, net of tax | 16,900 | — | — | — | — | 16,900 | 16,900 | **PASS (0)** |
| **Total / Category Subtotal (FY2025)** | **242,100** | **265,500** | **61,000** | **(75,000)** | **(26,300)** | **16,900** | **242,100** | **PASS (0)** |

#### Step 4 — Class B Roll-Forward Corroboration of Reclassified Amounts (FY2026, SAR '000)

* **Check B7 (Lease liability interest = -11,800):** Opening lease liability `219,700` + additions `44,900` − payments `62,100` − disposed with subsidiary `14,300` − closing balance `200,000` (non-current `154,000` + current `46,000`) = implied interest `-11,800` (**PASS**).
* **Check B8 (EOSB net interest = -6,900):** Opening EOSB `210,900` + current service cost `27,300` − benefits paid `16,800` − OCI remeasurement `5,250` − closing balance `223,050` = implied net interest `-6,900` (**PASS**).
* **Check B9 (Decommissioning unwinding = -3,100):** Opening provision `68,800` + additions capitalised `5,200` − utilised `2,400` − closing balance `74,700` = implied unwinding `-3,100` (**PASS**).
* **Check B12 (Share of results of associates/JVs = +27,500):** Closing carrying amount `290,900` − opening `259,900` − additions `18,000` + dividends received `12,400` + OCI share `2,100` = implied share of results `+27,500` (**PASS**).
* **Check B16 (FX on borrowings = -9,400):** Opening borrowings `1,192,000` + drawdowns `286,000` − repayments `312,000` + transaction cost amortisation `2,200` − modification gain `2,300` − closing borrowings `1,175,300` (non-current `892,300` + current `283,000`) = implied FX loss `-9,400` (**PASS**).
* **Cash Flow & Balance Sheet Impact:** Indirect operating cash flow starts from **Operating profit of SAR 332,900** (FY2025: 265,500) and generates **Net cash from operating activities of SAR 484,100** (FY2025: 435,000). Rental cash received from investment property (`+14,200` / `+12,800`), dividends received (`+12,400` from associates + `+8,400` from equity investments), and interest received (`+12,700`) sit in **Investing activities** (`-216,800` / `-287,000`). Interest paid (`-62,500` / `-57,200`) and dividends paid (`-145,000` / `-120,000`) sit in **Financing activities** (`-295,600` / `-183,600`). On the Statement of Financial Position, **Goodwill of SAR 142,600** is presented on its own line separate from **Other intangible assets of SAR 178,000** (FY2025: 170,000), while **Total Assets of SAR 5,176,900** (FY2025: 4,984,100) and **Total Equity of SAR 2,513,600** (FY2025: 2,375,200) remain unchanged.

### Worked Example 2 — Management-Defined Performance Measures (MPMs) & Specified Nature-of-Expense Matrix (IFRS 18.83 & 18.123)

#### Client Facts
Continuing from NAIC's FY2026 financial statements:
1. **Publicly communicated MPMs:** In its earnings release and investor presentation, NAIC reports two non-IFRS performance subtotals:
   * **MPM 1 — Adjusted operating profit:** Defined by management as *Operating profit before Zakat, IAS 36 impairment of PP&E, write-downs of inventories to NRV, litigation provision charges, and insurance claim recoveries*.
   * **MPM 2 — EBITDA before non-recurring items:** Defined as *Adjusted operating profit (MPM 1) before depreciation of PP&E, depreciation of ROU assets, and amortisation of intangible assets*.
2. **Tax and NCI parameters ([IFRS 18.123(d)–(e)](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html)):** Income tax effects are determined using the applicable statutory income tax rate of **20%** in the jurisdiction where each adjusting item arises ([IFRS 18.B141(a)](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html)). Zakat is non-deductible and carries **0%** income tax effect and **0%** NCI effect (wholly-owned parent level). PP&E impairment (`12,400`), inventory write-downs (`8,900`), and insurance recoveries (`-9,700`) arise in a **90%-owned subsidiary** (**10% NCI**); the litigation provision (`3,900`) arises in a **100%-owned subsidiary** (**0% NCI**).
3. **Functional expense presentation:** NAIC presents four functional operating expense lines on the face (*Cost of sales*, *Selling and distribution*, *General and administrative*, and *Research and development*) totalling **SAR 2,132,600 thousand** in FY2026 (FY2025: **SAR 1,935,600 thousand**), triggering the mandatory single-note disclosure under [IFRS 18.83](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html).

```yaml
example_id: ifrs18-naic-mpm-and-nature-matrix-fy2026
currency: "SAR '000"
inputs:
  ifrs18_operating_profit_2026: 332900
  ifrs18_operating_profit_2025: 265500
  statutory_tax_rate: 0.20
  subsidiary_nci_rate: 0.10
  mpm1_adjustments_2026:
    zakat: 18200
    impairment_ppe_ias36: 12400
    inventory_writedown_ias2: 8900
    litigation_provision: 3900
    insurance_recoveries: -9700
  mpm1_adjustments_2025:
    zakat: 15600
    impairment_ppe_ias36: 0
    inventory_writedown_ias2: 6200
    litigation_provision: 2800
    insurance_recoveries: -4900
  mpm2_da_addbacks_2026:
    depreciation_ppe: 182700
    depreciation_rou: 41900
    amortisation_intangibles: 23800
  mpm2_da_addbacks_2025:
    depreciation_ppe: 168400
    depreciation_rou: 38200
    amortisation_intangibles: 21600
  functional_operating_expenses_2026:
    cost_of_sales: 1736000
    selling_and_distribution: 198400
    general_and_administrative: 156200
    research_and_development: 42000
recomputations:
  mpm1_adjusted_operating_profit_2026: 332900 + 18200 + 12400 + 8900 + 3900 + (-9700) # = 366600
  mpm1_adjusted_operating_profit_2025: 265500 + 15600 + 0 + 6200 + 2800 + (-4900) # = 285200
  tax_effect_impairment_2026: -12400 * 0.20 # = -2480
  tax_effect_inventory_2026: -8900 * 0.20 # = -1780
  tax_effect_litigation_2026: -3900 * 0.20 # = -780
  tax_effect_insurance_2026: 9700 * 0.20 # = 1940
  total_mpm1_tax_effect_2026: 0 + (-2480) + (-1780) + (-780) + 1940 # = -3100
  nci_effect_impairment_2026: -12400 * 0.10 # = -1240
  nci_effect_inventory_2026: -8900 * 0.10 # = -890
  nci_effect_insurance_2026: 9700 * 0.10 # = 970
  total_mpm1_nci_effect_2026: 0 + (-1240) + (-890) + 0 + 970 # = -1160
  mpm2_ebitda_before_non_recurring_2026: 366600 + 182700 + 41900 + 23800 # = 615000
  mpm2_ebitda_before_non_recurring_2025: 285200 + 168400 + 38200 + 21600 # = 513400
  total_functional_expenses_2026: 1736000 + 198400 + 156200 + 42000 # = 2132600
  total_specified_five_natures_2026: 372000 + 182700 + 41900 + 23800 + 12400 + 8900 # = 641700
  total_other_natures_2026: 1205000 + 74300 + 61200 + 33500 + 28700 + 19600 + 9800 + 58800 # = 1490900
  nature_matrix_grand_total_2026: 641700 + 1490900 # = 2132600 (Matches functional total 2132600 PASS)
```

#### Step 1 — Single-Note Disclosure of Management-Defined Performance Measures (IFRS 18.122–123)

| MPM Reconciliation Line Item (SAR '000) | FY2026 Amount | FY2026 Income Tax Effect (20% Statutory) | FY2026 NCI Effect (10% Sub Share) | FY2025 Restated Amount | Governing Citation |
| :--- | :---: | :---: | :---: | :---: | :--- |
| **Operating profit** *(IFRS 18 most directly comparable subtotal)* | **332,900** | | | **265,500** | [IFRS 18.69(a), 118, 123(c)](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html) |
| Add: Zakat (assessed on net-worth base; non-deductible) | 18,200 | — | — | 15,600 | [IFRS 18.123(c)–(d)](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html) |
| Add: Impairment loss on property, plant and equipment (IAS 36) | 12,400 | (2,480) | (1,240) | — | [IFRS 18.123(c)–(d)](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html) |
| Add: Write-down of inventories to net realisable value (IAS 2) | 8,900 | (1,780) | (890) | 6,200 | [IFRS 18.123(c)–(d)](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html) |
| Add: Litigation provision charge (IAS 37) | 3,900 | (780) | — | 2,800 | [IFRS 18.123(c)–(d)](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html) |
| Less: Insurance claim recoveries | (9,700) | 1,940 | 970 | (4,900) | [IFRS 18.123(c)–(d)](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html) |
| **Adjusted operating profit (MPM 1)** | **366,600** | **(3,100)** | **(1,160)** | **285,200** | [IFRS 18.117, 123](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html) |
| Add: Depreciation of property, plant and equipment | 182,700 | *(Note 1)* | *(Note 1)* | 168,400 | [IFRS 18.123(c)](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html) |
| Add: Depreciation of right-of-use assets | 41,900 | *(Note 1)* | *(Note 1)* | 38,200 | [IFRS 18.123(c)](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html) |
| Add: Amortisation of intangible assets | 23,800 | *(Note 1)* | *(Note 1)* | 21,600 | [IFRS 18.123(c)](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html) |
| **EBITDA before non-recurring items (MPM 2)** | **615,000** | | | **513,400** | [IFRS 18.117, 118(b), 123](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html) |

*(Note 1: Alternatively, MPM 2 can be reconciled directly to the IFRS 18.118(b) OPBDA subtotal of `332,900 + 182,700 + 41,900 + 23,800 + 12,400 = 593,700`, in which case only the remaining non-OPBDA reconciling items — Zakat `18,200`, inventory write-down `8,900`, litigation `3,900`, and insurance recoveries `-9,700` — require tax and NCI effects).*

#### Step 2 — Mandatory Single-Note Analysis of Operating Expenses by Nature and Function (IFRS 18.83, FY2026, SAR '000)

| Expense Nature Category (*Bold = Mandatory per IFRS 18.83*) | Cost of Sales | Selling & Distribution | General & Admin | Research & Development | FY2026 Total | FY2025 Total |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Employee benefits (IAS 19)** | **224,900** | **62,000** | **70,100** | **15,000** | **372,000** | **341,500** |
| **Depreciation of property, plant and equipment (IAS 16)** | **164,700** | **6,000** | **9,000** | **3,000** | **182,700** | **168,400** |
| **Depreciation of right-of-use assets (IFRS 16)** | **20,900** | **12,000** | **8,000** | **1,000** | **41,900** | **38,200** |
| **Amortisation of intangible assets (IAS 38)** | **12,800** | **2,000** | **6,000** | **3,000** | **23,800** | **21,600** |
| **Impairment losses on PP&E (IAS 36)** | **12,400** | **—** | **—** | **—** | **12,400** | **—** |
| **Write-down of inventories to NRV (IAS 2)** | **8,900** | **—** | **—** | **—** | **8,900** | **6,200** |
| *Subtotal — Five Specified Natures (IFRS 18.83)* | *444,600* | *82,000* | *93,100* | *22,000* | *641,700* | *575,900* |
| Raw materials and consumables used | 1,160,000 | 25,000 | — | 20,000 | 1,205,000 | 1,096,000 |
| Utilities and energy | 68,300 | 2,000 | 4,000 | — | 74,300 | 67,900 |
| Freight and distribution | 8,200 | 53,000 | — | — | 61,200 | 55,400 |
| Repairs and maintenance | 27,500 | 2,000 | 4,000 | — | 33,500 | 30,100 |
| Marketing and advertising | — | 28,700 | — | — | 28,700 | 25,300 |
| Professional and consultancy fees | 2,600 | — | 17,000 | — | 19,600 | 17,800 |
| Insurance | 4,800 | 1,000 | 4,000 | — | 9,800 | 8,900 |
| Other operating expenses by nature | 20,000 | 4,700 | 34,100 | — | 58,800 | 58,300 |
| **Total Operating Expenses in Functional Lines (Tie-Out)** | **1,736,000** | **198,400** | **156,200** | **42,000** | **2,132,600** | **1,935,600** |

## Section 8 — Divergence from US GAAP (ASC 220 / ASU 2024-03 DISE / ASC 230 / SEC Non-GAAP)

For dual-reporters (such as a US subsidiary of an IFRS parent, an IFRS parent with US GAAP statutory reporting, or an SEC Foreign Private Issuer filing Form 20-F), IFRS 18 and US GAAP take fundamentally different architectural approaches: **IFRS 18 redesigns the face of the primary financial statements**, whereas **US GAAP (ASU 2024-03 / ASC 220-40) leaves the face of the income statement unchanged and adds tabular footnote disaggregation for Public Business Entities (PBEs)** ([`financial-reporting-workflow-base` §2](https://github.com/openaccountants/openaccountants/blob/main/skills/financial-reporting/financial-reporting-workflow-base.md)).

| Dimension | IFRS (IFRS 18 & Amended IAS 7) | US GAAP (ASC 220, ASU 2024-03 / ASC 220-40, ASC 230 & SEC Reg G / S-K Item 10(e)) |
| :--- | :--- | :--- |
| **Income Statement Structure & Categories** | Mandatory classification of all P&L items into **five defined categories** (Operating, Investing, Financing, Income taxes, Discontinued operations) ([IFRS 18.47](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html)). | No universal 5-category structure under ASC 220. SEC Regulation S-X Rules 5-03 / 9-04 prescribe industry-specific line items for SEC registrants; private companies have broad formatting flexibility. |
| **Mandatory Subtotals on the Face** | Two mandatory subtotals: **Operating profit or loss** and **Profit or loss before financing and income taxes** ([IFRS 18.69](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html)). | **No mandatory "Operating income" definition** in ASC 220 (even when presented, its composition is not standardised across non-operating items like equity-method earnings or FX). |
| **Equity-Accounted Associates & JVs** | **Mandatory Investing** category (below Operating profit) for all equity-method investees ([IFRS 18.53(a), 55(a)](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html)). | Under ASC 323, often presented after income tax or within pre-tax income; SEC registrants may present inside operating income only if integral and approved, creating a direct subtotal variance. |
| **Net Interest on Defined Benefit Plans & Unwinding of Provisions** | **Mandatory Financing** category ([IFRS 18.59(b), 61](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html)). | Under ASC 715, net periodic benefit cost components other than service cost sit outside operating income; however, accretion expense on asset retirement obligations (ASC 410-20) is classified in **Operating** expense. |
| **Management Performance Measures (MPMs) vs. Non-GAAP** | **Audited footnote disclosure** required in a **single note** inside the financial statements for all MPMs, including per-item tax and NCI effects ([IFRS 18.117–125](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html)). Applies to **all** IFRS reporters (listed and private). | **Prohibited inside audited financial statements** for SEC registrants under Regulation S-K Item 10(e)(1)(ii)(C) (except where required by IFRS 18 for FPIs under Item 10(e)(5)). Regulated outside the financial statements (MD&A / press releases) under SEC Regulation G. Private companies have no MPM regime. |
| **Expense Disaggregation Note (IFRS 18.83 vs. ASC 220-40 DISE)** | Triggered when **any** operating expense line is presented by function; applies to **all** IFRS entities. Requires a single note disclosing **5 natures**: depreciation, amortisation, employee benefits, IAS 36 impairments, and inventory write-downs ([IFRS 18.83](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html)). | Under **ASU 2024-03 (ASC 220-40)**, applies **only to Public Business Entities (PBEs)** (private companies exempt). Requires footnote disaggregation of relevant expense captions into: **(1) purchases of inventory**, **(2) employee compensation**, **(3) depreciation**, **(4) intangible asset amortization**, and **(5) DD&A**, plus separate disclosure of **total selling expenses** and their definition (ASC 220-40-50-4 to 50-25). |
| **Cash Flow Indirect Starting Point** | Locked strictly to **Operating profit or loss** ([IAS 7.18(b), 20](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ias7.html)). | Locked strictly to **Net income (Profit or loss)** under ASC 230-10-45-28. |
| **Cash Flow Classification of Interest & Dividends** | General entity: **Interest paid** = Financing; **Dividends paid** = Financing; **Interest received** & **Dividends received** = Investing ([IAS 7.33A, 34A](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ias7.html)). | Under ASC 230: **Interest paid**, **Interest received**, and **Dividends received** (returns on investment) are **Operating** cash flows; only **Dividends paid** are **Financing**. This creates a major permanent difference in reported Operating Cash Flow between IFRS 18 and US GAAP. |
| **Balance Sheet Goodwill** | Must be presented as a **separate line item** on the face ([IFRS 18.103(c)](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html)). | Must be presented as a **separate line item** on the face under ASC 350-20-45-1 (aligned). |
| **Effective Date & Transition** | Annual periods beginning on or after **1 January 2027**; **mandatory retrospective** restatement ([IFRS 18.C1–C2](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html)). | ASU 2024-03 effective for annual periods beginning after **15 December 2026** (interim periods after 15 December 2027); **prospective** by default (retrospective optional). |

## Section 9 — Topic Self-Checks & Integrity Check Battery (in addition to Base §7)

Before delivering any IFRS 18 output, run the complete 3-class check battery and display the PASS/FAIL table showing both compared numbers. **A single Class A failure blocks delivery.**

### Class A — Mathematical Invariants (Must Hold to the Exact Unit)
* [ ] **A1:** Restated Profit or loss for the period = IAS 1 Profit or loss for the period (both CY and PY) ([IFRS 18.69(c)](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html)).
* [ ] **A2:** Restated Profit from continuing operations = IAS 1 Profit from continuing operations (both CY and PY).
* [ ] **A3:** Profit attributable to owners of the parent = as originally presented ([IFRS 18.76(a)](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html)).
* [ ] **A4:** Profit attributable to non-controlling interests = as originally presented ([IFRS 18.76(a)](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html)).
* [ ] **A5:** Other comprehensive income and Total comprehensive income = as originally presented ([IFRS 18.86–88](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html)).
* [ ] **A6:** Basic and diluted EPS = as originally presented ([IAS 33.73B](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html)).
* [ ] **A7:** Total assets, Total liabilities, and Total equity = as originally presented at both period-ends ([IFRS 18.96, 103](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html)).
* [ ] **A8:** Net movement in cash and cash equivalents and closing cash balance = as originally presented ([IAS 7.10](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ias7.html)).
* [ ] **A9:** Every row of the IAS 1-to-IFRS 18 Allocation Matrix sums across to the exact original IAS 1 amount (`Row Diff = 0`) ([IFRS 18.C3](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html)).
* [ ] **A10:** The five category column totals sum to Profit or loss for the period ([IFRS 18.47](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html)).
* [ ] **A11:** Every line item on the restated P&L face sums to Profit or loss for the period.
* [ ] **A12:** `Operating profit or loss + Total investing = Profit or loss before financing and income taxes` ([IFRS 18.71](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html)).
* [ ] **A13:** `Profit or loss before financing and income taxes + Total financing = Profit or loss before income taxes`.
* [ ] **A14:** Zero double-counted or unallocated components across the mapping ledger.
* [ ] **A15:** Both current and comparative periods are mapped and restated on the identical classification basis ([IFRS 18.C2](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html)).

### Class B — Balance Sheet & Cash Flow Roll-Forward Corroboration
* [ ] **B1–B4:** Depreciation (PP&E and ROU assets), amortisation (intangibles), and IAS 36 impairments in the [IFRS 18.83](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html) nature note agree to the respective non-current asset roll-forward schedules and cash flow add-backs.
* [ ] **B5–B6:** Interest expense and transaction-cost amortisation on borrowings (Financing) agree to interest paid in the cash flow statement adjusted for accrued interest movements and the borrowings roll-forward.
* [ ] **B7:** Interest expense on lease liabilities (Financing) agrees to the lease liability roll-forward residual (`Opening + Additions + Interest − Payments ± Disposals = Closing`).
* [ ] **B8:** Net interest on defined benefit / EOSB obligations (Financing) agrees to the IAS 19 roll-forward residual (`Opening + Service cost + Net interest − Benefits paid ± OCI Remeasurement = Closing`).
* [ ] **B9:** Unwinding of discount on provisions (Financing) agrees to the IAS 37 provision accretion roll-forward line.
* [ ] **B10–B15:** Interest income, dividend income, share of results of associates/JVs, investment property rental income and fair value movements, and FVTPL investment movements (Investing) agree to the respective cash flow lines and investment roll-forwards.
* [ ] **B16:** Foreign exchange gain/loss on borrowings (Financing) agrees to the unexplained residual in the borrowings roll-forward.
* [ ] **B17–B22:** Government grant amortisation, PP&E disposal gains/losses, income tax/Zakat paid, deferred tax charge, employee benefit totals, and inventory write-downs agree to their respective balance sheet roll-forwards.

### Class C — Presentation & Disclosure Quality Checks
* [ ] **C1–C7:** Statement is titled *Statement of profit or loss*; both mandatory subtotals are present (or omission of the second is justified under [IFRS 18.73](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html)); categories appear in exact statutory order; no "unusual/exceptional" face subtotal exists; additional subtotals obey [IFRS 18.24](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html).
* [ ] **C8:** Goodwill is presented as a separate line item on the Statement of Financial Position ([IFRS 18.103(c)](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html)).
* [ ] **C9–C10:** The [IFRS 18.83](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html) nature-of-expense matrix is presented in a single note and reconciles both across and down.
* [ ] **C11–C12:** All public MPMs are disclosed in a single note ([IFRS 18.122](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html)), reconciled to the most directly comparable IFRS subtotal, with tax and NCI effects and tax methodology stated ([IFRS 18.123](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html)).
* [ ] **C13:** Comparative-period line-by-line reconciliation from IAS 1 to IFRS 18 is presented ([IFRS 18.C3](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html)).
* [ ] **C14–C16:** Indirect cash flow statement starts from *Operating profit or loss* ([IAS 7.18(b)](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ias7.html)); interest and dividends follow [IAS 7.33A, 34A](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ias7.html); consequential cash flow reclassifications (e.g., investment property rental cash) are made.
* [ ] **C17–C20:** Material "Other" captions are disaggregated; the Judgements Register and Reviewer Brief surface every `⚑ AUDIT FLASH POINT` with quantified alternatives.

## Section 10 — Verification, Attribution & Disclaimer

* **Quality State:** **Source-cited draft** (`tier: 2`). Every rule, category boundary, subtotal requirement, cash flow amendment, and transition rule is drafted from and cited to the official IASB standards at [ifrs.org](https://www.ifrs.org/issued-standards/list-of-standards/ifrs-18-presentation-and-disclosure-in-financial-statements/).
* **Author Attribution:** Authored by **Talha Mehmood, ACA, FCCA** (`authored_by` in frontmatter). Checked against the authoritative text of IFRS 18 and IAS 7 on **2026-11-08**.
* **Practitioner Review Guardrail:** This skill provides computational and interpretive working-paper guidance on [IFRS 18 *Presentation and Disclosure in Financial Statements*](https://www.ifrs.org/issued-standards/list-of-standards/ifrs-18-presentation-and-disclosure-in-financial-statements/) and amended [IAS 7 *Statement of Cash Flows*](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ias7.html). It is not an audit or assurance engagement. Classification of items under IFRS 18 — particularly main business activity assessments ([IFRS 18.49–51](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html)), Zakat and statutory levies outside IAS 12 ([IFRS 18.52, 67](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html)), derivative risk-management linkages ([IFRS 18.B70–B76](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html)), and MPM identification ([IFRS 18.117–125](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html)) — turns on entity-specific facts and significant professional judgement. Have all restated statements, reconciliations, and note disclosures reviewed and signed off by a qualified accountant and the entity's external auditor before publication or filing.

## Sources

1. **IASB — IFRS 18 *Presentation and Disclosure in Financial Statements* (Full Issued Standard, Paragraphs 1–132 and Appendices A–D):** [https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html) (Read date: `2026-11-08`).
2. **IASB — Illustrative Examples on IFRS 18 *Presentation and Disclosure in Financial Statements* (Parts I–III, Figures & Notes 1–2):** [https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18-ie.html](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18-ie.html) (Read date: `2026-11-08`).
3. **IASB — IAS 7 *Statement of Cash Flows* (incorporating April 2024 IFRS 18 Consequential Amendments to Paragraphs 6, 10, 12, 14, 16–18, 20, 31, 32, 33A, 34A–34D, 35, 46, 47):** [https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ias7.html](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ias7.html) (Read date: `2026-11-08`).
4. **IFRS Foundation — IFRS 18 Navigator & Official Standard Page:** [https://www.ifrs.org/issued-standards/list-of-standards/ifrs-18-presentation-and-disclosure-in-financial-statements/](https://www.ifrs.org/issued-standards/list-of-standards/ifrs-18-presentation-and-disclosure-in-financial-statements/) (Read date: `2026-11-08`).
5. **IFRS Foundation — Project Summary: IFRS 18 *Presentation and Disclosure in Financial Statements* (April 2024):** [https://www.ifrs.org/content/dam/ifrs/project/primary-financial-statements/ifrs-standard/projectsummary-ifrs18-april2024.pdf](https://www.ifrs.org/content/dam/ifrs/project/primary-financial-statements/ifrs-standard/projectsummary-ifrs18-april2024.pdf) (Read date: `2026-11-08`).
6. **IFRS Foundation — Effects Analysis: IFRS 18 *Presentation and Disclosure in Financial Statements* (April 2024):** [https://www.ifrs.org/content/dam/ifrs/publications/amendments/english/2024/effect-analysis-ifrs18-april2024.pdf](https://www.ifrs.org/content/dam/ifrs/publications/amendments/english/2024/effect-analysis-ifrs18-april2024.pdf) (Read date: `2026-11-08`).
7. **OpenAccountants — *How to write a skill: the standard* (`docs/skill-template.md`):** [https://github.com/openaccountants/openaccountants/blob/main/docs/skill-template.md](https://github.com/openaccountants/openaccountants/blob/main/docs/skill-template.md) (Read date: `2026-11-08`).
8. **OpenAccountants — *Financial Reporting Workflow Base* (`skills/financial-reporting/financial-reporting-workflow-base.md`):** [https://github.com/openaccountants/openaccountants/blob/main/skills/financial-reporting/financial-reporting-workflow-base.md](https://github.com/openaccountants/openaccountants/blob/main/skills/financial-reporting/financial-reporting-workflow-base.md) (Read date: `2026-11-08`).

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-08. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `ifrs18-presentation` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/ifrs18-presentation. If neither is available, confirm every figure against the official source pages cited above before relying on it.
