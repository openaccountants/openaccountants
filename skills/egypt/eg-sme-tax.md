---
name: eg-sme-tax
description: Use this skill whenever asked about Egypt's simplified or SME tax regime for small self-employed people, freelancers, professionals, sole proprietors, and small companies. Trigger on phrases like "Egypt simplified tax", "SME tax Egypt", "small business tax Egypt", "Law 6 of 2025 Egypt", "turnover tax Egypt", "freelancer simplified Egypt", "النظام الضريبي المبسط", "ضريبة على رقم الأعمال", "قانون 6 لسنة 2025", "حوافز المشروعات الصغيرة". Covers both the SME framework under Law No. 152 of 2020 (MSME Development Law) and the NEW integrated simplified tax regime under Law No. 6 of 2025 for businesses and professionals with annual turnover up to EGP 20 million. AI replies in the user's language (English or Arabic).
version: 1.1
jurisdiction: EG
tax_year: 2026
last_updated: 2026-11-01
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
depends_on:
  - income-tax-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# EG Sme Tax v1.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

This skill covers Egypt's turnover tax regime under Law 6 of 2025 for tax year 2026: businesses, professionals and companies with annual turnover up to EGP 20 million. Reply in the user's language, English or Arabic. Terms: حجم الأعمال = turnover; مصلحة الضرائب المصرية = ETA.

## Who this applies to

- **In:** any project with annual turnover not over EGP 20,000,000 that **asks** to use the law, professional activities included, whether or not registered when the law began (Law 6 art. 1). In force 1 March 2025.
- **Already under Law 152/2020:** these enterprises move to Law 6 directly, with no request (ETA Services Guide 18/2).
- **Conditions** (art. 3): file returns on time; join ETA's e-systems, including e-invoice or e-receipt, per the phases ETA sets; issue the documents.
- **Out** (art. 4): professional consulting where at least 90% of annual turnover comes from one or two persons, unless a minister's decision excepts the activity; any project that entered improperly, including splitting an activity with no economic reason. ETA carries the burden of proof on splitting.
- **Turnover is measured** (art. 2) from: the last final assessment; the last return if not yet assessed; for new registrants, the return stating expected turnover; or e-invoice and e-receipt data.
- **Default:** a taxpayer is on the general system (`eg-income-tax`) unless one of the first two bullets is met.

## Rates, bands and thresholds

| Item | Rate or amount | Conditions | Tax year | Official URL |
|---|---|---|---|---|
| Turnover under EGP 500,000 | 0.4% of turnover | Law 6 art. 10(1). Tax on turnover, not profit | 2026 | https://eta.gov.eg/sites/default/files/2025-02/law_no.6.of_.2025.pdf |
| 500,000 to under 2,000,000 | 0.5% | art. 10(2) | 2026 | same |
| 2,000,000 to under 3,000,000 | 0.75% | art. 10(3) | 2026 | same |
| 3,000,000 to under 10,000,000 | 1% | art. 10(4) | 2026 | same |
| 10,000,000 to 20,000,000 | 1.5% | art. 10(5). The ETA Services Guide prints 25,000,000 here; the statute says 20,000,000 and governs | 2026 | same |
| Tolerance | Over 20,000,000 by no more than 20%, once in the five years: stays in at 1.5% | Over 24,000,000, or a second breach: out from the following year | 2026 | same |
| Lock-in | Five years from the day after the request | art. 5; exit on form 11/1 طلبات after that | 2026 | same |
| Audit | Returns examined only after five years from the request | Income tax and VAT; art. 12 | 2026 | same |

Past periods, firms up to EGP 10 million (Law 151/2026 art. 4, as corrected): open tax for periods from **1 January 2023** (the Gazette said 2022; the notice of 8 Aug 2026 corrected it) to the last period before March 2025 is assessed as below, never below the tax in the return. The taxpayer may choose Law 91 instead.

