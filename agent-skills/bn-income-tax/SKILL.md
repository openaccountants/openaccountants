---
name: bn-income-tax
description: "Brunei personal income tax for 2026 (year of assessment 2026). Brunei levies no tax on the income of individuals, sole proprietorships or partnerships registered as business names, from employment, self-employment, dividends, interest or capital gains. Explains what an individual still pays (SPK retirement contributions for citizens and permanent residents), why there is no PAYE or personal return, and the sole proprietor or company decision. Use for questions like do I pay income tax in Brunei, Brunei salary tax, expat tax in Brunei, sole proprietor tax Brunei or personal tax return Brunei Darussalam."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/bn-income-tax"
  jurisdiction: "BN"
  tax_year: "2026"
  last_updated: "2026-11-22"
---

# Brunei Personal Income Tax v1.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Who this applies to

Individuals, residents or not, of any nationality, with income in Brunei Darussalam in 2026, and individuals trading as sole proprietors or in partnerships registered as business names.

**The rule.** The Revenue Division of the Ministry of Finance and Economy states that no tax is levied on (1) unincorporated businesses, that is sole proprietorships or partnerships registered as business names, (2) personal income, meaning any earnings of an individual from employment, self-employment, dividends, interest and the like, and (3) capital gains. The ordinary income tax schedule in Chapter 35 applies to companies (see [bn-corporate-income-tax](bn-corporate-income-tax.md)). Special withholding can apply to covered Brunei-source payments to non-residents.

So, for an individual:

- No income tax bands, no tax-free threshold, no personal reliefs, no personal return and no filing deadline.
- No PAYE: an employer withholds no income tax from salary.
- What does come off pay: SPK retirement contributions for eligible citizens and permanent residents below 60 (8.5% employee rate, owned by [bn-payroll-social](bn-payroll-social.md)).

## Rates, bands and thresholds

| Item | Amount and conditions | Tax year | Official URL |
|---|---|---|---|
| Tax on personal income (employment, self-employment, dividends, interest) | None levied | 2026 | https://www.mof.gov.bn/div_revenue_faq_corporatetax/ |
| Tax on sole proprietorships and partnerships registered as business names | None levied | 2026 | same |
| Capital gains tax | None levied | 2026 | same |
| Ordinary corporate income tax charge, section 35(1) | Applies to taxable companies, registered locally or elsewhere. Sections 35(2)–(2B) separately charge covered payments to non-residents. | 2026 | https://www.agc.gov.bn/wp-content/uploads/2026/07/CAP-35-2024-ED-INCOME-TAX-ACT.pdf#page=69 |
| Withholding on non-resident directors' fees paid by a Brunei company (sections 35(2B) and 37B) | 10%, withheld by the paying company, subject to any applicable treaty | 2026 | https://www.mof.gov.bn/div_revenue_withholdingoftax_whtrate/ |

## The base

There is no personal income tax base. Points that still matter for individuals:

1. **SPK contributions.** Eligible citizens and permanent residents below 60 in employment pay 8.5% of covered wages, and the employer adds its share. Self-employed citizens and permanent residents below 60 may register subject to the scheme's employment and registration conditions. Figures and method: [bn-payroll-social](bn-payroll-social.md).
2. **Business through a company.** Check the section 10(4) exemption for a company with gross sales or turnover of BND 1,000,000 or less in the basis period. If ordinary corporate tax applies, use the section 35 bands or qualifying-company concession and the 18.5% rate on the remaining chargeable income ([bn-corporate-income-tax](bn-corporate-income-tax.md)). Dividends received by an individual generally carry no ordinary personal income tax.
3. **Stamp duty** applies to listed instruments (property transfers, leases, share transfers) whoever signs them; see [bn-tax-overview](bn-tax-overview.md).
4. **Non-resident directors.** A Brunei company generally withholds 10% on remuneration paid to a non-resident director under sections 35(2B) and 37B, subject to any applicable treaty. The separate non-resident withholding rules can also apply to qualifying interest, royalties and other covered payments.

## Deadlines and filing

None for personal income tax: individuals do not file an income tax return in Brunei. Register a business name through the One Common Portal if the Business Names Act requires it. Pay SPK contributions for eligible staff and lodge the payment listing by the 15th of the following month under the ordinary timetable.

## Penalties and interest

None for personal income tax. SPK late payment carries a dividend loss charge and service charges ([bn-payroll-social](bn-payroll-social.md)).

## Cross-border points

- **Brunei residents with foreign income.** Brunei does not tax it. Whether the source country taxes it is a question for that country's rules and any Brunei treaty (treaty list in [bn-corporate-income-tax](bn-corporate-income-tax.md)).
- **Foreign workers in Brunei.** Ordinary salaries carry no Brunei personal income tax. Workers who are neither Brunei citizens nor permanent residents generally fall outside SPK. Their home country may tax them on worldwide income (for example US citizens): refer to that country's skill.
- **A certificate of residence** for treaty purposes is issued by the Revenue Division on application (COR form); individuals asking for one should be referred, as the Revenue Division pages describe it for companies.

## Two worked examples that recompute

**Example 1. SPK-eligible citizen employee, basic salary BND 3,500 a month.** Income tax is nil. The 8.5% SPK employee contribution is BND 297.50, leaving BND 3,202.50 before other deductions. A colleague on the same salary who is neither a citizen nor a permanent resident has no personal income tax or SPK deduction, leaving BND 3,500.00 before any other deductions.

