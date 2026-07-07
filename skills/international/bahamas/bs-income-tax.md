---
name: bahamas-income-tax
description: "Use this skill whenever asked about Bahamas tax obligations for individuals, self-employed persons, or sole traders. Trigger on phrases like \"do I pay income tax in the Bahamas\", \"NIB contributions\", \"National Insurance Board\", \"business licence fee\", \"VAT registration Bahamas\", \"real property tax Bahamas\", \"stamp duty Bahamas\", \"self-employed tax Bahamas\", \"payroll Bahamas\", or any question about tax filing or obligations for a person living or working in the Bahamas. Also trigger when computing NIB contribution amounts, preparing a business licence application, determining VAT registration thresholds, or advising on property taxes and stamp duty. This skill covers the full Bahamas tax reality: no personal income tax of any kind, NIB social contributions (the primary individual obligation), VAT, Business Licence, Real Property Tax, and Stamp Duty. ALWAYS read this skill before touching any Bahamas tax or compliance work."
jurisdiction: BS
tax_year: 2025
tier: 2
last_updated: 2026-07-06
---

# bahamas-income-tax

## Section 1 -- Quick Reference

**Section 1 -- Quick Reference**

| Field | Value |
| --- | --- |
| Country | Commonwealth of The Bahamas |
| Personal Income Tax | **NONE** -- The Bahamas levies no personal income tax of any kind |
| Currency | Bahamian Dollar (BSD), pegged 1:1 to USD |
| Tax year | Calendar year (1 January -- 31 December) |
| Primary individual obligation | National Insurance Board (NIB) contributions |
| Revenue authority (VAT, Business Licence, RPT) | Department of Inland Revenue (DIR) |
| NIB authority | National Insurance Board (nib-bahamas.com) |
| Filing portal (VAT) | https://vat.revenue.gov.bs/ |
| Annual income tax return | **Does not exist** -- no PIT return to file |
| Validated by | Pending -- requires sign-off by a qualified Bahamian practitioner |
| Validation date | Pending |
| Skill version | 0.1 |

### There Is No Personal Income Tax

The Bahamas has **no personal income tax** of any kind. This is not a low rate or a zero band -- the tax itself does not exist. Confirmed absent (Source: PwC Worldwide Tax Summaries -- Bahamas Individual, last reviewed 24 February 2026):

**Confirmed absent taxes**  _(PwC Worldwide Tax Summaries -- Bahamas Individual, last reviewed 24 February 2026)_

| Tax | Status |
| --- | --- |
| Income tax on employment or self-employment income | Does not exist |
| Capital gains tax | Does not exist |
| Inheritance, estate, or gift tax | Does not exist |
| Wealth or net worth tax | Does not exist |
| Transfer taxes on securities | Does not exist |
| Payroll income tax | Does not exist (NIB social contributions exist separately) |

### NIB Contribution Rates (Effective 1 July 2024)

A 1.5 percentage-point increase was implemented 1 July 2024 to address Pensions Branch fund sustainability. (Source: nibrateincrease.com; PwC Tax Summaries -- Bahamas Individual Other Taxes)

**NIB contribution rates**  _(nibrateincrease.com; PwC Tax Summaries -- Bahamas Individual Other Taxes)_

| Category | Rate from 1 Jul 2024 | Previous rate |
| --- | --- | --- |
| Employee | **4.65%** | 3.9% |
| Employer | **6.65%** | 5.9% |
| Combined (employee + employer) | **11.30%** | 9.8% |
| Self-employed | **10.30%** | 8.8% |
| Voluntarily insured | **6.50%** | 5.0% |

### NIB Insurable Wage Ceiling

(Source: NIB 2024 Adjustments -- nib-bahamas.com/2024-adjustments-to-the-insurable-wage-ceiling-pensions-and-grants/)

**NIB insurable wage ceiling**  _(nib-bahamas.com/2024-adjustments-to-the-insurable-wage-ceiling-pensions-and-grants/)_

| Period | Weekly ceiling | Monthly ceiling |
| --- | --- | --- |
| Previous (to 30 Jun 2024) | BSD 740 | BSD 3,207 |
| **Current (1 Jul 2024 -- 30 Jun 2026)** | **BSD 810** | **BSD 3,510** |
| Upcoming (from 1 Jul 2026) | BSD 830 | BSD 3,597 |

- **Earnings above ceiling and biennial adjustment** — Earnings above the weekly ceiling are not subject to NIB contributions. The ceiling is adjusted biennially based on the retail price index over the preceding two years plus 2%.  _(nib-bahamas.com/biennial-adjustments-to-pensions-grants-and-the-wage-ceiling)_

### Maximum Weekly and Annual NIB Contributions at Current Ceiling (BSD 810/week)

**Maximum weekly and annual NIB contributions**

| Party | Rate | Weekly max | Annual max (52 weeks) |
| --- | --- | --- | --- |
| Employee | 4.65% | BSD 37.67 | BSD 1,958 |
| Employer | 6.65% | BSD 53.87 | BSD 2,801 |
| Combined (employee + employer) | 11.30% | BSD 91.53 | BSD 4,760 |
| Self-employed (full both shares) | 10.30% | BSD 83.43 | BSD 4,338 |

*Arithmetic check: 37.67 + 53.87 = BSD 91.53/week combined. 91.53 × 52 = BSD 4,759.56 ≈ BSD 4,760. Self-employed: 810 × 10.30% = BSD 83.43/week × 52 = BSD 4,338.36.*

### VAT Rates (as of 1 September 2025)

(Source: Inland Revenue VAT -- inlandrevenue.finance.gov.bs/value-added-tax/; Higgs & Johnson 2025 Tax Legislative Updates)

**VAT rates**  _(inlandrevenue.finance.gov.bs/value-added-tax/; Higgs & Johnson 2025 Tax Legislative Updates)_

| Category | Rate | Applies to |
| --- | --- | --- |
| Standard | **10%** | Most goods and services |
| Reduced | **5%** | Unprepared groceries, medications, medical supplies, baby/adult diapers, feminine hygiene products (effective 1 Sep 2025) |
| Zero | **0%** | Exports; certain financial services |
| Exempt | Exempt | Residential rent; certain education; certain financial products |

- **Sweets/gum/sodas rate change** — From 1 Sep 2025, sweets, chewing gum, and sodas were moved back to 10% (from prior reduced-rate treatment).  _(PM Davis announcement -- bahamas.gov.bs)_

### Business Licence Fee Schedule

