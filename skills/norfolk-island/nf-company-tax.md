---
name: nf-company-tax
description: >
  Classify Norfolk Island company income tax residence, ordinary rates,
  base-rate entity eligibility and selected loss and franking rules for
  2026–27. Covers passive income, aggregated turnover, carryforward
  restrictions, the new loss carry-back framework and minimum-tax screening.
  Use for Norfolk corporate tax, company losses, reduced rates, dividends
  or group-threshold questions. Includes statutory citations, fictional
  computations and reviewer checks. Distinguishes company tax, imputation
  rates and multinational thresholds. This source-cited reference preserves
  unresolved special regimes, cross-border, accounting and filing conditions;
  it does not complete a corporate return, authorise a distribution or
  complete the country pack.
jurisdiction: NF
category: international
tax_year: 2026
tax_year_notes: "Primary income period 2026–27; new carry-back amendments apply to income years starting on or after 1 July 2026; source check 17 October 2026"
tier: 2
last_updated: 2026-10-17
version: 0.1
review_status: pending_review
depends_on:
  - workflow-base
  - corporate-income-tax-workflow-base
---

# Norfolk Island: ordinary company tax, losses and franking

Use `nf-tax-system` for Australian tax application and territorial
exceptions. A company is separate from its shareholders and from a sole
trader. This reference concerns selected ordinary company rules; trusts,
partnerships, regulated finance, funds, nonprofits, shipping and other
special regimes require their own rules and applicable refusals.

Load `workflow-base` and `corporate-income-tax-workflow-base`. Preserve
their source and period gates, confirmed profile, refusal messages,
universal outputs and every applicable corporate output and check. This
reference does not complete the corporate country-slot contract. Missing
mandatory sources, fields or runtime capabilities still prevent a
deliverable financial result. Unknown required facts remain Needs Input;
unresolved rules remain on hold. Use fictional cases only for illustration.

## Residence, income and tax profit

Section 6 of the 1936 Assessment Act adopts the 1997 Act's geographical
meaning of Australia, which expressly includes Norfolk Island. Its company
residence definition includes Australian incorporation, or foreign
incorporation with Australian business and either Australian central
management/control or voting power controlled by Australian-resident
shareholders. Establish the actual facts and applicable legal tests;
an NF business address alone does not settle a foreign company's residence
or a treaty position. [ASSESS]; [DICT, section 960-505][DICT]

Under sections 6-5 and 6-10, resident ordinary/statutory income generally
includes all sources; the foreign-resident branches include Australian
source and other statutorily included amounts. Exempt and non-assessable
non-exempt income need separate rules. A foreign company, permanent
establishment, dual residence, source dispute or treaty claim requires
further primary analysis and the workflow's refusal/overlay checks. [CORE]

Reconcile accounting profit to assessable income and allowable deductions
before applying tax rates. The financial statements' revenue, profit and
depreciation are not automatically their tax counterparts. Section 8-1's
general connection and capital/private/exempt/NANE/prohibition limits,
specific deductions and section 8-10's no-double-deduction rule remain
material. Asset deductions, interest restrictions, provisions, foreign
income, capital gains, grants, benefits and tax credits need their own
verified treatment. [CORE, sections 4-10, 4-15, Division 6 and Division 8][CORE]

Confirm the income period, any approved substituted accounting period,
functional and filing currency and conversion rules. Figures below are
stipulated Australian dollars unless explicitly stated in euros. They
do not supply an actual filing calendar or exchange rate.

## Ordinary company rates and base-rate entity tests

For an ordinary company outside the special branches, Rates Act section
23(2) gives **25% for a base rate entity** and **30% otherwise**. This is
not a progressive first-profit-band concession. Section 23 and section
23A contain other company categories; do not apply the ordinary rate to
them without analysis. [RATES]

Section 23AA requires both:

- Base rate entity passive income is **no more than 80% of assessable
  income** for the income year.
- **Aggregated turnover is less than $50 million**, worked out at the end
  of that year. Exactly $50 million fails this limb. [RATES]

Use assessable income for the passive percentage, not taxable profit,
book revenue or cash receipts. Apply the statutory two tests; do not add
an unsupported blanket business-activity condition to section 23AA.

Section 23AB includes specified corporate distributions and franking
credits, non-share dividends, interest, royalties, rent, qualifying-security
gains, net capital gains and partnership/trust amounts referable to passive
income through interposed entities. It excludes the specified non-portfolio
dividend from the distribution limb. Interest has particular financial-
entity, licence, prescribed-entity and equity-return exceptions in
subsections (2)–(3); a label such as business interest does not replace
those conditions. Actual classification needs the instrument and facts.
[RATES]

