---
name: sd-income-tax
description: Use this skill whenever asked about Sudanese personal income tax for resident individuals, sole proprietors, professionals, and non-residents earning Sudan-source income — to compute, review, or explain it. Trigger on phrases like "Sudan income tax", "Sudan personal tax", "ضريبة الدخل السودان", "Sudan tax brackets", "Sudan PAYE", "Sudan freelance tax", or any request to prepare or check a Sudanese individual income tax return. ALWAYS read this skill before touching any Sudan personal income tax work.
version: 0.1
jurisdiction: SD
tax_year: 2025
last_updated: 2026-07-22
review_status: pending_review
depends_on: - income-tax-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Sudan Personal Income Tax (ضريبة الدخل) Skill v0.1

## Sudan Personal Income Tax (ضريبة الدخل) Skill v0.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

> **Currency note:** All figures are in Sudanese Pounds (SDG — ج.س). Sudan has undergone multiple currency redenominations; verify current SDG values before filing.
> **YMYL — verify before relying.** Sudan's tax legislation has been subject to amendments and the political situation has disrupted tax administration. Where this skill says "verify current value," re-confirm against the Sudan Taxation Chamber (tax.gov.sd), PwC Worldwide Tax Summaries, or a qualified Sudan accountant before filing.

## Section 1 — Scope statement

This skill covers:

- Personal income tax (employment income) rates and progressive brackets
- Self-employed / sole proprietorship income tax (same progressive scale)
- Professional / non-commercial activity income
- Rental income from real estate
- Residence rules and taxation basis (territorial + person principle)
- Personal tax-free allowance (SDG 3,000)
- PAYE withholding and remittance mechanics
- Tax exemptions and special categories

This skill does NOT cover:

- Corporate / Business Profits Tax — see `sd-corporate-income-tax`
- VAT — see `sd-vat-gst`
- Payroll and social insurance contributions — see `sd-payroll-social`
- Company formation — see `sd-company-formation`
- Capital gains tax — separate schedule under Income Tax Act 1986
- Zakat — separate obligation under Zakat Act 2001

## Section 2 — Required inputs and refusal catalogue

### Required inputs

Before starting any Sudan personal income tax work, obtain:

1. **Residency status.** Resident if present in Sudan for **183 days or more** in the base period, or present in Sudan in the period and both preceding periods for 12 months or more, or has taken Sudan as place of residence with intention to settle. *(Income Tax Act 1986, terminology: "Resident")*
2. **Income categories:** employment (salary), business/professional income, rental income, or investment income
3. **Gross income** for the tax year with supporting documents
4. **Deductible expenses** with supporting documentation
5. **Withholding tax already suffered** (PAYE certificates or WHT certificates)
6. **Zakat payment certificate** (Zakat paid is deductible from business profits tax)

### Refusal catalogue

- **R-SD-1** — Do not produce a final filing figure without residency status confirmed.
- **R-SD-2** — Do not deduct an expense lacking documentary support. Disallow it.
- **R-SD-3** — Do not finalise tax using the SDG 3,000 personal allowance without verifying it has not been updated — Sudan's currency redenominations may have changed this figure.
- **R-SD-4** — Refuse to advise on tax evasion or under-declaration of income.
- **R-SD-5** — Do not apply double taxation treaty rates without confirming the specific treaty is in force.
- **R-SD-6** — Do not advise on corporate income tax — this skill is individuals only.
- **R-SD-7** — Do not give a binding figure where current-year bracket/allowance values cannot be verified; provide the formula and flag "verify current value."

## Section 3 — Rates and thresholds

### Personal income tax rates (employment / salary)

Sudan taxes employment income at progressive rates. The top marginal personal income tax rate is **15%** (Trading Economics; Income Tax Act 1986). Some sources cite a range of 5%–20% with 20% being the top rate for non-residents and fringe benefits.

**AUDIT FLASH POINT:** Multiple sources cite different top rates (15% vs 20%). The 15% rate is confirmed by Trading Economics and the Sudan Tax Authority page for residents. The 20% rate appears for non-resident taxpayers and fringe benefits per the Britacom tax profile. Verify the current bracket schedule before filing.