| Turnover (EGP) | Tax | Official URL |
|---|---|---|
| Under 250,000 | 1,000 a year | https://eta.gov.eg/sites/default/files/2026-08/law.no_.151.of_.2026.pdf |
| 250,000 to under 500,000 | 2,500 a year | same |
| 500,000 to under 1,000,000 | 5,000 a year | same |
| 1,000,000 to under 2,000,000 | 0.5% of turnover | same |
| 2,000,000 to under 3,000,000 | 0.75% | same |
| 3,000,000 to 10,000,000 | 1% | same |

## The base

Tax = annual turnover × band rate. No costs, no depreciation, no losses: a loss-making year still pays. The regime wins when turnover × rate is below the `eg-income-tax` table on profit. The general system wins at a loss or thin margin, where losses carry forward five years (Law 91 art. 29) and depreciation counts.

**What the regime removes:**
- Development fee (رسم تنمية الموارد) and stamp duty; notarisation and registration fees on company formation, credit, mortgage and security contracts, and land registration for the project (art. 7).
- Tax on gains from disposing of fixed assets, machines or production equipment (art. 8).
- Tax on dividends from the regime's activity (art. 9).
- Withholding and advance payments, both ways: payers do not withhold from the project and the project does not withhold (art. 11; Services Guide).
- Full books: simplified records set by the minister apply (art. 13).

**What stays:** VAT registration and rates (`egypt-vat`), payroll tax on the annual settlement, and every tax law where Law 6 is silent (art. 6).

**Carried from the earlier version, not checked against the law.** Kept so no working rule is lost. Any figure here is unverified, and where it differs from the tables above the tables win.

- **Default to general income-tax system unless opted in**: Default to the general income-tax system unless the user confirms they have formally applied to and been accepted into the Law 6/2025 regime. The regime is opt-in by request: it is not automatic.
- **Default to higher band near boundary**: Default to the higher band if turnover is near a band boundary.
- **Assume VAT registration required**: Assume VAT registration is still required at the standard EGP 500,000 registration threshold: Law 6/2025 simplifies VAT filing frequency, it does not abolish VAT.
- **Assume e-invoicing mandatory**: Assume e-invoicing / e-receipt compliance is mandatory to keep the incentives.
- **Assume 5-year lock-in applies**: Assume the 5-year lock-in applies once enrolled: do not advise the user they can freely exit.
- **Never compute final liability without sign-off**: Never compute a final liability without a credentialed Egyptian accountant sign-off. This skill is research-verified, not authority-certified.
- **Enrolment steps**: 1. Register / update registration with the Egyptian Tax Authority (eta.gov.eg). 2. Submit a formal request to benefit from Law 6/2025 (طلب الانتفاع بأحكام القانون) through the ETA portal. 3. Integrate with ETA electronic systems: e-invoice (الفاتورة الإلكترونية) and/or e-receipt (الإيصال الإلكتروني) as applicable. 4. Maintain simplified books and file the special simplified returns on time.
Refuse or escalate (do **not** silently produce a number) in these cases:

- **R-EG-1: Over threshold**: Turnover exceeds EGP 20m (outside the growth cushion). The taxpayer belongs in the general system; refuse to apply turnover rates.
- **R-EG-2: Artificial fragmentation**: The user appears to have split one business into several entities to stay under EGP 20m. The law excludes this; refuse and warn it is an abuse risk (تجزئة المشروع).
- **R-EG-3: Client-concentration exclusion**: Consultancy / professional arrangements where ~90%+ of revenue comes from one or two clients may be excluded (anti-disguised-employment). Flag and require verification.
- **R-EG-4: Not enrolled**: The user has not submitted the request to benefit. Do not apply the regime; default to the general system.
- **R-EG-5: Mid-commitment exit request**: User wants to leave within 5 years. Explain the lock-in; do not assume they can exit.
- **R-EG-6: Out-of-scope taxpayer**: Free zones, special economic zones, oil & gas, banks/insurance, or entities barred by sector rules. Refuse and refer to a credentialed Egyptian accountant.
- **R-EG-7: Prior-year liabilities / open audits**: Settlement of past dues and the "waiver" provisions have their own deadlines and conditions; refuse to opine on amnesty without ETA confirmation.
- **R-EG-8: No credentialed sign-off**: Always required before filing: never present output as final.
- **Income tax formula**: Income tax under the regime = turnover × band rate (see §1 table). There is no profit computation, no depreciation schedule, no expense substantiation for the income-tax charge: the rate already embeds an assumed margin. This is the main attraction: predictability and almost no accounting overhead.