(Source: Inland Revenue -- inlandrevenue.finance.gov.bs/tax-incentives/business-licence-new-rates-1/; PwC Corporate Other Taxes)

**Business Licence Fee Schedule**  _(inlandrevenue.finance.gov.bs/tax-incentives/business-licence-new-rates-1/; PwC Corporate Other Taxes)_

| Annual turnover | Licence tax |
| --- | --- |
| ≤ BSD 50,000 | BSD 100 flat fee |
| BSD 50,001 -- BSD 500,000 | 0.50% of turnover |
| BSD 500,001 -- BSD 5,000,000 | 0.75% of turnover |
| > BSD 5,000,000 | 1.25% of turnover |

### Conservative Defaults

**Conservative Defaults**

| Ambiguity | Default |
| --- | --- |
| Client asks about income tax | State clearly: there is no personal income tax in the Bahamas |
| Unknown NIB registration status | STOP -- instruct client to register with NIB if self-employed and not yet registered |
| Unknown business turnover (VAT threshold) | Assume VAT registration required; escalate to confirm |
| Unknown property ownership | Skip RPT section; note it for reviewer |
| Unknown business-use % (vehicle, phone, home) | 0% deduction for Business Licence cost purposes |
| Unknown expense category (Business Licence deductibility) | Not deductible until confirmed |
| Client asks about capital gains on property | No CGT in Bahamas; stamp duty applies on conveyance |

### Required Inputs

**Minimum viable** -- client's employment status (employed / self-employed / both), approximate annual earnings or turnover, and confirmation they are resident in or operating from the Bahamas.

**Recommended** -- NIB registration number (nine-digit), whether a Business Licence has been obtained, VAT registration status and number if applicable, property ownership details for RPT, any recent real estate transactions for stamp duty.

**Ideal** -- NIB Smart Card, Business Licence certificate, VAT registration certificate, DIR taxpayer file number, complete annual turnover figure, payroll records (for employers), bank statements for the full year.

**Refusal if minimum is missing -- SOFT WARN.** If employment status is unknown, issue a hard stop: "Employment and self-employment status is required to determine NIB contribution rates and obligations. Please confirm before proceeding."

### Refusal Catalogue

- **R-BS-1** — "The Bahamas levies no personal income tax. There is no tax return to file, no income to declare to a tax authority, and no income tax due. If you are asking about social contributions, see the NIB section. If you are a business paying corporate tax, this skill does not cover corporate tax -- escalate to a qualified Bahamian practitioner." (Client asks for a personal income tax computation.)
- **R-BS-2** — "The Bahamas has no capital gains tax. If you are selling real estate, stamp duty applies on the conveyance -- see Section 6. If you are selling securities, no transfer taxes apply." (Capital gains computation requested.)
- **R-BS-3** — "There is no inheritance, estate, or gift tax in the Bahamas. Estate planning and probate costs are legal/probate fees, not taxes. Escalate to a Bahamian attorney for estate planning." (Inheritance or estate planning.)
- **R-BS-4** — "This skill covers individuals and self-employed sole traders only. The Bahamas does not impose corporate income tax on profits, but companies face Business Licence fees, VAT registration obligations, and payroll NIB obligations. Escalate to a qualified Bahamian practitioner for company compliance." (Corporate / company tax.)
- **R-BS-5** — "Non-residents and expatriates face the same absence of income tax. However, work permit requirements, specific benefit-in-kind rules, and social security totalization agreements may apply. For complex expatriate situations, escalate to a Bahamian HR compliance specialist." (Non-resident / expatriate complex situations.)
- **R-BS-6** — "Client has outstanding NIB contributions, surcharges, or is subject to NIB enforcement. The 10% surcharge plus 1.5% compound monthly interest accumulates rapidly. Do not advise. Escalate to a Bahamian accountant or NIB-registered agent immediately." (NIB arrears or enforcement.)
- **R-BS-7** — "From July 2025, businesses with less than 50% zero or reduced-rated supplies cannot claim VAT refunds. Escalate to a DIR-registered VAT practitioner." (VAT refund claims.)  _(Higgs & Johnson 2025 Tax Legislative Updates)_

## Section 3 -- Transaction Pattern Library

This is the deterministic pre-classifier for bank statement lines. When a transaction matches a pattern below, apply the treatment directly. If none match, fall through to Tier 1 rules in Section 5.

**How to read this table.** Match by case-insensitive substring on the counterparty name or description. If multiple patterns match, use the most specific. NIB obligations are the primary personal tax cost in the Bahamas; VAT is relevant only if the client is VAT-registered.

### 3.1 NIB-Related Transactions

**NIB-Related Transactions**

| Pattern | Classification | Treatment | Notes |
| --- | --- | --- | --- |
| NIB CONTRIBUTION, NIB PAYMENT, NATIONAL INSURANCE | NIB contribution | Self-employed: deductible cost of doing business | Employee share is not a tax -- it funds social benefits |
| NIB C10, C10 FORM | NIB employer payment | Employer's NIB liability | C10 = monthly employer contribution form |
| NIB SURCHARGE, NIB PENALTY, NIB INTEREST | NIB penalty | NOT deductible | Penalties are not a business expense |
| NIB BENEFIT, NIB SICKNESS, NIB MATERNITY | NIB benefit received | Exclude from income analysis | These are social benefit receipts, not business income |

### 3.2 Business Licence Transactions

**Business Licence Transactions**

| Pattern | Classification | Treatment | Notes |
| --- | --- | --- | --- |
| BUSINESS LICENCE, BL RENEWAL, INLAND REVENUE BL | Business Licence fee | Deductible operating expense | Annual compliance cost |
| BUSINESS LICENCE PENALTY, LATE BL FEE | Business Licence penalty | NOT deductible |  |
| DIR PAYMENT, INLAND REVENUE PAYMENT | Regulatory payment | Verify type: BL tax, VAT, or RPT | Classify by supporting reference |

### 3.3 VAT-Related Transactions (VAT-Registered Clients)

**VAT-Related Transactions**

| Pattern | Classification | Treatment | Notes |
| --- | --- | --- | --- |
| VAT PAYMENT, DIR VAT, VAT RETURN PAYMENT | VAT liability payment | EXCLUDE | VAT liability payment, not an expense |
| VAT REFUND, DIR VAT REFUND | VAT refund received | EXCLUDE | VAT asset recovery, not income |
| [Invoice line] + 10% VAT | Sales invoice | Extract net (excl. VAT) as revenue | VAT collected is not income |
| [Invoice line] + 5% VAT | Reduced-rate sale | Extract net (excl. VAT) as revenue | Essentials category at 5% |

