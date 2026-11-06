---
name: il-freelancer-ops
description: "Use this skill when advising Israeli freelancers (עצמאים) on business operations, tax deadlines, threshold monitoring, invoice requirements, and accountant package preparation. Trigger on phrases like \"osek patur threshold\", \"freelancer Israel taxes\", \"עוסק פטור\", \"עוסק מורשה\", \"עסק זעיר\", \"esek za'ir\", \"mkdamot\", \"מקדמות\", \"havila l'roe cheshbon\", \"bituach leumi self-employed\", \"ביטוח לאומי עצמאי\", \"freelancer deadlines Israel\", or any Israel freelancer operations query. ALWAYS read this skill before advising on Israeli freelancer tax operations."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/il-freelancer-ops"
  jurisdiction: "IL"
  tax_year: "2026"
  last_updated: "2026-11-03"
---

# IL Freelancer Ops

## Israel Freelancer Operations Skill v1.1

> **Based on work by [Skills IL](https://github.com/skills-il/tax-and-finance)**, licensed under MIT. Adapted for the OpenAccountants format.

## Section 1: Quick reference

**Quick reference table**

| Field | Value | Source |
| --- | --- | --- |
| Country | Israel (מדינת ישראל) | |
| Scope | Freelancer tax operations, deadlines, threshold monitoring | |
| Currency | NIS (Israeli New Shekel: ₪) | |
| Business types | Osek Murshe (עוסק מורשה), Osek Patur (עוסק פטור), Esek Za'ir (עסק זעיר) | |
| VAT rate | 18% as at January 2026 (from January 2025) | https://www.gov.il/BlobFolder/generalpage/income-tax-guide-knowyourright/he/Guides_IncomeTax_da-2025.pdf (PDF p.140) |
| Osek Patur threshold (2025) | unverified: NIS 120,000 annual turnover | unverified |
| Osek Patur threshold (2026) | NIS 122,833 expected annual turnover as at January 2026, updated once a year | https://www.gov.il/BlobFolder/generalpage/income-tax-guide-knowyourright/he/Guides_IncomeTax_da-2025.pdf (PDF p.139) |
| Tax authority | Israel Tax Authority (ITA: רשות המיסים בישראל) |
| Filing portal | Shaam Online: https://www.misim.gov.il |
| Contributor | Open Accountants Community |

### Conservative defaults

**Conservative defaults table**

| Ambiguity | Default |
| --- | --- |
| Unknown business type | Treat as Osek Murshe (higher obligations) |
| Unknown VAT filing frequency | Bi-monthly |
| Revenue near threshold | Alert at 70%: do not wait until exceeded |
| Unknown whether invoice requires allocation number | Include allocation number |
| Unknown pension deposit status | Assume no deposit made: flag Dec 31 deadline |

## Section 2: Freelancer business types

### 2.1 Osek Murshe (עוסק מורשה): Authorized dealer

**Osek Murshe attributes**

| Attribute | Detail |
| --- | --- |
| Registration | Registered for VAT at ITA |
| VAT obligation | Must charge 18% VAT on all invoices |
| Invoice type | Heshbonit Mas (חשבונית מס: tax invoice) |
| Input VAT | Can deduct input VAT (Mas Tsumos: מס תשומות) on business expenses |
| VAT filing | Two-monthly if turnover in the determining year is up to NIS 1,775,000; monthly above NIS 1,775,000 (as at 1 January 2026, updated yearly), within 15 days after the period (https://www.gov.il/BlobFolder/generalpage/income-tax-guide-knowyourright/he/Guides_IncomeTax_da-2025.pdf, PDF p.141) |
| Annual return | Form 1301 (דוח שנתי) required |
| Advance payments | Mkdamot (מקדמות): bi-monthly income tax advances |

### 2.2 Osek Patur (עוסק פטור): Exempt dealer

**Osek Patur attributes**

| Attribute | Detail |
| --- | --- |
| Eligibility | Expected annual turnover below NIS 122,833 (as at January 2026); some professions listed in VAT Registration Regulations reg. 13 (for example doctors, architects, bookkeepers) must register as Osek Murshe whatever the turnover (https://www.gov.il/BlobFolder/generalpage/income-tax-guide-knowyourright/he/Guides_IncomeTax_da-2025.pdf, PDF pp.139-140) |
| VAT obligation | Does NOT charge VAT |
| Invoice type | Kabala (קבלה: receipt) only |
| Input VAT | Cannot deduct input VAT on purchases |
| VAT filing | No periodic VAT returns; declare the previous calendar year's turnover once a year, by 31 January (https://www.gov.il/BlobFolder/generalpage/income-tax-guide-knowyourright/he/Guides_IncomeTax_da-2025.pdf, PDF p.140) |
| Annual return | Form 1301 still required for income tax |
| Threshold monitoring | Must convert to Osek Murshe if threshold exceeded mid-year |

### 2.3 Esek Za'ir (עסק זעיר): Micro business

unverified: every row in this section (introduction date, section number, the 30% deduction, the restrictions and the shared ceiling). No official text for Esek Za'ir was opened.

**Esek Za'ir attributes**

| Attribute | Detail |
| --- | --- |
| Eligibility | Under the Osek Patur revenue threshold |
| Key benefit | 30% normative expense deduction: no receipts needed |
| Reporting | Simplified; exempt from annual income tax report in most cases |
| Restriction | Cannot be a former employee of the invoiced client |
| Restriction | No more than 25% of annual revenue from a single related party |
| Threshold | Shared with Osek Patur (NIS 122,833 for 2026, CPI-indexed) |

## Section 3: Invoice requirements

### 3.1 General rules

- **Invoice numbering**: Invoice numbering must be sequential with no gaps
- **Osek number requirement**: All invoices must include the freelancer's Osek number (מספר עוסק: 9-digit taxpayer ID)
- **Osek Murshe invoice requirement**: Osek Murshe: must issue Heshbonit Mas (tax invoice) showing VAT separately
- **Osek Patur invoice requirement**: Osek Patur: issues Kabala (receipt) only: must NOT show VAT

### 3.2 Allocation numbers (Mispar Haktzaa: מספר הקצאה)

- **Allocation number requirement**: From 2026, Osek Murshe must obtain an allocation number from the Tax Authority system for tax invoices

**Allocation number thresholds**

| Effective date | Invoice threshold (before VAT) | Source |
| --- | --- | --- |
| 1 January 2026 | NIS 10,000 | https://www.gov.il/BlobFolder/generalpage/income-tax-guide-knowyourright/he/Guides_IncomeTax_da-2025.pdf (PDF p.141, VAT Law s.47(a2)(2)) |
| 1 June 2026 | NIS 5,000 | same |

- **Missing allocation number consequence**: The recipient cannot deduct the input VAT on a tax invoice above the threshold that has no allocation number (rights guide, PDF p.141). Flag any issued invoice above the threshold that is missing an allocation number.

## Section 4: Tax deadline calendar

### 4.1 Periodic deadlines

**Periodic deadlines table**

| Deadline | Frequency | Date | Details |
| --- | --- | --- | --- |
| VAT filing (Osek Murshe, two-monthly) | Two-monthly | Within 15 days after the period (https://www.gov.il/BlobFolder/generalpage/income-tax-guide-knowyourright/he/Guides_IncomeTax_da-2025.pdf, PDF p.141) | Mar 15, May 15, Jul 15, Sep 15, Nov 15, Jan 15 |
| VAT filing (monthly filers) | Monthly | same | Turnover above NIS 1,775,000 in the determining year |
| Detailed VAT report (Doch Meforat, report 874) | Monthly | unverified: 23rd of the following month | unverified: required for annual turnover > NIS 500,000; forces monthly filing |
| Bituach Leumi advances | Monthly | unverified: 15th of each month | National Insurance advance payments |
| Mkdamot (income tax advances): monthly filers | Monthly | unverified: 15th of the month after the period | Per Tax Authority assessment letter |
| Mkdamot: bi-monthly filers | Bi-monthly | unverified: 19th of the month after the period | Per Tax Authority assessment letter |

### 4.2 Annual deadlines

**Annual deadlines table**

| Deadline | Date | Details |
| --- | --- | --- |
| Osek Patur annual turnover declaration | 31 January | Declare the previous calendar year's turnover (https://www.gov.il/BlobFolder/generalpage/income-tax-guide-knowyourright/he/Guides_IncomeTax_da-2025.pdf, PDF p.140) |
| Annual income tax report (Form 1301): paper | 29 May 2026 | For tax year 2025 filed in 2026 |
| Annual income tax report (Form 1301): online | June 30 | Online filing mandatory for most filers |
| Annual income tax report: CPA extension | unverified: July 31 or later | Via CPA association quota arrangement |
| Self-employed pension deposit deadline | December 31 | Last day to deposit for that tax year's benefits |

- **Shabbat/holiday deadline shift**: If a deadline falls on Shabbat (Saturday), it moves to Sunday. If it falls on a Jewish holiday (Chag), check the ITA website for adjusted dates.

### 4.3 Pension contribution deadlines (December 31)

- **Missed deadline consequence**: Missing December 31 forfeits both tax benefits for the entire year
- **Section 45א: 35% tax credit (Zikui): credit basis**: unverified: credit on contributions up to 5.5% of business income
- **Section 45א 2026 cap**: unverified: approximately NIS 11,640 + NIS 1,164. The 2026 booklet (2026 deduction booklet p.12) lists the s.47(a) qualifying-income ceiling for a self-employed member at NIS 9,700 a month and the s.47(a)(5) additional-income ceiling at NIS 24,250 a month; how they combine into a credit cap was not confirmed
- **Section 47: Income deduction (Nikui): deduction basis**: unverified: deduction of up to 11% of qualifying income
- **Section 47 2026 qualifying-income ceiling**: unverified: NIS 232,800; max deposit approximately NIS 25,608
- **Mandatory self-employed pension contribution 2026 rates**: unverified: 4.45% on income up to half the average wage; 12.55% above it
- **Average wage 2026**: NIS 13,769 a month (2026 deduction booklet p.12, "average wage in the economy")
- **Mandatory pension nature**: This is a legal obligation, not just a tax benefit

## Section 5: Osek Patur threshold monitoring

### 5.1 Alert levels

- **Tracking approach**: Track cumulative annual revenue against the Osek Patur threshold

**Alert levels table**

| Alert level | Revenue (2026) | Action |
| --- | --- | --- |
| Informational (70%) | ~NIS 86,000 | "You've reached 70% of the annual threshold. Consider planning for potential transition." |
| Warning (85%) | ~NIS 104,400 | "Approaching threshold. Review implications of converting to Osek Murshe." |
| Urgent (95%) | ~NIS 116,700 | "Very close to threshold. Conversion may be required soon." |

### 5.2 Transition implications

- **Transition steps**: When the threshold is exceeded, the freelancer must: 1. Register as Osek Murshe at the local Tax Authority office (Misrad Mas Hachnasa: משרד מס הכנסה) 2. Begin charging VAT (18%) on all invoices 3. Switch to issuing Heshbonit Mas (tax invoices) instead of Kabala (receipts) 4. Register for the allocation number system (for invoices above the threshold) 5. Begin filing periodic VAT returns 6. Start tracking input VAT on business expenses for deductions 7. Notify clients of new invoicing format 8. Bituach Leumi payments may increase

### 5.3 Esek Za'ir alternative

- **Esek Za'ir alternative**: If income is expected to stay near the threshold, the Esek Za'ir track offers a 30% normative expense deduction and simplified reporting but shares the same revenue ceiling as Osek Patur. It does not defer the obligation to convert to Osek Murshe if the threshold is exceeded.

## Section 6: Bituach Leumi (National Insurance) for self-employed

### 6.1 Contribution rates (2026)

**Contribution rates table**

Applies to a self-employed person aged 18 or over who has not reached retirement age. Under 18 or at retirement age the page gives different rates.

| Income range | NI rate | Health rate | Total | Source |
| --- | --- | --- | --- | --- |
| Up to NIS 7,703/month (from 01.01.2026) | 4.47% | 3.23% | 7.70% | https://www.btl.gov.il/Insurance/National%20Insurance/type_list/Self_Employed/Pages/rates.aspx |
| NIS 7,703 to NIS 51,910/month (the maximum income liable to contributions) | 12.83% | 5.17% | 18.00% | same |
| Monthly income below NIS 3,442 (from 01.01.2026) | Contributions are paid on the minimum income | | | same |

- **Minimum income floor**: NIS 3,442 a month from 01.01.2026: a self-employed person whose income is lower pays contributions on the minimum income (National Insurance self-employed page).
- **Minimum monthly advance**: unverified: NIS 187 a month
- **Maximum monthly advance**: unverified: NIS 7,850 a month (it does not match 18% of NIS 51,910)
- **Direct-debit extension**: unverified: direct-debit payers (הוראת קבע) get an automatic extension to the 22nd
- **NI tax deductibility**: unverified: 52% of the NI amount is tax-deductible for income tax purposes

## Section 7: Accountant package (Havila L'Roe Cheshbon: חבילה לרואה חשבון)

### 7.1 Package contents

- **Package contents list**: 1. **Issued invoices**: all invoices/receipts issued during the period, sorted by date 2. **Received invoices/receipts**: all expense documents (business purchases, subscriptions, equipment) 3. **Bank statement summary**: transaction list matched to invoices where possible 4. **Utility bills**: electricity, telecoms, water, organized by provider 5. **Revenue summary**: running annual total with monthly breakdown 6. **Cover sheet**: summary page with key figures

### 7.2 Cover sheet fields

**Cover sheet fields table**

| Field | Description |
| --- | --- |
| Period covered | Month / quarter / year |
| Total revenue (Bruto: ברוטו) | Gross income for the period |
| Total expenses | All deductible business expenses |
| Net income (Neto: נטו) | Revenue minus expenses |
| VAT collected | For Osek Murshe only |
| VAT paid on expenses (Mas Tsumos) | For Osek Murshe only |
| Net VAT payable/refundable | Output VAT minus Input VAT |
| Running annual revenue total | Year-to-date cumulative |
| Invoice count | Number of invoices issued and received |

### 7.3 Folder structure

- **Folder structure**: Organize by period: - `YYYY-MM/invoices-issued/` - `YYYY-MM/invoices-received/` - `YYYY-MM/utility-bills/` - `YYYY-MM/bank-statements/` - Cover sheet at the root of each period folder

## Section 8: Invoice aging tracker

- **Tracking approach**: Track all issued invoices by payment status:

**Invoice aging tracker table**

| Bucket | Age | Recommended action |
| --- | --- | --- |
| Current | 0–29 days | Monitor, no action needed |
| 30-day | 30–59 days | Friendly reminder to client |
| 60-day | 60–89 days | Formal follow-up with invoice copy and payment details |
| 90+ day | 90+ days | Alert for escalation consideration |

- **Partial payments tracking**: Track partial payments and maintain running totals: total outstanding, total overdue, by client.

## Section 9: Worked examples

### Example 1: Osek Patur approaching threshold

**Scenario:** Freelance web developer, Osek Patur, has earned NIS 95,000 by September with 3 months remaining.

**Working:**
- Average monthly income: NIS 95,000 ÷ 9 = ~NIS 10,556
- Projected annual total: NIS 10,556 × 12 = ~NIS 126,667
- 2026 threshold: NIS 122,833
- Status: projected to exceed threshold by ~NIS 3,834

**Action:** Alert at 85% level. Prepare transition checklist. Recommend consulting accountant before crossing the threshold.

### Example 2: Pension contribution deadline

**Scenario:** Self-employed consultant, annual business income NIS 300,000. December 15, no pension deposits yet.

**Working:**
- unverified (the 5.5% and 11% bases and the mandatory rates were not confirmed, and the 2026 qualifying-income ceilings in 2026 deduction booklet p.12 may cap them):
- Section 45א credit: 35% on up to 5.5% of NIS 300,000 = NIS 16,500 eligible → NIS 5,775 tax credit
- Section 47 deduction: up to 11% of NIS 300,000 = NIS 33,000 deductible (marginal benefit depends on tax bracket)
- Mandatory contribution: 4.45% on income up to half the average wage + 12.55% above it
- Deadline: December 31: missing it forfeits both benefits for the entire year

**Action:** Urgent alert. Deposit to pension fund, Kupat Gemel, or insurance policy before December 31.

## Section 10: Common errors and red flags

**Common errors and red flags table**

| Error | Why it matters |
| --- | --- |
| Confusing Osek Murshe with Osek Patur | Different VAT obligations, invoice types, and filing requirements |
| Skipping zero-revenue VAT returns | Osek Murshe must file bi-monthly returns even with no revenue; missing reports trigger penalties |
| Gap in invoice numbering | Violates Tax Authority requirements; sequential numbering is mandatory |
| Missing allocation number on invoices > NIS 5,000 before VAT (NIS 10,000 from 1 January to 31 May 2026) | Recipient loses the input VAT deduction (rights guide, PDF p.141) |
| Wrong annual report deadline | Form 1301 is due 29 May 2026 (paper) / 30 June 2026 (online) for tax year 2025: not April 30 |
| Confusing Section 45א credit with mandatory pension | They are separate: 45א/47 are voluntary tax benefits; mandatory contribution is a legal floor |
| Using Bituach Leumi based on monthly actual revenue | BL advances are based on projected annual income, not actual monthly revenue |

## Section 11: Reference material

**Reference material table**

| Resource | Reference |
| --- | --- |
| Tax Authority: Form 1301 / annual report | https://www.gov.il/he/service/reporting-and-payment-2025-annual-tax-report-for-individuals |
| Tax Authority: allocation numbers | https://www.gov.il/he/service/request-assignment-number-for-tax-invoice |
| Kol Zchut: Osek Patur | https://www.kolzchut.org.il/he/עוסק_פטור |
| Kol Zchut: Esek Za'ir | https://www.kolzchut.org.il/he/עסק_זעיר |
| Kol Zchut: Section 45א pension credit | https://www.kolzchut.org.il/he/זיכוי_ממס_הכנסה_בגין_הפרשות_לביטוח_פנסיוני |
| Bituach Leumi: self-employed rates | https://www.btl.gov.il/Insurance/National%20Insurance/type_list/Self_Employed/Pages/rates.aspx |
| ITA filing portal (Shaam Online) | https://www.misim.gov.il |

## Recomputed checks (2026)

```oa-check
name: Self-employed contributions, NIS 20,000 a month (2026)
inputs:
  m: 20000
steps:
  - c: 7703*0.077+(m-7703)*0.18
expected:
  c: 2806.59
```

```oa-check
name: Exempt dealer projection (2026)
inputs:
  e: 95000
steps:
  - o: e/9*12-122833
expected:
  o: 3833.67
```

## Sources

| Source | URL | Read on |
|---|---|---|
| Israel Tax Authority, salary-deduction booklet from January 2026 (updated April 2026), read p.12 (2026 adjusted amounts: s.47(a) ceilings NIS 9,700 and NIS 24,250 a month, average wage NIS 13,769) | https://www.gov.il/BlobFolder/generalpage/income-tax-monthly-deductions-booklet/he/generalInformation_income-tax-monthly-deductions-booklet_monthly-deductions-booklet-2026.pdf | 2026-11-03 |
| Israel Tax Authority, "Know your rights and duties" guide, tax year 2025 (published July 2026), Annex C VAT guide, read PDF pp.139-141 (Osek Patur NIS 122,833 and 31 January declaration, 18% rate, allocation-number limits under VAT Law s.47(a2)(2), two-monthly/monthly NIS 1,775,000 as at 1/1/2026, 15-day deadline) | https://www.gov.il/BlobFolder/generalpage/income-tax-guide-knowyourright/he/Guides_IncomeTax_da-2025.pdf | 2026-11-03 |
| National Insurance, self-employed rates page, read the working-age table, the NIS 7,703 band and NIS 51,910 ceiling from 01.01.2026, the under-18 and retirement-age rates, and the NIS 3,442 minimum income from 01.01.2026 | https://www.btl.gov.il/Insurance/National%20Insurance/type_list/Self_Employed/Pages/rates.aspx | 2026-11-03 |
| Israel Tax Authority, Form 1301 service page, tax year 2025 | https://www.gov.il/he/service/reporting-and-payment-2025-annual-tax-report-for-individuals | 2026-11-01 |

Not yet confirmed: Esek Za'ir (all of Section 2.3 and 5.3); the Osek Patur 2025 figure of NIS 120,000; Report 874 trigger and date; National Insurance and income-tax advance dates (15th, 19th, 22nd); the CPA extension date; the s.45A 5.5% base and its 2026 cap, the s.47 11% base and NIS 232,800 ceiling; mandatory pension rates; minimum and maximum National Insurance advances (the NIS 7,850 maximum does not match 18% of NIS 51,910); 52% deductibility; the paper and online Form 1301 dates rest on the tax year 2025 service page.

## Disclaimer

> **חשוב:** כל המידע בקובץ זה מיועד למטרות מידע וחישוב בלבד. יש לבדוק כל עמדה מול רואה חשבון (Ro'eh Cheshbon) או יועץ מס (Yo'etz Mas) מוסמך לפני הגשה או פעולה.

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional: such as a רואה חשבון (Ro'eh Cheshbon: CPA) or יועץ מס (Yo'etz Mas: tax advisor) licensed in Israel: before filing or acting upon.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-03. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `il-freelancer-ops` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/il-freelancer-ops. If neither is available, confirm every figure against the official source pages cited above before relying on it.
