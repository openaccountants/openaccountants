---
name: fj-income-tax
description: >
  Use this Fiji income tax reference for self-employed individuals, sole
  traders and wage earners: resident and non-resident rates, chargeable income,
  allowable deductions, advance tax, provisional tax, FNPF contribution, PAYE
  and the PIT return. Match requests such as "how much tax do I pay in Fiji",
  "FRCS income tax return", "PIT return", "Personal Income Tax Return for
  Business Individual", "self-employed tax Fiji", "provisional tax", "SRT",
  "Social Responsibility Tax", "ECAL", "FNPF contribution", "chargeable
  income", "tax-free threshold", "allowable deductions" and "VAT registration
  Fiji". Bands rest on Legal Notice 55 of 2023. No 2026 Act was read, so the
  2026-27 Budget measures are shown as held. This Tier 2 draft supports source
  checking and reviewer questions; it does not authorise filing, payment or a
  tax position.
version: 0.2
jurisdiction: FJ
tax_year: 2026
tax_year_notes: "2026 tax year (calendar year, 1 January to 31 December 2026, for individuals). Bands: Legal Notice 55 of 2023 from 1 January 2024, which FRCS repeats for the 2024 tax year onwards. Legal Notice 36 of 2025 amends the same Regulations and was not read. The 2026-27 Budget bills are held: no 2026 Income Tax, Tax Administration or FNPF amending Act was read at 5 November 2026."
last_updated: 2026-11-05
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
domain: income-tax
---

# Fiji Income Tax v0.2

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Who this applies to

This reference covers Fiji Income Tax on individuals under the Income Tax Act 2015 (ITA) and the Tax Administration Act 2009 (TAA), in Fijian dollars (FJD, written $), for the **2026 tax year**: 1 January to 31 December 2026 for individuals. Section 36 ITA allows a substituted tax year for companies only.

It covers sole traders and other business individuals (PIT-B), wage earners who must file (PIT-S), people with both employment and business income, and non-resident individuals with Fiji-source income. The authority is the Fiji Revenue and Customs Service (FRCS). The portal is the Taxpayer Online Service (TPOS). No workflow base is loaded: this guide has no `depends_on`.

### What this file is

This is a Tier 2 draft. No named reviewer applies to this text and nothing in it has been approved by an accountant. It is a working paper only: every output is an estimate for a qualified reviewer, and no output is a final computation.

Each statement carries one of these meanings:

- **Enacted:** read in an Act or Legal Notice, or in FRCS's revised Act where the amending text was not separately read. The revised Acts were read to 1 August 2025. FRCS states that they are produced for its internal purpose only, and they are not complete: the regulations printed in the revised Income Tax Act stop before Legal Notices 54 and 55 of 2023, and section 14(1)(c) omits the e-money words of Act 9 of 2025. The amending text leads where it was read.
- **FRCS practice:** read on an FRCS page, notice or Standard Interpretation Guideline (SIG). Practice is not statute. The statute wins where they differ, and the difference is recorded.
- **Fund page:** read on the Fiji National Provident Fund's website. It is not statute: the FNPF Act was not read, so every Fund page figure is covered on the 'Not yet confirmed:' line.
- **Bill:** printed in a 2026 Bill. No Bill figure is applied here.
- **Held:** not proven. It appears on the 'Not yet confirmed:' line at the end of Sources.

### Stop rules

Stop and give the message below when a trigger applies. A stop produces no partial classification. R-FJ-3 alone is a reviewer flag: compute, then give the message.

| Code | Trigger | Message |
| --- | --- | --- |
| R-FJ-1 | Residency status unknown | 'Residency determines whether the tax-free threshold and progressive bands apply (resident) or 20% from the first dollar up to $270,000, then 33% to 39%, applies (non-resident). This skill cannot compute tax without confirming residency. Please confirm before proceeding.' |
| R-FJ-2 | Company or partnership | 'This skill covers individuals and sole traders only. Companies (25% CIT) and partnerships file separate returns. Escalate to a Fiji-licensed practitioner.' |
| R-FJ-3 | Chargeable income above $270,000 | 'Chargeable income above $270,000 falls in the 33% to 39% income tax bands (SRT is integrated into these bands from 2024 and is not charged on top). Flag for reviewer before finalising.' |
| R-FJ-4 | Capital gains or asset disposals | 'Capital Gains Tax (10%) computations require specialised analysis. Out of scope. Escalate to a Fiji-licensed practitioner.' |
| R-FJ-5 | Arrears or enforcement | 'Client has outstanding tax arrears or is subject to FRCS debt management action. Late payment carries a 25% penalty plus a further 5% of the unpaid tax for each month of default. Do not advise. Escalate to a Fiji-licensed practitioner immediately.' |
| R-FJ-6 | VAT return requested | 'This skill covers income tax (PIT) only. Fiji VAT (12.5% from 1 August 2025, threshold $100,000) is a separate workflow.' |

Do not:

- apply a rate table without confirming resident or non-resident status, or give a non-resident the $30,000 nil band;
- add SRT or ECAL on income to the 2024 bands;
- allow personal expenses, Income Tax or Capital Gains Tax, fines or penalties as deductions;
- include VAT collected in business income without settling the VAT basis below;
- use current year income for advance tax, unless a section 110 estimate applies;
- present a calculation as definitive: always label it estimated.

### Residence

Section 6(1) ITA makes an individual resident if the individual:

1. resides in Fiji;
2. is domiciled in Fiji, unless the individual has a permanent place of abode outside Fiji;
3. is present in Fiji for a period of, or periods amounting in aggregate to, 183 days in any 12-month period; or
4. is an employee of the Government posted abroad.

Each limb is enough. Under section 6(2) a person who becomes resident in the current tax year, and was not resident for the preceding year, is resident only from the day first present in Fiji. Under section 6(3) a person who is not resident for the following year is resident only to the last day present in Fiji. SIG 2018-32 is FRCS's practice on these tests. It treats a permanent place of abode as a question of fact. That guideline was read in part.

A temporary resident is an individual resident solely or mainly to work in Fiji under an employment contract of not more than 3 years, not a Fijian citizen or permanent resident (section 2). That person's foreign income, other than employment income, is exempt (Exempt Income Regulations 2016, Schedule Part 3, paragraph 13).

## Rates, bands and thresholds

Read each table for the period named. Amounts are FJD. Section 8(1) ITA imposes the tax at rates set by regulations. The operative text for both tables is regulation 3(a) of the Income Tax (Rates of Tax and Levies) (Amendment) Regulations 2023 (Legal Notice 55 of 2023), in force 1 January 2024. FRCS's Tax Rates page and SIG 2024-09 repeat the same figures for the 2024 tax year onwards. The FRCS page said this holds until amended by the Income Tax Regulations. The revised Income Tax Act to 1 August 2025 still prints the earlier table and omits Legal Notice 55, so do not use the table printed there. Legal Notice 36 of 2025 amends these same Regulations and was not read. SIG 2026-07 cites it only for the insurance rate change. FRCS's page does not show that change, so the page cannot prove the bands are unchanged for 2026.

### Resident individuals

| Chargeable income | Income tax | Tax at top of band | Source |
| --- | --- | --- | --- |
| 0 to 30,000 | Nil | 0 | LN 55 of 2023 reg 3(a) https://www.frcs.org.fj/wp-content/uploads/2023/08/LN-52-65-Customs-Budget-Amendment-Income-Tax-Regs-Water-Resources.pdf ; FRCS table https://frcs.org.fj/tax-rates-and-codes/ |
| 30,001 to 50,000 | 18% of excess over 30,000 | 3,600 | same |
| 50,001 to 270,000 | 3,600 + 20% of excess over 50,000 | 47,600 | same |
| 270,001 to 300,000 | 47,600 + 33% of excess over 270,000 | 57,500 | same |
| 300,001 to 350,000 | 57,500 + 34% of excess over 300,000 | 74,500 | same |
| 350,001 to 400,000 | 74,500 + 35% of excess over 350,000 | 92,000 | same |
| 400,001 to 450,000 | 92,000 + 36% of excess over 400,000 | 110,000 | same |
| 450,001 to 500,000 | 110,000 + 37% of excess over 450,000 | 128,500 | same |
| 500,001 to 1,000,000 | 128,500 + 38% of excess over 500,000 | 318,500 | same |
| 1,000,001 and above | 318,500 + 39% of excess over 1,000,000 | none | same |

Marginal rates are 18% from $30,001, 20% from $50,001 to $270,000, then 33% rising to 39% above $1,000,000.

### Non-resident individuals

There is no nil band. The Legal Notice prints 3 bands to $270,000, all at 20%; they are merged here. Above $270,000 the percentages match the resident table on a higher base.

| Chargeable income | Income tax | Tax at top of band | Source |
| --- | --- | --- | --- |
| 0 to 270,000 | 20% of excess over 0 | 54,000 | LN 55 of 2023 reg 3(a) https://www.frcs.org.fj/wp-content/uploads/2023/08/LN-52-65-Customs-Budget-Amendment-Income-Tax-Regs-Water-Resources.pdf ; FRCS table https://frcs.org.fj/tax-rates-and-codes/ |
| 270,001 to 300,000 | 54,000 + 33% of excess over 270,000 | 63,900 | same |
| 300,001 to 350,000 | 63,900 + 34% of excess over 300,000 | 80,900 | same |
| 350,001 to 400,000 | 80,900 + 35% of excess over 350,000 | 98,400 | same |
| 400,001 to 450,000 | 98,400 + 36% of excess over 400,000 | 116,400 | same |
| 450,001 to 500,000 | 116,400 + 37% of excess over 450,000 | 134,900 | same |
| 500,001 to 1,000,000 | 134,900 + 38% of excess over 500,000 | 324,900 | same |
| 1,000,001 and above | 324,900 + 39% of excess over 1,000,000 | none | same |

