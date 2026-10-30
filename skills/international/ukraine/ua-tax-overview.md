---
name: ua-tax-overview
description: "A one-page map of the Ukrainian tax system for tax year 2026, from the Tax Code of Ukraine as consolidated on zakon.rada.gov.ua with the martial-law amendments to October 2026. Covers the tax year, currency, the tax authority, who is resident, personal income tax at 18% (5% and 9% on dividends), the military levy (5% for individuals, 1% for single-tax group 3, 10% of the minimum wage for groups 1, 2 and 4, none on company profit), corporate income tax at 18% with 25% for financial institutions and 50% for banks in 2026, the 15% withholding on payments to non-residents, the single-tax groups, VAT at 20%, 14%, 7% and 0% with the UAH 1,000,000 registration threshold, and the main filing and payment deadlines. Use for 'how does tax work in Ukraine', 'Ukraine tax overview', 'Ukraine tax rates 2026'. It points to the pack's domain skills for the detail: ua-income-tax, ua-corporate-income-tax, ukraine-vat, ua-single-tax, ua-social-contributions, ua-payroll, ua-crypto-tax, ua-tax-optimization."
jurisdiction: UA
category: international
tax_year: 2026
last_updated: 2026-10-30
version: 0.2
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Ukraine Tax Overview

## Ukraine Tax Overview v0.2

This is a map, not a computation skill. Each line gives the 2026 headline figure and its source, and names the skill in this pack that carries the full rules. Where a domain skill and this overview ever differ, the domain skill wins.

All article references are to the Tax Code of Ukraine (Податковий кодекс України, Law No. 2755-VI of 2 December 2010, "TCU"), consolidated text including amendments up to Law No. 4967-IX of 3 September 2026.

## The Ukrainian tax system at a glance

Ukraine taxes residents on worldwide income and non-residents on Ukrainian-source income. Martial law has been in force since 24 February 2022, and several temporary rules tied to it sit in the transitional provisions (section XX) of the Tax Code: the military levy, the 50% bank rate for 2026, and VAT invoice relief.