### Aggregated turnover is a separate measure

Section 328-115 adds relevant annual turnovers of the entity and connected
entities/affiliates, with the specified exclusions for dealings within that
set and amounts outside the connection/affiliation period. Standalone
sales do not settle group turnover. [TURNOVER]

Section 328-120 generally uses ordinary income derived in the ordinary
course of business. It excludes the specified GST amounts and retail-fuel
sales, uses an arm's-length amount for associate dealings, and requires
a reasonable full-year estimate where business was not carried on for
the whole income year. Preserve any applicable regulatory modification.
Do not substitute the income-tax passive-income denominator for turnover.
[TURNOVER]

Section 328-125 has control tests, including voting/income/capital rights,
discretionary trusts, indirect control and exceptions. Its 40% tests are
not a universal 50%-ownership rule; the Commissioner's 40%-to-under-50%
determination is conditional. Section 328-130's affiliate test concerns
directions, wishes or concert in business affairs, and does not make an
ordinary business relationship alone sufficient. Apply the complete
relevant provisions before accepting an actual aggregation. [TURNOVER]

## Tax losses and carryforward restrictions

Section 36-10 starts with deductible amounts excluding earlier tax losses,
subtracts assessable income and then applicable net exempt income. The
remaining amount is a tax loss. Restricted deductions, shipping rules,
excess franking offsets and other special rules can change the result.
A financial loss is not proof of an available tax loss; capital losses
require their own rules. [CORE]

Section 36-17 has separate corporate loss-deduction rules. With no net
exempt income, the entity chooses how much available loss to deduct from
the relevant excess of assessable income over other deductions, subject
to the statutory limits. Net exempt income can require prior utilisation;
multiple losses have an ordering rule. The excess-franking-offset limits
can require a nil choice or prohibit a deduction that creates such an
excess. The choice and later changes have their own return/notice rules.
Section 960-20 prevents reusing losses or net exempt income already used.
[CORE]; [DICT]

Division 165 adds conditions. Section 165-12 ordinarily requires the
relevant persons' **more-than-50% voting, dividend and capital rights**
throughout the ownership-test period, starting with the loss year and
ending with the deduction year. Primary/alternative tracing, special
rules and modifications remain material. Meeting a simple shareholding
percentage at year end is insufficient. [LOSSES]

Section 165-13 supplies a business-continuity alternative with its own
test time and period. Section 165-210's same-business rules retain the
new-business/new-transaction and purpose restrictions. Section 165-211's
similar-business alternative covers the specified items for income years
starting on or after **1 July 2015**, with asset, activity, identity,
development and purpose conditions. It is not an unrestricted election
to preserve losses after any acquisition. [LOSSES]

Section 165-15 can still prevent a deduction after an ownership test is
met where its control/purpose conditions apply, subject to its continuity
alternative. Partial-year, widely-held/group, transferred, debt-forgiveness
and other loss rules need further analysis. This reference establishes
neither a universal carryforward cap/expiry conclusion nor an actual
deductible balance or deferred-tax asset. [LOSSES]; [CORE]

## New loss carry-back framework for 2026–27

Schedule 1 of Tax Reform No. 2 Act 2026 replaces Division 160. Its
schedules commenced **1 October 2026**, and the replacement applies to
assessments for income years starting on or after **1 July 2026**. Do not
use the older 2020–23/$5 billion scheme or the superseded note in the
August assessment compilation as the current framework. [REFORM2]

New section 160-5 requires the current year to start on or after that
date; corporate-tax-entity status throughout the relevant existence period;
a loss year; at least one eligible carry-back year; non-SGE status for
the loss year; the specified return/assessment/no-return-required status
for the current year and five prior years; and a valid choice. A company
meets the corporate-tax-entity definition, but other statutory entity
types are outside this guide's ordinary-company illustrations. [REFORM2];
[DICT, sections 960-115 and 995-1][DICT]

An eligible carry-back year under **160-5(2)** is one of the two most
recent prior income years, with an income-tax liability and the required
corporate status throughout its existence. It is not any earlier profitable
year, and accounting profit or cash instalments are not a substitute for
the statutory liability. [REFORM2]

For each chosen eligible year, section 160-10's component is limited by
the relevant income-tax liability not already included in an earlier
component and by the method statement:

1. Start with the loss amount carried back to that eligible year.
2. Reduce it by that year's applicable net exempt income, without reusing
   net exempt income already utilised.
3. Multiply by the **corporate tax rate for the loss year**, which can
   differ from the gain year's rate. [REFORM2]