### 3.4 Income Patterns (Credits)

**Income Patterns (Credits)**

| Pattern | Classification | Treatment | Notes |
| --- | --- | --- | --- |
| CLIENT PAYMENT, INVOICE PAYMENT, TRANSFER IN [client name] | Business revenue | Self-employment income | If VAT-registered, extract net |
| ZELLE, PAYPAL TRANSFER, STRIPE PAYOUT, WIRE TRANSFER | Business revenue | Self-employment income | Confirm invoices match |
| SALARY, PAYROLL [employer name], WAGES | Employment income | Not self-employment | Covered by employer NIB; no income tax |
| RENTAL INCOME, RENT RECEIVED | Rental income | No income tax; RPT applies to the property | Report separately for Business Licence if above threshold |
| BANK INTEREST, INTEREST EARNED | Investment income | No income tax |  |
| GOVERNMENT GRANT, BAHAMAS INVEST GRANT | Check nature | Capital grants: exclude; revenue grants: include in Business Licence turnover |  |
| NIB BENEFIT, MATERNITY BENEFIT, RETIREMENT PENSION | Benefit payment | Exclude from business analysis | Social benefit, not taxable income |

### 3.5 Business Operating Expense Patterns (Debits) -- Deductible for Business Licence Purposes

**Business Operating Expense Patterns (Debits)**

| Pattern | Category | Treatment | Notes |
| --- | --- | --- | --- |
| OFFICE RENT, COMMERCIAL RENT [address] | Office rent | Deductible | Dedicated business premises |
| ACCOUNTANT FEES, CPA FEES, BOOKKEEPING | Professional fees | Deductible |  |
| ATTORNEY, LAWYER, LEGAL FEES (business) | Legal fees | Deductible | Must be business-related |
| OFFICE SUPPLIES, STATIONERY, PAPER, PRINTER INK | Office supplies | Deductible |  |
| MARKETING, GOOGLE ADS, META ADS, FACEBOOK ADS | Marketing | Deductible |  |
| BUSINESS INSURANCE, PROFESSIONAL LIABILITY | Insurance | Deductible | Business-related only |
| DOMAIN, HOSTING, AWS, DIGITALOCEAN, CLOUDFLARE | IT infrastructure | Deductible (operating) | Recurring subscription = expense |
| GOOGLE WORKSPACE, MICROSOFT 365, QUICKBOOKS | Software subscription | Deductible | Recurring = expense |
| BANK FEE, SERVICE CHARGE, WIRE FEE (business account) | Bank charges | Deductible | Business account only |
| TRAINING, CPD, COURSE, SEMINAR | Training | Deductible | Must relate to current business |

### 3.6 Expense Patterns -- NOT Deductible

**Expense Patterns -- NOT Deductible**

| Pattern | Category | Treatment | Notes |
| --- | --- | --- | --- |
| RESTAURANT, DINING, CLIENT MEAL, ENTERTAINMENT | Entertainment | NOT deductible | Personal/entertainment |
| PERSONAL WITHDRAWAL, DRAWINGS, ATM (personal) | Drawings | NOT deductible | Owner drawings |
| GROCERIES, SUPERMARKET, PERSONAL SHOPPING | Personal | NOT deductible |  |
| FINE, COURT FINE, TRAFFIC VIOLATION | Fines | NOT deductible | Public policy |
| INCOME TAX PAYMENT | N/A | There is no income tax | If seen, verify it is not a VAT, BL, or RPT payment |

### 3.7 Exclusions (Neither Income nor Expense)

**Exclusions (Neither Income nor Expense)**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| INTERNAL TRANSFER, OWN ACCOUNT | EXCLUDE | Between own accounts |
| LOAN REPAYMENT, MORTGAGE PRINCIPAL | EXCLUDE | Loan principal is not an expense |
| VAT PAYMENT, DIR VAT | EXCLUDE | VAT liability settlement |
| PROVISIONAL TAX, ADVANCE TAX | N/A -- no income tax in Bahamas | If seen, classify carefully; may be VAT instalment |
| STAMP DUTY PAYMENT | EXCLUDE from operating expenses | One-time property transaction cost, not recurring |

### 3.8 Bahamian Banks -- Statement Format Reference

**Bahamian Banks -- Statement Format Reference**

| Bank | Common Patterns | Notes |
| --- | --- | --- |
| Commonwealth Bank | TRANSFER, DD, PAYMENT, DEBIT CARD | Most common retail bank; PDF and online export |
| Bank of The Bahamas | TRANSFER, DIRECT DEBIT, DRAFT | Government-linked; PDF statements |
| Scotiabank Bahamas | PAYMENT, TFR, DD, CARD | Canadian bank; CSV available |
| FirstCaribbean (CIBC) | TRANSFER, PAYMENT, CHARGE | PDF; limited CSV |
| Fidelity Bank Bahamas | TRANSFER, WIRE, DEBIT | Business accounts common |
| Wise / Revolut Business | TRANSFER, CONVERSION, CARD PAYMENT | Clean CSV; multi-currency -- use BSD or USD amounts (1:1 peg) |

### Example 1 -- Employed Individual, Annual Salary BSD 45,000

**Scenario:** Maria is employed full-time at a Nassau hotel. Annual salary BSD 45,000.

**Step 1 -- Personal income tax:** BSD 0. No personal income tax exists in the Bahamas.

**Step 2 -- NIB contributions:**
- Weekly salary: 45,000 ÷ 52 = BSD 865.38 -- ABOVE the weekly ceiling of BSD 810
- Insurable wage = ceiling: BSD 810/week
- Employee NIB: 4.65% × BSD 810 = BSD 37.67/week × 52 = **BSD 1,958/year**
- Employer NIB: 6.65% × BSD 810 = BSD 53.87/week × 52 = **BSD 2,801/year**
- Take-home: BSD 45,000 − BSD 1,958 = **BSD 43,042/year** (no income tax deducted)

**Step 3 -- No other obligations:** No Business Licence (employed). No VAT (not in business). No income tax return to file.

**Summary:**
```
Annual salary:            BSD 45,000
Less: Employee NIB:       BSD (1,958)
Net take-home:            BSD 43,042
Income tax:               BSD 0
```

### Example 2 -- Self-Employed Freelancer, Annual Revenue BSD 30,000

**Scenario:** James is a self-employed web developer. Annual revenue BSD 30,000. Below VAT threshold.

**Step 1 -- Personal income tax:** BSD 0.