### SRT and ECAL on income

| Item | Position | Period | Source |
| --- | --- | --- | --- |
| Social Responsibility Tax (SRT) | Removed. Do not compute SRT on top of the bands. FRCS described the 2024 change as a '5% reduction' for brackets above $270,000. That is FRCS's wording on combined rates, and the figures to use are the bands above. | From 1 January 2024. Act 5 of 2023 ss 2 and 3 delete the charge, and s 1(2)(b) brings them into force on that date. Some revised Act notes say 1 August 2023; the Act's own commencement leads. | Act 5 of 2023 https://www.frcs.org.fj/wp-content/uploads/2023/07/Act-5-Income-Tax-Budget-Amendment.pdf ; SIG 2024-09 https://frcs.org.fj/files/2024/05/SIG-on-Change-in-Individual-Income-Tax-Rates.pdf |
| One-off payments | The SRT exemption for one-off payments no longer applies. A gain from the sale of an asset, redundancy payment, retiree allowance, gratuity allowance or exit inducement payment counts in chargeable income to determine the bracket, after any exemption. | From 1 January 2024 | SIG 2024-09 paras 5 and 11 https://frcs.org.fj/files/2024/05/SIG-on-Change-in-Individual-Income-Tax-Rates.pdf |
| ECAL on personal income | Not charged on the 2024 bands. FRCS's last individual table with an ECAL column is for 2020 and 2021, and its PAYE notice says the 2024 template excludes SRT and ECAL. | 2024 onwards | https://frcs.org.fj/public-notice/customer-service-new-pay-as-you-earn-paye-structure/ |
| ECAL on prescribed services | A separate levy, outside this guide. FRCS's rate row ends 'Till 31st July 2021'. Held. | Current status held | https://frcs.org.fj/tax-rates-and-codes/ |

### FNPF

| Party | Rate of total wages | Period | Status | Source |
| --- | --- | --- | --- | --- |
| Employee | 8% | Up to 31 July 2026, and unchanged from 1 August 2026 | Fund page; Fund Act not read | https://myfnpf.com.fj/employers/ |
| Employer | 10% | Up to 31 July 2026 | Fund page; Fund Act not read | same |
| Employer | 8% | 1 August 2026 to 31 July 2027, a temporary measure | Fund page says 16% total is current and gives the 8% split. Bill 22 of 2026 prints section 37(4A), total 16% for this period, with no split. No Act read. | https://myfnpf.com.fj/employers/ ; https://frcs.org.fj/files/2026/07/Bill-No.-22-Fiji-National-Provident-Fund-Budget-Amendment-Bill-2026.pdf |
| Employer additional, above the mandatory rate to 10% | The Budget Summary says a 150% tax deduction on the excess; the Fund page says a 150% tax rebate | From 1 August 2026 | Held: no enacting text read | https://frcs.org.fj/files/2026/06/Budget-Summary-of-Revenue-Policy-2026-2027-.pdf ; https://myfnpf.com.fj/employers/ |
| Voluntary and additional contributions | Limit of $250,000 a financial year for a member | From 1 February 2025, gazetted 31 January 2025 per the Fund; FNPF Act s 38(6) as cited there | Fund page; Gazette not read | https://myfnpf.com.fj/2025/02/19/fnpf-reverts-to-old-voluntary-and-additional-contribution-limit/ |
| Compulsory wage ceiling | unverified: no ceiling or absence of ceiling was read | Held | Held | No page read states this |

The Fund calculates contributions on total wages, inclusive of cents. Employee and employer contributions are not personal deductions: see 'FNPF and deductions' in The base.

### Other figures

| Item | Figure | Period and conditions | Status | Source |
| --- | --- | --- | --- | --- |
| Corporate income tax | 25% | FRCS row for tax year 2024 onwards. Context only | FRCS page | https://frcs.org.fj/tax-rates-and-codes/ |
| Capital Gains Tax | 10% | FRCS row for 2026. Context only: see R-FJ-4 | FRCS page | same |
| Fringe Benefits Tax | 20% | FRCS row for 2026. Context only | FRCS page | same |
| Resident Interest Withholding Tax | 10% | FRCS row for 2026. ITA s 112 requires withholding at the prescribed rate; Income Tax (Rates of Tax and Levies) Regulations 2016 Schedule para (5A) | FRCS page, revised Act | https://frcs.org.fj/tax-rates-and-codes/ ; https://frcs.org.fj/files/2026/06/INCOME-TAX-ACT-2015-Revised-to-1-August-2025.pdf |
| Provisional tax on contract payments | 5% | ITA s 114; Provisional Tax Regulations reg 3; FRCS row for 2026 | Enacted, revised Act | https://frcs.org.fj/files/2026/06/INCOME-TAX-ACT-2015-Revised-to-1-August-2025.pdf ; https://frcs.org.fj/tax-rates-and-codes/ |
| VAT standard rate | 12.5% | Supplies from 1 August 2025. 15% applied from 1 August 2023 (Act 6 of 2023 ss 1(2) and 3) to 31 July 2025. The revised Act's note to s 15(1) says 1 August 2024; the Act's own commencement leads, and FRCS's row says 2023. VAT Act s 15(1) as amended by Act 10 of 2025 s 5 | Enacted, Act 6 of 2023 and revised Act | https://frcs.org.fj/files/2026/06/VALUE-ADDED-TAX-ACT-1991-Revised-to-1-August-2025.pdf ; https://www.frcs.org.fj/wp-content/uploads/2023/07/Act-6-Value-Added-Tax-Budget-Amendment.pdf ; https://frcs.org.fj/tax-rates-and-codes/ |
| VAT registration threshold | Taxable supplies exceeding $100,000 in gross turnover | VAT Act s 22(1). Counts supplies, not being exempt supplies, made in Fiji. Looks back at the end of any month over that month and the 11 before; no liability arises if the CEO is satisfied that the next 12 months will not exceed the amount. Also looks ahead at the start of any month, over that month and the next 11, on reasonable grounds. Apply within 21 days (s 22(3)) | Enacted, revised Act | same |
| Asset write-off | Full cost in year acquired if cost is $10,000 or less | Depreciation Regulations reg 4, as amended by LN 63 of 2020. Conditions in The base | Enacted, revised Act | https://frcs.org.fj/files/2026/06/INCOME-TAX-ACT-2015-Revised-to-1-August-2025.pdf |
| Depreciation: motor vehicles, buses and minibuses under 30 passengers, goods vehicles under 7 tonnes, computers and data handling equipment, construction and earthmoving equipment | 40% diminishing value or 25% straight line | Depreciation Regulations Schedule 1, operative page checked visually | Enacted, revised Act | same |
| Depreciation: buses of 30 or more passengers, heavy goods vehicles, specialised trucks, tractors, trailers, trailer-mounted containers, manufacturing, mining or farming plant | 30% or 20% | same Schedule | Enacted, revised Act | same |
| Depreciation: vessels, aircraft, public utility plant, office furniture, fixtures and equipment, any other depreciable asset | 20% or 12.5% | same Schedule. SIG 2021-04 paras 10(d) and f label these columns the other way, and the Schedule leads | Enacted, revised Act | same |
| Depreciation: buildings, straight line only | Brick, stone or concrete 2.5%; timber 4%; steel or prefabricated steel 4%; steel on copra plantations 7%; bure 15%; other 2.5% | same Schedule | Enacted, revised Act | same |
| Advance tax single instalment limit | Total under $120 | Persons other than companies, tax year 2025 onwards. Act 5 of 2024 s 5 | Enacted | https://frcs.org.fj/files/2024/08/Act-5-Income-Tax-Budget-Amendment-Act-2024.pdf |
| Redundancy exemption | $15,000 | Exempt Income Regulations Schedule Part 3 para 2A | Enacted, revised Act | https://frcs.org.fj/files/2026/06/INCOME-TAX-ACT-2015-Revised-to-1-August-2025.pdf |
| Other employment lump sum exemption | Up to $5,000, as the CEO considers reasonable, reduced by earlier use | Same Schedule para 2. Excludes a redundancy payment, a fund refund, an amount due under the contract of employment and a payment for or in lieu of leave | Enacted, revised Act | same |
| Small and micro enterprise exemption | Prescribed small and micro enterprises in agriculture, fisheries or tourism, gross turnover not exceeding $500,000 | Same Schedule Part 9 para 4. What is prescribed sits in the Small and Micro Enterprises Incentives Regulations, not read | Enacted, revised Act | same |
| Presumptive Income Tax | Turnover under $100,000 | ITA s 9, which starts on a date the Minister appoints by Gazette notice (s 1(3)). No notice or rate was read. Do not apply it | Held | same |
| National minimum wage | unverified: FJD 5.00 an hour from 1 April 2025, carried from the earlier version | Payroll context only. Page not read | Held | Fiji Government media page not read |

### Budget measures held

