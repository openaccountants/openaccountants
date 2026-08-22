---
name: sd-corporate-income-tax
description: Use this skill whenever asked about Sudanese corporate income tax (Business Profits Tax) for resident companies, branches of foreign companies, and petroleum operations — to compute, review, or explain BPT liability, sector rates, deductions, losses, free zones, and the petroleum PSA regime. Trigger on phrases like "Sudan corporate tax", "Sudan BPT", "business profits tax Sudan", "ضريبة أرباح الأعمال السودان", "Sudan petroleum tax", or any request to prepare or check a Sudanese corporate tax return. ALWAYS read this skill before touching any Sudan corporate tax work.
version: 0.1
jurisdiction: SD
tax_year: 2025
last_updated: 2026-07-22
review_status: pending_review
depends_on:
  - income-tax-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Sudan Corporate Income Tax (Business Profits Tax — BPT) Skill

## Sudan Corporate Income Tax (Business Profits Tax — BPT) Skill v0.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

> **Currency note:** All monetary figures are in Sudanese Pounds (SDG — ج.س). Sudan has undergone multiple currency redenominations; verify current SDG values before filing.
> **YMYL — verify before relying.** Sudan's tax legislation has been subject to amendments, and the political situation (post-2021 military takeover, ongoing conflict since April 2023) has disrupted tax administration. Where this skill says "verify current value," re-confirm against the Sudan Taxation Chamber (tax.gov.sd), PwC Worldwide Tax Summaries, or a qualified Sudan accountant before filing.

## Section 1 — Scope statement

This skill covers:

- Business Profits Tax (BPT) rates and sector differentiation for resident companies
- Taxable income determination (accounting profit -> taxable profit adjustments)
- Allowable and disallowed deductions (Income Tax Act 1986, Art 18)
- Loss carryforward rules
- Withholding tax obligations on outbound payments (dividends, interest, royalties, services)
- Free Zones Act 2001 and investment incentive regime (Investment Incentive Law 2021)
- Petroleum production sharing agreement (PSA) regime — special tax treatment
- Filing requirements and self-assessment

This skill does NOT cover:

- Personal income tax for individuals — see `sd-income-tax`
- VAT — see `sd-vat-gst`
- Payroll and social insurance — see `sd-payroll-social`
- Company formation and registration — see `sd-company-formation`
- Capital gains tax — separate schedule under Income Tax Act 1986
- Zakat — separate religious obligation under Zakat Act 2001

## Section 2 — Filing requirements

**Filing requirements**  _(Income Tax Act 1986, Art 4, 10, 38, 39)_

| Item | Rule | Source |
| --- | --- | --- |
| **Who must file** | All resident companies, branches of foreign companies, and PEs of non-residents deriving Sudan-source income | Income Tax Act 1986, Art 4 |
| **Tax year** | Calendar year (1 Jan – 31 Dec); companies may use a different accounting period with approval | Income Tax Act 1986, Art 10 |
| **Return form** | Business Profits Tax return (إقرار ضريبة أرباح الأعمال) via Sudan Taxation Chamber | Income Tax Act 1986, Art 38 |
| **Filing deadline** | Within the period specified by the Secretary-General; commonly 4 months after year-end (verify current deadline) | Income Tax Act 1986, Art 38(1) |
| **Self-assessment** | Every person under self-assessment must submit return and pay tax due at time of filing; additional tax not exceeding 2x the understated amount may be imposed | Income Tax Act 1986, Art 38(2) |
| **Audited accounts** | Companies audited by the General Auditor submit return for the same period; companies with non-calendar year-end submit within the prescribed period | Income Tax Act 1986, Art 38(1) |
| **Record retention** | Accounting books (journal, ledger, inventory) must be kept for minimum 6 years in Arabic or English | Income Tax Act 1986, Art 39(3-5) |

## Section 3 — Rates and thresholds

### Sector-differentiated BPT rates

**Sector-differentiated BPT rates**  _(Income Tax Act 1986, Schedule; PwC; Britacom; Trading Economics)_