- **Top marginal personal income tax rate** — 15%  _(Trading Economics; Income Tax Act 1986)_

**Personal income tax rate categories**  _(Income Tax Act 1986; Trading Economics; Britacom tax profile)_

| Category | Rate range | Source |
| --- | --- | --- |
| **Resident employment income** | 5% – 15% (progressive) | Income Tax Act 1986; Trading Economics |
| **Non-resident employment income** | 20% (flat) | Income Tax Act 1986; Britacom tax profile |
| **Fringe benefits** | 20% | Income Tax Act 1986; Britacom tax profile |
| **Rental / real-estate income** | 10% | Income Tax Act 1986 (verify current rate) |
| **Sole proprietorship / partnership** | 0% – 20% (progressive) | Income Tax Act 1986; Britacom tax profile |
| **Capital gains (individual)** | 20% | Income Tax Act 1986; Britacom tax profile |

### Personal tax-free allowance (exemption)

- **Personal tax-free allowance** — SDG 3,000 SDG (All resident and non-resident individuals eligible; can offset self-employed ventures, rent income, professional services income)  _(Income Tax Act 1986; Britacom tax profile)_

**Verify current value:** The SDG 3,000 figure predates multiple currency redenominations. Confirm against current Taxation Chamber guidance before filing.

### PAYE withholding

- **PAYE withholding at source** — Employment income tax is **withheld at source by the employer (PAYE)** and remitted monthly  _(Income Tax Act 1986; tax.gov.sd)_
- **PAYE remittance deadline** — On or before the 15th of the month following deduction  _(Income Tax Act 1986; tax.gov.sd)_

### Individual annual return deadline

- **Individual annual return deadline** — As specified in the Income Tax Act; commonly within a set period after year-end (verify current deadline — some sources indicate 30 June)  _(Income Tax Act 1986; tax.gov.sd; taxratesbycountry.com)_

### Conservative defaults

**Conservative defaults**

| Ambiguity | Default |
| --- | --- |
| Unknown residency | Treat as **non-resident** (Sudan-source income only, 20% flat rate) until residency confirmed |
| Unknown whether 15% or 20% applies | Use 15% for residents, 20% for non-residents; flag both |
| Unknown personal allowance current value | Use SDG 3,000 and label "verify current value" |
| Unknown whether an expense is deductible | Treat as **non-deductible** until documentary support confirmed |
| Unknown income category | Default to employment income (most common); verify |

## Section 4 — Computation rules

### Step 1 — Determine residency

- **Resident (individual)** — An individual is **resident** if: (i) Present in Sudan for **183 days or more** in the base period; OR (ii) Present in Sudan in the period and both preceding periods for **12 months or more**; OR Has taken Sudan as their place of residence and shown intention to settle there  _(Income Tax Act 1986, terminology section)_

Residents are taxed on income arising in Sudan AND any place outside Sudan (worldwide for residents). Non-residents are taxed on Sudan-source income only.

### Step 2 — Classify income

**Income classification**

| Income type | Determination rule | Rate treatment |
| --- | --- | --- |
| Employment income | Gross salary + allowances | Progressive 5%-15% (resident) / 20% (non-resident) |
| Business/professional income | Net profit (gross income less deductible expenses) | Progressive 0%-20% (same as sole proprietorship) |
| Rental income | Gross rent less allowable property expenses | 10% |
| Capital gains | Gain on disposal of assets | 20% |
| Interest income (bank deposits) | Exempt | 0% |
| Pensions (government/municipal) | Exempt | 0% |

### Step 3 — Apply personal allowance

- **Taxable income** — Taxable income = Gross income - SDG 3,000 personal allowance (verify current value)

The SDG 3,000 allowance can offset self-employment income, rent income, and professional services income.

### Step 4 — Compute tax on progressive scale

- **Tax (resident employment income)** — For employment income (residents): Tax = Taxable income x applicable progressive rate (5% to 15%)
- **Tax (non-residents and fringe benefits)** — For non-residents and fringe benefits: Tax = Gross income x 20% (flat rate, no allowance — verify)

### Step 5 — Apply credits