The 2026-27 Budget Summary changes no individual rate band. Bills 14 to 26 of 2026 were gazetted on 26 June 2026 (Gazette Notice 704). FRCS's Budget page lists them as Bills. SIG 2026-09 cites Tourism Services Tax Act 2026 (Act 20 of 2026), which shows one Bill of the batch was enacted. It proves nothing about the others. On 5 November 2026 parliament.gov.fj returned a JavaScript challenge and laws.gov.fj gave no statute text, so the status of the other Bills could not be checked at either site.

| Measure | Text read | Status | Source |
| --- | --- | --- | --- |
| Stock write-off above $250,000 needs CEO approval, s 40(7A) | Bill 15 of 2026, to commence 1 August 2026; the Budget Summary's wording differs | Held | https://frcs.org.fj/files/2026/07/Bill-No.-15-Income-Tax-Budget-Amendment-No.2-Bill-2026.pdf |
| 15-year losses for aviation, s 30(3)(c) | same Bill | Held; not an individual measure on its face | same |
| Provisional tax summary to include certificate of exemption contractors, s 121(2) | same Bill | Held | same |
| 150% sports facility deduction, s 25(22) | same Bill | Held | same |
| Records must let the CEO readily ascertain tax liability, TAA s 34(1)(a); refund claim rules for diplomatic missions and international bodies, TAA s 33(6) deleted; search powers, TAA s 35(1A); sale of charged property, TAA s 28(7A); $1 a day for omitting a contractor from the provisional tax summary, TAA s 43B | Bill 14 of 2026, to commence 1 August 2026 | Held | https://frcs.org.fj/files/2026/07/Bill-No.-14-Tax-Administration-Budget-Amendment-Bill-2026.pdf |
| Peer-to-peer lending interest, employment taxation scheme, electronic fiscal device and donation measures | Budget Summary 2026-27 only | Held: announcement | https://frcs.org.fj/files/2026/06/Budget-Summary-of-Revenue-Policy-2026-2027-.pdf |

## The base

### Order of calculation

Work in this order, for the tax year, in FJD. Section numbers are ITA unless stated.

1. Confirm residence (section 6) and the income basis: all sources for a resident, Fiji sources only for a non-resident (section 14(3)).
2. Sort the employment income. If tax was withheld under section 111 and the person did **not** have 2 or more employments at the same time for all or part of the year, section 125 makes that tax final. The income stays out of gross income, no deduction or loss reduces it, and the tax is not reduced by credits. If the person had 2 or more employments at once, section 125 does not apply: include the employment income in gross income and claim the withheld tax as a credit (section 124).
3. Sort the interest the same way. Interest paid by a financial institution to a resident individual, with tax withheld under section 112, is final (section 125(1)(b)). Interest from another payer is final only if the individual's only other income is final-tax income or income taxed under section 9 (section 125(1)(c)).
4. Build gross income under section 14(1): (a) employment, business and property income; (b) other income according to ordinary concepts; (c) unexplained and unidentified deposits during the year in any bank account or e-money account if the deposit can be sourced to the person (Act 9 of 2025 s 3); (d) income another section includes; (e) forfeited deposits and instalments on capital assets. Leave out exempt income and income taxed under section 9, 10 or 11 (section 14(2)). Gross it up for tax withheld (section 124(1)).
5. Subtract allowable deductions (sections 21 to 29), depreciation (sections 31 to 34), then losses carried forward (section 30). Carried-forward losses reduce only gross income other than employment income (section 30(2) and (5)). The result is chargeable income. If current-year deductions exceed gross income other than employment income and employment income is in gross income, stop for a reviewer determination. Section 13 alone says gross income less deductions; section 30(1) makes the excess a net loss; and the deletion of section 125A points to leaving employment income whole and carrying the loss forward. That reading is an inference, held.
6. Compute tax on chargeable income from the resident or non-resident table. If final-tax employment income exists, use the section 8(6) formula: tax = A minus B, where A is tax on chargeable income plus that employment income, and B is tax on that employment income alone.
7. Subtract credits in section 8(4) order: first the foreign tax credit (section 60), then credits under sections 53(4), 110 and 124.

Do not report business profit as if it were the only income when final-tax employment income exists. Section 8(6) places the business income on top of the employment income.

### Income items

- **Business income** (section 17(1)) includes gross proceeds and gross fees, revenue from investing business capital, net gains from a venture or profit-making scheme or from a revenue-account disposal, other ordinary business income, and any commercial debt between associates that is forgiven.
- **Unexplained deposits:** this rule matters when working from a bank statement. FRCS may include a deposit the person cannot support (SIG 2026-07 paras 12 to 15). Explain every credit before leaving it out.
- **Rent** is property income (section 18), not business income, unless the facts make it business income. The PIT-B has a Rental Income/Loss schedule (line 37 on the 2022 form). Real estate agents file a Rental Annual Report under section 107 by the end of February, with a $1 a day penalty.
- **Interest** may be final tax: see step 3. Part 4 of the Exempt Income Schedule has further exemptions, and the former $1,000 exemption (para 10) was deleted from 1 January 2024 by LN 54 of 2023.
- **Dividends:** the revised Act prints 'Any dividend received is exempt income' (Exempt Income Schedule Part 5 para 1). FRCS's exemptions page is narrower: exempt if paid from retained earnings taxed at corporate level, and otherwise for the CEO to determine. The PIT-B has dividend lines. This conflict is unresolved, so make dividends Needs Input and refer them. From 1 August 2025 the definition of dividend no longer covers a gain on a reduction of shares, on redemption, cancellation, liquidation, dissolution or termination, or on reconstruction, reorganisation or amalgamation (Act 9 of 2025 s 2; SIG 2026-07 paras 7 and 8).
- **VAT:** the ITA read has no express rule on VAT in gross proceeds. VAT collected by a registered person is owed to FRCS, so show income net of VAT as a working treatment, and tick the matching box on the return: the PIT-B asks whether figures are VAT inclusive or VAT exclusive. On the same working basis, an unregistered person's receipts and expenses stay gross.

### Method of accounting

An employee accounts on a cash basis (section 37(1)). A person required to account for VAT on an invoice basis under section 36 of the VAT Act must use accrual for income tax (section 37(2)(c)). FRCS says the VAT payment basis needs the CEO's prior approval, for public or local authorities, non-profit organisations, or taxable supplies under $100,000 in 12 months; other registered businesses generally use the invoice basis. So most VAT-registered sole traders cannot be computed from bank receipts alone. Other individuals may use cash or accrual if the same basis applies to income and expenditure (section 37(3)), unless the CEO specifies a basis for their class (section 37(4)). A change of method needs the CEO's approval and adjustments so that nothing is omitted or counted twice (section 37(5), (6)).

### Deductions

Section 21(1)(a) allows expenditure and losses to the extent incurred in deriving income. Section 22(1) then denies, except as the Act provides:

| Limb | Denied |
| --- | --- |
| (a) | Expenditure or loss to the extent domestic or private |
| (b) | Expenditure or loss of an employee in deriving employment income |
| (c) | Amounts already in a net gain or net loss |
| (d) | Capital expenditure or loss, except as the Act provides |
| (e) | Dividends, distributions, capital withdrawn or sums employed as capital |
| (f) | Reserves, provisions and amounts capitalised |
| (g) | Amounts recoverable or recovered under insurance, guarantee, surety or indemnity |
| (h) | Income Tax or Capital Gains Tax, in Fiji or elsewhere, and any penalty, additional tax or interest on them or on fringe benefits tax |
| (i) | A fine or penalty for violating a law, rule or regulation |
| (j) | A contribution to a non-approved fund |
| (k) | Inducements to public officers |

'Wholly and exclusively' is FRCS page wording, not the test in section 21. Mixed use is an extent test: apportion (section 45 for classes of income; section 31(5) for depreciation). Section 106(3) lets the CEO disallow a claim if a receipt or other record cannot be produced without reasonable excuse. A deduction for a payment subject to withholding waits until the withheld tax is paid (section 22(2)). The PIT-B has lines for this (127, 129 and 139 on the 2022 form).

These 5 items need facts and reviewer judgement. Show no claim until the facts are in hand, and do not report that as the law.

- **Home office.** The Act read has no dedicated-room rule. Section 21 and section 22(1)(a) require an extent test. Use a documented basis such as rooms or floor area over rent, EFL electricity, WAF water and internet. Earlier versions of this guide said a dual-use room does not qualify and that is held. Flag room count, floor basis and exclusive use.
- **Motor vehicle.** Only the business share of fuel, insurance, maintenance and depreciation is deductible. A mileage log is the safe evidence, but no mileage log rule was read. The vehicle rate is in the table.
- **Phone and internet.** Business share only, on a reasonable estimate the client can support.
- **Entertainment.** No statutory bar was read. FRCS's employer page lists 'Entertainment expenses for business purposes' as allowable. Personal meals fail section 22(1)(a). Treat client meals as Needs Input with evidence of purpose, not as automatically denied.
- **Bad debts** (section 26). All 3 tests must be met: (a) the debt was previously included in gross income, or is money lent in the normal course of a money-lending business; (b) it is written off in the accounts for the year; (c) there are reasonable grounds for believing it is irrecoverable. The deduction cannot exceed the amount written off. FRCS's deductions page says 'after exhausting all recovery avenues', which is practice. Recoveries are dealt with by section 27.

### FNPF and deductions

