---
name: armenia-income-tax
description: Use this skill whenever asked about Armenian personal income tax for individuals, self-employed individual entrepreneurs (IE), and employees. Trigger on phrases like "how much income tax in Armenia", "Armenian PIT", "flat 20% tax", "funded pension contribution", "turnover tax", "micro-business regime", "individual entrepreneur tax", "withholding on salary Armenia", "annual income declaration", "AMD net pay", "State Revenue Committee", "stamp duty on salary", "health insurance contribution", or any question about filing or computing personal/self-employment income tax for an Armenian-resident or Armenian-source taxpayer. Also trigger when preparing or reviewing an Armenian payroll calculation, an annual individual income tax declaration, a turnover-tax return, or advising on the micro-business regime. This skill covers the flat PIT rate, schedular rates (dividends, interest, royalties, rent, property sales), residency tests, mandatory funded pension, health-insurance and stamp-duty payroll levies, turnover-tax and micro-business special regimes, filing deadlines, and penalties. ALWAYS read this skill before touching any Armenian income tax work.
version: 0.1
jurisdiction: AM
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
depends_on:
  - income-tax-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Armenia Personal Income Tax -- Self-Employed & Individuals

## Armenia Personal Income Tax -- Self-Employed & Individuals Skill v0.1

> **Tier 2 -- research-verified.** Figures below were cross-checked mainly via PwC Worldwide Tax Summaries (last reviewed 5 Feb 2026) and Vardanyan & Partners (a local Armenian law firm). Numeric schedules were not directly extracted from the State Revenue Committee (src.am) or the ARLIS Tax Code text in this research session. A reviewer must confirm against src.am and the Tax Code of the Republic of Armenia directly. Items flagged **[RESEARCH GAP -- reviewer to confirm]** are explicitly uncertain.

## Section 1 -- Quick Reference

**Section 1 -- Quick Reference**

| Field | Value |
| --- | --- |
| Country | Armenia (Republic of Armenia) |
| Tax | Personal Income Tax (PIT) -- "anhatakan ekamtahark" |
| Currency | AMD (Armenian dram) only |
| Tax year | Calendar year (1 January -- 31 December) |
| Primary legislation | Tax Code of the Republic of Armenia (Law HO-165-N, in force since 1 Jan 2018, as amended); amendments effective 1 Jan 2025 |
| Supporting legislation | Law on Funded Pensions; Law "On Universal Health Insurance" (adopted Dec 2025, contributions from **2026**); turnover-tax and micro-business regime provisions of the Tax Code |
| Tax authority | State Revenue Committee of the Republic of Armenia (SRC / Petekamutneri Komite) |
| Filing portal | src.am ; e-filing at file-online.taxservice.am |
| Annual filing deadline (TY2025) | 1 November 2026 (transitional); from TY2026: 2 March -- 1 July of the following year |
| Validated by | Pending -- requires sign-off by a qualified Armenian tax practitioner |
| Validation date | Pending |
| Skill version | 0.1 |

### Headline rate (2025)

- **Flat PIT rate** — Armenia levies a single FLAT personal income tax of 20% on employment income, self-employment/business income, and most "other" income. Residents are taxed on worldwide income; non-residents on Armenian-source income only. There are no personal allowances and no progressive brackets under the flat regime -- PIT is simply 20% of gross taxable income.  _(PwC Worldwide Tax Summaries -- Taxes on personal income)_

### PIT Rate Schedule (2025)

**PIT Rate Schedule (2025)**  _(PwC)_

| Income type | Rate | Notes | Source |
| --- | --- | --- | --- |
| Employment income (general) | 20% (flat) | Single flat rate since 1 Jan 2023 (phased reduction from 23% completed). Withheld monthly by employer. | PwC |
| Business / self-employment income (general regime) | 20% (flat) | Applies absent a valid special-regime election. | PwC |
| Other income (general) | 20% (flat) | Residents worldwide; non-residents Armenian-source. | PwC |
| Dividends | 5% | Withheld at source; refundable if reinvested in the same resident entity in the same tax year. Non-resident treaty rates may differ (5%/10%). | PwC |
| Interest income | 20% | Effective from 1 Jan 2023. | PwC |
| Royalties | 10% | Effective from 1 Jan 2023. | PwC |
| Property lease / rental income | 10% on gross rent | If annual rental income exceeds AMD 60,000,000, an additional 10% applies to the excess **[RESEARCH GAP -- reviewer to confirm; flagged from prior years, not reconfirmed this session]**. | PwC |
| Sale of property (real estate / vehicles) to a tax agent (legal entity / IE) | 10% (or 20% in specific cases) | 10% generally; 20% in certain cases (e.g. building/developer sales). Sales of property **between private individuals are EXEMPT**. | PwC |

### PIT Rate Schedule (2025)

> **Note (rate stability):** The flat 20% rate has applied since 1 Jan 2023 and is unchanged for the 2025 tax year. _Source: PwC._

### Special-regime rate map (small business / self-employed)

**Special-regime rate map (small business / self-employed)**  _(PwC / Vardanyan & Partners)_

