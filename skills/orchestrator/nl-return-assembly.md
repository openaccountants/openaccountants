---
name: nl-return-assembly
description: Final orchestrator skill that assembles the complete Netherlands filing package for Netherlands-resident self-employed individuals and sole proprietors (ZZP/eenmanszaak). Consumes outputs from all Netherlands content skills (nl-btw-return for BTW-aangifte, nl-income-tax for aangifte inkomstenbelasting Box 1/2/3, nl-zvw for zorgverzekeringswet bijdrage) to produce a single unified reviewer package containing every worksheet, every form, every brief section, all cross-skill reconciliations, and the final action list with payment instructions, filing instructions, and next-year planning. This is the capstone skill that runs last and produces the final deliverable. MUST be loaded alongside all Netherlands content skills listed above. Netherlands full-year residents only. Self-employed individuals and sole proprietors only.
version: 1.0
jurisdiction: NL
tax_year: 2025
last_updated: 2026-09-28
authored_by: OpenAccountants team
review_status: pending_review
trust_label: Written by the OpenAccountants team
category: orchestrator
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Netherlands annual return assembly for a sole proprietor

## Scope and year

Use this method to assemble a reviewable Dutch annual filing package for a full-year Netherlands-resident individual with a sole proprietorship. The annual income-tax calculation is for **2025**, filed in the following year; any **2026** forecast is a separate calculation. VAT returns retain their own periods. Research checked on 28 September 2026.

This Guide connects bookkeeping, business deductions, personal income tax, Zvw and VAT. It does not authorize submission or payment, establish a person's entrepreneur status, or turn an incomplete calculation into a filing-ready return. Part-year residence, foreign social insurance, treaty relief, a deceased taxpayer, substantial-interest transactions, business transfers and disputed employment status need the relevant specialist calculation before the affected part is signed off. Preserve the rest of the work while that issue is resolved. Benefits and allowances (toeslagen) are outside this package; do not present them as calculated or applied for.

## Ask the client first

Start with `nl-freelance-intake`, `netherlands-bookkeeping`, `nl-zzp-deductions`, `nl-deductions`, `nl-income-tax` and one of `nl-vat-return` or `netherlands-vat-return`, where relevant. Inspect each retrieved Guide's year, source dates, scope and actual contents. A matching title does not prove that its calculations are compatible. If a referenced Guide is unavailable or stale, obtain the official year-specific method and record the substitution. Do not invent a missing Guide or assume that an old `nl-btw-return` or `nl-zvw` reference resolved.

Create an input register containing the taxpayer, tax year, residence and insurance periods, fiscal-partner status, business identity, accounting period, source document, amount, currency, conversion method, owner and open question for every material item. Distinguish supplied evidence, confirmed facts, calculations and assumptions. Redact personal identifiers from any public or shared example.

Collect the following before marking the annual package complete:

