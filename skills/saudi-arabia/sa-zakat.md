---
name: sa-zakat
description: "Saudi Arabia ZATCA-administered business Zakat for 2026 under the current collection regulations: determine liable ownership and calendar, reconcile equity and liabilities, test deductible assets, adjusted profit and minimum/maximum bases, and prepare the annual workpaper. Covers mixed entities, listed-share exceptions, holding investments, provisions, financing and filing boundaries. Preserves the original Saudi LLC, mixed company and sole-trader historical cases with explicit missing-input decisions. Excludes personal religious Zakat and autonomous financial-sector calculations."
jurisdiction: SA
tax_year: 2026
last_updated: "2026-11-16"
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: "tax"
category: "international"
tax_year_notes: "Current regulations read 16 November 2026; preserved 2025 cases are the 2025-2026 filing cycle. Rate depends on verified calendar and day counts."
version: "1.1"
type: "computation"
---

# Saudi Arabia business Zakat: 2026

> **Produced by OpenAccountants (openaccountants.com)**
>
> This skill addresses the fiscal business levy administered by ZATCA. It does not give a religious opinion or calculate personal Zakat on non-commercial wealth. All outputs are preliminary working papers for qualified professional review.

## Scope

Read before any Saudi business-Zakat computation. Use the current **Implementing Regulations for Zakat Collection 1445**, issued by decision **1007** and amended by decision **1248**, rather than the old 2017 working-capital summary. This is the **2026** method. The original 2025 examples below remain the **2025-2026 filing cycle**, with their calendar and missing classification assumptions disclosed. [Current regulation cover and arts. 1-4, 17-28](https://zatca.gov.sa/en/RulesRegulations/Documents/ZAKAT%20COLLECTION.pdf).

**Quick reference:** identify liable ownership, actual fiscal calendar, financial-statement classifications and the adjusted profit first. Reconcile additions, asset deductions, liability matching and the statutory minimum/maximum. The charge is not invariably the larger of “working capital” and profit, and there is no universal rounded Gregorian rate. Do not default an unidentified owner to foreign, choose the larger tax burden in place of the law or manufacture an entitlement from a registration certificate.

Ordinary accounts-basis business calculations are covered. Financial-sector, fund, insurance and other special bases require their own method; estimated-basis taxpayers must first be routed to the relevant assessment chapter. CIT, WHT, VAT, e-invoicing, excise, RETT, customs, oil/hydrocarbon and gas-sector calculations are separate jobs. Load [CIT](sa-corporate-tax.md), [WHT](sa-withholding-tax.md), [VAT](saudi-arabia-vat.md), [e-invoicing](saudi-einvoice.md), [excise](sa-excise-tax.md), [RETT](sa-rett.md), [intake](sa-freelance-intake.md) or [return assembly](sa-return-assembly.md) as appropriate.

## Ask the client first

1. Legal form, Saudi residence, activity/licences, actual start/cessation, sector and whether accounts-basis or estimated-basis treatment applies.
2. Direct/indirect owners, qualifying Saudi/GCC treatment, listed versus founders' shares, year-end percentages and all dated ownership changes.
3. Exact fiscal start/end, Hijri or Gregorian calendar, actual fiscal days and the applicable Hijri-year day count; prior returns, notices, assessments and instalment approvals.
4. Complete financial statements and trial balance, including opening-to-closing equity/profit movements, all current/non-current assets and liabilities, book profit after Zakat/tax, adjusted-profit reconciliation, provisions and deferred tax.
5. Asset, investment, financing, lease, partner-loan, non-trading/trading, prepayment and related-party schedules, with contracts, purpose, classification and supporting certificates.
6. Prior Zakat payments/certificates, unresolved adjustments, holding/group elections, exemption application, objections and private rulings relied on.

No computation without ownership, complete accounts and the calendar. Do not presume a Hijri denominator, choose a Gregorian default or convert an ordinary sole trader into an estimated-basis assessment without establishing its category.

## The method, step by step

### 1. Identify the liable person, share and period

The regulation's “Saudi” definition includes GCC nationals accorded the corresponding treatment. Apply residence under art. 4 and principal-headquarters controls under art. 5. Art. 3 covers qualifying resident Saudi activity, Saudi-owned sole establishments/companies, Saudi shares in resident companies, specified funds/state-owned entities and the stated non-Saudi shares in listed resident companies **except non-Saudi founders' shares**. Art. 6 separates income-tax-covered persons/shares and its oil/hydrocarbon-producer ownership exception. A foreign shareholder in a listed company is therefore not automatically ordinary CIT ownership. [Arts. 1, 3-6](https://zatca.gov.sa/en/RulesRegulations/Documents/ZAKAT%20COLLECTION.pdf).

Record the beginning of collection using the earliest applicable commercial-registration, necessary-licence or capital-deposit event under art. 10, unless documented evidence supports another accepted start. Temporary inactivity does not automatically end Zakat. Permanent cessation requires notification/evidence; do not leave an inactive registration open and assume no obligation. On continuing activity, death, transfer or legal-form change, apply art. 13. Its ownership allocation is based on owners and shares **at the end of the Zakat year**, irrespective of percentage changes during the year: the old automatic time-weighting default is incorrect. [Arts. 10-13](https://zatca.gov.sa/en/RulesRegulations/Documents/ZAKAT%20COLLECTION.pdf).

Public-benefit, charitable, non-profit and waqf status is conditional. Examine art. 7's permitted disbursements, licence, constitutional documents, audited evidence and annual application; a government or charitable name alone is insufficient. Keep the exemption decision, its period and any cancellation trigger. [Arts. 7-8](https://zatca.gov.sa/en/RulesRegulations/Documents/ZAKAT%20COLLECTION.pdf).

### 2. Determine the calendar-dependent rate

| Parameter | 2026 rate or rule and conditions | Official source |
|---|---|---|
| Full Hijri-year rate | 2.5% of the statutory base | Art. 15(1), [regulation](https://zatca.gov.sa/en/RulesRegulations/Documents/ZAKAT%20COLLECTION.pdf) |
| Fiscal year differing from Hijri year | **Derived rate = 2.5% ÷ actual applicable Hijri-year days × actual fiscal-year days**; do not round the rate before computing the charge | Art. 15(2), [regulation](https://zatca.gov.sa/en/RulesRegulations/Documents/ZAKAT%20COLLECTION.pdf) |
| Short commencement period | Period below 354 days is subject to collection under the stated commencement rule | Art. 15(3), [regulation](https://zatca.gov.sa/en/RulesRegulations/Documents/ZAKAT%20COLLECTION.pdf) |
| Short concluding period | Period below 354 days is not subject to collection under the stated conclusion rule; establish actual permanent cessation | Art. 15(4), [regulation](https://zatca.gov.sa/en/RulesRegulations/Documents/ZAKAT%20COLLECTION.pdf) |
| Merger producing a new entity | Apply art. 14's special full-year/two-year treatment for short/long periods and calendar; do not automatically use the ordinary short-period rule | Art. 14, [regulation](https://zatca.gov.sa/en/RulesRegulations/Documents/ZAKAT%20COLLECTION.pdf) |
| Annual public-benefit exemption request | Within 120 days of Zakat year-end, with art. 7 conditions | Art. 7, [regulation](https://zatca.gov.sa/en/RulesRegulations/Documents/ZAKAT%20COLLECTION.pdf) |

The old fixed 2.577% headline and the generated 2.5772% headline are not the exact result of the cited day-count formula. Use the actual period and verified denominator. A day count used in an example below is an **explicit illustrative input**, not a prescribed denominator for every Gregorian year.

### 3. Reconcile financial statements and adjusted profit

Use the standards endorsed by SOCPA and the year-end values in the statement of financial position. Classify current/non-current items under the accounting and statutory rules; for liquidity-format statements apply the regulation's specific realisation/settlement treatment. Fair-value changes follow the stated year-end financial-statement treatment. Do not substitute CIT depreciation/provision rules for Zakat rules. [Arts. 9, 17-20](https://zatca.gov.sa/en/RulesRegulations/Documents/ZAKAT%20COLLECTION.pdf).

Reconcile **adjusted net profit/loss** to **net book profit/loss after Zakat and tax**. The difference, positive or negative, is a distinct addition/adjustment under art. 23(3). Do not add current profit twice when it already forms part of closing equity. Actual, documented, activity-related expenses are tested under arts. 62-65. The accepted-expense provisions include the specified depreciation, bad debts, owners' GOSI-registered remuneration, lawful directors' remuneration, documented wage differences, permitted donations, contractual education benefits, provisions made during the year and paid Zakat/income tax. These are not a licence to deduct any unsupported expense. [Arts. 23(3), 62-65](https://zatca.gov.sa/en/RulesRegulations/Documents/ZAKAT%20COLLECTION.pdf).

For bad debts, establish prior recognition, activity connection, non-related debtor and an authorised write-off supported by the licensed-accountant certificate, subject to art. 65's specific exceptions. Track reversals/recoveries and avoid a double benefit. For provisions, distinguish their income-statement expense from their balance-sheet classification; their treatment in profit and in equity/liability additions is not the same question. [Arts. 24, 62-65](https://zatca.gov.sa/en/RulesRegulations/Documents/ZAKAT%20COLLECTION.pdf).

### 4. Build the additions and liability-matching schedule

Start with equity and equivalents at year-end, then qualifying liabilities within the limits of deductible assets and the profit/loss adjustment. Identify share capital, reserves, retained profits/losses, revaluation/other equity, undistributed declared profits and any owner-loan reclassification. Dividends actually distributed follow art. 37, including the anti-reduction provision; losses carried forward and treasury shares reduce equity under their rules. Do not simply add opening retained earnings and the annual profit without the movements to closing balances. [Arts. 21, 23-24, 28-30, 36-41](https://zatca.gov.sa/en/RulesRegulations/Documents/ZAKAT%20COLLECTION.pdf).

General provisions/equivalents are treated as equity under art. 24; stable obligations to non-owners such as end-of-service/leave provisions are non-current liabilities. Non-current debts, customer advances/instruments, deferred-tax liabilities, contract obligations, lease liabilities and negative derivatives are addressed in art. 29. The name “Murabaha”, “Ijarah” or “Sukuk” alone does not determine the financial-statement or Zakat category. [Arts. 24, 29](https://zatca.gov.sa/en/RulesRegulations/Documents/ZAKAT%20COLLECTION.pdf).

Apply art. 25's matching corrections **before finalising additions**:

1. Where a non-current asset is **not deducted**, compute its proportion of total non-current assets and exclude that proportion of non-current liabilities from additions, subject to the non-deducted-asset cap.
2. Where a **current asset is deducted**, add the corresponding proportion of current liabilities using the deducted-current-asset/total-current-asset ratio, subject to the deducted-asset cap.
3. Total added liabilities may not exceed total deductible assets; check art. 27's minimum-base treatment. Current liabilities also have art. 29(2)'s specific excess-over-current-assets and substantive long-term/repeated-debt rules. They are not all excluded or all included.

The source equations are: **excluded non-current liability = non-deducted non-current asset ÷ total non-current assets × non-current liabilities**; **added current liability = deducted current asset ÷ total current assets × current liabilities**, with the statutory caps. [Arts. 20, 23, 25, 29](https://zatca.gov.sa/en/RulesRegulations/Documents/ZAKAT%20COLLECTION.pdf).

Partner credit loans are not automatically ordinary long-term debt. For the relevant unlisted/partnership case, art. 30 requires audited statements, liability classification, a defined repayment term, market return and absence of full control by a single owner; otherwise treat the loan as equity. Single-owner company/sole-establishment owner loans follow the specific equity rule. Partner debit loans have art. 31's separate conditions and restrictions; **a loan to a non-Zakat-paying debtor is not automatically deductible**. Do not offset owner/debtor/creditor balances to eliminate additions. [Arts. 30-34](https://zatca.gov.sa/en/RulesRegulations/Documents/ZAKAT%20COLLECTION.pdf).

### 5. Test each asset deduction by purpose and statutory category

| Asset or investment | Treatment/conditions | Official source |
|---|---|---|
| Non-trading investment in a domestic establishment | Non-current classification, non-trading purpose and investee registered/subject to ZATCA collection | Arts. 42-43, [regulation](https://zatca.gov.sa/en/RulesRegulations/Documents/ZAKAT%20COLLECTION.pdf) |
| Non-trading foreign establishment investment | Non-current, non-trading and separately calculated/reported Zakat with the prescribed licensed-accountant certificate and minimum-base treatment; no blanket disallowance solely because foreign | Arts. 42, 44, [regulation](https://zatca.gov.sa/en/RulesRegulations/Documents/ZAKAT%20COLLECTION.pdf) |
| Inability to calculate foreign investment's Zakat | Apply art. 46 only with its accepted justifications, data-access and ownership conditions; do not substitute an unsupported net-assets estimate | Art. 46, [regulation](https://zatca.gov.sa/en/RulesRegulations/Documents/ZAKAT%20COLLECTION.pdf) |
| Investment in a non-subject company or a wholly Zakat-owned external company | Apply the separate certified-computation or domestic-investment treatment in art. 47 | Art. 47, [regulation](https://zatca.gov.sa/en/RulesRegulations/Documents/ZAKAT%20COLLECTION.pdf) |
| Funds, bonds/sukuk and financing investments | Follow the specific fund/instrument rules; trading purpose and issuer treatment matter | Arts. 26, 42, 45, 55 and special chapters, [regulation](https://zatca.gov.sa/en/RulesRegulations/Documents/ZAKAT%20COLLECTION.pdf) |
| Fixed assets, capital advances, construction in progress, qualifying non-current contract costs and right-of-use assets | Held for business use, not resale, and within arts. 48-49; net financial-statement value and documentation govern | Arts. 48-49, [regulation](https://zatca.gov.sa/en/RulesRegulations/Documents/ZAKAT%20COLLECTION.pdf) |
| Intangibles | Held for non-trading purposes; no blanket exclusion of software, goodwill or brands | Art. 50, [regulation](https://zatca.gov.sa/en/RulesRegulations/Documents/ZAKAT%20COLLECTION.pdf) |
| Biological assets | Apply non-current/use versus current/sale classification, rather than a general fixed-asset label | Art. 51, [regulation](https://zatca.gov.sa/en/RulesRegulations/Documents/ZAKAT%20COLLECTION.pdf) |
| Inventory/raw materials/spares | Sale inventory and materials in the final product are not ordinary deductions; qualifying non-sale materials/spares and specified current raw materials require art. 52 and current-liability matching | Arts. 25, 52, [regulation](https://zatca.gov.sa/en/RulesRegulations/Documents/ZAKAT%20COLLECTION.pdf) |
| Employee housing and housing debts | Apply ownership/use and the interest-free/cost-only programme conditions; do not deduct every employee loan | Arts. 53-54, [regulation](https://zatca.gov.sa/en/RulesRegulations/Documents/ZAKAT%20COLLECTION.pdf) |
| Statutory deposits | Required deposit for the competent authority with no return, under the stated conditions | Art. 56, [regulation](https://zatca.gov.sa/en/RulesRegulations/Documents/ZAKAT%20COLLECTION.pdf) |
| Deferred-tax asset/liability | Asset is a listed deduction; liability is a listed addition subject to the full matching/base rules | Arts. 26(10), 29(1)(c), [regulation](https://zatca.gov.sa/en/RulesRegulations/Documents/ZAKAT%20COLLECTION.pdf) |
| Generic long-term prepayment | Classify its underlying purpose: the label alone does not establish a deductible capital advance/asset or contract cost | Arts. 26, 48-49, [regulation](https://zatca.gov.sa/en/RulesRegulations/Documents/ZAKAT%20COLLECTION.pdf) |

Keep deduction evidence and liability matching together. A holding company does not receive a blanket investment deduction, and a passive/temporarily inactive company does not automatically cease collection. Financing, lessor/BOT arrangements, debt instruments and investment funds have further special provisions; refer where those computations are material. [Arts. 11, 35, 42-56, special activity chapters](https://zatca.gov.sa/en/RulesRegulations/Documents/ZAKAT%20COLLECTION.pdf).

### 6. Apply the minimum and maximum, then ownership and rate

1. Compute the **raw base** from art. 23 additions less art. 26 deductions after the matching rules.
2. Check art. 27. If raw base is below adjusted net profit, its alternative base is the **lower of adjusted net profit and non-deducted assets plus the adjusted-profit/book-profit difference**. This is why “always use the higher of raw working capital and profit” is wrong. If raw base is negative and there is no adjusted net profit, art. 27(3) gives no accountable base; if raw base is positive with no adjusted profit, art. 27(4) uses the positive result.
3. Check art. 28's maximum: year-end **equity and equivalents plus the adjusted-profit/book-profit difference**, including prescribed reclassifications. Reconcile the bounds and full balance sheet; if the proposed bounds conflict, stop for a complete statutory calculation rather than choosing an unsupported precedence or forcing a negative charge.
4. For an ordinary mixed entity, determine the liable ownership share under the regulation, then apply the verified calendar rate to that Zakat base. Prepare a **separate** CIT profit-based calculation for relevant foreign ownership. Credits/payments and any approved instalments reconcile against each liability separately.

Record raw base, alternate-minimum test, maximum, ownership allocation, rate/day counts and final charge as separate lines. No unexplained balancing amount is allowed. [Arts. 13, 15, 21, 23-29](https://zatca.gov.sa/en/RulesRegulations/Documents/ZAKAT%20COLLECTION.pdf).

### 7. Holding groups, related parties and special sectors

Eligible companies with the same owners and a holding company with fully owned direct/indirect subsidiaries may use the consolidated-accounts/return provisions of art. 16. Check the complete ownership chain, separate information returns and ZATCA approval before ceasing consolidation. Other subsidiaries remain separately accountable; do not import the CIT no-consolidation rule or consolidate any majority-owned group. [Art. 16](https://zatca.gov.sa/en/RulesRegulations/Documents/ZAKAT%20COLLECTION.pdf).

Transfer-pricing instructions apply under art. 22. Keep associated-party financing and investment evidence and the relevant disclosure/valuation analysis. The [CIT skill](sa-corporate-tax.md) distinguishes disclosure, master/local files and CbCR, but its ordinary CIT/mixed small-enterprise test is not a Zakat-only phased threshold. The Zakat-only implementation and exemptions must be checked against the actual applicable TP instrument before claiming relief. [Art. 22](https://zatca.gov.sa/en/RulesRegulations/Documents/ZAKAT%20COLLECTION.pdf); [TP Bylaws arts. 1, 14-19](https://zatca.gov.sa/ar/RulesRegulations/Taxes/Documents/Transfer%20Pricing%202019%20%D8%AA%D8%B9%D9%84%D9%8A%D9%85%D8%A7%D8%AA%20%D8%AA%D8%B3%D8%B9%D9%8A%D8%B1%20%D8%A7%D9%84%D9%85%D8%B9%D8%A7%D9%85%D9%84%D8%A7%D8%AA.pdf).

Banks/financing activities, insurance/reinsurance, funds, BOT/lessor structures and specialised entities have separate chapters and cannot be completed by this ordinary-base shortcut. Regulatory deposits, capital, credit-loss provisions, technical reserves and participant pools require that sector method. Keep the original financing/intangible review discipline, but replace a generic “latest circular” caveat with the actual contract, applicable provision and unresolved fact. [Regulation special-activity provisions; arts. 35, 49-56](https://zatca.gov.sa/en/RulesRegulations/Documents/ZAKAT%20COLLECTION.pdf).

## Boundary and exception table

| Situation | Action |
|---|---|
| Ordinary wholly foreign taxable ownership | Route to CIT after checking listed-share and other ownership exceptions. |
| Ownership changes during continuing activity | Use art. 13 year-end rule, documenting changes; no automatic time weighting. |
| General provision versus stable third-party obligation | Classify as equity-equivalent or liability as prescribed; separately reconcile the expense. |
| Partner loan/foreign investment/intangible | Apply the specific conditions; no default base-increasing or base-reducing shortcut. |
| Sole trader with no qualifying accounts | Determine estimated-basis chapter/assessment before any accounts-basis example. |
| Charity, state entity, waqf or public-benefit claim | Obtain constitutional/licensing evidence, annual application and actual eligibility/decision. |
| Personal savings, gold or religious Zakat al-mal | Outside this fiscal skill; refer for the personal/religious inquiry. |
| Active assessment, objection or private ruling | Preserve notices and obtain the original instrument and specialist review. |

## Worked cases

The original entities and periods below are preserved as the **2025-2026 filing cycle**. All amounts are illustrative inputs, not legal thresholds. For the Gregorian arithmetic scenarios, **365 fiscal days and a verified 354-day Hijri denominator are explicitly assumed inputs**; confirm the actual legal denominator before a real return. The formula retains full precision until the charge is rounded.

### A. Riyadh-based 100%-Saudi-owned LLC: prepayment classification decides the base

Preserve the original **31 December 2025** year-end and figures: capital **SAR 5,000,000**, opening retained earnings **SAR 3,200,000**, statutory reserve **SAR 500,000**, general provision **SAR 200,000**, long-term bank Murabaha **SAR 4,000,000**, adjusted net profit **SAR 1,800,000**, fixed assets **SAR 6,500,000** and non-current prepayment **SAR 300,000**.

To make the illustration executable, assume the movement reconciliation establishes that all profit is retained, no dividends/other movements occurred, the provision is not already counted in equity, book/adjusted profit difference is zero, these are the only non-current assets/liabilities, and the loan/provision/asset conditions are met. Equity/equivalents are then **SAR 10,700,000**. Those are disclosed additional conditions, not facts inferred for an actual client.

**Route A1:** if the prepayment is a qualifying capital-asset advance or other art. 49 deduction, deductible assets are **SAR 6,800,000**, all **SAR 4,000,000** qualifying long-term debt is within that limit, and raw base is **SAR 7,900,000**. Neither the profit minimum nor equity maximum changes it. The exact assumed-day charge is **SAR 203,637.01**, not the old SAR 203,583 obtained by prematurely using 2.577%. [Arts. 15, 23-29, 48-49](https://zatca.gov.sa/en/RulesRegulations/Documents/ZAKAT%20COLLECTION.pdf).

**Route A2:** if the same non-current prepayment is not deductible, do not simply add SAR 300,000 to the base. Art. 25 first excludes **SAR 176,470.59** of non-current debt from additions, derived as 300,000 ÷ 6,800,000 × 4,000,000. The corrected raw base is **SAR 8,023,529.41**. Obtain the prepayment contract and full balance sheet before choosing a route. This is a statutory classification decision, not an election for the cheaper amount.

```oa-check
name: Historical Saudi LLC qualifying versus non-deductible non-current prepayment
inputs:
  capital: 5000000
  retained_earnings_before_current_profit: 3200000
  reserve: 500000
  general_provision: 200000
  retained_current_profit: 1800000
  long_term_debt: 4000000
  fixed_assets: 6500000
  non_current_prepayment: 300000
  fiscal_days: 365
  verified_hijri_days: 354
steps:
  - equity_equivalents: capital + retained_earnings_before_current_profit + reserve + general_provision + retained_current_profit
  - deductible_assets_if_qualifying: fixed_assets + non_current_prepayment
  - base_if_qualifying: equity_equivalents + min(long_term_debt, deductible_assets_if_qualifying) - deductible_assets_if_qualifying
  - charge_if_qualifying: base_if_qualifying * 0.025 * fiscal_days / verified_hijri_days
  - excluded_debt_if_not_qualifying: min(non_current_prepayment, non_current_prepayment / (fixed_assets + non_current_prepayment) * long_term_debt)
  - added_debt_if_not_qualifying: min(long_term_debt - excluded_debt_if_not_qualifying, fixed_assets)
  - base_if_not_qualifying: equity_equivalents + added_debt_if_not_qualifying - fixed_assets
expected:
  equity_equivalents: 10700000
  base_if_qualifying: 7900000
  charge_if_qualifying: 203637.01
  excluded_debt_if_not_qualifying: 176470.59
  base_if_not_qualifying: 8023529.41
```

The ordinary historical annual deadline is **30 April 2026**, derived from art. 102 for this year-end. The old generic 5%-per-month/capped-at-25% Zakat penalty is not used.

### B. Same LLC, 60% Saudi/40% Cayman ownership

Preserve the original **31 December 2025**, same balance-sheet facts and **60% Saudi national/40% Cayman-resident shareholder**. Use route A1 only if its conditions and year-end ownership are established. The Saudi share of the base is **SAR 4,740,000**, and the corresponding profit input is **SAR 1,080,000**; they remain different measures. Under the explicit day-count assumptions the Zakat charge is **SAR 122,182.20**. The old rounded-rate SAR 122,150 is reconciled to the exact formula. [Arts. 13, 15, 21-29](https://zatca.gov.sa/en/RulesRegulations/Documents/ZAKAT%20COLLECTION.pdf).

For the separate [CIT](sa-corporate-tax.md) workpaper, assume its adjustments independently confirm **SAR 720,000** foreign-share taxable profit and the owner skill's ordinary method gives **SAR 144,000**. Combining those two **conditional**, independently derived liabilities gives **SAR 266,182.20**, rather than the original unconditional SAR 266,150. Cayman residence does not establish all tax adjustments or WHT/treaty positions.

```oa-check
name: Historical mixed LLC Zakat allocation and separate CIT handoff
inputs:
  verified_full_zakat_base: 7900000
  saudi_share: 0.60
  independently_computed_foreign_share_cit: 144000
  fiscal_days: 365
  verified_hijri_days: 354
steps:
  - saudi_base: verified_full_zakat_base * saudi_share
  - zakat: saudi_base * 0.025 * fiscal_days / verified_hijri_days
  - combined_conditional_liabilities: zakat + independently_computed_foreign_share_cit
expected:
  saudi_base: 4740000
  zakat: 122182.20
  combined_conditional_liabilities: 266182.20
```

### C. Saudi individual sole trader: the alternate minimum needs an asset input

Preserve the original Saudi individual trading under a commercial registration, **31 December 2025**, adjusted profit **SAR 450,000** and raw base **SAR 380,000**. Establish accounts-basis treatment first. These two figures alone do **not** prove the old SAR 450,000 base: art. 27 also needs non-deducted assets and the book/adjusted-profit difference, plus art. 28's maximum.

For a transparent sensitivity, assume zero profit difference and an equity maximum of at least **SAR 450,000**. If verified non-deducted assets are **SAR 600,000**, the alternate minimum is SAR 450,000 and assumed-day charge **SAR 11,599.58**. If instead those assets are **SAR 400,000**, the alternate minimum/base is SAR 400,000 and charge **SAR 10,310.73**. The missing asset evidence decides the result; do not label either assumption a client fact. The original SAR 11,597 was a rounded-rate result on an incompletely established base. Personal non-commercial savings/gold remain outside this fiscal computation. [Arts. 15, 27-28](https://zatca.gov.sa/en/RulesRegulations/Documents/ZAKAT%20COLLECTION.pdf).

```oa-check
name: Sole trader alternate minimum changes with verified non-deducted assets
inputs:
  adjusted_profit: 450000
  raw_base: 380000
  profit_difference: 0
  non_deducted_assets_scenario_a: 600000
  non_deducted_assets_scenario_b: 400000
  fiscal_days: 365
  verified_hijri_days: 354
steps:
  - alternate_base_a: min(adjusted_profit, non_deducted_assets_scenario_a + profit_difference)
  - alternate_base_b: min(adjusted_profit, non_deducted_assets_scenario_b + profit_difference)
  - charge_a: alternate_base_a * 0.025 * fiscal_days / verified_hijri_days
  - charge_b: alternate_base_b * 0.025 * fiscal_days / verified_hijri_days
expected:
  alternate_base_a: 450000
  alternate_base_b: 400000
  charge_a: 11599.58
  charge_b: 10310.73
```

## When to refuse or refer

Preserve the original refusal identifiers and apply the corrected boundaries:

- **R-SA-Z-1:** ordinary wholly foreign taxable ownership: route to CIT, checking statutory listed-share/other exceptions first.
- **R-SA-Z-2:** oil/hydrocarbon/gas special ownership or concession: specialist regime, not this ordinary Zakat shortcut.
- **R-SA-Z-3:** natural-gas investment tax: separate statutory regime, outside this ordinary Zakat computation.
- **R-SA-Z-4:** financial-sector/financing/insurance special bases: no autonomous sector calculation. Holding/passive structures also require the investment and consolidation tests, rather than a blanket deduction.
- **R-SA-Z-5:** RETT interactions: load the separate property-transaction skill; do not combine its base with Zakat.
- **R-SA-Z-6:** individual personal religious Zakat, including savings, gold, agricultural and livestock Zakat: outside this fiscal method; refer for that separate inquiry.
- **R-SA-Z-7:** group/consolidated Zakat: the art. 16 overview identifies conditions, but a complete consolidated return requires a separate group workpaper and review.
- **R-SA-Z-8:** PE attribution or treaty positions: obtain the actual treaty/facts and route the CIT component to CIT.
- **R-SA-Z-9:** disputed assessments, objections and appeals: preserve notices and obtain licensed dispute review; do not pre-empt the disputed calculation.
- **R-SA-Z-10:** stale regulation or unidentified circular: verify the applicable current text and version before finalising; record the actual financing/intangible provision and unresolved fact.

Also hold for an unverified calendar/denominator, unexplained opening-to-closing equity, unsupported asset deduction, partner loan, treaty/foreign ownership issue or unidentified special instrument. The original instruction to flag financing/intangible uncertainty remains: identify **which arrangement/item, provision and missing evidence** needs review. Do not substitute an unspecified circular or a default base-increasing adjustment for research.

## Filing and payment

1. Confirm ZATCA registration **before the end of the initial fiscal year** and the actual commencement date; verify the account rather than assuming the commercial-registration link completed every tax action. [Arts. 10, 98](https://zatca.gov.sa/en/RulesRegulations/Documents/ZAKAT%20COLLECTION.pdf).
2. Prepare Arabic supporting documents and the accounts-basis approved return in ZATCA's system. Reconcile financial-statement values, additions, matching, deductions, adjusted profit, limits, ownership, day counts and charge. Attach the financial statements and required schedules/certificates for the actual case. The declaration is not a substitute for the workpapers and this skill does not invent current box numbers. [Arts. 98-99, 102](https://zatca.gov.sa/en/RulesRegulations/Documents/ZAKAT%20COLLECTION.pdf).
3. File and pay within **120 days of Zakat year-end**. If the final day is an official holiday, the deadline moves to the **first following working day**. Pay through **SADAD** or another accepted means and retain return/payment acknowledgements. [Art. 102](https://zatca.gov.sa/en/RulesRegulations/Documents/ZAKAT%20COLLECTION.pdf).
4. Retain return-supporting documents in the Kingdom for **at least 10 years** and supply requested evidence under the applicable notice/procedure. Correct a discovered error by requesting amendment; the approved amendment has its own completion period. [Arts. 103-105, 110-111](https://zatca.gov.sa/en/RulesRegulations/Documents/ZAKAT%20COLLECTION.pdf).
5. Reconcile the Zakat certificate and any outstanding balance/assessment to the actual ZATCA account. Do not promise certificate issuance merely from a submitted form or assert a universal certificate prerequisite for CR confirmation, every customs clearance or every property transfer without the relevant service rule.

### Late payment, instalments and assessment boundaries

| Procedure | Current rule/condition | Official source |
|---|---|---|
| Ordinary return/payment | 120 days after year-end; holiday adjustment as above | Art. 102, [regulation](https://zatca.gov.sa/en/RulesRegulations/Documents/ZAKAT%20COLLECTION.pdf) |
| Permanent-cessation notification | Written application within 60 days of cessation, with the stated effect of delayed notice | Art. 11, [regulation](https://zatca.gov.sa/en/RulesRegulations/Documents/ZAKAT%20COLLECTION.pdf) |
| Supporting-document retention | At least 10 years within the Kingdom | Art. 110, [regulation](https://zatca.gov.sa/en/RulesRegulations/Documents/ZAKAT%20COLLECTION.pdf) |
| Correction following approved amendment request | Complete within 30 days; otherwise reapply | Art. 103(2), [regulation](https://zatca.gov.sa/en/RulesRegulations/Documents/ZAKAT%20COLLECTION.pdf) |
| Ordinary assessment/correction | Generally 5 years from statutory return deadline; art. 106 defines extended and unrestricted cases | Art. 106, [regulation](https://zatca.gov.sa/en/RulesRegulations/Documents/ZAKAT%20COLLECTION.pdf) |
| Extended assessment | 10 years for listed late/incomplete/non-compliant/non-payment/non-filing situations; evasion, consent/request and non-registration have their stated special treatment | Art. 106, [regulation](https://zatca.gov.sa/en/RulesRegulations/Documents/ZAKAT%20COLLECTION.pdf) |
| Late-payment collection demands | Successive demands with the stated 30-day periods, then statutory recovery procedures; not an invented generic monthly percentage | Art. 120, [regulation](https://zatca.gov.sa/en/RulesRegulations/Documents/ZAKAT%20COLLECTION.pdf) |

An instalment plan requires the actual request/approval under art. 118, with reasons, liabilities, proposed payments and supporting documents. Breach can cancel the plan under art. 119; do not automatically apply CIT's advance-instalment formula to Zakat. Larger-taxpayer quarterly notices and any individual collection arrangement must be read before use. [Arts. 94, 117-120](https://zatca.gov.sa/en/RulesRegulations/Documents/ZAKAT%20COLLECTION.pdf).

False or incomplete information can produce an assessment, assumptions and statutory recovery; art. 115's advance warning and art. 116's objection-payment/guarantee conditions matter in a dispute. No generic “5% per month capped at 25%” Zakat charge, failure-to-file schedule or blanket tax-amnesty entitlement is established by these provisions. Refer live disputes with the original notice, dates and undisputed amounts rather than inventing the sanction. [Arts. 105-106, 112-120](https://zatca.gov.sa/en/RulesRegulations/Documents/ZAKAT%20COLLECTION.pdf).

## Completion checklist

- Ownership/residence, listed-share exceptions, activity category and commencement/cessation are documented.
- Equity is closing equity, not a double-count of retained/current profit; adjusted profit follows Zakat rules.
- Every liability addition and asset deduction has its specific legal test; matching and owner-loan restrictions are applied.
- Raw, alternative minimum and maximum bases reconcile; actual calendar/day counts determine the unrounded rate.
- Zakat, CIT and WHT are separate workpapers; filing, payment, certificate and notice evidence agree.
- The output states: **“This Zakat computation is preliminary. The stated base, classification, calendar and identified unresolved items require qualified Saudi Zakat review and sign-off before submission.”**

## Sources

| Official text | Actual reading on 2026-11-16 |
|---|---|
| [Implementing Regulations for Zakat Collection 1445, decisions 1007 and 1248](https://zatca.gov.sa/en/RulesRegulations/Documents/ZAKAT%20COLLECTION.pdf) | Read on 2026-11-16. Read cover and arts. 1-29, 30-56, 62-65, 92-106, 110-120 and 126-128 for population, residence, period, rates, ordinary accounts/base, financing/investments, procedure and interpretation boundaries. Special-sector chapters are identified as a handoff, not claimed as a complete sector-method review. |
| [TP Bylaws, official amended scanned consolidation](https://zatca.gov.sa/ar/RulesRegulations/Taxes/Documents/Transfer%20Pricing%202019%20%D8%AA%D8%B9%D9%84%D9%8A%D9%85%D8%A7%D8%AA%20%D8%AA%D8%B3%D8%B9%D9%8A%D8%B1%20%D8%A7%D9%84%D9%85%D8%B9%D8%A7%D9%85%D9%84%D8%A7%D8%AA.pdf) | Read on 2026-11-16. Read relevant definitions and arts. 14-19 for the distinction between disclosure, documentation and CbCR; Zakat-only phase/threshold application remains an explicit boundary rather than borrowing the CIT test. |
| [Income Tax Law](https://zatca.gov.sa/ar/HelpCenter/guidelines/Documents/%D9%86%D8%B8%D8%A7%D9%85%20%D8%B6%D8%B1%D9%8A%D8%A8%D8%A9%20%D8%A7%D9%84%D8%AF%D8%AE%D9%84.pdf) | Read on 2026-11-16. Read arts. 2, 6-7 and ownership-related boundaries for the separate CIT handoff; CIT computations remain owned by the CIT skill. |

**Not yet confirmed:** a universal Hijri denominator or fixed rounded Gregorian rate; current taxpayer-specific portal boxes and certificate conditions for CR, government-contract, customs or RETT services; larger-taxpayer advance-Zakat thresholds/notices; any generic percentage penalty/failure-to-file schedule or Zakat entitlement under a tax-only amnesty; Zakat-only TP implementation phases for a particular year; complete banking/financing/insurance/fund/BOT methods and bespoke instruments; the historical cases' actual prepayment classification, complete equity movement and calendar denominator. The old fixed-rate/higher-of formula, default time-weighting, blanket foreign-investment disallowance, related-debtor deduction and ignored deferred-tax treatment are superseded by the cited specific rules, not retained as usable alternatives.
