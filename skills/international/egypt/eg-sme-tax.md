---
name: eg-sme-tax
description: Use this skill whenever asked about Egypt's simplified or SME tax regime for small self-employed people, freelancers, professionals, sole proprietors, and small companies. Trigger on phrases like "Egypt simplified tax", "SME tax Egypt", "small business tax Egypt", "Law 6 of 2025 Egypt", "turnover tax Egypt", "freelancer simplified Egypt", "النظام الضريبي المبسط", "ضريبة على رقم الأعمال", "قانون 6 لسنة 2025", "حوافز المشروعات الصغيرة". Covers both the SME framework under Law No. 152 of 2020 (MSME Development Law) and the NEW integrated simplified tax regime under Law No. 6 of 2025 for businesses and professionals with annual turnover up to EGP 20 million. AI replies in the user's language (English or Arabic).
version: 1.0
jurisdiction: EG
tax_year: 2026
last_updated: 2026-07-13
review_status: pending_review
depends_on:
  - income-tax-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# EG Sme Tax

## Egypt — Simplified / SME Tax Regime (Law No. 6 of 2025 + Law No. 152 of 2020)

This skill covers Egypt's turnover-based **integrated simplified tax system** (النظام الضريبي المتكامل المبسط) introduced by **Law No. 6 of 2025**, plus the underlying **MSME Development Law No. 152 of 2020** (قانون تنمية المشروعات المتوسطة والصغيرة ومتناهية الصغر). It is written for small self-employed people, freelancers, professionals (أصحاب المهن الحرة), sole proprietors, and small companies whose annual turnover does not exceed **EGP 20 million**.

> Respond in the user's language. If the user writes in Arabic, reply in Arabic and keep the native legal terms (e.g. رقم الأعمال = turnover, الإقرار الضريبي = tax return, مصلحة الضرائب المصرية = Egyptian Tax Authority).

## 1. Quick Reference

**Quick Reference**

| Field | Value |
| --- | --- |
| Country | Egypt (EG) |
| Regime | Integrated simplified tax system — turnover-based (الضريبة على رقم الأعمال) |
| Eligibility | Annual turnover ≤ **EGP 20,000,000** (whether or not registered for tax) |
| Tax basis | **% of annual turnover** (not net profit) — 0.4% to 1.5% by band |
| Currency | EGP (Egyptian Pound) |
| Legislation | **Law No. 152 of 2020** (MSME Development Law) + **Law No. 6 of 2025** (integrated simplified system) |
| Authority | Egyptian Tax Authority — **ETA** (مصلحة الضرائب المصرية) |
| Portal | eta.gov.eg |
| Effective date | Law No. 6 of 2025: published 12 Feb 2025, effective **1 March 2025** |
| Commitment | Locked into the regime for **5 years** from the request date |
| Quality tier | **Research-verified — pending sign-off by an Egyptian accountant** |
| Version | 1.0 |

### Turnover-band income tax rates (Law No. 6 of 2025)

**Turnover-band income tax rates**  _(Law No. 6 of 2025)_

| Annual turnover (EGP) | Income tax rate (% of turnover) |
| --- | --- |
| Less than 500,000 | **0.4%** |
| 500,000 to less than 2,000,000 | **0.5%** |
| 2,000,000 to less than 3,000,000 | **0.75%** |
| 3,000,000 to less than 10,000,000 | **1.0%** |
| 10,000,000 to less than 20,000,000 | **1.5%** |

The income tax is a flat percentage of **annual turnover** (إجمالي رقم الأعمال السنوي), not taxable profit. The band is determined by the year's turnover.

> Rates corroborated across multiple Big-4 / law-firm alerts (EY, WTS, and Egyptian law firms). **Verify the current band rates against ETA and the Executive Regulations before filing**, as Executive Regulations and ministerial decrees can refine bands.

### Conservative defaults