**Step 2 -- NIB contributions (self-employed rate 10.30%):**
- Weekly earnings: 30,000 ÷ 52 = BSD 576.92/week -- BELOW the ceiling of BSD 810
- Insurable wage = actual earnings: BSD 576.92/week
- Annual NIB: 10.30% × BSD 30,000 = **BSD 3,090/year**
- Monthly NIB payment (due 15th of following month): 3,090 ÷ 12 = **BSD 257.50/month**

**Step 3 -- Business Licence:**
- Turnover ≤ BSD 50,000: flat fee **BSD 100**
- Renewal filing by 31 January; payment by 31 March

**Step 4 -- VAT:** BSD 30,000 < BSD 100,000 threshold. **No VAT registration required** (voluntary registration available).

**Step 5 -- No RPT** (renting; does not own property).

**Summary:**
```
Annual revenue:           BSD 30,000
NIB (10.30%):             BSD (3,090)
Business Licence fee:     BSD (100)
Income tax:               BSD 0
Approximate net:          BSD 26,810
```

### Example 3 -- Self-Employed at NIB Ceiling, BSD 60,000 Revenue

**Scenario:** Sandra is a self-employed accountant, revenue BSD 60,000/year.

**Step 1 -- Personal income tax:** BSD 0.

**Step 2 -- NIB contributions:**
- Weekly earnings: 60,000 ÷ 52 = BSD 1,153.85/week -- ABOVE ceiling of BSD 810
- Insurable wage = ceiling: BSD 810/week
- Annual NIB: 10.30% × BSD 810 × 52 = 10.30% × BSD 42,120 = **BSD 4,338/year**
- Earnings above ceiling (BSD 1,153.85 − BSD 810 = BSD 343.85/week) attract NO additional NIB

**Step 3 -- Business Licence:**
- Turnover BSD 60,000 (in band BSD 50,001 -- BSD 500,000): 0.50% × BSD 60,000 = **BSD 300**

**Step 4 -- VAT:** BSD 60,000 < BSD 100,000 threshold. Not required; may register voluntarily.

**Summary:**
```
Annual revenue:           BSD 60,000
NIB (at ceiling):         BSD (4,338)
Business Licence fee:     BSD (300)
Income tax:               BSD 0
Approximate net:          BSD 55,362
```

### Example 4 -- VAT-Registered Consultant, BSD 180,000 Revenue

**Scenario:** David is a self-employed management consultant, revenue BSD 180,000/year including VAT charged at 10%. VAT registered.

**Step 1 -- Revenue (net of VAT):**
- BSD 180,000 includes 10% VAT. Net revenue = BSD 180,000 ÷ 1.10 = **BSD 163,636**
- VAT collected = BSD 163,636 × 10% = BSD 16,364 (liability to DIR, not income)

**Step 2 -- Personal income tax:** BSD 0.

**Step 3 -- NIB:**
- Weekly net earnings: 163,636 ÷ 52 = BSD 3,146 -- ABOVE ceiling
- NIB = 10.30% × BSD 810 × 52 = **BSD 4,338/year**

**Step 4 -- Business Licence:**
- Turnover BSD 163,636 (band BSD 50,001 -- BSD 500,000): 0.50% × BSD 163,636 = **BSD 818**
- Certified turnover statement by accountant required (>BSD 100,000)

**Step 5 -- VAT obligations:**
- Quarterly VAT return (turnover ≤ BSD 5M)
- Due within 21 days of end of each quarter
- Pay net VAT (output VAT collected minus input VAT on business purchases)

**Summary:**
```
Gross revenue invoiced:   BSD 180,000
Less: VAT collected:      BSD (16,364)
Net business revenue:     BSD 163,636
NIB (at ceiling):         BSD (4,338)
Business Licence fee:     BSD (818)
Income tax:               BSD 0
```

### Example 5 -- Property Purchase, Stamp Duty Calculation

**Scenario:** Nicole purchases a residential property in Nassau for BSD 250,000.

**Step 1 -- Personal income tax on transaction:** BSD 0.

**Step 2 -- Stamp duty (graduated, shared 50/50 buyer/seller by default):**
- First BSD 20,000 at 4%: BSD 20,000 × 4% = BSD 800
- Next BSD 30,000 (BSD 20,001 -- BSD 50,000) at 6%: BSD 30,000 × 6% = BSD 1,800
- Next BSD 50,000 (BSD 50,001 -- BSD 100,000) at 8%: BSD 50,000 × 8% = BSD 4,000
- Remaining BSD 150,000 (above BSD 100,000) at 10%: BSD 150,000 × 10% = BSD 15,000
- **Total stamp duty: BSD 21,600**
- Nicole's share (buyer, 50%): **BSD 10,800**
- Seller's share (50%): **BSD 10,800**

*Arithmetic check: 800 + 1,800 + 4,000 + 15,000 = BSD 21,600 ✓*

**Step 3 -- First-time buyer exemption:** If Nicole is a first-time buyer purchasing a dwelling up to BSD 500,000, she is **exempt** from stamp duty. (Source: Churchill & Jones Realty stamp duty guide)

**Step 4 -- VAT provisional invoice (from July 2025):** Before executing conveyance, parties must obtain a provisional VAT invoice from DIR. (Source: Higgs & Johnson 2025 Tax Legislative Updates)

**Step 5 -- Payment deadline:** Stamp duty due **within 6 months** of transaction closing.

### Example 6 -- Employer Payroll NIB (3 Employees)

**Scenario:** Small business with 3 employees, all earning BSD 600/week.

**NIB per employee per week:**
- Employee share: 4.65% × BSD 600 = BSD 27.90
- Employer share: 6.65% × BSD 600 = BSD 39.90
- Combined per employee: BSD 67.80/week

**NIB for all 3 employees per month (≈4.333 weeks):**
- Total employee NIB: BSD 27.90 × 3 × 4.333 = BSD 362.95/month
- Total employer NIB: BSD 39.90 × 3 × 4.333 = BSD 518.74/month
- **Total monthly NIB (C10 form): BSD 881.70**
- Due: **15th of the following month** via C10 form

*BSD 600/week is below the BSD 810 ceiling, so full earnings are insurable. Arithmetic: 27.90 + 39.90 = BSD 67.80/employee/week. 67.80 × 3 = 203.40/week × 4.333 = BSD 881.51 ≈ BSD 882/month ✓*

### 5.1 The Fundamental Rule -- No Personal Income Tax

