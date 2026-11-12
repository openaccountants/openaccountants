---
name: venezuela-tax-optimization
description: "Compare legal Venezuela tax-planning choices for individuals, sole traders and companies in tax year 2026. Covers personal deductions, income timing, source-separated operating losses, individual versus company computations, related-party finance, municipal-tax deductions, distributions and foreign tax credits. Retains the planning questions for IVA, payroll contributions, LOCTI, special economic zones, cryptocurrency and sector incentives, with explicit limits where current primary evidence is unavailable. Use for reducir impuestos, planificación fiscal, desgravamen único o detallado, pérdidas fiscales, subcapitalización, dividendos, ISAE and Venezuela tax optimization. Produces documented alternatives, recomputing working papers, research gaps and a professional-review brief before a tax position is taken."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/venezuela-tax-optimization"
  jurisdiction: "VE"
  tax_year: "2026"
  last_updated: "2026-11-11"
---

# Venezuela tax optimization (2026) v0.2

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

**Answer layer.** Compare documented alternatives using the taxpayer's actual legal classification, source, timing and complete tax base. For a resident individual, compare eligible itemized personal deductions with the mutually exclusive 774 U.T. allowance; calculate both complete liabilities, including applicable personal rebates. For business losses, preserve source and vintage: the next three tax periods qualify, with a 25% limit on each period's matching-source enrichment. Related-party interest capacity depends on independent debt as well as related debt. Distributions are not automatically taxed a second time in full. [LISLR arts. 4, 50, 52, 55, 57-59, 64-71, 116](https://contraloriadebarquisimeto.gob.ve/images/baselegal/LOAFSP.pdf).

**Required inputs before a recommendation:** fiscal year and RIF; residence/domicile, legal form and activities; actual applicable UT evidence; receipts and invoice dates; source-separated tax reconciliation; personal expenses and dependants; loss vintages; month-end related and independent debt; opening/closing equity; distribution history; foreign tax and treaty evidence; and current taxpayer-specific calendars. Missing evidence is a missing input, not permission to assume a historical bolívar amount.

This Guide produces a planning brief and working papers, not a completed return. The primary gazettes read on 11 November 2026 are identified below with their actual enactment dates. The current UT currency value, administrative filing instructions and several incentives/parafiscal measures were not established from accessible primary text. Those topics remain explicitly tracked in Sources. This version is tier 2 and is not professionally approved.

## Who this applies to

Use this decision workflow for Venezuelan-resident/domiciled individuals and ordinary companies, and alongside the relevant income-tax Guide for non-residents, permanent establishments or fixed bases. Residents/domiciled persons generally pay on income of any origin; non-residents without a PE/fixed base are subject on Venezuelan-source enrichment; a foreign person with a PE/fixed base reports domestic and foreign income attributable to it. The place of a bank account or currency does not determine income source. Identify the causes and use of the activity under art. 6. [LISLR arts. 1, 6](https://contraloriadebarquisimeto.gob.ve/images/baselegal/LOAFSP.pdf#page=4).

A sole trader and a company are different taxpayers. Apply art. 8/50 to the individual and art. 9/52 to a company limited by shares or assimilated entity. Partnerships, communities and consortia within art. 10 generally compute at entity level but income tax is collected from members, subject to that article's mining-royalty exception and formal/joint-liability rules. Do not call every small company transparent. [LISLR arts. 7-10](https://contraloriadebarquisimeto.gob.ve/images/baselegal/LOAFSP.pdf#page=6).

### Scope statement and handoffs

The scope includes the old Guide's ten planning levers: personal deductions; losses; legal form; special economic zones; treaty/distribution relief; finance; LOCTI; municipal taxes; IVA; and employment contributions. It also retains cryptocurrency, anti-drug/sports/high-net-wealth contributions, sector taxes, ordinary/special filing calendars, record retention, reusable prompts and working-paper controls. A topic without verified current law is recorded as unconfirmed, never silently treated as inapplicable.

Load [individual income tax](venezuela-income-tax.md), [ordinary company tax](venezuela-corporate-tax.md), [IVA](venezuela-iva.md), [social contributions](venezuela-social-contributions.md) and [payroll](venezuela-payroll.md) for their respective computations, checking each file's date and explicit gaps. Detailed transfer-pricing documentation, treaty articles and specialist calculations require the relevant dedicated Guide and underlying law. This file supplies the comparison method and statutory ISLR decisions; it does not assert complete 2026 country coverage.

**AUDIT FLASH POINT**: artificial forms are not a planning safe harbour. COT art. 16 permits the administration, through its prescribed examination/determination procedure, to disregard companies, contracts or other legal forms manifestly inappropriate to the economic reality pursued when they reduce tax obligations. Document the commercial transaction and beneficial parties, not just the tax saving. A purportedly conservative high-tax default can also be wrong: compute the rule that actually applies or stop the affected calculation. [COT art. 16](https://www.cmchacao.gob.ve/wp-content/uploads/2025/08/Decreto-con-Rango-Valor-y-Fuerza-de-Ley-que-Reforma-la-Ley-que-Establece-el-Impuesto-al-Valor-Agregado.pdf#page=4).

## Rates, bands and thresholds

All amounts below are statutory tax units (U.T.), unless another unit is expressly named. Apply the annual UT in force at fiscal close; for a nonannual tax period COT art. 3 uses the UT in force at the beginning. This does not authorize using UT for municipal rates or employment benefits. No current bolívar conversion is supplied. [COT art. 3, third paragraph](https://www.cmchacao.gob.ve/wp-content/uploads/2025/08/Decreto-con-Rango-Valor-y-Fuerza-de-Ley-que-Reforma-la-Ley-que-Establece-el-Impuesto-al-Valor-Agregado.pdf#page=2).

| Item | Amount and conditions | Official source |
|---|---|---|
| Resident individual Tarifa 1 | 6% on first 1,000 U.T.; individual/asimilated art. 8 taxpayer outside a separate regime | LISLR arts. 8, 50, https://contraloriadebarquisimeto.gob.ve/images/baselegal/LOAFSP.pdf#page=13 |
| Individual second band | 9% on portion over 1,000 through 1,500 U.T. | LISLR art. 50, https://contraloriadebarquisimeto.gob.ve/images/baselegal/LOAFSP.pdf#page=13 |
| Individual third band | 12% on portion over 1,500 through 2,000 U.T. | LISLR art. 50, https://contraloriadebarquisimeto.gob.ve/images/baselegal/LOAFSP.pdf#page=13 |
| Individual fourth band | 16% on portion over 2,000 through 2,500 U.T. | LISLR art. 50, https://contraloriadebarquisimeto.gob.ve/images/baselegal/LOAFSP.pdf#page=13 |
| Individual fifth band | 20% on portion over 2,500 through 3,000 U.T. | LISLR art. 50, https://contraloriadebarquisimeto.gob.ve/images/baselegal/LOAFSP.pdf#page=13 |
| Individual sixth band | 24% on portion over 3,000 through 4,000 U.T. | LISLR art. 50, https://contraloriadebarquisimeto.gob.ve/images/baselegal/LOAFSP.pdf#page=13 |
| Individual seventh band | 29% on portion over 4,000 through 6,000 U.T. | LISLR art. 50, https://contraloriadebarquisimeto.gob.ve/images/baselegal/LOAFSP.pdf#page=13 |
| Individual top band | 34% on portion over 6,000 U.T.; non-resident individuals have the separate 34% rule on their statutory enrichment, not these resident bands | LISLR art. 50, https://contraloriadebarquisimeto.gob.ve/images/baselegal/LOAFSP.pdf#page=13 |
| Ordinary company Tarifa 2 | 15% first 2,000 U.T.; 22% portion over 2,000 through 3,000; 34% excess over 3,000; art. 9 taxpayers outside special regimes | LISLR arts. 9, 52, https://contraloriadebarquisimeto.gob.ve/images/baselegal/LOAFSP.pdf#page=13 |
| Domestic financial/insurance activity | 40% proportional tax on specified banking, financial, insurance/reinsurance net enrichment of domiciled legal persons/entities; not ordinary Tarifa 2 | LISLR art. 52, first paragraph, https://contraloriadebarquisimeto.gob.ve/images/baselegal/LOAFSP.pdf#page=13 |
| Sector Tarifa 3 | The statutory text sets 50% for art. 11 activities and 60% for art. 12 mining royalties/participations; taxpayer, activity and source determine applicability. A complete current hydrocarbons computation requires the unconfirmed sector measures | LISLR arts. 11-12, 53, https://contraloriadebarquisimeto.gob.ve/images/baselegal/LOAFSP.pdf#page=13 |
| Standard personal allowance | 774 U.T. for resident individuals opting out of art. 57 itemized deductions; do not combine the methods | LISLR art. 58, https://contraloriadebarquisimeto.gob.ve/images/baselegal/LOAFSP.pdf#page=14 |
| Principal-home loan interest | Actual qualifying payments, capped at 1,000 U.T. for the tax year; art. 57 conditions and no double deduction apply | LISLR art. 57(4), https://contraloriadebarquisimeto.gob.ve/images/baselegal/LOAFSP.pdf#page=14 |
| Permanent-home rent | Actual qualifying payments, capped at 800 U.T. for the tax year; establish the actual housing facts under art. 57 | LISLR art. 57(4), https://contraloriadebarquisimeto.gob.ve/images/baselegal/LOAFSP.pdf#page=14 |
| Personal tax rebate | 10 U.T. for resident individual; additional 10 U.T. for qualifying spouse and each eligible dependant, with separate-return/shared-support conditions | LISLR arts. 59-60, https://contraloriadebarquisimeto.gob.ve/images/baselegal/LOAFSP.pdf#page=14 |
| Operating-loss use | Next three periods after the loss period; no more than 25% of matching-source enrichment in each; keep territorial and foreign loss pools separate | LISLR arts. 4, 55, https://contraloriadebarquisimeto.gob.ve/images/baselegal/LOAFSP.pdf#page=14 |
| Ordinary taxable dividend | 34% on the dividend portion taxable under arts. 64-68; full withholding on payment or book credit. Sector rates and stock dividends have separate rules | LISLR arts. 64-73, https://contraloriadebarquisimeto.gob.ve/images/baselegal/LOAFSP.pdf#page=15 |
| Resident individual filing trigger | Net annual global enrichment over 1,000 U.T. OR gross income over 1,500 U.T.; exclusively primary agricultural/livestock/fishing/fish-farming activity uses gross income over 2,625 U.T. | LISLR art. 77, https://contraloriadebarquisimeto.gob.ve/images/baselegal/LOAFSP.pdf#page=16 |
| Entity annual declaration | Companies, assimilated entities and the other identified art. 77 entities declare enrichment/loss regardless of amount; non-resident individuals separately declare Venezuelan enrichment/loss regardless of amount | LISLR arts. 77, 79, https://contraloriadebarquisimeto.gob.ve/images/baselegal/LOAFSP.pdf#page=16 |
| Estimated declaration enabling threshold | Prior-year net enrichment over 1,500 U.T. permits prescribed category-based estimated-return requirements; it is not a complete current calendar or universal liability rule | LISLR art. 80, https://contraloriadebarquisimeto.gob.ve/images/baselegal/LOAFSP.pdf#page=17 |

For a mechanical cross-check only, the marginal Tarifa 1 bands produce fixed subtraction amounts of **0, 30, 75, 155, 255, 375, 575 and 875 U.T.** respectively; Tarifa 2 produces **0, 140 and 500 U.T.** These are arithmetic derived from the bands, not additional statutory deductions. For example, at the start of the second company band, tax is 300 U.T., so `0.22 × 2,000 - 300 = 140`. Do not subtract both a fixed subtraction and the lower-band tax. [Derived from LISLR arts. 50, 52](https://contraloriadebarquisimeto.gob.ve/images/baselegal/LOAFSP.pdf#page=13).

## The base

### What this file is and the method, step by step

1. **Fix the facts and baseline.** Establish legal form, domicile/residence, PE, activities, special-taxpayer status and fiscal year. Reconcile territorial and foreign receipts, costs and deductions. Compute the current-law baseline before considering a change; identify all other taxes, compliance costs and cash-flow effects separately. [LISLR arts. 1, 4, 6-10, 16](https://contraloriadebarquisimeto.gob.ve/images/baselegal/LOAFSP.pdf#page=4).
2. **Apply actual income and expense timing.** Income is generally available when the producing transaction occurs. Art. 5 separately provides proportional recovery for credit assignments/discount operations recoverable over several annualities; credit income of its enumerated lenders/entities and rental/subrental income is available on accrual. Employment income and fortuitous gains become available when paid. An unpaid ordinary business invoice is not therefore automatically deferred. Under art. 32, deductions for transaction-realization income generally follow expenditure accrued in the tax year, subject to its express art. 27 exceptions; deductions for income available on payment generally require expenditure actually paid that year, without losing the applicable depreciation/casualty-loss deductions. A planned payment or invoice delay alone does not alter these operative conditions. [LISLR arts. 5, 27, 32](https://contraloriadebarquisimeto.gob.ve/images/baselegal/LOAFSP.pdf#page=5).
3. **Test each deduction before valuing it.** Ordinary business expenses must be non-cost, normal and necessary domestic expenditure to produce enrichment, subject to the law's exceptions. Maintain seller invoices and required RIF; do not deduct capital expenditure immediately simply to absorb a loss. Keep foreign expenses, exempt-income expenses and common costs properly allocated. For employment/remuneration costs comply with employer obligations; interest must finance income production and pass the finance restrictions below. [LISLR arts. 15, 23, 27, 89](https://contraloriadebarquisimeto.gob.ve/images/baselegal/LOAFSP.pdf#page=8).
4. **Apply each lever below to a genuine alternative.** Calculate the entire alternative liability with marginal bands, correct source and vintage. Show both tax and cash after compliance/financing costs; a deduction reduces the base while a credit reduces tax. Do not multiply an expense by the top rate if the alternative crosses a band. [LISLR arts. 2, 4, 50, 52, 55-59](https://contraloriadebarquisimeto.gob.ve/images/baselegal/LOAFSP.pdf#page=4).
5. **Reconcile credits and delivery.** Match actual withholding/advances against annual tax under art. 83; an excess under art. 56 can be requested against later declarations, without prejudice to refund rights. Do not count the same tax as expense and credit. Deliver the comparison, evidence, deadline list and unresolved items for professional sign-off. [LISLR arts. 56, 83-85, 88](https://contraloriadebarquisimeto.gob.ve/images/baselegal/LOAFSP.pdf#page=14).

### Lever 1: standard versus itemized personal deductions

Art. 57 applies to resident individuals. First construct the **eligible** itemized total; then compare it with art. 58's 774 U.T. alternative. The itemized categories have different territorial conditions, so a blanket rule excluding every foreign payee is inaccurate. [LISLR arts. 57-58](https://contraloriadebarquisimeto.gob.ve/images/baselegal/LOAFSP.pdf#page=14).

| Eligible item | Condition and documentation | Official source |
|---|---|---|
| Education | Payments to educational institutes in Venezuela for taxpayer/descendants not older than 25; the age limit does not apply to special education. Art. 57(1) supplies no separate monetary cap | LISLR art. 57(1), https://contraloriadebarquisimeto.gob.ve/images/baselegal/LOAFSP.pdf#page=14 |
| Insurance | Premiums paid to companies domiciled in Venezuela for hospitalization, surgery and maternity; a stand-alone life policy is not listed in art. 57(2) | LISLR art. 57(2), https://contraloriadebarquisimeto.gob.ve/images/baselegal/LOAFSP.pdf#page=14 |
| Medical, dental, hospitalization | Services provided in Venezuela to taxpayer and the qualifying persons in art. 59; art. 57(3) supplies no separate monetary cap | LISLR art. 57(3), https://contraloriadebarquisimeto.gob.ve/images/baselegal/LOAFSP.pdf#page=14 |
| Housing | Actual principal-home acquisition-loan interest or permanent-home rent within the respective cap; establish the transaction, payment and dwelling rather than assuming all mortgage principal qualifies | LISLR art. 57(4), https://contraloriadebarquisimeto.gob.ve/images/baselegal/LOAFSP.pdf#page=14 |
| Common gates | Paid within tax year, supporting receipts with recipient RIF, no cost/expense double count, no reimbursable employer/contractor/insurer amounts; divide shared education/insurance expenditure between contributors | LISLR art. 57, first/second paragraphs, https://contraloriadebarquisimeto.gob.ve/images/baselegal/LOAFSP.pdf#page=14 |
| Official-service exception | The listed diplomatic/consular and other public/state representatives' expenses abroad during official duties are treated as domestic for these deductions | LISLR art. 57, third paragraph, https://contraloriadebarquisimeto.gob.ve/images/baselegal/LOAFSP.pdf#page=14 |

The itemized method is not automatically better merely because a client has many receipts. Exclude ineligible life insurance, reimbursement claims, business-deducted amounts and unsupported payments, apply housing limits, then compare both final taxes. A deduction cannot create a personal rebate or a loss entitlement that the law does not supply. Apply art. 59's personal/family rebates separately. Education's descendant age condition in art. 57 is not the same as the dependant-rebate test. [LISLR arts. 55, 57-60](https://contraloriadebarquisimeto.gob.ve/images/baselegal/LOAFSP.pdf#page=14).

For rebates, art. 59 allows the taxpayer's own 10 U.T., spouse not separated as to property and eligible direct ascendants/descendants resident in Venezuela. Adult descendants qualify only if incapacitated for work or studying and younger than 25. Separate spouse declarations remove the spouse rebate and only one may claim family charges; multiple supporters divide the dependant rebate. Its official-service exception relaxes the residence condition for specified relatives. Spousal aggregation/separate-return treatment must first be determined under arts. 54/78; do not duplicate deductions or rebates across returns. [LISLR arts. 54, 59, 78](https://contraloriadebarquisimeto.gob.ve/images/baselegal/LOAFSP.pdf#page=14).

**Decision:** if eligible itemized total exceeds 774 U.T., itemizing generally lowers the ordinary base; otherwise the standard allowance is at least as large. Run both complete returns where separate-regime income or joint-filing facts make a simple comparison incomplete. Retain the decision and evidence annually; there is no current bolívar threshold in this Guide.

### Lever 2: preserve and use genuine losses

Separate Venezuelan and foreign operating losses. Use each only against same-source enrichment within the next three periods after the loss arose, at no more than 25% of that period's enrichment. A 2023 operating loss can therefore be eligible in 2024, 2025 **and 2026**; 2026 is not excluded merely because it is the fourth calendar label in an inclusive list. The law provides forward use, not carryback. [LISLR arts. 4, 55](https://contraloriadebarquisimeto.gob.ve/images/baselegal/LOAFSP.pdf#page=14).

Forecast actual expected income by source and vintage before a loss expires. Genuine commercial activity may change the projection; do not shift recognition contrary to arts. 5/32, invent sales, create artificial losses or characterize an expired loss as current. Uncompensated net inflation losses cannot carry forward under art. 181 and are not ordinary operating losses. Banks, financial/insurance/reinsurance businesses and designated special taxpayers are excluded from the statutory inflation-adjustment system under art. 171. [LISLR arts. 5, 32, 55, 171, 181](https://contraloriadebarquisimeto.gob.ve/images/baselegal/LOAFSP.pdf#page=26); [COT art. 16](https://www.cmchacao.gob.ve/wp-content/uploads/2025/08/Decreto-con-Rango-Valor-y-Fuerza-de-Ley-que-Reforma-la-Ley-que-Establece-el-Impuesto-al-Valor-Agregado.pdf#page=4).

Record vintage, source, original amount, previous use, balance, each remaining eligible period and projected cap. Convert real results using the legally applicable measurement evidence; the illustrations below do not assume that a nominal bolívar loss changes just because UT changes. Current inflation implementation and the grammatically incomplete foreign-currency adjustment sentence in printed art. 186 remain unconfirmed.

### Lever 3: compare legal forms, not headline rates

Compute individual and company tax separately on the actual legally attributed bases. A company cannot use the resident individual's 774 U.T. allowance or personal rebates. Nor do the individual and company rates suddenly become equal once business profit exceeds 3,000 or 4,000 U.T.: those are different marginal bands, and lower bands remain relevant. The numeric comparison below demonstrates this. A company may also have different deductible costs, compliance burdens and distribution consequences. [LISLR arts. 8-10, 50, 52, 57-59](https://contraloriadebarquisimeto.gob.ve/images/baselegal/LOAFSP.pdf#page=6).

| Alternative | What must be compared | Official source |
|---|---|---|
| Genuine individual business | Individual net enrichment, eligible personal deductions, rebates and applicable Tarifa 1; do not misclassify employment as a business | LISLR arts. 8, 27, 50, 57-59, https://contraloriadebarquisimeto.gob.ve/images/baselegal/LOAFSP.pdf#page=13 |
| Ordinary company retaining profit | Company tax under Tarifa 2; future distribution exposure is a separate computation and retention does not by itself erase tax on an already taxable distribution | LISLR arts. 9, 52, 64-71, https://contraloriadebarquisimeto.gob.ve/images/baselegal/LOAFSP.pdf#page=15 |
| Company distributing profit | Company tax plus only the properly allocated taxable dividend; compare investor-level consequences and any actual in-force treaty, not an assumed second charge on all after-tax profit | LISLR arts. 3, 64-73, https://contraloriadebarquisimeto.gob.ve/images/baselegal/LOAFSP.pdf#page=15 |
| Member-taxed partnership/consortium | Entity enrichment/control duties plus member tax and joint liability under art. 10; not automatic ordinary-company taxation | LISLR arts. 7, 10, https://contraloriadebarquisimeto.gob.ve/images/baselegal/LOAFSP.pdf#page=6 |
| Financial or extractive activity | Establish the actual special taxpayer/activity regime first; incorporation is not an election to avoid a statutory sector rate | LISLR arts. 11-12, 52-53, https://contraloriadebarquisimeto.gob.ve/images/baselegal/LOAFSP.pdf#page=13 |

**Decision:** recommend a legal form only after modeling actual commercial needs, owner cash requirements, costs and distributions. The old rule that a company is beneficial only with a foreign treaty holding company is not supported by these statutes. Do not establish an artificial conduit to obtain an assumed treaty rate. [LISLR art. 3](https://contraloriadebarquisimeto.gob.ve/images/baselegal/LOAFSP.pdf#page=4); [COT art. 16](https://www.cmchacao.gob.ve/wp-content/uploads/2025/08/Decreto-con-Rango-Valor-y-Fuerza-de-Ley-que-Reforma-la-Ley-que-Establece-el-Impuesto-al-Valor-Agregado.pdf#page=4).

### Lever 4: special economic zones and incentives

Preserve La Guaira, military Aragua, Paraguaná and Isla La Tortuga as distinct review cases. Obtain the actual zone decree, authorized activities, geographic perimeter, agreement/admission evidence, current implementing resolution and any annual cap before computing an incentive. Distinguish an exemption from a credit or reimbursement: a future refund is not cash already available to meet a filing/payment obligation. No zone-specific refund rate, duration, export ratio or certification procedure was established from primary text for this rewrite; each is listed in Sources.

LISLR art. 195 permits presidential category/regional exonerations under specified conditions, periods and controls, and ties enjoyment to compliance with the law, regulation and actual decree. That enabling provision does **not** itself prove eligibility for a named zone. The COT reserves exemptions/rebates and authorization of benefits to law. Use a baseline without an assumed incentive and a separately labeled pending alternative; do not report the pending alternative as a current saving. [LISLR art. 195](https://contraloriadebarquisimeto.gob.ve/images/baselegal/LOAFSP.pdf#page=29); [COT art. 3](https://www.cmchacao.gob.ve/wp-content/uploads/2025/08/Decreto-con-Rango-Valor-y-Fuerza-de-Ley-que-Reforma-la-Ley-que-Establece-el-Impuesto-al-Valor-Agregado.pdf#page=2).

The old Tortuga manufacturing feasibility scenario remains a required workpaper: project tax payable, the legally verified incentive cash flows, setup/running costs and expiry/clawback risks. Its old asserted duration and full-refund computation are unconfirmed and cannot support a recommendation. Export customs drawback is a separate issue from a zone reimbursement; neither availability nor non-operation is inferred from commentary.

### Lever 5: distributions and treaty relief

Start with the dividend base, not the rate. Art. 64 taxes dividends originating in the payer's net income above taxed fiscal net income; art. 65 addresses untaxed, nonexempt/nonexonerated net income, paid or credited in cash or kind, including the specified own-share capital increases. Under art. 66, reconcile net income, taxed fiscal income and relevant dividends received. Art. 67 allocates distributions first to the preceding period's taxed fiscal income, then its qualifying already-taxed received dividends, then its untaxed excess. Art. 68 works back through earlier profit years once that period's profits are exhausted. A statement that all dividends suffer an additional charge is wrong. [LISLR arts. 64-68](https://contraloriadebarquisimeto.gob.ve/images/baselegal/LOAFSP.pdf#page=15).

Ordinary taxable dividend enrichment is subject to 34% with full withholding on payment/book credit. Art. 71 separately addresses stock-dividend advance payment and the special sector dividend rates; art. 72 requires proration where payer income was subject to different tariffs. Credits, deposits and advances to shareholders can be deemed dividends under art. 70, subject to its actual interest-and-cash-repayment exception. A loan label or a stock dividend is therefore not an automatic extraction exemption. [LISLR arts. 70-73](https://contraloriadebarquisimeto.gob.ve/images/baselegal/LOAFSP.pdf#page=16).

For a foreign company/PE, art. 69's deemed distribution is a different rule. Its reinvestment exception requires complete domestic reinvestment of the identified difference, retention for at least five years and annual external-auditor certification with the return. Do not apply this branch exception to every domestic company's retained profits. Foreign dividends under art. 66, first paragraph, have separate proportional taxation and an art. 2 foreign-tax-credit interaction. [LISLR arts. 2, 66, 69](https://contraloriadebarquisimeto.gob.ve/images/baselegal/LOAFSP.pdf#page=15).

For Spain, United States, Mexico, France, Canada and Brazil, preserve the old treaty-review scenarios but quote **no unconfirmed rate or ownership threshold**. Art. 3 requires an in-force treaty, proven residence and compliance with that treaty; foreign residence certificates require official translation and legalization. Read the actual dividend definition, beneficial-owner rule if present, ownership conditions, anti-abuse provisions, effective dates and claim procedure before calculating relief. The number of treaty partners is also unconfirmed. A generic domestic anti-abuse rule does not establish that every treaty contains the same principal-purpose test. [LISLR art. 3](https://contraloriadebarquisimeto.gob.ve/images/baselegal/LOAFSP.pdf#page=4); [COT art. 16](https://www.cmchacao.gob.ve/wp-content/uploads/2025/08/Decreto-con-Rango-Valor-y-Fuerza-de-Ley-que-Reforma-la-Ley-que-Establece-el-Impuesto-al-Valor-Agregado.pdf#page=4).

### Lever 6: related-party financing and thin capitalization

The operative provision is **LISLR art. 116**, not art. 38. First establish genuine borrowing used to produce income under art. 27(2), arm's-length terms under art. 109 and direct/indirect relatedness under arts. 114-115. Then compute the art. 116 restriction using **both independent and related debt**. Replacing a related loan with bank debt does not automatically restore capacity: independent debt consumes equity headroom. Interposed unrelated persons do not exclude indirect related transactions. [LISLR arts. 27(2), 109, 114-116](https://contraloriadebarquisimeto.gob.ve/images/baselegal/LOAFSP.pdf#page=20).

- Equity average `E`: opening plus closing net equity divided by two, before that year's inflation adjustment and excluding that year's profit/loss.
- Debt averages: each month's last-day balances summed and divided by months in the fiscal year; omit that month's accrued interest from its last-day balance.
- Let `Dind` be average independent debt, `Drel` average direct/indirect related debt, and `Irel` the otherwise qualifying related interest. If `Drel` is positive, headroom is `max(E - Dind, 0)`; the deductible fraction is at most `min(headroom / Drel, 1)`. No positive headroom supplies no capacity under that formula. Reconcile the actual statutory computation and classification before accepting the result.
- Interest allowed by the ratio still needs all other deduction/arm's-length conditions. Art. 116 can treat nonmarket related debt as equity even when total debt does not exceed equity; consider ability to obtain the loan independently, debt level, amount, rate and terms.

These are executable conditions from [LISLR art. 116](https://contraloriadebarquisimeto.gob.ve/images/baselegal/LOAFSP.pdf#page=20). Its equity recharacterization and any resulting distribution effects require professional review rather than a mechanical ratio-only recommendation.

**Decision:** compare a genuine equity injection, loan capitalization, repayment, or commercial external borrowing using the **actual dates and annual averaging**. A last-day capitalization does not retroactively alter preceding month-end debt or instantly make all annual interest deductible. Include financing cost, owner liquidity, legal formalities and other tax effects. The former interest-only savings examples are recomputed below under explicit all-year assumptions.

### Lever 7: LOCTI sector classification

Retain the separate gambling/bingo/casino, alcohol/tobacco, hydrocarbons/mining, other-activity and multiple-activity cases. Do not select a favorable activity label merely to lower a contribution. Obtain the actual current LOCTI text, threshold, measurement period, highest-currency mechanism, mixed-activity rule and competent collection instructions. The old monthly threshold, rate matrix, asserted petroleum exemption and SIDCAI payment procedure have not been confirmed from primary law for this version and supply no numerical saving. The gambling-versus-other example is retained as a comparison template requiring verified classification/base/rates before computation. A contribution cannot be assumed to be an ISLR credit; test its actual statute and the paid-tax deduction gate separately. [LISLR art. 27(3)](https://contraloriadebarquisimeto.gob.ve/images/baselegal/LOAFSP.pdf#page=9).

### Lever 8: municipal ISAE documentation and deduction

LISLR art. 27(3) allows taxes **paid** by reason of economic activities or income-producing property, excluding the taxes imposed by LISLR. Check the ordinary normal/necessary rule, records and actual payment. The income-tax consequence of a valid municipal levy is a **deduction**, not a credit equal to the levy. Compute the full before/after Tarifa 2 tax; use a marginal-rate multiplication only when the deduction remains within that band. [LISLR arts. 27(3), 32, 52, 89](https://contraloriadebarquisimeto.gob.ve/images/baselegal/LOAFSP.pdf#page=9).

Keep municipality, establishment/activity, gross-income allocation, period, current ordinance/tariff, notices, receipts and reconciliation separately. For a business in three municipalities, first establish each jurisdiction's legal allocation and charge under its actual ordinance, avoid duplicate receipts, then aggregate only qualifying paid amounts for the income-tax workpaper. No general national municipal-rate range, UT minimum or negotiable classification is asserted. Those old claims and any national harmonization limits are unconfirmed; a municipal deduction does not establish that the underlying levy was correctly assessed.

### Lever 9: IVA, imports, exports and currency settlement

Retain ordinary/reduced/luxury categories, exported goods and exported services, imported basic goods and designated-importer relief, foreign-currency/crypto payment, input credits, withholding and cash-flow planning as separate questions. Read [IVA](venezuela-iva.md) and the actual current VAT law/rate decree, invoice and withholding instructions before assigning a rate. Foreign receipt of an invoice or payment alone does not prove a qualifying exported service; classify actual service/use and statutory conditions. Do not combine a possible IVA currency surcharge with IGTF as if they were the same tax.

The old Guide contradicts itself on exported services and treats an authorized surcharge range as an operative universal payment tax. Its current operative IVA rate/decree combinations, luxury categories/value tests, import measures and currency/crypto treatment are explicitly unconfirmed here. This workflow does not recommend bolívar settlement or a nominal export structure on an assumed tax saving. Compare only legally verified alternatives including output tax, eligible input credit, withholding timing and actual recovery delays; no numerical IVA saving is supplied in this file.

### Lever 10: employment contributions and genuine classification

Keep IVSS risk class, employer/employee base and cap, FAOV, historical FAV/LPH, INCES ordinary wages versus utilidades, unemployment/employment regime, LOPCYMAT occupational-risk obligations and the special pension contribution as distinct workpapers. Obtain the current primary enactment, registration/classification decision, salary components, minimum-wage evidence, contribution rates/caps and calendar. The old alternative housing regime must not be charged in addition merely because two labels appeared in a table. Do not assume LOPCYMAT has a universal zero contribution or that INPSASEL can lower an IVSS rate on request.

Safety improvements are a genuine commercial consideration, but a reduced contribution requires the actual competent authority/classification rule. Distinguish payroll tax, employee deduction and employer cost, and model any allowable cost deduction under LISLR only after employer-compliance conditions are satisfied. A smaller stated salary or a benefit called a bonus does not prove exclusion from tax or social-insurance bases. The current wage/bonus interpretation, contribution rules and dates not confirmed here are retained in Sources. [LISLR art. 27(1)](https://contraloriadebarquisimeto.gob.ve/images/baselegal/LOAFSP.pdf#page=9).

The old safety example's claimed combined saving is unsupported and arithmetically double-counted its single IVSS difference. Retain a line for each independently evidenced actual saving; do not sum an unverified second saving. No payroll-saving amount is represented as current.

### Other old cases: cryptocurrency, special sectors and additional contributions

Money **or in-kind** annual net available enrichment falls within LISLR art. 1; art. 16 includes regular/incidental receipts and sales/services. Therefore crypto receipts cannot be ignored merely because they were not paid in bolívares. Reconstruct wallet/exchange statements, dates, transaction purpose, invoices, costs, conversion evidence and counterparties. Distinguish service consideration, trading, mining, transfers between own wallets and investment disposal before applying source, availability and cost rules. No crypto-specific valuation safe harbour, blanket market-value-at-receipt rule or year-end revaluation mandate was established here. Art. 186's printed foreign-currency adjustment sentence is incomplete and is not supplied with an invented operative verb. [LISLR arts. 1, 5, 16, 23, 186](https://contraloriadebarquisimeto.gob.ve/images/baselegal/LOAFSP.pdf#page=4).

Petroleum/hydrocarbons, mining royalties, banks/insurance, mixed companies and production-sharing arrangements remain specialist cases. The statutory sector framework above does not confirm the old alleged later hydrocarbons reform, transition period or contribution exemptions. Anti-drug, sport and high-net-wealth charges also remain named gaps; accounting profit alone does not prove their liability/base. Use actual applicable enactments and professional review, not unsupported generic percentages.

## Deadlines and filing

### Filing requirements and statutory duties

LISLR art. 77 supplies the declaration populations and strict **over** thresholds in the rates table. Do not replace them with a single net-income threshold using greater-than-or-equal. Art. 79 separately covers non-resident individual declarations. Companies and the other named entities declare even losses. These statutory tests are distinct from the amount of tax remaining after deductions/credits. [LISLR arts. 77-79](https://contraloriadebarquisimeto.gob.ve/images/baselegal/LOAFSP.pdf#page=16).

Art. 81 refers to the annual taxable period and leaves exceptional shorter-period cases to regulation. Arts. 80/82/85 leave implementing conditions and timing for estimates, self-assessment and payments. A calendar-year assumption cannot establish every taxpayer's fiscal year, March deadline, installment sequence or special-taxpayer calendar. Those old numerical dates remain unconfirmed here. [LISLR arts. 80-85](https://contraloriadebarquisimeto.gob.ve/images/baselegal/LOAFSP.pdf#page=17).

### Filing and payment sequence for the planning brief

1. Confirm RIF/representative, actual fiscal period, source/entity classification and special-taxpayer designation from records; RIF registration is addressed by art. 96. Obtain current official SENIAT instructions and taxpayer-specific notices for definitive/estimated returns and applicable withholdings. [LISLR arts. 77-85, 96](https://contraloriadebarquisimeto.gob.ve/images/baselegal/LOAFSP.pdf#page=16).
2. Complete the tax reconciliation and both planning alternatives before using the live form. Document income/expense timing, personal deduction election, rebates, loss vintages, financing, distributions, tax credits and other-tax effects. [LISLR arts. 2, 4-5, 27, 32, 50-59, 64-73, 83, 116](https://contraloriadebarquisimeto.gob.ve/images/baselegal/LOAFSP.pdf).
3. Map the approved calculation to the **actual authorized return and fields**, preserving computation/input evidence. Portal menus, form numbers, box labels, attachments, payment references and installment elections are not confirmed here; do not fabricate an electronic filing walkthrough. [LISLR arts. 77, 82, 85](https://contraloriadebarquisimeto.gob.ve/images/baselegal/LOAFSP.pdf#page=16).
4. Preserve filed return, acknowledgement, actual payment evidence, withholding certificates, excess-credit requests and signed working papers. A planning computation is not proof of filing/payment. [LISLR arts. 56, 83-85, 88-89](https://contraloriadebarquisimeto.gob.ve/images/baselegal/LOAFSP.pdf#page=14).

**Access record:** official gazette facsimiles on Venezuelan public-body hosts opened successfully. Direct SENIAT/return-portal attempts for current administrative instructions did not yield readable text; ordinary-browser/archive attempts documented in Sources did not establish the missing rules. This is a decision Guide with a partial filing handoff, not a verified current portal manual.

### Annual planning calendar without invented statutory dates

| Stage | Action and evidence to retain |
|---|---|
| Start of the actual fiscal period | Confirm taxpayer classification, opening loss vintages, opening equity and current official calendars; assign an owner to every unconfirmed item |
| Each accounting close | Reconcile realized/accrued/paid income and expenses; preserve debt month-end balances, payroll records, municipal receipts, IVA ledgers and contribution evidence |
| Before a genuine investment/expense decision | Compare eligible personal expenditure or documented business cost with the baseline; check whether expense timing or a cap actually changes this year's tax |
| Before a distribution or financing change | Reconcile profit-year tax pools, beneficial parties, treaty proof, debt averages and legal effective dates; do not assume a last-day entry repairs the entire year |
| Before fiscal close | Project same-source loss absorption and expiry; determine UT evidence applicable at close and inflation eligibility; do not force income contrary to availability rules |
| Before each verified filing/payment deadline | Finalize professional review, actual form mapping, credits and payment arrangements; preserve acknowledgement and payment evidence |
| After filing | Reconcile actual amounts/credits, follow evidenced refund requests, preserve records and carry only still-eligible source/vintage balances |

This calendar is a working-paper workflow. It replaces the old month-by-month presumed legal dates; it supplies no legal extension or installment concession.

### Retention is not a blanket five-year rule

COT art. 155(3) requires ordered records while the tax is not prescribed. Art. 55 generally specifies six years for its listed rights/actions; art. 56 extends specified cases to ten, including nonfiling, registration failures, foreign-linked facts and deficient accounting/retention. Starting dates, interruption and suspension require arts. 59-63. Do not destroy records simply a fixed number of years after a return, and preserve older records supporting an open loss or tax pool. Criminal limitation rules are separate. [COT arts. 55-63, 155](https://www.cmchacao.gob.ve/wp-content/uploads/2025/08/Decreto-con-Rango-Valor-y-Fuerza-de-Ley-que-Reforma-la-Ley-que-Establece-el-Impuesto-al-Valor-Agregado.pdf#page=7).

## Penalties and interest

COT art. 91 uses the **official exchange rate of the highest-valued currency published by BCV at payment** for the fines expressed in that unit. It does not say to assume USD, euros or UT. Determine the actual applicable penalty and rate evidence before converting. [COT art. 91](https://www.cmchacao.gob.ve/wp-content/uploads/2025/08/Decreto-con-Rango-Valor-y-Fuerza-de-Ley-que-Reforma-la-Ley-que-Establece-el-Impuesto-al-Valor-Agregado.pdf#page=11).

For declarations, art. 103(1) covers nonfiling or delay over one year: a fine of 150 times that exchange-rate unit plus ten continuous days' closure where premises exist. Art. 103(3) covers incomplete declarations or delay up to and including one year: 100 times. Its other identified communications/format/substitute-return infringements carry 50 times; low-tax investment information has separate larger sanctions. Closure extends to all establishments/branches. Art. 108 increases pecuniary formal sanctions by 200% for designated special taxpayers, rather than making the total merely 200% of the base. Do not apply the annual-return provision automatically to a withholding offense. [COT arts. 103, 108](https://www.cmchacao.gob.ve/wp-content/uploads/2025/08/Decreto-con-Rango-Valor-y-Fuerza-de-Ley-que-Reforma-la-Ley-que-Establece-el-Impuesto-al-Valor-Agregado.pdf#page=12).

Late-payment interest arises automatically from the due date through extinguishment at **1.2 times** the applicable active bank rate for each relevant period, not a flat annual 1.2%. Art. 66 defines the reference as BCV's prior-month average for the six largest commercial/universal banks by deposits, excluding preferential portfolios, with publication/fallback rules. Actual monthly rates and balances are missing here, so no interest amount is supplied. Underassessment, evasion, withholding and failure to remit require their own facts and statutes; refer suspected fraud/regularization rather than inventing a universal penalty. [COT arts. 66, 109-124](https://www.cmchacao.gob.ve/wp-content/uploads/2025/08/Decreto-con-Rango-Valor-y-Fuerza-de-Ley-que-Reforma-la-Ley-que-Establece-el-Impuesto-al-Valor-Agregado.pdf#page=8).

## Cross-border points

A legal alternative must preserve the source of each income and expense. Foreign operating losses cannot offset territorial enrichment. Art. 2 permits foreign income tax actually paid on included foreign enrichment to be credited, capped by Venezuelan global tax in the proportion foreign net enrichment bears to global net enrichment; separately proportional income uses its Venezuelan-item tax cap. Foreign tax is translated at its payment-date rate, distinct from art. 16's fiscal-year-average conversion of foreign gross income. [LISLR arts. 1-4, 16, 55](https://contraloriadebarquisimeto.gob.ve/images/baselegal/LOAFSP.pdf#page=4).

Foreign-source business expenses require art. 27's normal/necessary test, compliant foreign documents identifying provider/vendor and domicile, transaction nature, date/amount and Spanish translation. Demonstrated PE transaction-purpose and management expenses have their own art. 27 rules and limits for head-office/group payments; foreign technical services available domestically have a separate limitation. Do not replace a disallowed fee with a nominal royalty or loan. [LISLR art. 27, fourteenth, sixteenth and seventeenth paragraphs](https://contraloriadebarquisimeto.gob.ve/images/baselegal/LOAFSP.pdf#page=10).

Related-party transactions require arm's-length prices under art. 109, import/export methodology under art. 110 and indirect/interposed transactions under art. 115. Low-tax-jurisdiction counterparties raise art. 117's rebuttable presumption; low-tax investments under arts. 98-108 are a distinct regime needing current primary lists and facts. Treaty relief and dividend/branch questions follow the previous levers. Outbound withholding under art. 84 occurs on payment or book credit, whichever is earlier; art. 196 continues Decree 1.808 pending relevant providencias, but no current payment-code/rate table is confirmed here. [LISLR arts. 84, 98-117, 196](https://contraloriadebarquisimeto.gob.ve/images/baselegal/LOAFSP.pdf#page=18).

## Two worked examples that recompute

All examples are hypothetical. UT illustrations do not assert a current bolívar conversion. Bolívares used for the fixed nominal financing and municipal-cost illustrations are invented inputs, not statutory thresholds. Personal examples are final ordinary net enrichment before personal allowance, no special income, one resident taxpayer, no spouse/dependants, no credits except the stated personal rebate and no withholding. Statutory inputs come from LISLR arts. 27, 50, 52, 55, 57-59, 64-71 and 116 in the linked gazette. The full cases preserve and correct the old examples/tests.

### Case 1: itemizing wins, and the opposite decision

A resident professional has 5,000 U.T. before personal allowance. Eligible paid medical/hospital costs are 1,000 U.T., eligible hospitalization/surgery insurance 200, eligible domestic education 300 and principal-home interest 900. Itemized total is 2,400 U.T.; ordinary base 2,600. Under standard allowance the base is 4,226. Tarifa 1 before the personal rebate is respectively 265 and 650.54 U.T.; after the same 10 U.T. rebate, 255 and 640.54. Itemizing saves 385.54 U.T. No life-insurance payment is included. [LISLR arts. 50, 57-59](https://contraloriadebarquisimeto.gob.ve/images/baselegal/LOAFSP.pdf#page=14).

```oa-check
name: Personal deduction decision, itemized wins
inputs:
  net_enrichment: 5000
  medical: 1000
  eligible_insurance: 200
  education: 300
  home_interest: 900
steps:
  - itemized: medical + eligible_insurance + education + min(home_interest, 1000)
  - base_itemized: max(net_enrichment - itemized, 0)
  - base_standard: max(net_enrichment - 774, 0)
  - tax_itemized: base_itemized * 0.20 - 255 - 10
  - tax_standard: base_standard * 0.29 - 575 - 10
  - saving: tax_standard - tax_itemized
expected:
  itemized: 2400
  base_itemized: 2600
  base_standard: 4226
  tax_itemized: 255
  tax_standard: 640.54
  saving: 385.54
```

In the opposite decision, final ordinary enrichment is 3,500 U.T. and all eligible itemized payments total only 500 U.T. Itemizing leaves a 3,000 U.T. base; the standard leaves 2,726. Tax after the personal rebate is 335 versus 280.20 U.T. Choose the standard; the saving is 54.80 U.T. This also replaces the old basic personal test, which omitted the rebate and rounded its bolívar arithmetic prematurely.

```oa-check
name: Personal deduction decision, standard wins
inputs:
  net_enrichment: 3500
  eligible_itemized: 500
steps:
  - standard_base: net_enrichment - 774
  - itemized_base: net_enrichment - eligible_itemized
  - standard_tax: standard_base * 0.20 - 255 - 10
  - itemized_tax: itemized_base * 0.20 - 255 - 10
  - saving_standard: itemized_tax - standard_tax
expected:
  standard_base: 2726
  itemized_base: 3000
  standard_tax: 280.20
  itemized_tax: 335
  saving_standard: 54.80
```

### Case 2: loss use through the third following period

An ordinary company has a 2023 Venezuelan operating loss of 3,000 U.T. and final Venezuelan enrichment before loss of 2,000, 4,000 and 6,000 U.T. in 2024-2026. Assume the figures have already been properly measured for this illustration; no inflation or foreign loss, credits or later loss exists. The cap permits 500, 1,000 and 1,500 U.T. respectively. The entire loss is used by the end of 2026; 2027 would be outside this vintage's window. Company tax in those years is 225, 520 and 1,030 U.T.; without losses it would be 300, 860 and 1,540. Total saving is 925 U.T. [LISLR arts. 4, 52, 55](https://contraloriadebarquisimeto.gob.ve/images/baselegal/LOAFSP.pdf#page=14).

```oa-check
name: Three following periods include the third following year
inputs:
  loss_2023: 3000
  income_2024: 2000
  income_2025: 4000
  income_2026: 6000
steps:
  - use_2024: min(loss_2023, income_2024 * 0.25)
  - balance_2024: loss_2023 - use_2024
  - use_2025: min(balance_2024, income_2025 * 0.25)
  - balance_2025: balance_2024 - use_2025
  - use_2026: min(balance_2025, income_2026 * 0.25)
  - expired_after_2026: balance_2025 - use_2026
  - tax_2024: (income_2024 - use_2024) * 0.15
  - tax_2025: (income_2025 - use_2025) * 0.22 - 140
  - tax_2026: (income_2026 - use_2026) * 0.34 - 500
  - total_saving: 300 + 860 + 1540 - tax_2024 - tax_2025 - tax_2026
expected:
  use_2024: 500
  use_2025: 1000
  use_2026: 1500
  expired_after_2026: 0
  tax_2024: 225
  tax_2025: 520
  tax_2026: 1030
  total_saving: 925
```

For the old final-year-cap test, change the facts to a 2023 loss of 4,000 U.T., none previously used, and 2026 same-source enrichment of 12,000 U.T. Use only 3,000, leaving 1,000 to expire after 2026. Final base is 9,000 and tax 2,560 U.T., against 3,580 without the loss; saving 1,020. A further foreign loss cannot replace or enlarge this domestic claim.

```oa-check
name: Final eligible loss year, quarter cap and expiry
inputs:
  opening_loss: 4000
  current_income: 12000
steps:
  - allowed_loss: min(opening_loss, current_income * 0.25)
  - taxable_base: current_income - allowed_loss
  - tax_without: current_income * 0.34 - 500
  - tax_with: taxable_base * 0.34 - 500
  - saving: tax_without - tax_with
  - expires: opening_loss - allowed_loss
expected:
  allowed_loss: 3000
  taxable_base: 9000
  tax_without: 3580
  tax_with: 2560
  saving: 1020
  expires: 1000
```

### Case 3: related finance with independent debt and a genuine alternative

Assume opening/closing equity both Bs. 200,000, independent month-end debt Bs. 50,000 and related month-end debt Bs. 300,000 throughout the year. Related interest otherwise qualifies and is paid at a hypothetical 12% contractual rate: Bs. 36,000. Headroom is 150,000; deductible fraction 0.5, deductible interest 18,000, disallowed interest 18,000. If the business is wholly in Tarifa 2's top band for both alternatives, that disallowance adds Bs. 6,120 tax. The rate is the statutory marginal 34%; the contractual interest rate is an invented fact. [LISLR arts. 27, 52, 109, 116](https://contraloriadebarquisimeto.gob.ve/images/baselegal/LOAFSP.pdf#page=20).

A **start-of-year** genuine capitalization of Bs. 75,000, maintained throughout, makes equity 275,000 and related debt 225,000; after the same independent debt, capacity is 225,000. Ratio restrictions no longer disallow interest, assuming all other conditions hold. But annual interest is now only 27,000 because less is borrowed. The before/after net interest cost must reflect that difference; it is not correct to call the eliminated disallowance alone the entire economic saving. A year-end-only change requires new average calculations.

```oa-check
name: Financing decision includes independent debt and changed interest cost
inputs:
  equity: 200000
  independent_debt: 50000
  related_debt: 300000
  contractual_interest_rate: 0.12
  capitalization_at_start: 75000
steps:
  - original_interest: related_debt * contractual_interest_rate
  - headroom: max(equity - independent_debt, 0)
  - allowed_original: original_interest * min(headroom / related_debt, 1)
  - disallowed_original: original_interest - allowed_original
  - disallowance_tax: disallowed_original * 0.34
  - new_equity: equity + capitalization_at_start
  - new_related_debt: related_debt - capitalization_at_start
  - new_interest: new_related_debt * contractual_interest_rate
  - new_capacity: max(new_equity - independent_debt, 0)
  - allowed_new: new_interest * min(new_capacity / new_related_debt, 1)
  - net_interest_cost_original: original_interest - allowed_original * 0.34
  - net_interest_cost_new: new_interest - allowed_new * 0.34
  - net_cost_reduction: net_interest_cost_original - net_interest_cost_new
expected:
  original_interest: 36000
  headroom: 150000
  allowed_original: 18000
  disallowed_original: 18000
  disallowance_tax: 6120
  new_equity: 275000
  new_related_debt: 225000
  new_interest: 27000
  allowed_new: 27000
  net_interest_cost_original: 29880
  net_interest_cost_new: 17820
  net_cost_reduction: 12060
```

The older small-loan test can be retained under its explicit no-independent-debt, all-year balances: equity Bs. 80,000, related debt 120,000, invented contractual interest 10%. Allowed interest is 8,000, disallowed 4,000; top-band incremental tax is 1,360. It is not a universal shortcut when independent debt, nonmarket terms or changing monthly balances exist.

```oa-check
name: Small related loan test, independent debt explicitly absent
inputs:
  equity: 80000
  related_debt: 120000
  independent_debt: 0
  interest: 12000
steps:
  - deductible: interest * min(max(equity - independent_debt, 0) / related_debt, 1)
  - disallowed: interest - deductible
  - added_tax: disallowed * 0.34
expected:
  deductible: 8000
  disallowed: 4000
  added_tax: 1360
```

### Case 4: legal-form comparison with retained profits

Assume actual net enrichment from the activity is 4,500 U.T. under both genuine legal forms after all applicable ordinary expenses. Individual has no itemized payments, uses 774 allowance and own 10 rebate: taxable base 3,726; tax 509.24. Ordinary company taxable base remains 4,500; tax 1,030. In this example the individual has 520.76 U.T. less current income tax. This is **not** a recommendation without actual legal/commercial facts and all other taxes. No distribution is made in the company alternative, so none is imputed here. This also preserves the old multi-band company test. [LISLR arts. 8-10, 50, 52, 58-59](https://contraloriadebarquisimeto.gob.ve/images/baselegal/LOAFSP.pdf#page=13).

```oa-check
name: Individual and retained-profit company, complete band comparison
inputs:
  final_activity_net: 4500
steps:
  - individual_base: final_activity_net - 774
  - individual_tax: individual_base * 0.24 - 375 - 10
  - company_tax: min(final_activity_net, 2000) * 0.15 + min(max(final_activity_net - 2000, 0), 1000) * 0.22 + max(final_activity_net - 3000, 0) * 0.34
  - tax_difference: company_tax - individual_tax
expected:
  individual_base: 3726
  individual_tax: 509.24
  company_tax: 1030
  tax_difference: 520.76
```

### Case 5: dividend tax is limited to its properly allocated base

Assume an ordinary domestic payer's preceding-year **approved net income** is 10,000 U.T. and its **net fiscal income already taxed** is 8,000; no relevant dividends received, exemptions or older pools. A 9,000 distribution is allocated under art. 67: 8,000 to taxed income, 1,000 to untaxed excess. Ordinary dividend tax is 340; shareholder receives 8,660. The remaining pool is 1,000 of untaxed excess. Compare an 8,000 distribution: all comes from taxed fiscal income, so this chapter generates zero dividend tax on those facts. These are distribution amounts, not a fresh corporation-tax base. [LISLR arts. 64-68, 71](https://contraloriadebarquisimeto.gob.ve/images/baselegal/LOAFSP.pdf#page=15).

```oa-check
name: Distribution decision respects taxed and untaxed income pools
inputs:
  approved_net_income: 10000
  already_taxed_fiscal_income: 8000
  proposed_dividend: 9000
  alternative_dividend: 8000
steps:
  - untaxed_pool: max(approved_net_income - already_taxed_fiscal_income, 0)
  - taxable_proposed: min(max(proposed_dividend - already_taxed_fiscal_income, 0), untaxed_pool)
  - proposed_withholding: taxable_proposed * 0.34
  - proposed_net: proposed_dividend - proposed_withholding
  - remaining_untaxed_pool: untaxed_pool - taxable_proposed
  - taxable_alternative: min(max(alternative_dividend - already_taxed_fiscal_income, 0), untaxed_pool)
  - alternative_withholding: taxable_alternative * 0.34
expected:
  untaxed_pool: 2000
  taxable_proposed: 1000
  proposed_withholding: 340
  proposed_net: 8660
  remaining_untaxed_pool: 1000
  alternative_withholding: 0
```

The old Spain-versus-domestic extraction example and treaty test remain pending. Replace their assumed treaty rates with the actual article and conditions only after primary verification; compare the same **properly computed taxable dividend base** under each law. A combined effective-tax calculation must use consistent pretax profit, corporation tax, distribution and shareholder tax, never subtract company tax again from a figure described as already after tax. No unsourced treaty saving is reproduced.

### Case 6: paid municipal tax is a deduction, not a tax credit

Assume a valid paid municipal business levy of Bs. 300,000 passes all art. 27(3) gates. Independent evidence establishes that both company bases, before and after this deduction, remain wholly above the top Tarifa 2 boundary after proper UT conversion. The tax reduction is 102,000 and the net levy cost 198,000. This retains the old municipal example; it is **not** a municipal-rate calculation. A business across three municipalities must first establish the correct assessment/payment in each. [LISLR arts. 27(3), 32, 52](https://contraloriadebarquisimeto.gob.ve/images/baselegal/LOAFSP.pdf#page=9).

```oa-check
name: Municipal levy deduction, both alternatives wholly in top band
inputs:
  qualifying_paid_levy: 300000
steps:
  - islr_reduction: qualifying_paid_levy * 0.34
  - after_tax_levy_cost: qualifying_paid_levy - islr_reduction
expected:
  islr_reduction: 102000
  after_tax_levy_cost: 198000
```

### Remaining scenario controls

The old high-medical-spend architect is represented by Case 1's full eligibility comparison; the multi-year company recovery by Case 2; the final-year loss test by its second block; the two finance examples by Case 3; legal-form/rate and company-band tests by Case 4; ordinary distribution by Case 5; and ISAE savings by Case 6. These examples use corrected law, no historical UT currency default, and explicit rebates/averaging. The old itemized-versus-standard higher-spend test is the same Case 1 decision with different client inputs, not a separate legal entitlement.

The old zone manufacturer, six named treaty-country holding scenarios, LOCTI misclassification, IVA classification/export/import/currency alternatives, IVSS safety reclassification, alleged zero LOPCYMAT cost, combined payroll saving and cryptocurrency-receipt cases remain review tasks under their respective levers and the named gaps below. They do not have numerical outputs because the necessary primary inputs were not confirmed. Never fill a missing rate by copying the old worked example.

## Ask the client first

Before posing a question, read the available client records and latest correspondence. Ask only for missing facts, distinguishing absent evidence from unresolved law.

1. Provide RIF, entity documents, residence/domicile facts, spouse/property regime, fiscal year, actual activities/locations, PE details and special-taxpayer designation. Who owns/manages the business and who needs cash?
2. Provide source-separated income, transactions/availability dates, actual expenses/payments, compliant invoices/RIF, reimbursements and existing deductions. Which current official UT evidence applies at the actual fiscal close?
3. For personal planning, identify each domestic education/medical/insurance/housing payment, purpose, recipient, actual payment date, shared contributions, dependants' age/residence/study/incapacity, spouse declarations and official-service facts.
4. Provide every operating-loss vintage by source, previous use and return, inflation-system history and excluded-taxpayer status. Which profitable periods actually fall before expiry?
5. Provide full related/independent financing contracts and beneficial parties; each month-end balance; opening/closing equity excluding current profit/loss and inflation adjustment; actual interest payment/accrual; dates and commercial terms of any proposed change.
6. For dividends, provide approved financial statements, taxed fiscal income and received-dividend pools by profit year, past distributions, shareholder advances, recipient residence, treaty text/status and any branch reinvestment/auditor evidence.
7. For municipal/IVA/payroll/LOCTI/zone proposals, provide the actual ordinance/law/decree/classification/admission, current calendars, salary/contribution records, import/export/service-use evidence and payment/refund history. A client statement does not substitute for primary legal authority.
8. For foreign income/crypto, provide contracts, wallet/exchange statements, source/timing facts, costs, conversion records, foreign tax payment evidence and actual foreign residence/treaty claims. Identify prior nonfiling, assessments, audits and unresolved credits.

### Reusable prompts for basic and complex work

- **Personal:** “Given these verified expenses and family facts, compare both allowable personal-deduction methods, full marginal tax and rebates for this fiscal year. Exclude ineligible or reimbursable expenses and explain the decision.”
- **Company:** “Reconcile these actual source-separated results to Tarifa 2, list eligible paid municipal taxes, apply source/vintage loss caps and reconcile documented advances.”
- **Finance:** “Using these month-end debts and opening/closing equity, compute art. 116 capacity. Compare actual dated capitalization, repayment and external-financing alternatives, with interest cost and all other deduction gates.”
- **Distribution:** “Reconstruct taxed and untaxed profit pools by year. Apply arts. 64-73, then separately test a verified treaty's exact conditions. Show cash to shareholder and consistent effective-tax denominators.”
- **Multi-year:** “Project each genuine operating-loss vintage through its three following periods. Show source, annual cap, unused balance, expiry and a compliant timing alternative, with no artificial revenue shift.”
- **Municipal:** “For each of three municipalities, establish the actual ordinance, allocation, assessed/paid amount and receipts, then compute only the legally deductible ISLR effect.”
- **Zone/LOCTI/payroll/IVA:** “List each missing official rate, period, eligibility or administrative instruction before quantifying the proposed classification or incentive. Produce a baseline and an explicitly pending alternative, with cash-flow and compliance costs.”
- **Crypto:** “Reconstruct transactions and their actual legal character/source/timing; list valuation-law gaps instead of assuming a blanket receipt or year-end rule.”

### Working-paper template and self-checks

```text
VENEZUELA 2026 TAX-PLANNING BRIEF
Client / RIF / preparer / reviewer / actual fiscal period:
Residence, legal form, activities, PE and special-taxpayer status:
Baseline business facts; proposed commercial change and effective date:
Primary law/article/official URL/exact quote/read date for each input:
Applicable UT evidence at fiscal close; unresolved currency conversions:
A. Source-separated gross receipts, availability, cost and net enrichment
B. Ordinary expenses: normal/necessary, accrued/paid condition, invoices/RIF
C. Personal eligible itemized schedule versus standard; rebates separately
D. Loss source/vintage/opening use/cap/balance/last eligible period
E. Company or individual marginal bands; proportional items kept separate
F. Municipality-by-municipality assessment/paid receipt and deduction
G. Related/independent month-end debt; opening/closing equity; ratio/terms
H. Distribution profit-year pools, taxable portion, recipient and treaty proof
I. IVA, LOCTI, employment, zone and other taxes: confirmed basis or pending
J. Foreign tax inclusion/payment/cap; withholding/advance/credit trail
K. Baseline and alternative total tax, cash timing and compliance costs
L. Actual verified deadlines, form/fields, payment and acknowledgement
M. Penalty/interest facts, applicable unit/date and record-retention review
N. Unresolved items, recommendation limits, preparer and professional sign-off
```

Check each input against evidence; recompute arithmetic; verify the actual marginal bands and source/vintage limits; separate deductions from credits; remove duplicate taxes/receipts; check every eligibility exception; and ensure the brief matches the client's actual facts. A signed professional conclusion, filed return and payment evidence are separate records.

### When to refuse or refer

Stop the affected recommendation when its legal input, measurement or client evidence is absent. Refer petroleum/mixed-company/production-sharing regimes, sector reforms, APAs and transfer-pricing benchmarking, contested related finance, low-tax investments, treaty shopping, complex distribution pools, disputed crypto valuation, incentive certification, current special-taxpayer calendar questions, tax disputes and suspected evasion/undeclared years for the specific primary law and qualified professional review. Do not calculate anti-drug, sports or high-net-wealth charges from an assumed accounting-profit rule. Refer facts; do not assert a missing rate is zero.

**Prohibitions:** no artificial losses or sham contracts; no stale UT currency default; no unsourced treaty holding-company rates; no personal deduction for an unlisted insurance product or double-counted/reimbursable expense; no foreign-loss/territorial-income netting; no inflation-loss carryforward; no ratio check ignoring independent debt or actual averages; no universal dividend second charge; no UT/USD assumption for COT fines; no unverified zone/LOCTI/payroll/IVA saving; no unsupported assertion that export drawback does or does not operate; no current sector-transition date inferred from the old Guide. [LISLR arts. 3-5, 27, 32, 55, 57-59, 64-71, 116, 181, 195](https://contraloriadebarquisimeto.gob.ve/images/baselegal/LOAFSP.pdf); [COT arts. 3, 16, 91](https://www.cmchacao.gob.ve/wp-content/uploads/2025/08/Decreto-con-Rango-Valor-y-Fuerza-de-Ley-que-Reforma-la-Ley-que-Establece-el-Impuesto-al-Valor-Agregado.pdf).

### Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional in the relevant jurisdiction before filing or acting upon. The most up-to-date version is maintained at [openaccountants.com](https://www.openaccountants.com).

## Sources

| Primary source | Official URL | Read on | What was actually opened and read |
|---|---|---|---|
| LISLR, Gaceta Oficial 6.210 Extraordinario, 30 December 2015, consolidated statute | https://contraloriadebarquisimeto.gob.ve/images/baselegal/LOAFSP.pdf | 2026-11-11 | Actual gazette PDF on the public comptroller's host, including arts. 1-16, 23, 27, 32, 38, 50-60, 64-89, 96, 109-118, 171, 181, 186, 193, 195-196 and neighboring conditions; printed PDF page 13 visually checked for art. 50/52 rate columns. Art. 55: “tres (3) períodos de imposición siguientes”; art. 116: “adicionadas con el monto de las deudas contraídas con partes independientes”. The filename names another law in the same gazette; these claims use the actual LISLR text. |
| COT, Gaceta Oficial 6.507 Extraordinario, 29 January 2020 | https://www.cmchacao.gob.ve/wp-content/uploads/2025/08/Decreto-con-Rango-Valor-y-Fuerza-de-Ley-que-Reforma-la-Ley-que-Establece-el-Impuesto-al-Valor-Agregado.pdf | 2026-11-11 | Actual gazette PDF hosted by the municipal council; arts. 3, 16, 55-63, 66, 91, 103, 108-109 and 155 with neighboring text. Art. 91: “moneda de mayor valor”; art. 155(3): “mientras el tributo no esté prescrito”. Its filename names the IVA amendment also included in the gazette; the COT was read. |

The enactment dates are historical and stated honestly; the 2026 coverage label is not a claim that a complete current administrative instruction set was obtained. No private commentary supplies missing current figures. The following list preserves unresolved topics from the prior Guide individually so they can be researched without treating historical claims as current law.

**Not yet confirmed:** G01 current UT bolívar value, effective date and claimed historical percentage increase; G02 ordinary/short-period fiscal-year choices, annual filing deadline and installment dates; G03 current special-taxpayer calendars, advances, IVA withholding designations, payment codes and remittance dates; G04 live SENIAT portal/form/field/attachment/payment/credit-refund procedures; G05 each named treaty's in-force status, dividend definition, actual rate/ownership conditions, anti-abuse provisions and claim procedure, including Spain, United States, Mexico, France, Canada and Brazil, and the total treaty count; G06 La Guaira zone refund rate/duration; G07 military Aragua zone refund rate/duration; G08 Paraguaná zone refund rate/duration; G09 Isla La Tortuga zone refund rate/duration and manufacturer cash-flow projection; G10 zone export condition, customs reimbursement, annual cap/publication timing, admission/certification and alleged Resolution 015-25 rules; G11 export customs drawback's current availability or claimed non-operation; G12 LOCTI gambling/bingo/casino/alcohol/tobacco classification and rate; G13 LOCTI hydrocarbons/mining classification/rate and alleged petroleum exemption; G14 LOCTI other/multiple-activity rates, threshold, base, monthly measurement, highest-currency conversion, competent collector and SIDCAI payment procedure; G15 municipal ISAE current ordinance-specific rates, minimum, allocation and national harmonization limits; G16 IVA ordinary/reduced/luxury operative rate/decree combinations, luxury value tests and exact qualifying categories; G17 IVA export-service conditions, input-credit eligibility and recovery procedures; G18 alleged basic-import exemption suspension and replacement designated-importer measures, current duration and eligibility; G19 IVA foreign-currency/crypto additional-rate operation versus distinct IGTF application/exemptions; G20 IVSS employer risk classification, employee rate, bases/caps, competent classification authority and payment dates; G21 FAOV rates/base/cap/payment dates and whether the historical FAV/LPH table refers to any separate current liability; G22 INCES employer/employee rates, ordinary salary versus utilidades bases and payment dates; G23 unemployment/employment contribution rates/bases/caps; G24 LOPCYMAT/risk contribution operation, assessment and rates rather than an assumed zero; G25 special pension contribution scope/base/rate/payment; G26 current minimum wage, non-salary bonus classification and applicable judicial interpretation; G27 crypto-specific valuation/recognition and claimed year-end remeasurement; G28 complete foreign-currency/indexed-asset adjustment rule where printed LISLR art. 186 is grammatically incomplete; G29 inflation-system implementation and current measurement series; G30 current hydrocarbons/PSA/mixed-company reform, transition and contribution exemptions; G31 anti-drug, sports and high-net-wealth charge scope/base/rate/procedure; G32 current BCV highest-valued-currency conversion, monthly interest rates, withholding-specific sanctions and exact case-specific retention/limitation consequences. These are research gaps, not zero rates or exclusions from the client's engagement.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-11. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `venezuela-tax-optimization` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/venezuela-tax-optimization. If neither is available, confirm every figure against the official source pages cited above before relying on it.
