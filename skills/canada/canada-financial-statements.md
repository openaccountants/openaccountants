---
name: canada-financial-statements
description: Use this skill when preparing, reviewing, or advising on annual financial statements for a Canadian company. Trigger on phrases like "ASPE", "IFRS Canada", "Canadian GAAP", "CPA Canada Handbook", "financial statements Canada", "compilation engagement", "review engagement Canada", "audit Canada", "CBCA", "OBCA", "annual return Canada", "CSRE 2400", or any question about preparing and reporting statutory accounts under Canadian corporate law. Covers ASPE/IFRS frameworks, assurance level options, required statements, formats, notes, filing requirements, and audit/review thresholds.
version: 1.1
jurisdiction: CA
tax_year: 2025
tax_year_notes: Historical 2025 statement workpaper; dated statutory follow-ups and proposed future amendments do not recertify every framework or the whole skill for the current year.
last_updated: 2026-11-25
depends_on:
  - financial-statements-workflow-base
category: financial-statements
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
reviewed_by: "Nathan Wiebe"
reviewed_on: 2026-11-03
tier: 1
domain: financial-statements
---

# Canada Financial Statements

## Canada Financial Statements Skill v1.1

This corrects the historical 2025 workpaper. **HOLD (unverified)** means the affected conclusion cannot be used to select a framework, recognize/measure an amount, claim compliance or decide a filing/assurance obligation until the named operative source and case inputs are established. A held accounting-standard statement is a research topic, not current advice. No operative licensed ASPE/IFRS/assurance text was read in this unit.

## Rates and thresholds

Reviewed against the cited tax authorities by **Nathan Wiebe** on 2026-06-21.
That historical attribution does not approve this proposed correction. Unresolved conditions and accounting-standard claims remain explicitly held below.

### Financial Statements

