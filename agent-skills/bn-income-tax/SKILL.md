---
name: bn-income-tax
description: "Brunei personal income tax for 2026 (year of assessment 2026). Brunei levies no tax on the income of individuals, sole proprietorships or partnerships registered as business names, from employment, self-employment, dividends, interest or capital gains. Explains what an individual still pays (SPK retirement contributions for citizens and permanent residents), why there is no PAYE or personal return, and the sole proprietor or company decision. Use for questions like do I pay income tax in Brunei, Brunei salary tax, expat tax in Brunei, sole proprietor tax Brunei or personal tax return Brunei Darussalam."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/bn-income-tax"
  jurisdiction: "BN"
  tax_year: "2026"
  last_updated: "2026-11-14"
---

# Brunei Personal Income Tax v1.0

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Who this applies to

Individuals, residents or not, of any nationality, with income in Brunei Darussalam in 2026, and individuals trading as sole proprietors or in partnerships registered as business names.

**The rule.** The Revenue Division of the Ministry of Finance and Economy states that no tax is levied on (1) unincorporated businesses, that is sole proprietorships or partnerships registered as business names, (2) personal income, meaning any earnings of an individual from employment, self-employment, dividends, interest and the like, and (3) capital gains. Income tax under the Income Tax Act (Chapter 35) is charged on companies only (see [bn-corporate-income-tax](bn-corporate-income-tax.md)).

So, for an individual:

- No income tax bands, no tax-free threshold, no personal reliefs, no personal return and no filing deadline.
- No PAYE: an employer withholds no income tax from salary.
- What does come off pay: SPK retirement contributions for citizens and permanent residents below 60 (8.5% employee rate, owned by [bn-payroll-social](bn-payroll-social.md)).

## Rates, bands and thresholds

| Item | Amount and conditions | Tax year | Official URL |
|---|---|---|---|
| Tax on personal income (employment, self-employment, dividends, interest) | None levied | 2026 | https://www.mof.gov.bn/div_revenue_faq_corporatetax/ |
| Tax on sole proprietorships and partnerships registered as business names | None levied | 2026 | same |
| Capital gains tax | None levied | 2026 | same |
| Income Tax Act charge | Applies to corporations, registered locally or elsewhere; "the provisions of the Act shall not have effect in respect of incomes of any other persons or bodies of persons" | 2026 | https://www.mof.gov.bn/div_revenue_typesoftaxes_incometax/ |
| Withholding on non-resident directors' fees paid by a Brunei company (section 37B) | 10%, withheld by the paying company | 2026 | https://www.mof.gov.bn/div_revenue_withholdingoftax_whtrate/ |

## The base

There is no personal income tax base. Points that still matter for individuals:

1. **SPK contributions.** Citizens and permanent residents below 60 in employment pay 8.5% of wages; the employer adds its share. Self-employed citizens and permanent residents may register as SPK self-employed members. Figures and method: [bn-payroll-social](bn-payroll-social.md).
2. **Business through a company.** Once the business is a company (Sdn Bhd), its profits are taxed at 18.5% after the section 35 threshold or new-company exemption ([bn-corporate-income-tax](bn-corporate-income-tax.md)). Dividends the individual then receives are not taxed.
3. **Stamp duty** applies to listed instruments (property transfers, leases, share transfers) whoever signs them; see [bn-tax-overview](bn-tax-overview.md).
4. **Non-resident directors.** A Brunei company paying a non-resident director withholds 10% (section 37B). This is the only income tax an individual can bear on Brunei-source pay, and it is collected from the company.

## Deadlines and filing

None for personal income tax: individuals do not file an income tax return in Brunei. A sole proprietor's obligations are registration of the business name with the Registry of Companies and Business Names through the One Common Portal and, for citizen or permanent resident staff, SPK contributions by the 15th of the following month.

## Penalties and interest

None for personal income tax. SPK late payment carries a dividend loss charge and service charges ([bn-payroll-social](bn-payroll-social.md)).

## Cross-border points

- **Brunei residents with foreign income.** Brunei does not tax it. Whether the source country taxes it is a question for that country's rules and any Brunei treaty (treaty list in [bn-corporate-income-tax](bn-corporate-income-tax.md)).
- **Foreign workers in Brunei.** No Brunei tax on their salary; they are not registered to SPK. Their home country may tax them on worldwide income (for example US citizens): refer to that country's skill.
- **A certificate of residence** for treaty purposes is issued by the Revenue Division on application (COR form); individuals asking for one should be referred, as the Revenue Division pages describe it for companies.

## Two worked examples that recompute

**Example 1. Citizen employee, basic salary BND 3,500 a month.** Income tax nil. SPK employee contribution 8.5% = BND 297.50. Net pay BND 3,202.50. A foreign colleague on the same salary takes home BND 3,500.00 (no tax, no SPK).

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

**Example 2 (decision). Sole proprietor or Sdn Bhd? Profit BND 300,000.** As a registered business name the profit is untaxed: tax nil. As an existing company (not in its first three years of assessment), tax is BND 100,000 x 4.625% + BND 150,000 x 9.25% + BND 50,000 x 18.5% = BND 27,750. As a newly incorporated company in its first three years, the first BND 100,000 is exempt, so BND 23,125. On tax alone the sole proprietorship wins by the full company tax; the reasons to incorporate are limited liability, contracts that require a company, and foreign shareholders, which the tax figure does not capture.

```oa-check
name: Brunei sole proprietor vs company, profit BND 300,000
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
2. Are they a Brunei citizen or permanent resident, and under 60 (SPK)?
3. Are they a director of a Brunei company while living abroad (10% withholding)?
4. Are they a citizen or resident of another country that taxes worldwide income?
5. Do they hold or transfer property or shares in Brunei (stamp duty)?

## Sources

| Source | What was read | URL | Read on |
|---|---|---|---|
| Revenue Division, FAQ corporate tax | Read for "Currently, NO tax is levied on" unincorporated businesses, personal income and capital gains | https://www.mof.gov.bn/div_revenue_faq_corporatetax/ | 2026-11-14 |
| Revenue Division, types of taxes: income tax | Read for the charge on corporations under section 8(1) and that the Act has no effect on incomes of other persons | https://www.mof.gov.bn/div_revenue_typesoftaxes_incometax/ | 2026-11-14 |
| Revenue Division, withholding tax rates | Read for the 10% rate on non-resident directors' remuneration (section 37B) | https://www.mof.gov.bn/div_revenue_withholdingoftax_whtrate/ | 2026-11-14 |
| TAP, SPK members' contribution | Read for the 8.5% member rate used in Example 1 | https://www.tap.com.bn/spk-members-contribution | 2026-11-14 |
| TAP, SPK self-employed | Read for self-employed membership (citizens and PRs below 60) | https://www.tap.com.bn/spk-self-employed | 2026-11-14 |

Not yet confirmed: whether the Revenue Division issues certificates of residence to individuals (its page describes the process for companies); the Income Tax Act (Chapter 35) section text itself, as the agc.gov.bn statute links did not open by direct URL.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-14. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `bn-income-tax` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/bn-income-tax. If neither is available, confirm every figure against the official source pages cited above before relying on it.