| Sector | Rate | Source |
| --- | --- | --- |
| **Standard (general/industrial companies)** | 15% | Income Tax Act 1986, Schedule; PwC Worldwide Tax Summaries — Sudan; Trading Economics |
| **Banks and financial institutions** | 30% | Income Tax Act 1986, Schedule; Britacom tax profile |
| **Tobacco / cigarette companies** | 30% | Income Tax Act 1986, Schedule; Britacom tax profile |
| **Petroleum and natural resources operations** | 30% (under PSA terms; may vary by concession agreement) | Income Tax Act 1986, Schedule; Britacom tax profile |
| **Agricultural companies** | Exempt (0%) | Income Tax Act 1986, Schedule |
| **Capital gains (corporate)** | 20% | Income Tax Act 1986; Britacom tax profile |
| **Sole proprietorship / partnership (progressive)** | 0% – 20% (progressive rates, same as personal income tax) | Income Tax Act 1986; Britacom tax profile |

### Withholding tax rates on payments

**Withholding tax rates on payments**  _(Income Tax Act 1986; PwC; Britacom)_

| Payment type | Rate | Character | Source |
| --- | --- | --- | --- |
| **Interest (to non-residents)** | 7% | Final | Income Tax Act 1986; PwC |
| **Royalties (to non-residents)** | 15% | Final | Income Tax Act 1986 |
| **Technical / management services (to non-residents)** | 15% | Final | Income Tax Act 1986 |
| **Dividends** | No separate dividend WHT | — | Income Tax Act 1986 (verify current treatment) |
| **Payments to resident taxpayers** | 4% – 15% | Credit / advance payment | Income Tax Act 1986; Britacom |
| **Payments to non-resident taxpayers** | 14% | Standard WHT on contracts | Income Tax Act 1986; Britacom |
| **Imports of goods (resident payer)** | 2% | Creditable | Income Tax Act 1986 |

## Section 4 — Computation rules

### Step 1 — Determine taxable income

- **Determine taxable income** — Tax base is **net profit** (accounting profit adjusted for tax) of the enterprise. ``` Net profit = Gross income (business profits + rental + personal income + gross income) - Allowable deductions ```  _(Income Tax Act 1986, Art 4)_

### Step 2 — Apply sector rate

- **Apply sector rate** — ``` BPT = Net profit x Sector rate (15% standard / 30% banks, tobacco, petroleum / 0% agriculture) ```  _(Income Tax Act 1986, Schedule)_

### Step 3 — Apply deductions and credits

- **Apply deductions and credits** — ``` Tax payable = BPT - WHT credits - Advance payments ```  _(Income Tax Act 1986)_

### Step 4 — Loss carryforward

- **Loss carryforward** — Business losses are computed similarly to profits and may be carried forward (verify carryforward period — commonly 5 years under standard practice).  _(Income Tax Act 1986, terminology: "Loss" in relation to business profits means a loss computed in a similar manner to profits)_

### Allowable deductions (Income Tax Act 1986, Art 18(1)(A))

- **Allowable deductions** — 1. Expenses related to the activity and necessary for its operation 2. Communication expenses (telephone, telex, fax, internet) — work-related fully deductible 3. Subscriptions to trade chambers, scientific journals, bulletins related to work 4. Advertising expenses as determined by the Secretary-General 5. Hospitality and entertainment expenses related to work (as determined by Secretary-General) 6. Rent paid for the workplace 7. **Depreciation of fixed assets** at rates specified in the First Schedule 8. Legal expenses related to the work 9. Professional allowance (subject to Art 18 and Art 38 declaration) 10. Salaries, wages, and similar payments (subject to personal income tax payment) 11. **Zakat paid** during the accounting period (subject to proof of payment) 12. Bonuses, grants, and rewards to employees — not exceeding 3 months' salary per year 13. Repair costs for buildings, machinery, and equipment (not capital expenditure; no depreciation allowed under Second Schedule) 14. **Bad debts** — must be: (a) supported by audited accounts; (b) related to the activity; (c) of specific value in accounts; (d) legal action taken and decision issued  _(Income Tax Act 1986, Art 18(1)(A))_

### Non-deductible expenses