- **Default to general income-tax system unless opted in** — Default to the general income-tax system unless the user confirms they have formally applied to and been accepted into the Law 6/2025 regime. The regime is opt-in by request — it is not automatic.  _(Conservative defaults)_
- **Default to higher band near boundary** — Default to the higher band if turnover is near a band boundary.  _(Conservative defaults)_
- **Assume VAT registration required** — Assume VAT registration is still required at the standard EGP 500,000 registration threshold — Law 6/2025 simplifies VAT filing frequency, it does not abolish VAT.  _(Conservative defaults)_
- **Assume e-invoicing mandatory** — Assume e-invoicing / e-receipt compliance is mandatory to keep the incentives.  _(Conservative defaults)_
- **Assume 5-year lock-in applies** — Assume the 5-year lock-in applies once enrolled — do not advise the user they can freely exit.  _(Conservative defaults)_
- **Never compute final liability without sign-off** — Never compute a final liability without a credentialed Egyptian accountant sign-off. This skill is research-verified, not authority-certified.  _(Conservative defaults)_

## 2. Eligibility & Enrolment

### Who can join the Law 6/2025 simplified system

- **Eligible activities** — Any project / activity — commercial, industrial, service, or professional (مهنة حرة) — including freelancers and sole proprietors.  _(Law No. 6 of 2025)_
- **Annual turnover cap** — EGP 20,000,000 EGP  _(Law No. 6 of 2025)_
- **Applies regardless of prior registration** — Applies whether or not the person is already registered for tax (the law explicitly targets the informal sector / غير المسجلين to bring them in).  _(Law No. 6 of 2025)_
- **Companies and natural persons qualify** — Companies as well as natural persons qualify, subject to the same turnover cap.  _(Law No. 6 of 2025)_

### How to enrol (via ETA)

- **Enrolment steps** — 1. Register / update registration with the Egyptian Tax Authority (eta.gov.eg). 2. Submit a formal request to benefit from Law 6/2025 (طلب الانتفاع بأحكام القانون) through the ETA portal. 3. Integrate with ETA electronic systems — e-invoice (الفاتورة الإلكترونية) and/or e-receipt (الإيصال الإلكتروني) as applicable. 4. Maintain simplified books and file the special simplified returns on time.  _(eta.gov.eg)_
- **5-year commitment start** — Once accepted, the taxpayer is committed for 5 years counting from the day after the request is submitted — withdrawal before then is generally not permitted.  _(Law No. 6 of 2025)_

### Relationship to Law No. 152 of 2020 (MSME definitions)

- **Law 152/2020 purpose** — Law 152/2020 is the development / classification law; it defines enterprise size by turnover (and by capital for newly incorporated firms).  _(Law No. 152 of 2020)_
- **Micro (متناهية الصغر)** — turnover < EGP 1 million EGP  _(Law No. 152 of 2020)_
- **Small (صغيرة)** — turnover EGP 1 million to < EGP 50 million (industrial/service classification varies) EGP  _(Law No. 152 of 2020)_
- **Medium (متوسطة)** — turnover EGP 50 million up to EGP 200 million EGP  _(Law No. 152 of 2020)_

> **Verify the current Law 152/2020 size bands** — they were set by executive decree and have been updated. Law 152/2020 grants development incentives and registration with the MSME Development Agency (جهاز تنمية المشروعات); the *turnover tax* itself flows from **Law 6/2025**. The two operate together: the tax simplification (Law 6) targets the ≤ EGP 20m segment that overlaps the micro/small categories under Law 152.

### Refusal catalogue

Refuse or escalate (do **not** silently produce a number) in these cases:

- **R-EG-1 — Over threshold** — Turnover exceeds EGP 20m (outside the growth cushion). The taxpayer belongs in the general system; refuse to apply turnover rates.  _(R-EG-1)_
- **R-EG-2 — Artificial fragmentation** — The user appears to have split one business into several entities to stay under EGP 20m. The law excludes this; refuse and warn it is an abuse risk (تجزئة المشروع).  _(R-EG-2)_
- **R-EG-3 — Client-concentration exclusion** — Consultancy / professional arrangements where ~90%+ of revenue comes from one or two clients may be excluded (anti-disguised-employment). Flag and require verification.  _(R-EG-3)_
- **R-EG-4 — Not enrolled** — The user has not submitted the request to benefit. Do not apply the regime; default to the general system.  _(R-EG-4)_
- **R-EG-5 — Mid-commitment exit request** — User wants to leave within 5 years. Explain the lock-in; do not assume they can exit.  _(R-EG-5)_
- **R-EG-6 — Out-of-scope taxpayer** — Free zones, special economic zones, oil & gas, banks/insurance, or entities barred by sector rules. Refuse and refer to a credentialed Egyptian accountant.  _(R-EG-6)_
- **R-EG-7 — Prior-year liabilities / open audits** — Settlement of past dues and the "waiver" provisions have their own deadlines and conditions; refuse to opine on amnesty without ETA confirmation.  _(R-EG-7)_
- **R-EG-8 — No credentialed sign-off** — Always required before filing — never present output as final.  _(R-EG-8)_