The offset is generally capped at the lesser of the component sum and
the franking account balance at the current year's end. Section 160-10(3)
has a specified foreign-resident/non-NZ-franking-company exception to that
balance cap, with conditions for the relevant carry-back years. Do not
apply either the cap or exception indiscriminately. [REFORM2]

Section 160-25 excludes the specified transferred losses, excess-franking-
offset loss component and group-entry liabilities. Section 160-30 has a
disposition/control/financial-benefit/purpose integrity rule; its purpose
need not be the dominant purpose, although merely incidental purpose is
excluded. Continuing a business does not by itself clear that rule.
Actual restructures and questionable positions retain the corporate
workflow's refusals and practitioner gate. [REFORM2]

The choice specifies amounts by prior year in the approved form by
current-year return lodgement or a later day allowed by the Commissioner.
Changes require the approved notice within the applicable limited amendment
period and take effect from the original choice date. This guide supplies
no actual return date, approved form or election submission. [REFORM2,
sections 160-15 and 160-20][REFORM2]

Reconcile utilisation under section 960-20. Do not infer an unused loss
from a cash refund divided by a rate, or assume a capped allocation remains
available for carryforward. A refund can also debit the franking account
under sections 205-25, 205-30 and 205-35, subject to their residency, event
and other conditions. Model choices, utilisation and franking consequences
together before any actual election or distribution. [DICT]; [FRANK]

## Dividends and imputation rates

The **corporate tax rate for imputation purposes** is distinct from the
current income-tax rate. The section 995-1 definition generally uses the
prior year's aggregated turnover, passive income and assessable income
as assumptions for the current year's rate test; it has a specified rule
where the entity did not exist in the prior year. Do not automatically
frank at the current income-tax rate. [DICT]

Sections 202-40 and 202-45 distinguish frankable from unfrankable
distributions, including relevant capital, deemed-dividend and other
exclusions. Sections 202-55–202-65 determine the maximum franking credit
and limit an overstated distribution-statement amount. For a stipulated
frankable cash distribution and established imputation rate `r`, the
maximum-credit formula is equivalent to:

`cash distribution × r / (1 − r)`.

The statutory formulation uses the applicable corporate gross-up rate,
whose formula is `(1 − r) / r`. Neither formula establishes that a
distribution is legally permitted, that credits are available, or that
benchmark, residency and other franking requirements are met. Actual
shareholder taxation, withholding, private-company benefits, capital
returns and distribution mechanics remain held. [FRANK]; [DICT]

## Keep three size tests and minimum taxes separate

The **$50 million** aggregated-turnover test concerns the ordinary reduced
company rate. **SGE status** under section 960-555 concerns, among other
branches, a global parent's annual global income of **$1 billion or more**,
accounting/notional group membership and possible Commissioner
determinations. Sections 960-560–960-575 govern its definitions. A small
standalone Norfolk operation does not prove non-SGE status for carry-back.
[RATES]; [DICT]

The Minimum Tax Act expressly extends to **every external Territory**.
Its ordinary Applicable MNE Group test uses annual revenue of at least
**€750 million in at least two of the four prior Fiscal Years**, with
Rules-based alternatives. The euro threshold is adjusted for a Fiscal Year
other than 12 months; currency translation follows the Rules. Group,
constituent-entity, excluded-entity and location conditions require their
own analysis. These tests differ from both SGE status and the company
rate's aggregated turnover. [MINIMUM, sections 4 and 12–17][MINIMUM]

The Act's IIR/DMT framework applies to Fiscal Years starting on or after
**1 January 2024**; its UTPR charge applies to starts on or after
**1 January 2025**. The current Rules define a **15% Minimum Rate**. A
25% or 30% nominal income-tax rate does not establish the jurisdictional
GloBE effective tax rate or eliminate top-up obligations. Actual IIR,
DMT/UTPR allocation, covered taxes, exclusions, safe harbours, substance
carve-outs and reporting need the complete applicable sources and group
facts. No top-up amount or automatic exclusion is supplied here.
[MINIMUM]; [MINRULES, section 10-5][MINRULES]

## Fictional computations and classification patterns

All relevant eligibility, deduction and special-rule conditions below are
stipulated satisfied unless the row tests that condition. These are
components, not company return balances or recommended choices.