- **Tax payable** — Tax payable = Tax computed - PAYE already withheld - WHT credits

## Section 5 — Edge cases and special rules

### Tax exemption categories (Schedule 1, Income Tax Act 1986)

1. **Pensions** paid to members of municipal services or disciplinary departments
2. **Payments and transfers** to envoys, diplomats, and employees of international organizations
3. **Interest** from bank deposits, savings accounts, and postal savings funds
4. **Personal income of employees over 50 years old** working in government or private sectors — provided the tax-exempt income does not exceed the highest salary in the government salary plan (does not include remuneration of board members of government or state-owned enterprises)
5. **Charitable bodies** — the Minister may, after consultation with the Minister of Welfare and Social Insurance, reimburse taxes collected from legally registered charitable bodies
6. **Activities under the Zakat Act 2001** and the **Islamic Endowments Act 1996** are outside the Income Tax Act's scope entirely
7. **Expatriate personnel** working on major development projects (oil industry, dams, roads, bridges) may receive tax exemption benefits

### Residence — non-individual (companies)

- **Resident (non-individual/company)** — For a non-individual (company), **resident** means control and management are exercised directly in Sudan in the period.  _(Income Tax Act 1986)_

### Currency conversion

- **Currency conversion** — Documents or invoices in a currency other than SDG must be converted at the **exchange rate at the time of the transaction**, with the exchange rate used stated.  _(Income Tax Act 1986, Art 39(3-5))_

### Income subject to tax (Art 4, Income Tax Act 1986)

- **Income subject to tax** — Tax is levied for the assessment year on income from the base period arising from: 1. **Sudan** — for residents and non-residents 2. **Any place outside Sudan** — for residents Despite any law granting tax exemption, tax is imposed on profits from commercial activity, which includes: - Business profits - Rental income from real estate - Personal income - Gross income This applies even if the person no longer owns the income source in the assessment year.  _(Art 4, Income Tax Act 1986)_

### Record-keeping

- **Record-keeping** — Every person subject to tax must keep accounting books (manual or electronic) — journal, ledgers, and inventory — plus supporting documents for **not less than 6 years** after the base period, in either **Arabic or English**.  _(Income Tax Act 1986, Art 39(3-5))_

### Self-assessment and penalties

- **Self-assessment additional tax** — Every person under self-assessment must submit their return and pay tax due at the time of filing. If the return is found incorrect after review, an **additional tax not exceeding twice (2x) the amount of tax** determined from the audit may be imposed.  _(Income Tax Act 1986, Art 38(2))_

**AUDIT FLASH POINT:** The 2x penalty for self-assessment under-declaration is significant. Conservative computation is essential; do not finalise aggressive tax positions without professional review.

## Section 6 — Worked examples

### Example 1 — Resident employee, moderate income

**Scenario:** Sudanese resident employee with annual gross salary of SDG 1,200,000.

- Total income: SDG 1,200,000 (employment income)
- Less personal allowance: SDG 3,000 (verify current value)
- Taxable income: SDG 1,197,000
- Tax at progressive rates (assume 15% marginal rate):
  - Lower bands at 5%-10% + remaining at 15% (verify exact bracket schedule)
  - Estimated tax: approximately **SDG 180,000** (verify with current bracket schedule)
- Less PAYE already withheld: depends on monthly withholding
- *Flag: exact bracket computation requires confirmed bracket thresholds — verify current schedule*

### Example 2 — Non-resident consultant

**Scenario:** Non-resident consultant earns SDG 500,000 of Sudan-source professional fees.

- Non-resident rate: 20% flat
- Tax = 500,000 x 20% = **SDG 100,000**
- Personal allowance: typically not available to non-residents (verify)
- WHT may already cover this if payer withheld at source

### Example 3 — Rental income

**Scenario:** Resident landlord receives SDG 600,000 annual rental income.

- Rental income rate: 10%
- Tax = 600,000 x 10% = **SDG 60,000**
- Personal allowance may offset: SDG 60,000 - SDG 3,000 adjustment (verify whether allowance applies to rental)
- *Flag: verify whether the 10% rate is applied to gross rent or net rent after property expenses*

