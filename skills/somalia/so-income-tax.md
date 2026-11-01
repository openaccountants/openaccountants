---
name: so-income-tax
description: >
  Somalia individual annual income-tax working paper for 2026 preparation using the enacted Income Tax Act 37 of 2025. Use for personal income classification, annual taxable income, resident and non-resident rate selection, minor taxation and return preparation. It separates employment, business and investment income, withholding finality, deductions and payment credits. It highlights a material discrepancy in the printed annual top-band constant and stops before a final position requiring that unresolved figure. Two executable cases cover the enacted middle band and the written Ministry exception for a minor. Residence, payroll and company deduction mechanics link to their country Guides. Implementation notices, live form instructions and specialist computations remain explicit gaps. This is a conditional statutory baseline with fresh independent review pending, not a completed return or accountant attestation.
jurisdiction: SO
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
category: international
tax_year: 2026
last_updated: 2026-11-01
version: 0.1
tax_year_notes: "2026 preparation from enacted statutory baseline; effective implementation and current filing workflow unresolved."
---

# Somalia individual annual income-tax reconciliation v0.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Who this applies to

**Partial statutory-baseline method for 2026 preparation; implementation and the annual top-band discrepancy are unresolved.** It classifies an individual's employment, business and investment income and prepares a provisional annual reconciliation. It does not prove that new Act 37 applied on a particular day or establish a submitted return. Resolve dated implementation/postponement instruments and the relevant administration before finalising. The Act permits transitional measures. [Arts.9–11,105–106, PDF 35–37,124–125](https://sag.gov.so/media/documents/bulletins-contents/legislation/2025/Sharciyeedka_Canshuurta_Dakhliga.pdf).

