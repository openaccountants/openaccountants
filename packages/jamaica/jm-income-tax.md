---
name: jm-income-tax
description: >
  Jamaica personal income tax for year of assessment 2026, for resident and
  non-resident individuals, self-employed persons filing Form S04 and S04a, and
  employees with other income. Covers the income tax threshold (J$1,902,360 a year
  from 1 April 2026, effective J$1,876,614 for 2026), the 25% and 30% rates and the
  J$6 million break on statutory income, pension and age reliefs, Education Tax,
  NHT and NIS for the self-employed, the prior-year loss restriction, filing on 15
  March and quarterly estimates. Trigger on Jamaica income tax, TAJ, S04, S04a,
  IT01, statutory income, tax-free threshold, self-employed tax Jamaica, Education
  Tax, NHT, NIS. Built from Tax Administration Jamaica publications; not reviewed
  by an accountant.
version: 1.0
jurisdiction: JM
tax_year: 2026
last_updated: 2026-11-14
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
category: international
tier: 2
domain: income-tax
type: computation
---

# Jamaica Personal Income Tax v1.0

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Who this applies to

Individuals with income chargeable to Jamaican income tax for the **year of assessment 2026** (calendar year 1 January to 31 December 2026). The authority is Tax Administration Jamaica (TAJ). Amounts are Jamaican dollars (J$, JMD).

| Field | Value |
|---|---|
| Tax year | Year of assessment 2026, 1 January to 31 December 2026 |
| Who is in | Resident individuals (income from all sources, local or overseas); non-residents with Jamaica-source income; self-employed persons, including partners and Jamaican nationals employed to non-residents (embassies, overseas employers), whom TAJ treats as self-employed |
| Who is out | Companies (use `jm-corporate-income-tax`); employer payroll mechanics (use `jm-payroll-social`); GCT (use `jamaica-gct`); estates and trusts |
| Main returns | Form S04 (self-employed annual return), Form S04a (declaration of estimated income), IT01 (individuals with other income) |
| Portal | TAJ online services, https://www.jamaicatax.gov.jm (an e-Services account is needed; all income tax returns are filed online) |

Self-employed persons who owe no income tax but owe Education Tax, NIS or NHT still file Form S04 to account for those contributions.

### Refusals and boundaries

- **R-JM-1, residency unknown.** Residence decides whether the threshold applies. Do not compute until it is confirmed.
- **R-JM-2, company or partnership return.** Companies file IT02 and partnerships IT03; this skill covers the individual partner's own S04 only.
- **R-JM-3, non-resident with complex sourcing or treaty claims.** Escalate; a non-resident has no threshold and pays 25% unless a treaty sets another rate.
- **R-JM-4, estate or trust income.** Out of scope; escalate.
- **R-JM-5, arrears or TAJ enforcement.** Escalate to a practitioner; do not advise on settlement.
- **R-JM-6, GCT return requested.** Use `jamaica-gct`.
- **R-JM-7, property transfer tax or stamp duty.** Transactional taxes outside this skill; escalate.

## Rates, bands and thresholds

The 25% and 30% rates apply to **statutory income** (total income less exemptions and deductions). Statutory income up to the threshold is taxed at 0%, statutory income above the threshold up to J$6,000,000 at 25%, and statutory income above J$6,000,000 at 30%. The J$6 million break is a level of statutory income, not an amount above the threshold.