- **Non-deductible expenses** — 1. Expenses not related to the activity or not necessary for its operation 2. Must be actual expenses supported by documents (except customary undocumented expenses like internal travel, hospitality, routine maintenance) 3. Must relate to the relevant base period (not previous or subsequent years) 4. Must relate to an activity subject to tax for the relevant base period  _(Income Tax Act 1986, Art 18)_

### Initial depreciation allowance

- **Initial depreciation allowance** — Newly purchased machinery and equipment receive **20% initial depreciation** of purchase price after being put into production. %  _(Investment Incentive Law 2021)_

## Section 5 — Edge cases and special rules

### Free Zones and Investment Incentives

- **Free Zones and Investment Incentives** — - Investment projects economically aligned with the **Investment Incentive Law 2021** are **exempt from corporate income tax** starting from the date of commercial production, for a period **not exceeding 5 years** - Capital equipment of qualifying investment projects is **exempt from VAT** (list approved by Ministry of Investment and International Cooperation) - Free Trade Zones and Duty-Free Zones enjoy customs exemptions and tax incentives - Projects in designated underdeveloped areas receive special preferences - Exporters of goods and providers of taxable services enjoy **zero VAT rate** with input VAT refund entitlement **AUDIT FLASH POINT:** Free zone exemptions are time-limited (5 years max). Track the commercial production start date carefully — the exemption clock starts then, not at company registration.  _(Investment Incentive Law 2021)_

### Petroleum Production Sharing Agreement (PSA) regime

- **Petroleum PSA regime** — - Petroleum operations are taxed at **30%** BPT rate - However, most petroleum operations are conducted under **PSA terms** that govern the fiscal regime: - The state (via Sudan National Petroleum Corporation / Sudapet) and the contractor (international oil company) share production - **Cost oil** — contractor recovers costs from a portion of produced oil - **Profit oil** — remaining oil is split between government and contractor per negotiated terms - Tax is typically paid by the contractor on its profit oil share - The PSA terms may override standard BPT provisions — each concession agreement must be reviewed individually - A flat 5% royalty is referenced in some investment documents for companies already exempt from tax under the Investment Law **AUDIT FLASH POINT:** PSA terms are confidential and concession-specific. Never assume standard BPT applies to petroleum operations without verifying the specific concession agreement. The 30% rate is the statutory fallback, not necessarily the effective rate.  _(Income Tax Act 1986, Schedule; Britacom tax profile)_

### Transfer pricing

- **Transfer pricing** — Sudan does not have formal transfer pricing legislation comparable to OECD guidelines. Related-party transactions should follow arm's length principle as a matter of general tax administration practice. No formal CbCR or TP documentation requirements are currently in force — verify with the Taxation Chamber.  _(verify with the Taxation Chamber)_

### Currency conversion

- **Currency conversion** — Documents or invoices in a currency other than SDG must be converted at the **exchange rate at the time of the transaction**, with the exchange rate used stated.  _(Income Tax Act 1986, Art 39(3-5))_

### Tax exemptions (Schedule 1 and ministerial orders)

- **Tax exemptions** — - Pensions paid to members of municipal services or disciplinary departments - Payments and transfers to envoys, diplomats, and employees of international organizations - Interest from bank deposits, savings accounts, and postal savings funds - Personal income of employees **over 50 years old** working in government or private sectors (capped at highest government salary) - Charitable bodies (Minister may reimburse taxes collected from legally registered charities) - Activities under the **Zakat Act 2001** and **Islamic Endowments Act 1996** are outside the Income Tax Act's scope - Expatriate personnel working on major development projects (oil industry, dams, roads, bridges) may receive tax exemption benefits  _(Income Tax Act 1986, Schedule 1 and ministerial orders)_

### Double taxation treaties

- **Double taxation treaties** — As of January 2024, Sudan has concluded and brought into force double taxation agreements with 17 countries and regions. Verify treaty availability and rates before applying.  _(Britacom tax profile)_

## Section 6 — Worked examples

### Example 1 — Standard manufacturing company

**Scenario:** Khartoum-based manufacturing company with taxable profit of SDG 50,000,000.