- **Stamp duty exemption**: Stamp duty (ضريبة الدمغة) on the enterprise's contracts/instruments.
- **State Financial Resources Development Fee exemption**: State Financial Resources Development Fee (رسم تنمية موارد الدولة).
- **Notarisation / registration fees exemption**: Notarisation / registration fees for articles of association and contracts.
- **Capital gains tax exemption**: Capital gains tax on the sale of machinery, equipment, and fixed assets.
- **Dividend tax exemption**: Tax on dividends (ضريبة الأرباح الموزعة) distributed within the regime.
- **Withholding/advance-payment removal**: Withholding tax (الخصم تحت حساب الضريبة) and advance-payment systems at source: the enterprise is taken out of these collection mechanisms.
- **Above 20% or repeated breach**: If the excess is above 20%, or the threshold is breached repeatedly, all reduced-tax benefits are revoked from the following year and the taxpayer moves to the general system.
- **5-year audit deferral**: Income tax and VAT returns of an enrolled enterprise are not inspected (audited) until 5 years have passed from the request date, provided the taxpayer stays compliant. This is a major compliance relief, not a permanent exemption.
| unverified: Return | Standard system | Under Law 6/2025 |
| --- | --- | --- |
| VAT (ضريبة القيمة المضافة) | Monthly | **Quarterly**: filed within one month after the quarter-end, with payment |
| Income tax (ضريبة الدخل) | Annual, profit-based, complex | **Annual simplified return** on a special template, turnover-based |
| Payroll / wage tax (ضريبة كسب العمل) | Monthly remittance + reconciliation | Obligation limited to the **annual settlement declaration** plus remittance |
| Withholding tax | Periodic | **Removed** (enterprise taken out of the WHT/advance-payment system) |

The regime simplifies filing cadence, not the existence of the taxes.
- **Standard VAT rate**: 14% % (verify current; certain goods/services have special rates such as the 5% machinery rate or the schedule/table-tax items)
- **E-invoicing/e-receipt precondition**: E-invoicing / e-receipt integration is a precondition for staying in the regime: non-compliance can forfeit the incentives.
Because the turnover tax is charged on gross turnover regardless of profit, it favours high-margin, low-cost activities (typical of freelancers and professionals) and can hurt low-margin, high-cost activities.

**Break-even logic**

- **Break-even comparison**: Compare: - Simplified tax = Turnover × band rate (e.g. 0.5% for a EGP 1.5m freelancer). - General income tax = Net profit × progressive personal income tax rate (top brackets reach roughly the high-20s/30s percent: verify current 2026 brackets, which were widened by the 2025 reforms). The simplified regime wins whenever: ``` Turnover × band_rate  <  Net_profit × effective_general_rate ``` Rearranging, the simplified regime is cheaper when your net margin exceeds: ``` break-even margin  ≈  band_rate / effective_general_rate ``` Because band rates are tiny (0.4% to 1.5%) and the general top rate is large, the break-even margin is very low: for most genuinely profitable freelancers and small service businesses, the simplified regime is dramatically cheaper.

The general system can still win when:

- The business runs at a loss or near-zero margin (turnover tax is payable even on a loss; income tax on a loss is nil and losses may carry forward).
- The business has very high deductible costs (e.g. trading/reselling with thin markups), making the effective profit-based charge lower than 0.4% to 1.5% of turnover.
- The taxpayer values loss carry-forward and capital allowances that the simplified flat charge ignores.