- **PAE (publicly accountable)** — HOLD (unverified operative Handbook scope/requirements): IFRS (Part I)  _(CPA Canada Handbook Part I; IAS 1)_
- **Private enterprise** — HOLD (unverified operative Handbook scope/requirements): ASPE (Part II)  _(CPA Canada Handbook Part II)_
- **Not-for-profit** — HOLD (unverified operative Handbook scope/requirements): ASNPO (Part III)  _(CPA Canada Handbook Part III)_
- **Goodwill** — HOLD (unverified operative standard): do not use a current five/ten-year amortization election or the old 3064.87/40-year citation. The original AcSB project describes proposed amendments, planned final issuance in the first half of 2027; its exposure explanation proposes a 1 January 2029 start with early application. Proposed early application does not establish an issued election. The current base-rule and IFRS treatments also remain held pending operative standards. [AcSB project](https://www.frascanada.ca/en/aspe/projects/goodwill-and-acquired-intangibles); [exposure explanation](https://www.frascanada.ca/en/aspe/projects/goodwill-and-acquired-intangibles/in-brief-acsb-ed-relief-from-recognition-acquired-intangible-assets-amortization-goodwill).
- **Leases** — HOLD (unverified operative Handbook scope/requirements): ASPE: finance/operating; IFRS: right-of-use (IFRS 16)  _(CPA Canada Handbook ASPE s.3065; IFRS 16)_
- **Revenue** — HOLD (unverified operative Handbook scope/requirements): ASPE: risks/rewards; IFRS: five-step (IFRS 15)  _(CPA Canada Handbook ASPE s.3400; IFRS 15)_
- **CBCA** — Non-distributing corporation: all shareholders, including non-voting, may resolve not to appoint an auditor until the following annual meeting. No revenue threshold appears in this provision; financial statements remain a separate duty. [CBCA 163](https://laws-lois.justice.gc.ca/eng/acts/C-44/section-163.html).
- **OBCA (Ontario)** — HOLD (unverified current applicability): indexed section 148 text was read, but direct current-page version/currency was unresolved. Do not certify a present waiver from that receipt. [official Act](https://www.ontario.ca/laws/statute/90b16).
- **CNCA (federal NPO)** — Use the soliciting/non-soliciting, inclusive-revenue and annual-resolution decision tree in Section 10; no universal below-50,000/below-250,000 shortcut. [Corporations Canada](https://ised-isde.canada.ca/site/corporations-canada/en/not-profit-corporations/financial-statements-and-review).
- **Charity** — CRA recommends professional audit where income exceeds $250,000; that statement is not a mandatory CRA audit threshold. Corporate law, funders and other actual obligations remain separate. [CRA charity statements](https://www.canada.ca/en/revenue-agency/services/charities-giving/charities/operating-a-registered-charity/financial-statements.html).
- **Audit** — HOLD (unverified operative Handbook scope/requirements): CAS  _(CPA Canada Handbook — CAS)_
- **Review** — HOLD (unverified operative Handbook scope/requirements): CSRE 2400  _(CPA Canada Handbook — CSRE 2400)_
- **Compilation (NTR)** — HOLD (unverified operative Handbook scope/requirements): CSRS 4200  _(CPA Canada Handbook — CSRS 4200)_
- **T2 corporate return** — 6 months after fiscal year-end  _(ITA s.150(1)(a))_
- **GIFI** — General Index of Financial Information — CRA standard codes  _(CRA — GIFI — canada.ca)_
- **Annual return (CBCA)** — Within 60 days of anniversary  _(CBCA s.263; Corporations Canada)_
- **Late T2 penalty** — Ordinary 5% of unpaid tax plus 1% per complete month, maximum 12; bind actual balance and applicable penalty branch. [CRA T4012](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/t4012/t2-corporation-income-tax-guide-before-you-start.html).

## Section 1 -- Quick Reference

**Quick Reference**

| Field | Value |
| --- | --- |
| Country | Canada |
| Currency | CAD workpaper convention only; HOLD (unverified) actual reporting currency and any qualifying functional-currency election. [RC4088 scope](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/rc4088/general-index-financial-information-gifi.html) |
| Filing authority | Corporations Canada (federal); Provincial corporate registries (provincial) |
| Primary legislation | Canada Business Corporations Act (CBCA); Provincial acts (OBCA, BCBCA, ABCA, etc.) |
| Supporting legislation | Income Tax Act (R.S.C. 1985, c.1); CPA Canada Handbook |
| CRA filing deadline | 6 months after fiscal year-end (corporate tax return T2) |
| Annual return | CBCA ordinary 60-day anniversary rule covers incorporation, amalgamation or continuance; initial-event year excluded. Provincial rules differ. [registry policy](https://ised-isde.canada.ca/site/corporations-canada/en/business-corporations/policy-annual-filings-canada-business-corporations-act) |
| Digital filing | CRA My Business Account (T2); Corporations Canada Online Filing |

## Section 2 -- Reporting Framework

**Reporting Framework**

| Entity type | Applicable standard | CPA Handbook |
| --- | --- | --- |
| Publicly accountable enterprises (PAE) | HOLD (unverified operative standard): IFRS as issued by IASB (Canadian-adopted) | Part I |
| Private enterprises | HOLD (unverified operative standard): ASPE (Accounting Standards for Private Enterprises) | Part II |
| Not-for-profit organizations | HOLD (unverified operative standard): ASNPO | Part III |
| Pension plans | HOLD (unverified operative standard): Part IV (specific standards) | Part IV |
| Private enterprise choosing IFRS | HOLD (unverified operative standard): IFRS (permitted but not required) | Part I |

### Key difference: ASPE vs IFRS

HOLD (unverified operative standard) every ASPE and IFRS cell below, including the IFRS column. These are research topics, not current requirements.

**Key difference: ASPE vs IFRS**

| Area | ASPE | IFRS |
| --- | --- | --- |
| Financial instruments | HOLD (unverified operative standard): Simplified (cost/amortised cost focus) | HOLD (unverified operative standard): Complex (IFRS 9 — ECL, fair value hierarchy) |
| Leases | HOLD (unverified operative standard): Finance/operating distinction | HOLD (unverified operative standard): IFRS 16 — right-of-use model |
| Revenue | HOLD (unverified operative standard): Risks/rewards transfer model | HOLD (unverified operative standard): IFRS 15 — five-step model |
| Goodwill | HOLD (unverified operative standard): Current goodwill rule/election not verified; do not apply proposed 5/10-year relief as an issued standard | HOLD (unverified operative standard): Not amortised; annual impairment test |
| Employee benefits | HOLD (unverified operative standard): Simplified pension accounting | HOLD (unverified operative standard): IAS 19 — full actuarial measurement |


## Section 3 -- Size Thresholds

HOLD (unverified) the nationwide negative claim about no statutory size thresholds. Framework scope and corporate/securities/funder duties need separate operative authority; one federal provision does not settle the whole country.

**Size Thresholds criteria**

| Criterion | Determining factor |
| --- | --- |
| Public accountability | HOLD (unverified) exact PAE definition, framework trigger and exceptions; a securities filing rule does not certify the Handbook population |
| Private enterprise | HOLD (unverified) framework/election eligibility until operative scope is read |
| Audit requirement | Bind actual incorporating law, securities/funder/contract requirements and any valid waiver; revenue matters in the CNCA branches below. [CNCA review table](https://ised-isde.canada.ca/site/corporations-canada/en/not-profit-corporations/financial-statements-and-review) |

### Audit waiver conditions (CBCA s.163)

- **Audit waiver conditions** — CBCA section 163 applies to a corporation that is not a distributing corporation. All shareholders, including those not otherwise entitled to vote, resolve not to appoint an auditor; validity runs only to the following annual meeting. This provision has no revenue test and does not waive statements or every independent securities/funder obligation. HOLD actual status and resolution. [CBCA 162](https://laws-lois.justice.gc.ca/eng/acts/C-44/section-162.html); [163](https://laws-lois.justice.gc.ca/eng/acts/C-44/section-163.html).

### Provincial variations (examples)

**Provincial variations (examples)**

| Jurisdiction | Audit waiver condition |
| --- | --- |
| CBCA (federal) | Non-distributing; all shareholders including non-voting; only to following annual meeting. [163](https://laws-lois.justice.gc.ca/eng/acts/C-44/section-163.html) |
| OBCA (Ontario) | HOLD (unverified present currency): indexed 148 text indicates non-offering corporation/all shareholders written consent for that year, but current version was not reconciled. [Act](https://www.ontario.ca/laws/statute/90b16) |
| BCBCA (British Columbia) | Section 203 requires all shareholders unanimously, including non-voting, effective for one financial year. Do not claim 203 itself excludes reporting issuers; securities audit duties are separate. [203(2)-(3)](https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/02057_08) |
| ABCA (Alberta) | A non-reporting issuer may use a special resolution under 163, effective only until the following annual meeting; unanimity is not the statutory minimum. [official B-9 section 163](https://kings-printer.alberta.ca/documents/Acts/B09.pdf) |
| Quebec (QBCA) | HOLD (unverified current applicability): official 239 PDF read covers non-reporting issuer/unanimity including non-voting/to next annual meeting, but retrieved consolidation is dated 1 September 2025. [official PDF](https://www.legisquebec.gouv.qc.ca/en/pdf/cs/S-31.1.pdf) |

## Section 4 -- Required Financial Statements

HOLD (unverified) the ASPE/IFRS requirement and comparison cells below pending operative standards. They do not establish compliance. Separately, CBCA 155 requires its statutory statements/comparatives but subsection (2) permits omission of the prior-year statements with an explanation; do not convert that into a universal ASPE rule. [CBCA 155](https://laws-lois.justice.gc.ca/eng/acts/C-44/section-155.html).

**Required Financial Statements**

| Document | ASPE | IFRS |
| --- | --- | --- |
| Balance Sheet / Statement of Financial Position | HOLD (unverified operative standard): Required | HOLD (unverified operative standard): Required |
| Income Statement / Statement of Comprehensive Income | HOLD (unverified operative standard): Required | HOLD (unverified operative standard): Required (+ OCI) |
| Statement of Retained Earnings / Changes in Equity | HOLD (unverified operative standard): Required (retained earnings) | HOLD (unverified operative standard): Required (full equity) |
| Statement of Cash Flows | HOLD (unverified operative standard): Required | HOLD (unverified operative standard): Required |
| Notes to Financial Statements | HOLD (unverified operative standard): Required | HOLD (unverified operative standard): Required (full IFRS disclosure) |
| Comparative information | HOLD (unverified operative standard): Encouraged (not mandatory under ASPE) | HOLD (unverified operative standard): Mandatory (minimum one prior period) |


## Section 5 -- Year-End Adjustments Checklist

**Year-End Adjustments Checklist**

| # | Adjustment | Canada-specific notes |
| --- | --- | --- |
| 1 | Amortization/depreciation | HOLD (unverified operative standard): ASPE 3061; systematic and rational; CCA rates for tax (not accounting) |
| 2 | Provisions | HOLD (unverified operative standard): ASPE 3290; likely, estimable contingencies |
| 3 | Employee benefits | HOLD (unverified operative standard): ASPE 3462; accrued vacation, bonus; pension funding vs expense |
| 4 | Bad debt allowance | HOLD (unverified operative standard): ASPE 3856; incurred loss model (not ECL for ASPE) |
| 5 | Inventory | HOLD (unverified operative standard): ASPE 3031; lower of cost (FIFO/weighted average) and NRV; no LIFO |
| 6 | Income taxes | HOLD (unverified operative standard): ASPE 3465; taxes payable method OR future income taxes method (choice) |
| 7 | Foreign exchange | HOLD (unverified operative standard): ASPE 1651; temporal method; current rate for monetary |
| 8 | Leases | HOLD (unverified operative standard): ASPE 3065; finance/operating classification |
| 9 | Government assistance | HOLD (unverified operative standard): ASPE 3800; cost reduction or income approach |
| 10 | Goodwill impairment | HOLD (unverified operative standard): ASPE 3064 topic retained; current impairment/amortization requirements unverified; proposed 5/10-year relief is not certified current |
| 11 | Related party transactions | HOLD (unverified operative standard): ASPE 3840; measured at exchange amount or carrying value |
| 12 | Scientific Research & Experimental Development (SR&ED) | HOLD (unverified operative standard): Capitalise or expense; ITC recognition |


## Section 6 -- Income Statement Format

Illustrative layout only, not a verified ASPE format or compliance checklist. HOLD (unverified) actual recognition, measurement, framework, totals and presentation requirements; the operative standard was not read.

```
Revenue
Cost of goods sold
  ─── Gross profit ───

Expenses:
  Selling expenses
  General and administrative expenses
  Amortization of capital assets
  Amortization of intangible assets
  ─── Total expenses ───

  ─── Income from operations ───

Other income (expenses):
  Interest income
  Interest expense
  Gain (loss) on disposal of assets
  Foreign exchange gain (loss)
  ─── Total other income (expenses) ───

  ─── Income before income taxes ───

Provision for income taxes (current and future/deferred)
  ─── Net income for the year ───
```

## Section 7 -- Balance Sheet Format

Illustrative layout only. HOLD (unverified) actual classification, measurement, framework-specific headings/disclosures and reporting currency; this layout is not an operative standard.

```
ASSETS

Current assets
  Cash and cash equivalents
  Short-term investments
  Accounts receivable
  Inventories
  Prepaid expenses
  Current portion of notes receivable

Capital assets (Property, plant and equipment)
  Land
  Buildings (net of accumulated amortization)
  Equipment (net of accumulated amortization)
  Leasehold improvements (net)

Intangible assets
  Goodwill
  Patents, trademarks, licences

Other assets
  Long-term investments
  Due from related parties

Total assets

─────────────────────────────────────

LIABILITIES

Current liabilities
  Bank indebtedness
  Accounts payable and accrued liabilities
  Income taxes payable
  Current portion of long-term debt
  Deferred revenue

Long-term liabilities
  Long-term debt
  Obligations under capital leases
  Future income tax liability (or deferred tax)

Total liabilities

─────────────────────────────────────

SHAREHOLDERS' EQUITY
  Share capital
  Contributed surplus
  Retained earnings

Total shareholders' equity

Total liabilities and shareholders' equity
```

## Section 8 -- Notes to Financial Statements

**Notes to Financial Statements**

| # | Disclosure | ASPE | IFRS |
| --- | --- | --- | --- |
| 1 | Significant accounting policies | HOLD (unverified operative standard): Required (Section 1505) | HOLD (unverified operative standard): Required (IAS 1/IAS 8) |
| 2 | Capital assets / PPE | HOLD (unverified operative standard): Required (Section 3061) | HOLD (unverified operative standard): Required (IAS 16) |
| 3 | Financial instruments | HOLD (unverified operative standard): Required (Section 3856) | HOLD (unverified operative standard): Required (IFRS 7 — extensive) |
| 4 | Related party transactions | HOLD (unverified operative standard): Required (Section 3840) | HOLD (unverified operative standard): Required (IAS 24) |
| 5 | Commitments and contingencies | HOLD (unverified operative standard): Required (Section 3290) | HOLD (unverified operative standard): Required (IAS 37) |
| 6 | Income taxes | HOLD (unverified operative standard): Required (Section 3465) | HOLD (unverified operative standard): Required (IAS 12) |
| 7 | Revenue | HOLD (unverified operative standard): Simplified | HOLD (unverified operative standard): Required (IFRS 15 — extensive) |
| 8 | Leases | HOLD (unverified operative standard): Required (Section 3065) | HOLD (unverified operative standard): Required (IFRS 16) |
| 9 | Employee benefits / pensions | HOLD (unverified operative standard): If applicable (Section 3462) | HOLD (unverified operative standard): Required (IAS 19) |
| 10 | Subsequent events | HOLD (unverified operative standard): Required (Section 3820) | HOLD (unverified operative standard): Required (IAS 10) |
| 11 | Going concern | HOLD (unverified operative standard): Required if uncertainty | HOLD (unverified operative standard): Required (IAS 1) |
| 12 | Segment information | HOLD (unverified operative standard): Not required | HOLD (unverified operative standard): Required (IFRS 8 — listed) |


## Section 9 -- Filing Requirements

**Filing Requirements**

| Item | Detail |
| --- | --- |
| Corporate tax return (T2) | Filed with CRA within 6 months of fiscal year-end |
| Financial statements / T2 | GIFI normally substitutes for physical statements; required notes/reports and the insurance-company exception remain relevant. HOLD actual submission package; do not demand complete physical statements from every corporation. [RC4088](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/rc4088/general-index-financial-information-gifi.html) |
| GIFI | Standard classification system for mapping financial statement lines to T2 |
| Annual return (CBCA) | Ordinary 60 days after incorporation/amalgamation/continuance anniversary; initial-event year excluded. [registry policy](https://ised-isde.canada.ca/site/corporations-canada/en/business-corporations/policy-annual-filings-canada-business-corporations-act) |
| Provincial annual return | Ontario ordinary six months after taxation year-end; registry return is separate from T2. Bind actual population. [OBR](https://www.ontario.ca/page/ontario-business-registry); [official instructions](https://forms.mgcs.gov.on.ca/dataset/6c1fdc85-c100-493d-93ca-d86ef2c6a260/resource/a1e78643-e06e-403f-9aec-f26c10b26712/download/on00229e.pdf) |
| NI 51-102 annual financial statements | Non-venture issuer: earlier of 90 days after financial year-end or the foreign filing date; venture issuer: earlier of 120 days or foreign filing. HOLD actual issuer status, scope and exceptions; not every PAE is this population. [4.1-4.2](https://www.bclaws.gov.bc.ca/civix/document/id/lc/statreg/110_2004) |
| Filing format | T2 electronically via CRA My Business Account or certified tax software |
| Late filing penalty — T2 | Ordinary 5% of unpaid tax plus 1% per complete month, maximum 12; actual unpaid balance and repeat/demand/nonresident/large-corporation branches remain separate. [T4012](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/t4012/t2-corporation-income-tax-guide-before-you-start.html) |
| Failure to file penalty | HOLD (unverified) any additional provincial amount/provision and actual conditions; do not automatically double the federal penalty |

### Assurance engagement topics

HOLD (unverified) all operative assurance-standard identifiers, scope and report wording below; the labels retain research topics, including legacy Notice to Reader terminology. An actual engagement requires current operative standards and the applicable law/contract. No universal PAE audit or lender requirement follows from this table.

**Assurance engagement topics**

| Level | Standard | When used |
| --- | --- | --- |
| Audit | CAS (Canadian Auditing Standards) | Required by statute or shareholders; PAEs |
| Review | CSRE 2400 | Lender requirements; shareholder preference |
| Compilation (Notice to Reader) | CSRS 4200 | Owner-managed private companies; no assurance |

## Section 10 -- Audit Requirements

**Audit Requirements**

| Category | Requirement |
| --- | --- |
| Publicly accountable enterprise (PAE) | HOLD (unverified) universal PAE claim and CAS identifier. NI 51-102 4.1 supports its actual reporting-issuer audit population, not every accounting PAE. [NI 51-102](https://www.bclaws.gov.bc.ca/civix/document/id/lc/statreg/110_2004) |
| CBCA corporation | Bind non-distributing status and all-shareholder annual waiver under 162-163 as described above; other duties separate. [163](https://laws-lois.justice.gc.ca/eng/acts/C-44/section-163.html) |
| OBCA corporation | HOLD (unverified current applicability) as stated in the Ontario row above; no present waiver certification |
| Federal not-for-profit (CNCA) | Use the complete inclusive soliciting/non-soliciting decision tree below; bind actual gross revenues, status and resolutions. [registry table](https://ised-isde.canada.ca/site/corporations-canada/en/not-profit-corporations/financial-statements-and-review) |
| Provincial NPO | HOLD (unverified) actual provincial law, population and thresholds; federal CNCA is not a provincial rule |
| Registered charity | CRA recommends professional audit above $250,000 income; it is not a mandatory CRA threshold. Bind independent corporate/funder duties. [CRA statement](https://www.canada.ca/en/revenue-agency/services/charities-giving/charities/operating-a-registered-charity/financial-statements.html) |

### Federal CNCA decision tree

HOLD actual soliciting status, last completed financial year's gross annual revenues, any Director deeming decision and resolutions before selecting a branch. These are public-accountant appointment/engagement rules, not exemptions from financial statements. [179](https://laws-lois.justice.gc.ca/eng/acts/C-7.75/section-179.html); [182](https://laws-lois.justice.gc.ca/eng/acts/C-7.75/section-182.html); [188](https://laws-lois.justice.gc.ca/eng/acts/C-7.75/section-188.html); [189](https://laws-lois.justice.gc.ca/eng/acts/C-7.75/section-189.html); [Regulations 80/84](https://laws-lois.justice.gc.ca/eng/regulations/SOR-2011-223/FullText.html).

| Actual branch | Ordinary appointment/engagement rule |
| --- | --- |
| Soliciting, revenue at most $50,000 | Designated: review if public accountant appointed; members can require audit by ordinary resolution. Appointment may be waived annually by all members entitled to vote. [registry table](https://ised-isde.canada.ca/site/corporations-canada/en/not-profit-corporations/financial-statements-and-review) |
| Soliciting, over $50,000 through $250,000 inclusive | Audit by default; a special resolution can require review, valid only to following annual meeting. [189](https://laws-lois.justice.gc.ca/eng/acts/C-7.75/section-189.html) |
| Soliciting, over $250,000 | Audit under the ordinary branch; no revenue-only review shortcut. [189](https://laws-lois.justice.gc.ca/eng/acts/C-7.75/section-189.html) |
| Non-soliciting, revenue at most $1,000,000 | Designated: review if public accountant appointed; members can require audit by ordinary resolution. Appointment may be waived annually by all members entitled to vote. [registry table](https://ised-isde.canada.ca/site/corporations-canada/en/not-profit-corporations/financial-statements-and-review) |
| Non-soliciting, over $1,000,000 | Audit under the ordinary branch. [189](https://laws-lois.justice.gc.ca/eng/acts/C-7.75/section-189.html); [prescribed amounts](https://laws-lois.justice.gc.ca/eng/regulations/SOR-2011-223/FullText.html) |

Do not import the CBCA all-shareholders/non-voting rule into CNCA member consent. The statutory member voting population and actual resolution matter. A valid no-public-accountant branch does not certify the compilation standard or remove other legal/funder obligations.

### Practical guidelines (lender-driven)

HOLD (unverified market policy): the three original loan bands below have no verified nationwide lender population or legal threshold. Obtain the actual lender covenant/engagement requirements; these bands cannot select an assurance level.

**Practical guidelines (lender-driven)**

| Loan amount | Typical assurance required |
| --- | --- |
| < CAD 250,000 | Compilation (Notice to Reader) often accepted |
| CAD 250,000–1,000,000 | Review engagement typically required |
| > CAD 1,000,000 | Audit typically required |

### Auditor qualification

- **Auditor qualification** — HOLD (unverified) an all-province licensing/CPD statement and actual practitioner eligibility. CBCA 161 and BC 205-206 support their own independence/authorization populations; verify the actual law, authorization, independence and engagement, not a universal title shortcut. [CBCA 161](https://laws-lois.justice.gc.ca/eng/acts/C-44/section-161.html); [BC 205-206](https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/02057_08).

## Illustrative arithmetic checks

The original layouts had no numeric case inputs. These synthetic figures exercise only their arithmetic; they are not statutory thresholds, recognition conclusions, verified standards or client records. HOLD actual classification, recognition, measurement, framework and presentation before use.

```oa-check
name: Illustrative income-statement layout arithmetic only
inputs:
  revenue: 100000
  cost_of_goods_sold: 60000
  operating_expenses: 20000
  other_income: 3000
  other_expense: 1000
  assumed_tax_expense: 4000
steps:
  - gross_profit: revenue - cost_of_goods_sold
  - income_from_operations: gross_profit - operating_expenses
  - net_other_income: other_income - other_expense
  - income_before_tax: income_from_operations + net_other_income
  - illustrative_net_income: income_before_tax - assumed_tax_expense
expected:
  gross_profit: 40000
  income_from_operations: 20000
  net_other_income: 2000
  income_before_tax: 22000
  illustrative_net_income: 18000
```

```oa-check
name: Illustrative balance-sheet layout arithmetic only
inputs:
  current_assets: 50000
  other_assets: 30000
  current_liabilities: 20000
  other_liabilities: 30000
  share_capital: 10000
  assumed_retained_earnings: 20000
steps:
  - total_assets: current_assets + other_assets
  - total_liabilities: current_liabilities + other_liabilities
  - total_equity: share_capital + assumed_retained_earnings
  - liabilities_plus_equity: total_liabilities + total_equity
  - reconciliation_difference: total_assets - liabilities_plus_equity
expected:
  total_assets: 80000
  total_liabilities: 50000
  total_equity: 30000
  liabilities_plus_equity: 80000
  reconciliation_difference: 0
```

## Sources

The unchanged baseline reuses completed 21 November reads. No operative licensed accounting/assurance Handbook text was read. The original standard-setter proposal-status evidence is separately identified and does not certify a current accounting standard. Ontario/Quebec currency and transport gaps remain holds, not findings of repeal or dead law.

| Primary source | Completed scope | Read date |
| --- | --- | --- |
| [CBCA 162](https://laws-lois.justice.gc.ca/eng/acts/C-44/section-162.html) | Auditor appointment, read with section 163; other obligations remain separate | 2026-11-21 |
| [CBCA 163](https://laws-lois.justice.gc.ca/eng/acts/C-44/section-163.html) | Non-distributing corporation; all shareholders including non-voting; valid to the following annual meeting; no revenue condition in this section | 2026-11-21 |
| [CBCA 155](https://laws-lois.justice.gc.ca/eng/acts/C-44/section-155.html) | Statutory statements and comparatives, including the subsection (2) explained prior-year omission; not proof of an ASPE rule | 2026-11-21 |
| [CBCA 161](https://laws-lois.justice.gc.ca/eng/acts/C-44/section-161.html) | Operative independence and disqualification conditions for its statutory population | 2026-11-21 |
| [CNCA 179](https://laws-lois.justice.gc.ca/eng/acts/C-7.75/section-179.html) | Designated-corporation definition: gross revenues and soliciting status | 2026-11-21 |
| [CNCA 182](https://laws-lois.justice.gc.ca/eng/acts/C-7.75/section-182.html) | Appointment waiver by all members entitled to vote; annual duration | 2026-11-21 |
| [CNCA 188](https://laws-lois.justice.gc.ca/eng/acts/C-7.75/section-188.html) | Designated-corporation review by default if accountant appointed; audit by ordinary resolution | 2026-11-21 |
| [CNCA 189](https://laws-lois.justice.gc.ca/eng/acts/C-7.75/section-189.html) | Non-designated audit; soliciting review by special resolution and revenue condition, valid to next annual meeting. Bounded follow-up on 25 November | 2026-11-21; bounded follow-up 2026-11-25 |
| [CNCA Regulations](https://laws-lois.justice.gc.ca/eng/regulations/SOR-2011-223/FullText.html) | Prescribed amounts in sections 80 and 84 read from the official full text | 2026-11-21 |
| [Corporations Canada NPO table](https://ised-isde.canada.ca/site/corporations-canada/en/not-profit-corporations/financial-statements-and-review) | Soliciting and non-soliciting revenue bands with inclusive boundaries. Bounded follow-up on 25 November | 2026-11-21; bounded follow-up 2026-11-25 |
| [CRA charity statements](https://www.canada.ca/en/revenue-agency/services/charities-giving/charities/operating-a-registered-charity/financial-statements.html) | Professional audit recommendation where income exceeds $250,000; not a mandatory CRA threshold. Bounded follow-up on 25 November | 2026-11-21; bounded follow-up 2026-11-25 |
| [Alberta official B-9 PDF](https://kings-printer.alberta.ca/documents/Acts/B09.pdf) | Section 163: non-reporting issuer; special resolution valid to following annual meeting. Bounded 25 November read succeeded after an earlier failed retrieval | 2026-11-21; bounded follow-up 2026-11-25 |
| [BC BCA](https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/02057_08) | Sections 203, 205 and 206; bounded 25 November re-read of 203(2)-(3): all shareholders including non-voting, unanimous resolution, one financial year | 2026-11-21; bounded follow-up 2026-11-25 |
| [NI 51-102](https://www.bclaws.gov.bc.ca/civix/document/id/lc/statreg/110_2004) | Section 4.1 reporting-issuer audit population; 4.2 non-venture 90 days, venture 120 days, earlier foreign filing. Bounded follow-up on 25 November | 2026-11-21; bounded follow-up 2026-11-25 |
| [Ontario BCA](https://www.ontario.ca/laws/statute/90b16) | Indexed section 148 read; present version not confirmed because the current page did not load. HOLD | 2026-11-21 |
| [Quebec BCA PDF](https://www.legisquebec.gouv.qc.ca/en/pdf/cs/S-31.1.pdf) | Section 239 read from the official PDF consolidated to 1 September 2025; current applicability HOLD | 2026-11-21 |
| [CRA T4012](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/t4012/t2-corporation-income-tax-guide-before-you-start.html) | Six-month return deadline, electronic filing, ordinary and repeat penalties; My Business Account expressly listed. Not the payment deadline | 2026-11-21 |
| [CRA RC4088](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/rc4088/general-index-financial-information-gifi.html) | Introduction and appendix: GIFI instead of physical statements, notes/reports, insurer exception and functional currency | 2026-11-21 |
| [CBCA annual policy](https://ised-isde.canada.ca/site/corporations-canada/en/business-corporations/policy-annual-filings-canada-business-corporations-act) | 60 days after incorporation, amalgamation or continuance anniversary; initial event year excluded | 2026-11-21 |
| [Ontario registry](https://www.ontario.ca/page/ontario-business-registry) | Ordinary annual return period tied to taxation year; official instructions also read | 2026-11-21 |
| [Ontario ON00229e](https://forms.mgcs.gov.on.ca/dataset/6c1fdc85-c100-493d-93ca-d86ef2c6a260/resource/a1e78643-e06e-403f-9aec-f26c10b26712/download/on00229e.pdf) | Six months after taxation year-end; provincial return separate from T2 | 2026-11-21 |
| [AcSB project](https://www.frascanada.ca/en/aspe/projects/goodwill-and-acquired-intangibles) | Original standard-setter proposal status and planned final issuance in first half of 2027, including project status and June 2026 decision summary. Bounded follow-up on 25 November; not operative Handbook text | 2026-11-21; bounded follow-up 2026-11-25 |
| [AcSB exposure explanation](https://www.frascanada.ca/en/aspe/projects/goodwill-and-acquired-intangibles/in-brief-acsb-ed-relief-from-recognition-acquired-intangible-assets-amortization-goodwill) | Proposed 1 January 2029 start with early application; not an issued current election | 2026-11-21 |

**Not yet confirmed:** Quick-reference accounting-standard scope (IFRS/ASPE/ASNPO/pension) and choice of financial year are removed from the usable reference table; HOLD actual framework eligibility and fiscal period/year-end choice or change. Also held: every operative ASPE/IFRS/ASNPO/pension/assurance-standard requirement and scope, current goodwill base/election and 40-year citation, national framework/size negatives, Ontario/Quebec present applicability, actual fiscal period/currency/functional-currency eligibility, current provincial licensing/CPD and every case's status/resolutions/filing package or independent funder/securities obligations. Original statement/note/checklist topics are retained as non-usable research holds. Loan bands/layouts are illustrative or unsupported policy, not verified standards. Five statutory/CRA contradiction groups are corrected; no complete fact census or whole-skill verification is claimed.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional before filing or acting upon.