| Item | Amount, 2026 | Conditions | Source |
|---|---|---|---|
| Tax year | Year of assessment 2026, 1 January to 31 December 2026 | Calendar year | TAJ, rates, threshold and exemptions 2013 to 2028: https://www.jamaicatax.gov.jm/documents/10194/15307403/INDIVIDUAL_INCOME_TAX_RATES_THRESHOLD_AND_EXEMPTIONS_2013-2028.pdf/c0987986-f35c-7106-85a4-d488a6f52627 |
| Rates of income tax | 25% and 30% | Same two rates for 2018 to 2028 | same |
| Income tax threshold, effective for the year | J$1,876,614 | Annual return computation, resident individuals only | same |
| Threshold, annual rate 1 January to 31 March 2026 | J$1,799,376 a year (J$149,948 a month) | PAYE pay periods in that quarter; TAJ's table prints 1,799,360 in its computation line, but the monthly figure and the quarter total (J$449,844) follow 1,799,376 | TAJ, payroll taxes and statutory contributions (April 2025 edition): https://www.jamaicatax.gov.jm/documents/10194/53547865/Payroll+Taxes+and+Statutory+Contributions+%28Employee+Employer%29.pdf/bef9095b-fb2d-db4a-5de4-b19405bd8631 |
| Threshold, annual rate from 1 April 2026 | J$1,902,360 a year (J$158,530 a month) | Pay periods 1 April to 31 December 2026; nine months give J$1,426,770 | same |
| Break between 25% and 30% | J$6M of statutory income a year (J$500,000 a month for PAYE) | Statutory income above J$6M is taxed at 30% | TAJ, rates, threshold and exemptions 2013 to 2028: https://www.jamaicatax.gov.jm/documents/10194/15307403/INDIVIDUAL_INCOME_TAX_RATES_THRESHOLD_AND_EXEMPTIONS_2013-2028.pdf/c0987986-f35c-7106-85a4-d488a6f52627 |
| Pension relief | J$250,040 | Pension income from an approved scheme or a statutory fund in Jamaica | same |
| Age relief | J$250,040 | Individual aged 65 or over | same |
| Total relief, pensioner aged 65 or over | J$2,376,694 | Threshold plus both reliefs (TAJ's self-employed guide prints a total with two digits swapped, an arithmetic slip; the rates table total is used here) | same |
| Non-resident individual | 25% from the first dollar, no threshold | No treaty, or a treaty giving Jamaica the taxing right without a rate | TAJ, non-residents and income tax: https://www.jamaicatax.gov.jm/documents/10194/20399532/1-Non-residents+and+Income+Tax+Final+Document.pdf/d8ccd3fa-4a99-e798-1a4b-841e952d82ba |
| Rent paid to a non-resident | 25% withheld by the payer | Payer issues a withholding certificate | same |
| NIS, self-employed | 6% | Earnings from self-employment up to the J$5,000,000 wage ceiling; age 18 to 65, or to 70 if still gainfully occupied | TAJ, income tax and statutory contributions for self-employed individuals (updated November 2026): https://www.jamaicatax.gov.jm/documents/10194/20399532/4-Income+Tax+and+Self+Employed+Individuals++%28+Updated+Nov.+2026+%29.pdf/c4f3878c-7a44-0a3b-d4a2-4a8cbef3f9ef |
| NIS wage ceiling | J$5,000,000 a year | From 2022 onwards | same |
| NHT, self-employed | 3% of statutory income | Age 18 to 65 | same |
| Education Tax, self-employed | 2.25% of statutory income | No age limit; no threshold | same |
| HEART, self-employed person who is an employer | Payable when the monthly wage bill exceeds J$14,444 | Not deducted from employees' pay | same |
| Prior-year loss, annual set-off cap | 50% of the year's income less exemptions and deductions other than the loss | Cap lifted if the business has run six years or less, or gross sales are under J$15,000,000; unused loss carries forward indefinitely | same |
| Annual return S04 and S04a | 15 March of the following year | S04a for the current year is filed with the S04 | same |
| Estimated tax instalments | 15 March, 15 June, 15 September, 15 December | Quarterly, on the S04a estimate | same |
| NIS, NHT, Education Tax for employees | 3% (to J$5,000,000), 2% of gross, 2.25% of statutory income | Employees; owned by `jm-payroll-social` | TAJ, payroll taxes and statutory contributions (April 2025 edition): https://www.jamaicatax.gov.jm/documents/10194/53547865/Payroll+Taxes+and+Statutory+Contributions+%28Employee+Employer%29.pdf/bef9095b-fb2d-db4a-5de4-b19405bd8631 |
| Withholding on specified services | 3% of the invoice value before GCT | Withheld by tax withholding agents on invoices of J$50,000 or more; the 3% is a credit on the supplier's return | TAJ, withholding tax on specified services brochure: https://www.jamaicatax.gov.jm/documents/10181/917523/wtss_brochure_sept2015+-.pdf/ddde1b72-c11c-4130-b273-fb4697c0da90 |

Threshold history kept for open earlier years: 2024 effective J$1,650,090; 2025 effective J$1,774,554 (J$1,700,088 a year to 31 March 2025, J$1,799,376 from 1 April 2025); 2027 effective J$1,978,212 (J$2,003,496 from 1 April 2027). Pension and age reliefs were J$207,530 each for 2024 and J$250,040 from 2025. Source: the TAJ rates PDF and the April 2025 payroll PDF above.

### Formula

```
statutory income (SI) = total income from all sources
                        - business expenses and capital allowances
                        - allowable deductions (NIS paid, approved superannuation or retirement scheme)
                        - exemptions (pension relief, age relief)
                        - prior-year loss (capped where the cap applies)
income tax = 25% x (min(SI, 6,000,000) - threshold, not below 0)
           + 30% x (SI - 6,000,000, not below 0)
Education Tax (self-employed) = 2.25% x SI
NHT (self-employed) = 3% x SI
```

A non-resident: income tax = 25% x Jamaica-source statutory income (no threshold), unless a treaty rate applies.

## The base

### What is income

Total income includes income from all sources, local or overseas, for a resident: sale of goods, fees and charges for services, rent, share of partnership profit, employment income and pension income. A partnership reports its profit and sharing on Form IT03; each partner reports their share on their own S04.

### Deductions and exemptions (TAJ self-employed guide)

- **Business expenses** incurred in earning the income are deductible, such as staff wages, rent for business premises and interest on business loans.
- **Personal or domestic expenses, depreciation and other accounting estimates are not deductible.** Capital allowances replace depreciation, at the rate the First Schedule to the Income Tax Act sets for the asset type, claimed on Income Tax Schedule 2 (capital allowances, as of YA 2025).
- **Allowable deductions** (Income Tax Act s. 13 as TAJ describes it) include contributions to an approved superannuation fund or approved retirement scheme, and NIS paid.
- **Exemptions** (Income Tax Act s. 12 as TAJ describes it): pension relief and age relief, at the amounts in the rates table.
- **NHT and Education Tax** are computed on statutory income; TAJ does not list either as a deduction from it. Treat them as not deductible from the income tax base.
- **Prior-year losses**: capped at 50% as in the rates table, with the six-year and J$15,000,000 exceptions. The threshold cannot create or enlarge a loss.

### Classification rules kept from the earlier version

- **Wholly and exclusively.** An expense is deductible only if incurred in producing the income. Mixed-use costs are apportioned on a reasonable, documented basis; the conservative default is 0% until the client supplies the business share.
- **Capital items** go through Schedule 2, never straight to the profit and loss account.
- **Not deductible:** entertainment and client meals, personal living costs, fines and penalties, income tax itself, drawings.
- **GCT collected** by a GCT-registered trader is not income; extract the net amount.
- **Grants**: a revenue grant is income; a capital grant is not. Ask the client.
- **Bad debts**: deduct only if the income was declared before, recovery steps were taken and the debt is irrecoverable; flag for review.
- **Approved superannuation**: deduct only if the scheme is approved; flag for review.
- **Foreign-currency receipts**: convert to J$ at the date of receipt (Bank of Jamaica rate).
- **Internal transfers** between the client's own accounts are excluded.

### Conservative defaults

| Ambiguity | Default |
|---|---|
| Unknown residency status | Stop; do not apply the threshold until residency is confirmed |
| Unknown pensioner or age status | Do not apply the reliefs |
| Unknown business-use share (vehicle, home office, phone) | 0% deduction |
| Unknown expense category | Not deductible |
| Unknown GCT registration status | Ask whether turnover approaches J$15,000,000 (see `jamaica-gct`) |
| Unknown business age or gross sales, prior loss claimed | Apply the 50% cap |

### Transaction patterns (bank statement pre-classifier)

Match case-insensitively on the counterparty or description; the most specific pattern wins; if none matches, use the rules above.

| Pattern | Treatment | Notes |
|---|---|---|
| Client name with TRANSFER, DEPOSIT, PAYMENT RECEIVED, WIRE | Business income | If GCT-registered, take the amount net of GCT |
| INVOICE, PROFESSIONAL FEES, CONSULTANCY, SERVICES | Business income | Check for 3% withholding certificates from withholding agents |
| STRIPE, PAYPAL, WISE PAYOUT | Business income, platform payout | Match to invoices; convert to J$ at the date received |
| UPWORK, FIVERR, TOPTAL, FREELANCER | Business income, net of commission | Gross up if the commission is charged separately |
| SALARY, WAGES, EMOLUMENTS, EMPLOYER name | Employment income | PAYE should have been deducted |
| RENT RECEIVED | Rental income | Part of total income |
| INTEREST, BANK INTEREST | Interest income | Check the withholding certificate; credit tax withheld |
| DIVIDEND | Dividend income | Rate to confirm, see Not yet confirmed |
| TAJ REFUND, TAX REFUND | Exclude | Not income |
| GRANT, MSME GRANT | Check nature | Revenue grant income; capital grant excluded |
| OFFICE RENT, LEASE (commercial address) | Deductible | Dedicated business premises |
| PROFESSIONAL INDEMNITY, ACCOUNTANT, LAWYER (business), STATIONERY, MARKETING, GOOGLE ADS, META ADS, TRAINING, PROFESSIONAL BODY, BANK CHARGE, STRIPE FEE, PAYPAL FEE, DOMAIN, HOSTING, AWS, POSTAGE, COURIER | Deductible | Business-related only |
| GOOGLE WORKSPACE, MICROSOFT 365, ADOBE, CANVA, FIGMA, NOTION, SLACK, ZOOM, ANTHROPIC, OPENAI, GITHUB, DROPBOX | Deductible subscription | A perpetual licence of significant cost is capital: Schedule 2 |
| JPS (electricity), NWC (water), FLOW, DIGICEL (telecoms) | Business share only | 100% if a dedicated office; default 0% if mixed |
| CARIBBEAN AIRLINES, JETBLUE, AMERICAN AIRLINES, HOTEL, AIRBNB, UBER, KNUTSFORD EXPRESS, TAXI | Deductible if wholly business travel | Keep the purpose |
| PETROL, FUEL, RUBIS, TOTAL, PARKING | Business share only | Mileage log needed |
| RESTAURANT, DINING, ENTERTAINMENT, CLIENT MEAL | Not deductible | |
| GROCERIES, SUPERMARKET, PERSONAL | Not deductible | |
| FINE, PENALTY, TRAFFIC TICKET | Not deductible | |
| TAJ PAYMENT, INCOME TAX PAYMENT | Not deductible | Credit only if it is an estimated tax payment |
| DRAWINGS, ATM (personal) | Not deductible | |
| LAPTOP, COMPUTER, PRINTER, FURNITURE, VEHICLE, AIR CONDITIONING, BUILDING | Capital item, Schedule 2 | Rates per the First Schedule; see Not yet confirmed |
| NIS CONTRIBUTION | Deduction in arriving at statutory income | Not a profit and loss expense |
| NHT, EDUCATION TAX (own) | Not deducted from statutory income | Employer's own contributions on staff are a business cost |
| HEART (employer) | Business cost | Employer only |
| S04A PAYMENT, ESTIMATED TAX | Credit against the year's tax | Not an expense |
| PAYE WITHHELD | Credit against the year's tax | |
| OWN TRANSFER, SAVINGS ACCOUNT | Exclude | |

Bank statement formats seen: NCB and Scotiabank Jamaica (PDF or CSV, DD/MM/YYYY, description holds the counterparty), JMMB Bank and Sagicor Bank (PDF, short descriptions), Wise, PayPal and Stripe (multi-currency CSV). Common terms: TRF (transfer), DD (direct debit), SO (standing order), EMOLUMENTS (employment pay), STATUTORY DEDUCTIONS (NIS, NHT, Education Tax), TRN (Taxpayer Registration Number).

### Working paper layout

```
JAMAICA INCOME TAX, S04 WORKING PAPER, YEAR OF ASSESSMENT 2026
A. Gross income: business, employment, rental, interest, dividends, other
B. Business expenses (wholly and exclusively), by category
C. Net business income (A business - B)
D. Capital allowances (Schedule 2)
E. Allowable deductions: NIS paid, approved superannuation or retirement scheme
F. Exemptions: pension relief J$250,040, age relief J$250,040, where they apply
G. Prior-year loss (50% cap unless an exception applies)
H. Statutory income = A total - B - D - E - F - G
I. Income tax: 25% x (min(H, 6,000,000) - 1,876,614) + 30% x (H - 6,000,000), none below 0
J. Education Tax 2.25% x H; NHT 3% x H; NIS 6% of self-employed earnings to J$5,000,000
K. Credits: PAYE, 3% specified-services withholding, other withholding certificates, S04a payments
L. Tax due or refund = I - K
Reviewer flags: residency, reliefs, contribution receipts, GCT status, mixed-use items,
entertainment excluded, capital items in Schedule 2, loss cap applied, estimates labelled.
```

## Deadlines and filing

| Step | What | When |
|---|---|---|
| 1 | TRN (Taxpayer Registration Number); a branch extension if GCT-registered or an employer | Before trading |
| 2 | Income tax registration is implicit: the first return, payment or assessment registers the person | n/a |
| 3 | Form S04 annual return for the year, with balance sheet, profit and loss account and the tax computation; schedules: 1 trading details, 2 capital allowances, 3 employee expenses, 4 certificates, 7 employment tax credit, 8 connected person transactions; S04 Schedule A (NHT) and B (NIS) | 15 March 2027 for YA 2026 |
| 4 | Form S04a, estimated income, taxes and contributions for the current year, filed with the S04 | 15 March |
| 5 | Quarterly estimated payments | 15 March, 15 June, 15 September, 15 December |
| 6 | Balance: actual tax above estimates is due when the S04 is filed; excess estimates may be refunded | With the S04 |

A combined self-computing S04/S04a/S03 form is available. Returns are filed online through the TAJ portal (e-Services account, applied for online or at a Revenue Service Centre). Payment: at tax offices (cash, debit card, credit card, manager's cheque) or online (Direct Funds Transfer with a DFTN, NCB Bill Pay, BNS Bill Pay, or card through the TAJ account).

## Penalties and interest

The late-filing penalty and interest rate for a late S04 were not confirmed on a TAJ page read for this version; see Not yet confirmed. Filing on time and paying late keeps any late-filing charge separate from interest. Extensions need written permission from the Commissioner General. For an employer's PAYE failures (50% a year increase, interest, S02 penalty) see `jm-payroll-social`.

## Cross-border points

- **Residents** are taxed on income from all sources, including overseas.
- **Non-residents** get no threshold and pay 25% on Jamaica-source income unless a treaty sets a rate. Where withholding applies, the payer withholds and remits; otherwise the non-resident or a local representative (agent, attorney, branch or manager) files a return.
- **Treaty rates** TAJ lists (dividends portfolio / substantial, interest, royalties, management fees): Canada 15 / 22.5, 15, 10, 12.5; Denmark 15 / 10, 12.5, 10, 10; Germany 15 / 10, 10 bank or 12.5 other, 10, s. 40; Israel 22.5 / 15, 15, 10, s. 40; Italy 10 / 5, 10, 10, s. 40; Norway 15 / 15, 12.5, 10, 10; Sweden 22.5 / 10, 12.5, 10, 10; United Kingdom 15 / 10, 12.5, 10, 12.5; United States 15 / 10, 12.5, 10, business profit; CARICOM 0 / 0, 15, 15, 15; Switzerland 15 / 10, 10, 10, 10; China 5, 7.5, 10; France 15 / 10, 10, 10, 10; Spain 10 / 5, 10, 10, 10; Mexico 10 / 5, 10, 10, 10; Japan 10 / 5, 10, 2 equipment or 10 other. Read each treaty before applying.
- **Refunds and exemptions** for non-residents: online application with TRN, proof of income and notarised proof of foreign residence; in person with Form 1N.
- **Jamaican nationals working for non-residents** (embassies, overseas employers) are self-employed for TAJ purposes and file S04.

## Two worked examples that recompute

### Example 1: Resident employee, salary J$3,600,000 for 2026, no pension

Annual view at the effective 2026 threshold (the employer applies the monthly amounts during the year; the annual return trues it up). NIS 3% of J$3,600,000 = J$108,000 (below the ceiling). Statutory income = J$3,492,000. Education Tax 2.25% of statutory income = J$78,570. NHT 2% of gross = J$72,000. Income tax = 25% of (J$3,492,000 - J$1,876,614) = J$403,846.50; no 30% slice.

```oa-check
name: JM 2026 employee, salary 3.6m, annual computation
inputs:
  gross: 3600000
  threshold: 1876614
steps:
  - nis: min(gross, 5000000) * 0.03
  - si: gross - nis
  - ed_tax: si * 0.0225
  - nht: gross * 0.02
  - income_tax: max(min(si, 6000000) - threshold, 0) * 0.25 + max(si - 6000000, 0) * 0.30
expected:
  nis: 108000
  si: 3492000
  ed_tax: 78570
  nht: 72000
  income_tax: 403846.50
```

### Example 2: Self-employed retailer with a J$8,000,000 prior-year loss, does the 50% cap apply?

Income less all exemptions and deductions except the loss is J$10,000,000 for 2026. Case A: in business more than six years with gross sales of J$30,000,000, so the cap applies: loss used J$5,000,000, statutory income J$5,000,000, income tax J$780,846.50, loss carried forward J$3,000,000. Case B: in business four years, so no cap: the full J$8,000,000 is used, statutory income J$2,000,000, income tax J$30,846.50. The age of the business and the J$15,000,000 sales test decide a difference of J$750,000.

```oa-check
name: JM 2026 self-employed prior-year loss cap, both ways
inputs:
  pre_loss: 10000000
  loss: 8000000
  threshold: 1876614
steps:
  - used_a: min(loss, pre_loss * 0.5)
  - si_a: pre_loss - used_a
  - tax_a: max(min(si_a, 6000000) - threshold, 0) * 0.25 + max(si_a - 6000000, 0) * 0.30
  - carried_a: loss - used_a
  - si_b: pre_loss - min(loss, pre_loss)
  - tax_b: max(min(si_b, 6000000) - threshold, 0) * 0.25 + max(si_b - 6000000, 0) * 0.30
  - difference: tax_a - tax_b
expected:
  used_a: 5000000
  si_a: 5000000
  tax_a: 780846.50
  carried_a: 3000000
  si_b: 2000000
  tax_b: 30846.50
  difference: 750000
```

Check against TAJ's own 2026 illustration (Example 5 in the self-employed guide): statutory income J$15,900,000 gives 25% x J$4,123,386 = J$1,030,846.50 plus 30% x J$9,900,000 = J$2,970,000, total J$4,000,846.50, the same formula.

### Test cases kept from the earlier version (corrected)

- Resident employee, salary J$1,200,000: income tax nil (below the threshold); NIS J$36,000; Education Tax still due, 2.25% of J$1,164,000 = J$26,190.
- Non-resident with Jamaica-source business income J$2,000,000 and no expenses: 25% x J$2,000,000 = J$500,000, no threshold.
- Self-employed, J$150,000 client entertainment claimed: remove it, not deductible.
- Laptop J$180,000 claimed as an expense: remove from the profit and loss account and claim capital allowances on Schedule 2 at the First Schedule rate.

## Ask the client first

1. Were you resident in Jamaica for 2026? (Decides the threshold and worldwide scope.)
2. Are you self-employed, employed, or both? Any partnership share, rent, interest, dividends or overseas income?
3. Are you 65 or over, and do you receive a pension from an approved scheme or statutory fund?
4. How long has the business operated, what were gross sales, and do you have prior-year losses?
5. What NIS, approved superannuation or retirement scheme contributions, S04a payments, PAYE and withholding certificates (including 3% specified-services certificates) do you have?
6. Is turnover at or above J$15,000,000, and are you GCT-registered? Do you use a home office, vehicle or phone partly for business, and what share? What capital assets did you buy? What is your TRN?

### Prohibitions

- Never apply the threshold to a non-resident.
- Never apply the J$6,000,000 break to income above the threshold; it is a level of statutory income.
- Never omit Education Tax because income is below the threshold.
- Never deduct NHT or Education Tax from statutory income.
- Never treat income tax, fines or entertainment as deductible.
- Never expense a capital item.
- Never present a computation as final; label it an estimate for review.
- Never treat GCT collected as income.
- Never skip the TRN check.

## Sources

| Source | URL | Read on |
|---|---|---|
| TAJ, individual income tax rates, threshold and exemptions 2013 to 2028 (last updated April 2025): read for the 25% and 30% rates, the effective thresholds 2024 to 2028, pension and age relief and the J$6M and J$500,000 monthly break | https://www.jamaicatax.gov.jm/documents/10194/15307403/INDIVIDUAL_INCOME_TAX_RATES_THRESHOLD_AND_EXEMPTIONS_2013-2028.pdf/c0987986-f35c-7106-85a4-d488a6f52627 | 2026-11-14 |
| TAJ, payroll taxes and statutory contributions, employee and employer (April 2025 edition): read for the threshold steps on 1 April 2024, 2025, 2026 and 2027, monthly amounts, and the employee NIS, NHT and Education Tax rates | https://www.jamaicatax.gov.jm/documents/10194/53547865/Payroll+Taxes+and+Statutory+Contributions+%28Employee+Employer%29.pdf/bef9095b-fb2d-db4a-5de4-b19405bd8631 | 2026-11-14 |
| TAJ, income tax and statutory contributions for self-employed individuals (updated November 2026): read in full for who is self-employed, S04 and S04a filing, deductions, the loss cap, self-employed NIS, NHT, Education Tax and HEART, payment dates and methods, and the worked examples | https://www.jamaicatax.gov.jm/documents/10194/20399532/4-Income+Tax+and+Self+Employed+Individuals++%28+Updated+Nov.+2026+%29.pdf/c4f3878c-7a44-0a3b-d4a2-4a8cbef3f9ef | 2026-11-14 |
| TAJ, non-residents and income tax: read in full for the 25% rate, no threshold, the treaty rate table, refunds, exemptions and rent withholding | https://www.jamaicatax.gov.jm/documents/10194/20399532/1-Non-residents+and+Income+Tax+Final+Document.pdf/d8ccd3fa-4a99-e798-1a4b-841e952d82ba | 2026-11-14 |
| TAJ, self-employed statutory forms page: read for the S04, S04a, combined form and the schedule list | https://www.jamaicatax.gov.jm/web/guest/self-employed-statutory | 2026-11-14 |
| TAJ, withholding tax on specified services brochure (September 2015): read for the 3% rate, the J$50,000 invoice threshold and remittance within 14 days | https://www.jamaicatax.gov.jm/documents/10181/917523/wtss_brochure_sept2015+-.pdf/ddde1b72-c11c-4130-b273-fb4697c0da90 | 2026-11-14 |
| TAJ, notes and instructions for returns IT01 to IT05 (revised November 2013): read for the IT01 structure and the rule that non-residents get no tax-free amount; its dividend rates table was read but not relied on for 2026 | https://www.jamaicatax.gov.jm/documents/10181/106853/notes_and_instructions.pdf/0e07453f-7925-4475-ab0e-c5457a8b3214 | 2026-11-14 |

Not yet confirmed: the late-filing penalty and the interest rate on late income tax for individuals in 2026 (the earlier version said J$5,000 a month and 33.33% a year; TAJ's employer guide of 2019 gives 16.62681% for PAYE only); the 2026 withholding rates on dividends (resident and non-resident, including the reported cut to 15% for non-residents from 1 April 2025) and on interest; the First Schedule capital allowance rates and the accelerated allowances reported for 2025 and 2026 spend; the private motor vehicle cost cap of US$35,000 for capital allowances; the 5% cap on charitable donations; the company car benefit scale (earlier version: J$30,000 to J$140,000); the NHT refund rule details (earlier version: after seven years); the minimum wage (earlier version: J$16,000 a week from 1 June 2025); the 21-day GCT registration timing; the six-year assessment and refund time limits; whether NIS is due on approved pension income. The Income Tax Act on laws.moj.gov.jm returned an error (503) and was not read.