Always weigh the non-tax benefits: no audit for 5 years, no WHT/advance payments, quarterly (not monthly) VAT, exemptions from stamp duty / development fee / capital gains / dividends: these reduce cost and friction even when the headline tax is close.

Remember the **5-year lock-in (§2)**: a taxpayer who expects to scale past EGP 20m soon, or to swing into losses, should model multiple years before committing.
**Tier 2: escalate to a credentialed Egyptian accountant when**

- Turnover is within ~10% of any band boundary or of the EGP 20m cap.
- The activity may be excluded (client concentration, fragmentation, regulated sector). See R-EG-2, R-EG-3, R-EG-6.
- There are prior-year liabilities, open audits, or amnesty/settlement questions (R-EG-7).
- The taxpayer is considering exit within the 5-year lock-in (R-EG-5).
- Cross-border income, free-zone/SEZ status, or non-resident issues arise.
- VAT registration status, schedule-tax (table-tax) items, or special VAT rates are involved.

1. Q: Freelancer with EGP 1.2m turnover: which band? → 0.5% (500k to <2m).
2. Q: EGP 2.5m turnover band? → 0.75% (2m to <3m).
3. Q: EGP 8m turnover band? → 1.0% (3m to <10m).
4. Q: EGP 15m turnover band? → 1.5% (10m to <20m).
5. Q: EGP 25m turnover, second breach: eligible? → No, apply R-EG-1.
6. Q: Is the tax on profit or turnover? → Turnover (gross رقم الأعمال).
7. Q: How often is VAT filed in the regime? → Quarterly.
8. Q: Can the taxpayer leave after 2 years? → No: 5-year lock-in (R-EG-5).
9. Q: Is dividend tax due on distributions within the regime? → No (exempted).
10. Q: Is enrolment automatic? → No: must submit a request to ETA (R-EG-4).
11. Q: Low-margin reseller, 2% margin, EGP 9m: does simplified always win? → No, compare with the general system (Example 3).
12. Q: 90% of revenue from one client: proceed? → Flag R-EG-3 (exclusion risk), escalate.
- Do NOT present any tax figure as final or filed without sign-off from a qualified Egyptian accountant (محاسب قانوني / EGP-credentialed tax advisor).
- Do NOT assume a taxpayer is in the Law 6/2025 regime: confirm they have submitted and had accepted the request to benefit.
- Do NOT advise structuring or splitting a business to stay under EGP 20m (fragmentation is excluded and is an abuse risk: R-EG-2).
- Do NOT tell a taxpayer they can freely exit before 5 years.
- Do NOT treat the turnover tax as covering VAT, payroll tax, or registration obligations: those still exist (with simplified cadence).
- Do NOT apply the regime to over-threshold, regulated-sector, or free-zone/SEZ taxpayers (R-EG-6).
- Do NOT quote rates, thresholds, the VAT rate, or income-tax brackets as settled without verifying against ETA and the Executive Regulations: flag anything unconfirmed with "verify current value".
- Do NOT opine on amnesty/settlement of prior-year dues without ETA confirmation (R-EG-7).

## Deadlines and filing

| Return | Rule | Source |
|---|---|---|
| Annual income tax | Form 20 إقرارات: 1 January to 31 March for individuals; within four months of year end for companies | Art. 12; Services Guide 18/2 |
| VAT | Quarterly, within the month after the quarter, with payment | Art. 12 |
| Payroll | Annual settlement return with payment only | Art. 12 |

**Steps to join:**
1. New taxpayer: file form 1 (individual) or form 2 (company) with documents within 30 days of starting, and complete form 10/1 طلبات. ETA reviews and issues the tax card.
2. Existing taxpayer: log in on the ETA tax system for merged offices, or https://eservice.incometax.gov.eg/etax for others.
3. Enter user name and password and choose نظام المحاسبة المبسط.
4. Open form 10/1 طلبات.
5. Enter the data, the sales figure in numbers and words, and choose how turnover is set.
6. Press موافق, enter your name and the legal representative's, and press send. ETA states the filing is instant, with no fee.
7. The five years start the next day. Errors are fixed by a signed record at the tax office.