| Regime | Eligibility ceiling | Rate(s) | Source |
| --- | --- | --- | --- |
| General PIT regime | (default) | 20% flat on net income | PwC |
| Turnover tax | Prior-year sales turnover ≤ AMD 115,000,000 | 5% secondary raw-materials trade / 7% production / 10% trading & other / 1% high-tech / 10% rental, interest, royalties | PwC -- Corporate Other taxes |
| Micro-business (microenterprise) | Annual turnover ≤ AMD 24,000,000 | Broadly EXEMPT from main taxes; fixed reduced employee salary tax ~AMD 5,000/employee/month **[RESEARCH GAP -- reviewer to confirm exact current amount and post-July-2025 scope]** | Vardanyan & Partners |

### Conservative Defaults

**Conservative Defaults**

| Ambiguity | Default |
| --- | --- |
| Unknown residency status | Treat as **Armenian tax resident** (worldwide income) -- the broader, more conservative base |
| Unknown regime (general vs turnover vs micro) | **General 20% PIT regime** -- special regimes require a valid, timely election |
| Unknown employee date of birth | Assume born **on/after 1 Jan 1974** -- mandatory funded pension applies |
| Unknown whether stamp duty / health insurance applies | **Include them** in net-pay computations (statutory deductions) |
| Unknown income type | Treat as general income at **20%** |
| Unknown deductibility of a business cost | **Not deductible** until substantiated |
| Unknown VAT registration | Assume the turnover-tax / general boundary at AMD 115,000,000 governs |

## Section 2 -- Required Inputs and Refusal Catalogue

### Required Inputs

- **Minimum viable / Recommended / Ideal inputs** — **Minimum viable** -- the income figure(s) and income type (employment, self-employment, dividends, interest, royalties, rent, property sale), plus confirmation of residency status and (for payroll) the employee's monthly gross salary and whether born on/after 1 Jan 1974. **Recommended** -- full bank statement for the tax year in CSV/PDF/pasted text, payroll registers, the prior-year annual declaration or turnover-tax returns, confirmation of any special-regime election (turnover tax / micro-business) and its election date, and the SRC taxpayer registration (TIN / HVHH). **Ideal** -- complete income and expenditure records, contracts evidencing income type, funded-pension and health-insurance withholding records, stamp-duty records, and any treaty residence certificate for non-resident or dual-resident situations. **Refusal if minimum is missing -- SOFT WARN.** No income figure or income type at all = hard stop. A bank statement without supporting income-type detail = proceed with a reviewer warning: "This Armenian computation was produced from limited data. The reviewer must confirm residency, income type, and any special-regime election before filing."

### Refusal Catalogue

- **R-AM-1** — Residency status unknown and material. "Armenian residency (≥183 days, centre of vital interests, or state service) determines whether worldwide or only Armenian-source income is taxed. Confirm residency before relying on this output for a cross-border taxpayer."
- **R-AM-2** — Companies and partnerships. "This skill covers individuals and individual entrepreneurs (IE) only. Corporate profit tax for legal entities is out of scope. Escalate to an Armenian tax practitioner."
- **R-AM-3** — Treaty / non-resident reduced rates. "Treaty-reduced rates for non-residents (dividends, interest, royalties) are not enumerated in this skill. Out of scope. Escalate to an Armenian tax practitioner."
- **R-AM-4** — Capital gains / developer property sales. "Property sales taxed at 20% (e.g. building/developer disposals) and complex capital transactions require specialised analysis. Escalate to an Armenian tax practitioner."
- **R-AM-5** — Arrears / enforcement. "Client has outstanding Armenian tax arrears or SRC enforcement exposure. Late-payment interest accrues at 0.075%/day. Do not advise. Escalate immediately."
- **R-AM-6** — VAT return requested. "This skill covers personal income tax and the turnover/micro regimes only. Armenian VAT (general regime above AMD 115,000,000 turnover) is a separate workflow. Escalate or use a dedicated VAT skill."

## Section 3 -- Transaction Pattern Library

This is the deterministic pre-classifier. When a bank statement transaction matches a pattern below, apply the treatment directly. Do not second-guess. If none match, fall through to Tier 1 rules in Section 5.

**How to read this table.** Match by case-insensitive substring on the counterparty name or description as it appears in the bank statement. Armenian statements may be in Armenian, Russian, or English; both Armenian-script and transliterated terms are listed. If multiple patterns match, use the most specific. If none match, fall through to Tier 1 rules.

### 3.1 Income Patterns (Credits on Bank Statement)

**3.1 Income Patterns (Credits on Bank Statement)**

