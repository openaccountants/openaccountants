---
name: bahrain-income-tax
description: "Use this skill whenever asked about Bahrain personal income tax for individuals or the self-employed. Trigger on phrases like \"how much income tax do I pay in Bahrain\", \"Bahrain personal income tax\", \"self-employed tax Bahrain\", \"do I file a tax return in Bahrain\", \"income tax return Bahrain\", \"tax on salary Bahrain\", \"freelancer tax Bahrain\", \"sole trader tax Bahrain\", or any question about computing or filing personal income tax in the Kingdom of Bahrain. CRITICAL: Bahrain has NO personal income tax regime — no brackets, no rates, no PIT returns, no PIT deadlines. This skill exists to state that clearly and to redirect the user to what actually applies to individuals and the self-employed: Social Insurance (SIO) contributions, the expatriate End-of-Service Benefit (EOSB) funded scheme, VAT at 10% for business/self-employed turnover, the Wage Protection System (WPS), and corporate-level taxes (DMTT / hydrocarbon). ALWAYS read this skill before touching any Bahrain \"income tax\" work."
jurisdiction: BH
domain: international
tax_year: 2026
tier: 2
last_updated: 2026-07-06
---

# bahrain-income-tax

## Bahrain Personal Income Tax -- Self-Employed Skill v0.1