- **No personal income tax legislation** — There is no personal income tax legislation in the Bahamas. No individual is required to: File an annual income tax return with any authority; Declare employment or self-employment income to a tax collector; Pay tax on salary, professional fees, rental income, dividends, interest, or capital gains. The primary fiscal obligation for individuals is NIB contributions, which are social insurance premiums, not income tax.

### 5.2 NIB Contribution Calculation Rules

- **Employed individuals calculation steps** — 1. Determine weekly insurable wage: the lower of (a) actual weekly gross earnings or (b) the weekly ceiling (currently BSD 810). 2. Employee share: insurable wage × 4.65%. 3. Employer share: insurable wage × 6.65%. 4. Employer remits both shares monthly via C10 form by the 15th of the following month.
- **Self-employed individuals calculation steps** — 1. Determine weekly insurable earnings: the lower of (a) actual weekly net self-employment earnings or (b) the weekly ceiling (BSD 810). 2. Self-employed rate: insurable earnings × 10.30% (covers both employee and employer shares). 3. Register using Form R1 within 10 working days of commencing self-employment. 4. Pay monthly by the 15th of the following month.  _(nib-bahamas.com/Registration)_
- **Earnings above the weekly ceiling** — No NIB is payable on earnings above BSD 810/week. The ceiling applies per week, not per year.

### 5.3 NIB Benefits Funded by Contributions

(Source: nib-bahamas.com/about-nib/benefits-and-assistance/)

Ten cash benefits are funded: Sickness, Maternity, Funeral, Retirement (Pensions), Invalidity, Survivorship, Unemployment, Industrial Injury, Disablement, and Death.

**NIB Benefits (2025)**  _(nib-bahamas.com/about-nib/benefits-and-assistance/)_

| Benefit (2025) | Amount |
| --- | --- |
| Minimum retirement pension | ~BSD 364/month |
| Maternity grant (from Jul 2025) | BSD 570 |
| Funeral benefit | BSD 2,060 (rising to BSD 2,100 from Jul 2026) |

- **Qualification for benefits** — To qualify for most benefits, the claimant must have accumulated sufficient contribution weeks. Contributions must be current (no arrears).

### 5.4 VAT: When It Applies to Individuals

- **VAT applicability** — VAT is relevant to individuals only if they are carrying on a business (self-employed, sole trader). Pure employees have no VAT obligation.
- **VAT registration threshold** — BSD 100,000 in annual taxable supplies. Must register within 14 days of becoming liable.  _(inlandrevenue.finance.gov.bs/value-added-tax/faqs/)_
- **Filing and payment** — General (turnover ≤ BSD 5M): quarterly return, due 21 days after end of quarter. Large taxpayer (turnover > BSD 5M): monthly return, due 14 days after end of month. E-commerce businesses, hotels, and vacation rental services: must register regardless of turnover.
- **Record-keeping** — Maintain accounting records for at least 5 years.  _(Inland Revenue VAT FAQs)_

### 5.5 Business Licence: Who Needs One

- **Who needs a licence** — Every person carrying on business in the Bahamas must hold a Business Licence -- including self-employed individuals and sole traders.  _(Inland Revenue Business Licence)_
- **Key deadlines** — New business: obtain licence before commencing operations. Annual renewal application: 31 January (for the current year). Licence tax payment: 31 March. Business cessation notification to DIR: within 14 days, no later than 31 December.
- **Financial statement requirements by turnover threshold** — > BSD 100,000: certified turnover statement by qualified accountant. BSD 250,000 -- BSD 5,000,000: review engagement report. > BSD 5,000,000: audited financial statements.  _(Inland Revenue Business Licence rates)_

### 5.6 Real Property Tax (RPT): Rules

- **RPT applicability** — RPT applies to owners of real property. Rates depend on classification.  _(inlandrevenue.finance.gov.bs/real-property-tax/faqs-rpt/)_

**Owner-Occupied Residential**  _(inlandrevenue.finance.gov.bs/real-property-tax/faqs-rpt/)_

| Assessed value | Rate |
| --- | --- |
| First BSD 300,000 | Exempt |
| BSD 300,001 -- BSD 500,000 | 0.625% |
| Above BSD 500,000 | 1.0% |
| Annual cap | BSD 150,000 |

**Residential (4 units or fewer, not owner-occupied)**  _(inlandrevenue.finance.gov.bs/real-property-tax/faqs-rpt/)_

| Assessed value | Rate |
| --- | --- |
| Up to BSD 75,000 | BSD 300 flat |
| Above BSD 75,000 | 0.625% |

**Commercial / 5+ units / Foreign-Owned Rentals**  _(inlandrevenue.finance.gov.bs/real-property-tax/faqs-rpt/)_

| Assessed value | Rate |
| --- | --- |
| First BSD 500,000 | 0.75% |
| BSD 500,001 -- BSD 2,000,000 | 1.0% |
| Above BSD 2,000,000 | 1.5% |
| Annual cap (from 2025 amendment) | BSD 150,000 |

**Vacant Land -- Foreign-Owned Only**  _(inlandrevenue.finance.gov.bs/real-property-tax/faqs-rpt/)_

| Assessed value | Rate |
| --- | --- |
| First BSD 7,000 | BSD 100 flat |
| Above BSD 7,000 | 2.0% |

- **RPT deadlines and discounts** — Annual payment deadline: 31 March. Early payment discount: 10% if paid by 31 March. Pensioner discount (Bahamian citizen, 65+): 50% off balance. Annual surcharge if unpaid by 31 December: 5% surcharge, plus 5% interest on outstanding amounts. Property declaration to DIR: by 31 December each year.

### 5.7 Stamp Duty on Real Estate Conveyances

**Stamp Duty on Real Estate Conveyances**  _(Churchill & Jones Realty stamp duty guide; Higgs & Johnson 2025 Tax Legislative Updates)_

| Consideration | Stamp duty rate |
| --- | --- |
| Up to BSD 20,000 | 4% |
| BSD 20,001 -- BSD 50,000 | 6% |
| BSD 50,001 -- BSD 100,000 | 8% |
| Above BSD 100,000 | 10% |

- **Split, exemption, and deadlines** — Normally split equally (50/50) between buyer and seller unless otherwise agreed. First-time buyer exemption: Exempt on a dwelling house or vacant land for a dwelling up to BSD 500,000. Stamp duty on mortgage instruments: approximately 1% of mortgage amount [RESEARCH GAP -- reviewer to confirm exact current rate]. Leases < 5 years: 2.5% of annual rent. Payment deadline: within 6 months of transaction closing. From 1 July 2025: Parties must obtain a provisional VAT invoice from DIR before executing conveyance instruments. Failure: 3% of consideration penalty (joint and several: transferor + agent).  _(Higgs & Johnson 2025 Tax Legislative Updates)_