- **Employee contribution:** no deduction was found. Section 23 gives the deduction to an employer, and excludes amounts deducted from wages. Section 22(1)(b) denies an employee's expenses. The PIT-B's only FNPF line read is 'Excess FNPF Employer Contribution Not Exceeding 10%' (line 114). An earlier version of this guide said employee contributions are deductible: that is withdrawn.
- **Sole trader as employer:** employer contributions for staff are deductible under section 23. Regulation 8 of the Other Incentives Regulations and SIG 2021-32 gave an extra deduction for additional contributions: its current level is held.
- **Employee side of employer contributions:** employer contributions up to the statutory minimum are exempt (Exempt Income Schedule Part 6 para 1), as are additional contributions up to 10% of the month's total salary or wages (para 1A). A pension or annuity, and a lump sum or refund of contributions, paid by the Fund are exempt (paras 3 and 4).
- **A self-employed person's own voluntary contribution:** no deduction was found, but no complete search was made. Hold it.

### Depreciation

- Choose one method for all assets: diminishing value or straight line (section 31(2)). Structural improvements use straight line (section 31(3)). A change needs the CEO's written approval (section 31(4)).
- Deduct the fair proportional part for mixed use (section 31(5)). If an asset is not used for the whole year, multiply by days used over days in the year (section 31(6)): SIG 2021-04 uses 184/365 from 1 July.
- No depreciation applies in the year of disposal (section 34(1)). Consideration above written down value, up to depreciation allowed, returns to gross income (section 34(1)(a)); a shortfall below written down value is deductible (section 34(1)(c)); consideration above cost on a capital asset goes to Capital Gains Tax (section 34(1)(b)): see R-FJ-4. For an asset used partly to derive income and partly for another use, only the proportional part counts (section 34(2), which names subsection (1)(a) and (b) although the deduction limb is now (c)).
- **Write-off:** a depreciable asset costing $10,000 or less may be deducted in full in the year acquired, if it is regarded as a whole, can be separately identified and has a separate function (Depreciation Rates Regulations reg 4; SIG 2021-04 paras 61 and 62). So 'never expense a capital item in full' is wrong. Do not split one asset to reach the limit. Under diminishing value, where the written down value has reached 5% or less of cost at the end of a tax year, the taxpayer must deduct that sum in that year (reg 4(3)).
- Asset class must be settled before a rate is used. A printer or scanner may be data handling equipment or office equipment: flag it. The Income Tax (Allowances) Regulations 2019 were not read.

### Losses

A net loss arises when deductions exceed gross income other than employment income (section 30(1)). It carries forward against gross income other than employment income for 8 tax years if incurred on or after 1 January 2019, or 4 if incurred on or before 31 December 2018 (section 30(2) and (3)). The earliest loss goes first (section 30(4)). Employment income cannot be reduced by a carried-forward loss (section 30(5)).

Section 125A once allowed up to $20,000 of a current-year business loss against employment income (SIG 2020-14). Act 5 of 2024 s 6 deleted section 125A from 1 August 2024. Do not apply it to 2025 or later. Its effect for the 2024 tax year is held because the Act has no transitional rule. Foreign losses are ring-fenced: see Cross-border points.

### Other points

- Jointly owned property: income, expenditure and losses follow each owner's interest, and equal interests are assumed if they cannot be ascertained (section 43). Each individual's chargeable income is computed separately (section 50). Spouses in business together are not treated as partners unless the CEO is satisfied that each makes a separate and distinct contribution of capital or personal skills (section 51(4)). Partnerships themselves stop at R-FJ-2.
- Donations and incentives are claimed on specific lines of the PIT-B and depend on approvals. Act 9 of 2025 added: section 24(12A), 100% for a business's cash donation to a health centre, nursing station, aged care facility, orphanage or drug rehabilitation centre from 1 August 2025; section 25(19), 150% for a cash donation to an accredited start-up support programme (the Act says 'a person'; SIG 2026-07 para 22 says 'business taxpayer'); section 25(20) and (21), 25% of any new capital expenditure exceeding $100,000 incurred by the business in a tax year for providing a tour activity in Fiji, being any approved non-accommodation activity provided by a registered business. SIG 2026-07 para 24 speaks of setting up a new non-accommodation tour activity; the Act does not say the activity must be new, so an existing operator is held. SIG 2026-07 paras 22 to 25 cover both. SIG 2026-07 says apprenticeship, placement, part-time and disability incentives were extended to 31 December 2026 by LN 37 of 2025, which was not read.
- A taxpayer carrying on a business that accepts or makes payment through a payment service must keep a separate payment instrument used only for business transactions, and retain the records for not less than 7 years after the end of the tax period (TAA s 34A, from 1 January 2026 under Act 8 of 2025 s 1(2)).

### Bank statement classification

Use this library as a first pass: match by case-insensitive substring on the counterparty or description, most specific pattern first. If nothing matches, use the rules above. A match does not override a fact in the file. These bank-statement patterns come from the earlier version of this guide and are working aids, not law.

| Credits | Line | Treatment |
| --- | --- | --- |
| Client name + TRANSFER, DEPOSIT, PAYMENT RECEIVED; FEES, PROFESSIONAL FEES, CONSULTANCY | Business income | Income. If VAT-registered, split VAT at the rate for the supply date |
| STRIPE PAYOUT, STRIPE TRANSFER, PAYPAL PAYOUT, PAYPAL TRANSFER, WISE PAYOUT, WISE TRANSFER | Business income | Match to invoices. Translate foreign amounts (section 139) |
| UPWORK, FIVERR, TOPTAL | Business income | Gross up: the commission is a separate expense |
| SALARY, WAGES, PAY, EMPLOYER [name] | Employment income | Apply steps 2 and 6 of the order of calculation |
| RENT RECEIVED, RENTAL | Property income | Not self-employment income |
| INTEREST, INTEREST RECEIVED | Interest | Check for final tax at step 3 |
| DIVIDEND, DIVIDENDS | Dividend | Needs Input: see Income items |
| FRCS REFUND, TAX REFUND | Exclude | Refund of tax, if evidenced |
| GOVERNMENT GRANT, GOVT ASSISTANCE | Check nature | Needs Input: nature of the grant. No provision on grants was read. Hold for the reviewer |
| Any other credit | Hold | Unexplained deposits can be gross income under section 14(1)(c) |

| Debits | Category | Treatment |
| --- | --- | --- |
| OFFICE RENT, RENT [commercial address] | Office rent | Deductible for dedicated business premises |
| PROFESSIONAL INDEMNITY, PI INSURANCE; ACCOUNTANT, AUDITOR, BOOKKEEP, CA FEES; LAWYER, LEGAL, SOLICITOR (business); STATIONERY, OFFICE SUPPLIES; MARKETING, GOOGLE ADS, META ADS, FACEBOOK ADS | Business costs | Deductible if business-related. Legal fees of a capital or private nature are not |
| TRAINING, CPD, COURSE, SEMINAR, CONFERENCE | Training | Deductible if it relates to the current business |
| BANK FEE, SERVICE FEE, MAINTENANCE FEE; STRIPE FEE, PAYPAL FEE, TRANSACTION FEE | Bank and payment fees | Deductible for the business account |
| DOMAIN, HOSTING, CLOUDFLARE, AWS, DIGITALOCEAN | IT infrastructure | Small recurring spend is expense; a large purchase may be capital |
| GOOGLE WORKSPACE, MICROSOFT 365, OFFICE 365; ADOBE, CANVA, FIGMA, NOTION, SLACK, ZOOM; ANTHROPIC, OPENAI, GITHUB, ATLASSIAN, DROPBOX | Software subscription | Operating expense. For a foreign supplier check non-resident withholding first: Cross-border points |
| Perpetual software licence (high value) | Capital item | Capitalise, unless the write-off applies |
| EFL, ENERGY FIJI, FIJI ELECTRICITY; WATER AUTHORITY, WAF; VODAFONE, DIGICEL, TELECOM FIJI, BROADBAND | Utilities and telecoms | Business share only, on the extent test in section 21. Full share only if the facts show no private use. Needs Input if the share is not supported |
| FIJI AIRWAYS, AIR FIJI, FLIGHT; HOTEL, BOOKING.COM, RESORT, AIRBNB; TAXI, BUS, FERRY | Travel | Deductible to the extent of business travel |
| FUEL, PETROL, DIESEL, TOTAL, MOBIL; PARKING | Vehicle | Business share only; parking fines are never deductible |
| RESTAURANT, DINNER, LUNCH, ENTERTAINMENT, CLIENT MEAL | Entertainment | Needs Input: see Deductions |
| GROCERIES, SUPERMARKET, MH, NEW WORLD, RB PATEL | Personal | Not deductible |
| FINE, PENALTY, INFRINGEMENT | Fines | Not deductible: section 22(1)(i) |
| FRCS PAYMENT, INCOME TAX, TAX PAYMENT | Tax | Not deductible: section 22(1)(h). Allocate to credit or liability |
| DRAWINGS, PERSONAL WITHDRAWAL, ATM (personal) | Drawings | Not an expense |
| LAPTOP, COMPUTER, MACBOOK, DESKTOP; PRINTER, SCANNER, COPIER; FURNITURE, DESK, CHAIR; VEHICLE, CAR (business) | Capital | Write-off test first, then the Schedule rate, business share only |
| INTERNAL TRANSFER, OWN ACCOUNT, BETWEEN ACCOUNTS; LOAN REPAYMENT, LOAN PRINCIPAL; VAT PAYMENT, FRCS VAT | Exclude | Not income or expense. Loan interest is a separate question |
| FNPF, PROVIDENT FUND CONTRIBUTION | Check whose | Employer share for staff: section 23. Employee share or own contribution: no deduction applied |
| PROVISIONAL TAX, PT INSTALMENT | Check which | Tax withheld by a payer or an advance instalment is a credit; never an expense |