**Annual:** file form 20 on the same system. The older Form 111 guide applies to Law 152/2020 returns: https://eta.gov.eg/sites/default/files/2021-01/SMALL-PROJECTS_0.pdf. Its boxes were not read for form 20.

## Penalties and interest

- Late or missing returns break the art. 3 condition and carry the fines in `eg-income-tax`.
- Delay charge and ceiling: `eg-income-tax`.
- Passing the tolerance ends the regime from the following year (art. 10).

## Cross-border points

Law 6 has no cross-border rule. Income or payments crossing the border fall under Law 91 and `eg-withholding-tax` (art. 6).

## Two worked examples that recompute

**Case 1. Consultancy, turnover 12,000,000.** 1.5% = 180,000. Check first that one or two clients do not supply 90% of turnover.

```oa-check
name: Turnover 12m at 1.5 percent
inputs:
  turnover: 12000000
steps:
  - tax: turnover * 0.015
expected:
  tax: 180000.00
```

**Case 2. Decision: reseller, turnover 9,000,000, profit 200,000.** Turnover regime: 1% = 90,000. General: 10% on 15,000 = 1,500; 15% on 15,000 = 2,250; 20% on 130,000 = 26,000; total 29,750. The general system wins by 60,250, and the choice binds for five years. It needs e-invoices behind the costs and loses the dividend and audit reliefs.

```oa-check
name: Low-margin reseller, regime decision
inputs:
  turnover: 9000000
  profit: 200000
steps:
  - simplified: turnover * 0.01
  - general: 1500 + 2250 + (profit - 70000) * 0.20
  - general_saves: simplified - general
expected:
  simplified: 90000.00
  general: 29750.00
  general_saves: 60250.00
```

Other cases: turnover 400,000 pays 1,600. Turnover 22,000,000 for the first time pays 330,000 and stays in; 26,000,000 ends the regime next year.

## Ask the client first

1. Turnover this year and last, and by which art. 2 measure?
2. Request already filed, and on what date? Or formerly under Law 152/2020?
3. Share of turnover from the top two clients, if consulting.
4. Net profit, to run both systems.
5. On e-invoice or e-receipt? Returns on time?
6. Any sign the activity was split?

If turnover is over the limit, the client is outside, or the client wants out inside five years, say so and do not apply the rates. Do not help split a business.

## Sources

| Source | URL | Read on |
|---|---|---|
| Law 6 of 2025, whole text (OCR; rates checked against the Services Guide) | https://eta.gov.eg/sites/default/files/2025-02/law_no.6.of_.2025.pdf | 2026-11-01 |
| ETA Services Guide, 2nd edition: section 18/2 and registration pages | https://eta.gov.eg/sites/default/files/2025-08/guide.of_.the_.egyptian.tax_.authority.services.second%20edition.pdf | 2026-11-01 |
| Law 151 of 2026, art. 4 (page images read) | https://eta.gov.eg/sites/default/files/2026-08/law.no_.151.of_.2026.pdf | 2026-11-01 |
| Correction notice (page image read) | https://eta.gov.eg/sites/default/files/2026-08/law.no_.149.150.151.of_.2026.retractation.pdf | 2026-11-01 |
| ETA Form 111 guide | https://eta.gov.eg/sites/default/files/2021-01/SMALL-PROJECTS_0.pdf | 2026-11-01 |

Not yet confirmed: ministerial decisions under Law 6/2025 (form 20 text and boxes, simplified records, any activities excepted from the 90% rule, and any 2026 change to the regime). The MSME size bands in Law 152/2020 and any later update. The direct move for Law 152 enterprises rests on the Services Guide, not the statute. Whether regulated sectors, free zones or special economic zones are barred: Law 6 art. 4 does not list them, and the old skill's list had no official source. Whether a company's or a natural person's status changes any rate: the text draws no distinction. How the five-year audit date treats enterprises moved without a request.

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
