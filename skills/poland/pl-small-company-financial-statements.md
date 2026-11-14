---
name: pl-small-company-financial-statements
description: >
  Prepare and review Polish Accounting Act annual accounts for an ordinary
  standalone sp. z o.o. that qualifies as small but not micro and validly elects
  Annex 5. Covers the 2026 reporting framework, both profit and loss formats,
  balance sheet mapping, notes, measurement, depreciation, current and deferred
  tax, audit, management report relief, signatures, approval and KRS filing.
  Trigger on Polish small company accounts, załącznik 5, bilans, rachunek zysków
  i strat or sprawozdanie finansowe. Refuses regulated entities, groups, branches,
  MSR accounts and insolvency. This source cited draft requires professional
  review and does not establish filing readiness.
jurisdiction: PL
category: financial-statements
tax_year: 2026
tax_year_notes: "2026 accounts. Accounting Act consolidation at 26 March 2026, with selected later amendments checked on 1 November 2026; conditional 2027 approval and filing rules."
tier: 2
last_updated: 2026-11-02
version: 0.2
review_status: pending_review
depends_on:
  - financial-statements-workflow-base
  - workflow-base
  - pl-corporate-income-tax
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Poland: small company financial statements, Annex 5, 2026

Load this with `financial-statements-workflow-base` and `workflow-base`. Their intake, confirmation checkpoints, 6 outputs and 14 self-checks apply. Use the local rules below where the generic base would give a different caption, classification, measurement or disclosure. This is a Tier 2 draft awaiting review by a Polish accounting professional.