Statement layouts seen in the earlier version, unverified and to be checked against the statement itself: ANZ Fiji (PDF, CSV; Date, Description, Debit, Credit, Balance; DD/MM/YYYY; TRANSFER, DD, EFTPOS, FEE), BSP (PDF, CSV; Date, Particulars, Withdrawal, Deposit, Balance; PAYMENT, TFR, DIRECT DEBIT, CHARGE), Westpac Fiji (PDF; Date, Description, Amount, Balance; TRANSFER, DEBIT, CARD, FEE), HFC Bank (PDF; Date, Particulars, Withdrawals, Deposits; TRANSFER, DEPOSIT, WITHDRAWAL), Bred Bank Fiji (PDF, CSV; Date, Description, Amount, Currency; PAYMENT, TRANSFER, FEE).

Common terms: EFTPOS is a card terminal payment, so check the merchant. DD is a recurring direct debit. TFR is a transfer, so check direction. EFL is Energy Fiji Limited and WAF is the Water Authority of Fiji.

## Deadlines and filing

| Obligation | Date | Basis |
| --- | --- | --- |
| Income Tax return, including a net loss | Within 3 months after the end of the tax year: 31 March 2027 for tax year 2026 | ITA s 104(1). FRCS confirmed 31 March 2026 for 2025 returns |
| Income Tax payment | Same date as the return, or another prescribed date | ITA s 108(1). FRCS's debt page speaks of 30 days after a notice of assessment: held for a self-assessment |
| Extension of time to file | Apply in writing before the due date. The taxpayer or, from 1 August 2025, the tax agent may apply. The CEO may grant it upon satisfaction that there is reasonable cause | TAA s 5(1), (2). The extension does not move payment (s 5(3)). Any general extension for a year must come from an FRCS notice for that year; none was read for 2025 or 2026 |
| Extension of time to pay | Apply in writing. The CEO may allow time or instalments; a missed instalment makes the balance payable at once | TAA s 25 |
| Advance tax | 30 April, 31 August and 30 November. If the year's total is under $120, one payment on 30 September | ITA s 110(1), (2), Act 5 of 2024 s 5, tax year 2025 onwards |
| Provisional tax | A resident person or Fiji permanent establishment paying under a contract for service, including progress payments, withholds 5% of the payment. Not required where the total to be paid to any one person in a year is less than $1,000 (reg 8). None on a holder of a certificate of exemption (reg 3A). Commissions are withheld as prescribed: FRCS's page says 5% | ITA s 114; Provisional Tax Regulations regs 3, 3A and 8. Payer remits by the end of the following calendar month under s 117(1); reg 5 says the fifteenth day of the next month. FRCS's monthly reminders match s 117(1), and the conflict is held |
| Records | Keep in Fiji in English for 7 years, unless section 34(2) applies; not less than 7 years after the end of the tax period for payment service records | TAA ss 34 and 34A. Section 34(2) lets a taxpayer dispense with records early in 2 cases: (a) a company in liquidation and finally dissolved, or a person other than a company that has ceased business, 3 months after the custodian tells the CEO by registered letter of the proposal, if the CEO issues no preservation directive; (b) any other case, on a written application before the 7 years end, if the CEO agrees by written notice. Section 34A prints no such exception |
| Amended assessment | Within 6 years of filing a self-assessment or service of notice; at any time for fraud, wilful neglect or serious omission | TAA s 11(2) |
| Objection | 60 consecutive days from service of an assessment, 30 for other decisions, in the approved form | TAA s 16(1) |

**Advance tax amount** (section 110(3)): each payment = 33⅓% × (A minus B), where A is the assessed Income Tax for the preceding year, including under self-assessment, after any foreign tax credit, and B is the part of A paid by withholding. Where the prior year is not assessed by the first due date, or income started during the year, each payment is one-third of the estimated Income Tax other than tax to be collected by withholding, and a statement is filed by the first due date (section 110(4), (5)). A person who reasonably believes the liability will be significantly lower than the previous year's may file an estimate before the end of the sixth month, and each payment is then one-third of that estimate, other than tax to be collected by withholding (section 110(6)). If a required statement is not filed, the CEO estimates (section 110(7)). A revised estimate applies to payments before and after it is filed (section 110(9)). The revised Act prints 'one-ninth' in section 110(4); Act 5 of 2024 s 5 reads one-third, and the Act leads. Each payment is a credit, and any excess is refundable (section 110(10)).

FRCS's Provisional Tax page and its Advance Tax page describe different things. Provisional tax is withholding on payments. Advance tax is the instalment. Earlier versions of this guide used 'provisional tax' for both.

**Who files.** An individual need not file if the only income is final-tax employment income or final-tax interest (section 105). FRCS says PAYE is a final tax and most employees do not file. FRCS lists 6 cases for a PIT-S: more than one employment during the year; employment for part of the year; employment by a foreign mission; employment overseas; migrating and not being employed in Fiji; a COVID 19 fund donation deduction for 2023 and prior years. FRCS's list is wider than sections 105 and 125, which turn on employments at the same time. Consecutive jobs or a part year may need a PIT-S on FRCS's list whilst the tax stays final: held. Use the PIT-B for a business individual, including with employment income.

**Filing in TPOS.** FRCS's steps for a PIT-S are: log on to TPOS, go to the 'Request' tile, select 'Income Tax', then 'Request to File Personal Income Tax Return'. The PIT-B follows FRCS's TPOS user guide, which was not opened. The form read is the tax year 2022 PIT-B, so check line numbers on the current form:

1. Enter employment, interest, dividend and foreign income, then business and rental figures (lines 22 to 38), and state whether figures are VAT inclusive or VAT exclusive.
2. Enter the non-allowable deductions, then the allowable deductions and concessions (to line 164).
3. Check the business summary (165 to 173), chargeable income subtotals (174), tax liability (175), credits for PAYE, provisional tax and interest withholding (176), foreign tax credit (177) and total liability (178).
4. Complete the declaration. A tax agent files through TPOS and gives a tax agent declaration. Then pay.

Pay with the Tax Identification Number as the narration, and give the payment type and period: FRCS says these are mandatory for bill pay, online EFT and direct deposits. FRCS's asset declaration framework for sole proprietors was deferred on its February 2026 notice until further notice. TAA s 3(3)(c) stays in the Act and SIG 2026-08 describes it, so check the current position before filing.

### Working paper

Working paper only. Mark every item not supported by documents as 'PENDING -- reviewer must confirm'.

```
FIJI INCOME TAX -- PIT WORKING PAPER
Tax year: 2026       Client: ________       Residency: Resident / Non-resident
Taxpayer type: Sole trader / Employment and business (PIT-B) / Wage earner (PIT-S)
Number of employments at the same time in the year: ____
A. BUSINESS INCOME: A1 client payments; A2 platform payouts; A3 other; A4 total
B. DEDUCTIONS: B1 office rent; B2 professional insurance; B3 accountancy and legal;
   B4 office supplies; B5 software; B6 marketing; B7 bank and payment fees;
   B8 training; B9 travel; B10 telecoms business share; B11 home office share;
   B12 vehicle business share; B13 depreciation or write-off; B14 other; B15 total
C. NET BUSINESS PROFIT OR LOSS: A4 minus B15
D. OTHER INCOME IN GROSS INCOME: D1 employment where section 125 does not apply;
   D2 rent net of rental expenses (section 21), a loss shown as negative;
   D3 interest not final; D4 other
E. LOSSES BROUGHT FORWARD, earliest first, not against employment income;
   any amount not used carries on (section 30(3))
F. CHARGEABLE INCOME: let N = C + D2 + D3 + D4.
   N nil or more: the greater of nil and (N minus E), plus D1.
   N below nil, D1 nil: F is nil; the shortfall is a net loss carried forward
   (section 30(1)).
   N below nil, D1 above nil: PENDING -- reviewer must confirm F and the loss
   carried forward. Held: section 13 alone gives D1 + N; section 30(1) with the
   deletion of section 125A points to D1, with the shortfall carried forward
G. FINAL-TAX EMPLOYMENT INCOME, outside gross income, for section 8(6)
H. TAX: H1 tax on F plus G; H2 tax on G; H3 tax on F = H1 minus H2
I. CREDITS: I1 foreign tax credit; I2 advance tax paid; I3 provisional tax
   withheld; I4 PAYE where section 125 does not apply; I5 interest withholding
   not final; I6 total
J. TAX DUE OR REFUND: H3 minus I6
```

Reviewer flags: residency confirmed; number of employments confirmed; VAT status and basis confirmed (turnover against $100,000); home office arrangement; vehicle share and evidence; phone and internet share; every credit explained; asset class and write-off test; employee FNPF not claimed; chargeable income above $270,000; advance tax and provisional tax split; entertainment and personal costs excluded.

## Penalties and interest

Penalties are computed separately for each section (TAA s 48(1)). Since 1 August 2025 the CEO may impose a penalty and prosecute for the same act or omission on all taxpayers regardless of turnover (Act 8 of 2025 s 9; SIG 2026-08 paras 28 to 30). A penalty paid is not refunded when the CEO also prosecutes under section 48(3A) (s 48(8); SIG 2026-08 para 31). A person is liable only once the CEO assesses the penalty and serves notice (s 48(4)). Penalties and interest on Income Tax are not deductible (ITA s 22(1)(h), (i)).