| Pattern | Income type | Treatment | Notes |
| --- | --- | --- | --- |
| Client name + TRANSFER, VARCUM, ՎՃԱՐՈՒՄ, PAYMENT | Business / self-employment | 20% general PIT (or turnover tax if elected) | Match to invoices; net of VAT if VAT-registered |
| GANDZ, FEES, CONSULTING, ԾԱՌԱՅՈՒԹՅՈՒՆ | Business / self-employment | 20% general PIT | Professional service fees |
| ASHKHATAVARDZ, SALARY, ASHKHATAVARД (ԱՇԽԱՏԱՎԱՐՁ) | Employment income | 20% PIT withheld by employer | Already net if employer withheld -- verify |
| STRIPE PAYOUT, PAYPAL, WISE, UPWORK, FIVERR | Business / self-employment | 20% general PIT | Platform payout -- match to underlying income |
| DIVIDEND, SHAHUTABAZHIN (ՇԱՀՈՒԹԱԲԱԺԻՆ) | Dividends | 5% (refundable if reinvested same year, same entity) | Withheld at source |
| TOKOS, INTEREST, ՏՈԿՈՍ | Interest income | 20% | Effective from 1 Jan 2023 |
| ROYALTY, ARTONAGIN (ԱՐՏՈՆԱԳԻՆ) | Royalties | 10% |  |
| VARDZAKALUTYUN, RENT RECEIVED, ՎԱՐՁԱԿԱԼՈՒԹՅՈՒՆ | Property lease / rental | 10% on gross | +10% on excess over AMD 60m/yr **[RESEARCH GAP]** |
| SRC REFUND, TAX REFUND, HARKI VERADARDZ | EXCLUDE | Not income | Prior-year refund |
| PROPERTY SALE TO ENTITY/IE | Property sale | 10% (or 20% certain cases) | Sale between private individuals = EXEMPT |

### 3.2 Expense / Deduction Patterns (Debits) -- relevant to IE / self-employed under general regime

**3.2 Expense / Deduction Patterns (Debits) -- relevant to IE / self-employed under general regime**

| Pattern | Category | Treatment | Notes |
| --- | --- | --- | --- |
| GRASENYAKI VARDZ, OFFICE RENT | Office rent | Deductible (general regime) | Dedicated business premises |
| HASHVAPAH, ACCOUNTANT, AUDIT | Accountancy fees | Deductible |  |
| IRAVABAN, LAWYER, LEGAL, NOTARY | Legal fees | Deductible | Business-related only |
| GRASENYAKAYIN, OFFICE SUPPLIES, STATIONERY | Office supplies | Deductible |  |
| MARKETING, GOOGLE ADS, META ADS, FACEBOOK | Marketing/advertising | Deductible |  |
| GOOGLE WORKSPACE, MICROSOFT 365, ADOBE, ANTHROPIC, OPENAI, GITHUB | Software subscription | Deductible | Recurring operating expense |
| BANK CHARGE, MIJNORDAVCAR, SPASARKUM | Bank charges | Deductible | Business account |
| STRIPE FEE, PAYPAL FEE | Payment processing | Deductible |  |

### 3.2 Expense / Deduction Patterns (Debits) -- relevant to IE / self-employed under general regime

> **Important:** Under the **turnover-tax** and **micro-business** regimes, tax is computed on **gross turnover**, NOT on net profit -- expense deductions in 3.2 are largely irrelevant there. Only the general 20% regime is profit-based.

### 3.3 Statutory Payroll Deductions (Debits / withholdings) -- NOT business expenses

**3.3 Statutory Payroll Deductions (Debits / withholdings) -- NOT business expenses**

| Pattern | Category | Treatment | Notes |
| --- | --- | --- | --- |
| PIT WITHHOLDING, ANHATAKAN HARK | PIT | 20% withheld monthly, remitted by 20th of following month | Employer = tax agent |
| KENSAPOZH, FUNDED PENSION, PENSION CONTRIBUTION | Funded pension | See Section 5.4 formula | Employee withholding + state co-financing |
| STAMP DUTY, DEFENCE STAMP, NTAGOSGHARI | Stamp (military/defence) duty | AMD 1,000 or AMD 15,000/month (Dec 2025) | Tiered by gross salary |
| HEALTH INSURANCE, ARJOGHJUTYAN APAHOVAGRUTYUN | Health insurance contribution | AMD 4,800 or AMD 10,800/month reference premium (from 2026; net is state-subsidised — see §5.7) | Employees earning > AMD 200,000/month |

### 3.4 Exclusions (Neither Income nor Deductible Expense)

**3.4 Exclusions (Neither Income nor Deductible Expense)**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| INTERNAL TRANSFER, OWN ACCOUNT, SEPAKAN HASHIV | EXCLUDE | Own-account transfer |
| LOAN, VARK, REPAYMENT | EXCLUDE | Loan principal movement |
| VAT PAYMENT, AAH (ԱԱՀ) | EXCLUDE | VAT liability payment, not an expense |
| TAX PAYMENT, HARKI VCHARUM | EXCLUDE | Income tax itself is not deductible |
| DRAWINGS, PERSONAL WITHDRAWAL, ATM (personal) | EXCLUDE | Not an expense |

### 3.5 Armenian Banks -- Statement Format Reference

**3.5 Armenian Banks -- Statement Format Reference**

| Bank | Common Patterns | Notes |
| --- | --- | --- |
| Ameriabank | TRANSFER, PAYMENT, FEE, CARD | PDF/CSV; English + Armenian descriptions |
| Ardshinbank | VARCUM, SPASARKUM, KARTI | PDF; Armenian-script descriptions common |
| Acba Bank | TRANSFER, COMMISSION, DD | PDF/CSV |
| Inecobank | PAYMENT, TRANSFER, FEE | CSV available; clean counterparty names |
| Converse Bank | VARCUM, TOKOS, SPASARKUM | PDF; mixed Armenian/English |