- BPT = 50,000,000 x 15% = **SDG 7,500,000**
- Less WHT credits on imports (2%): assume SDG 500,000
- Tax payable = 7,500,000 - 500,000 = **SDG 7,000,000**

### Example 2 — Bank operating in Sudan

**Scenario:** Foreign-owned bank with taxable profit of SDG 200,000,000.

- BPT = 200,000,000 x 30% = **SDG 60,000,000**
- No special deductions apply; bank profits are not eligible for investment incentives
- WHT on interest paid to non-residents: 7% final tax

### Example 3 — Company in a Free Zone (investment incentive)

**Scenario:** Manufacturing company established in a free zone, commenced commercial production in January 2021. Taxable profit SDG 30,000,000 for tax year 2025.

- Investment incentive exemption: 5 years from commercial production (Jan 2021 - Dec 2025)
- Tax year 2025 falls within the exemption period — **BPT = SDG 0**
- Exemption expires Dec 2025; from 2026, standard 15% rate applies
- **AUDIT FLASH POINT:** Maintain a calendar tracking the exemption expiry; the tax position changes dramatically in 2026

### Example 4 — Withholding on payment to non-resident contractor

**Scenario:** Sudanese company pays SDG 10,000,000 to a non-resident technical services provider.

- WHT = 10,000,000 x 15% = **SDG 1,500,000** (final tax on the non-resident)
- The Sudanese company must withhold and remit within the prescribed period
- The non-resident cannot claim the personal allowance on WHT-taxed income

## Section 7 — Self-checks

Before delivering output, verify:

- [ ] Sector rate correctly identified (15% standard, 30% banks/tobacco/petroleum, 0% agriculture)
- [ ] All deductions claimed are on the allowable list (Art 18(1)(A))
- [ ] Bad debts meet all 4 conditions (audited accounts, activity-related, specific value, legal action)
- [ ] Depreciation rates match the First Schedule
- [ ] Free zone exemption period traced to commercial production start date
- [ ] Petroleum operations checked against specific PSA terms (not just the 30% statutory rate)
- [ ] Currency conversions use transaction-date exchange rates
- [ ] Zakat payments are separately claimed and supported by proof of payment
- [ ] Record retention compliance (6 years minimum, Arabic or English)
- [ ] DTA treaty consulted for cross-border payments before applying WHT rates

## Section 8 — Reference material

**Reference material**  _(Section 8 — Reference material)_

| Resource | Reference |
| --- | --- |
| Sudan Taxation Chamber | https://tax.gov.sd/en/income-tax-2/ |
| Income Tax Act 1986 (PDF) | https://tax.gov.sd/wp-content/uploads/2025/02/ — legislation section |
| PwC Worldwide Tax Summaries — Sudan | https://taxsummaries.pwc.com/sudan |
| Britacom tax profile | https://www.britacom.org/zt/BRPolicies/Sudan/ |
| US State Dept Investment Climate Statement | https://www.state.gov/reports/2022-investment-climate-statements/sudan/ |
| Investment Incentive Law 2021 | Ministry of Investment and International Cooperation, Sudan |
| Trading Economics — Sudan corporate tax rate | https://tradingeconomics.com/sudan/corporate-tax-rate |

## PROHIBITIONS

- Do NOT advise on, enable, or overlook tax evasion, under-declaration of profits, or fictitious expenses.
- Do NOT apply a 15% standard rate to banks, tobacco, or petroleum operations without checking the 30% sector rate.
- Do NOT compute petroleum operation tax without reviewing the specific PSA / concession agreement terms.
- Do NOT assume free zone exemption is permanent — it is capped at 5 years from commercial production.
- Do NOT finalise a tax figure when current-year rates cannot be verified against the Sudan Taxation Chamber — give the formula and flag "verify current value."
- Do NOT apply DTA rates without confirming the specific treaty is in force.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, tax attorney, or equivalent licensed practitioner in Sudan) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://www.openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.

**Sources:** Income Tax Act 1986 (Sudan) — tax.gov.sd; PwC Worldwide Tax Summaries — Sudan; Britacom tax profile; Trading Economics; US State Department Investment Climate Statement 2022; Investment Incentive Law 2021.

> Contributed by Ahmed Hassan.

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