- **Tax year.** The Tax Code allows tax periods of a calendar year, half-year, three quarters, quarter, month or day _(TCU art. 34.1)_. Personal income tax and the annual corporate income tax return are both on the calendar year (1 January to 31 December) _(TCU art. 49.18.4, 137.4)_.
- **Currency.** Ukrainian hryvnia (UAH). Taxes are paid in money in the national currency of Ukraine, except where the Code or customs law says otherwise _(TCU art. 35.1)_.
- **Tax authority.** The controlling body is the central executive body that implements state tax policy _(TCU art. 41.1.1)_: the State Tax Service of Ukraine (Державна податкова служба України), [tax.gov.ua](https://tax.gov.ua/). Returns are filed through its Electronic Cabinet.
- **Who is resident (individuals).** A person whose place of residence is in Ukraine. If the person also has a home abroad, the tie-breakers are, in order: permanent home, centre of vital interests (closer personal or economic ties), then citizenship. Family living in Ukraine, or registration as an entrepreneur, is enough to place the centre of vital interests there. Being an e-resident is not enough _(TCU art. 14.1.213(в))_.
- **Who is resident (companies).** A legal person, and its separate units, formed and operating under Ukrainian law, wherever it is located _(TCU art. 14.1.213(а))_.
- **Residence basis of taxation.** A resident is taxed on total taxable income, on Ukrainian-source income taxed at payment, and on foreign income _(TCU art. 163.1)_. A non-resident is taxed only on income from a Ukrainian source _(TCU art. 163.2)_.

### Individuals

- **Personal income tax (PIT), main rate.** 18% of the tax base, including salary and other employment income _(TCU art. 167.1)_. Detail: `ua-income-tax`, `ua-payroll`.
- **PIT on dividends.** 5% on dividends paid by a Ukrainian company that pays corporate income tax _(TCU art. 167.5.2)_. 9% (half the 18% rate) on dividends from non-residents, collective investment institutions and companies that do not pay corporate income tax _(TCU art. 167.5.4)_. Other passive income is taxed at 18% _(TCU art. 167.5.1)_.
- **Military levy (temporary).** Charged until the Verkhovna Rada decides the reform of the Armed Forces is complete _(TCU section XX, subsection 10, point 16-1)_. Rates for 2026 _(point 16-1, sub-point 1.3)_:
  - individuals taxed under PIT: **5%** of the same income that PIT is charged on;
  - single-tax groups 1, 2 and 4 (entrepreneurs): **10% of the minimum wage** set by law on 1 January, per month, which is **UAH 864.70 a month** for 2026 (10% of UAH 8,647);
  - single-tax group 3 (except e-residents): **1%** of single-tax income.
  The levy on single-tax payers applies from 1 January 2025 to 31 December of the third calendar year after the year martial law ends _(sub-point 1.1, as amended by Law No. 4835-IX of 7 April 2026)_. Pay of service members is taxed at a separate rate under sub-point 1.3(4), and their money allowance is exempt during martial law _(sub-point 1.7)_.
- **Annual PIT declaration.** Due by 1 May of the year after the tax year _(TCU art. 49.18.4)_. For 2026 that day, 1 May 2027, is a Saturday, so the deadline moves to the next operational day _(TCU art. 49.20)_. Tax shown on the declaration is paid by **1 August** of that year _(TCU art. 179.7)_. A resident leaving Ukraine for permanent residence abroad files no later than 60 calendar days before departure _(TCU art. 179.3)_.
- **Crypto.** Detail: `ua-crypto-tax`.

### Entrepreneurs on the simplified (single tax) system

- **Minimum wage and subsistence minimum, 2026.** From 1 January 2026 the minimum wage is **UAH 8,647 a month** and the subsistence minimum for able-bodied persons is **UAH 3,328 a month** _(Law No. 4695-IX of 3 December 2025 on the State Budget of Ukraine for 2026, art. 7 and 8)_. The Tax Code ties the single-tax limits and fixed rates and the entrepreneurs' military levy to these 1 January figures.
- **Groups and income limits.** Each limit is a multiple of the minimum wage set by law on 1 January of the tax year _(TCU art. 291.4)_:
  - group 1: no employees, retail sales at markets or household services to the public, income up to **167** minimum wages (**UAH 1,444,049** for 2026);
  - group 2: services to single-tax payers or the public, production or sale of goods, restaurants; up to 10 employees; income up to **834** minimum wages (**UAH 7,211,598** for 2026);
  - group 3: entrepreneurs with any number of employees and legal entities, income up to **1,167** minimum wages (**UAH 10,091,049** for 2026);
  - group 4: agricultural producers (companies with at least 75% agricultural output in the previous year, and family-farm entrepreneurs meeting the art. 291.4(4) conditions).
- **Rates.** Group 1: up to **10%** of the subsistence minimum for able-bodied persons a month (at most **UAH 332.80** for 2026); group 2: up to **20%** of the minimum wage a month (at most **UAH 1,729.40** for 2026); both set by the local council _(TCU art. 293.1, 293.2)_. Group 3, entrepreneurs and legal entities alike: **3%** of income if they also pay VAT, **5%** if VAT is included in the single tax _(TCU art. 293.3)_. Entrepreneurs in groups 1 to 3 pay **15%** on income over the limit, on income from activity outside their group or outside the simplified system, and on income received by a non-allowed payment method _(TCU art. 293.4)_. Group 3 legal entities pay double the art. 293.3 rate (**6%** or **10%**) on those same kinds of income _(TCU art. 293.5)_.
- **Tax period.** A calendar year for groups 1, 2 and 4 _(TCU art. 294.1)_. Detail: `ua-single-tax`.
- **Unified social contribution (ЄСВ).** Set by a separate law, not the Tax Code. Detail: `ua-social-contributions`.

### Companies

- **Corporate income tax (CIT), base rate.** **18%** _(TCU art. 136.1)_.
- **Financial institutions (except insurers).** **25%** _(TCU art. 136.1-1)_.
- **Banks, 2026.** **50%** for the 2026 tax periods, and the same rate for the advance tax on dividends paid by banks _(TCU section XX, subsection 4, point 73)_.
- **Insurers.** A tax on income at **3%** on insurance contracts, or **0%** on long-term life, voluntary medical and non-state pension insurance, charged together with the 18% CIT _(TCU art. 136.2)_.
- **Diia City residents** that opt for the special regime: **9%** of the special base _(TCU art. 136.8)_. Detail and when this pays: `ua-tax-optimization`.
- **Withholding on payments to non-residents.** **15%** on Ukrainian-source income paid to a non-resident, unless a tax treaty gives a lower rate; the exceptions are in art. 141.4.4, 141.4.5 and 141.4.11 _(TCU art. 141.4.2)_.
- **Military levy.** Companies paying CIT are not on the list of levy payers, so company profit bears no levy _(TCU section XX, subsection 10, point 16-1, sub-point 1.1)_.
- **Returns.** Quarterly filers file within **40 calendar days** of the quarter end _(TCU art. 49.18.2)_. The annual return is due within **60 calendar days** of the year end _(TCU art. 49.18.3, 49.18.6)_, so 1 March 2027 for 2026. Tax is paid within **10 calendar days** after the filing deadline _(TCU art. 57.1)_. Detail: `ua-corporate-income-tax`.

### VAT (ПДВ)

- **Rates.** **20%** standard; **0%** on exports and other listed supplies; **7%** on medicines, medical devices, cultural services, hotel accommodation and other listed supplies; **14%** on listed agricultural produce _(TCU art. 193.1 (а), (б), (в), (г); art. 195)_.
- **Registration threshold.** A business must register when its taxable supplies in the last 12 calendar months exceed **UAH 1,000,000** (excluding VAT) _(TCU art. 181.1)_. Single-tax payers of groups 1 to 3 are outside this rule (see `ukraine-vat`).
- **Returns and payment.** A monthly return within **20 calendar days** after the month end _(TCU art. 49.18.1)_, and payment within **10 calendar days** after that deadline _(TCU art. 57.1)_.
- **Tax invoices** must be registered in the Unified Register of Tax Invoices; the periods, the martial-law extensions and the fines are in `ukraine-vat` _(TCU art. 201.10, 120-1)_.

## Which skill to use

| Question | Skill |
|---|---|
| A sole proprietor on the general system: PIT and military levy on net profit, the annual declaration | `ua-income-tax` |
| Company profit tax, rates for banks and financial institutions, withholding on payments abroad | `ua-corporate-income-tax` |
| VAT registration, rates, tax invoices, the monthly return | `ukraine-vat` |
| The single tax: groups, limits, rates | `ua-single-tax` |
| ЄСВ for entrepreneurs | `ua-social-contributions` |
| Hiring staff: PIT, military levy and ЄСВ on salaries | `ua-payroll` |
| Crypto and virtual assets | `ua-crypto-tax` |
| Lawful ways to lower the tax bill, Diia City | `ua-tax-optimization` |
| Registering a business | `ua-formation` |

## Sources

| Source | URL | Read on |
|---|---|---|
| Tax Code of Ukraine, Law No. 2755-VI, consolidated text with amendments to Law No. 4967-IX of 03.09.2026: art. 14.1.213, 34.1, 35.1, 41.1.1, 49.18, 49.20, 57.1, 136, 137.4, 141.4.2, 163, 167, 179.3, 179.7, 181.1, 193.1, 291.4, 293, 294.1; section XX, subsection 4, point 73; subsection 10, point 16-1. zakon.rada.gov.ua refused connections from our network, so the official text was read from the web.archive.org capture of 12 October 2026 | https://zakon.rada.gov.ua/laws/show/2755-17 (capture: https://web.archive.org/web/20261012050950/https://zakon.rada.gov.ua/laws/show/2755-17/print) | 2026-10-30 |
| Law of Ukraine No. 4695-IX of 03.12.2025 "On the State Budget of Ukraine for 2026", art. 7 (subsistence minimum) and art. 8 (minimum wage). zakon.rada.gov.ua refused connections again on 30 October 2026 (curl and a browser tab), so the text was read from the web.archive.org capture of 18 December 2025 | https://zakon.rada.gov.ua/laws/show/4695-20 (capture: https://web.archive.org/web/20251218063046/https://zakon.rada.gov.ua/laws/show/4695-20) | 2026-10-30 |
| State Tax Service of Ukraine, official site (returned 403 to our reader; named as the filing channel only) | https://tax.gov.ua/ | 2026-10-30 |

Not yet confirmed: whether the State Budget law for 2026 was amended after December 2025 in a way that changes the 1 January 2026 minimum wage or subsistence minimum (the latest capture we could open is 18 December 2025); the ЄСВ rate and bases (separate law, not read); the bank CIT rate for 2027 onward; whether the Verkhovna Rada passed tax amendments after 12 October 2026.

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