## 3. Turnover-band Rates & What Taxes Are Replaced / Exempted

### The core mechanic

- **Income tax formula** — Income tax under the regime = turnover × band rate (see §1 table). There is no profit computation, no depreciation schedule, no expense substantiation for the income-tax charge — the rate already embeds an assumed margin. This is the main attraction: predictability and almost no accounting overhead.  _(§1 table)_

### Taxes / charges exempted or removed for the enrolled taxpayer

Under Law 6/2025, qualifying enterprises are relieved from a bundle of taxes and fees, reported consistently across Big-4 and law-firm alerts:

- **Stamp duty exemption** — Stamp duty (ضريبة الدمغة) on the enterprise's contracts/instruments.  _(Law No. 6 of 2025)_
- **State Financial Resources Development Fee exemption** — State Financial Resources Development Fee (رسم تنمية موارد الدولة).  _(Law No. 6 of 2025)_
- **Notarisation / registration fees exemption** — Notarisation / registration fees for articles of association and contracts.  _(Law No. 6 of 2025)_
- **Capital gains tax exemption** — Capital gains tax on the sale of machinery, equipment, and fixed assets.  _(Law No. 6 of 2025)_
- **Dividend tax exemption** — Tax on dividends (ضريبة الأرباح الموزعة) distributed within the regime.  _(Law No. 6 of 2025)_
- **Withholding/advance-payment removal** — Withholding tax (الخصم تحت حساب الضريبة) and advance-payment systems at source — the enterprise is taken out of these collection mechanisms.  _(Law No. 6 of 2025)_

### Growth cushion (تجاوز الحد)

- **Within 20% excess, single event** — If turnover exceeds EGP 20m once within the 5-year window by no more than 20%, the enterprise keeps the benefit at the 1.5% band for one additional year.  _(Law No. 6 of 2025)_
- **Above 20% or repeated breach** — If the excess is above 20%, or the threshold is breached repeatedly, all reduced-tax benefits are revoked from the following year and the taxpayer moves to the general system.  _(Law No. 6 of 2025)_

### Audit / inspection deferral

- **5-year audit deferral** — Income tax and VAT returns of an enrolled enterprise are not inspected (audited) until 5 years have passed from the request date, provided the taxpayer stays compliant. This is a major compliance relief, not a permanent exemption.  _(Law No. 6 of 2025)_

## 4. Simplified VAT & Filing Under the Regime

**Filing comparison table**

| Return | Standard system | Under Law 6/2025 |
| --- | --- | --- |
| VAT (ضريبة القيمة المضافة) | Monthly | **Quarterly** — filed within one month after the quarter-end, with payment |
| Income tax (ضريبة الدخل) | Annual, profit-based, complex | **Annual simplified return** on a special template, turnover-based |
| Payroll / wage tax (ضريبة كسب العمل) | Monthly remittance + reconciliation | Obligation limited to the **annual settlement declaration** plus remittance |
| Withholding tax | Periodic | **Removed** (enterprise taken out of the WHT/advance-payment system) |

The regime simplifies filing cadence, not the existence of the taxes.

### Key VAT points

- **VAT registration still applies** — VAT registration still applies at the general turnover threshold (EGP 500,000 — verify current value). Law 6/2025 changes how often you file, not whether you must register.  _(VAT Law No. 67 of 2016)_
- **Standard VAT rate** — 14% % (verify current; certain goods/services have special rates such as the 5% machinery rate or the schedule/table-tax items)  _(VAT Law No. 67 of 2016)_
- **E-invoicing/e-receipt precondition** — E-invoicing / e-receipt integration is a precondition for staying in the regime — non-compliance can forfeit the incentives.  _(Law No. 6 of 2025)_

> Confirm the **VAT registration threshold (EGP 500,000)** and the **14% standard rate** against the current VAT Law (Law 67/2016 as amended) and ETA before relying on them.