| Stipulated facts | Result or review branch |
|---|---|
| Ordinary company, aggregate turnover $49 million; assessable income $1 million, passive income $800,000 | Exactly 80% passes the passive limb; with the turnover limb satisfied, ordinary rate **25%**. |
| Same facts except passive income $800,001 | Above 80%; ordinary rate **30%**. |
| Same qualifying passive mix but aggregate turnover exactly $50 million | Turnover limb fails; ordinary rate **30%**. |
| Relevant annual turnovers $28 million and $27 million, with $5 million of qualifying excluded dealings | Aggregate **$50 million**; do not grant the reduced rate from either entity's standalone size. |
| Accounting profit $100,000; add back book depreciation $5,000; independently verified tax depreciation $8,000 and excluded income $2,000; no other adjustment | Stipulated taxable profit **$95,000**. Basic tax **$23,750 at 25%**, or **$28,500 at 30%**; actual rate and credits separately established. |
| Eligible deductions $120,000, assessable income $100,000, applicable net exempt income $5,000; no restricted/franking/special component | Section 36-10 tax loss **$15,000**, not $20,000. Availability for use still needs the loss rules. |
| Eligible resident non-SGE company; loss-year rate 25%; stipulated choice $160,000 to the most recent eligible year with $10,000 unused net exempt income and $40,000 eligible liability, plus $140,000 to the other year with nil exempt income and $20,000 eligible liability; franking cap $50,000 | Components: **$37,500** and **$20,000** after the liability cap. Sum **$57,500**, then resident franking cap gives an offset of **$50,000**. No unused-loss or final refund balance is inferred. |
| Established imputation rate 25%, otherwise frankable cash distribution $750 | Maximum franking credit **$250**. All other distribution and franking conditions remain separate. |
| Established imputation rate 30%, otherwise frankable cash distribution $700 | Maximum franking credit **$300**. Do not use this result merely because current company income tax is 30%. |
| Ordinary 12-month GloBE revenue test; prior four years €740m, €760m, €780m and €730m | Two years meet the revenue limb; complete group/entity/Rules analysis is still required. |
| A relevant GloBE Fiscal Year is six months | Its ordinary threshold component is **€375 million**, subject to the Act and Rules; do not substitute that amount for a 12-month year. |
| Ownership history, aggregate-group facts or an approved choice is missing | Needs Input. A profit/loss figure, an NF address or a rate table does not establish entitlement. |

Check rate boundaries, different income/turnover measures, all group facts,
loss utilisation and restrictions, the loss-year rate, eligible prior
liabilities, franking cap/exception and imputation assumptions. Reconcile
credits and payments exactly once under the corporate workflow. Do not
prepare an actual election, distribution, return or payment from these rows.

## Sources, currency and remaining coverage

Checked on 17 October 2026: selected Rates Act compilation 66, 1936 Act
compilation 193 and 1997 Act compilation 267 provisions. The latter's
recorded interval ends on 30 September 2026; the later Tax Reform No. 2
Act's replacement Division 160 and other relevant amendment targets are
applied separately. Its asset amendments also mean the older compilation's
small-asset figures cannot be copied as current without further analysis.

Live records identified the Minimum Tax Act's original version and Rules
compilation 3, effective **2 July 2026**, as latest. Read the cited
provisions, not every page of each acquired volume. Native DOM alternative
text recovered the franking and corporate gross-up formulas omitted from
plain text extraction. No current-year group or taxpayer determination is
implied by acquiring the sources.

Complete profit adjustments, sector regimes, losses/group relief beyond
these selected provisions, asset rules, treaties/PEs, interest/CFC/hybrid
and transfer-pricing rules, withholding, credits, complete minimum-tax
computations, legal distributions, filings/instalments/records, accounting
provisions and remaining country slots remain open. No complete Norfolk
pack, actual return, independent model engagement benchmark or practitioner
sign-off is claimed. No client records or identifiers are needed for these
fictional checks.

[ASSESS]: https://www.legislation.gov.au/C1936A00027/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_1/document_1.html
[CORE]: https://www.legislation.gov.au/C2004A05138/2026-08-27/2026-08-27/text/original/epub/OEBPS/document_1/document_1.html
[RATES]: https://www.legislation.gov.au/C2004A03348/2026-07-01/text
[TURNOVER]: https://www.legislation.gov.au/C2004A05138/2026-08-27/2026-08-27/text/original/epub/OEBPS/document_7/document_7.html
[LOSSES]: https://www.legislation.gov.au/C2004A05138/2026-08-27/2026-08-27/text/original/epub/OEBPS/document_4/document_4.html
[FRANK]: https://www.legislation.gov.au/C2004A05138/2026-08-27/2026-08-27/text/original/epub/OEBPS/document_5/document_5.html
[DICT]: https://www.legislation.gov.au/C2004A05138/2026-08-27/2026-08-27/text/original/epub/OEBPS/document_10/document_10.html
[REFORM2]: https://www.legislation.gov.au/C2026A00071/asmade
[MINIMUM]: https://www.legislation.gov.au/C2024A00132/asmade
[MINRULES]: https://www.legislation.gov.au/F2024L01740/2026-07-02/text

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