> **HEADLINE: Bahrain has NO personal income tax.** There is no PIT regime of any kind — no brackets, no rates, no personal tax return, no PIT filing deadline, and no PIT payment obligation — for any individual, whether employed, self-employed, resident, or non-resident. Income and capital gains earned outside Bahrain are likewise not taxed in Bahrain. There is no net-wealth tax, no estate/inheritance/gift tax, and no individual capital gains tax. (Source: PwC Tax Summaries — Bahrain Individual, last reviewed 11 Jan 2026, https://taxsummaries.pwc.com/bahrain/individual/taxes-on-personal-income and .../other-taxes.)
>
> This skill therefore does NOT compute income tax. It documents what DOES apply to an individual or self-employed person in Bahrain: **Social Insurance (SIO)** contributions, the expatriate **End-of-Service Benefit (EOSB)** funded scheme, **VAT** for business/self-employed turnover, the **Wage Protection System (WPS)**, and the **corporate-level taxes** that may reach a self-employed person who incorporates.

## Section 1 -- Quick Reference

**Quick Reference table**

| Field | Value |
| --- | --- |
| Country | Kingdom of Bahrain |
| Personal income tax | **NONE — no PIT regime exists** (PwC, reviewed 11 Jan 2026) |
| Currency | Bahraini Dinar (BHD) only |
| Tax year | Calendar year (1 January -- 31 December) |
| PIT legislation | **None** — there is no personal income tax statute |
| What actually applies | Social Insurance (SIO) contributions; expat EOSB scheme; VAT (self-employed/business); Wage Protection System (WPS); corporate DMTT / hydrocarbon tax |
| Social insurance authority | Social Insurance Organisation (SIO, formerly GOSI), https://www.sio.gov.bh |
| VAT / tax authority | National Bureau for Revenue (NBR), https://www.nbr.gov.bh |
| Payroll compliance authority | Labour Market Regulatory Authority (LMRA), https://www.lmra.gov.bh |
| PIT filing deadline | **N/A — no personal income tax return exists** |
| SIO remittance frequency | Monthly (employer withholds and remits) |
| VAT filing frequency | Quarterly (most businesses); monthly for large businesses |
| Validated by | Pending — requires sign-off by a Bahrain-qualified tax/payroll professional |
| Validation date | Pending |
| Skill version | 0.1 |

### Personal Income Tax Rate Table

**Personal Income Tax Rate Table**

| Taxable Income (BHD) | Rate |
| --- | --- |
| All income, any amount | **0% — there is no personal income tax in Bahrain** (PwC, reviewed 11 Jan 2026) |

- **No brackets/allowance/PIT computation** — There are no brackets, no personal allowance, and no PIT computation. Any request to "compute Bahrain personal income tax" must return BHD 0 PIT, with the explanation that no PIT regime exists, and then redirect to SIO / VAT / WPS as relevant.

### Social Insurance (SIO) Contribution Rates -- Bahraini Nationals (Private Sector)

**SIO rates -- Bahraini Nationals**

| Component | Employee | Employer (2025) | Employer (2026) |
| --- | --- | --- | --- |
| Pension / retirement | 7% | (part of total) | (part of total) |
| Unemployment | 1% | (incl.) | (incl.) |
| Work injury | -- | (incl.) | (incl.) |
| **TOTAL** | **8%** | **17%** | **18%** |

- **Employee total unchanged through phase-in** — Employee total = **8%** (7% pension + 1% unemployment), unchanged through the phase-in.  _((newsofbahrain.com/106412; meinsurancereview.com aid=49089))_
- **Employer phase-in schedule** — Employer total = **17% from January 2025**, rising to **18% from 1 January 2026**, then **+1% per year until it reaches 21% in 2028**.  _((newsofbahrain.com/106412; mercans.com EOSB/social-security alert 2026))_
- **Combined rate note** — Combined (employer + employee): **25% in 2025** (17% + 8%) → **26% in 2026** (18% + 8%). PwC's individual "other taxes" page (reviewed 11 Jan 2026) cites the 2025 snapshot of 17%/8%; for 2026 use the 18% employer figure.  _(https://taxsummaries.pwc.com/bahrain/individual/other-taxes)_
- **Insurable-earnings ceiling** — BHD 4,000 per month — contributions are computed on a salary capped at BHD 4,000/month.  _((newsofbahrain.com/106412))_
- **Contribution floor / minimum insurable wage** — **[RESEARCH GAP — reviewer to confirm]** (only the BHD 4,000 ceiling is well-sourced).

### Social Insurance (SIO) Contribution Rates -- Expatriate (Non-GCC) Employees

**SIO rates -- Expatriate (Non-GCC) Employees**

| Component | Employee | Employer | Total |
| --- | --- | --- | --- |
| Work injury (only branch covered) | 1% | 3% | **4%** |
| **TOTAL** | **1%** | **3%** | **4%** |

- **Work-injury only coverage** — Expats are covered for the **work-injury branch only** — no pension, no unemployment.  _((https://taxsummaries.pwc.com/bahrain/individual/other-taxes; newsofbahrain.com/106412))_
- **GCC nationals use home-country rates** — **GCC nationals** working in Bahrain contribute at **their home country's** social-security rates under the GCC unified extension/insurance protection scheme — NOT Bahrain's rates.  _((https://taxsummaries.pwc.com/bahrain/individual/other-taxes))_

### Expatriate End-of-Service Benefit (EOSB) -- Funded SIO Scheme (effective 1 March 2024)

**EOSB Funded Scheme rates**

| Service period | Monthly contribution rate | Equivalent |
| --- | --- | --- |
| First 3 years of service | **4.2% of monthly wage** | ≈ 0.5 month's salary per year |
| Beyond 3 years of service | **8.4% of monthly wage** | ≈ 1 month's salary per year |

- **Replacement of lump-sum gratuity** — The traditional lump-sum expat gratuity was replaced by this funded, SIO-administered monthly contribution from 1 March 2024.  _((mercans.com EOSB alert; SIO EOSB page https://www.sio.gov.bh/en/end-of-service-benefits))_

### VAT (National Bureau for Revenue -- NBR), for self-employed / business activity

**VAT table**

| Field | Value |
| --- | --- |
| Standard rate | **10%** (raised from 5% effective 1 January 2022) (bh.bh business-vat_en; avalara VAT rates) |
| Mandatory registration threshold | Annual taxable supplies **> BHD 37,500** (bh.bh business-vat_en; NBR portal) |
| Voluntary registration | Annual taxable supplies **BHD 18,750 -- 37,500** (NBR VAT General Guide) |
| Filing frequency | **Quarterly** (most); **monthly** for large businesses (typically annual supplies > BHD 3,000,000 — confirm: **[RESEARCH GAP — reviewer to confirm exact trigger]**) (NBR VAT General Guide) |
| Filing & payment deadline | Within **30 days** / by the last day of the month following the end of each tax period (NBR VAT General Guide) |

### Conservative Defaults

**Conservative Defaults table**

| Ambiguity | Default |
| --- | --- |
| "Compute my Bahrain personal income tax" | Return **BHD 0 PIT** and explain no PIT regime exists; redirect to SIO/VAT/WPS |
| Unknown nationality (for SIO) | STOP — SIO rate depends on Bahraini / non-GCC expat / GCC national; do not apply a rate without it |
| Unknown whether wage exceeds SIO ceiling | Apply the **BHD 4,000/month** ceiling to insurable earnings |
| Unknown SIO year (employer rate) | Use the **year-specific** rate (17% for 2025, 18% for 2026); never average |
| Unknown self-employed turnover vs VAT threshold | Treat as below threshold (no mandatory VAT) but flag to confirm against BHD 37,500 |
| Unknown VAT registration status | Assume not registered until confirmed; do not net out VAT |
| Request for corporate / hydrocarbon / DMTT computation | Out of scope for this individual skill — escalate |

## Section 2 -- Required Inputs and Refusal Catalogue

### Required Inputs

- **Minimum viable inputs** — **Minimum viable** -- confirmation of what is actually being asked. If the user asks for "income tax", the minimum is simply the statement that Bahrain has no PIT. For any SIO/payroll question: nationality category (Bahraini / non-GCC expat / GCC national), gross monthly wage, and the relevant year (2025 vs 2026 employer rate differs). For VAT: annual taxable turnover and VAT registration status.
- **Recommended documents** — **Recommended** -- payslips or payroll register, SIO contribution statements, bank statement for the tax year (CSV, PDF, or pasted text), and VAT registration certificate if registered.
- **Ideal documents** — **Ideal** -- full payroll run with SIO splits, EOSB accrual schedule, VAT returns for the period, and any corporate accounts if the individual has incorporated.
- **Refusal if minimum missing** — **Refusal if minimum is missing -- SOFT WARN.** For a pure "income tax" question, no documents are needed — the answer is that no PIT exists. For SIO/VAT work, missing nationality or year = proceed only with an explicit reviewer warning that the figures are provisional.

### Refusal Catalogue

- **R-BH-1** — Personal income tax computation requested. "Bahrain has no personal income tax. There are no brackets, no rates, and no return to file. The personal income tax due is BHD 0. The recurring obligations that DO apply to individuals are Social Insurance (SIO) contributions and, for business/self-employed activity, VAT. Let me redirect you to the relevant section."  _(R-BH-1)_
- **R-BH-2** — Nationality category unknown (SIO). "Social Insurance contribution rates differ by nationality: Bahraini nationals (8% employee / 17% employer in 2025, 18% in 2026), non-GCC expatriates (1% employee / 3% employer, work-injury only), and GCC nationals (home-country rates). This skill cannot compute SIO without knowing which category applies."  _(R-BH-2)_
- **R-BH-3** — Corporate / hydrocarbon / DMTT computation. "Corporate-level taxes — the 46% hydrocarbon tax and the 15% Domestic Minimum Top-up Tax (DMTT) for large MNE groups — are out of scope for this individual skill. Escalate to a Bahrain corporate tax specialist."  _(R-BH-3)_
- **R-BH-4** — Detailed VAT return preparation. "This skill covers personal/individual matters and only summarises VAT. For full Bahrain VAT return preparation, use the bahrain-vat skill."  _(R-BH-4)_
- **R-BH-5** — Foreign / cross-border income taxation. "Bahrain does not tax foreign income of individuals, but the foreign jurisdiction may. Cross-border and treaty analysis is out of scope. Escalate to a qualified professional."  _(R-BH-5)_
- **R-BH-6** — VAT penalty exposure / NBR enforcement. "The VAT penalty figures available here are from a secondary advisory and are flagged as unverified. Do not advise on enforcement exposure. Escalate to a qualified professional and confirm against the NBR penalty schedule."  _(R-BH-6)_

## Section 3 -- Transaction Pattern Library

This is the deterministic pre-classifier. Because Bahrain has no PIT, there is no income-tax return to populate — there are **no PIT boxes**. The purpose of classifying transactions here is to identify (a) business revenue relevant to the **VAT** threshold, (b) **SIO** contribution movements, (c) **EOSB** contributions, and (d) items to exclude. Match by case-insensitive substring on the counterparty/description as it appears in the bank statement. If multiple patterns match, use the most specific. If none match, fall through to Tier 1 rules in Section 5.

### 3.1 Income Patterns (Credits on Bank Statement)

**Income Patterns table**

| Pattern | Tag | Treatment | Notes |
| --- | --- | --- | --- |
| Client name + TRANSFER, DEPOSIT, PAYMENT RECEIVED | Business revenue (VAT-relevant) | Count toward VAT turnover | NOT subject to PIT. If VAT-registered, gross includes 10% VAT |
| FEES, PROFESSIONAL FEES, CONSULTANCY, ATAAB (fees) | Business revenue | Count toward VAT turnover | Typical self-employed receipt |
| STRIPE PAYOUT, PAYPAL PAYOUT, WISE PAYOUT, PAYTABS | Platform payout | Count toward VAT turnover | Match to underlying invoices |
| UPWORK, FIVERR, TOPTAL | Freelance platform | Count toward VAT turnover | Net of platform commission |
| RATIB, SALARY, EMPLOYER [name] | Employment income | NOT taxed (no PIT) | Note: SIO contributions are deducted at payroll |
| EJAR, RENT RECEIVED | Rental income | NOT taxed (no PIT) | No individual income tax on rent |
| FAWA'ID, INTEREST RECEIVED | Investment income | NOT taxed (no PIT) |  |
| ARBAH, DIVIDEND | Investment income | NOT taxed (no PIT) |  |
| NBR REFUND, VAT REFUND | EXCLUDE | Not income | VAT refund from NBR |
| TAMKEEN, GOVERNMENT GRANT, SUBSIDY | Check nature | May count toward VAT turnover if a taxable supply | Verify grant nature |

### 3.2 Expense / Payroll Patterns (Debits on Bank Statement)

**Expense/Payroll Patterns table**

| Pattern | Tag | Treatment | Notes |
| --- | --- | --- | --- |
| SIO, GOSI, SOCIAL INSURANCE, TA'MINAT | SIO contribution | Statutory contribution (not PIT) | Employer + employee split; capped at BHD 4,000/month wage |
| EOSB, END OF SERVICE, SIO EOSB | EOSB contribution | Statutory expat scheme | 4.2% first 3 yrs / 8.4% thereafter |
| NBR VAT, VAT PAYMENT | VAT remittance | EXCLUDE (not an expense) | Net VAT paid to NBR |
| WPS, WAGE PROTECTION, LMRA WPS | Payroll routing | Compliance routing, not a tax | Wages must flow through WPS |
| LMRA, WORK PERMIT, FEES LMRA | Labour fees | Business cost | Work-permit / LMRA fees |
| OFFICE RENT, EJAR MAKTAB | Business cost | Business expense (no PIT relief — informational only) | No income tax to deduct against |
| ACCOUNTANT, AUDITOR, BOOKKEEP | Business cost | Business expense (informational) |  |
| SOFTWARE, SUBSCRIPTION, ANTHROPIC, OPENAI, GITHUB | Business cost | Business expense (informational) |  |
| PERSONAL, GROCERIES, SUPERMARKET, LULU, CARREFOUR | Personal | EXCLUDE | Private living costs |
| INTERNAL TRANSFER, OWN ACCOUNT | EXCLUDE | Own-account transfer |  |

- **Deductibility not a PIT concept** — > **Important:** Because there is no PIT, "deductibility" of business expenses is **not** a personal income tax concept in Bahrain. Expense classification here matters only for VAT input recovery (if VAT-registered) and for corporate accounts (if incorporated). Do not present any expense as reducing a personal income tax bill — there is none.

### 3.3 Bahraini Banks -- Statement Format Reference

**Bahraini Banks table**

| Bank | Common Patterns | Notes |
| --- | --- | --- |
| Bank of Bahrain and Kuwait (BBK) | TRANSFER, DD, SO, CHARGES | PDF/CSV; date format DD/MM/YYYY |
| National Bank of Bahrain (NBB) | PAYMENT, TRF, FEE | PDF/CSV; counterparty in description |
| Ahli United Bank (AUB) | TRANSFER, DIRECT DEBIT, CHARGE | PDF; CSV available |
| Bahrain Islamic Bank (BisB) | MURABAHA, TRANSFER, FEE | Islamic-finance terminology |
| Benefit / BenefitPay | POS, TRANSFER, BILL | Domestic payment network; clean counterparty names |

## Section 4 -- Worked Examples

### Example 1 -- "How much income tax do I owe on my Bahrain salary?"

**Input line:**
`25/03/2026 ; NBB CREDIT ; EMPLOYER GULF TECH WLL ; RATIB MARCH ; +1,500.000 ; BHD`

**Reasoning:**
This is salary. Bahrain has no personal income tax, so the income tax due is BHD 0 regardless of amount. What IS deducted at payroll is the employee's SIO contribution. If the individual is a Bahraini national, employee SIO = 8% of insurable wage (capped at BHD 4,000/month). On BHD 1,500: 8% × 1,500 = **BHD 120.000** employee SIO. (PwC; newsofbahrain.com/106412)

**Classification:** PIT = **BHD 0** (no regime). Employee SIO (Bahraini national) = **BHD 120.000**.

### Example 2 -- Bahraini national, salary above the SIO ceiling (2026)

**Input line:**
`25/04/2026 ; BBK CREDIT ; EMPLOYER MANAMA HOLDING BSC ; SALARY APR ; +5,000.000 ; BHD`

**Reasoning:**
Salary BHD 5,000 exceeds the insurable-earnings ceiling of BHD 4,000/month, so contributions are computed on BHD 4,000, not BHD 5,000. (newsofbahrain.com/106412)
- Employee SIO (Bahraini national) = 8% × 4,000 = **BHD 320.000**.
- Employer SIO 2026 = 18% × 4,000 = **BHD 720.000**. (mercans.com 2026 alert)
- Personal income tax = **BHD 0** (no PIT). (PwC, reviewed 11 Jan 2026)

**Classification:** PIT = BHD 0; employee SIO = BHD 320.000; employer SIO = BHD 720.000 (both on the BHD 4,000 capped wage).

### Example 3 -- Non-GCC expatriate employee

**Input line:**
`25/05/2026 ; AUB CREDIT ; EMPLOYER DESERT LOGISTICS WLL ; SALARY MAY ; +900.000 ; BHD`

**Reasoning:**
Non-GCC expatriate. SIO covers the work-injury branch only: employee 1%, employer 3%. (PwC; newsofbahrain.com/106412)
- Employee SIO = 1% × 900 = **BHD 9.000**.
- Employer SIO = 3% × 900 = **BHD 27.000**.
- EOSB (assume within first 3 years of service) = 4.2% × 900 = **BHD 37.800** (employer-funded, paid to SIO). (mercans.com EOSB alert)
- Personal income tax = **BHD 0** (no PIT).

**Classification:** PIT = BHD 0; employee SIO = BHD 9.000; employer SIO = BHD 27.000; EOSB = BHD 37.800.

### Example 4 -- Self-employed consultant, VAT threshold check

**Input line (illustrative annual total):**
Annual taxable receipts from consulting = BHD 42,000 across the year.

**Reasoning:**
There is no personal income tax on the BHD 42,000 of self-employment income. (PwC) However, annual taxable supplies exceed the mandatory VAT registration threshold of **BHD 37,500**, so the consultant **must register for VAT** with the NBR and charge VAT at 10%. (bh.bh business-vat_en; NBR portal)
- Income tax due = **BHD 0**.
- VAT obligation = **mandatory registration** (turnover > BHD 37,500); charge 10% on taxable supplies; file quarterly; pay within 30 days of period end.

**Classification:** PIT = BHD 0; VAT = mandatory registration triggered.

### Example 5 -- Self-employed freelancer below VAT threshold

**Input line (illustrative annual total):**
Annual taxable receipts from freelancing = BHD 20,000.

**Reasoning:**
No personal income tax (BHD 0). Annual supplies of BHD 20,000 are below the mandatory threshold of BHD 37,500 but within the voluntary band of BHD 18,750 -- 37,500, so VAT registration is **optional, not required**. (NBR VAT General Guide)

**Classification:** PIT = BHD 0; VAT = voluntary registration available, not mandatory.

### Example 6 -- SIO contribution debit on statement (exclude from any tax computation)

**Input line:**
`28/02/2026 ; BBK DD ; SIO CONTRIBUTION ; FEB PAYROLL ; -440.000 ; BHD`

**Reasoning:**
This is a statutory social-insurance remittance, not a tax and not a PIT-relevant expense. It does not reduce any personal income tax because none exists. Record it as a payroll/SIO movement only.

**Classification:** SIO contribution (payroll). PIT impact = none (BHD 0 regime).

## Section 5 -- Tier 1 Rules (When Data Is Clear)

### 5.1 No Personal Income Tax

- **No personal income tax rule** — There is no personal income tax in Bahrain. Any PIT computation returns **BHD 0**. There is no PIT return, no PIT deadline, no personal allowance, and no concept of "chargeable income" or "allowable deductions" for personal income tax purposes. Do not invent brackets.  _(PwC Tax Summaries — Bahrain Individual, reviewed 11 Jan 2026 (https://taxsummaries.pwc.com/bahrain/individual/taxes-on-personal-income))_

### 5.2 No Wealth, Estate, or Capital Gains Tax on Individuals

- **No wealth/estate/CGT rule** — No net-wealth/net-worth tax, no estate/inheritance/gift tax, and no individual capital gains tax. Foreign-source income and gains of residents or non-residents are not taxed in Bahrain.  _(PwC Tax Summaries — Bahrain Individual "Other taxes", reviewed 11 Jan 2026 (https://taxsummaries.pwc.com/bahrain/individual/other-taxes))_

### 5.3 Social Insurance (SIO) -- Bahraini Nationals

**SIO Bahraini Nationals table**  _(PwC; newsofbahrain.com/106412; mercans.com 2026 alert)_

| Item | Value |
| --- | --- |
| Employee contribution | 8% (7% pension + 1% unemployment) |
| Employer contribution (2025) | 17% |
| Employer contribution (2026) | 18% |
| Phase-in | +1%/year to 21% by 2028 |
| Insurable-earnings ceiling | BHD 4,000/month |
| Insurable-earnings floor | **[RESEARCH GAP — reviewer to confirm]** |

- **Contributions computed on capped earnings** — Contributions are computed on insurable earnings capped at BHD 4,000/month and remitted monthly by the employer.  _(PwC; newsofbahrain.com/106412; mercans.com 2026 alert)_

### 5.4 Social Insurance (SIO) -- Non-GCC Expatriates

- **Work-injury only branch** — Work-injury branch only: employee 1%, employer 3% (total 4%). No pension, no unemployment.  _(PwC; newsofbahrain.com/106412)_

### 5.5 Social Insurance (SIO) -- GCC Nationals

- **Home-country rates for GCC nationals** — GCC nationals working in Bahrain contribute at their **home country's** social-security rates under the GCC unified insurance-protection scheme, not Bahrain's rates.  _(PwC)_

### 5.6 Expatriate End-of-Service Benefit (EOSB)

- **EOSB funded scheme rule** — Funded SIO scheme effective 1 March 2024: 4.2% of monthly wage for the first 3 years of service, then 8.4% beyond 3 years. Replaces the traditional lump-sum gratuity for expats.  _(mercans.com EOSB alert; SIO EOSB page (https://www.sio.gov.bh/en/end-of-service-benefits))_

### 5.7 VAT for Self-Employed / Business Activity

**VAT table (Section 5.7)**  _(NBR (https://www.nbr.gov.bh); bh.bh business-vat_en; avalara VAT rates)_

| Item | Value |
| --- | --- |
| Standard rate | 10% (since 1 January 2022) |
| Mandatory registration | Annual taxable supplies > BHD 37,500 |
| Voluntary registration | BHD 18,750 -- 37,500 |
| Filing | Quarterly (monthly for large businesses) |
| Deadline | Within 30 days of period end |

- **VAT as principal recurring obligation** — VAT is the principal recurring tax obligation for a self-employed person whose turnover crosses the threshold. It is administered separately from any (non-existent) income tax.  _(NBR (https://www.nbr.gov.bh); bh.bh business-vat_en; avalara VAT rates)_

### 5.8 Wage Protection System (WPS)

- **WPS compliance rule** — All private-sector wages must be paid through CBB-licensed banks / approved payment service providers and registered with LMRA so payments are documented and timely. Enhanced WPS ("WPS 2.0") becomes mandatory for all private-sector employers from early 2026 (phased rollout). This is a payroll-compliance regime, not a tax.  _(LMRA Resolution (68) of 2019, effective 11 July 2019 (https://www.lmra.gov.bh/en/page/show/631, .../638); KPMG enhanced-WPS alert (kpmg.com flash-alert 2025-262))_

### 5.9 Minimum Wage

- **No private-sector minimum wage** — There is **no statutory minimum wage in the private sector** for either Bahraini nationals or expatriates. A BHD 300/month minimum applies **only to Bahraini nationals in the public/government sector**.  _(truein.com/gcc-blogs/bahrain-employment-laws; minimum-wage.org/international/bahrain)_

### 5.10 Corporate-Level Taxes (context for incorporated self-employed)

**Corporate-Level Taxes table**  _(PwC Tax Summaries — Bahrain Corporate, reviewed 11 Jan 2026 (https://taxsummaries.pwc.com/bahrain/corporate/taxes-on-corporate-income); EY DMTT alert (ey.com Bahrain DMTT))_

| Tax | Rate | Who it hits |
| --- | --- | --- |
| General corporate income tax | None | — |
| Hydrocarbon / oil & gas | 46% of net profits per accounting period | Companies extracting/refining fossil fuels in Bahrain |
| Domestic Minimum Top-up Tax (DMTT) | 15% minimum effective rate | MNE groups with global consolidated revenue ≥ €750m in ≥2 of the preceding 4 fiscal years; effective for fiscal years beginning on/after 1 January 2025; excludes purely domestic businesses; administered by NBR |

## Section 6 -- Tier 2 Catalogue (Reviewer Judgement Required)

### 6.1 SIO Year and Rate Selection

- **Year-specific rate confirmation** — The employer SIO rate is **year-specific** (17% in 2025, 18% in 2026, rising to 21% by 2028). Confirm the period of the payroll run before applying a rate. **Flag for reviewer:** confirm which calendar year's employer rate applies, especially for payrolls straddling 1 January.

### 6.2 Nationality Classification for SIO

- **Nationality classification** — Bahraini national vs non-GCC expat vs GCC national drives entirely different rates. GCC nationals use home-country rates. **Conservative default:** STOP — do not compute SIO without confirmed nationality category. **Flag for reviewer:** confirm nationality and, for GCC nationals, the applicable home-country regime.

### 6.3 EOSB Service-Length Tier

- **EOSB tier apportionment** — 4.2% applies to the first 3 years; 8.4% thereafter. Mixed-tier years require apportionment. **Flag for reviewer:** confirm start date of service and whether the 3-year boundary is crossed during the period.

### 6.4 VAT Registration Threshold Timing

- **VAT threshold timing test** — Mandatory registration is triggered by crossing BHD 37,500 of annual taxable supplies; the precise look-back/forward test should be confirmed against the NBR VAT registration guide (updated Sept 2025, vatupdate.com). **Flag for reviewer:** confirm whether the threshold is breached on a rolling or projected basis.

### 6.5 VAT Monthly-Filing Trigger

- **Monthly filing trigger research gap** — Large businesses file monthly; the commonly cited trigger is annual supplies above BHD 3,000,000. **[RESEARCH GAP — reviewer to confirm exact trigger against the NBR VAT General Guide.]**

### 6.6 VAT Penalties

- **VAT penalties research gap** — Late registration penalty up to BHD 10,000; other non-compliance BHD 500 -- 20,000; late filing/payment 5% -- 25% of VAT due. These come from a **secondary advisory (ecabahrain.com)**, not an NBR primary page. **[RESEARCH GAP — reviewer to confirm against the NBR penalty schedule.]**

### 6.7 Municipal Tax on Expat Rentals

- **Municipal tax research gap** — A municipal tax (commonly cited as ~10%) may apply to rental of property occupied by expatriates. **[RESEARCH GAP — reviewer to confirm the exact rate against the PwC corporate "other taxes" page.]**  _(https://taxsummaries.pwc.com/bahrain/corporate/other-taxes)_

### 6.8 Incorporation Decision

- **Incorporation decision guidance** — A self-employed person who incorporates does not generally face corporate income tax (none exists) but may be exposed to DMTT only if part of a large MNE group, or to hydrocarbon tax only in that sector. **Flag for reviewer:** confirm whether any corporate-level tax could apply before advising on incorporation.

## Section 7 -- Excel Working Paper Template

```
BAHRAIN INDIVIDUAL / SELF-EMPLOYED -- WORKING PAPER
Tax Year: 2026
Client: ___________________________
Nationality category: Bahraini / Non-GCC expat / GCC national
Status: Employed / Self-employed / Both

A. PERSONAL INCOME TAX
  A1. Personal income tax due ................... BHD 0.000
      (Bahrain has NO personal income tax regime)

B. SOCIAL INSURANCE (SIO) -- per month
  B1. Gross monthly wage ........................ ___________
  B2. Insurable wage (lesser of B1 and 4,000) ... ___________
  B3. Employee rate (8% Bahraini / 1% expat) .... ___________
  B4. Employee SIO (B2 x B3) .................... ___________
  B5. Employer rate (18% Bahraini 2026 /
      3% expat) ................................. ___________
  B6. Employer SIO (B2 x B5) .................... ___________

C. EXPATRIATE EOSB (if applicable)
  C1. Service length tier (4.2% <=3yr / 8.4%) ... ___________
  C2. EOSB contribution (B1 x C1) .............. ___________

D. VAT (self-employed / business)
  D1. Annual taxable supplies .................. ___________
  D2. Registration status:
       > 37,500 = MANDATORY
       18,750-37,500 = VOLUNTARY
       < 18,750 = not eligible .................. ___________
  D3. VAT rate (10%) ........................... ___________
  D4. Output VAT on taxable supplies ........... ___________

E. WPS COMPLIANCE
  E1. Wages routed through CBB-licensed bank? ... Y / N
  E2. Registered with LMRA? ..................... Y / N

REVIEWER FLAGS:
  [ ] Confirmed: no PIT applies (output is BHD 0)?
  [ ] Nationality category confirmed for SIO?
  [ ] Correct SIO year/rate applied (17% 2025 / 18% 2026)?
  [ ] BHD 4,000 insurable ceiling applied?
  [ ] EOSB service-length tier correct?
  [ ] VAT threshold (37,500 / 18,750) tested?
  [ ] WPS routing confirmed?
  [ ] Any corporate DMTT/hydrocarbon exposure ruled out?
```

## Section 8 -- Bank Statement Reading Guide

### Bahraini Bank Statement Formats

**Bank Statement Formats table**

| Bank | Format | Key Fields | Notes |
| --- | --- | --- | --- |
| Bank of Bahrain and Kuwait (BBK) | PDF, CSV | Date, Description, Debit, Credit, Balance | Most common; description holds counterparty + reference |
| National Bank of Bahrain (NBB) | PDF, CSV | Value Date, Description, Amount, Balance | Card transactions show merchant |
| Ahli United Bank (AUB) | PDF, CSV | Date, Particulars, Withdrawals, Deposits |  |
| Bahrain Islamic Bank (BisB) | PDF | Date, Description, Amount | Islamic-finance terms (murabaha, etc.) |
| Benefit / BenefitPay | CSV | Date, Counterparty, Amount, Reference | Domestic payment network; clean names |

- **Currency decimal note** — > **Currency note:** the Bahraini Dinar (BHD) is quoted to **three decimal places** (fils). 1 BHD = 1,000 fils. Always carry three decimals in computations and outputs.

### Key Arabic / Bahraini Banking Terms

**Arabic/Bahraini Banking Terms table**

| Term | English | Classification Hint |
| --- | --- | --- |
| RATIB / راتب | Salary | Employment receipt (no PIT; SIO deducted) |
| TAHWEEL / TRF | Transfer | Check direction for revenue/expense |
| KHASM MUBASHIR / DD | Direct debit | Regular expense (utility, SIO, subscription) |
| EJAR / إيجار | Rent | Rental income (no PIT) or office-rent expense |
| FAWA'ID / فوائد | Interest | Interest income (no PIT) or bank charge |
| ARBAH / أرباح | Dividend / profit | Investment income (no PIT) |
| TA'MINAT / تأمينات | Social insurance | SIO contribution (payroll, not a tax) |
| RUSUM / رسوم | Fees / charges | Bank or government fee |
| BENEFIT / POS | Card payment | Expense — check merchant |

## Section 9 -- Onboarding Fallback

If the user asks about "income tax" or provides a bank statement but cannot answer onboarding questions immediately:

1. State plainly that **Bahrain has no personal income tax** — the PIT answer is BHD 0, with no return to file.
2. Classify transactions using the pattern library (Section 3) to surface SIO, EOSB, and VAT-relevant items.
3. Mark all Tier 2 items as "PENDING -- reviewer must confirm".
4. Apply conservative defaults (Section 1).
5. Generate the working paper (Section 7) with clear flags.
6. Present the following questions to the client:

```
ONBOARDING QUESTIONS -- BAHRAIN INDIVIDUAL / SELF-EMPLOYED
1. Are you asking about income tax? (Note: Bahrain has none — PIT = BHD 0.)
2. Nationality category: Bahraini national, non-GCC expatriate, or GCC national?
3. Are you employed, self-employed, or both?
4. Gross monthly wage (for SIO)? Which year does it relate to (2025 or 2026)?
5. If expatriate: start date of service (for EOSB 4.2% vs 8.4% tier)?
6. Self-employed: what is your annual taxable turnover (for VAT threshold)?
7. Are you VAT-registered with the NBR? Mandatory (>37,500) or voluntary?
8. Are wages routed through a CBB-licensed bank and registered with LMRA (WPS)?
9. Have you incorporated, and if so is your group large enough for DMTT?
```

## Section 10 -- Reference Material

### Key Authority References

**Key Authority References table**

| Topic | Reference |
| --- | --- |
| No personal income tax | PwC Tax Summaries — Bahrain Individual, reviewed 11 Jan 2026 (https://taxsummaries.pwc.com/bahrain/individual/taxes-on-personal-income) |
| No wealth/estate/CGT on individuals | PwC Tax Summaries — Bahrain Individual "Other taxes", reviewed 11 Jan 2026 (https://taxsummaries.pwc.com/bahrain/individual/other-taxes) |
| SIO rates (locals 8%/17%; expats 1%/3%; GCC home-country) | PwC; newsofbahrain.com/106412; mercans.com 2026 alert |
| SIO ceiling BHD 4,000/month; employer phase-in to 21% by 2028 | newsofbahrain.com/106412; meinsurancereview.com aid=49089 |
| SIO employer 18% from 1 Jan 2026 | mercans.com EOSB/social-security alert |
| Expat EOSB 4.2% / 8.4% (from 1 Mar 2024) | mercans.com EOSB alert; SIO EOSB page (https://www.sio.gov.bh/en/end-of-service-benefits) |
| VAT 10% (since 1 Jan 2022); threshold BHD 37,500 | bh.bh business-vat_en; NBR portal; avalara VAT rates |
| VAT voluntary band BHD 18,750-37,500; quarterly/monthly; 30-day deadline | NBR VAT General Guide; ecabahrain.com (secondary) |
| VAT registration guide update (Sept 2025) | vatupdate.com 2025/09/24 |
| WPS (Resolution 68 of 2019); enhanced WPS early 2026 | LMRA pages 631/638; KPMG flash-alert 2025-262 |
| No private-sector minimum wage; BHD 300 public sector only | truein.com; minimum-wage.org/international/bahrain |
| Corporate hydrocarbon 46%; DMTT 15% from FY2025 | PwC Corporate, reviewed 11 Jan 2026; EY DMTT alert |

### Why There Are No "Tax Boxes"

Unlike most jurisdictions in this library, Bahrain has no personal income tax return, so this skill does not map transactions to return boxes. The deterministic outputs are instead: (1) PIT = BHD 0 always; (2) SIO employee/employer contributions; (3) EOSB contributions; (4) VAT registration status and output VAT. Treat any tool or prompt that expects a "chargeable income" or "tax due" field by returning zero for PIT and routing the substantive figures to SIO/VAT.

### Test Suite

**Test 1 -- Personal income tax on any salary.**
Input: Resident individual, salary BHD 60,000/year.
Expected: Personal income tax = **BHD 0** (no PIT regime). No return to file.

**Test 2 -- Bahraini national employee SIO (within ceiling, 2026).**
Input: Bahraini national, monthly wage BHD 1,500, year 2026.
Expected: Employee SIO = 8% × 1,500 = **BHD 120.000**; Employer SIO = 18% × 1,500 = **BHD 270.000**; PIT = BHD 0.

**Test 3 -- Bahraini national above SIO ceiling (2026).**
Input: Bahraini national, monthly wage BHD 5,000, year 2026.
Expected: Insurable wage capped at BHD 4,000. Employee SIO = 8% × 4,000 = **BHD 320.000**; Employer SIO = 18% × 4,000 = **BHD 720.000**; PIT = BHD 0.

**Test 4 -- Non-GCC expatriate SIO + EOSB.**
Input: Non-GCC expat, monthly wage BHD 900, 2 years of service.
Expected: Employee SIO = 1% × 900 = **BHD 9.000**; Employer SIO = 3% × 900 = **BHD 27.000**; EOSB = 4.2% × 900 = **BHD 37.800**; PIT = BHD 0.

**Test 5 -- Self-employed above VAT threshold.**
Input: Self-employed, annual taxable supplies BHD 42,000.
Expected: PIT = BHD 0. VAT registration = **MANDATORY** (> BHD 37,500); charge 10%.

**Test 6 -- Self-employed in voluntary VAT band.**
Input: Self-employed, annual taxable supplies BHD 20,000.
Expected: PIT = BHD 0. VAT registration = **VOLUNTARY** (BHD 18,750 -- 37,500); not mandatory.

**Test 7 -- GCC national SIO.**
Input: GCC national working in Bahrain, monthly wage BHD 2,000.
Expected: SIO assessed at **home-country rates**, not Bahrain's; do not apply 8%/18%. PIT = BHD 0.

## PROHIBITIONS

- NEVER invent personal income tax brackets, rates, or a PIT return for Bahrain — there is none; PIT is always BHD 0
- NEVER tell a user they must file a personal income tax return in Bahrain
- NEVER present business expenses as reducing a personal income tax bill — no PIT exists to reduce
- NEVER apply an SIO rate without a confirmed nationality category (Bahraini / non-GCC expat / GCC national)
- NEVER apply SIO contributions to wages above the BHD 4,000/month insurable ceiling
- NEVER use the 2025 employer SIO rate (17%) for a 2026 payroll — use the year-specific rate (18% for 2026)
- NEVER apply Bahrain SIO rates to a GCC national — they pay home-country rates
- NEVER state VAT penalty or municipal-tax figures as confirmed — they are flagged research gaps pending reviewer verification
- NEVER treat SIO or EOSB contributions as taxes or as PIT deductions
- NEVER present any figure as definitive — always label outputs as estimated and pending professional review

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
