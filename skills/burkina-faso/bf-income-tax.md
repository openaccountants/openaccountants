---
name: bf-income-tax
description: >
  Burkina Faso business income tax reference for the 2026 tax year, covering individuals with commercial, industrial, agricultural or non-commercial professional income. Use for IBICA, IBNC, progressive annual profit bands, minimum tax, CGA reductions, turnover regimes, CME contributions and the election from a microenterprise regime to real-profit taxation. It distinguishes accrual business profit from the professional receipts-and-paid-expenses base, and separates statutory return preparation from unverified electronic filing details. Two executable cases compare ordinary tax with the applicable minimum and the cost of a regime election. Personal employment tax, investment income, rental income and treaty residence require their own analysis.
jurisdiction: BF
tax_year: 2026
last_updated: 2026-11-01
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
version: 1.1
---

# Burkina Faso business income tax (IBICA / IBNC) v1.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Who this applies to

Use this for 2026 business/professional income, not a single comprehensive personal income tax. IBICA covers individuals' industrial, commercial, craft, agricultural, fishing, pastoral, forestry and sylvicultural profits, including the art. 2 listed property-trading, furnished-letting and similar activities. It also covers the art. 44 entities that elect IBICA. IBNC covers independent liberal professions, non-commercial offices and residual profit sources, with the taxpayer groups and ancillary receipts in arts. 28–30. An independent professional collaborating without subordination remains a liberal professional. Salary tax belongs in [payroll](bf-payroll.md). [CGI arts. 1–3, 28–31, 43–44](https://dgi.bf/wp-content/uploads/2026/10/CGI-2026-v2.pdf).