## Section 4 -- Worked Examples

> All figures recomputed end-to-end. Rates per PwC / Vardanyan & Partners as cited in Section 1.

### Example 1 -- Employee, monthly gross AMD 400,000 (below pension 500k threshold)

**Input line:**
`05/03/2025 ; AMERIABANK ; EMPLOYER LLC ; ASHKHATAVARDZ MARCH ; +400,000.00 ; AMD`

**Reasoning (monthly):**
- PIT: 20% × 400,000 = **AMD 80,000**
- Funded pension: gross < 500,000 → 5% × 400,000 = **AMD 20,000**
- Stamp (defence) duty: gross ≤ 1,000,000 → **AMD 1,000**
- Health insurance: gross > 200,000 and ≤ 500,000 → **AMD 4,800** reference premium (from 2026; actual net likely ~AMD 300 after state subsidy — see §5.7)
- Net pay (using reference premium) = 400,000 − 80,000 − 20,000 − 1,000 − 4,800 = **AMD 294,200** _(net is higher if the ~AMD 300 subsidised figure applies — reviewer to confirm)_

**Classification:** Employment income, flat 20% PIT, pension 5% tier, lowest stamp/health tier.

### Example 2 -- Employee, monthly gross AMD 600,000 (above pension 500k threshold)

**Input line:**
`05/03/2025 ; INECOBANK ; EMPLOYER LLC ; SALARY MARCH ; +600,000.00 ; AMD`

**Reasoning (monthly):**
- PIT: 20% × 600,000 = **AMD 120,000**
- Funded pension: gross ≥ 500,000 → 10% × 600,000 − 25,000 = 60,000 − 25,000 = **AMD 35,000**
- Stamp duty: gross ≤ 1,000,000 → **AMD 1,000**
- Health insurance: gross ≥ 500,001 → **AMD 10,800**
- Net pay = 600,000 − 120,000 − 35,000 − 1,000 − 10,800 = **AMD 433,200**

**Classification:** Employment income, 10%-minus-25,000 pension tier, top stamp/health tier above 500,001.

### Example 3 -- Employee, monthly gross AMD 1,200,000 (above pension base cap)

**Input line:**
`05/03/2025 ; ARDSHINBANK ; EMPLOYER LLC ; SALARY MARCH ; +1,200,000.00 ; AMD`

**Reasoning (monthly):**
- PIT: 20% × 1,200,000 = **AMD 240,000**
- Funded pension: base capped at AMD 1,125,000 → 10% × 1,125,000 − 25,000 = 112,500 − 25,000 = **AMD 87,500** (the statutory maximum)
- Stamp duty: gross > 1,000,001 → **AMD 15,000**
- Health insurance: gross ≥ 500,001 → **AMD 10,800**
- Net pay = 1,200,000 − 240,000 − 87,500 − 15,000 − 10,800 = **AMD 846,700**

**Classification:** Employment income at the pension contribution ceiling; max funded-pension AMD 87,500/month confirmed.

### Example 4 -- Individual Entrepreneur, general regime, annual income AMD 10,000,000

**Input:** IE NOT under a special regime (e.g. excluded professional service), annual gross income AMD 10,000,000.

**Reasoning (annual):**
- General PIT: 20% × 10,000,000 = **AMD 2,000,000** _(applied to taxable income; assume no allowable deductions here for illustration)_
- Funded pension (IE): income > 6,000,000 → 10% × 10,000,000 − 300,000 = 1,000,000 − 300,000 = **AMD 700,000**
- Health insurance (IE): income > 2,400,001 → flat **AMD 129,600**
- Net after statutory levies = 10,000,000 − 2,000,000 − 700,000 − 129,600 = **AMD 7,170,400**

**Classification:** General-regime IE; pension 10%-minus-300,000 tier; IE health-insurance flat charge applies.

### Example 5 -- Turnover-tax IE (trading), quarterly turnover AMD 5,000,000

**Input:** IE under turnover-tax regime (prior-year sales ≤ AMD 115,000,000), trading activity, quarterly turnover AMD 5,000,000.

**Reasoning:**
- Turnover tax (trading & other): 10% × 5,000,000 = **AMD 500,000** for the quarter
- Computed on gross turnover -- no expense deductions
- Quarterly filing; pay within 20 days of period end

**Classification:** Turnover tax 10% trading rate. Note funded-pension and (where applicable) IE health-insurance contributions still apply separately per Section 5.

### Example 6 -- Dividend received

**Input line:**
`20/04/2025 ; CONVERSE BANK ; RESIDENT CO LLC ; SHAHUTABAZHIN ; +1,000,000.00 ; AMD`

**Reasoning:**
- Dividend: 5% × 1,000,000 = **AMD 50,000** withheld at source.
- Refundable if reinvested in the **same resident entity in the same tax year**.

**Classification:** Schedular 5% dividend rate. Flag reinvestment-refund eligibility for reviewer.