Article references are to the Accounting Act of 29 September 1994, [Dz.U. 2026 poz. 522](https://api.sejm.gov.pl/eli/acts/DU/2026/522/text.pdf), unless stated. Its legal snapshot is **26 March 2026**. The selected later changes and their commencement are identified in the sources section. Recheck the law and technical filing rules for the actual preparation and submission dates.

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## What this file is

This is a template migration of retained research, not a new law-reading exercise or whole-guide current-law verification. The dated events below identify historical source checks with their actual retained extents. Acquisition times, legal cutoffs and this migration date are not reading dates. Every retained table row is explicitly unverified in this migration; the source index does not independently qualify every statement on that row. Resolve all applicable holds before using a figure.

It produces the retained accounting base workflow working papers and reviewer brief for the qualified 2026 Annex 5 case. It does not issue an audit opinion, establish a distribution entitlement or validate a filing.

## Scope statement

### 1. Framework, eligibility and responsibilities

This companion covers a solvent, going concern, ordinary **spółka z ograniczoną odpowiedzialnością**, or **sp. z o.o.**, using Polish Accounting Act rules, standing alone and validly choosing Annex 5. It covers neither a micro entity nor the complete Polish reporting system.

**Stop and use an appropriate separately qualified workflow** for S.A., simple joint stock companies, financial or regulated activity, ASIs, groups or subsidiaries, consolidation, foreign branches, public or non-profit bodies, liquidation, bankruptcy, restructuring, succession, MSR/IFRS accounts or a material acquisition, merger or other transaction whose recognition rules have not been established. Do not treat this companion as an audit opinion or prepare a distribution from accounting profit alone.

#### Size and exclusions

Article 3(1)(1b) defines small as **not micro** and not exceeding at least 2 of these limits under its reporting-year and preceding-year tests:

| Measure | Small limit | Micro limit, for the exclusion screen | Source or qualification |
|---|---:|---:| --- |
| Balance-sheet assets at year end | PLN 33,000,000 | PLN 2,000,000 | unverified: retained statement; scoped source checks below do not qualify this whole row |
| Annual net sales of goods and products | PLN 66,000,000 | PLN 4,000,000 | unverified: retained statement; scoped source checks below do not qualify this whole row |
| Average annual full-time equivalent employment | 50 | 10 | unverified: retained statement; scoped source checks below do not qualify this whole row |

Read the complete status rules before classifying: the small definition tests the reporting and preceding year, uses the reporting year for a new activity or commencement of statutory books and separately preserves status until at least 2 limits are exceeded in **both** the reporting and preceding year. Apply the corresponding micro status and loss-of-status rules first. An election to use Annex 5 does not turn a micro entity into a small entity. Net sales have the Article 3(1)(30a)(a) definition, including discounts, grants and other adjustments and excluding VAT and other turnover taxes. These PLN size limits are distinct from the EUR audit thresholds.

Article 3(1h) treats specified entities as large for its listed simplifications regardless of size. Screen all 7 categories: Article 2(1)(3) regulated entities; entities intending to seek or seeking the relevant authorisation or ASI-manager registration; ASIs; regulated-market issuers including intended or pending admission; alternative-market issuers; domestic payment institutions; electronic-money institutions. 'Unlisted' alone is insufficient. The amendment in poz. 644 extends the deemed-large gate to Article 45(3)(1) and Article 49(6) from 29 May 2026. No simplification is established until the complete relevant gate is satisfied.

#### Decisions and required documents

A sp. z o.o. is a capital company under Commercial Companies Code, or **KSH**, Article 4 §1 point 2. The shareholders exercise the ordinary accounts approval function under KSH Articles 228 and 231; a sole shareholder exercises the meeting's powers under Article 156. Check the company agreement, representation, meeting procedure and actual resolutions. Management is not automatically the approving body.

Under Article 49c(1)(2), the approving body decides on the small balance sheet under 46(5)(5), P&L under 47(4)(5), additional information under 48(4) and management report relief under 49(5). Record each choice and its authority; do not infer all choices from a single size label. Management chooses the P&L variant. Other accounting-policy options have their own conditions and do not all require this same election.

For this qualified Annex 5 case, Article 45(2) requires **balance sheet, P&L and additional information**, comprising an introduction and notes. Audit alone does not add a cash flow statement or equity movement statement to this ordinary small entity's package. Article 45(3) has separate category tests; apply them before concluding those statements are unnecessary. Management report and audit report duties are assessed separately below.

Obtain the reporting period, prior statements, adjusted and unadjusted trial balances, actual chart and policies, asset register, inventory evidence, receivable/payable detail, bank and loan records, payroll/accrual support, tax working papers, events after year end, company agreement, size evidence, elections, audit assessment and all preparation/signature/approval dates. Missing necessary evidence produces **Needs Input**, with the affected statement or computation held.

## Filing requirements

### 8. Preparation, signatures, approval and filing

| Act | Responsible body and ordinary rule | Source or qualification |
|---|---| --- |
| Prepare annual statements | Management ensures preparation within 3 months from balance-sheet date and presents them to the competent bodies, Article 52(1) | unverified: retained statement; scoped source checks below do not qualify this whole row |
| Sign | Bookkeeper responsible for keeping the books and management sign, with signing dates; preserve refusals and written reasons. Apply the complete multi-person procedure below | unverified: retained statement; scoped source checks below do not qualify this whole row |
| Make documents available | For the sp. z o.o., provide annual statements and management report, and mandatory audit report where relevant, at least 15 days before the meeting, Article 68 | unverified: retained statement; scoped source checks below do not qualify this whole row |
| Audit, if required | Complete the required audit before approval, Article 53(1a); selection and contract must occur early enough for significant inventory attendance, Article 66 | unverified: retained statement; scoped source checks below do not qualify this whole row |
| Approve | Competent shareholders approve within 6 months of balance-sheet date, Article 53(1); ordinary meeting within 6 months after financial year end, KSH 231 §1 | unverified: retained statement; scoped source checks below do not qualify this whole row |
| Allocate profit/cover loss | Separate competent decision. For a mandatory-audit entity, Article 53(3) requires approval preceded by an unmodified or qualified audit opinion; allocation/coverage without that condition is void by law. The unaudited route under 53(4) requires prior approval. Apply KSH/company-agreement distribution restrictions separately | unverified: retained statement; scoped source checks below do not qualify this whole row |
| File approved package | Management files with the competent court register within 15 days of approval, Article 69(1) | unverified: retained statement; scoped source checks below do not qualify this whole row |
| If not approved on time | File within 15 days after the Article 53 approval deadline, then again within 15 days after subsequent approval, Article 69(2) | unverified: retained statement; scoped source checks below do not qualify this whole row |

KSH 231 §4¹ separately lets shareholders request the corresponding meeting documents from convening; provide them promptly and within 2 ordinary working days, electronically on request. Check those rights alongside Article 68's advance availability requirement.

These rules assume ordinary operating facts. The Act has separate bankruptcy, restructuring and succession routes, and KSH 231 §6 has a conditional full-year suspension/no-book-closure exception. Do not apply them to this case by inference. For a stipulated **31 December 2026** year end, the ordinary 3- and 6-month rules give **31 March 2027** and **30 June 2027**. If approval occurs on 30 June, the ordinary 15-day rule gives **15 July 2027**. These are conditional illustrations, not an extension to delay an earlier approval-triggered filing deadline or a verified live deadline.

#### Signature and format checks

Article 45 requires electronic statements with a qualified electronic signature, trusted signature or personal signature. A KRS-enterprise-register company using local Act rules uses the published ministerial logical structure and format. A scanned paper statement or a PDF working paper does not replace the required structured original.

Under Article 52(2b), multi-person management can use signature by at least one member **after** the other members give the specified compliance statements or refusals; refusal is equivalent to refusal of signature and requires reasons. The statements/refusals identify the accounts, including the date and time of the bookkeeper's signature. Attach and retain the required documents. Article 52(2d) permits the specified electronic signatures or handwritten paper originals for these statements/refusals; under 52(2e), a management member signing the accounts ensures electronic copies of paper originals. Check the procedure for each actual signatory. A single board signature without those conditions is insufficient. Management report signatures also apply 52(1)–(2e) correspondingly under 52(3), except that the bookkeeper does not sign that report, alongside Article 49(7).

The [official schema list](https://www.gov.pl/web/kas/struktury-e-sprawozdan) identifies **SFJMAZ(2), 2025/08/07/13818**, for small-entity statements in złoty and **SFJMAT(2), 2025/09/10/13846**, in thousands, for statements prepared from 1 January 2026. Verify the applicable current schema, rounding, technical validation and signatures on the actual preparation/submission date. This guide has not validated a completed XML file or a live submission.

#### Destination, package and consequences

Use the Ministry of Justice's **Repozytorium Dokumentów Finansowych, RDF**, through the official court-register service. [Ministry of Finance guidance](https://www.gov.pl/web/finanse/jakie-dokumenty-i-w-jakim-formacie-zgodnie-z-ustawa-o-rachunkowosci-jednostka-majaca-siedzibe-na-terytorium-rp-powinna-zlozyc-do-krs) identifies the annual accounts, approval/profit-allocation or loss-coverage resolution and applicable audit/management reports, in the form prepared and signed, plus required signature-related statements/refusals. Verify the authorised submitter and current RDF instructions; preparation, signing, approval and successful registration are separate events.

For this KRS-enterprise-register company, [current tax-authority guidance](https://podatki.gov.pl/e-sprawozdania-finansowe) routes the financial statements to **KRS**, without a duplicate statement submission to Szef KAS or the tax office. This does not remove the separate CIT return, payment, tax-book or other reporting duties. Establish their dates under the actual tax period and tax guide; do not substitute the accounts filing deadline for CIT-8.

Article 79 includes failure to submit required documents to the court register, arrange a mandatory audit or make Article 68 documents available, with a fine or restriction of liberty. Article 77 separately addresses unlawful/non-reliable books or statements, with a fine, imprisonment up to 2 years or both. Do not invent a flat late-filing fee or treat these criminal consequences as the complete set of court enforcement measures. Late filing, enforcement, possible liability and remedies require a qualified local reviewer.

## Rates and thresholds

| Item | Amount or rule | Conditions and official source |
|---|---|---|
| Small/micro size classification | See the complete PLN size table and both-year/new-activity/status rules in Scope statement | unverified in this migration; Accounting Act Article 3(1)(1a)/(1b)/(30a), with all exclusions retained: https://api.sejm.gov.pl/eli/acts/DU/2026/522/text.pdf |
| Mandatory audit | See the complete preceding-year 2-of-3 EUR/assets/sales/employment test under Audit assessment | unverified in this migration; distinguish at-least audit limits and Article 3(2) conversion from small-size not-exceeding limits: https://api.sejm.gov.pl/eli/acts/DU/2026/522/text.pdf |
| Book depreciation | No universal life, rate, value threshold or next-month start is established | unverified in this migration; company-supported Article 32/33/44b rules and capital-company exclusions remain under Computation rules: https://api.sejm.gov.pl/eli/acts/DU/2026/522/text.pdf |

## Computation rules

Execute the retained sections in order: validate the actual chart and balances, make supported recognition/measurement and closing adjustments, reconcile the chosen P&L variant and balance sheet, assess current/deferred tax separately and complete every applicable note. The detailed sections retain both Annex 5 P&L formats, the balance hierarchy and all 18 note categories.

### 2. Profit and loss statement

Use the management-selected Annex 5 variant consistently, with current and preceding-year figures. The English captions below are working translations; preserve the official Polish captions and schema when producing statutory statements. Article 47(3) separately identifies the revenues and costs of planned discontinued operations affecting future periods where the company remains a going concern. Do not invent an extraordinary-item subtotal: assess the exceptional or incidental item note instead.

#### Functional variant: wariant kalkulacyjny

| Caption | Content or calculation | Source or qualification |
|---|---| --- |
| A | Net sales of products and goods | unverified: retained statement; scoped source checks below do not qualify this whole row |
| B | Cost of products and goods sold | unverified: retained statement; scoped source checks below do not qualify this whole row |
| C | Selling expenses | unverified: retained statement; scoped source checks below do not qualify this whole row |
| D | General administration expenses | unverified: retained statement; scoped source checks below do not qualify this whole row |
| E | Sales profit/loss: A − B − C − D | unverified: retained statement; scoped source checks below do not qualify this whole row |
| F | Other operating income, including revaluation of non-financial assets | unverified: retained statement; scoped source checks below do not qualify this whole row |
| G | Other operating expenses, including revaluation of non-financial assets | unverified: retained statement; scoped source checks below do not qualify this whole row |
| H | Financial income, with the subdivisions below | unverified: retained statement; scoped source checks below do not qualify this whole row |
| I | Financial expenses, with the subdivisions below | unverified: retained statement; scoped source checks below do not qualify this whole row |
| J | Gross profit/loss: E + F − G + H − I | unverified: retained statement; scoped source checks below do not qualify this whole row |
| K | Income tax allocated to this result | unverified: retained statement; scoped source checks below do not qualify this whole row |
| L | Net profit/loss: J − K | unverified: retained statement; scoped source checks below do not qualify this whole row |

Financial income H has I dividends/profit participations from entities in which an equity involvement is held, including related entities with that involvement; II interest, including from related entities; III financial-asset disposal gains, including in related entities; IV financial-asset revaluation. Financial expenses I has I interest, including to related entities; II financial-asset disposal losses, including in related entities; III financial-asset revaluation.

#### Nature variant: wariant porównawczy

| Caption | Content or calculation | Source or qualification |
|---|---| --- |
| A | Net sales and equivalents: I net sales; II change in products, increase positive and decrease negative; III production cost of products for own use | unverified: retained statement; scoped source checks below do not qualify this whole row |
| B | Operating costs: I depreciation/amortisation; II materials and energy; III external services; IV wages; V social insurance and other benefits, including retirement benefits; VI other costs, including goods sold | unverified: retained statement; scoped source checks below do not qualify this whole row |
| C | Sales profit/loss: A − B | unverified: retained statement; scoped source checks below do not qualify this whole row |
| D | Other operating income, including revaluation of non-financial assets | unverified: retained statement; scoped source checks below do not qualify this whole row |
| E | Other operating expenses, including revaluation of non-financial assets | unverified: retained statement; scoped source checks below do not qualify this whole row |
| F | Financial income, with the same 4 subdivisions as functional H | unverified: retained statement; scoped source checks below do not qualify this whole row |
| G | Financial expenses, with the same 3 subdivisions as functional I | unverified: retained statement; scoped source checks below do not qualify this whole row |
| H | Gross profit/loss: C + D − E + F − G | unverified: retained statement; scoped source checks below do not qualify this whole row |
| I | Income tax allocated to this result | unverified: retained statement; scoped source checks below do not qualify this whole row |
| J | Net profit/loss: H − I | unverified: retained statement; scoped source checks below do not qualify this whole row |

Keep production changes and own-use production separate from sales. Reconcile expense-by-nature and functional cost records so that inventory production, capitalised work and cost of sales are not counted twice. Articles 46–50 and Annex 5 govern presentation; a convenient generic P&L template cannot replace them.

### 3. Balance sheet

Use Annex 5's **Aktywa / Pasywa** structure, retaining its hierarchy and comparative figures. These are statement captions, not ledger account codes.

| Assets, Aktywa | Equity and liabilities, Pasywa | Source or qualification |
|---|---| --- |
| A. Non-current assets | A. Equity | unverified: retained statement; scoped source checks below do not qualify this whole row |
| I. Intangible assets | I. Basic/share capital | unverified: retained statement; scoped source checks below do not qualify this whole row |
| II. Tangible non-current assets, including fixed assets and assets under construction | II. Supplementary capital, including issue proceeds above nominal value | unverified: retained statement; scoped source checks below do not qualify this whole row |
| III. Long-term receivables | III. Revaluation reserve, including fair-value revaluation | unverified: retained statement; scoped source checks below do not qualify this whole row |
| IV. Long-term investments, including property and long-term financial assets | IV. Other reserve capital | unverified: retained statement; scoped source checks below do not qualify this whole row |
| V. Long-term prepayments/accruals | V. Prior-years' profit/loss | unverified: retained statement; scoped source checks below do not qualify this whole row |
| B. Current assets | VI. Current net profit/loss | unverified: retained statement; scoped source checks below do not qualify this whole row |
| I. Inventories | VII. Interim deductions from net profit, negative | unverified: retained statement; scoped source checks below do not qualify this whole row |
| II. Short-term receivables, including trade receivables split up to and over 12 months | B. Liabilities and provisions | unverified: retained statement; scoped source checks below do not qualify this whole row |
| III. Short-term investments, including short-term financial assets and, within those, cash in hand/bank | I. Provisions, including retirement and similar benefits | unverified: retained statement; scoped source checks below do not qualify this whole row |
| IV. Short-term prepayments/accruals | II. Long-term liabilities, including loans/borrowings | unverified: retained statement; scoped source checks below do not qualify this whole row |
| C. Unpaid contributions to basic/share capital | III. Short-term liabilities, including loans/borrowings, trade liabilities split up to and over 12 months and special funds | unverified: retained statement; scoped source checks below do not qualify this whole row |
| D. Own shares | IV. Accruals/deferred items | unverified: retained statement; scoped source checks below do not qualify this whole row |
| Total assets | Total equity and liabilities | unverified: retained statement; scoped source checks below do not qualify this whole row |

Follow Article 3(1)(18)/(22) and Annex 5: short-term receivables/payables include **all trade balances**, with the required up-to/over-12-month subcaptions. Other balances follow their separate nature and maturity tests. Unpaid capital and own shares are separate **asset** captions in this format; do not import a generic contra-equity presentation. Show accumulated depreciation and impairment in the relevant carrying values. Keep unlike balances separate; financial-asset/liability netting requires Article 46(2a)'s unconditional right and net/simultaneous settlement intention. Article 50 allows necessary detail and omission of positions absent in **both** years, not indiscriminate removal of statutory subdivisions.

### 4. Mapping the entity's chart

Article 10 requires management's written Polish accounting policies, including its own chart, event classifications, subsidiary-ledger links, books/data structures, processing system and protection. It does not prescribe universal numerical account codes.

Create an entity-specific mapping with **actual code, account name, debit/credit balance, source/subledger, statutory caption, note, comparative caption and any justified split**. Validate all trial-balance codes against that approved chart. An unfamiliar code requires evidence, not a guessed national code.

| Actual account content | Mapping rule | Source or qualification |
|---|---| --- |
| Fixed asset cost and accumulated depreciation/impairment | Net to the relevant A.I/A.II asset class; retain separate movement schedules | unverified: retained statement; scoped source checks below do not qualify this whole row |
| Stock, product movements and goods sold | B.I inventory plus the selected P&L variant's distinct sales/cost/product-change captions; reconcile the cost system | unverified: retained statement; scoped source checks below do not qualify this whole row |
| Trade and other debtors | Relevant receivable caption with statutory maturity and nature splits; reconcile impairment and tax separately | unverified: retained statement; scoped source checks below do not qualify this whole row |
| Bank, cash and investments | B.III or A.IV as the statutory nature/classification requires; identify restricted balances and any separate valuation policy | unverified: retained statement; scoped source checks below do not qualify this whole row |
| Share capital, reserves, prior and current results | Separate equity captions; match legal documents and the P&L result; identify unpaid capital and own shares separately | unverified: retained statement; scoped source checks below do not qualify this whole row |
| Loans, trade creditors, tax, payroll and other obligations | Relevant liability/provision/deferred caption and required maturity subdivisions; do not offset unrelated debit balances | unverified: retained statement; scoped source checks below do not qualify this whole row |
| Revenue, operating costs, interest and revaluations | Selected Annex 5 P&L caption; identify capitalised amounts, related-entity subdivisions and note disclosures | unverified: retained statement; scoped source checks below do not qualify this whole row |
| Current/deferred income tax | P&L tax only for the part attributable there; identify equity-related tax separately and reconcile assets/liabilities | unverified: retained statement; scoped source checks below do not qualify this whole row |

Every account must be mapped once, or split with a documented reconciliation whose total equals the account. Clear suspense, unexplained balances, inconsistent opening figures and unbalanced trial balances before final statements. A mapping table alone does not establish recognition or measurement.

### 5. Introduction and notes

The Annex 5 introduction gives the company's name, office/address and register number; limited duration where relevant; period; simplifications actually used; going concern basis and threats; chosen policies for valuation, depreciation, result and preparation. Do not list an unelected relief as an adopted policy.

Its additional information includes **in particular** all 18 categories below. Assess each, record the factual basis for inapplicability and add material information required by Articles 4(1a) and 48(1). Annex 5 is not an exhaustive safe harbour. Include proposed profit allocation/loss coverage under Article 48(1); approval of accounts does not itself authorise that distribution.

1. Movement schedules for tangible fixed assets, intangibles and long-term investments: opening value, revaluation/acquisition/disposal/internal-transfer movements, closing value and corresponding accumulated depreciation/amortisation movements.
2. Non-current-asset impairment during the year, separately financial and non-financial.
3. Goodwill and explanation of its amortisation period under Article 44b(10).
4. Where fair value is used: significant non-market assumptions; long-/short-term fair values and result/reserve effects; short-term derivative scope, nature and material terms; revaluation reserve movements.
5. Active deferred costs representing the difference between financial assets received and the payment obligation.
6. Long-term liabilities by balance-sheet position with contractual remaining maturity beyond 5 years; secured liabilities and nature/form of security.
7. Links between multiple balance-sheet positions for the same asset/liability, including long-/short-term splits.
8. Contingent liabilities, guarantees/sureties and bill guarantees, asset security and its form; separate pension/similar contingencies and related/associated-entity contingencies.
9. Assets under construction cost, including interest and exchange differences capitalised during the year.
10. Interest and exchange differences capitalised into goods or product cost during the year.
11. Amount and nature of individual exceptionally large or incidental income/expense items.
12. Average annual employment.
13. Loans/advances to management, supervisory and administrative bodies, principal terms and interest, repayments, write-downs/forgiveness and guarantees/sureties, totalled for each category.
14. Material subsequent events omitted from the statements and their financial-position/result effect.
15. Material policy and preparation-method changes with reasons.
16. Numerical information and explanations ensuring comparative consistency.
17. Lowest-level consolidating parent's name and office if a subsidiary. A group relationship triggers this companion's scope refusal, not an invented 'none'.
18. Complete own-share information where Article 49(5) management-report relief is used, as specified in section 10.

Cross-reference notes to statements and schedules. Assess securities, guarantees, commitments, related parties and events even if no corresponding trial-balance account exists. A zero balance does not prove absence of a disclosure.

### 6. Closing, measurement and depreciation

Apply economic substance, accrual and matching, prudence and materiality under Articles 4–8. Similar individually small items may be material in aggregate. Small status does **not** let this capital company elect the Article 7(2b) prudence relief: Article 7(2c)(2) excludes it. Nor can it elect Article 39(6)'s employee-benefit accrual relief, because 39(7)(2) excludes capital companies.

Article 28 supplies balance-date measurement, including fixed/intangible asset cost less depreciation/impairment, inventory capped at net selling price, prudent receivable valuation and reliable provision estimates. Assess permanent impairment under 28(7), probable/certain reliably measurable obligations under 35d and accrued service/employee/warranty obligations under 39. Establish the evidence and recognition destination before posting. Do not substitute a generic aged-debt percentage or spread an existing obligation merely over a lease term.

#### Inventory and evidence

Articles 26–27 distinguish physical counts, external confirmations and documentary verification. Cash outside banks, physical securities, tangible stock and qualifying fixed assets use the count route; bank/external financial assets, receivables/loans and entrusted assets use confirmation subject to verification exceptions. Inaccessible assets, land/property rights, disputed/doubtful balances, public-law balances, balances with persons without accounting books and justified impossibility of the normal method require documentary/value verification. Silence is not confirmation.

The 3-month-before-year-end to day-15-next-year window is conditional, with movement reconciliation and exclusions including cash, securities, work in progress and Article 17(2)(4) stock expensed on purchase/manufacture. Guarded stock with quantity/value records can qualify for the 2-year alternative; specified property and guarded fixed assets/construction equipment can qualify for 4 years. Verify every condition rather than treating these as small-company privileges. Count third-party property where required and notify owners. Document inventory results and explain/settle differences in the books of the year to which the inventory date belongs.

#### Depreciation and amortisation schedule

For every asset record its actual code/class, cost, acquisition and acceptance-for-use dates, residual value, method, economic useful life or rate, part-period convention, additions/disposals, impairment, accumulated charges, closing carrying value, initial recognition destination and later release from capitalised cost.

Article 32 requires systematic planned allocation over the established economic period. Start **no earlier than acceptance for use**; end **no later than** full allocation, designation for liquidation/sale or discovery of a shortage, with possible residual sale value. Determine method and period/rate on acceptance using utilisation, technological/economic change, capacity, restrictions and residual value. Verify periods/rates periodically and correct subsequent years prospectively. The Act does not supply a universal typical life, rate, straight-line method, annual review frequency or next-month start. Obtain the supported company policy and asset facts before calculating a charge.

Article 32(6) permits collective or one-off depreciation for assets of low individual value without setting a monetary threshold. **Do not apply tax depreciation automatically:** the 32(7) tax-rule option is barred to capital companies by 32(8)(2). Article 33 imports the relevant rules for intangibles. Completed development costs require all 33(2) conditions and economic-life amortisation; the 5-year maximum applies only where that life exceptionally cannot be estimated reliably. Acquired goodwill has its own 44b(10) straight-line charge to other operating expenses over economic useful life, with a 5-year maximum only if life cannot reliably be estimated. Acquisition recognition and negative-goodwill calculations require a separately qualified transaction workflow.

Distinguish a policy change under Article 8(2), with reasons, quantified effects and comparability, from a prospective depreciation estimate correction under 32(3). Generic workflow formulas do not create a policy election.

#### Other ordinary measurement policies

Article 34(4) permits weighted average, FIFO, LIFO or the stated specific-identification method for qualifying similar inventories with differing costs. Use the documented, consistent company choice. Purchase-price, work-in-progress and standard-cost simplifications have separate non-distortion, timing and valuation conditions; do not omit work in progress solely because the company is small. Inventory write-downs to net selling price enter **other operating costs**, Article 34(5), rather than automatically the generic base's cost-of-sales entry. Article 35c governs reversal when the cause ceases.

Under Article 35b, use payment probability, debtor circumstances, security and reliable estimates for receivable impairment. This can include justified general impairment of overdue or not-yet-due balances with a significant non-collection probability. No statutory flat ageing percentage is established here. Charge operating or finance costs according to the receivable's nature; account for later write-off and reversal separately. A debtor's insolvency does not mean the reporting company itself fails this guide's solvency scope. Tax deductibility needs its own rules.

Article 30 generally uses the balance-date NBP mean rate for foreign-currency balance-sheet measurement, with express exceptions. Transaction-date entries distinguish the rate actually applied by the transaction's nature for currency dealings/settlements from the preceding-day NBP mean rate for other cases or where an actual rate is unjustified. Do not assume every quoted bank rate was applied, use one rate for every purpose or replace the statutory preceding-day wording with an unqualified 'previous working day'. Resolve publication-calendar and no-NBP-rate cases before computing. Exchange differences generally enter finance income/costs, but qualifying capitalisation and investment routes differ under Articles 28, 30 and 35.

For leases, Article 3(4) assigns the asset to the user if any of its 7 conditions holds: transfer of title; below-market purchase right; term at least 3/4 of economic life with the stated substantial-correspondence test; discounted contractual payments exceeding 90% of inception market value with the specified inclusions/exclusions; favourable promised renewal; termination costs/losses borne by the user; or user-specific adaptation preventing other use without major change. Article 3(5) supplies the corresponding provider classification. Eligible small entities may instead elect tax-rule classification under **3(6)**, subject to 3(1h) and the actual tax rules/contracts. That option has no capital-company exclusion here and does **not** create entitlement to the barred tax-depreciation election.

Article 41 distinguishes advance receipts for future performance and conditional asset/development funding from earned revenue. Qualifying funding not required by separate law to enter equity is released to other operating income alongside depreciation/amortisation. Check grant terms and applicable law. Investment purpose, initial/subsequent valuation, disposal, reserve recycling and transfer rules under Articles 3(1)(17), 28 and 35 also differ by category. Article **28b** permits an eligible small entity to disapply regulations issued under **81(2)(4)**, subject to the deemed-large gate; record the actual policy choice and continuing Act obligations. Those regulations were not qualified here. If their applicability or the policy is unresolved, hold the affected financial-instrument measurement, including ordinary balances to which they may apply. Derivatives, hedge accounting, complex instruments, investment-property policy and production/service contracts under 34a–34d require their complete applicable rules and evidence before entries; hold those affected computations rather than extrapolating these ordinary rules.

#### Information after year end

Under Article 54, material information received after preparation but before approval, or information invalidating going concern, requires appropriate amendment and entries in the year concerned; notify the auditor where applicable. A later event not changing the balance-date condition receives the appropriate note. Effects of information received after approval enter the year received. A prior-year error that makes the prior statements fail Article 4(1) goes to equity as prior-year profit/loss under 54(3); that is not the route for every minor error.

### 7. Current and deferred tax

Establish Polish tax residence, ordinary CIT status, accounting/tax periods and the complete applicable computation before calculating current tax. Use the qualified period rules and holds in `pl-corporate-income-tax`, then reconcile accounting profit to the separate tax-source bases, timing/permanent differences, losses, deductions, credits and advances. Do not equate small accounting status with 9% CIT eligibility, or apply a headline rate to book profit. Its minimum-tax, Estonian CIT, group, financial-sector and Pillar Two refusals continue to hold the affected entry here.

Articles 37 and 42 distinguish the income-tax charge from payment and payable balances. Separate current expense, advance payments, settlement payable/receivable and items recognised outside P&L. Do not book a tax payment itself as this year's P&L charge without the reconciliation.

Article 37 uses **carrying amount versus tax base** for temporary differences. Recognise deductible temporary differences and usable tax losses as deferred-tax assets subject to prudence, and taxable temporary differences as deferred-tax provisions. Use rates applicable when the obligation arises, with evidence for future utilisation. Show assets/provisions separately unless the legal simultaneous-settlement condition permits netting. Attribute equity-related deferred tax to equity; only the P&L portions enter the Annex 5 tax caption. Differences between accounting and taxable profit alone do not establish all temporary differences or their recognition.

Article 37(10) separately permits eligible micro/small entities to omit deferred-tax assets and provisions. There is no capital-company exclusion in that paragraph, but the Article 3(1h) gate still applies. Record and disclose the actual accounting-policy choice; it does not waive current CIT. Without an established choice, tax bases, utilisation evidence, applicable rates or complete current computation, return **Needs Input** and hold the affected entries and final statements. Article 37(12)'s specified minimum/top-up-tax deferred-balance prohibition is not a general current-CIT exemption.

## Edge cases and special rules

### 9. Audit assessment

Article 64 separately covers consolidated statements, named regulated/entity categories, certain special statements and annual statements of continuing entities. Do not label all small companies audit-exempt.

For an ordinary entity in the remaining-entity route, mandatory audit applies where the **preceding financial year** met at least **2 of 3**:

| Measure | At least | Source or qualification |
|---|---:| --- |
| Average annual full-time equivalent employment | 50 | unverified: retained statement; scoped source checks below do not qualify this whole row |
| Balance-sheet assets | EUR 3,125,000 equivalent in PLN | unverified: retained statement; scoped source checks below do not qualify this whole row |
| Net sales of goods and products | EUR 6,250,000 equivalent in PLN | unverified: retained statement; scoped source checks below do not qualify this whole row |

Use Article 3(2)'s NBP average EUR rate at the relevant balance-sheet date. Do not import the first-working-day-of-October conversion applicable to a different books threshold. The amended financial thresholds first apply to financial years beginning after 31 December 2024, using the stated preceding-year transition. Test actual figures and all category/special-route requirements before recording the conclusion. Annex 5 eligibility and audit liability can coexist.

The approving body selects the audit firm unless the governing rules provide otherwise; management cannot make that selection. Management concludes the contract in time for significant inventory attendance; the first statutory audit contract lasts at least 2 years, with extensions of at least 2 years. Independence, validity and termination rules remain applicable. Poz. 640 changes the Article 66(6)(1) invalidity references from 28 May 2026 and applies to audits already begun but unfinished; use the amended provision, not the unamended consolidated text alone. A draft or purportedly signed report does not establish audit validity.

### 10. Management report

Article 49(1) normally requires the capital company's management report. Article 49(5), with the approving-body election under 49c, permits the eligible small entity to omit it **only if** the additional information includes all required own-share disclosures: reasons for acquisitions; numbers and nominal values, or carrying values where relevant, acquired/disposed and capital proportions; consideration; all acquired/retained own shares and proportions. Assess the required disclosure even where management reports no transactions. No-transaction facts do not themselves elect the relief.

If a report is prepared, cover the material financial position/result, risks and threats, significant events through approval, expected development, important R&D, current/expected financial situation, own shares, branches and financial-instrument risks/management. Include relevant financial KPIs and the Article 49(3a) statement cross-references/explanations. Article **49(6)** separately lets eligible micro/small entities omit **49(3)(2)** non-financial KPIs and employee/environment information from the report they do prepare. It does not omit financial KPIs, paragraph 2 risks or the entire report. The amended deemed-large gate includes paragraph 6. Do not import Article 49a's micro-only fair-presentation presumption into Annex 5.

### 11. Going concern

Management assesses all information available when preparing the statements under Article 5(2), looking forward **at least 1 year from the balance-sheet date**. Assess continuity without material reduction, liquidation or bankruptcy unless inconsistent with facts or law. Record forecasts, financing/repayment terms, legal/factual threats and management's evidence. The horizon starts at the balance-sheet date, not preparation or approval, and the assessment is updated for material subsequent information.

State the going concern basis and threats in the introduction and supply all material explanations. A threat is not resolved by writing a standard confirmation. If that basis is inappropriate, stop this going concern workflow and qualify the alternative measurement/reporting route; Article 29 and insolvency procedures are not established here.

## Self-checks

### 12. Currency, presentation and delivery

Books and statutory statements use Polish and **PLN**, Articles 9 and 45(5). Thousands of PLN are permitted only where they do not distort the picture. Label the unit consistently on statements, notes, mapping and movement schedules; reconcile exact ledger values before rounding and disclose any presentation rounding difference rather than altering a source balance. For human-readable working papers, document a consistent decimal-comma presentation; validate actual machine numbers against the chosen schema instead of inserting visual thousands separators into numeric fields. This working-paper convention is not an attestation of an XML schema's numeric rules. Foreign-currency transactions follow their separate measurement rules in section 6.

Deliver the base's **P&L, balance sheet, notes, year-end adjustment schedule, filing checklist and reviewer brief**. The brief must identify eligibility/elections, policies, mapping, currentness and technical schema checks, material estimates, audit/report decisions, subsequent events, signatures and outstanding facts. Reconcile all statement totals, comparatives, notes and tax recognition locations; account for every adjusted trial-balance balance. Hold final statements, signatures and filing where a mandatory fact, source or computation is unresolved. This companion supplies the scoped statutory framework; it supplies no professional sign-off, actual company classification or filing confirmation.

### Hypothetical case 1: both P&L variants reconcile

All amounts below are invented PLN working-paper amounts, not a sample statutory filing. Assume the ordinary small-but-not-micro Annex 5 scope, valid elections, complete current/prior-period records and all accounting recognition and classification decisions have already been qualified. Sales are 1,200,000; cost of sales 700,000, selling costs 50,000 and administration 100,000. Other operating income/costs are 20,000/30,000 and financial income/costs 10,000/20,000. Separately supported total P&L tax expense is supplied as 60,000, not computed from book profit or a presumed CIT rate. For the nature variant, supplied cost categories total 850,000; inventory change and own work capitalised are both zero, with no unexplained functional/nature difference. Sales profit is 350,000 in each variant, operating profit 340,000, gross profit 330,000 and net profit 270,000. The block checks arithmetic and variant reconciliation only; it does not qualify the ledger or notes.

```oa-check
name: PL Annex 5 hypothetical P and L reconciliation
inputs:
  sales: 1200000
  cost_of_sales: 700000
  selling: 50000
  administration: 100000
  other_operating_income: 20000
  other_operating_costs: 30000
  financial_income: 10000
  financial_costs: 20000
  tax_expense: 60000
  depreciation: 50000
  materials: 200000
  external_services: 100000
  taxes_fees: 20000
  wages: 300000
  social_other: 100000
  other_nature: 80000
  inventory_change: 0
  own_work: 0
steps:
  - functional_sales_profit: sales - cost_of_sales - selling - administration
  - functional_operating: functional_sales_profit + other_operating_income - other_operating_costs
  - gross_profit: functional_operating + financial_income - financial_costs
  - net_profit: gross_profit - tax_expense
  - nature_costs: depreciation + materials + external_services + taxes_fees + wages + social_other + other_nature
  - nature_sales_profit: sales + inventory_change + own_work - nature_costs
  - variant_difference: nature_sales_profit - functional_sales_profit
expected:
  functional_sales_profit: 350000
  functional_operating: 340000
  gross_profit: 330000
  net_profit: 270000
  nature_costs: 850000
  nature_sales_profit: 350000
  variant_difference: 0
```

### Hypothetical case 2: eligible deferred-tax omission policy

Compare only after Article 37(10) eligibility, all Article 3(1h) exclusions and a valid documented omission policy have been established. Assume separately qualified current tax expense of 60,000 and a deferred tax expense of 10,000 that belongs wholly in P&L, with no equity, OCI, uncertain recognition, prior-period or netting issue. These are supplied accounting amounts, not a CIT or temporary-difference computation. With gross profit 330,000, recognition gives net profit 260,000; valid omission gives 270,000, a 10,000 presentation difference. This does not change current tax payable or cash tax and is not a recommendation to choose the larger profit; unsupported eligibility or tax measurement holds the comparison.

```oa-check
name: PL Annex 5 hypothetical policy decision: deferred tax presentation
inputs:
  gross_profit: 330000
  current_tax_expense: 60000
  deferred_tax_expense: 10000
steps:
  - net_with_deferred: gross_profit - current_tax_expense - deferred_tax_expense
  - net_with_valid_omission: gross_profit - current_tax_expense
  - net_difference: net_with_valid_omission - net_with_deferred
expected:
  net_with_deferred: 260000
  net_with_valid_omission: 270000
  net_difference: 10000
```
## Sources

This is a template migration of retained research, not a new law-reading exercise or whole-guide current-law verification. The dated events below identify historical source checks with their actual retained extents. Acquisition times, legal cutoffs and this migration date are not reading dates. Every retained table row is explicitly unverified in this migration; the source index does not independently qualify every statement on that row. Resolve all applicable holds before using a figure.

| Official source | Exact URL | Recorded date and event | Reading extent and limits |
|---|---|---|---|
| Dz.U. 2026 poz. 522 | https://api.sejm.gov.pl/eli/acts/DU/2026/522/text.pdf | 2026-11-01: historical independent source check | Selected complete articles/clauses and complete Annex 5 only; 89-unit retained map. Legal cutoff 26 March 2026, not a whole-Act reading. |
| Dz.U. 2026 poz. 640 | https://api.sejm.gov.pl/eli/acts/DU/2026/640/text.pdf | 2026-11-01: historical independent source check | Complete 1-page Act, all 4 articles and metadata; audit changes and transition. |
| Dz.U. 2026 poz. 644 | https://api.sejm.gov.pl/eli/acts/DU/2026/644/text.pdf | 2026-11-01: historical independent source check | Complete selected Articles 1, 2, 6, 18 and 19 and relevant footnotes; not the whole 35-page Act. Later ESAP/KSH dates are not 2026 duties. |
| Dz.U. 2026 poz. 1206 | https://api.sejm.gov.pl/eli/acts/DU/2026/1206/text.pdf | 2026-11-01: historical independent source check | Complete Articles 2 and 57 only, not the whole 51-page Act; 11 January 2027 commencement qualified. |
| Dz.U. 2024 poz. 18 | https://api.sejm.gov.pl/eli/acts/DU/2024/18/text.pdf | 2026-11-01: historical independent source check | Complete KSH Articles 4, 151, 156, 191-197, 227, 228 and 231; legal cutoff 5 December 2023; later full amendment chain not established. |
| Dz.U. 2024 poz. 96 | https://api.sejm.gov.pl/eli/acts/DU/2024/96/text.pdf | 2026-11-01: historical independent source check | Complete constitutional judgment only; broadcasting subject excluded. |
| Dz.U. 2026 poz. 176 | https://api.sejm.gov.pl/eli/acts/DU/2026/176/text.pdf | 2026-11-01: historical independent source check | Complete selected Article 1 and Articles 28-35 only; not whole Act. |
| Dz.U. 2026 poz. 187 | https://api.sejm.gov.pl/eli/acts/DU/2026/187/text.pdf | 2026-11-01: historical independent source check | Complete selected Article 138 and Articles 147-161 only; not whole Act. |
| Financial statements guidance | https://podatki.gov.pl/e-sprawozdania-finansowe | 2026-11-01: original guide records guidance checked | Selected package/routing information; no live XML, valid signature or RDF filing acceptance. |
| KRS document guidance | https://www.gov.pl/web/finanse/jakie-dokumenty-i-w-jakim-formacie-zgodnie-z-ustawa-o-rachunkowosci-jednostka-majaca-siedzibe-na-terytorium-rp-powinna-zlozyc-do-krs | 2026-11-01: original guide records guidance checked | Selected document/format information; no live filing validation. |
| Structured schema guidance | https://www.gov.pl/web/kas/struktury-e-sprawozdan | 2026-11-01: original guide records guidance checked | Selected published schema information; actual current XML/schema/submission unvalidated. |

### Sources and temporal limits

- [Accounting Act consolidation, Dz.U. 2026 poz. 522](https://api.sejm.gov.pl/eli/acts/DU/2026/522/text.pdf): selected complete provisions identified above and complete Annex 5, with its 26 March 2026 legal cutoff. The reproduced 2024 poz. 1863 Article 14 distinguishes first-year application from commencement: the listed revised classifications/simplifications and Annex 5 first apply for years beginning after 31 December 2023; the audit financial thresholds have their separate later transition.
- [Dz.U. 2026 poz. 640](https://api.sejm.gov.pl/eli/acts/DU/2026/640/text.pdf): complete Act, including Accounting Act Article 66(6)(1), audit transition and commencement on 28 May 2026.
- [Dz.U. 2026 poz. 644](https://api.sejm.gov.pl/eli/acts/DU/2026/644/text.pdf): complete Accounting Act-changing Article 1 and relevant transition/commencement. Current classification/reporting changes start 29 May 2026; the selected ESAP collection changes start 10 January 2028 and are not a 2026 ESAP duty. KSH-changing Article 6 starts 10 January 2030.
- [Dz.U. 2026 poz. 1206](https://api.sejm.gov.pl/eli/acts/DU/2026/1206/text.pdf): complete Accounting Act-changing Article 2 and commencement Article 57. Article 2 starts **11 January 2027**, changing excluded bank/financial/insurance branch and upper-parent routes. It does not extend ordinary Article 69(1)/(2) 15-day periods to 60 days. This is not a review of the entire 51-page Act.
- [KSH consolidation, Dz.U. 2024 poz. 18](https://api.sejm.gov.pl/eli/acts/DU/2024/18/text.pdf), legal cutoff 5 December 2023: complete Articles 4, 151, 156, 191–197, 227, 228 and 231 for the scoped company-law link. Selected relevant later units in [2024 poz. 96](https://api.sejm.gov.pl/eli/acts/DU/2024/96/text.pdf), [2026 poz. 176](https://api.sejm.gov.pl/eli/acts/DU/2026/176/text.pdf), [2026 poz. 187](https://api.sejm.gov.pl/eli/acts/DU/2026/187/text.pdf) and 2026 poz. 644 do not change that ordinary sp. z o.o. approval link or 6-month meeting rule. This does not establish a complete future KSH chain or the validity of actual meeting procedure.
- Ministry of Finance [electronic statements guidance](https://podatki.gov.pl/e-sprawozdania-finansowe), [KRS package guidance](https://www.gov.pl/web/finanse/jakie-dokumenty-i-w-jakim-formacie-zgodnie-z-ustawa-o-rachunkowosci-jednostka-majaca-siedzibe-na-terytorium-rp-powinna-zlozyc-do-krs) and [schema list](https://www.gov.pl/web/kas/struktury-e-sprawozdan), checked 1 November 2026. Selected requirements do not attest to a completed file's acceptance or future portal availability.

The retained sources were read for the selected units, not as a whole-law, all-regulations, case-law or administrative-practice review. Specific transaction policies, entity evidence, legal changes after the check and actual tax/filing implementation require further qualification before reliance.

Not yet confirmed: all retained fact, scope, measurement, amendment-chain, schema, signature, approval, audit and filing holds; exact original per-URL reading days beyond the recorded historical events; current law and technical filing requirements at actual preparation/submission; professional clearance. The unused original KSH 2000 HTML and a fourth merely captured RDF announcement are not promoted to current, dated sources.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon. The upstream project is maintained at [openaccountants.com](https://www.openaccountants.com). This fork's migrated version and recorded review status are maintained in [ryanduguid/openaccountants](https://github.com/ryanduguid/openaccountants); upstream services do not publish or verify this fork's changes.

<!-- openaccountants-cta-block -->

---

## Talk to a verified accountant

This guide is maintained in the
[ryanduguid/openaccountants fork](https://github.com/ryanduguid/openaccountants).
Check its quality tier, recorded review status and cited sources before use.
Choose a practitioner whose credentials and engagement scope you have verified.
The links below are optional upstream services; they do not publish or verify
this fork's changes.

- Upstream connection service: https://www.openaccountants.com/connect
- Upstream accountant network: https://www.openaccountants.com/network

> **General reference only.** This document does not constitute tax, legal, or
> financial advice. Verify figures against the cited primary sources or with a
> licensed professional before relying on them.