First choose the tax regime. CME excludes liberal professions and the livestock contribution group, irrespective of legal form. Never assign CME solely because turnover is low. [CGI arts. 533–534](https://dgi.bf/wp-content/uploads/2026/10/CGI-2026-v2.pdf).

## Rates, bands and thresholds

| Item and conditions | Amount/rule | Official source |
|---|---|---|
| Annual rounded taxable IBICA/IBNC profit, progressive slices | First XOF 500,000: 10%; next XOF 500,000: 20%; excess above XOF 1 million: 27.5%; discard profit below XOF 1,000 | [CGI arts. 13, 39(1)](https://dgi.bf/wp-content/uploads/2026/10/CGI-2026-v2.pdf) |
| CGA member profit tax | 30% reduction, distinct from minimum-tax relief | [CGI arts. 14, 39(2)](https://dgi.bf/wp-content/uploads/2026/10/CGI-2026-v2.pdf) |
| IBICA MFP; annual turnover excluding VAT rounded down to XOF 100,000 | 0.5%, floor XOF 1 million RNI / XOF 300,000 RSI | [CGI arts. 23–24](https://dgi.bf/wp-content/uploads/2026/10/CGI-2026-v2.pdf) |
| Exclusive service-station manager or authorised prepaid-phone recharge distributor | Applicable MFP floor only | [CGI art. 24](https://dgi.bf/wp-content/uploads/2026/10/CGI-2026-v2.pdf) |
| CGA IBICA member MFP; newly created enterprise | 50% MFP reduction; first operating period exempt from MFP | [CGI arts. 25(2), 27](https://dgi.bf/wp-content/uploads/2026/10/CGI-2026-v2.pdf) |
| IBNC ordinary minimum even on a loss; first operating period exempt | XOF 1 million RNI / XOF 300,000 RSI; special groups below replace these amounts | [CGI art. 39(4)–(5)](https://dgi.bf/wp-content/uploads/2026/10/CGI-2026-v2.pdf) |
| Authorised compliant private nursing practice / delivery clinic | IBNC minimum XOF 50,000 / XOF 200,000 respectively | [CGI art. 39(4)](https://dgi.bf/wp-content/uploads/2026/10/CGI-2026-v2.pdf) |
| Authorised compliant educational establishment | IBNC minimum XOF 500,000 RNI / XOF 200,000 RSI; XOF 100,000 for an individual operator whose receipts stay below XOF 15 million for three successive periods | [CGI art. 39(4)](https://dgi.bf/wp-content/uploads/2026/10/CGI-2026-v2.pdf) |
| RNI | Annual turnover excluding VAT at least XOF 50 million | [CGI art. 527](https://dgi.bf/wp-content/uploads/2026/10/CGI-2026-v2.pdf) |
| RSI | XOF 15 million to below XOF 50 million excluding VAT; also CME-excluded taxpayers below RNI threshold | [CGI art. 529](https://dgi.bf/wp-content/uploads/2026/10/CGI-2026-v2.pdf) |
| CME déclaratif | Individuals: XOF 5 million to below XOF 15 million annual turnover; legal persons below XOF 15 million, subject to exclusions | [CGI art. 533-1](https://dgi.bf/wp-content/uploads/2026/10/CGI-2026-v2.pdf) |
| CME forfait | Individuals below XOF 5 million annual turnover, subject to exclusions | [CGI art. 533-2](https://dgi.bf/wp-content/uploads/2026/10/CGI-2026-v2.pdf) |
| CME member of CGA | 25% contribution reduction | [CGI art. 197](https://dgi.bf/wp-content/uploads/2026/10/CGI-2026-v2.pdf) |

The statute prints profit bands as “0 à 500.000”, “501.000 à 1.000.000”, then above XOF 1 million. Apply them to the profit rounded down to thousands; do not charge the top rate to the whole profit. These are business-profit bands without the salary-family reduction in art. 113. [CGI arts. 13, 39 and 113](https://dgi.bf/wp-content/uploads/2026/10/CGI-2026-v2.pdf).

## The base

**IBICA.** Use the net-profit/all-operations base, including relevant disposals, under arts. 4–9; apply the corporate deductibility provisions by art. 6/9. Separate assets and personal expenditure. An actually working full-time spouse's pay must be non-excessive and the spouse affiliated to compulsory Burkina social security; fictitious/excessive pay loses the whole deduction. Split mixed business/private costs; where the business portion cannot be precisely determined, art. 11 assigns two-thirds to business. Do not deduct head-office or assistance fees merely because paid: the combined 10% cap and actual-service/linked-company conditions in art. 62 are explained in [corporate tax](bf-corporate-tax.md). [CGI arts. 4–11, 53 and 62](https://dgi.bf/wp-content/uploads/2026/10/CGI-2026-v2.pdf).

**IBNC.** Net profit is receipts less necessary professional expenses, with the disposal/cessation adjustments in art. 32. Receipts include collected advances, replacement fees, remuneration gifts and ancillary professional receipts; true client disbursement funds satisfying art. 33 are excluded. Expenses must be paid during the period and meet the applicable art. 53 conditions. Art. 34 separately caps actual non-excessive foreign study/assistance charges at 10% of overheads, permits qualifying full-time spouse pay, and uses the two-thirds fallback for unmeasurable mixed expenses. Personal/luxury costs, capital purchases, capital repayments and statutory penalties are not current deductions (art. 35). Do not silently substitute IBICA accruals for this paid-expense base. [CGI arts. 32–35](https://dgi.bf/wp-content/uploads/2026/10/CGI-2026-v2.pdf).

**IBICA minimum.** Compute MFP, reduce it for effective CGA membership if applicable, then compare with progressive tax after its separate CGA reduction. MFP for the same year is credited against IBICA excluding penalty additions; the excess is acquired by the Treasury, not refunded (art. 16). RNI pays MFP monthly; RSI quarterly. Each period applies 0.5% to that period's turnover, rounds the tax down to XOF 1,000 and respects the annual floor divided by twelve/four. This instalment rounding is distinct from annual turnover rounding (arts. 23–26). IBNC uses its own art. 39 minimum, not the IBICA turnover MFP. Do not assume the IBICA CGA minimum reduction also reduces the IBNC statutory minimum. [CGI arts. 16, 23–27, 39](https://dgi.bf/wp-content/uploads/2026/10/CGI-2026-v2.pdf).

**Regime changes.** Starting-year thresholds are prorated under arts. 527/529. Crossing the RSI or CME threshold during the year ends that regime; notify the administration within thirty days under arts. 529/533-1/533-2. Downgrades from RNI/RSI require three consecutive years below the relevant threshold. Both RNI and RSI require normal SYSCOHADA accounting, not a cashbook merely because called “simplifié” (arts. 528/531). CME-to-RSI election is by letter before 1 February, effective 1 January and binding for three years; thereafter withdrawal in January. RSI-to-RNI election before 1 February also requires timely tax compliance, conforming accounts/invoices and a VAT undertaking. DGI has thirty clear days to respond, silence is acceptance, and the accepted option binds for three years, subject to the statutory administration cancellation rule. [CGI arts. 527–535](https://dgi.bf/wp-content/uploads/2026/10/CGI-2026-v2.pdf).

**CME fixed-place table.** CME replaces only IBICA/IS, MFP, TPA and patente; other taxes retain their ordinary rules (art. 532). Art. 536 bases déclaratif on last-year turnover or projected start-year turnover, forfait on estimated annual receipts from daily receipts, and assigns the following fixed-place tariff. Zone A is Ouagadougou/Bobo-Dioulasso; B is Banfora, Dédougou, Fada N'Gourma, Gaoua, Kaya, Koudougou, Koupéla, Ouahigouya, Pô, Tenkodogo, Manga, Ziniaré, Dori and Pouytenga; C is other provincial capitals/urban communes; D is other localities. [CGI arts. 532, 536](https://dgi.bf/wp-content/uploads/2026/10/CGI-2026-v2.pdf).

| Annual turnover/receipts XOF; fixed location | Class | A | B | C | D | Official source |
|---|---|---|---|---|---|---|
| 0–1,500,000 | 8 | 10,000 | 6,000 | 2,500 | 2,000 | [CGI art. 536](https://dgi.bf/wp-content/uploads/2026/10/CGI-2026-v2.pdf) |
| Above 1,500,000 through 3,000,000 | 7 | 20,000 | 12,000 | 9,000 | 3,500 | [CGI art. 536](https://dgi.bf/wp-content/uploads/2026/10/CGI-2026-v2.pdf) |
| Above 3,000,000, below 5,000,000 | 6 | 30,000 | 20,000 | 12,000 | 6,000 | [CGI art. 536](https://dgi.bf/wp-content/uploads/2026/10/CGI-2026-v2.pdf) |
| 5,000,000 through 7,000,000 | 5 | 60,000 | 42,000 | 30,000 | 14,000 | [CGI art. 536](https://dgi.bf/wp-content/uploads/2026/10/CGI-2026-v2.pdf) |
| Above 7,000,000 through 9,000,000 | 4 | 80,000 | 60,000 | 42,000 | 18,000 | [CGI art. 536](https://dgi.bf/wp-content/uploads/2026/10/CGI-2026-v2.pdf) |
| Above 9,000,000 through 11,000,000 | 3 | 120,000 | 80,000 | 54,000 | 30,000 | [CGI art. 536](https://dgi.bf/wp-content/uploads/2026/10/CGI-2026-v2.pdf) |
| Above 11,000,000 through 13,000,000 | 2 | 160,000 | 120,000 | 80,000 | 48,000 | [CGI art. 536](https://dgi.bf/wp-content/uploads/2026/10/CGI-2026-v2.pdf) |
| Above 13,000,000, below 15,000,000 | 1 | 200,000 | 160,000 | 120,000 | 80,000 | [CGI art. 536](https://dgi.bf/wp-content/uploads/2026/10/CGI-2026-v2.pdf) |

Itinerant trading uses art. 538 instead: XOF 40,000 per motor vehicle; 12,000 per motorised two/three-wheeler or cart; 9,000 per bicycle; 6,000 for other means; 4,000 on foot. Fair traders count as itinerant. Do not apply the fixed-place grid to them. [CGI art. 538](https://dgi.bf/wp-content/uploads/2026/10/CGI-2026-v2.pdf).

## Deadlines and filing

1. Identify taxpayer, activity, regime, start date and effective elections. Reconcile the appropriate profit or CME base to records.
2. IBICA: prepare the official annual result declaration by 30 April of the following year, and pay by that date. Attach art. 18/21 statements: normal SYSCOHADA/applicable special accounts, tax package, detailed income/expenses, salary and third-party remuneration statements, depreciation, provisions, rent/landlord data and detailed bad-debt data. Check relevant customer lists and company-election/statute attachments under arts. 19/21; a required financial-statement visa/certification is a separate local professional job. [CGI arts. 15, 17–21](https://dgi.bf/wp-content/uploads/2026/10/CGI-2026-v2.pdf).
3. IBICA MFP: submit the administration's turnover declaration and payment by the 15th of the next month for RNI or the 10th of the month after the quarter for RSI. Do not apply the income-return deadline to these interim obligations. [CGI art. 26](https://dgi.bf/wp-content/uploads/2026/10/CGI-2026-v2.pdf).
4. IBNC: submit the official declaration of preceding-year gross receipts, detailed expenses and net profit, with normal SYSCOHADA accounts, tax package, salary/third-party remuneration statements, retroceded-fee recipients, rents, depreciation and bad-debt details. File and pay by the last day of February; a professional civil society declares each member's share. [CGI arts. 39–40](https://dgi.bf/wp-content/uploads/2026/10/CGI-2026-v2.pdf).
5. CME: declare existence within thirty days of starting, maintain the minimal treasury receipts/expenses system and issue invoices. Déclaratif taxpayers file the prescribed prior-year form by 31 March and pay with it. Art. 537 allows quarterly payments in the first ten days of April, July, October and January. Hold a CME tax card. [CGI arts. 537, 539–540](https://dgi.bf/wp-content/uploads/2026/10/CGI-2026-v2.pdf).

The statutory filing destination is the competent tax service/receiver. Current eSINTAX form IDs, boxes, uploads, acknowledgement and payment-reference workflow remain unverified. These instructions prepare the statutory package; they do not authorise an invented portal walkthrough.

## Penalties and interest

IBICA/IBNC late or missing profit returns: art. 754 starts at 10% of duties, minimum XOF 50,000; repeat 25% with the same minimum. Filing after formal notice is 25%; the stated repeat/assessment branch is 50%; failure to file within thirty days after notice is 100%, minimum XOF 100,000. Inaccurate bases bring the good-faith/bad-faith/fraud branches of 25%/50%/100%, doubled for recurrence (art. 755). Late/insufficient profit-tax payment is 10% plus 1% per month or fraction (art. 756). MFP-obligation defaults under art. 26 produce 25% for late declaration or 50% for assessment (art. 758). For the specified annual obligations/attachments, art. 757(1) sets XOF 200,000; art. 757(2) raises that fine to XOF 500,000 for loss-making taxpayers and XOF 1,500,000 for convention businesses or businesses with a temporary exemption regime. Separate transfer-pricing branches in art. 757(2)–(4) are not this ordinary-attachment fine. CME-specific sanctions and sanction cumulation are not established here. [CGI arts. 754–758](https://dgi.bf/wp-content/uploads/2026/10/CGI-2026-v2.pdf).

## Cross-border points

IBICA uses Burkina-operated enterprise profits and treaty allocations under art. 3/46; IBNC adopts territoriality/annuality by art. 31. Foreign-paid assistance has the distinct IBNC rule above; controlled business charges require the corporate/TP analysis. Investment income, foreign residence, treaty relief and exit taxation are separate jobs, not exemptions inferred from these business bands. Ordinary RSI/CME operations are VAT-exempt subject to the options in arts. 301/530; never substitute the old blanket “no VAT” instruction for checking the effective option. [CGI arts. 3, 31, 46, 301, 307(1), 530](https://dgi.bf/wp-content/uploads/2026/10/CGI-2026-v2.pdf).

## Two worked examples that recompute

**IBICA progressive tax and MFP.** An established, non-CGA RSI trader has profit XOF 2,456,789 and turnover excluding VAT XOF 30,050,000. Round profit to XOF 2,456,000. The three slices give XOF 550,400. Turnover rounds to XOF 30 million; 0.5% is XOF 150,000, raised to the RSI minimum XOF 300,000. Profit tax controls; credit only evidenced same-year MFP payments, excluding penalties.

```oa-check
name: IBICA profit tax versus RSI minimum
inputs:
  profit: 2456789
  turnover: 30050000
steps:
  rounded_profit: floor(profit / 1000) * 1000
  progressive: min(rounded_profit, 500000) * 0.10 + min(max(rounded_profit - 500000, 0), 500000) * 0.20 + max(rounded_profit - 1000000, 0) * 0.275
  mfp: max(floor(turnover / 100000) * 100000 * 0.005, 300000)
  tax: max(progressive, mfp)
expected:
  progressive: 550400
  mfp: 300000
  tax: 550400
```

**Decision: retain CME or elect RSI?** An established non-CGA fixed-place commercial sole trader in Zone A has turnover XOF 10 million and adjusted profit XOF 2 million, no other activity/exclusion, and no VAT-option benefit. CME class 3 costs XOF 120,000. An effective timely RSI election gives progressive IBICA XOF 425,000, greater than MFP XOF 300,000. On these taxes alone CME costs XOF 305,000 less. The election also binds three years and changes accounting/VAT analysis; this arithmetic is not a recommendation without those facts.

```oa-check
name: CME versus RSI election
inputs:
  profit: 2000000
  turnover: 10000000
  cme: 120000
steps:
  ibica: 500000 * 0.10 + 500000 * 0.20 + (profit - 1000000) * 0.275
  mfp: max(turnover * 0.005, 300000)
  rsi_tax: max(ibica, mfp)
  additional_tax: rsi_tax - cme
expected:
  rsi_tax: 425000
  additional_tax: 305000
```

## Ask the client first

- Which activities, legal form and subordination/independence facts identify IBICA, IBNC or salary?
- What are actual and forecast turnover excluding VAT, start date and the preceding three years' regimes?
- Which elections, CGA membership and special authorisations are effective?
- What profit/receipt records and paid-expense evidence support the base and any foreign fees?
- For CME, which locality, fixed/itinerant activity and means of transport apply?
- What minimum-tax payments, other income and foreign operations need reconciliation?

## Sources

| Source | Actual reading scope | Read on |
|---|---|---|
| [DGI official CGI 2026](https://dgi.bf/wp-content/uploads/2026/10/CGI-2026-v2.pdf) | Edition statement; arts. 1–21, 23–35, 39–40, 43–46, 53, 62, 113, 197, 301, 307(1), 527–540 and 754–758, including regime boundaries and adjacent conditions. Relevant provisions read, not the full code. | 2026-11-01 |

Not yet confirmed: live form IDs/boxes, portal upload/acknowledgement/payment-reference steps; complete financial-statement visa/certification and customer-list execution; IBNC reference in art. 34 to art. 53 points 2–6 where current art. 53 prints five points; CME sanctions; personal/rental/investment income, treaty residence, foreign relief, exit taxation and sanction cumulation. Independent review of this rewrite is pending; no accountant has attested to it.

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