### 5.8 Non-Deductible Items

**Non-Deductible Items**

| Item | Reason |
| --- | --- |
| Entertainment, client meals | Personal/entertainment; not wholly for business |
| Owner drawings | Not an expense |
| NIB surcharges and penalties | Penalties are not operating costs |
| Business Licence late penalties | Penalties |
| Personal living expenses | Not business-related |
| Court fines, traffic violations | Public policy |
| Income tax payments | There is no income tax; if a payment is seen, verify its nature |

### 6.1 Home Office Deduction (Business Licence Cost Basis)

There is no income tax deduction system in the Bahamas, but Business Licence fees are based on turnover (not profit), so home-office cost allocation is relevant for understanding profitability rather than for reducing a declared tax base.

For VAT-registered clients, the business-use proportion of home utilities may affect which input VAT is creditable.

**Flag for reviewer:** Confirm whether client's business address is home or commercial, and confirm what proportion of home expenses are genuinely attributable to the business. The Bahamas has no statutory guidance on this proportion -- reviewer must apply judgment.

**Conservative default:** 0% home office allocation until reviewer confirms.

### 6.2 Vehicle Business Use

Relevant for VAT input tax recovery (if VAT-registered) and for understanding true business costs.

- Client must document approximate business vs personal mileage
- No statutory mileage rate exists in the Bahamas [RESEARCH GAP -- reviewer to confirm any DIR guidance]

**Conservative default:** 0% business use until confirmed.

### 6.3 NIB Contribution Status Verification

Before advising a client, confirm:
- Are they registered with NIB? (nine-digit NIB number assigned on registration)
- Are contributions current? (check with NIB directly)
- Is the client voluntarily insured (if not employed or self-employed in the traditional sense)?

Arrears with NIB accumulate rapidly (10% surcharge + 1.5%/month compound). If arrears are suspected, escalate immediately.

### 6.4 VAT Input Tax Apportionment (Mixed-Use Businesses)

If a VAT-registered business makes both taxable and exempt supplies, input VAT must be apportioned. Partial exemption calculation:

- Standard method: proportion of taxable to total supplies (by value)
- From July 2025: businesses with < 50% zero/reduced-rated supplies cannot claim VAT refunds (Source: Higgs & Johnson 2025)

**Flag for reviewer:** Confirm supply mix and apportionment method for VAT-registered clients with exempt supplies.

### 6.5 Real Property Tax Assessment Disputes

The assessed value (used for RPT rate bands) is set by DIR and may differ from market value. A property owner may dispute the assessment.

**Flag for reviewer:** If client believes assessed value is overstated, escalate to a Bahamian real property attorney or appraiser before filing.

### 6.6 Business Licence Turnover Definition

The turnover figure used for Business Licence purposes is gross revenue (not net profit, not value-added). For VAT-registered businesses, confirm whether turnover is inclusive or exclusive of VAT for Business Licence computation purposes. [RESEARCH GAP -- reviewer to confirm whether DIR uses gross or VAT-exclusive turnover for Business Licence rate band computation]

## Section 7 -- Working Paper Template

```
BAHAMAS TAX COMPLIANCE -- WORKING PAPER
Tax Year: 2025
Client: ___________________________
Employment Status: Employed / Self-Employed / Both
NIB Number: ___________________________
VAT Registration Number (if applicable): ___________________________
Business Licence Number (if applicable): ___________________________

A. PERSONAL INCOME TAX
   A1. PIT due:    BSD 0 (no PIT in the Bahamas)
   A2. PIT return to file:    NONE

B. NIB CONTRIBUTIONS
   B1. Employment type:    Employed / Self-Employed / Voluntary
   B2. Annual gross earnings / net self-employment earnings:    BSD ___________
   B3. Weekly earnings:    BSD ___________
   B4. Weekly insurable wage (lesser of B3 and BSD 810 ceiling):    BSD ___________
   B5. Rate: Employed-employee 4.65% / Self-employed 10.30%:    ___%
   B6. Annual NIB contribution:    BSD ___________
      (= B4 × B5 × 52 weeks)
   B7. Monthly NIB payment (B6 ÷ 12):    BSD ___________
   B8. Payment due date: 15th of each following month    [ ]
   B9. Employer NIB (if applicable, 6.65% × B4 × 52):    BSD ___________

C. BUSINESS LICENCE (Self-Employed / Sole Traders Only)
   C1. Annual gross turnover:    BSD ___________
   C2. Licence tax rate (from rate schedule):    ___%  or  BSD 100 flat
   C3. Annual licence tax:    BSD ___________
   C4. Renewal application filed by 31 January:    [ ]
   C5. Licence tax paid by 31 March:    [ ]
   C6. Financial statement requirement:
       [ ] > BSD 100k: certified turnover statement
       [ ] BSD 250k -- BSD 5M: review engagement report
       [ ] > BSD 5M: audited financial statements

D. VAT (VAT-Registered Clients Only)
   D1. VAT registration number:    ___________
   D2. Annual taxable supplies:    BSD ___________
   D3. Filing frequency: Quarterly (≤ BSD 5M) / Monthly (> BSD 5M):    ___________
   D4. Output VAT collected (period):    BSD ___________
   D5. Input VAT creditable (period):    BSD ___________
   D6. Net VAT due (D4 - D5):    BSD ___________
   D7. Return and payment due (21 days / 14 days after period end):    ___________

E. REAL PROPERTY TAX (Property Owners Only)
   E1. Property classification:    Owner-Occupied / Non-Owner-Occupied / Commercial / Vacant
   E2. Assessed value:    BSD ___________
   E3. RPT computed per rate table:    BSD ___________
   E4. Early payment discount (10% if paid by 31 March):    BSD ___________
   E5. Net RPT payable:    BSD ___________
   E6. Payment due: 31 March    [ ]
   E7. Property declaration to DIR by 31 December:    [ ]

F. STAMP DUTY (Real Estate Transactions Only)
   F1. Consideration (property value):    BSD ___________
   F2. Stamp duty (graduated per rate table):    BSD ___________
   F3. Client's share (typically 50%):    BSD ___________
   F4. First-time buyer exemption applies?    Yes / No
   F5. Provisional VAT invoice obtained from DIR?    [ ] (required from Jul 2025)
   F6. Payment due within 6 months of closing:    [ ]

REVIEWER FLAGS:
   [ ] NIB registration confirmed and contributions current?
   [ ] Employment / self-employment status confirmed?
   [ ] Business Licence obtained before operations commenced?
   [ ] VAT registration status confirmed (above/below BSD 100k threshold)?
   [ ] RPT assessed value verified?
   [ ] Any stamp duty transaction in period -- provisional VAT invoice obtained?
   [ ] No PIT return required -- confirmed with client?
   [ ] All T2 items flagged for reviewer?
```