### Example 7 -- Property sale between private individuals (EXEMPT)

**Input line:**
`12/05/2025 ; AMERIABANK ; PRIVATE BUYER ; APARTMENT SALE ; +45,000,000.00 ; AMD`

**Reasoning:**
- Sale of real estate **between private individuals is EXEMPT** from PIT.
- (Contrast: sale to a tax agent / legal entity / IE would be 10%, or 20% in developer/building cases.)

**Classification:** EXEMPT. No PIT. Confirm the buyer is a private individual, not a tax agent.

### 5.1 The Flat PIT Rate

- **Flat PIT rate 20%** — PIT is a single flat 20% on employment income, self-employment/business income (general regime), and most other income. There are no personal allowances and no progressive brackets. Residents are taxed on worldwide income; non-residents on Armenian-source income only.  _(Tax Code of Armenia (HO-165-N); PwC)_

### 5.2 Residency Tests

- **Residency test criteria** — An individual is an Armenian tax resident if ANY of the following holds: ≥183 days physical presence in Armenia during the tax year (1 Jan -- 31 Dec); OR Centre of vital interests is in Armenia; OR the individual is in Armenian civil / state service. Default to resident treatment when status is unknown (Section 1).  _(Tax Code; PwC -- Residence)_

### 5.3 Schedular Rates

**5.3 Schedular Rates**  _(PwC)_

| Income type | Rate | Source |
| --- | --- | --- |
| Dividends | 5% (refundable if reinvested same year, same resident entity) | PwC |
| Interest | 20% | PwC |
| Royalties | 10% | PwC |
| Property lease / rental | 10% on gross (+10% on excess over AMD 60m/yr **[RESEARCH GAP]**) | PwC |
| Sale of property to a tax agent | 10% (or 20% in certain cases); private-to-private EXEMPT | PwC |

### 5.4 Mandatory Funded Pension Contribution

- **Employee funded pension formula** — If gross < AMD 500,000: contribution = 5% × gross. If gross ≥ AMD 500,000: contribution = 10% × gross − AMD 25,000. Base capped at AMD 1,125,000/month (= 15 × minimum monthly salary of AMD 75,000), giving a maximum employee contribution of AMD 87,500/month. Arithmetic check at cap: 10% × 1,125,000 − 25,000 = 112,500 − 25,000 = 87,500.  _(Law on Funded Pensions; PwC -- Other taxes)_
- **IE funded pension formula** — If income ≤ AMD 6,000,000: contribution = 5% × income. If income > AMD 6,000,000: contribution = 10% × income − AMD 300,000. Aligned to the AMD 1,125,000/month base cap (= AMD 13,500,000/year), giving the same annual maximum AMD 1,050,000 (= 87,500 × 12).  _(PwC)_

### 5.4 Mandatory Funded Pension Contribution

- **Applicability** — Mandatory for employees born on/after 1 Jan 1974; the State co-finances the remainder from the budget.  _(Law on Funded Pensions; PwC -- Other taxes)_

### 5.5 Employer Social Security Contributions -- NONE

- **No employer social security contribution** — Private-sector employers in Armenia pay NO separate social security contribution. The only worker-side mandatory levies are the employee funded pension (with state co-financing), the stamp/defence duty, and the health-insurance contribution.  _(Vardanyan & Partners -- Payroll guide)_

### 5.6 Stamp (Military / Defence) Duty on Salaries

**5.6 Stamp (Military / Defence) Duty on Salaries**  _(PwC -- Other taxes)_

| Monthly gross | Stamp duty |
| --- | --- |
| Up to AMD 1,000,000 | AMD 1,000/month |
| Above AMD 1,000,001 | AMD 15,000/month |

### 5.6 Stamp (Military / Defence) Duty on Salaries

> **[RESEARCH GAP -- reviewer to confirm]** The schedule above AMD 1,000,001 is likely graduated to higher fixed amounts for very high salaries; only two tiers were captured this session.

### 5.7 Mandatory Health Insurance Contribution

- **Health insurance contribution overview** — Law "On Universal Health Insurance" was adopted December 2025; contributions apply from 2026 (NOT from 25 Dec 2025). Mandatory only for employees with monthly gross > AMD 200,000. The full reference premium is AMD 129,600/year (≈ AMD 10,800/month) per adult.  _(PwC -- Other taxes; armenian-lawyer.com; profin.am)_

**5.7 Mandatory Health Insurance Contribution**  _(PwC)_

| Monthly gross | Reference premium tier (per PwC) |
| --- | --- |
| AMD 200,001 -- 500,000 | AMD 4,800/month |
| ≥ AMD 500,001 | AMD 10,800/month |

### 5.7 Mandatory Health Insurance Contribution

- **IE health insurance flat amount** — Individual entrepreneurs: flat AMD 129,600 annually, if annual gross income > AMD 2,400,001.  _(PwC)_

### 5.7 Mandatory Health Insurance Contribution