### Example 4 — Sole proprietor (commercial activity)

**Scenario:** Sole proprietor with annual gross receipts of SDG 2,000,000 and documented deductible expenses of SDG 800,000.

- Net profit = 2,000,000 - 800,000 = SDG 1,200,000
- Less personal allowance: SDG 3,000
- Taxable = SDG 1,197,000
- Progressive rates 0%-20% (same as sole proprietorship/partnership schedule)
- Estimated tax: approximately **SDG 200,000** at marginal rates (verify with exact bracket schedule)

### Example 5 — Employee over 50 years old (exemption)

**Scenario:** Government employee, age 55, annual salary SDG 900,000.

- Personal income of employees over 50 working in government sectors is exempt
- Condition: tax-exempt income does not exceed the highest salary in the government salary plan
- Tax = **SDG 0** (if condition met)
- *Flag: verify the "highest salary in the government salary plan" cap for the current year*

## Section 7 — Self-checks

Before delivering output, verify:

- [ ] Residency status confirmed (183-day test or 12-month test)
- [ ] Correct rate applied (15% progressive for resident employment; 20% for non-resident/fringe benefits)
- [ ] Personal allowance of SDG 3,000 applied (verify current value)
- [ ] All exempt income categories checked (pensions, diplomatic, bank interest, over-50 exemption)
- [ ] Rental income correctly classified (10% rate — verify gross vs net)
- [ ] Currency conversions use transaction-date exchange rates
- [ ] PAYE remittance deadline (15th of following month) communicated
- [ ] Record retention compliance noted (6 years minimum, Arabic or English)
- [ ] Self-assessment 2x penalty risk flagged for aggressive positions

## Section 8 — Bank statement reading guide

Sudanese bank statements (كشف حساب) may appear in Arabic or English. Common Sudanese banks:

- **Bank of Khartoum (بنك الخرطوم):** Arabic-first; debit = مدين, credit = دائن
- **Omdurman National Bank (بنك أمدرمان الوطني):** Bilingual
- **Central Bank of Sudan (بنك السودان المركزي):** Regulatory authority

### Key Arabic banking terms

**Key Arabic banking terms**

| Arabic | English |
| --- | --- |
| كشف حساب | bank statement |
| رصيد | balance |
| مدين | debit |
| دائن | credit |
| إيداع | deposit |
| سحب | withdrawal |
| تحويل | transfer |
| مرتب / راتب | salary |
| إيجار | rent |
| فوائد | interest (bank deposit — exempt from income tax) |

## Section 9 — Reference material

**Reference material**  _(Sudan Taxation Chamber; PwC Worldwide Tax Summaries; Trading Economics; Britacom; TaxRatesByCountry)_

| Resource | Reference |
| --- | --- |
| Sudan Taxation Chamber — Income Tax | https://tax.gov.sd/en/income-tax-2/ |
| PwC Worldwide Tax Summaries — Sudan | https://taxsummaries.pwc.com/sudan |
| Trading Economics — Sudan PIT rate | https://tradingeconomics.com/sudan/personal-income-tax-rate |
| Britacom tax profile — Sudan | https://www.britacom.org/zt/BRPolicies/Sudan/ |
| TaxRatesByCountry — Sudan | https://taxratesbycountry.com/tax-rates-in-sudan/ |

## PROHIBITIONS

- Do NOT advise on, enable, or overlook tax evasion or under-declaration of income.
- Do NOT finalise a tax figure when current-year brackets or the personal allowance cannot be verified — give the formula and flag "verify current value."
- Do NOT apply the SDG 3,000 personal allowance without labelling it "verify current value" — currency redenominations may have changed this.
- Do NOT apply DTA rates without confirming the specific treaty is in force.
- Do NOT handle corporate income tax — this skill is individuals only.
- Do NOT present output as a filed return or as professional sign-off.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, tax attorney, or equivalent licensed practitioner in Sudan) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://www.openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.

**Sources:** Income Tax Act 1986 (Sudan) — tax.gov.sd; PwC Worldwide Tax Summaries — Sudan; Trading Economics; Britacom tax profile; TaxRatesByCountry.

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