- Opening and closing trial balances; prior submitted accounts and return; invoices, bank reconciliations, debtors, creditors, accruals, stock, work in progress and financing records.
- The complete asset register, including opening assets, disposal proceeds, private use, depreciation and investment deductions; opening fiscal reserves and carryforward decisions.
- Evidence for entrepreneur classification, hours and any starter claim; partner work; mixed and private expenditure; pension/annuity and disability-insurance records.
- Salary and pension annual statements, benefits, withholding, home and mortgage documents, applicable personal deductions, asset/debt statements and substantial-interest information.
- Every VAT return, correction, ICP/OSS report where applicable, assessment, payment and refund; KOR participation dates; income-tax and Zvw provisional assessments and their payment histories.
- Filing invitations, extensions and actual portal deadlines. The income-tax invitation controls the submission deadline; it is often before 1 May, but the date in the letter governs. ([Filing deadline](https://www.belastingdienst.nl/wps/wcm/connect/nl/belastingaangifte/content/wanneer-moet-ik-aangifte-doen))

## The method, step by step

1. Confirm the year, scope, evidence and compatible dependency methods.
2. Close the books and reconcile commercial accounts to fiscal profit.
3. Apply evidenced business deductions, then assemble the personal tax boxes and credits.
4. Calculate Zvw separately and reconcile the actual VAT periods and payments.
5. Resolve material conflicts, assemble the reviewer package, and distinguish approval from submission.
6. Prepare any later-year forecast separately from the historical return.

### Workflow and unresolved facts

Maintain a status for each schedule: ready for review, evidence missing, calculation conflict, out of scope, reviewed, or submitted with receipt. An unresolved material amount or eligibility condition prevents approval of the affected return. Continue independent schedules, identify the exact missing evidence and show how it affects the conclusion. Do not replace missing opening balances with zero or treat an unexplained difference as harmless because it is small.

When two sources disagree, identify the year, taxpayer category, publication edition and applicable rule before choosing a value. Record the resolution. A number appearing on an official page is not sufficient if its worked example concerns another year. Keep a source register linking every material rule to its applicable period and to the worksheet that uses it.

## Close the books and prove fiscal profit

Prepare commercial accounts, then a separate bridge to fiscal profit. Dutch profit determination applies fiscal valuation and year-allocation rules to the profit-and-loss account and balance sheet. Review depreciation, asset classification, private use, mixed costs, reserves, investment deductions and disinvestment additions individually. ([Profit determination](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/inkomstenbelasting_voor_ondernemers/winst_uit_onderneming))

Reconcile opening balances to the preceding closing records, then document adjustments. Tie cash and bank to statements, reconcile invoices to debtors and creditors, and identify owner transfers and tax payments. Owner drawings are not business expenses and private capital introduced is not trading revenue. ([Owner transfers](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/inkomstenbelasting_voor_ondernemers/privestortingen_en_priveonttrekkingen))

Prepare a movement schedule for each material asset, debt and reserve. As an accounting control, reconcile closing equity less opening equity, plus owner drawings, less capital introduced, to the profit represented by those balances. Align valuation and other equity adjustments before comparing it with the fiscal-profit worksheet. Investigate differences instead of inserting a balancing private withdrawal.

If an opening asset register is absent, reconstruct it from prior accounts and evidence or leave depreciation unresolved. Looking only at purchases made during the current year omits continuing assets. For each cost, show gross invoice, recoverable VAT, remaining business cost or asset basis, private element and tax adjustment. Non-recoverable VAT does not by itself make a private or restricted cost fully deductible.

There are no new FOR additions from **2023** onward. Preserve an existing reserve and evaluate any required release separately; an existing balance does not justify a new annual deduction. ([Oudedagsreserve](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/inkomstenbelasting_voor_ondernemers/fiscale_reserves/oudedagsreserve))

## Business deductions and taxable profit

Carry across the approved fiscal-profit schedule before ondernemersaftrek. Show investment deductions, private-use additions and reserve movements in their proper stages, then each eligible ondernemersaftrek component and any permitted prior-year carryforward. Require evidence for eligibility and maintain loss/carryforward schedules. Avoid treating a deduction unavailable this year as a current-year expense.

For a qualifying entrepreneur below AOW age at the start of **2025**, the ordinary zelfstandigenaftrek is **€2,470**, subject to the hours condition and profit limitation; starter cases and older taxpayers need their applicable rules. ([2025 zelfstandigenaftrek](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/verandering_inkomstenbelasting_vorige_jaren/veranderingen-inkomstenbelasting-2025/ondernemersaftrek-2025/zelfstandigenaftrek-2025)) The MKB exemption for **2025 and 2026** is **12.7%** of profit after ondernemersaftrek. It also reduces an eligible loss. The tax benefit is subject to the applicable rate limitation, so subtracting the exemption from the base is not the entire high-income tax calculation. ([MKB exemption](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/inkomstenbelasting_voor_ondernemers/mkb_winstvrijstelling))

Output both profit before personal business deductions and taxable business profit. They serve different downstream calculations. Record the approved deduction schedule rather than recalculating its figures from a previous Guide's defaults.

## Assemble income tax by box

### Box 1

Combine taxable business profit with the taxpayer's other relevant income and deductions, including the properly calculated home balance. Keep business costs, personal deductions, entrepreneur deductions and tax credits distinct. A private mortgage deduction must not be booked as a sole-trader operating expense. ([Box 1](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/prive/inkomstenbelasting/heffingskortingen_boxen_tarieven/boxen_en_tarieven/box_1/))

For **2025**, a person below AOW age throughout the year and within the ordinary full-year combined tax/national-insurance regime uses **35.82%** up to **€38,441**, **37.48%** above that through **€76,817**, and **49.50%** above that. Use the age-specific and insurance-specific calculation where those assumptions do not hold. Do not apply a single rate to all income. ([Year and age tables](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/prive/inkomstenbelasting/heffingskortingen_boxen_tarieven/boxen_en_tarieven/box_1/))

Import the actual deduction-rate adjustment and eligible tax credits from the checked personal-tax calculation. The **2025** general tax credit depends on aggregate income, while the labour credit uses its own employment-income definition. Do not automatically use taxable business profit as the labour-credit base. Apply the person's age, insurance period and credit limits. Reconcile wage withholding as a prepayment, without deducting it from income or subtracting payroll credits a second time. ([Tax credits](https://www.belastingdienst.nl/wps/wcm/connect/fisin/fisin2025/heffingskortingen))

### Box 2 and Box 3

If substantial-interest income is present, import a separately checked Box 2 calculation and any eligible dividend withholding. An owner of a sole proprietorship can also hold shares privately; do not assume Box 2 is absent from the business's legal form. If none applies, record the factual basis for that conclusion.

For Box 3, reconcile the relevant assets and debts to the applicable valuation date and classification. The **2025** standard method has a **€57,684** exemption per person, **€115,368** for fiscal partners where applicable, and a **36%** tax rate on the calculated taxable return, not on the asset balance. Do not carry an earlier year's exemption into this return. ([2025 calculation](https://www.belastingdienst.nl/wps/wcm/connect/nl/box-3/content/berekening-box-3-inkomen-2025))

The **2025** income-tax return permits the taxpayer to supply actual-return information; the Belastingdienst compares the standard and actual-return calculations and uses the favourable outcome. Collect the complete required income and value-change evidence before treating an actual-return comparison as complete. Earlier-year reporting uses a different route. ([Actual return](https://www.belastingdienst.nl/wps/wcm/connect/nl/box-3/content/werkelijk-rendement-belastingaangifte)) Keep the detailed Box 3 worksheet and assumptions in the reviewer package; do not replace the comparison with interest received alone.

### Fiscal partners

Confirm the partnership period and any full-year election before allocating eligible common items. Reconcile each allocated item's combined total and preserve each person's separate assessment estimate. Wages and business profit cannot be shifted to a partner. Eligible home balances, common Box 3 amounts and other permitted items have their own allocation rules; dividend withholding can be allocated where the rules permit, while wage withholding cannot. ([Fiscal partnership, section 1.5](https://www.belastingdienst.nl/wps/wcm/connect/fisin/fisin2025/fiscaal_partnerschap)) Compare the complete calculations, including credits, rather than choosing an allocation from marginal rates alone.

## Calculate Zvw separately

Build a separate contribution-income schedule. For **2025**, the assessment contribution is **5.26%** and the maximum contribution income is **€75,864**. Include the covered income categories and account for income already subject to employer levy or contribution withholding. An employer's Zvw levy is not an additional amount of the employee's taxable pay. ([2025 Zvw](https://www.belastingdienst.nl/wps/wcm/connect/fisin/fisin2025/inkomensafhankelijke_bijdrage_zorgverzekeringswet))

For ordinary taxable business profit, use the legally defined contribution-income base; the Zvw Act links this to taxable business profit, not the complete Box 1 total. A home deduction or unrelated personal deduction therefore must not automatically reduce the Zvw base. Identify any release of an existing FOR for a qualifying annuity conversion: the Act expressly excludes that qualifying release from contribution income. Check the statutory conditions and reconcile the adjustment with the profit and annuity schedules; do not apply the exclusion to every reserve release. Use the applicable cap and ordering for mixed income, and refer foreign insurance, part-year coverage, exceptional pensions or a negative contribution-income case for the appropriate calculation. ([Zvw Act, contribution income](https://wetten.overheid.nl/BWBR0018450/2025-01-01))

Keep the estimated Zvw assessment and provisional Zvw payments separate from income-tax payments. Show gross assessed liability, existing assessments, amounts paid or refunded and the estimated remaining settlement, with no duplicate deduction for the same prepayment.

## Reconcile VAT without inventing an annual return

Use the business's actual assigned periods and KOR status. A KOR participant ordinarily does not submit normal VAT returns or recover input VAT; KOR is not an annual-return election. Check exceptional or incidental obligations separately. ([KOR](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/btw/hoe_werkt_de_btw/kleineondernemersregeling/kleineondernemersregeling)) Retain all required returns and corrections in the annual review package even though they are different filings from income tax.

Map the VAT schedule to the **2025** official form and its Dutch-established-business instructions. Do not carry legacy KOR reduction or estimation boxes into a modern return. Keep output VAT, reverse-charge VAT, deductible input VAT and adjustments distinct. Hospitality food/drink and private or exempt-use purchases require particular attention to input-tax restrictions. ([2025 VAT notes](https://download.belastingdienst.nl/belastingdienst/docs/toelichting_bij_btw_aangifte_ob0731t53fd.pdf))

As a review control, reconcile ledger revenue to the reported sales bases through an explicit bridge. Explain differences caused by period timing, exempt sales, non-Dutch supplies, asset disposals, private-use adjustments and other classifications. Reverse-charge purchase bases are not turnover from sales. The bridge must reconcile after these identified differences; raw VAT totals and income-tax revenue need not be identical.

Maintain an independent VAT-control-account reconciliation: opening payable/receivable, period liabilities or refunds, annual adjustments and corrections, payments, refunds received, and closing balance. Do not net a VAT refund against an income-tax payment instruction without an actual authorised set-off. ICP periods and reporting status need their own check rather than automatic copying of the VAT filing frequency.

Keep cents in supporting calculations and show the return's prescribed rounding separately. Retain each submitted return and receipt, and distinguish drafted corrections from accepted submissions. The filing/payment dates and payment reference come from the official invitation or portal for that period. Payment timing is based on receipt by the authority. ([2025 VAT notes](https://download.belastingdienst.nl/belastingdienst/docs/toelichting_bij_btw_aangifte_ob0731t53fd.pdf))

## Worked and decision checks

These are assembly controls, not complete personal tax assessments.

**MKB sequence, 2025.** Suppose the approved business schedule has fiscal profit of **€40,000**, the person qualifies for ordinary zelfstandigenaftrek of **€2,470**, and there are no other adjustments or deductions. Profit after that deduction is **€37,530**. At **12.7%**, the exemption is **€4,766.31**, leaving **€32,763.69** taxable business profit before return-entry rounding. This is not final income tax or necessarily the labour-credit base. ([Deduction](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/verandering_inkomstenbelasting_vorige_jaren/veranderingen-inkomstenbelasting-2025/ondernemersaftrek-2025/zelfstandigenaftrek-2025), [MKB](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/inkomstenbelasting_voor_ondernemers/mkb_winstvrijstelling))

**Mixed-income Zvw, 2025.** The annual statement shows **€40,000** already subject to employer Zvw levy and the checked additional contribution-income schedule shows **€50,000**. The remaining cap is **€35,864**. At **5.26%**, the assessment contribution on that remainder is **€1,886.4464** before assessment rounding. Do not charge the full additional income or deduct a home balance from this cap calculation. ([Official mixed-income example](https://www.belastingdienst.nl/wps/wcm/connect/fisin/fisin2025/inkomensafhankelijke_bijdrage_zorgverzekeringswet))

**KOR.** A client supplies proof of full-period KOR participation and no ordinary VAT return obligation, but a foreign purchase appears. Do not invent an annual KOR return or silently ignore the purchase. Resolve whether an incidental obligation arises; keep that item open until the transaction-specific VAT method is checked. ([KOR](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/btw/hoe_werkt_de_btw/kleineondernemersregeling/kleineondernemersregeling), [incidental returns in VAT notes](https://download.belastingdienst.nl/belastingdienst/docs/toelichting_bij_btw_aangifte_ob0731t53fd.pdf))

**Missing opening assets.** Current purchase invoices are complete but the preceding asset register is missing. The current purchases can be classified; annual depreciation and fiscal profit remain unresolved. Request the opening records instead of treating every existing asset as fully depreciated. ([Profit determination](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/inkomstenbelasting_voor_ondernemers/winst_uit_onderneming))

**Year conflict.** A dependency uses **13.31%** MKB for **2025**. Reject that input: the official annual distinction is **13.31%** for **2024**, and **12.7%** for **2025**. Recompute affected downstream schedules before approval. ([MKB](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/inkomstenbelasting_voor_ondernemers/mkb_winstvrijstelling))

**Payment versus filing.** Completing the return does not create a single immediate income-tax/Zvw/VAT payment. Read each actual notice and reconcile prior assessments. A prior-year provisional assessment has a different payment timetable from a current-year instalment arrangement. ([Provisional-assessment payments](https://www.belastingdienst.nl/wps/wcm/connect/nl/voorlopige-aanslag/content/voorlopige-aanslag-aangevraagd-hoe-gaat-het-met-betalen))

## Reviewer package and action list

Deliver an editable master workbook, a reviewer brief and a client action list. Use separate workbook schedules for VAT, each tax box, assets/depreciation, business costs and deductions, Zvw, reconciliations and the later-year forecast. Keep live formulas where practical, check formula errors and independently reconcile calculated totals. If the environment cannot produce a workbook, supply usable editable tables and state the limitation. Deliver files through the available workspace mechanism; do not assume a particular filesystem path or attachment tool. The package should include:

- Scope, year, taxpayer and partner facts; document index; decisions and unresolved matters.
- Accounts, balance movements, fiscal-profit bridge, asset/depreciation schedule, investment and entrepreneur deductions, carryforwards, and private-use adjustments.
- Separate Box 1, Box 2 and Box 3 calculations; partner allocation comparison; deductions, credits, withholding and provisional-assessment reconciliation.
- Separate Zvw schedule; VAT period summaries, correction register, ICP/OSS status where relevant, and VAT control-account reconciliation.
- Official source register with applicable years and retrieval dates; cross-check results; reviewer changes and final approval status.
- Per-return action list: owner, form/portal, period, outstanding evidence, filing deadline, payment deadline, official payment reference source, amount status and submission/payment receipt.

Do not label a spreadsheet as an official filed form. Obtain the taxpayer's authorisation for an actual submission or payment and retain the resulting receipt. Use official notice/portal payment details; never generate a bank account or payment reference from an example. If a deadline has passed, flag the actual position and route the required late filing or correction instead of presenting an old calendar as a future plan.

## Separate 2026 forecast

Start a new forecast with **2026** income, cost, deduction and personal-fact assumptions. Re-evaluate the year-specific rules rather than increasing the **2025** result by a percentage. Reconcile the forecast with the existing provisional income-tax and Zvw assessments and document whether an amendment is recommended. Changes in expected business profit are a reason to review the provisional assessment. ([Provisional-assessment review](https://www.belastingdienst.nl/wps/wcm/connect/nl/voorlopige-aanslag/content/in-welke-situaties-moet-ik-mijn-voorlopige-aanslag-wijzigen))

Record cash already paid separately from tax expense and show the expected remaining reserve. Mark proposals for later years as proposals until effective legislation is checked. The forecast must not alter the completed historical return.

## When to refuse or refer

- Refer migration, foreign insurance, treaty, death, business-transfer and substantial-interest questions to the relevant specialist method before approving the affected calculation.
- Hold an affected return when material facts, opening balances, dependency rules or eligibility remain unsupported; continue independent schedules.
- Do not submit, pay or claim accountant attestation from the existence of this assembled package.

## Self-checks before approval

- Every schedule names its taxpayer, period and applicable rule year; all dependency conflicts are resolved.
- Opening records, asset movements, owner transfers, fiscal profit and the balance sheet reconcile without invented entries.
- VAT eligibility and income-tax deductibility were assessed separately, with a complete VAT-to-revenue bridge.
- Deduction eligibility, MKB order, loss handling, credit bases and partner allocations have evidence.
- Zvw uses its own statutory base and cap, with prior employer-levied income and assessments accounted for.
- Amounts in the summary trace to schedules; rounding differences are explicit; no prepayment is counted twice.
- Every unresolved material issue prevents approval of the affected return; unaffected work is retained.
- Filing, payment and proposed corrections each have an owner and evidence-backed deadline. No submission is claimed without its receipt.

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
