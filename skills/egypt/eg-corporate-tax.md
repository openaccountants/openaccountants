---
name: eg-corporate-tax
description: Use this skill whenever asked about Egyptian corporate income tax for tax year 2026 on resident companies, partnerships, branches and permanent establishments of foreign companies, to compute, review, or explain the tax on legal persons' profits, deductions, thin capitalisation, losses, depreciation, dividends, capital gains, advance payments and the annual return. Trigger on phrases like "Egypt corporate tax", "Egypt CIT", "Egyptian company tax", "22.5% Egypt", "thin cap Egypt", "ضريبة أرباح الأشخاص الاعتبارية", "ضريبة دخل الشركات", "إقرار الشركات", "permanent establishment Egypt", or any request to prepare or check an Egyptian company tax return. ALWAYS read this skill before touching any Egypt corporate tax work.
version: 0.5
jurisdiction: EG
tax_year: 2026
last_updated: 2026-11-26
depends_on:
  - income-tax-workflow-base
category: international
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: corporate-tax
type: computation
---

# EG Corporate Tax v0.5

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

For an ordinary company in Egypt's general profit-tax regime, reconcile accounting profit to taxable profit, round the base down to EGP 10 and apply the standard 22.5% rate. Establish the taxpayer's regime and the exceptions below before computing. All example amounts are EGP; the computation is for the company's 2026 financial year. Reply in the user's language, English or Arabic.

## Who this applies to

