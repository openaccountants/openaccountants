---
name: tw-company-formation
description: "Use this skill to set up a company, sole proprietorship (行號) or limited partnership in Taiwan in 2026 and register it for tax. It covers the entity types, the one-stop online process (name check, preparatory bank account, CPA capital verification, company registration, tax registration), government fees (name check NT$150 online, registration fee of NT$1 per NT$4,000 of capital with a NT$1,000 minimum and NT$300 off online), and the health insurance, labour insurance and 6% labour pension set-up for staff. Built from the law, not reviewed by an accountant."
jurisdiction: TW
tax_year: 2026
tax_year_notes: "Calendar 2026. Fees and steps from the government portal guide (sources dated January 2025, read 14 November 2026)."
version: "2.0"
last_updated: 2026-11-14
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
category: international
tier: 2
domain: formation
type: filing-howto
---

# Taiwan company formation and entity choice (2026)

> **General reference only.** Built from the law, not reviewed by an accountant. Do not file or act on it without review by a qualified professional in Taiwan.

## Scope

Three business forms register with the Ministry of Economic Affairs (MOEA) system or local governments: a **company** (公司: company limited by shares 股份有限公司, or limited company 有限公司), a **sole proprietorship or partnership business** (商業, 行號) and a **limited partnership** (有限合夥). Foreign companies may also open a branch (not a separate legal entity) or a representative office. Foreign investors must obtain foreign investment approval from the MOEA's investment review department before incorporation (Statute for Investment by Foreign Nationals). Company tax: `tw-corporate-income-tax`. Business tax (VAT) registration and returns: `taiwan-vat`. Health insurance: `tw-nhi`.

## Rates, bands and thresholds

| Item | Figure | Conditions | Source |
| --- | --- | --- | --- |
| Company name pre-check | NT$300 (NT$150 online) | Company, limited partnership or business name | https://www.gov.tw/News_Content_26_541581 |
| Company registration fee | NT$1 per NT$4,000 of capital in the articles; minimum NT$1,000 | NT$300 less if filed online | same |
| Business (行號) registration fee | NT$1,000 | NT$200 less if filed online | same |
| Bank account proof for a 行號 | Not needed if capital is under 25萬 (250 thousand NT dollars) | Companies always open a preparatory account | same |
| CPA capital verification | Required for companies | Not required for a 行號 | same |
| Labour insurance unit | Compulsory with 5 or more employees | Voluntary for 1 to 4 | same |
| Employment insurance and occupational accident insurance | Compulsory from the first employee | Registered units | same |
| Labour pension contribution | At least 6% of monthly wages | Employer, for each employee | same |
| Health insurance unit | Compulsory for every employer, with or without staff | NHIA | same |

## Ask the client first

1. Which form (company limited by shares, limited company, 行號, limited partnership, branch) and why (liability, investors, work permits).
2. Shareholders, directors and responsible person; foreign investors (investment approval first).
3. Capital amount (registration fee and CPA verification).
4. Business scope and address; online sales (domain names must be registered for tax).
5. Staff to hire (insurance units and pension).
6. Expected sales (business tax registration and filing in `taiwan-vat`).

## The method, step by step

1. **Choose the form.** Company limited by shares: larger or foreign-invested businesses, shares transferable. Limited company: simpler, for SMEs. 行號: sole trader or partnership, unlimited liability, no CPA capital check. Branch: extension of a foreign parent. The director and shareholder minimums under the Company Act (old file: one corporate or two individual shareholders for a company limited by shares; at least one director for a limited company) are not confirmed here; check the Company Act.
2. **Foreign investment approval** (foreign investors only), before the steps below.
3. **Name pre-check** online through the MOEA one-stop service (NT$150) with one to five candidate names; check the business registration public search first.
4. **Open a preparatory bank account** and deposit the capital.
5. **CPA capital verification report** (companies).
6. **Company registration** online through the one-stop service (fee: capital / 4,000, minimum 1,000, less 300 online) or at the city or county government.
7. **Tax registration (稅籍登記)** after the registration approval, online or at the National Taxation Bureau. From 1 January 2023, online sellers must register their domain names and web addresses; sellers on another operator's platform register that platform account.
8. **Insurance and pension:** set up the NHI unit (always), employment and occupational accident insurance (any employee), labour insurance (5 or more employees) and contribute at least 6% of wages to the labour pension.
9. **Annual compliance:** enterprise income tax (provisional in September, final in May, `tw-corporate-income-tax`), business tax returns (`taiwan-vat`), withholding statements, and MOEA filings for changes of directors, capital, address or business scope.

### Boundary and exception table

| Situation | Treatment |
| --- | --- |
| 行號 with capital under NT$250,000 | No bank account proof needed |
| Company with no employees | Still sets up the NHI unit for the responsible person |
| 1 to 4 employees | Labour insurance optional; employment and occupational accident insurance still compulsory |
| Foreign-invested company sponsoring work permits | Capital expectations apply in practice (old file: around NT$500,000; not confirmed) |
| Online sales | Domain name and web address in the tax registration |

## Worked cases

**Limited company with NT$5,000,000 capital, filed online in 2026.** Registration fee: 5,000,000 / 4,000 = 1,250, less the 300 online reduction = NT$950. Name pre-check online NT$150. Government fees: NT$1,100. (A company with capital of NT$4,000,000 or less pays the NT$1,000 minimum before the reduction.)

```oa-check
name: TW 2026 limited company registration fees, online
inputs:
  capital: 5000000
steps:
  - base_fee: max(capital / 4000, 1000)
  - registration: base_fee - 300
  - name_check: 150
  - total: registration + name_check
expected:
  base_fee: 1250
  registration: 950
  total: 1100
```

## When to refuse or refer

- Foreign investment in restricted or prohibited sectors, or investment from Mainland China (separate approval regime): refer.
- Nominee shareholders to hide the beneficial owner: refuse.
- Licensed sectors (banking, insurance, securities): refer to the sector regulator.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| Government portal (我的E政府), start-up guide citing the MOEA one-stop service, the SME administration and the digital industry agency (January 2025). Read for the steps, name pre-check, registration fees, CPA verification, tax registration, domain name rule, insurance units and 6% pension | https://www.gov.tw/News_Content_26_541581 | 2026-11-14 |
| MOEA, Regulations on company registration fees (公司登記規費收費準則). Not read: HTTP 403 to curl and WebFetch | https://law.moea.gov.tw/LawContent.aspx?id=FL011293 | 2026-11-14 |

Not yet confirmed: Company Act minimum numbers of shareholders and directors; whether the 2025 guide's fees changed in 2026; the practical capital expectation for work-permit sponsors; typical timelines (old file: 4 to 8 weeks) and professional fees (old file: NT$60,000 to 150,000), both from a vendor page and removed.