Use the [residence working paper](so-cross-border-residence.md), which owns all statutory day/home/citizenship/posting and part-year tests. Working in Somalia is not the residence test. Resolve whether a payment is taxable income, exempt income or a final-withholding payment before selecting a rate. Sole traders must first screen the separate simplified-business regime. The payroll calculation belongs to [payroll](so-payroll-social.md). [Arts.9–15,77–78,95; Schedule 2](https://sag.gov.so/media/documents/bulletins-contents/legislation/2025/Sharciyeedka_Canshuurta_Dakhliga.pdf).

Regulation 106-1 permits postponement by public notice specifying the period. Regulation 2-2 permits circular inflation adjustments to listed amounts. Regulation 107-1 preserves specified Federal Member State collection pending a formal allocation circular; that allocation instrument has not been established. The [official annual report](https://revenuedirectorate.gov.so/sites/default/files/Annual%20Revenue%20Performance_2025_FINAL11.pdf) describes implementation delays and FY2026 plans, without settling a precise application date. Keep these as specific unresolved instruments, not a claim that no notice exists. [Regulations2-2,106-1,107-1, PDF 3,38–39](https://mof.gov.so/sites/default/files/Publications/Income%20Tax%20Regulation_%200141%2C%202025.pdf).

## Rates, bands and thresholds

| Item | Enacted annual table and conditions | Official source |
|---|---|---|
| Resident ordinary individual, annual taxable income not exceeding USD 1,200 | No tax, subject to the minor and simplified-regime exceptions | [Schedule 1 art.1(1)–(2), PDF 126–127](https://sag.gov.so/media/documents/bulletins-contents/legislation/2025/Sharciyeedka_Canshuurta_Dakhliga.pdf) |
| Resident annual band USD 1,201–6,000 | Printed table gives 6%; the USD 288 starting amount in the next band supports a marginal reading above the exempt band. Stop if exact fractional-dollar boundary treatment matters | [Schedule 1 art.1(1), PDF 126](https://sag.gov.so/media/documents/bulletins-contents/legislation/2025/Sharciyeedka_Canshuurta_Dakhliga.pdf) |
| Resident annual band USD 6,001–18,000 | USD 288 plus 12% of excess over USD 6,000, subject to the minor/special-gain rules | [Schedule 1 art.1(1)–(3), PDF 126–127](https://sag.gov.so/media/documents/bulletins-contents/legislation/2025/Sharciyeedka_Canshuurta_Dakhliga.pdf) |
| Annual amount above USD 18,000 | **Unresolved conflict:** the enacted scan prints USD 1,788 plus 18% of excess over USD 18,000. The preceding band reaches USD 1,728. Do not silently change the printed constant or finalise this band without an authoritative correction/interpretation | [Schedule 1 art.1(1), PDF 126](https://sag.gov.so/media/documents/bulletins-contents/legislation/2025/Sharciyeedka_Canshuurta_Dakhliga.pdf) |
| Resident under age18 at year end | 20% flat unless Ministry is satisfied that all included amounts meet the arm's-length standard and confirms this in writing | [Schedule 1 art.1(2), PDF 127](https://sag.gov.so/media/documents/bulletins-contents/legislation/2025/Sharciyeedka_Canshuurta_Dakhliga.pdf) |
| Non-resident natural person | 18% flat on taxable income within charge; this does not mean 18% on every gross remittance and does not determine source or final-withholding treatment | [Schedule 1 art.1(4), PDF 127](https://sag.gov.so/media/documents/bulletins-contents/legislation/2025/Sharciyeedka_Canshuurta_Dakhliga.pdf) |
| Qualifying investment-asset gains/recognised-fund lump sums | Special allocation above USD 18,000: 15% up to actual qualifying gain/lump sum and 18% for the rest; first establish asset/fund and amount conditions | [Schedule 1 art.1(3), PDF 127](https://sag.gov.so/media/documents/bulletins-contents/legislation/2025/Sharciyeedka_Canshuurta_Dakhliga.pdf) |

The top-band conflict is material: USD 288 + 12% × (USD 18,000 − USD 6,000) = USD 1,728, which is USD 60 below the printed constant. The [Directorate monthly table](https://revenuedirectorate.gov.so/direct-tax) uses USD 144 at its top-band entry, whose annual multiple is also USD 1,728. These observations identify the conflict; they are not permission to correct the law. The two worked cases below avoid that annual band entirely.

**Sole-trader regime decision before ordinary annual rates.** Regulation 9-1 applies to a resident individual with exclusively Somali-source business income, not a partnership member, whose three-year rolling-average turnover does not exceed USD 50,000 before transition/circular adjustments. Professional and principally immovable-property-leasing businesses and other circular-listed activities are excluded by regulation 9-2, subject to the transition below. With adequate records accepted by the Ministry, an election out binds the election year and following two assessment years. For an eligible taxpayer, each quarter’s business tax is the higher of USD 37.50 and1.5% of that quarter’s defined turnover, on a cash basis; only the specified article 13(3)(a),(b),(g) receipts enter that turnover and article 13(4) exclusions remain. Other taxable income remains under ordinary rules; business immovable property is treated as an investment asset. [Regulations9-1,9-2, PDF 5–6](https://mof.gov.so/sites/default/files/Publications/Income%20Tax%20Regulation_%200141%2C%202025.pdf).

For the first five assessment years of implementation, regulation 105-1 increases that baseline threshold **by**250%,200%,150%,100%,50% respectively. It suspends the regulation 9-1(2)(a) professional/activity exclusions, but does not grant the higher threshold to a person who would otherwise be excluded. Identify the actual implementation year and relevant profession before computing the threshold. Do not label calendar2026 the first implementation year without the instrument. Regulation 9-3 separately modifies accounting for qualifying individuals/partnerships; it is not another turnover tax. Its eligibility, expense-verification technology and transition calculation remain a distinct incomplete method. [Regulations9-3,105-1, PDF 6–8,34–35](https://mof.gov.so/sites/default/files/Publications/Income%20Tax%20Regulation_%200141%2C%202025.pdf).

## The base

1. **Fix the taxpayer, period and classification.** Obtain residence and age evidence, any approved period/implementation decision and all income sources. Separate employment, business and investment amounts, then distinguish exempt and final-withholding items. The default year is the calendar year; this is not a joint household computation. [Arts.10–11,25, PDF 36–37,48](https://sag.gov.so/media/documents/bulletins-contents/legislation/2025/Sharciyeedka_Canshuurta_Dakhliga.pdf).
2. **Reconcile employment.** Include salary, bonuses, allowances, overtime, termination/restrictive-payment and other employment amounts unless a specific exclusion applies. Distinguish employer-business reimbursements from personal expenses. Article 12 excludes qualifying employer-business reimbursements, specified pension-fund contributions, regulated necessary accommodation and non-allocable collective benefits on their stated conditions. Do not exclude an allowance merely because payroll calls it reimbursement. Employment income is calculated without general expense deductions under article 16. Value noncash benefits under the applicable regulation before calculating tax. [Arts.12,16,26, PDF 37–38,41,48](https://sag.gov.so/media/documents/bulletins-contents/legislation/2025/Sharciyeedka_Canshuurta_Dakhliga.pdf).
3. **Reconcile business/investment separately.** Business includes fees, trading income, specified asset gains and related inclusions; investment includes rent, debt returns, dividends, royalties and qualifying investment-asset disposal gains. Exempt/final-withholding amounts and cross-category duplicates are excluded under their specific provisions. Income-producing expense and loss rules differ by category. Use the [ordinary-business deduction method](so-corporate-income-tax.md#the-base) only for the mechanics shared by the Act, then apply the individual's own regime and rates. Do not apply the corporate rate to a sole trader. [Arts.13–24, PDF 39–47](https://sag.gov.so/media/documents/bulletins-contents/legislation/2025/Sharciyeedka_Canshuurta_Dakhliga.pdf).
4. **Determine assessable geographic scope and timing.** Residence controls worldwide assessable scope; a non-resident requires PE/source analysis. Employment and investment use cash timing; ordinary business uses accrual unless simplified rules modify it. Distinguish gross receipts, assessable category income and taxable income. [Arts.11,26–28, PDF 37,48–49](https://sag.gov.so/media/documents/bulletins-contents/legislation/2025/Sharciyeedka_Canshuurta_Dakhliga.pdf).
5. **Aggregate and apply specific reliefs.** Combine assessable category incomes, then deduct only established pension/charitable reliefs under articles 70 and76, subject to article 10's aggregate limit. Obtain fund recognition and contribution evidence before claiming relief; these relief computations remain outside this bounded method. Do not deduct personal spending or invent a personal allowance. [Arts.10,16,70,76, PDF 36,41,83–84,91](https://sag.gov.so/media/documents/bulletins-contents/legislation/2025/Sharciyeedka_Canshuurta_Dakhliga.pdf).
6. **Select the correct annual rule and reconcile payments.** Test minor status and written Ministry exception, non-residence, simplified business, qualifying gains/lump sums and the unresolved top band before the ordinary table. Show gross tax, separately established foreign credit, creditable withholding and instalments, and balance. Final-withholding amounts are not automatically included again in ordinary taxable income or credited a second time. [Arts.9,86,95–98,101–103; Schedule 1 art.1](https://sag.gov.so/media/documents/bulletins-contents/legislation/2025/Sharciyeedka_Canshuurta_Dakhliga.pdf).

An unresolved rental withholding/asset disposal is not evidence of zero tax. The predecessor's old quarterly rental bands and no-defined-residence summary cannot support a current position. Specific rental/final-withholding, asset-basis, gain/loss, pension and charitable-relief jobs remain held until their complete conditions and procedures are sourced.

## Deadlines and filing

Article 101 generally requires an income return by 31 March after the calendar year; its non-calendar alternative is the 30th day after year end. Under article 103 the self-assessed balance is due on the return deadline. Article 102 exempts specified resident cases, including solely employment taxable income subject to article 90 withholding, unless the Ministry gives written notice or the taxpayer elects to file. Other business, investment or non-withheld employment triggers the separate instalment/estimate analysis; do not infer no return from PAYE having been paid on one income stream. [Arts.97–103, PDF 116–123](https://sag.gov.so/media/documents/bulletins-contents/legislation/2025/Sharciyeedka_Canshuurta_Dakhliga.pdf).

Prepare source-by-source income schedules, statutory adjustments, taxable income, tax and credit/balance reconciliation. Attach withholding certificates and required statements under article 101. The [official form links](https://revenuedirectorate.gov.so/direct-tax) include a PIT workbook, but its current acceptance, exact boxes, submission destination, payment reference and receipt workflow have not been established. Verify the accepted version and registration/TIN instructions before entering a return. Archive the submitted file, acknowledgement and payment evidence, and reconcile any notice. Until that path is established, label the output a working paper rather than a filed return. [Arts.98,101–103](https://sag.gov.so/media/documents/bulletins-contents/legislation/2025/Sharciyeedka_Canshuurta_Dakhliga.pdf).

## Penalties and interest

No current numeric late-filing, late-payment, understatement, interest, assessment-limit or objection rule has been verified for this Guide. Do not insert a guessed percentage or zero. Keep the served notice, dates and demanded amounts; obtain the operative Revenue Administration Act/regulation and any amendment before calculating consequences or an objection deadline.

## Cross-border points

Link the [residence screen](so-cross-border-residence.md) and [related-party pricing paper](so-transfer-pricing.md) when those facts arise. Residence, source, PE, foreign credits, treaty entitlement and the asset consequences of arrival/departure require distinct evidence. The non-resident annual rate is not a treaty rate. Do not assume no gain tax because there is no separately named capital-gains tax. Act 14 and Schedule 1 expressly address investment-asset disposal gains. No treaty, exemption, foreign credit or departure treatment is granted by these examples. [Arts.11,14,37,77–88; Schedule 1 art.1](https://sag.gov.so/media/documents/bulletins-contents/legislation/2025/Sharciyeedka_Canshuurta_Dakhliga.pdf).

## Two worked examples that recompute

**Supported resident annual income.** Assume an adult resident with USD 12,000 of correctly established ordinary taxable income, no simplified/special-gain treatment, no credits, and resolved implementation. In the enacted middle annual band, USD 288 + 12% × (USD 12,000 − USD 6,000) = USD 1,008. This does not establish a monthly withholding method or resolve the annual top band.

```oa-check
name: Adult resident annual middle-band income
inputs:
  taxable_income: 12000
steps:
  excess: taxable_income - 6000
  gross_tax: 288 + excess * 0.12
expected:
  excess: 6000
  gross_tax: 1008
```

**Minor decision.** Assume USD 12,000 of correctly established resident taxable income and age17 at year end. Without the required written Ministry confirmation, the enacted flat20% gives USD 2,400. If the Ministry both accepts all included amounts as arm's length and confirms this in writing, the ordinary middle-band computation gives USD 1,008. The USD 1,392 difference is conditional on that decision; an AI's own price opinion cannot replace the written confirmation.

```oa-check
name: Minor flat rate versus documented Ministry exception
inputs:
  taxable_income: 12000
steps:
  minor_tax: taxable_income * 0.20
  ordinary_tax: 288 + (taxable_income - 6000) * 0.12
  difference: minor_tax - ordinary_tax
expected:
  minor_tax: 2400
  ordinary_tax: 1008
  difference: 1392
```

## Ask the client first

- What assessment year, administration and dated implementation instructions apply?
- What are residence, date of birth, home/travel facts and any Ministry decisions?
- What employment, business, rental, investment, foreign and disposal amounts were received, with contracts and certificates?
- Which benefit/reimbursement, fund/charity and deductible-expense documents establish classification and relief?
- Which simplified-regime facts, losses, withholding, instalments and foreign taxes exist?
- Which current registration/form/payment instructions or notices were received?

## Sources

| Official source | Actual reading and limits | Read on |
|---|---|---|
| [Attorney General Act 37/2025](https://sag.gov.so/media/documents/bulletins-contents/legislation/2025/Sharciyeedka_Canshuurta_Dakhliga.pdf) | Original Somali gazette cached; arts.9–28,89–103 and Schedules1–3 read with neighbours. Critical scope/base, ceiling, return/exemption and annual-rate scans PDF 35–36,41,46,122–123,126–128 visually inspected. Prior residence evidence preserved separately. Specialist relief/gain chapters not certified as complete workflows. | 2026-11-01 |
| [Income Tax Regulation 0142-2025](https://mof.gov.so/sites/default/files/Publications/Income%20Tax%20Regulation_%200141%2C%202025.pdf) | English scanned official PDF, filename0141 but decree/cover0142; regulations2-2,9-1 to9-3,90-1 to90-3,97-1,99-1,105-1 to105-10,106-1 and107-1 read in context. Critical PDF 5–6,26–28,34,37–38 visually inspected. No later circular/notice established. | 2026-11-01 |
| [Directorate Annual Report2025](https://revenuedirectorate.gov.so/sites/default/files/Annual%20Revenue%20Performance_2025_FINAL11.pdf) | Downloaded19page official report; implementation progress/delay text PDF 3,11–13,18 read. Report describes planned FY2026 implementation and postponed enforcement; it is not a commencement/public notice. | 2026-11-01 |
| [Revenue Directorate direct-tax page](https://revenuedirectorate.gov.so/direct-tax) | Monthly payroll table, corporate/rental summaries and form links opened; monthly top constant compared with annual statute, not substituted for it. | 2026-11-01 |

Not yet confirmed: effective implementation and later instruments; authoritative resolution of annual top-band constant and fractional-dollar band boundaries; modified-cash regime and actual simplified transition-year/election determination; current registration/FormTR1 validity, PIT boxes, submission/payment/receipt path; complete rental withholding, asset disposal, pension/charitable relief and foreign-credit/treaty/PE/entry/exit computations; numeric sanctions and procedure. Predecessor USD 200 exemption, ambiguous intermediate monthly bands and old quarterly rental brackets are held as superseded/unverified history, not reproduced as current rules. Fresh independent pack review pending; no accountant attestation.

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