| Failure | Penalty | Basis and limits |
| --- | --- | --- |
| Return with tax payable not filed | 20% of the tax payable under the return | TAA s 43(1)(a) |
| Same, each month of default | 5% of the tax payable for each month | TAA s 43(1)(b), 'subject to paragraph (a)'. FRCS's penalties page reads (a) 'and' (b) together. Default ends when the CEO receives the document (s 43(2)) |
| Any other failure to file or lodge, including a return with no tax payable | $1 a day | TAA s 43(1)(c) |
| Tax not paid by the due date or extended date | 25% of the unpaid tax | TAA s 44(2). 'Tax' does not include penalty (s 44(1)) |
| Same, each month of default | 5% of the unpaid tax for each month | TAA s 44(3). FRCS's debt page calls this a 'further interest penalty', and the Act calls it a penalty. Refund to the extent the tax was not payable (s 44(4)) |
| Records not kept | 75% of tax payable for the period if knowing or reckless; 20% otherwise | TAA s 45. FRCS's page shows 25% for the second limb, and the Act leads |
| False or misleading statement causing a shortfall | Shortfall × 15% × number of years after the year of assessment for the return | TAA s 46(2)(a). None if the person did not know and could not reasonably be expected to know, or the shortfall came from a reasonably arguable position in a self-assessment (s 46(5)). A position contrary to a ruling in force is not reasonably arguable unless the ruling is held to be incorrect (s 46(5A)). FRCS's page shows 75% and 25%; Act 13 of 2020 replaced the section's 75% and 20% |
| False or misleading statement with no shortfall but a tax benefit from overstatement | Benefit × 15% × the same number of years | TAA s 46A, with the same defences |
| Advance tax estimate under 100% of actual liability | 40% of the shortfall | ITA s 110(11). None if beyond the person's control and all reasonable care was taken (s 110(12)). The 3-year pause under s 110(13) began on 1 August 2020 |
| Business payment instrument rules | Offence: fine up to $25,000, imprisonment up to 10 years, or both | TAA s 34A(2), Act 8 of 2025 s 6 |
| Employer FNPF contributions unpaid | 10% of the outstanding balance for each month | FNPF Act s 40(1) as replaced by Act 11 of 2024 s 5, from 1 January 2025 |

**Interest.** No general interest charge on Income Tax arrears was found in the sections read, and no complete search was made. The earlier statement '5% per month interest' describes the section 44(3) penalty.

**Relief.** A person may apply in writing with reasons, and the CEO may remit a penalty in whole or in part on application or on the CEO's own motion (TAA s 48(6), (7)). FRCS's debt page says early engagement may qualify a person for remission 'to a maximum of 100%', given tax history, cooperation and commitment. That is FRCS practice. The amnesties in TAA ss 48A to 48E covered past periods.

## Cross-border points

- **Non-resident.** Only Fiji-source income is in gross income (section 14(3)(b)). Sources are in section 7. Use the non-resident table: there is no nil band.
- **Moving in or out.** Apply section 6(2) and (3), then split the year. FRCS requires a PIT-S where someone is migrating and will not be employed in Fiji.
- **Foreign income of a resident.** The credit is the lesser of foreign Income Tax paid and the person's average Fiji rate times net foreign-source income (section 60(1), (2), (8)). Compute it separately for business and other foreign income (section 60(3)). The foreign tax must be paid within 2 years after the end of the tax year, or longer if the CEO allows (section 60(5)). An unused credit is not refunded, carried back or carried forward (section 60(7)). SIG 2019-12 is FRCS's guide, not read here.
- **Foreign losses.** Foreign deductions offset only taxable foreign-source income. A foreign loss carries forward against that income for 4 years (section 61).
- **Currency.** Express all amounts in Fiji dollars. Translate at the exchange rate on the date the amount is taken into account, which means the telegraphic transfer rate issued by a financial institution relevant to the transaction (section 139(1), (2), (4)). An average rate for the year, for business income and related deductions, needs the CEO's prior written permission (section 139(3)).
- **Paying a non-resident.** FRCS lists non-resident withholding at 15% on royalties, management fees, natural resource amounts and professional or other independent services, and 10% on interest, for 2026. Whether a subscription to a foreign software supplier falls in those classes is held. The deduction waits for withheld tax to be paid (section 22(2)). The insurance premium rate differs: SIG 2026-07 gives 3.75% from 1 August 2025 under LN 36 of 2025, whilst FRCS's page shows 3% for 2026.
- **Treaties.** Fiji's agreements were not read. Do not apply a treaty rate from this guide.

## Two worked examples that recompute

Each case recomputes. Amounts are FJD and estimates. All bands are from the tables above.

### Example 1: one PAYE job and a side business

A resident has one employer all year, $60,000 of employment income with PAYE withheld as final tax, and $40,000 of chargeable business income. The business income sits on top under section 8(6). Taxing $40,000 alone would give $1,800, which is wrong.

```oa-check
name: FJ section 8(6) with one employment
inputs:
  business_chargeable: 40000
  final_tax_employment: 60000
steps:
  - aggregate: business_chargeable + final_tax_employment
  - a_tax: pct(max(min(aggregate, 50000) - 30000, 0), 18) + pct(max(min(aggregate, 270000) - 50000, 0), 20)
  - b_tax: pct(max(min(final_tax_employment, 50000) - 30000, 0), 18) + pct(max(min(final_tax_employment, 270000) - 50000, 0), 20)
  - tax_on_business: a_tax - b_tax
  - wrong_standalone: pct(max(min(business_chargeable, 50000) - 30000, 0), 18)
expected:
  aggregate: 100000
  a_tax: 13600
  b_tax: 5600
  tax_on_business: 8000
  wrong_standalone: 1800
```

Result: Income Tax of $8,000 on the business income, before credits. If this person had a second job at the same time for any part of the year, this example would not apply and Example 2 would.

### Example 2: 2 jobs at the same time

A resident has 2 employments at once, $20,000 from each. The second employer withheld at the S code tax rate of 20%, with no Special Tax Rate Certificate (Income Tax (Withholding Tax) Regulations 2013 regs 2, 7(2) and 8), and the first withheld nil. Section 125 does not apply, so a PIT-S is required and both amounts are chargeable. Withheld tax is a credit, and the excess is a refund.

```oa-check
name: FJ two employments with credit for PAYE
inputs:
  primary_employment: 20000
  secondary_employment: 20000
  primary_paye: 0
  secondary_s_code_percent: 20
steps:
  - chargeable: primary_employment + secondary_employment
  - tax: pct(max(min(chargeable, 50000) - 30000, 0), 18)
  - credits: primary_paye + pct(secondary_employment, secondary_s_code_percent)
  - balance: tax - credits
expected:
  chargeable: 40000
  tax: 1800
  credits: 4000
  balance: -2200
```

Result: tax of $1,800 and a refund position of $2,200.

### Example 3: residence decides the table

The same chargeable income gives different tax. At $40,000 the resident pays $1,800 and the non-resident $8,000. At $400,000 they pay $92,000 and $98,400.

```oa-check
name: FJ resident and non-resident at 40000 and 400000
inputs:
  low: 40000
  high_excess_over_350000: 50000
steps:
  - resident_low: pct(low - 30000, 18)
  - non_resident_low: 6000 + pct(low - 30000, 20)
  - resident_high: 74500 + pct(high_excess_over_350000, 35)
  - non_resident_high: 80900 + pct(high_excess_over_350000, 35)
  - gap_low: non_resident_low - resident_low
expected:
  resident_low: 1800
  non_resident_low: 8000
  resident_high: 92000
  non_resident_high: 98400
  gap_low: 6200
```

### Example 4: write-off limit

A sole trader, 100% business use, buys equipment on 1 July 2026. A $9,000 computer meets all 3 tests and is written off. The limit is a gate, not a cap: a $12,000 computer gets no write-off of any part, so the 25% straight-line or 40% diminishing value rate applies for 184 of 365 days, on the method chosen for all assets.

```oa-check
name: FJ write-off against depreciation
inputs:
  eligible_cost: 9000
  cost_over: 12000
  days: 184
steps:
  - write_off: eligible_cost
  - straight_line: round(pct(cost_over, 25) * days / 365, 2)
  - diminishing_value: round(pct(cost_over, 40) * days / 365, 2)
expected:
  write_off: 9000
  straight_line: 1512.33
  diminishing_value: 2419.73
```

### Example 5: advance tax

For 2026, a sole trader's 2025 assessed tax was $13,600, and $5,600 of it was paid by withholding. Each of the 3 payments is one-third of the difference. A second person's total comes to $90, under $120, so it falls due as one payment on 30 September.

```oa-check
name: FJ advance tax instalments
inputs:
  assessed_prior_year: 13600
  withheld_prior_year: 5600
  small_case_total: 90
steps:
  - base: max(assessed_prior_year - withheld_prior_year, 0)
  - each_instalment: round(base / 3, 2)
  - small_case_single_payment: small_case_total
expected:
  base: 8000
  each_instalment: 2666.67
  small_case_single_payment: 90
```

### Example 6: VAT split by supply date

A VAT-registered sole trader on the working net treatment receives $1,150 for a supply at 15% in March 2025, and $1,125 for a supply at 12.5% in 2026. Each gives $1,000 of income. The rate depends on the time of supply.