## 5. When the Simplified Regime Beats the General System

Because the turnover tax is charged on gross turnover regardless of profit, it favours high-margin, low-cost activities (typical of freelancers and professionals) and can hurt low-margin, high-cost activities.

### Break-even logic

- **Break-even comparison** — Compare: - Simplified tax = Turnover × band rate (e.g. 0.5% for a EGP 1.5m freelancer). - General income tax = Net profit × progressive personal income tax rate (top brackets reach roughly the high-20s/30s percent — verify current 2026 brackets, which were widened by the 2025 reforms). The simplified regime wins whenever: ``` Turnover × band_rate  <  Net_profit × effective_general_rate ``` Rearranging, the simplified regime is cheaper when your net margin exceeds: ``` break-even margin  ≈  band_rate / effective_general_rate ``` Because band rates are tiny (0.4%–1.5%) and the general top rate is large, the break-even margin is very low — for most genuinely profitable freelancers and small service businesses, the simplified regime is dramatically cheaper.

The general system can still win when:

- The business runs at a loss or near-zero margin (turnover tax is payable even on a loss; income tax on a loss is nil and losses may carry forward).
- The business has very high deductible costs (e.g. trading/reselling with thin markups), making the effective profit-based charge lower than 0.4%–1.5% of turnover.
- The taxpayer values loss carry-forward and capital allowances that the simplified flat charge ignores.

Always weigh the non-tax benefits: no audit for 5 years, no WHT/advance payments, quarterly (not monthly) VAT, exemptions from stamp duty / development fee / capital gains / dividends — these reduce cost and friction even when the headline tax is close.

> Remember the **5-year lock-in (§2)**: a taxpayer who expects to scale past EGP 20m soon, or to swing into losses, should model multiple years before committing.

## 6. Worked Examples

> All figures illustrative. Confirm bands, rates, and the user's enrolment status before relying on any number. Verify the 2026 general income-tax brackets.

### Example 1 — Freelance software developer (high margin)

- Turnover: EGP 1,500,000; costs: EGP 150,000; net profit: EGP 1,350,000.
- Band: 500k–<2m → 0.5%.
- Simplified income tax = 1,500,000 × 0.5% = EGP 7,500.
- General system (illustrative ~25% effective on EGP 1,350,000) ≈ EGP 337,500.
- Simplified wins overwhelmingly. Plus quarterly VAT, no WHT, 5-year no-audit.

### Example 2 — Small consultancy near the top band

- Turnover: EGP 12,000,000; net profit ~EGP 4,000,000.
- Band: 10m–<20m → 1.5%.
- Simplified income tax = 12,000,000 × 1.5% = EGP 180,000.
- General system (illustrative ~22.5% on EGP 4m) ≈ EGP 900,000.
- Simplified still wins by a wide margin given the healthy margin.
- R-EG-3 check: if 90%+ of that EGP 12m comes from one client, the consultancy may be excluded — flag before proceeding.

### Example 3 — Low-margin reseller (general system may win)

- Turnover: EGP 9,000,000; net profit only EGP 200,000 (thin 2.2% margin).
- Band: 3m–<10m → 1.0%.
- Simplified income tax = 9,000,000 × 1.0% = EGP 90,000.
- General system (illustrative ~20% effective on EGP 200,000) ≈ EGP 40,000.
- General system is cheaper here — turnover tax punishes the thin margin. Recommend modelling both and getting accountant sign-off before enrolling.

### Example 4 — Growth-cushion breach

- Year 3 turnover spikes to EGP 22,000,000 (10% over EGP 20m), first breach.
- Within the 20% tolerance and a single event → keeps 1.5% band for one more year: tax ≈ 22,000,000 × 1.5% = EGP 330,000.
- If next year turnover hits EGP 26m (30% over) → benefits revoked from the following year; move to the general system. Apply R-EG-1.

### Example 5 — Micro freelancer (lowest band)

- Turnover: EGP 400,000; net profit EGP 360,000.
- Band: <500k → 0.4%.
- Simplified income tax = 400,000 × 0.4% = EGP 1,600.
- Note VAT registration threshold (EGP 500,000 — verify) is not yet crossed, so VAT registration may not be required. Income-tax personal exemptions under the general system might also produce a low charge — compare and confirm.