### Bahamian Bank Statement Formats

**Bahamian Bank Statement Formats**

| Bank | Format | Key Fields | Notes |
| --- | --- | --- | --- |
| Commonwealth Bank (Bahamas) | PDF, online export | Date, Description, Debit, Credit, Balance | Most common retail bank; description contains counterparty |
| Bank of The Bahamas | PDF | Date, Particulars, Withdrawals, Deposits | Government-linked bank; less structured descriptions |
| Scotiabank Bahamas | PDF, CSV | Value Date, Description, Amount, Balance | Canadian multinational; clean CSV export |
| FirstCaribbean (CIBC) | PDF | Date, Description, Debit, Credit | Caribbean regional bank |
| Fidelity Bank Bahamas | PDF, CSV | Date, Description, Amount, Balance | Common for business accounts |
| Wise / Revolut Business | CSV | Date, Counterparty, Amount, Currency, Reference | Clean data; multi-currency; note BSD = USD (1:1 peg) |

### Key Bahamian Banking and Tax Terms

**Key Bahamian Banking and Tax Terms**

| Term | Meaning | Classification Hint |
| --- | --- | --- |
| C10 FORM | Monthly NIB employer contribution form | NIB payment -- business expense |
| R1 FORM | NIB self-employed / voluntary registration form | Registration, not a payment |
| DIR | Department of Inland Revenue | VAT / BL / RPT authority |
| NIB | National Insurance Board | Social contributions authority |
| BL | Business Licence | Annual licence fee |
| RPT | Real Property Tax | Annual property tax |
| STAMP DUTY | Conveyance tax | Property transaction tax |
| BSD / B$ | Bahamian Dollar | Pegged 1:1 to USD; treat as USD equivalent |
| WIRE / TT | Telegraphic Transfer / Wire | International payment -- check invoices |
| CONCH, WALK-IN PAYMENT | In-person DIR/NIB payment | Often for BL or RPT |
| NASSAU, FREEPORT | City references | No tax difference by island for NIB/BL/VAT |

### USD vs BSD Amounts

- **USD vs BSD equivalence** — The Bahamian Dollar is pegged 1:1 to the US Dollar and freely exchangeable. Bank statements may show USD amounts interchangeably. For all tax computations, treat BSD and USD as equivalent. Do not apply any currency conversion.

## Section 9 -- Onboarding Fallback

If the client provides a bank statement but cannot answer onboarding questions immediately:

1. Classify all transactions using the pattern library (Section 3)
2. Mark all Tier 2 items as "PENDING -- reviewer must confirm"
3. Apply conservative defaults (Section 1)
4. Generate the working paper (Section 7) with clear flags
5. Confirm immediately: "There is no personal income tax in the Bahamas. No income tax return is required."
6. Present the following questions to the client:

```
ONBOARDING QUESTIONS -- BAHAMAS TAX COMPLIANCE
1. Are you an employee, self-employed, or both?
2. What is your approximate annual gross income (or annual turnover if self-employed)?
3. Are you registered with the National Insurance Board (NIB)?
   If yes, what is your NIB number?
   If self-employed, do you pay your monthly NIB contributions by the 15th?
4. Do you hold a Business Licence?
   If yes, when is your renewal due and have you filed/paid for 2025?
5. Are you registered for VAT with the Department of Inland Revenue?
   If yes, what is your annual turnover?
6. Do you own any real property in the Bahamas?
   If yes, what classification (owner-occupied / rental / commercial)?
   Have you paid your 2025 Real Property Tax?
7. Did you buy or sell any real estate in 2025?
   If yes, has stamp duty been paid within 6 months of closing?
8. Do you employ any staff?
   If yes, are you filing C10 forms and paying NIB by the 15th monthly?
```

### Key Legislation and Authority References

**Key Legislation and Authority References**

| Topic | Reference / Authority |
| --- | --- |
| No personal income tax | PwC Worldwide Tax Summaries -- Bahamas Individual (reviewed 24 Feb 2026); no enabling legislation exists |
| NIB contribution rates | National Insurance Board -- nibrateincrease.com; nib-bahamas.com; PwC Individual Other Taxes |
| NIB insurable wage ceiling | nib-bahamas.com/2024-adjustments-to-the-insurable-wage-ceiling-pensions-and-grants/ |
| NIB biennial review mechanism | nib-bahamas.com/biennial-adjustments-to-pensions-grants-and-the-wage-ceiling |
| NIB registration (Form R1) | nib-bahamas.com/Registration |
| NIB employer obligations (C10) | Workzoom Bahamas Payroll NIB Compliance Guide; NIB Contributions FAQ |
| VAT rates and administration | Inland Revenue -- inlandrevenue.finance.gov.bs/value-added-tax/about-vat/ |
| VAT reduced rate (5%, from Sep 2025) | PM Davis announcement -- bahamas.gov.bs; Higgs & Johnson 2025 |
| VAT registration thresholds | inlandrevenue.finance.gov.bs/value-added-tax/faqs/ |
| VAT penalties | inlandrevenue.finance.gov.bs/value-added-tax/fees-fines-and-penalties/ |
| Business Licence rates | inlandrevenue.finance.gov.bs/tax-incentives/business-licence-new-rates-1/ |
| Business Licence penalties | inlandrevenue.finance.gov.bs/business-licence/fees-fines-and-penalties-bl/ |
| Real Property Tax rates | inlandrevenue.finance.gov.bs/real-property-tax/faqs-rpt/ |
| RPT 2025 amendments (BSD 150k cap) | Real Property Tax Amendment Bill 2025 -- laws.bahamas.gov.bs |
| Stamp duty rates | Churchill & Jones Realty -- churchilljonesrealty.com/stamp-duties-taxes/ |
| Stamp duty + VAT invoice rule (Jul 2025) | Higgs & Johnson 2025 Tax Legislative Updates |
| Customs duties (general) | PwC Corporate Other Taxes; Bahamas Customs -- bahamascustoms.gov.bs |
| Minimum wage (BSD 6.50/hr from Jan 2023) | WageIndicator; Playroll Bahamas minimum wage guide |
| Procedural obligations overview | Higgs & Johnson -- higgsjohnson.com/principal-procedural-obligations-of-a-taxpayer-in-the-bahamas/ |