```oa-check
name: FJ VAT split at 15 and 12.5 percent
inputs:
  receipt_before_august_2025: 1150
  receipt_2026: 1125
steps:
  - income_before: receipt_before_august_2025 / 1.15
  - vat_before: receipt_before_august_2025 - income_before
  - income_2026: receipt_2026 / 1.125
  - vat_2026: receipt_2026 - income_2026
expected:
  income_before: 1000
  vat_before: 150
  income_2026: 1000
  vat_2026: 125
```

### Example 7: late return and late payment

Tax payable is $10,000, and the return and payment are 3 months of default late. Section 43 and section 44 count separately. The total treats section 43(1)(a) and (b) as cumulative, as FRCS's penalties page does. Whether paragraphs (a) and (b) add together is held, because (b) is 'subject to paragraph (a)'. How FRCS counts the months is also held: its VAT notice says 'each subsequent month'.

```oa-check
name: FJ late filing and late payment penalties
inputs:
  tax: 10000
  months: 3
steps:
  - filing_initial: pct(tax, 20)
  - filing_monthly: pct(tax, 5) * months
  - payment_initial: pct(tax, 25)
  - payment_monthly: pct(tax, 5) * months
  - total: filing_initial + filing_monthly + payment_initial + payment_monthly
expected:
  filing_initial: 2000
  filing_monthly: 1500
  payment_initial: 2500
  payment_monthly: 1500
  total: 7500
```

### Earlier cases rechecked

| Case | Input | Result |
| --- | --- | --- |
| Client payment, 15 March 2025, VAT-registered | $1,150 at 15% | Income $1,000; VAT $150 excluded, on the working net treatment. This is before 1 August 2025; see Example 6 for 2026 |
| Adobe subscription, 1 April 2025 | $69 | Deductible; net of recoverable input VAT if registered, on the working net treatment. Check non-resident withholding |
| Client dinner, 22 April 2025 | $180 | Needs Input, no longer an automatic denial |
| FNPF on $3,000 monthly wage | 8% | Employee $240, not a deduction. Employer $300 (total $540) to 31 July 2026; $240 (total $480) from 1 August 2026. Held: Fund page only, no Act read |
| Resident | $25,000 | Nil |
| Resident | $45,000 | 18% × 15,000 = $2,700 |
| Resident | $80,000 | 3,600 + 20% × 30,000 = $9,600 |
| Resident | $270,000 | 3,600 + 20% × 220,000 = $47,600. The 33% band starts above $270,000 |
| Resident | $400,000 | 74,500 + 35% × 50,000 = $92,000. No SRT or ECAL. Flag under R-FJ-3 |
| Non-resident | $40,000 | $8,000 |

## Ask the client first

1. **Status and years:** resident or non-resident, dates in and out of Fiji, and which tax year.
2. **Work:** sole trader, employment plus business, or wage earner; how many employments at the same time; PAYE and final-tax interest; rent, dividends and other income.
3. **Records:** a full-year bank and e-money statement, sales and purchase invoices and receipts, FNPF records, prior return or assessment, income and expenditure account, asset register and Tax Identification Number. Explain every deposit.
4. **VAT:** registered or not, turnover against $100,000, and invoice or payment basis.
5. **Mixed use and assets:** home office basis, vehicle share and log, phone and internet share, assets bought with cost and date, and depreciation method used in earlier years.
6. **Payments:** advance tax paid with confirmations, provisional tax withheld with certificates, FNPF paid for staff and for the client, foreign tax paid, and any chargeable income above $270,000.

**Minimum to start:** a full-year bank statement in CSV, PDF or pasted text, and answers to questions 1 and 2. No bank statement is a hard stop. A bank statement without invoices may proceed with this warning: 'This Fiji PIT computation was produced from bank statement alone. The reviewer must verify that all deductions claimed are supported by valid documentation and meet the extent test in section 21 of the Income Tax Act 2015.'

**Missing facts.** A default below only keeps the working paper moving. Each must be shown as an open item, and it is never a finding of law.

| Missing fact | Working default |
| --- | --- |
| Residency | Stop: R-FJ-1 |
| Whether income exceeds $270,000 | Compute from the figures; flag if above |
| Business use of vehicle, phone or home | No claim, shown as Needs Input |
| Expense category | No claim, shown as Needs Input |
| VAT registration | Needs Input. Test receipts against $100,000 before treating as unregistered |
| Asset class | Needs Input. Do not guess a rate |
| Entertainment or personal | Needs Input |

If the client cannot answer at once: classify with the library, mark Tier 2 items 'PENDING -- reviewer must confirm', apply the defaults, prepare the working paper with flags, then send the 6 questions above.

## Sources

Rates were read in the Legal Notice and FRCS's own page. FRCS's revised Acts were read for section numbers and text, with the limit in 'What this file is'.