## 7. Tier 2 + Reference + Test Suite

### Tier 2 — escalate to a credentialed Egyptian accountant when

- Turnover is within ~10% of any band boundary or of the EGP 20m cap.
- The activity may be excluded (client concentration, fragmentation, regulated sector). See R-EG-2, R-EG-3, R-EG-6.
- There are prior-year liabilities, open audits, or amnesty/settlement questions (R-EG-7).
- The taxpayer is considering exit within the 5-year lock-in (R-EG-5).
- Cross-border income, free-zone/SEZ status, or non-resident issues arise.
- VAT registration status, schedule-tax (table-tax) items, or special VAT rates are involved.

### Reference (verify each before filing)

- Law No. 6 of 2025 — integrated simplified tax system; published Official Gazette 12 Feb 2025, effective 1 March 2025. Plus its Executive Regulations and any ETA implementing decrees.
- Law No. 152 of 2020 — MSME Development Law (size definitions; development incentives via جهاز تنمية المشروعات).
- Income Tax Law No. 91 of 2005 (as amended) — the general system.
- VAT Law No. 67 of 2016 (as amended) — VAT rate (14%) and registration threshold (EGP 500,000) — verify current values.
- Egyptian Tax Authority — eta.gov.eg — portal, enrolment request, e-invoicing/e-receipt, return templates.
- Corroborating professional commentary used for this skill: EY Global tax alert, WTS, and Egyptian law-firm alerts (2025).

### Test suite (self-checks)

1. Q: Freelancer with EGP 1.2m turnover — which band? → 0.5% (500k–<2m).
2. Q: EGP 2.5m turnover band? → 0.75% (2m–<3m).
3. Q: EGP 8m turnover band? → 1.0% (3m–<10m).
4. Q: EGP 15m turnover band? → 1.5% (10m–<20m).
5. Q: EGP 25m turnover, second breach — eligible? → No, apply R-EG-1.
6. Q: Is the tax on profit or turnover? → Turnover (gross رقم الأعمال).
7. Q: How often is VAT filed in the regime? → Quarterly.
8. Q: Can the taxpayer leave after 2 years? → No — 5-year lock-in (R-EG-5).
9. Q: Is dividend tax due on distributions within the regime? → No (exempted).
10. Q: Is enrolment automatic? → No — must submit a request to ETA (R-EG-4).
11. Q: Low-margin reseller, 2% margin, EGP 9m — does simplified always win? → No, compare with the general system (Example 3).
12. Q: 90% of revenue from one client — proceed? → Flag R-EG-3 (exclusion risk), escalate.

## PROHIBITIONS

- Do NOT present any tax figure as final or filed without sign-off from a qualified Egyptian accountant (محاسب قانوني / EGP-credentialed tax advisor).
- Do NOT assume a taxpayer is in the Law 6/2025 regime — confirm they have submitted and had accepted the request to benefit.
- Do NOT advise structuring or splitting a business to stay under EGP 20m (fragmentation is excluded and is an abuse risk — R-EG-2).
- Do NOT tell a taxpayer they can freely exit before 5 years.
- Do NOT treat the turnover tax as covering VAT, payroll tax, or registration obligations — those still exist (with simplified cadence).
- Do NOT apply the regime to over-threshold, regulated-sector, or free-zone/SEZ taxpayers (R-EG-6).
- Do NOT quote rates, thresholds, the VAT rate, or income-tax brackets as settled without verifying against ETA and the Executive Regulations — flag anything unconfirmed with "verify current value".
- Do NOT opine on amnesty/settlement of prior-year dues without ETA confirmation (R-EG-7).

## Disclaimer

This skill is research-verified against the Egyptian Tax Authority (eta.gov.eg), Big-4 (EY) and reputable Egyptian law-firm and tax-advisory publications on Law No. 6 of 2025 and Law No. 152 of 2020, current to May 2026. It is not a substitute for professional advice and has not yet been signed off by a qualified Egyptian accountant. Egyptian tax law, the Executive Regulations of Law 6/2025, band rates, thresholds, the VAT rate/threshold, and the general income-tax brackets are subject to change by decree. Always verify current figures with ETA and obtain sign-off from a credentialed Egyptian tax professional before filing or relying on any output. Provided by openaccountants.com as open-source guidance, without warranty.

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