### Penalties Summary Table

**Penalties Summary Table**

| Obligation | Penalty |
| --- | --- |
| NIB late payment | 10% surcharge + 1.5% compound interest/month (Source: NIB Contributions FAQ) |
| NIB failure to register (employer) | Fines up to BSD 5,000 + prosecution (Source: Workzoom; Higgs & Johnson) |
| VAT late filing | BSD 100 fixed + 10% of unpaid tax (Source: Inland Revenue VAT Fines) |
| VAT monthly interest | 1.5% per month on outstanding balance |
| VAT late registration | Retroactive back-tax + penalties imposed by DIR |
| Business Licence late application | BSD 100 (Source: inlandrevenue.finance.gov.bs/business-licence/fees-fines-and-penalties-bl/) |
| Business Licence late tax payment | 10% of tax liability |
| Business Licence interest (30+ days) | 5% per annum |
| RPT annual surcharge (unpaid by 31 Dec) | 5% surcharge + 5% interest |
| Stamp duty -- no provisional VAT invoice | 3% of consideration (joint/several: transferor + agent) (Source: Higgs & Johnson 2025) |
| Operating without Business Licence | Prosecution |

### Test Suite

**Test 1 -- Employee, salary at ceiling.**
Input: Employed, weekly salary BSD 950 (above BSD 810 ceiling).
Expected: Insurable wage = BSD 810/week. Employee NIB = 4.65% × BSD 810 = BSD 37.67/week = BSD 1,958/year. No income tax. Take-home ≈ BSD 950 × 52 − BSD 1,958 = BSD 49,400 − BSD 1,958 = BSD 47,442/year.

**Test 2 -- Employee, salary below ceiling.**
Input: Employed, weekly salary BSD 500 (below BSD 810 ceiling).
Expected: Insurable wage = BSD 500/week. Employee NIB = 4.65% × BSD 500 = BSD 23.25/week = BSD 1,209/year. Employer NIB = 6.65% × BSD 500 = BSD 33.25/week = BSD 1,729/year. No income tax.

**Test 3 -- Self-employed, below ceiling.**
Input: Self-employed, annual net earnings BSD 25,000.
Expected: Weekly = BSD 480.77 (below BSD 810). Annual NIB = 10.30% × BSD 25,000 = BSD 2,575. Monthly payment = BSD 214.58. Business Licence: BSD 100 flat (below BSD 50k). No income tax.

**Test 4 -- Self-employed, above ceiling.**
Input: Self-employed, annual net earnings BSD 100,000.
Expected: Weekly = BSD 1,923 (above BSD 810). Insurable = BSD 810/week. Annual NIB = 10.30% × BSD 810 × 52 = BSD 4,338. Business Licence: 0.50% × BSD 100,000 = BSD 500. No income tax.

**Test 5 -- VAT registration threshold.**
Input: Self-employed, annual taxable supplies BSD 95,000.
Expected: Below BSD 100,000 threshold. VAT registration NOT required (but voluntary registration available). No VAT return to file.

**Test 6 -- Stamp duty, first-time buyer.**
Input: First-time buyer, purchasing a dwelling for BSD 400,000.
Expected: Normally stamp duty would be: BSD 800 (first BSD 20k) + BSD 1,800 (next BSD 30k) + BSD 4,000 (next BSD 50k) + BSD 30,000 (remaining BSD 300k at 10%) = BSD 36,600 total. BUT first-time buyer exemption applies (dwelling ≤ BSD 500k). Stamp duty = BSD 0.

**Test 7 -- Stamp duty, non-exempt buyer.**
Input: Second-property buyer, purchasing for BSD 75,000.
Expected: BSD 800 (4% × 20k) + BSD 1,800 (6% × 30k) + BSD 2,000 (8% × 25k) = BSD 4,600 total. Split equally: each party pays BSD 2,300.
*Arithmetic check: 20,000 × 4% = 800; 30,000 × 6% = 1,800; 25,000 × 8% = 2,000. Sum = BSD 4,600. Each party BSD 2,300 ✓*

**Test 8 -- No income tax return.**
Input: Any individual (employed or self-employed) asks if they need to file an income tax return in the Bahamas.
Expected: No. There is no personal income tax and no tax return to file. The only individual compliance obligations are NIB (social contributions), Business Licence (if in business), and VAT (if turnover ≥ BSD 100,000).

**Test 9 -- Employer NIB (C10 Form).**
Input: Employer with 2 employees, each earning BSD 700/week.
Expected: BSD 700 < BSD 810 ceiling; full earnings are insurable. Per employee/week: employee 4.65% × 700 = BSD 32.55; employer 6.65% × 700 = BSD 46.55. Combined per employee: BSD 79.10/week. For 2 employees monthly ≈ BSD 79.10 × 2 × 4.333 = BSD 685.78 ≈ BSD 686/month. Due 15th of following month via C10 form.

**Test 10 -- RPT, owner-occupied property.**
Input: Owner-occupied residential property, assessed value BSD 450,000.
Expected: First BSD 300,000 exempt. Next BSD 150,000 at 0.625%: BSD 150,000 × 0.625% = BSD 937.50. Total RPT = BSD 937.50. If paid by 31 March: 10% early-payment discount = BSD 93.75 saving; net BSD 843.75.

## PROHIBITIONS

- NEVER compute, estimate, or imply that the Bahamas levies personal income tax on individuals
- NEVER generate an income tax return or income declaration form for a Bahamian individual
- NEVER confuse NIB contributions (social insurance) with income tax -- they are separate systems with separate authorities
- NEVER skip NIB compliance guidance -- it is the primary individual tax obligation and penalties accumulate rapidly
- NEVER advise a self-employed client to start business without first addressing Business Licence and NIB registration
- NEVER allow entertainment expenses as deductible without reviewer confirmation
- NEVER omit the provisional VAT invoice warning for real estate transactions (required from July 2025)
- NEVER present these computations as definitive without reviewer sign-off -- always label as estimated
- NEVER confuse BSD (Bahamian Dollar) with a different currency -- it is pegged 1:1 to USD
- NEVER apply a stamp duty first-time buyer exemption without confirming it is a dwelling (not commercial) and consideration ≤ BSD 500,000

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