| Source | URL | Read on |
| --- | --- | --- |
| LN 54 and 55 of 2023 (Exempt Income and Rates of Tax and Levies amendments), read in full; other notices in the bundle not relied on | https://www.frcs.org.fj/wp-content/uploads/2023/08/LN-52-65-Customs-Budget-Amendment-Income-Tax-Regs-Water-Resources.pdf | 2026-11-05 |
| FRCS Tax Rates page, all tables read; relative stamp 'Last Updated - 3 days ago' | https://frcs.org.fj/tax-rates-and-codes/ | 2026-11-05 |
| Income Tax Act 2015, revised to 1 August 2025: ss 1, 2 (part), 6 to 9, 13, 14, 15, 17, 18, 21 to 23, 26, 27, 30, 31, 34, 36, 37, 43, 45, 50, 51, 60, 61, 104 to 108, 110 to 112, 114, 117, 124, 125, 139 and the Exempt Income, Depreciation Rates, Provisional Tax and Withholding Tax Regulations (regs 2, 7 and 8 for the S code) and Rates of Tax and Levies Regulations (Schedule para (5A)), each in part | https://frcs.org.fj/files/2026/06/INCOME-TAX-ACT-2015-Revised-to-1-August-2025.pdf | 2026-11-05 |
| Tax Administration Act 2009, revised to 1 August 2025: ss 3, 5, 11, 16, 25, 34, 34A, 43 to 46C, 48 to 48E, in part | https://frcs.org.fj/files/2026/06/TAX-ADMINISTRATION-ACT-2009-Revised-1-August-2025.pdf | 2026-11-05 |
| Value Added Tax Act 1991, revised to 1 August 2025: ss 15 and 22, in part | https://frcs.org.fj/files/2026/06/VALUE-ADDED-TAX-ACT-1991-Revised-to-1-August-2025.pdf | 2026-11-05 |
| Income Tax (Budget Amendment) Act 2023, Act 5 of 2023, read in full | https://www.frcs.org.fj/wp-content/uploads/2023/07/Act-5-Income-Tax-Budget-Amendment.pdf | 2026-11-05 |
| Value Added Tax (Budget Amendment) Act 2023, Act 6 of 2023, read in full | https://www.frcs.org.fj/wp-content/uploads/2023/07/Act-6-Value-Added-Tax-Budget-Amendment.pdf | 2026-11-05 |
| Income Tax (Budget Amendment) Act 2024, Act 5 of 2024, read in full | https://frcs.org.fj/files/2024/08/Act-5-Income-Tax-Budget-Amendment-Act-2024.pdf | 2026-11-05 |
| FNPF (Budget Amendment) Act 2024, Act 11 of 2024, read in full | https://frcs.org.fj/files/2024/08/Act-11-Fiji-National-Provident-Fund-Budget-Amendment-Act-2024.pdf | 2026-11-05 |
| SIG 2026-07, Income Tax Act national budget amendments 2025-26, with Act 9 of 2025 in its appendix, read in full | https://frcs.org.fj/files/2026/06/SIG-on-Income-Tax-Act-2015-National-Budget-Amendments-2025-2026.pdf | 2026-11-05 |
| SIG 2026-08, Tax Administration Act national budget amendments 2025-26, paras 1 to 44 read, with Act 8 of 2025 read in full from page images of its appendix; appendix page on the National Payment System Act not read | https://frcs.org.fj/files/2026/06/SIG-2026-08-Tax-Administration-Act-2009-National-Budget-Amendement-2025-2026.pdf | 2026-11-05 |
| SIG 2024-09, change in individual income tax rates, read in part: paras 1 to 18 | https://frcs.org.fj/files/2024/05/SIG-on-Change-in-Individual-Income-Tax-Rates.pdf | 2026-11-05 |
| SIG 2026-09, Tourism Services Tax, read in part for the Act citation | https://frcs.org.fj/files/2026/08/SIG-on-Tourism-ServiceS-Tax-version-2-final-27Aug2026.pdf | 2026-11-05 |
| SIG 2018-32, residency for individuals, read in part | https://www.frcs.org.fj/wp-content/uploads/2018/09/SIG-2018-32-Residency-for-Individuals.pdf | 2026-11-05 |
| SIG 2020-14, business losses against employment income, read in part; overtaken by Act 5 of 2024 s 6 | https://www.frcs.org.fj/wp-content/uploads/2021/08/SIG-2020-14-Offsetting-of-Business-Loss-Against-Employment-Income.pdf | 2026-11-05 |
| SIG 2021-04, depreciation, read in part: paras 9 to 11, 41 to 43, 60 to 62 | https://www.frcs.org.fj/wp-content/uploads/2021/08/SIG-2021-04-Depreciation.pdf | 2026-11-05 |
| SIG 2021-32, employer FNPF contribution, read in part | https://www.frcs.org.fj/wp-content/uploads/2021/09/SIG-2021-32-Tax-Treatment-on-Employer-FNPF-Contribution.pdf | 2026-11-05 |
| SIG 2020-29, advance payment of tax, read in part; earlier 9-instalment regime | https://www.frcs.org.fj/wp-content/uploads/2020/08/SIG-2020-29-Advance-Payment-of-Tax-Section-110-of-ITA-2015.pdf | 2026-11-05 |
| 2026-27 Budget Summary of Revenue Policy, income tax parts read; announcement only | https://frcs.org.fj/files/2026/06/Budget-Summary-of-Revenue-Policy-2026-2027-.pdf | 2026-11-05 |
| Bill 14 of 2026, Tax Administration, read in part: clauses 1 to 5 and 8 to 11, and the clause list of the explanatory note; Divisions 5A and 5B not read in detail; Bill only | https://frcs.org.fj/files/2026/07/Bill-No.-14-Tax-Administration-Budget-Amendment-Bill-2026.pdf | 2026-11-05 |
| Bill 15 of 2026, Income Tax, clauses read in full, explanatory note read in part; Bill only | https://frcs.org.fj/files/2026/07/Bill-No.-15-Income-Tax-Budget-Amendment-No.2-Bill-2026.pdf | 2026-11-05 |
| Bill 22 of 2026, FNPF, read in full; Bill only | https://frcs.org.fj/files/2026/07/Bill-No.-22-Fiji-National-Provident-Fund-Budget-Amendment-Bill-2026.pdf | 2026-11-05 |
| Gazette Notice 704 of 2026, Bills 14 to 26, read in full | https://frcs.org.fj/files/2026/07/GN-57-Bills-to-be-presented-in-Parliament-Nos.14-26-1.pdf | 2026-11-05 |
| PIT-B return, tax year 2022 form, read in full; older than the year covered | https://www.frcs.org.fj/wp-content/uploads/2023/03/PERSONAL-INCOME-TAX-RETURN-FOR-BUSINESS-INDIVIDUAL.pdf | 2026-11-05 |
| Talk Tax Sole-traders leaflet, read in full; old thresholds, records point only | https://www.frcs.org.fj/wp-content/uploads/2018/02/99.Talk-Tax-Soletraders-v2.pdf | 2026-11-05 |
| FRCS Personal Income Tax page, PIT-S list and TPOS steps read | https://frcs.org.fj/our-services/taxation-section/individuals/lodging-your-tax-return/personal-income-tax/ | 2026-11-05 |
| FRCS Provisional Tax page, read in full | https://frcs.org.fj/our-services/taxation-section/non-individuals/reporting-and-paying-taxes/provisional-tax/ | 2026-11-05 |
| FRCS Advance Tax page, read in full | https://frcs.org.fj/our-services/taxation-section/non-individuals/reporting-and-paying-taxes/advance-tax/ | 2026-11-05 |
| FRCS Penalties and Offences page, percentages read | https://frcs.org.fj/our-services/taxation-section/non-individuals/debt-management-services/penalties-and-offences/ | 2026-11-05 |
| FRCS Debt Management page, penalty and remission text read | https://frcs.org.fj/our-services/taxation-section/non-individuals/debt-management-services/ | 2026-11-05 |
| FRCS Deductions and Allowances page for employers, read in full | https://frcs.org.fj/our-services/taxation-section/non-individuals/employers/deductions-and-allowances/ | 2026-11-05 |
| FRCS Deductions page for individuals, read in full | https://frcs.org.fj/our-services/taxation-section/individuals/deductions-and-offsets/deductions/ | 2026-11-05 |
| FRCS Exemptions page, dividend and interest parts read | https://frcs.org.fj/our-services/taxation-section/individuals/deductions-and-offsets/exemptions/ | 2026-11-05 |
| FRCS Rental Annual Report page, read in full | https://frcs.org.fj/our-services/taxation-section/non-individuals/reporting-and-paying-taxes/rental-annual-report/ | 2026-11-05 |
| FRCS notice, new PAYE structure, read in part: bands and SRT lines | https://frcs.org.fj/public-notice/customer-service-new-pay-as-you-earn-paye-structure/ | 2026-11-05 |
| FRCS notice, deferral of asset declaration framework, read in full | https://frcs.org.fj/public-notice/deferral-of-asset-declaration-framework/ | 2026-11-05 |
| FRCS notice, unidentified deposits (payment narration), read in full | https://frcs.org.fj/public-notice/unidentified-deposits/ | 2026-11-05 |
| FRCS notice, cash and accrual methods for VAT reporting, read in full | https://frcs.org.fj/public-notice/public-notice-important-notice-to-all-taxpayers-clarification-on-cash-and-accrual-accounting-methods-for-vat-reporting/ | 2026-11-05 |
| FRCS notice, reminder for October 2026 filing and payment, read in full | https://frcs.org.fj/public-notice/reminder-tax-filing-and-payment-notice-5/ | 2026-11-05 |
| FNPF Employers page, contribution rate section read | https://myfnpf.com.fj/employers/ | 2026-11-05 |
| FNPF notice on the voluntary and additional contribution limit, read in full | https://myfnpf.com.fj/2025/02/19/fnpf-reverts-to-old-voluntary-and-additional-contribution-limit/ | 2026-11-05 |
| TPOS portal, named only | https://tpos.frcs.org.fj/taxpayerportal/#/Logon | not read; named on 2026-11-05 |
| FRCS File On Time page, cited by the earlier version | https://frcs.org.fj/about-us/cis-2025-2028/key-tax-obligations/file-on-time/ | tried 2026-11-05: 404, not read |
| FRCS Debt Management page at the earlier path | https://frcs.org.fj/our-services/taxation/debt-management-service/debt-management-services-dms/ | tried 2026-11-05: 404, not read |
| FRCS PAYE tax tables at the earlier path | https://frcs.org.fj/our-services/calculators/paye-tax-tables/ | tried 2026-11-05: 404, not read |
| SIG 2026-01, e-money services, linked from FRCS's SIG list | https://frcs.org.fj/files/2026/01/SIG-2026-01-Tax-Implications-on-E-money-Services.pdf | tried 2026-11-05: 404, not read |
| SIG 2026-02, VAT national budget amendments, linked from FRCS's SIG list | https://frcs.org.fj/files/2026/01/SIG-2026-02-VALUE-ADDED-TAX-ACT-1991-NATIONAL-BUDGET-AMMENDMENTS-2025-2026-.pdf | tried 2026-11-05: 404, not read |
| Parliament of Fiji, Acts and Bills lists | https://www.parliament.gov.fj/acts/ ; https://www.parliament.gov.fj/bills/ | tried 2026-11-05: JavaScript challenge, not read |
| Fiji laws site | https://www.laws.gov.fj/ | tried 2026-11-05: no statute text, not read |

Not yet confirmed: enactment, final text and commencement of Bills 14, 15 and 22 of 2026 and any regulations under them, including the FNPF 16% period and split in an Act, the employer 150% measure, a rebate on the Fund page and a deduction in the Budget Summary, and every Budget measure held above; any earlier 2026 Income Tax amendment implied by the title 'No. 2'; Legal Notice 36 of 2025, which amends the same Regulations as the bands, Legal Notice 37 of 2025, and whether any later notice alters the bands; the FNPF Act for every Fund page rate, and the Gazette for the $250,000 limit; any FNPF wage ceiling; deduction for a self-employed person's own voluntary FNPF contribution, after a complete search; the current level of the extra deduction for additional employer contributions; ECAL on prescribed services; Presumptive Income Tax commencement and rate; whether section 25(20) reaches an existing tour operator, against SIG 2026-07 para 24; whether section 125A's removal affects the 2024 tax year; whether a current-year loss can reduce employment income after that removal (this guide infers it cannot); whether consecutive jobs or a part year need a PIT-S on FRCS's list when sections 105 and 125 require none; dividend exemption scope (Exempt Income Schedule Part 5 against the FRCS exemptions page); home office and mileage evidence rules; express VAT treatment in gross proceeds; provisional tax on the VAT-exclusive amount, FRCS page practice; section 117 against regulation 5 on remittance date; section 108 against FRCS's 30 days after assessment for self-assessment; whether TAA s 43(1)(a) and (b) add together, and how months of default are counted; TAA ss 45 and 46 against the percentages on FRCS's penalties page; a general interest charge on arrears; any filing extension for 2025 or 2026 returns, and past extensions such as 31 May; the asset declaration thresholds, format and restart date, and whether the requirement runs from 1 August 2025 (Act 8 of 2025) or 1 January 2026 (SIG 2026-08); the 2026 PIT-B and PIT-S forms and FRCS's TPOS user guide; Income Tax (Allowances) Regulations 2019 and Employment Incentives Regulations; class of printers and scanners for depreciation; grant treatment; non-resident withholding on foreign software subscriptions and the 3% or 3.75% insurance rate; treaty position; source rules in section 7 beyond employment income; SIG 2026-01 and SIG 2026-02; national minimum wage; bank statement layouts.

### Version history

| Version | Date | Change |
| --- | --- | --- |
| 0.2 | 2026-11-05 | Converted to the upstream template. Tied bands to Legal Notice 55 of 2023; corrected residence, deduction test, employee FNPF, depreciation, advance and provisional tax, VAT rate, penalties and losses; held the 2026-27 Budget measures. |
| 0.1 | 2026-11-01 | Legacy version. Named no reviewer. |

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.