- Resident legal persons are taxable on worldwide profits; non-resident legal persons on profits through an Egyptian permanent establishment (PE): Law 91/2005 art. 47. Capital companies, partnerships and de facto partnerships are legal persons under art. 48. The State-body and specialist cases below must be resolved before using the ordinary-company computation.
- **State economic activity:** Law 159/2023 art. 1 cancels tax and fee exemptions conferred by laws, regulations or decisions on the specified State entities, including State-owned or State-participated entities and companies, for their economic or investment activities. Those activities are subject to their governing laws. The provision covers administrative-apparatus units, local-administration units, public authorities and bodies with special budgets. It does not make every activity of every State body taxable.
- Art. 1 preserves international agreements in force in Egypt, exemptions for military works and tasks, defence and national security, and exemptions for basic public utility services. Art. 2 preserves the treatment of contracts concluded before commencement until their performance is complete. Under art. 4, commencement was **26 July 2023**. [Official Law 159/2023, arts. 1-4](https://eta.gov.eg/sites/default/files/2024-12/law_no._159_for_2023.pdf).
- **State-body application:** direct or indirect interests, the economic-activity definition, mixed activities and separate accounts, renewals or increased contract volumes under Decree 242/2024, the basic-utility list, the National Service Projects Organisation exclusion in art. 47, and special-law exemptions such as social-insurance-body investments: **Check this point with one of our partner accountants.** Obtain the entity's founding law, exemption instrument, activity and contract before concluding its position; a reported opinion is not a blanket exemption.
- Individuals and sole traders: use `eg-income-tax`. For the elected Law 6/2025 regime, use `eg-sme-tax` to establish eligibility and election. Withholding obligations, payroll, VAT and transfer-pricing documentation are handled in `eg-withholding-tax`, `eg-payroll`, `egypt-vat` and `eg-transfer-pricing`.
- **Special entities and exemptions:** banks, insurers, designated finance companies, the Suez Canal Authority, petroleum bodies and exploration/production companies; cooperatives, public bodies, non-profit or treaty-exempt bodies, private insurance and investment funds, land reclamation and farming exemptions: **Check this point with one of our partner accountants.** Do not assume the standard rate or ordinary provision treatment applies to them.

## Rates, bands and thresholds

| Item | Rule and conditions | Tax year | Official URL |
|---|---|---|---|
| Standard corporate rate | 22.5% of net annual taxable profit; round the tax base down to the nearest EGP 10; specialist entities are referred above | 2026 | https://www.wipo.int/wipolex/ar/legislation/details/20194 (art. 49 first paragraph); https://portal.eta.gov.eg/sites/default/files/2024-03/law_no.96-2015.pdf (operative 2015 replacement) |
| Ordinary thin-capitalisation limit | 3 times average equity under Law 30/2023 art. 5 for tax years 2024-2027. This is a limit on interest deductibility, not permission to deduct every loan cost. Art. 52(1), including the exclusions for banks, insurers and ministerially designated finance companies, must also be applied | 2026 | https://eta.gov.eg/sites/default/files/2024-03/law_no.30-2023.pdf (issuing art. 5); https://eta.gov.eg/sites/default/files/2026-08/law.no_.151.of_.2026.pdf (art. 52(1), issuing art. 6) |
| Buildings, installations, fittings, ships and aircraft | 5% per tax period on purchase, construction, development, renewal or rebuilding cost under art. 25(1) | 2026 | https://eta.gov.eg/sites/default/files/2024-03/law_no.91-2005.pdf |
| Purchased intangible assets, including goodwill | 10% per tax period on purchase, development, improvement or renewal cost under art. 25(2) | 2026 | https://eta.gov.eg/sites/default/files/2024-03/law_no.91-2005.pdf |
| Computers, information systems, software and data-storage equipment | 50% per tax year on the depreciation pool basis, not original cost; arts. 25(3)(a), 26 | 2026 | https://eta.gov.eg/sites/default/files/2024-03/law_no.91-2005.pdf |
| Other depreciable business assets | 25% per tax year on the depreciation pool basis; assets in the separate categories above and non-depreciable assets below are excluded; arts. 25(3)(b), 26 | 2026 | https://eta.gov.eg/sites/default/files/2024-03/law_no.91-2005.pdf |
| Initial production-machinery allowance | 30% of qualifying new or used machinery/equipment cost in the first period of use **on the taxpayer's request**, with regular books and accounts. Reduce the basis before ordinary depreciation. Without a request, use ordinary arts. 25-26 depreciation; art. 27 as replaced by Law 17/2015 art. 6 | 2026 | https://portal.eta.gov.eg/sites/default/files/2026-03/law.no_.17.of_.2015.pdf |
| Donations to qualifying non-government recipients | Up to 10% of annual net profit: registered Egyptian NGOs/foundations, educational institutions and hospitals under government supervision, and Egyptian scientific-research institutions; art. 23(8) | 2026 | https://eta.gov.eg/sites/default/files/2024-03/law_no.91-2005.pdf |
| Ordinary trading-loss carry-forward | Use against following-year profits, carrying any balance annually through the fifth following year; art. 29. Ownership/activity changes, securities losses and completed long-term contracts need the separate referral below | 2026 | https://eta.gov.eg/sites/default/files/2024-03/law_no.91-2005.pdf |

Law 151/2026 re-enacted the ordinary art. 52(1) rule but its repeal provision does not repeal Law 30/2023 art. 5. Use that express transitional schedule for an ordinary 2026 computation. **Infrastructure-project exceptions and allocation of disallowed interest between different-rate loans: Check this point with one of our partner accountants.**

## The base

1. **Reconcile profit.** Art. 51 applies the commercial/industrial profit rules unless Book Three provides a special rule. Begin with accounting profit and identify tax adjustments; keep accounting depreciation separate from tax depreciation.
2. **Establish cost evidence.** Costs must relate to, and be necessary for, the business (art. 22(1)). Art. 22(2), replaced by Law 30/2023, requires real costs supported by electronic invoices from July 2023 and electronic receipts from January 2025. The Minister may extend either deadline by up to one year and exempt particular costs from electronic evidence; costs not customarily documented are excepted. Do not convert this into an unconditional rule that every unsupported payment is deductible or that every paper document is prohibited. Determine the applicable exception before claiming the cost.
3. **Add back ordinary-company provisions** under art. 52(2). Distributions of profit/dividends and shareholder attendance fees, board-membership remuneration/allowances and employees' distributed profit shares are also non-deductible (art. 52(3)-(5)). Specialist bank and insurer provisions are referred above.
4. **Classify penalties and taxes.** Art. 24(2) disallows court-imposed fines, financial penalties and damages for a felony or intentional misdemeanour by the taxpayer or a subordinate. Do not apply a blanket add-back to all contractual compensation: art. 23(9) addresses contractual liability. Egyptian income tax under Law 91 is not deductible (art. 24(3)); business-borne taxes and fees other than that income tax are deductible under art. 23(3), subject to the normal business-cost conditions.
5. **Test interest separately.** Under art. 24(4), disallow loan interest above twice the Central Bank credit/discount rate at the start of the calendar year in which the tax period ends. Art. 24(5) disallows debt interest paid to natural persons who are not taxable or are exempt. Art. 24(6), added by Law 11/2013, disallows financing/investment costs related to legally exempt income. The thin-cap limit does not override these restrictions, business purpose, exempt interest-income offsets under art. 23(1), or arm's-length pricing of related-party finance (`eg-transfer-pricing`).
6. **Compute thin capitalisation.** Executive Regulations arts. 58-59 include loans, advances, bonds, bills and other fixed/variable-return debt finance. Equity is paid-up capital plus reserves and retained profits less carried losses; exclude untaxed revaluation reserves. Losses reduce retained profits/reserves, without reducing equity below paid-up capital. Average equity and average loans each equal opening plus closing balances divided by two. Exclude interest-free loans, loans with non-taxable returns and loans with an interest-payment grace period until that period ends. Compare qualifying average loans with the applicable multiple of average equity. The worked example uses one rate; mixed rates are referred.
7. **Replace book depreciation.** Use the categories above. Under art. 26 and Executive Regulations art. 34, adjust each pool for additions/improvements and disposals/compensation. A negative pool balance is added to taxable profit; a non-negative balance not exceeding EGP 10,000 is deducted in full. Otherwise apply that pool's statutory rate and carry the residual basis forward. Land, art, antiques, jewellery and other inherently non-wasting assets are not depreciated (art. 25(4)). Donated assets credited to reserves: **Check this point with one of our partner accountants.**
8. **Donations.** Art. 23(7) allows donations to government, local units and other public legal persons without the percentage cap; apply art. 23(8)'s cap only to the qualifying non-government recipients listed above. Add back a claimed deduction above the applicable limit.
9. **Losses.** Identify ordinary trading losses by originating year before applying the carry-forward. Loss forfeiture on ownership/activity changes, the listing test and look-forward rule, changes of legal form and revaluation/tax deferral: **Check this point with one of our partner accountants.** Do not assume book-value continuity alone makes a reorganisation tax-neutral.
10. **Long-term manufacturing, fitting-out, construction or related-service contracts spanning tax periods, including percentage-of-completion profit and the completed-contract loss adjustment:** **Check this point with one of our partner accountants.** The ordinary carry-forward row is not a blanket ban on adjusting earlier contract profits.
11. **Bad debts and recoveries; health-insurance solidarity contributions; entertainment, start-up, R&D or training deductions:** **Check this point with one of our partner accountants.** A book write-off or an unsupported enhanced-deduction percentage is not a tax deduction.
12. **Dividends received, participation relief, listed/non-government bond income, listed or unlisted securities gains and losses, fair-value acquisition-cost uplifts, dividend/distribution tax and the listing incentive:** **Check this point with one of our partner accountants.** Law 151/2026 commenced on 29 July 2026; do not apply a single assumed exemption to the whole financial year or use a repealed listed-gains rate. Obtain holding, disposal and distribution dates, ownership and listing information.

## Deadlines and filing

| Step | Rule | Official source |
|---|---|---|
| Annual company return | Before 1 May each year, or within four months after the financial year end; Law 206/2020 art. 31(c) | https://eta.gov.eg/sites/default/files/2024-03/law_no.206-2020.pdf |
| Completeness and exemptions | Complete all prescribed tables/data and attachments within the deadline; an incomplete return is not recognised. A return is required for exempt periods too; art. 31(c) | https://eta.gov.eg/sites/default/files/2024-03/law_no.206-2020.pdf |
| Signatures | Taxpayer/legal representative signs the annual return. An independent preparer also signs or the return is treated as not filed. A registered accountant's signature is required for capital companies, cooperatives, natural persons and partnerships where annual turnover exceeds EGP 2 million; art. 31(d) | https://eta.gov.eg/sites/default/files/2024-03/law_no.206-2020.pdf |
| Electronic filing | Art. 32 requires the available electronic channel, secret password and legally authorised electronic signature. Obtain the correct office/system and current form before submission | https://eta.gov.eg/sites/default/files/2024-03/law_no.206-2020.pdf |
| Payment | Pay the return balance on the day of filing after crediting tax withheld/collected, advance payments and any yield due. Excess withholding first settles prior liabilities; otherwise it is refunded unless the taxpayer requests future use in writing; art. 32 | https://eta.gov.eg/sites/default/files/2024-03/law_no.206-2020.pdf |
| Errors and amendments | An error discovered within the year following the statutory annual deadline requires an amended return. Within 30 days after that deadline, the amendment counts as the original. The right is lost on discovery of evasion or notice of commencement of audit; art. 33 | https://eta.gov.eg/sites/default/files/2024-03/law_no.206-2020.pdf |
| Cessation/transfer | Complete cessation in Egypt: return within 60 days. Transfer of all or part of the business: separate transfer return within 60 days, with the relevant evidence, and include its data in the annual return; art. 31(d) | https://eta.gov.eg/sites/default/files/2024-03/law_no.206-2020.pdf |

Working sequence: reconcile the accounts, tax adjustments and available credits; establish the filing channel and form for the taxpayer's office; obtain signatures; submit and pay by the applicable statutory dates; retain the submitted return, acknowledgement and payment evidence. Current portal screens, return-box numbers, approval of a non-calendar year and the special final-return procedure for public-sector entities: **Check this point with one of our partner accountants.** This computation does not establish a general company-audit obligation.

**Electing/renewing/cancelling advance payments, the withholding substitution, instalment dates and yield:** **Check this point with one of our partner accountants.** Do not assume the ordinary company must pay equal quarterly instalments.

## Penalties and interest

**Late filing, late payment, record failures, evasion, manager liability and offence settlement:** **Check this point with one of our partner accountants.** Obtain the actual due date, filing/payment dates, tax period, notices and offence history. This Guide supplies no penalty or interest calculation; the tax year of a profit computation does not itself fix the rate for a later payment default.

## Cross-border points

**Residence and PE status, treaty relief, PE deemed distributions and head-office charges, foreign-tax credits and foreign losses, free-zone/special-economic-zone treatment:** **Check this point with one of our partner accountants.** Use `eg-cross-border` and `eg-withholding-tax` with the actual treaty, country, income, payment and foreign-tax evidence. Do not treat ordinary corporate tax as the only possible charge on a PE.

## Two worked examples that recompute

**Case 1. Trading company, calendar 2026.** Keep the original inputs: accounting profit 10,000,000; general provision 500,000; book depreciation 800,000; other-assets pool 2,400,000; customer withholding 150,000. Assume an ordinary resident trading company at the standard rate, a qualifying tax pool after all additions/disposals and any initial allowance, a non-deductible general provision, evidenced available withholding, and no other adjustments, losses or reliefs. Tax depreciation = 2,400,000 x 25% = 600,000. Taxable profit = 10,000,000 + 500,000 + 800,000 - 600,000 = 10,700,000. Tax = 2,407,500; balance = **2,257,500**. Statutory annual deadline: before 1 May 2027. Sources: Law 91 arts. 25-26, 51-52; Law 96/2015 art. 49; Law 206 arts. 31-32, linked above.

```oa-check
name: Company profit with provision and depreciation adjustments
inputs:
  profit: 10000000
  provision: 500000
  book_dep: 800000
  pool: 2400000
  withheld: 150000
steps:
  - tax_dep: pool * 0.25
  - taxable: floor((profit + provision + book_dep - tax_dep) / 10) * 10
  - tax: taxable * 0.225
  - payable: tax - withheld
expected:
  tax_dep: 600000.00
  taxable: 10700000.00
  tax: 2407500.00
  payable: 2257500.00
```

**Case 2. Decision: shareholder loan or equity.** Original inputs: average equity 20,000,000, average qualifying loans 80,000,000, one interest rate 15%, gross interest 12,000,000. Assume the ordinary 2026 ratio, no specialist exception, all loans included under arts. 58-59, and all other interest-deduction tests satisfied (including taxable lenders, business purpose, rate ceiling and arm's-length terms). The thin-cap limit is 60,000,000. Interest on excess debt is 3,000,000; its tax effect at 22.5% is 675,000 **relative to deducting the entire original interest expense**. Deductible interest is 9,000,000.

If 20,000,000 of the original debt is instead equity for the whole period, average equity is 40,000,000 and loans 60,000,000. The limit becomes 120,000,000; interest falls to 9,000,000, with no thin-cap disallowance. Deductible interest is again 9,000,000: this substitution does **not** automatically save 675,000 of income tax compared with the original structure at equal profit before financing costs. The equity investor's required return and other financing costs are missing, so the figures alone do not settle the financing choice.

Preserving the original future sensitivity: under Law 30/2023 art. 5's enacted **2028** 2:1 schedule, the original 20,000,000 equity/80,000,000 loans would disallow 6,000,000 of interest. This is a projection under the law read on 26 November 2026, not confirmation of future law. Sources: Law 30/2023 issuing art. 5; Executive Regulations arts. 58-59; Law 96/2015 art. 49.

```oa-check
name: Thin capitalisation and debt to equity decision for 2026
inputs:
  equity: 20000000
  loans: 80000000
  rate: 0.15
  substitute: 20000000
steps:
  - interest: loans * rate
  - limit: equity * 3
  - disallowed: max(loans - limit, 0) * rate
  - extra_tax: disallowed * 0.225
  - deductible: interest - disallowed
  - equity_after: equity + substitute
  - loans_after: loans - substitute
  - limit_after: equity_after * 3
  - interest_after: loans_after * rate
  - disallowed_after: max(loans_after - limit_after, 0) * rate
  - deductible_after: interest_after - disallowed_after
  - tax_deduction_change: (deductible_after - deductible) * 0.225
  - disallowed_2028: max(loans - equity * 2, 0) * rate
expected:
  interest: 12000000.00
  limit: 60000000.00
  disallowed: 3000000.00
  extra_tax: 675000.00
  deductible: 9000000.00
  equity_after: 40000000.00
  loans_after: 60000000.00
  limit_after: 120000000.00
  interest_after: 9000000.00
  disallowed_after: 0.00
  deductible_after: 9000000.00
  tax_deduction_change: 0.00
  disallowed_2028: 6000000.00
```

## Ask the client first

Obtain legal form, residence/PE facts, financial-year dates, turnover and regime/election; State ownership/exemption documents and relevant contracts; a profit reconciliation and asset-pool roll-forward; opening/closing equity and debt with lender status, rate and grace periods; holdings, dividends and disposal dates; losses by year and changes of ownership/activity; customer withholding, advances and foreign taxes. For any referred topic, obtain the specialist conclusion before using an exemption, deduction, rate or deadline affected by it.

Do not help hide profit, invent costs or shift profit to related parties off arm's length. Do not present output as a filed return or a professional sign-off.

## Sources

| Official text and scope read | URL | Read on |
|---|---|---|
| Law 91/2005, Gazette scans: arts. 22-29, 47-49, 51-54; exact Arabic pages recovered; original text checked against the amendments below, not used as a consolidated 2026 text | https://eta.gov.eg/sites/default/files/2024-03/law_no.91-2005.pdf | 2026-11-26 |
| Law 96/2015: art. 1 replacing art. 49 first paragraph; Arabic PDF p. 2 | https://portal.eta.gov.eg/sites/default/files/2024-03/law_no.96-2015.pdf | 2026-11-26 |
| Law 17/2015: issuing arts. 6 and 9, Arabic PDF pp. 27-28; taxpayer-request condition for art. 27 | https://portal.eta.gov.eg/sites/default/files/2026-03/law.no_.17.of_.2015.pdf | 2026-11-26 |
| Law 11/2013: issuing art. 3 adding art. 24(6), Arabic PDF p. 7; exempt-income financing/investment costs | https://portal.eta.gov.eg/sites/default/files/2024-03/law_no.11-2013.pdf | 2026-11-26 |
| Law 30/2023: art. 22(2), art. 52(1), issuing art. 5 transitional schedule; operative 2026 application compared with Law 151 | https://eta.gov.eg/sites/default/files/2024-03/law_no.30-2023.pdf | 2026-11-26 |
| Law 151/2026: whole text, particularly art. 52(1), issuing arts. 6-7; commencement is not assumed to settle all financial-year allocation questions | https://eta.gov.eg/sites/default/files/2026-08/law.no_.151.of_.2026.pdf | 2026-11-26 |
| Law 159/2023: all four articles, Arabic Gazette page; cancellation, exclusions, old contracts and commencement | https://eta.gov.eg/sites/default/files/2024-12/law_no._159_for_2023.pdf | 2026-11-26 |
| Executive Regulations, Decree 991/2005: arts. 58-59, Arabic PDF pp. 27-28 | https://eta.gov.eg/sites/default/files/2024-03/law_no.991-2005.pdf | 2026-11-26 |
| WIPO Lex Arabic statutory consolidation through Law 16/2020: arts. 21-29, 47-55; used to identify older amendments and compare unchanged depreciation/cost rules, not for superseded 2026 rates/exemptions | https://www.wipo.int/wipolex/ar/legislation/details/20194 | 2026-11-26 |
| WIPO Lex Arabic regulations consolidated through Decree 296/2020: art. 34 pool computation, compared with original statutory art. 26 | https://www.wipo.int/wipolex/fr/legislation/details/19951 | 2026-11-26 |
| Law 206/2020: arts. 31-34, Arabic PDF pp. 17-20; recovered saved ETA scan and prior completed return-assembly reading | https://eta.gov.eg/sites/default/files/2024-03/law_no.206-2020.pdf | 2026-11-26 |
| ETA income-tax legislation register: later amendment list and operative source links | https://portal.eta.gov.eg/ar/content/qwanyn-aldrybt-ly-aldkhl | 2026-11-26 |

Not yet confirmed: no unverified rule is usable in the computation. The specifically identified specialist applications above are referrals, not assumed exemptions or deductions. **Check this point with one of our partner accountants.**

> Originally contributed by Ahmed Hassan; rebuilt against the law by the OpenAccountants team.