```oa-check
name: Brunei citizen employee, BND 3,500 basic, no income tax
inputs:
  basic: 3500
steps:
  - income_tax: basic * 0
  - spk_employee: round(basic * 0.085, 2)
  - net_citizen: basic - income_tax - spk_employee
  - net_foreign: basic - income_tax
expected:
  income_tax: 0.00
  spk_employee: 297.50
  net_citizen: 3202.50
  net_foreign: 3500.00
```

**Example 2 (decision). Sole proprietor or Sdn Bhd? Chargeable profit BND 300,000 and gross turnover BND 1,200,000.** The sole proprietor pays no ordinary income tax. An existing company pays BND 100,000 × 4.625% + BND 150,000 × 9.25% + BND 50,000 × 18.5% = BND 27,750. For a qualifying company in its first 3 YAs, the first BND 100,000 is exempt, yielding BND 23,125. Assume that the qualifying company is incorporated and registered in Brunei, resident there in each of the 3 YAs and not limited by guarantee. If gross sales or turnover for the company instead falls at or below BND 1,000,000, both forms have nil ordinary income tax under these assumptions. Consider limited liability, contract requirements and whether the proposed owners are eligible for the business form.

```oa-check
name: Brunei sole proprietor vs company, BND 300,000 profit and BND 1,200,000 turnover
inputs:
  profit: 300000
  rate: 0.185
steps:
  - tax_sole: profit * 0
  - band2: clamp(profit - 100000, 0, 150000) * 0.5 * rate
  - band3: max(profit - 250000, 0) * rate
  - tax_company_existing: min(profit, 100000) * 0.25 * rate + band2 + band3
  - tax_company_new: band2 + band3
expected:
  tax_sole: 0.00
  tax_company_existing: 27750.00
  tax_company_new: 23125.00
```

## Ask the client first

1. Is the person an individual, a sole proprietor or partnership, or a company?
2. Are they a Brunei citizen or permanent resident, and under 60 (SPK)? If comparing with a company, what is its gross sales or turnover for the basis period?
3. Are they a non-resident director of a Brunei company or receiving another covered Brunei-source payment?
4. Are they a citizen or resident of another country that taxes worldwide income?
5. Do they hold or transfer property or shares in Brunei (stamp duty)?

## Sources

| Source | What was read | URL | Read on |
|---|---|---|---|
| Income Tax Act, Chapter 35 | Turnover exemption under section 10 and corporate and non-resident charges under section 35 | https://www.agc.gov.bn/wp-content/uploads/2026/07/CAP-35-2024-ED-INCOME-TAX-ACT.pdf | 2026-11-22 |
| Revenue Division, corporate tax FAQ | Ordinary income tax treatment of unincorporated businesses, personal income and capital gains | https://www.mof.gov.bn/div_revenue_faq_corporatetax/ | 2026-11-22 |
| Revenue Division, corporate certificate of residence form | Published applicant eligibility | https://www.mof.gov.bn/wp-content/uploads/2025/10/2.-Certificate-of-Residence-Form-2023.pdf | 2026-11-22 |
| TAP, complete contribution payment | Employer's ordinary contribution and payment listing deadline | https://www.tap.com.bn/employers-responsibilities-complete-contribution-payment | 2026-11-22 |
| Business Names Act, Chapter 92 | When an individual or firm must register a business name | https://www.agc.gov.bn/AGC%20Images/LAWS/ACT_PDF/B/CHAPTER%20092.pdf | 2026-11-22 |
| National Retirement Scheme Act, Chapter 273 | Covered employees and wages, contributions and collection under sections 2, 10 and 11 | https://www.agc.gov.bn/wp-content/uploads/2026/07/CAP-283-2024-ED-NATIONAL-RETIREMENT-SCHEME-ACT.pdf | 2026-11-22 |
| National Retirement Scheme Rules 2023 | The ordinary 15th-of-the-following-month deadline under rules 16–18 | https://www.agc.gov.bn/wp-content/uploads/2026/07/S-22-2023-NATIONAL-RETIREMENT-SCHEME-RULES-2023.pdf | 2026-11-22 |
| Revenue Division, types of taxes: income tax | Read for the charge on corporations under section 8(1) and that the Act has no effect on incomes of other persons | https://www.mof.gov.bn/div_revenue_typesoftaxes_incometax/ | 2026-11-14 |
| Revenue Division, withholding tax rates | Read for the 10% rate on non-resident directors' remuneration (section 37B) | https://www.mof.gov.bn/div_revenue_withholdingoftax_whtrate/ | 2026-11-14 |
| TAP, SPK members' contribution | Read for the 8.5% member rate used in Example 1 | https://www.tap.com.bn/spk-members-contribution | 2026-11-14 |
| TAP, SPK self-employed | Read for self-employed membership (citizens and PRs below 60) | https://www.tap.com.bn/spk-self-employed | 2026-11-14 |

Not yet confirmed: whether the Revenue Division issues tax certificates of residence to individuals. The published COR form covers companies. The wording and commencement of [Income Tax Act Amendment Order S 27/2026](https://www.agc.gov.bn/brulaw_gazette2026/) also remain unconfirmed.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-22. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `bn-income-tax` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/bn-income-tax. If neither is available, confirm every figure against the official source pages cited above before relying on it.