> **[RESEARCH GAP -- reviewer to confirm — MATERIAL]** Two issues a reviewer MUST resolve before relying on the net-pay figures below:
> 1. **Timing:** contributions run from **2026**, not 25 Dec 2025 (that is the law's adoption, not the contribution start). Any "eff. 25 Dec 2025" tag elsewhere in this skill means "from 2026 under the Dec-2025 law."
> 2. **State subsidy:** the AMD 4,800 / 10,800 figures are the *reference premium* tiers. The scheme is heavily state-subsidized, so the employee's actual **net** deduction is much lower — one source indicates only **~AMD 300/month** for the AMD 200,001–500,000 band. The worked examples below use the gross premium tiers and therefore likely OVERSTATE the net deduction; confirm the in-force subsidy schedule against src.am before use.

### 5.8 Minimum Monthly Wage

- **Minimum monthly wage** — AMD 75,000/month, effective since 1 Jan 2023, unchanged through 2025-2026. (Drives the AMD 1,125,000 = 15 × 75,000 pension base cap.)  _(Armenpress)_

### 5.9 Turnover Tax Regime (Small Business / Self-Employed)

- **Eligibility** — Prior-year sales turnover ≤ AMD 115,000,000.  _(PwC -- Corporate Other taxes)_

**5.9 Turnover Tax Regime (Small Business / Self-Employed)**

| Activity | Rate |
| --- | --- |
| Secondary raw-materials trade | 5% |
| Production | 7% |
| Trading & other | 10% |
| High-tech | 1% |
| Rental, interest, royalties | 10% |

### 5.9 Turnover Tax Regime (Small Business / Self-Employed)

- **Computation and filing** — Computed on gross turnover (no profit deductions). Quarterly filing; pay within 20 days of period end. Crossing AMD 115,000,000 moves the taxpayer into the general VAT regime (the VAT registration threshold is the same AMD 115,000,000).  _(PwC)_

### 5.10 Micro-Business (Microenterprise) Regime

- **Eligibility and treatment** — Eligibility: annual turnover ≤ AMD 24,000,000. Broadly EXEMPT from main taxes. Salaries paid to employees still bear a fixed reduced income tax of ~AMD 5,000/employee/month [RESEARCH GAP -- reviewer to confirm exact current amount and whether it still applies after the July 2025 exclusions]. Many professional / B2B services (consulting, IT, legal, accounting, advertising, medicine) have been EXCLUDED since July 2025. Election by 20 February of the tax year (existing businesses); within 20 days of registration (new businesses).  _(Vardanyan & Partners)_

### 5.11 PIT Withholding and Remittance

- **Withholding and remittance** — Employers (tax agents) withhold flat 20% PIT monthly from employment income and remit to the State Budget by the 20th day of the following month, together with funded-pension, stamp-duty, and health-insurance amounts. Where supporting documentation is lacking, tax agents withhold at 20%.  _(PwC -- Tax administration)_

### 5.12 Non-Deductible / Excluded Items (general regime IE)

**5.12 Non-Deductible / Excluded Items (general regime IE)**

| Item | Reason |
| --- | --- |
| Income tax itself | Tax on income |
| VAT collected / paid (registered) | Liability movement, not income/expense |
| Drawings / personal withdrawals | Not an expense |
| Personal living costs | Not business-related |
| Loan principal | Capital movement |

### 6.1 Residency Determination (cross-border)

≥183-day count, centre-of-vital-interests, and state-service tests can conflict, especially for dual-resident or recently-arrived individuals. Conservative default: resident (worldwide income). Flag for reviewer: day-count records, treaty tie-breakers, residence certificate.

### 6.2 Dividend Reinvestment Refund

5% dividend tax is refundable if reinvested in the same resident entity in the same tax year. Flag for reviewer: confirm the reinvestment occurred, into the same entity, within the same tax year, with documentation.

### 6.3 Property Sale Characterisation

10% to a tax agent vs 20% for developer/building sales vs EXEMPT between private individuals. Flag for reviewer: confirm buyer status (private vs tax agent) and whether the seller is a developer.

### 6.4 Rental Income Excess Surcharge

Additional 10% on annual rental income over AMD 60,000,000 is [RESEARCH GAP -- reviewer to confirm]. Flag for reviewer: confirm whether the surcharge is in force for TY2025 and its base.

### 6.5 Regime Election Eligibility (turnover / micro)

Eligibility depends on prior-year turnover, activity type (post-July-2025 professional-service exclusions), and a timely election. Flag for reviewer: confirm a valid, timely election exists and the activity is eligible; otherwise default to general 20%.

### 6.6 Funded Pension -- Born-Before-1974 Employees

Mandatory funded pension applies to those born on/after 1 Jan 1974; older employees fall outside the mandatory scheme. Flag for reviewer: confirm date of birth before applying or omitting the contribution.

### 6.7 Allowable Deductions for General-Regime IE

The Tax Code permits deduction of documented business expenses for general-regime IE; specific limits and documentation standards were not enumerated this session. Flag for reviewer: confirm deductibility and substantiation against the Tax Code.

## Section 7 -- Excel Working Paper Template

```
ARMENIA INCOME TAX -- WORKING PAPER
Tax Year: 2025
Taxpayer: ___________________________
Residency: Resident (worldwide) / Non-resident (AM-source)
Type: Employee / IE general / IE turnover-tax / IE micro-business

PART A -- EMPLOYMENT INCOME (monthly)
  A1. Monthly gross salary (AMD)                  ___________
  A2. PIT 20% (A1 x 0.20)                          ___________
  A3. Funded pension:
        if A1 < 500,000: 5% x A1
        if A1 >= 500,000: 10% x min(A1,1,125,000) - 25,000
        (max 87,500)                               ___________
  A4. Stamp duty (1,000 if A1<=1,000,000;
        15,000 if A1>1,000,001)                    ___________
  A5. Health insurance (if A1>200,000:
        4,800 if A1<=500,000; 10,800 if A1>=500,001)___________
  A6. NET PAY (A1 - A2 - A3 - A4 - A5)             ___________

PART B -- IE GENERAL REGIME (annual)
  B1. Annual gross income                          ___________
  B2. Allowable deductions (T2 - reviewer)         ___________
  B3. Taxable income (B1 - B2)                      ___________
  B4. PIT 20% (B3 x 0.20)                           ___________
  B5. Funded pension:
        if B1 <= 6,000,000: 5% x B1
        if B1 > 6,000,000: 10% x min(B1,13,500,000) - 300,000 ___________
  B6. Health insurance (129,600 if B1>2,400,001)   ___________
  B7. NET AFTER LEVIES (B1 - B4 - B5 - B6)         ___________

PART C -- TURNOVER TAX (quarterly)
  C1. Quarterly turnover                           ___________
  C2. Rate (5/7/10/1/10 % per activity)            ___________
  C3. Turnover tax (C1 x C2)                       ___________

PART D -- SCHEDULAR INCOME
  D1. Dividends x 5%                               ___________
  D2. Interest x 20%                               ___________
  D3. Royalties x 10%                              ___________
  D4. Rent x 10% (+10% over 60m? [RESEARCH GAP])   ___________

REVIEWER FLAGS:
  [ ] Residency confirmed?
  [ ] Regime (general/turnover/micro) confirmed + election date?
  [ ] Employee born on/after 1 Jan 1974?
  [ ] Stamp duty + health insurance in-force dates confirmed?
  [ ] Property sale: buyer private vs tax agent?
  [ ] Dividend reinvestment refund eligibility?
  [ ] Rental surcharge over 60m confirmed?
  [ ] Micro-business employee salary tax amount confirmed?
```

### Armenian Bank Statement Formats

**Armenian Bank Statement Formats**

| Bank | Format | Key Fields | Notes |
| --- | --- | --- | --- |
| Ameriabank | PDF, CSV | Date, Description, Debit, Credit, Balance | English + Armenian; most common |
| Ardshinbank | PDF | Date, Particulars, Withdrawals, Deposits | Armenian-script descriptions common |
| Acba Bank | PDF, CSV | Date, Description, Amount, Balance |  |
| Inecobank | CSV | Date, Counterparty, Amount, Reference | Clean data; English available |
| Converse Bank | PDF | Date, Description, Debit, Credit | Mixed Armenian/English |

### Key Armenian Banking / Tax Terms

**Key Armenian Banking / Tax Terms**

| Term (transliteration) | Armenian | English | Classification Hint |
| --- | --- | --- | --- |
| Varcum | ՎՃԱՐՈՒՄ | Payment / transfer | Check direction for income/expense |
| Ashkhatavardz | ԱՇԽԱՏԱՎԱՐՁ | Salary | Employment income (Box: PIT 20% withheld) |
| Shahutabazhin | ՇԱՀՈՒԹԱԲԱԺԻՆ | Dividend | 5% schedular |
| Tokos | ՏՈԿՈՍ | Interest | 20% schedular (or bank charge) |
| Artonagin | ԱՐՏՈՆԱԳԻՆ | Royalty | 10% schedular |
| Vardzakalutyun | ՎԱՐՁԱԿԱԼՈՒԹՅՈՒՆ | Rent / lease | 10% on gross |
| Hark | ՀԱՐԿ | Tax | Tax payment -- exclude |
| AAH | ԱԱՀ | VAT | VAT liability -- exclude |
| Kensapozh | ԿԵՆՍԱԹՈՇԱԿ | Pension | Funded pension contribution |
| Spasarkum | ՍՊԱՍԱՐԿՈՒՄ | Service / charge | Bank charge or service fee |

## Section 9 -- Onboarding Fallback

If the client provides a bank statement but cannot answer onboarding questions immediately:

1. Classify all transactions using the pattern library (Section 3).
2. Mark all Tier 2 items as "PENDING -- reviewer must confirm".
3. Apply conservative defaults (Section 1): resident, general 20% regime, pension applies, include stamp duty + health insurance.
4. Generate the working paper (Section 7) with clear flags.
5. Present the following questions to the client:

```
ONBOARDING QUESTIONS -- ARMENIA INCOME TAX
1. Are you an Armenian tax resident? (>=183 days in Armenia, centre of vital
   interests here, or in Armenian state service?)
2. What is your income type: employment, self-employment (IE), dividends,
   interest, royalties, rent, or property sale?
3. If self-employed: are you under a special regime (turnover tax or
   micro-business)? When did you elect it?
4. If employed: what is your monthly gross salary, and were you born on or
   after 1 January 1974?
5. Did you receive any foreign-source income (you may need to file an annual
   declaration)?
6. Any property sales? Was the buyer a private individual or a company/IE?
7. Any dividends you reinvested in the same company in the same year?
8. What is your SRC taxpayer registration (TIN / HVHH)?
```

### Key References

**Key References**

| Topic | Reference | Source |
| --- | --- | --- |
| Flat PIT rate, schedular rates | Tax Code HO-165-N | PwC -- Taxes on personal income |
| Residency tests | Tax Code | PwC -- Residence |
| Funded pension, health insurance, stamp duty | Law on Funded Pensions; Tax Code amendments | PwC -- Other taxes |
| Turnover tax, VAT threshold, micro-business | Tax Code | PwC -- Corporate Other taxes; Vardanyan & Partners |
| Withholding, filing deadlines | Tax Code | PwC -- Tax administration |
| Penalties | Tax Code (as amended 1 Jan 2025) | Vardanyan & Partners -- Tax calendar 2025 |
| Minimum wage | Government decision | Armenpress |

### Forms and Deadlines

**Forms and Deadlines**

| Form / report | Purpose | Deadline | Source |
| --- | --- | --- | --- |
| Annual individual income tax declaration | Individuals with income not taxed at source (foreign-source, certain self-employment/other); universal-declaration filers | TY2025: by **1 November 2026** (transitional); from TY2026: **2 March -- 1 July** of following year | PwC |
| Monthly unified payroll / income tax & social payment calculation | Tax-agent report of withheld PIT, funded pension, stamp duty, health insurance | Payment + report by **20th** of following month | PwC |
| Turnover tax return | Quarterly small-business / IE return | Quarterly; pay within **20 days** of period end | PwC |
| Regime eligibility statement (turnover / micro) | Elect/confirm special regime | By **20 February** (existing); within **20 days** of registration (new) | Vardanyan & Partners |

### Penalties

**Penalties**

| Type | Detail | Source |
| --- | --- | --- |
| Late-payment interest/penalty | **0.075% per day** on overdue tax (from 1 Jan 2025; previously 0.04%/day), capped at 730 days | Vardanyan & Partners -- Tax calendar 2025 |
| Failure to file individual income tax return | **AMD 5,000** (ordinary individuals); up to **AMD 50,000** (major participants / large filers) | Vardanyan & Partners |

### Penalties

> **[RESEARCH GAP -- reviewer to confirm]** The 0.075%/day late-payment rate (from 1 Jan 2025) supersedes the older 0.04%/day per the local guide; confirm against the current Tax Code.

### Test Suite

**Test 1 -- Employee, gross AMD 400,000/month.**
Expected: PIT 80,000; pension 20,000 (5% tier); stamp 1,000; health 4,800; **net AMD 294,200**.

**Test 2 -- Employee, gross AMD 600,000/month.**
Expected: PIT 120,000; pension 35,000 (10% − 25,000); stamp 1,000; health 10,800; **net AMD 433,200**.

**Test 3 -- Employee, gross AMD 1,200,000/month (pension cap).**
Expected: PIT 240,000; pension 87,500 (capped); stamp 15,000; health 10,800; **net AMD 846,700**.

**Test 4 -- IE general, annual income AMD 10,000,000 (no deductions).**
Expected: PIT 2,000,000; pension 700,000 (10% − 300,000); IE health 129,600; **net after levies AMD 7,170,400**.

**Test 5 -- Turnover-tax IE, trading, quarterly turnover AMD 5,000,000.**
Expected: turnover tax 10% = **AMD 500,000** (on gross, no deductions).

**Test 6 -- Dividend AMD 1,000,000.**
Expected: 5% = **AMD 50,000** withheld; refundable if reinvested same entity, same year.

**Test 7 -- Property sale AMD 45,000,000 between private individuals.**
Expected: **EXEMPT** -- AMD 0 PIT. (Sale to a tax agent would be 10% / 20%.)

## PROHIBITIONS

- **Prohibitions list** — NEVER apply progressive brackets or a personal allowance -- Armenia uses a single flat 20% PIT with no allowance NEVER omit the funded-pension contribution for an employee born on/after 1 Jan 1974 NEVER use the 5% pension tier above AMD 500,000 gross -- switch to 10% minus AMD 25,000, capped at AMD 87,500/month NEVER apply an employer social security contribution -- private-sector employers pay none NEVER tax a property sale between private individuals -- it is EXEMPT NEVER apply turnover-tax or micro-business rates without a confirmed, timely regime election NEVER treat turnover-tax / micro-business as profit-based -- they are computed on gross turnover NEVER allow income tax itself, VAT, drawings, or loan principal as deductions NEVER omit stamp duty or (from 2026) the health-insurance contribution from net-pay computations NEVER present an unflagged figure that is marked [RESEARCH GAP] as final -- escalate to a reviewer NEVER present tax calculations as definitive -- always label as estimated

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.

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
