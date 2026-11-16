---
name: gr-cross-border
description: "Greece cross-border tax for tax year 2026 (calendar year). Covers tax residence tests for individuals (home, centre of vital interests, more than 183 days in any 12 months) and companies (Greek incorporation, registered seat, place of effective management); arriving under the special inbound regimes (art. 5A EUR 100,000 lump sum for high-net-worth movers, art. 5B 7% flat tax on foreign income of pensioners, art. 5C 50% exemption on Greek employment or business income for 7 years); leaving (deregistration procedure, the company exit tax of art. 66A); non-residents with Greek-source income such as rent or salary; withholding on outbound dividends, interest, royalties and fees, with the EU directive exemptions; treaty relief and the foreign tax credit. Trigger phrases: moving to Greece, leaving Greece, non-resident, expat, exit tax, digital nomad, Greek non-dom, 5A 5B 5C, golden visa tax. Out of scope: self-employed income tax (gr-income-tax), company tax (gr-corporate-income-tax), EFKA contributions of the self-employed (gr-efka) and of employees and employers (gr-employee-contributions), VAT (gr-vat-return)."
version: 0.4
jurisdiction: GR
tax_year: 2026
last_updated: 2026-11-16
type: situation-rules
category: cross-border
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: cross-border
---

# Greece: cross-border tax (arriving, leaving, non-residents, withholding) v0.4

This is the hub skill for anyone or any company crossing the Greek border. It sets out the residence tests, the three inbound regimes, what leaving involves, how non-residents are taxed on Greek income, and the withholding rates on payments abroad. It links to the pack's other skills for the detail of each tax:

- Self-employed income tax, presumptive income, prepayments: `gr-income-tax`
- Company income tax: `gr-corporate-income-tax`
- EFKA social contributions for the self-employed: `gr-efka`
- EFKA contributions on employees' pay, withheld and paid by the employer: `gr-employee-contributions`
- VAT: `gr-vat-return`
- Overview of the system: `gr-tax-overview`

The law is the Income Tax Code (Κώδικας Φορολογίας Εισοδήματος, ΚΦΕ, ν. 4172/2013). We read the Ministry of Finance's administrative codification of the Code, which includes amendments up to ν. 5264/2025 (Α' 239/19.12.2025), published April 2026. Procedure, fines and interest are in the Tax Procedure Code (Κώδικας Φορολογικής Διαδικασίας, ΚΦΔ, ν. 5104/2024), read in the AADE codification circular Ε.2109/2025, which includes amendments up to ν. 5259/2025. Greece's tax authority is AADE (Independent Authority for Public Revenue). For individuals the tax year is the calendar year (art. 8). The TPC consolidation is supplemented here by Law 5301/2026 art. 37 for the late-return rules. The source scopes and later-law gaps are stated below.

**Quick reference:** identify residence and income source before considering 5A, 5B or 5C. The rates below are domestic defaults, not a treaty conclusion. Collect the six facts in Ask the client first before computing; an immigration or golden-visa permission is not approval of a tax regime.

## Who this applies to

**Individuals (art. 4 ΚΦΕ).** A person is Greek tax resident if:

1. their permanent or principal residence, their habitual abode, or the centre of their vital interests (personal and economic ties) is in Greece; or
2. they are a Greek national serving abroad as a consular, diplomatic or similar public official or civil servant.

A person who is in Greece for more than 183 days in total in any 12-month period is resident from the first day of their presence in Greece. The day test does not apply to someone in Greece only for tourism, medical treatment or similar private reasons whose stay does not exceed 365 days, including short periods abroad, without overriding the home/vital-interests test in art. 4(1) (art. 4(2)).

The day-count test makes residence effective from the first day of presence once it is met. This does not decide every arrival/departure-year allocation or override a treaty residence tie-breaker; do not infer a general split-year prohibition from this provision. The move out of Greece follows the AADE deregistration procedure described under "Deadlines and filing".

**Companies and other legal entities (art. 4(3) and (4) ΚΦΕ).** An entity is Greek tax resident for a tax year if any one of these applies:

1. it was incorporated or formed under Greek law;
2. its registered seat is in Greece; or
3. its place of effective management is in Greece at any time during the tax year.

Place of effective management is judged on the facts, in particular: where day-to-day management happens, where strategic decisions are taken, where the annual general meeting is held, where the books are kept, where the board (or other executive body) meets, and where the board members live. The residence of the majority of shareholders can also be taken into account alongside these factors.

**Who is in scope here.** Anyone moving to or from Greece, a non-resident with Greek-source income, a Greek payer making payments abroad, and a Greek company moving its residence, assets or a permanent establishment out of Greece.

## Rates, bands and thresholds

| Item | Figure | Tax year | Source |
|---|---|---|---|
| Scale for employment, pension and business income: EUR 0 to 10,000 | 9% | 2026 | ΚΦΕ art. 15(1)(a), as replaced by ν. 5246/2025 art. 3(1), [ΚΦΕ codification](https://minfin.gov.gr/wp-content/uploads/2026/04/%CE%9A%CE%A9%CE%94%CE%99%CE%9A%CE%9F%CE%A0%CE%9F%CE%99%CE%97%CE%A3%CE%97-%CE%A4%CE%9F%CE%A5-%CE%9A%CE%A9%CE%94%CE%99%CE%9A%CE%91-%CE%A6%CE%9F%CE%A1%CE%9F%CE%9B%CE%9F%CE%93%CE%99%CE%91%CE%A3-%CE%95%CE%99%CE%A3%CE%9F%CE%94%CE%97%CE%9C%CE%91%CE%A4%CE%9F%CE%A3-%CE%9C%CE%95%CE%A7%CE%A1%CE%99-%CE%A4%CE%9F-%CE%9D-5264-2025.pdf) |
| EUR 10,000.01 to 20,000 | 20% | 2026 | same  [official text](https://minfin.gov.gr/wp-content/uploads/2026/04/%CE%9A%CE%A9%CE%94%CE%99%CE%9A%CE%9F%CE%A0%CE%9F%CE%99%CE%97%CE%A3%CE%97-%CE%A4%CE%9F%CE%A5-%CE%9A%CE%A9%CE%94%CE%99%CE%9A%CE%91-%CE%A6%CE%9F%CE%A1%CE%9F%CE%9B%CE%9F%CE%93%CE%99%CE%91%CE%A3-%CE%95%CE%99%CE%A3%CE%9F%CE%94%CE%97%CE%9C%CE%91%CE%A4%CE%9F%CE%A3-%CE%9C%CE%95%CE%A7%CE%A1%CE%99-%CE%A4%CE%9F-%CE%9D-5264-2025.pdf) |
| EUR 20,000.01 to 30,000 | 26% | 2026 | same  [official text](https://minfin.gov.gr/wp-content/uploads/2026/04/%CE%9A%CE%A9%CE%94%CE%99%CE%9A%CE%9F%CE%A0%CE%9F%CE%99%CE%97%CE%A3%CE%97-%CE%A4%CE%9F%CE%A5-%CE%9A%CE%A9%CE%94%CE%99%CE%9A%CE%91-%CE%A6%CE%9F%CE%A1%CE%9F%CE%9B%CE%9F%CE%93%CE%99%CE%91%CE%A3-%CE%95%CE%99%CE%A3%CE%9F%CE%94%CE%97%CE%9C%CE%91%CE%A4%CE%9F%CE%A3-%CE%9C%CE%95%CE%A7%CE%A1%CE%99-%CE%A4%CE%9F-%CE%9D-5264-2025.pdf) |
| EUR 30,000.01 to 40,000 | 34% | 2026 | same  [official text](https://minfin.gov.gr/wp-content/uploads/2026/04/%CE%9A%CE%A9%CE%94%CE%99%CE%9A%CE%9F%CE%A0%CE%9F%CE%99%CE%97%CE%A3%CE%97-%CE%A4%CE%9F%CE%A5-%CE%9A%CE%A9%CE%94%CE%99%CE%9A%CE%91-%CE%A6%CE%9F%CE%A1%CE%9F%CE%9B%CE%9F%CE%93%CE%99%CE%91%CE%A3-%CE%95%CE%99%CE%A3%CE%9F%CE%94%CE%97%CE%9C%CE%91%CE%A4%CE%9F%CE%A3-%CE%9C%CE%95%CE%A7%CE%A1%CE%99-%CE%A4%CE%9F-%CE%9D-5264-2025.pdf) |
| EUR 40,000.01 to 60,000 | 39% | 2026 | same  [official text](https://minfin.gov.gr/wp-content/uploads/2026/04/%CE%9A%CE%A9%CE%94%CE%99%CE%9A%CE%9F%CE%A0%CE%9F%CE%99%CE%97%CE%A3%CE%97-%CE%A4%CE%9F%CE%A5-%CE%9A%CE%A9%CE%94%CE%99%CE%9A%CE%91-%CE%A6%CE%9F%CE%A1%CE%9F%CE%9B%CE%9F%CE%93%CE%99%CE%91%CE%A3-%CE%95%CE%99%CE%A3%CE%9F%CE%94%CE%97%CE%9C%CE%91%CE%A4%CE%9F%CE%A3-%CE%9C%CE%95%CE%A7%CE%A1%CE%99-%CE%A4%CE%9F-%CE%9D-5264-2025.pdf) |
| Over EUR 60,000 | 44% | 2026 | same  [official text](https://minfin.gov.gr/wp-content/uploads/2026/04/%CE%9A%CE%A9%CE%94%CE%99%CE%9A%CE%9F%CE%A0%CE%9F%CE%99%CE%97%CE%A3%CE%97-%CE%A4%CE%9F%CE%A5-%CE%9A%CE%A9%CE%94%CE%99%CE%9A%CE%91-%CE%A6%CE%9F%CE%A1%CE%9F%CE%9B%CE%9F%CE%93%CE%99%CE%91%CE%A3-%CE%95%CE%99%CE%A3%CE%9F%CE%94%CE%97%CE%9C%CE%91%CE%A4%CE%9F%CE%A3-%CE%9C%CE%95%CE%A7%CE%A1%CE%99-%CE%A4%CE%9F-%CE%9D-5264-2025.pdf) |
| Taxpayers with dependent children: 2nd band 18%, 16% or 9% (1, 2 or 3 children); 3rd band 24%, 22%, 20% or 18% (1 to 4 children, 2 points less for each child over 4); 0% on the first two bands with 4 or more children | see art. 15(1)(b) to (d) | 2026 | same  [official text](https://minfin.gov.gr/wp-content/uploads/2026/04/%CE%9A%CE%A9%CE%94%CE%99%CE%9A%CE%9F%CE%A0%CE%9F%CE%99%CE%97%CE%A3%CE%97-%CE%A4%CE%9F%CE%A5-%CE%9A%CE%A9%CE%94%CE%99%CE%9A%CE%91-%CE%A6%CE%9F%CE%A1%CE%9F%CE%9B%CE%9F%CE%93%CE%99%CE%91%CE%A3-%CE%95%CE%99%CE%A3%CE%9F%CE%94%CE%97%CE%9C%CE%91%CE%A4%CE%9F%CE%A3-%CE%9C%CE%95%CE%A7%CE%A1%CE%99-%CE%A4%CE%9F-%CE%9D-5264-2025.pdf) |
| Young taxpayers, first EUR 20,000: 0% up to age 25; 9% aged 26 to 30 | art. 15(1)(e) | 2026 | same  [official text](https://minfin.gov.gr/wp-content/uploads/2026/04/%CE%9A%CE%A9%CE%94%CE%99%CE%9A%CE%9F%CE%A0%CE%9F%CE%99%CE%97%CE%A3%CE%97-%CE%A4%CE%9F%CE%A5-%CE%9A%CE%A9%CE%94%CE%99%CE%9A%CE%91-%CE%A6%CE%9F%CE%A1%CE%9F%CE%9B%CE%9F%CE%93%CE%99%CE%91%CE%A3-%CE%95%CE%99%CE%A3%CE%9F%CE%94%CE%97%CE%9C%CE%91%CE%A4%CE%9F%CE%A3-%CE%9C%CE%95%CE%A7%CE%A1%CE%99-%CE%A4%CE%9F-%CE%9D-5264-2025.pdf) |
| Tax reduction on employment and pension income (art. 16), no dependent children | EUR 777, reduced by EUR 20 per EUR 1,000 of taxable employment and pension income over EUR 12,000 | 2024 onwards, so 2026 | ΚΦΕ art. 16(1) and (2), as amended by ν. 5045/2023 art. 43, same  [official text](https://minfin.gov.gr/wp-content/uploads/2026/04/%CE%9A%CE%A9%CE%94%CE%99%CE%9A%CE%9F%CE%A0%CE%9F%CE%99%CE%97%CE%A3%CE%97-%CE%A4%CE%9F%CE%A5-%CE%9A%CE%A9%CE%94%CE%99%CE%9A%CE%91-%CE%A6%CE%9F%CE%A1%CE%9F%CE%9B%CE%9F%CE%93%CE%99%CE%91%CE%A3-%CE%95%CE%99%CE%A3%CE%9F%CE%94%CE%97%CE%9C%CE%91%CE%A4%CE%9F%CE%A3-%CE%9C%CE%95%CE%A7%CE%A1%CE%99-%CE%A4%CE%9F-%CE%9D-5264-2025.pdf) |
| Electronic payment spending requirement for residents, subject to art. 15(6) exceptions | 30% of real employment, pension and business income, capped at EUR 20,000 of spending; 22% tax on any shortfall. Does not apply to non-residents filing in Greece | 2026 | ΚΦΕ art. 15(6)(b) and (c)(iv), same  [official text](https://minfin.gov.gr/wp-content/uploads/2026/04/%CE%9A%CE%A9%CE%94%CE%99%CE%9A%CE%9F%CE%A0%CE%9F%CE%99%CE%97%CE%A3%CE%97-%CE%A4%CE%9F%CE%A5-%CE%9A%CE%A9%CE%94%CE%99%CE%9A%CE%91-%CE%A6%CE%9F%CE%A1%CE%9F%CE%9B%CE%9F%CE%93%CE%99%CE%91%CE%A3-%CE%95%CE%99%CE%A3%CE%9F%CE%94%CE%97%CE%9C%CE%91%CE%A4%CE%9F%CE%A3-%CE%9C%CE%95%CE%A7%CE%A1%CE%99-%CE%A4%CE%9F-%CE%9D-5264-2025.pdf) |
| Rental income from Greek property: EUR 0 to 12,000 | 15% | 2026 | ΚΦΕ art. 40(4), as amended by ν. 5246/2025 art. 8, same  [official text](https://minfin.gov.gr/wp-content/uploads/2026/04/%CE%9A%CE%A9%CE%94%CE%99%CE%9A%CE%9F%CE%A0%CE%9F%CE%99%CE%97%CE%A3%CE%97-%CE%A4%CE%9F%CE%A5-%CE%9A%CE%A9%CE%94%CE%99%CE%9A%CE%91-%CE%A6%CE%9F%CE%A1%CE%9F%CE%9B%CE%9F%CE%93%CE%99%CE%91%CE%A3-%CE%95%CE%99%CE%A3%CE%9F%CE%94%CE%97%CE%9C%CE%91%CE%A4%CE%9F%CE%A3-%CE%9C%CE%95%CE%A7%CE%A1%CE%99-%CE%A4%CE%9F-%CE%9D-5264-2025.pdf) |
| Rental income: EUR 12,000.01 to 24,000 | 25% | 2026 | same  [official text](https://minfin.gov.gr/wp-content/uploads/2026/04/%CE%9A%CE%A9%CE%94%CE%99%CE%9A%CE%9F%CE%A0%CE%9F%CE%99%CE%97%CE%A3%CE%97-%CE%A4%CE%9F%CE%A5-%CE%9A%CE%A9%CE%94%CE%99%CE%9A%CE%91-%CE%A6%CE%9F%CE%A1%CE%9F%CE%9B%CE%9F%CE%93%CE%99%CE%91%CE%A3-%CE%95%CE%99%CE%A3%CE%9F%CE%94%CE%97%CE%9C%CE%91%CE%A4%CE%9F%CE%A3-%CE%9C%CE%95%CE%A7%CE%A1%CE%99-%CE%A4%CE%9F-%CE%9D-5264-2025.pdf) |
| Rental income: EUR 24,000.01 to 36,000 | 35% | 2026 | same  [official text](https://minfin.gov.gr/wp-content/uploads/2026/04/%CE%9A%CE%A9%CE%94%CE%99%CE%9A%CE%9F%CE%A0%CE%9F%CE%99%CE%97%CE%A3%CE%97-%CE%A4%CE%9F%CE%A5-%CE%9A%CE%A9%CE%94%CE%99%CE%9A%CE%91-%CE%A6%CE%9F%CE%A1%CE%9F%CE%9B%CE%9F%CE%93%CE%99%CE%91%CE%A3-%CE%95%CE%99%CE%A3%CE%9F%CE%94%CE%97%CE%9C%CE%91%CE%A4%CE%9F%CE%A3-%CE%9C%CE%95%CE%A7%CE%A1%CE%99-%CE%A4%CE%9F-%CE%9D-5264-2025.pdf) |
| Rental income: over EUR 36,000 | 45% | 2026 | same  [official text](https://minfin.gov.gr/wp-content/uploads/2026/04/%CE%9A%CE%A9%CE%94%CE%99%CE%9A%CE%9F%CE%A0%CE%9F%CE%99%CE%97%CE%A3%CE%97-%CE%A4%CE%9F%CE%A5-%CE%9A%CE%A9%CE%94%CE%99%CE%9A%CE%91-%CE%A6%CE%9F%CE%A1%CE%9F%CE%9B%CE%9F%CE%93%CE%99%CE%91%CE%A3-%CE%95%CE%99%CE%A3%CE%9F%CE%94%CE%97%CE%9C%CE%91%CE%A4%CE%9F%CE%A3-%CE%9C%CE%95%CE%A7%CE%A1%CE%99-%CE%A4%CE%9F-%CE%9D-5264-2025.pdf) |
| Deduction from gross rent for an individual landlord (repairs, maintenance and other property costs) | 5% | 2026 | ΚΦΕ art. 39(3)(a), same  [official text](https://minfin.gov.gr/wp-content/uploads/2026/04/%CE%9A%CE%A9%CE%94%CE%99%CE%9A%CE%9F%CE%A0%CE%9F%CE%99%CE%97%CE%A3%CE%97-%CE%A4%CE%9F%CE%A5-%CE%9A%CE%A9%CE%94%CE%99%CE%9A%CE%91-%CE%A6%CE%9F%CE%A1%CE%9F%CE%9B%CE%9F%CE%93%CE%99%CE%91%CE%A3-%CE%95%CE%99%CE%A3%CE%9F%CE%94%CE%97%CE%9C%CE%91%CE%A4%CE%9F%CE%A3-%CE%9C%CE%95%CE%A7%CE%A1%CE%99-%CE%A4%CE%9F-%CE%9D-5264-2025.pdf) |
| Art. 5A lump-sum tax on all foreign income (high-net-worth movers) | EUR 100,000 a year, for up to 15 tax years | 2026 | ΚΦΕ art. 5A(2) and (4), same; [AADE guide, 12.11.2025](https://aade.gr/sites/default/files/2025-11/forologika_kinitra.pdf) |
| Art. 5A extension to each relative (spouse, ascendants and descendants in the direct line; AADE treats civil partners as spouses) | EUR 20,000 a year per relative | 2026 | ΚΦΕ art. 5A(2) and art. 2(στ), same; AADE guide, section 1.3  [official text](https://minfin.gov.gr/wp-content/uploads/2026/04/%CE%9A%CE%A9%CE%94%CE%99%CE%9A%CE%9F%CE%A0%CE%9F%CE%99%CE%97%CE%A3%CE%97-%CE%A4%CE%9F%CE%A5-%CE%9A%CE%A9%CE%94%CE%99%CE%9A%CE%91-%CE%A6%CE%9F%CE%A1%CE%9F%CE%9B%CE%9F%CE%93%CE%99%CE%91%CE%A3-%CE%95%CE%99%CE%A3%CE%9F%CE%94%CE%97%CE%9C%CE%91%CE%A4%CE%9F%CE%A3-%CE%9C%CE%95%CE%A7%CE%A1%CE%99-%CE%A4%CE%9F-%CE%9D-5264-2025.pdf) |
| Art. 5A minimum Greek investment (not needed if the person holds an investor residence permit under art. 16 ν. 4251/2014) | EUR 500,000, completed within 3 years of the application | 2026 | ΚΦΕ art. 5A(1)(b), same  [official text](https://minfin.gov.gr/wp-content/uploads/2026/04/%CE%9A%CE%A9%CE%94%CE%99%CE%9A%CE%9F%CE%A0%CE%9F%CE%99%CE%97%CE%A3%CE%97-%CE%A4%CE%9F%CE%A5-%CE%9A%CE%A9%CE%94%CE%99%CE%9A%CE%91-%CE%A6%CE%9F%CE%A1%CE%9F%CE%9B%CE%9F%CE%93%CE%99%CE%91%CE%A3-%CE%95%CE%99%CE%A3%CE%9F%CE%94%CE%97%CE%9C%CE%91%CE%A4%CE%9F%CE%A3-%CE%9C%CE%95%CE%A7%CE%A1%CE%99-%CE%A4%CE%9F-%CE%9D-5264-2025.pdf) |
| Art. 5B flat tax on all foreign income of a pensioner | 7% a year, for up to 15 tax years | 2026 | ΚΦΕ art. 5B(2) and (4), same  [official text](https://minfin.gov.gr/wp-content/uploads/2026/04/%CE%9A%CE%A9%CE%94%CE%99%CE%9A%CE%9F%CE%A0%CE%9F%CE%99%CE%97%CE%A3%CE%97-%CE%A4%CE%9F%CE%A5-%CE%9A%CE%A9%CE%94%CE%99%CE%9A%CE%91-%CE%A6%CE%9F%CE%A1%CE%9F%CE%9B%CE%9F%CE%93%CE%99%CE%91%CE%A3-%CE%95%CE%99%CE%A3%CE%9F%CE%94%CE%97%CE%9C%CE%91%CE%A4%CE%9F%CE%A3-%CE%9C%CE%95%CE%A7%CE%A1%CE%99-%CE%A4%CE%9F-%CE%9D-5264-2025.pdf) |
| Art. 5C exemption on Greek employment or business income | 50% of that income exempt from income tax, for 7 tax years | 2026 | ΚΦΕ art. 5C(2), (4) and (7), same  [official text](https://minfin.gov.gr/wp-content/uploads/2026/04/%CE%9A%CE%A9%CE%94%CE%99%CE%9A%CE%9F%CE%A0%CE%9F%CE%99%CE%97%CE%A3%CE%97-%CE%A4%CE%9F%CE%A5-%CE%9A%CE%A9%CE%94%CE%99%CE%9A%CE%91-%CE%A6%CE%9F%CE%A1%CE%9F%CE%9B%CE%9F%CE%93%CE%99%CE%91%CE%A3-%CE%95%CE%99%CE%A3%CE%9F%CE%94%CE%97%CE%9C%CE%91%CE%A4%CE%9F%CE%A3-%CE%9C%CE%95%CE%A7%CE%A1%CE%99-%CE%A4%CE%9F-%CE%9D-5264-2025.pdf) |
| Ordinary corporate income tax; exit tax uses the applicable art. 58 rate | 22% ordinary rate; qualifying banks and agricultural entities have different art. 58 rates | 2021 onwards, so 2026 | ΚΦΕ art. 58(1)(a) and art. 66A(2), same  [official text](https://minfin.gov.gr/wp-content/uploads/2026/04/%CE%9A%CE%A9%CE%94%CE%99%CE%9A%CE%9F%CE%A0%CE%9F%CE%99%CE%97%CE%A3%CE%97-%CE%A4%CE%9F%CE%A5-%CE%9A%CE%A9%CE%94%CE%99%CE%9A%CE%91-%CE%A6%CE%9F%CE%A1%CE%9F%CE%9B%CE%9F%CE%93%CE%99%CE%91%CE%A3-%CE%95%CE%99%CE%A3%CE%9F%CE%94%CE%97%CE%9C%CE%91%CE%A4%CE%9F%CE%A3-%CE%9C%CE%95%CE%A7%CE%A1%CE%99-%CE%A4%CE%9F-%CE%9D-5264-2025.pdf) |
| Withholding on dividends | 5% | 2026 | ΚΦΕ art. 64(1)(a), same  [official text](https://minfin.gov.gr/wp-content/uploads/2026/04/%CE%9A%CE%A9%CE%94%CE%99%CE%9A%CE%9F%CE%A0%CE%9F%CE%99%CE%97%CE%A3%CE%97-%CE%A4%CE%9F%CE%A5-%CE%9A%CE%A9%CE%94%CE%99%CE%9A%CE%91-%CE%A6%CE%9F%CE%A1%CE%9F%CE%9B%CE%9F%CE%93%CE%99%CE%91%CE%A3-%CE%95%CE%99%CE%A3%CE%9F%CE%94%CE%97%CE%9C%CE%91%CE%A4%CE%9F%CE%A3-%CE%9C%CE%95%CE%A7%CE%A1%CE%99-%CE%A4%CE%9F-%CE%9D-5264-2025.pdf) |
| Withholding on interest | 15% general rule; art. 64(6) and (9) exclude specified bank-loan and qualifying non-resident corporate-bond interest; qualifying listed-bond interest for resident individuals is 5% under arts. 37(5), 40(2) | 2026 | ΚΦΕ art. 64(1)(b), same  [official text](https://minfin.gov.gr/wp-content/uploads/2026/04/%CE%9A%CE%A9%CE%94%CE%99%CE%9A%CE%9F%CE%A0%CE%9F%CE%99%CE%97%CE%A3%CE%97-%CE%A4%CE%9F%CE%A5-%CE%9A%CE%A9%CE%94%CE%99%CE%9A%CE%91-%CE%A6%CE%9F%CE%A1%CE%9F%CE%9B%CE%9F%CE%93%CE%99%CE%91%CE%A3-%CE%95%CE%99%CE%A3%CE%9F%CE%94%CE%97%CE%9C%CE%91%CE%A4%CE%9F%CE%A3-%CE%9C%CE%95%CE%A7%CE%A1%CE%99-%CE%A4%CE%9F-%CE%9D-5264-2025.pdf) |
| Withholding on royalties and other payments | 20%; none where the payee is a Greek-resident legal person or a Greek permanent establishment | 2026 | ΚΦΕ arts. 64(1)(c) and 62(5), same  [official text](https://minfin.gov.gr/wp-content/uploads/2026/04/%CE%9A%CE%A9%CE%94%CE%99%CE%9A%CE%9F%CE%A0%CE%9F%CE%99%CE%97%CE%A3%CE%97-%CE%A4%CE%9F%CE%A5-%CE%9A%CE%A9%CE%94%CE%99%CE%9A%CE%91-%CE%A6%CE%9F%CE%A1%CE%9F%CE%9B%CE%9F%CE%93%CE%99%CE%91%CE%A3-%CE%95%CE%99%CE%A3%CE%9F%CE%94%CE%97%CE%9C%CE%91%CE%A4%CE%9F%CE%A3-%CE%9C%CE%95%CE%A7%CE%A1%CE%99-%CE%A4%CE%9F-%CE%9D-5264-2025.pdf) |
| Withholding on fees for technical works, management, consulting and similar services | 20% where the payee is an individual (a Greek-resident individual only where the transaction exceeds EUR 300) or a legal person not resident in Greece or the EU/EEA; none where the payee is a legal person resident in Greece or the EU/EEA. Contractors building technical works of any kind carry 3% on the value of the work, whoever the payee | 2026 | ΚΦΕ arts. 62(1)(d), 62(2), 62(3), 64(1)(d) and 64(8), same  [official text](https://minfin.gov.gr/wp-content/uploads/2026/04/%CE%9A%CE%A9%CE%94%CE%99%CE%9A%CE%9F%CE%A0%CE%9F%CE%99%CE%97%CE%A3%CE%97-%CE%A4%CE%9F%CE%A5-%CE%9A%CE%A9%CE%94%CE%99%CE%9A%CE%91-%CE%A6%CE%9F%CE%A1%CE%9F%CE%9B%CE%9F%CE%93%CE%99%CE%91%CE%A3-%CE%95%CE%99%CE%A3%CE%9F%CE%94%CE%97%CE%9C%CE%91%CE%A4%CE%9F%CE%A3-%CE%9C%CE%95%CE%A7%CE%A1%CE%99-%CE%A4%CE%9F-%CE%9D-5264-2025.pdf) |
| Dividends to an EU parent (Parent-Subsidiary Directive) | 0% only with at least 10% held for at least 24 months plus all EU-form, residence and tax-subjection conditions below | 2026 | ΚΦΕ art. 63(1), same  [official text](https://minfin.gov.gr/wp-content/uploads/2026/04/%CE%9A%CE%A9%CE%94%CE%99%CE%9A%CE%9F%CE%A0%CE%9F%CE%99%CE%97%CE%A3%CE%97-%CE%A4%CE%9F%CE%A5-%CE%9A%CE%A9%CE%94%CE%99%CE%9A%CE%91-%CE%A6%CE%9F%CE%A1%CE%9F%CE%9B%CE%9F%CE%93%CE%99%CE%91%CE%A3-%CE%95%CE%99%CE%A3%CE%9F%CE%94%CE%97%CE%9C%CE%91%CE%A4%CE%9F%CE%A3-%CE%9C%CE%95%CE%A7%CE%A1%CE%99-%CE%A4%CE%9F-%CE%9D-5264-2025.pdf) |
| Interest and royalties to an associated EU company (Interest and Royalties Directive) | 0% only with qualifying 25% direct association for at least 24 months plus all EU-form, residence and tax-subjection conditions below | 2026 | ΚΦΕ art. 63(2), same  [official text](https://minfin.gov.gr/wp-content/uploads/2026/04/%CE%9A%CE%A9%CE%94%CE%99%CE%9A%CE%9F%CE%A0%CE%9F%CE%99%CE%97%CE%A3%CE%97-%CE%A4%CE%9F%CE%A5-%CE%9A%CE%A9%CE%94%CE%99%CE%9A%CE%91-%CE%A6%CE%9F%CE%A1%CE%9F%CE%9B%CE%9F%CE%93%CE%99%CE%91%CE%A3-%CE%95%CE%99%CE%A3%CE%9F%CE%94%CE%97%CE%9C%CE%91%CE%A4%CE%9F%CE%A3-%CE%9C%CE%95%CE%A7%CE%A1%CE%99-%CE%A4%CE%9F-%CE%9D-5264-2025.pdf) |

The approximate EUR 50,850 phase-out point mentioned in Example 1 is derived arithmetic, not a statutory band: EUR 12,000 + (777 / 20) x 1,000 = EUR 50,850 on a continuous, unrounded reading. Apply the actual art. 16 method and the held 5C basis question before determining final tax.

## The base

**Residents are taxed on worldwide income; non-residents only on Greek-source income** (art. 3 ΚΦΕ, as AADE states on its [non-resident](https://aade.gr/en/greeks-abroad-non-residents/income-taxation/taxation-greek-sourced-income-obtained-non-residents-pit) and [resident](https://aade.gr/en/greeks-abroad-non-residents/income-taxation/taxation-non-greek-sourced-income-obtained-greek-tax-residents-pit) pages). The general charge is not limited to income remitted to Greece. Art. 3(1) has a specific exception for qualifying foreign personnel of AN 89/1967 offices; establish that status before applying worldwide taxation. Greek-source income (art. 5(1)) includes employment exercised in Greece, Greek state and Greek fund pensions, business carried on through a Greek permanent establishment, rent from property in Greece, gains on Greek property, and the other categories listed in art. 5(1).

**Non-residents and tax reductions (art. 20).** A non-resident does not get the tax reductions of arts. 16 to 19 (for example the employment and pension tax reduction of art. 16), unless they are resident in another EU or EEA state and either (a) at least 90% of their worldwide income arises in Greece, or (b) they show their taxable income is low enough that they would get the reduction under their home state's law.

**Art. 5A, high-net-worth movers.** All conditions must be met:

1. not Greek tax resident in 7 of the 8 years before the move;
2. an investment of at least EUR 500,000 in Greek real estate, businesses, securities or shares in Greek entities, made by the person, a relative or a company they control by majority, completed within 3 years of the application (AADE says investments count from 12.12.2019). This condition does not apply to a person who holds an investor residence permit under art. 16 ν. 4251/2014.

The lump sum covers all foreign income, whatever its amount. Foreign income under the regime is not declared (art. 67(1)). Greek-source income is taxed under the normal rules and declared. Foreign tax paid on covered income cannot be credited. Art. 5A(8) exempts foreign-situated movable property passing by inheritance or gift to the qualifying person or relative, and such property transferred by that person to another; it is not an exemption for Greek property. Failing to pay the full lump sum in any year ends the regime from that year, and the person is taxed on worldwide income. If the investment is not completed within 3 years, the regime is withdrawn from the first year. On withdrawal, the general-rule tax for each affected year cannot be less than EUR 100,000; the lump sums already paid are credited only up to the tax then due, without a refund of an excess (art. 5A(5)).

**Art. 5B, pensioners.** The conditions are that the person receives foreign pension income, was not Greek tax resident in 5 of the 6 years before the move, and moves from a state that has an administrative cooperation agreement on tax with Greece. The 7% applies to all foreign income, not only the pension. Both Greek and foreign income are declared on the return (art. 67(1)). Arts. 5A and 5B cannot be combined. Either can be combined with 5C if each article's conditions are met (AADE guide, section 4).

**Art. 5C, people moving to work or do business in Greece.** The conditions are:

1. not Greek tax resident in 5 of the 6 years before the move;
2. moving from an EU or EEA state, or from a state with an administrative cooperation agreement on tax with Greece;
3. working in Greece for a Greek entity or a Greek permanent establishment of a foreign business, or starting an individual business in Greece (art. 5C(7)); and
4. declaring an intention to stay in Greece for at least 2 years.

Half of the Greek employment or business income is exempt from income tax for 7 tax years in total. The article also exempts that half from the special solidarity contribution of art. 43A, but that contribution was abolished for all income from 1.1.2023 (art. 72(74) ΚΦΕ), so it no longer matters. The regime cannot be extended beyond 7 years. If conditions 3 or 4 fail in any year, the regime ends from that year (art. 5C(5)). AADE adds that the person is also exempt from presumptive (deemed) living-expense income based on homes and cars for the 7 years. If employment or business stops for more than 12 months, withdrawal is from the tax year of cessation, not merely from the end of the 12-month interval; moving residence abroad ends the regime from the move year (AADE guide, section 3.3).

**Companies leaving: exit tax (art. 66A ΚΦΕ).** This applies only to Greek-resident legal persons and entities, and to permanent establishments in Greece. This company exit-tax article does not apply to individuals; that does not establish the absence of every possible personal tax charge on departure. The charge is on market value minus tax value of assets when any of these happens:

1. assets move from the Greek head office to a permanent establishment abroad;
2. assets move from a Greek permanent establishment to the head office or another permanent establishment abroad;
3. the company moves its tax residence out of Greece (except assets that stay effectively connected with a Greek permanent establishment); or
4. the business of a Greek permanent establishment moves abroad.

In each case the charge applies only where Greece loses the right to tax the assets. It is taxed at the applicable art. 58 rate for the year of exit, ordinarily 22%, not a universal rate for every legal entity. Instalments (see "Deadlines and filing") end, and the unpaid tax falls due at once, if the assets or the business are sold, the assets or residence later move to a third state, subject to the qualifying EEA recovery-assistance exception, the company goes bankrupt or into liquidation, or an instalment is more than 3 months late (art. 66A(5) and (6)). A genuine collection risk may require a guarantee. A delay of no more than 3 months does not itself accelerate the balance but carries late interest; other acceleration events must be notified within 3 working days. The 12-month return exception for temporary security/securities-financing or prudential/liquidity transfers still requires a nil return and may require a guarantee. Art. 66A implements art. 5 of the Anti-Tax Avoidance Directive (2016/1164/EU) and applies to transfers from 1.1.2020.

**Withholding scope (arts. 62 and 64).** Withholding applies to dividends, interest and royalties. It applies to fees for technical, management, consulting and similar services when the recipient is an individual, or a legal person resident outside Greece and outside the EU and EEA (art. 62(1)(d) and (3)). A legal person resident in Greece or in another EU or EEA state receiving those fees is not subject to withholding (art. 62(2)). A non-EU/EEA recipient of royalties or of those fees can elect to be taxed as Greek residents are and credit the tax withheld (art. 62(3)). A treaty may restrict the domestic charge only where the actual treaty conditions are satisfied and the prescribed relief form/residence evidence is supplied; a residence certificate alone is not a determination of entitlement.

## Deadlines and filing

| Event | Deadline | Source |
|---|---|---|
| Get a Greek tax number (AFM) as a non-resident, appointing a tax representative where required | Use AADE’s online "TIN & Authentication Key" application, identity verification in the office or by myAADElive where offered, and retain the electronic certificate/authentication key before using services requiring an AFM; do not infer a universal tax-law registration deadline from this service page | [AADE: TIN for non-residents](https://aade.gr/en/greeks-abroad-non-residents/registration-tax-register/issuance-tax-identification-number-and-authentication-key-and-appointment) |
| Art. 5A application | By 31 March of the tax year (also open to people who moved in the previous tax year), with proof that the EUR 500,000 minimum investment has been transferred to an account with a bank in Greece. AADE decides by the last working day of June | ΚΦΕ art. 5A(3)  [official text](https://minfin.gov.gr/wp-content/uploads/2026/04/%CE%9A%CE%A9%CE%94%CE%99%CE%9A%CE%9F%CE%A0%CE%9F%CE%99%CE%97%CE%A3%CE%97-%CE%A4%CE%9F%CE%A5-%CE%9A%CE%A9%CE%94%CE%99%CE%9A%CE%91-%CE%A6%CE%9F%CE%A1%CE%9F%CE%9B%CE%9F%CE%93%CE%99%CE%91%CE%A3-%CE%95%CE%99%CE%A3%CE%9F%CE%94%CE%97%CE%9C%CE%91%CE%A4%CE%9F%CE%A3-%CE%9C%CE%95%CE%A7%CE%A1%CE%99-%CE%A4%CE%9F-%CE%9D-5264-2025.pdf) |
| Art. 5A lump sum | One payment by the last working day of July each year; first year within 30 days of approval | ΚΦΕ art. 5A(2)  [official text](https://minfin.gov.gr/wp-content/uploads/2026/04/%CE%9A%CE%A9%CE%94%CE%99%CE%9A%CE%9F%CE%A0%CE%9F%CE%99%CE%97%CE%A3%CE%97-%CE%A4%CE%9F%CE%A5-%CE%9A%CE%A9%CE%94%CE%99%CE%9A%CE%91-%CE%A6%CE%9F%CE%A1%CE%9F%CE%9B%CE%9F%CE%93%CE%99%CE%91%CE%A3-%CE%95%CE%99%CE%A3%CE%9F%CE%94%CE%97%CE%9C%CE%91%CE%A4%CE%9F%CE%A3-%CE%9C%CE%95%CE%A7%CE%A1%CE%99-%CE%A4%CE%9F-%CE%9D-5264-2025.pdf) |
| Art. 5B application | By 31 March of the tax year (also open to people who moved in the previous tax year). The regime starts from the following tax year; AADE decides within 60 days | ΚΦΕ art. 5B(3) and (4)  [official text](https://minfin.gov.gr/wp-content/uploads/2026/04/%CE%9A%CE%A9%CE%94%CE%99%CE%9A%CE%9F%CE%A0%CE%9F%CE%99%CE%97%CE%A3%CE%97-%CE%A4%CE%9F%CE%A5-%CE%9A%CE%A9%CE%94%CE%99%CE%9A%CE%91-%CE%A6%CE%9F%CE%A1%CE%9F%CE%9B%CE%9F%CE%93%CE%99%CE%91%CE%A3-%CE%95%CE%99%CE%A3%CE%9F%CE%94%CE%97%CE%9C%CE%91%CE%A4%CE%9F%CE%A3-%CE%9C%CE%95%CE%A7%CE%A1%CE%99-%CE%A4%CE%9F-%CE%9D-5264-2025.pdf) |
| Art. 5B tax | One payment by the last working day of July each year | ΚΦΕ art. 5B(2)(b)  [official text](https://minfin.gov.gr/wp-content/uploads/2026/04/%CE%9A%CE%A9%CE%94%CE%99%CE%9A%CE%9F%CE%A0%CE%9F%CE%99%CE%97%CE%A3%CE%97-%CE%A4%CE%9F%CE%A5-%CE%9A%CE%A9%CE%94%CE%99%CE%9A%CE%91-%CE%A6%CE%9F%CE%A1%CE%9F%CE%9B%CE%9F%CE%93%CE%99%CE%91%CE%A3-%CE%95%CE%99%CE%A3%CE%9F%CE%94%CE%97%CE%9C%CE%91%CE%A4%CE%9F%CE%A3-%CE%9C%CE%95%CE%A7%CE%A1%CE%99-%CE%A4%CE%9F-%CE%9D-5264-2025.pdf) |
| Art. 5C application (online in myAADE) | Start of work by 2 July: apply by the end of that year, or during the following year, which then counts as the first year. Start after 2 July: apply for the following year, by the end of that year. AADE decides within 60 days | ΚΦΕ art. 5C(3); AADE guide, section 3.2  [official text](https://minfin.gov.gr/wp-content/uploads/2026/04/%CE%9A%CE%A9%CE%94%CE%99%CE%9A%CE%9F%CE%A0%CE%9F%CE%99%CE%97%CE%A3%CE%97-%CE%A4%CE%9F%CE%A5-%CE%9A%CE%A9%CE%94%CE%99%CE%9A%CE%91-%CE%A6%CE%9F%CE%A1%CE%9F%CE%9B%CE%9F%CE%93%CE%99%CE%91%CE%A3-%CE%95%CE%99%CE%A3%CE%9F%CE%94%CE%97%CE%9C%CE%91%CE%A4%CE%9F%CE%A3-%CE%9C%CE%95%CE%A7%CE%A1%CE%99-%CE%A4%CE%9F-%CE%9D-5264-2025.pdf) |
| Individual income tax return (residents, and non-residents with Greek-source income) | 15 March to 15 July of the year after the tax year; for 2026 income, in 2027. A person who moves residence abroad may file at any time within the filing year; this is not an indefinite extension | ΚΦΕ art. 67(3); [AADE: filing obligations](https://aade.gr/en/greeks-abroad-non-residents/income-taxation/fulfillment-tax-obligations) |
| Move of tax residence out of Greece | Application by the last business day of the first ten days of March of the year after departure; supporting documents by the last business day of the first ten days of September; applications accepted until 31 December of that year | [AADE: transferring tax residency abroad](https://aade.gr/en/greeks-abroad-non-residents/income-taxation/transferring-tax-residency-greece-abroad) |
| Company exit tax return | 3 working days before the exit event. The tax is paid in one sum with the return, or in 5 equal annual interest-free instalments where the move is to an EU state or an EEA state with a tax-debt recovery assistance agreement. The first instalment is paid with the return and the rest by the last working day of each of the next 4 years | ΚΦΕ art. 66A(3) and (4)  [official text](https://minfin.gov.gr/wp-content/uploads/2026/04/%CE%9A%CE%A9%CE%94%CE%99%CE%9A%CE%9F%CE%A0%CE%9F%CE%99%CE%97%CE%A3%CE%97-%CE%A4%CE%9F%CE%A5-%CE%9A%CE%A9%CE%94%CE%99%CE%9A%CE%91-%CE%A6%CE%9F%CE%A1%CE%9F%CE%9B%CE%9F%CE%93%CE%99%CE%91%CE%A3-%CE%95%CE%99%CE%A3%CE%9F%CE%94%CE%97%CE%9C%CE%91%CE%A4%CE%9F%CE%A3-%CE%9C%CE%95%CE%A7%CE%A1%CE%99-%CE%A4%CE%9F-%CE%9D-5264-2025.pdf) |

Non-residents earning only interest on Greek government bonds and T-bills, or on qualifying corporate bonds under art. 37(5), do not have to file a return (art. 67(1)).

## Penalties and interest

From the Tax Procedure Code (ν. 5104/2024), supplemented by [Law 5301/2026 art. 37](https://www.aade.gr/sites/default/files/2026-05/%CE%BD%205301_2026.pdf) for art. 53 (its (1A), (2) and (7), except (7)(ε), apply to breaches from 19 April 2024). Read the exact return type and exceptions before assessing a fine. The underlying consolidation is the [AADE codification Ε.2109/2025](https://www.aade.gr/sites/default/files/2025-12/e2109_2025.pdf):

| Breach | Penalty | Source |
|---|---|---|
| General informational/no-tax return and individual income-return breaches, subject to book-category and statutory exceptions below | EUR 100 per breach under art. 53(1); do not apply this as the universal book-keeping income-return fine | ΚΦΔ art. 53(1)  [official text](https://www.aade.gr/sites/default/files/2025-12/e2109_2025.pdf) |
| Late or missing tax/withholding return for single-entry taxpayers, subject to art. 53(1A), (7) and (13); excludes capital-tax and informational returns | EUR 250 per breach | ΚΦΔ art. 53(2), Law 5301/2026 art. 37  [official text](https://www.aade.gr/sites/default/files/2026-05/%CE%BD%205301_2026.pdf) |
| Same, double-entry taxpayers | EUR 500 per breach | ΚΦΔ art. 53(2), Law 5301/2026 art. 37  [official text](https://www.aade.gr/sites/default/files/2026-05/%CE%BD%205301_2026.pdf) |
| No return filed where tax would be due (income tax, withholding and others) | 50% of the tax due on the missing return | ΚΦΔ art. 53(6)  [official text](https://www.aade.gr/sites/default/files/2025-12/e2109_2025.pdf) |
| Late original income return with tax up to EUR 100; late amended income return with additional tax up to EUR 100 | No fixed fine under art. 53(1) or (2) | ΚΦΔ art. 53(7)(c)  [official text](https://www.aade.gr/sites/default/files/2026-05/%CE%BD%205301_2026.pdf) |
| Late original withholding return, or late amended withholding return whose original was also late, with tax/additional tax up to EUR 100; excludes gambling winnings | No art. 53(1)/(2) fixed fine | Law 5301/2026 art. 37, art. 53(7)(δ)  [official text](https://www.aade.gr/sites/default/files/2026-05/%CE%BD%205301_2026.pdf) |
| Late or missing VAT return with no tax payable, any book category | EUR 100; timely-original late amended VAT/withholding returns have the art. 53(7)(α) exemption | Law 5301/2026 art. 37, art. 53(1A), (7)  [official text](https://www.aade.gr/sites/default/files/2026-05/%CE%BD%205301_2026.pdf) |
| Late returns relating to a tax year wholly or partly in minority, including a parent’s return for attributed minor income | Art. 53(13) exemption from its listed fixed fines; applies to late returns submitted after publication of Law 5301/2026 | Law 5301/2026 art. 37(4), (10)  [official text](https://www.aade.gr/sites/default/files/2026-05/%CE%BD%205301_2026.pdf) |
| Inaccurate return: tax difference 5% to 20% of the tax declared | 10% of the difference | ΚΦΔ art. 54(1)(a)  [official text](https://www.aade.gr/sites/default/files/2025-12/e2109_2025.pdf) |
| Tax difference over 20% and up to 50% | 25% of the difference | ΚΦΔ art. 54(1)(b)  [official text](https://www.aade.gr/sites/default/files/2025-12/e2109_2025.pdf) |
| Tax difference over 50% | 50% of the difference | ΚΦΔ art. 54(1)(c)  [official text](https://www.aade.gr/sites/default/files/2025-12/e2109_2025.pdf) |
| Inaccurate withholding tax return | 50% of the difference | ΚΦΔ art. 54(2)  [official text](https://www.aade.gr/sites/default/files/2025-12/e2109_2025.pdf) |
| Late payment | Interest from the day after the payment deadline. There is no interest on interest | ΚΦΔ art. 52(1) and (5)  [official text](https://www.aade.gr/sites/default/files/2025-12/e2109_2025.pdf) |

The late-payment interest rate is not set in art. 52. It is set by ministerial decision under ΚΦΔ art. 83(47): decision ΔΠΕΙΣ 1198598 ΕΞ 2013 (Β' 19/2014), as kept in force by decision [Α.1120/2025](https://www.aade.gr/sites/default/files/2025-08/a_1120_2025.pdf) (Β' 4367/08.08.2025, in force from 10.08.2025). Α.1120/2025 freezes that rate for two years unless the ECB main refinancing rate moves by a cumulative 5 percentage points from its 1.1.2014 level. We did not read the percentage itself on an official page. See "Not yet confirmed".

For the inbound regimes, the sanction is losing the regime. Under 5A and 5B, failing to pay the full annual tax ends the regime from that year. Under 5A, an investment not completed within 3 years withdraws the regime from the first year.

## Cross-border points

**Treaties first.** Where Greece has a double tax treaty with the other state, the treaty decides which state may tax. The non-resident must give a tax residence certificate from their state to get treaty relief (AADE). Greek residents get an electronic residence certificate (e-TRC) through myAADE ([AADE: DTA forms](https://aade.gr/en/greeks-abroad-non-residents/income-taxation/forms-application-double-taxation-agreements)). For a person resident in both states under domestic law, the treaty tie-breaker decides residence. Check the specific treaty.

**Foreign tax credit, not exemption (art. 9 ΚΦΕ).** A Greek resident deducts foreign tax paid on foreign income from the Greek tax on that income. The credit cannot exceed the Greek tax on that income. Under art. 5A there is no credit for foreign tax on covered income. Art. 5B does not override treaties.

**Social security (EU/EEA and Switzerland).** Determine the applicable insurance system separately from income-tax residence and the 5C election. Use `gr-employee-contributions` for employees, employer shares, ceilings and APD, and `gr-efka` for self-employment. Cross-border posting, replacement-worker, expected-duration and A1 evidence must be checked before assuming Greek or home-system insurance. The previous specific Regulation 883/2004 and A1 propositions are held under Sources because the official EU text could not be read in this pass. Do not use them as a verified posting decision.

**Companies.** The 22% rate, deductions and filing are in `gr-corporate-income-tax`. Withholding on outbound dividends, interest, royalties and fees is set out above. Fees for technical, management and consulting services paid to a legal person resident in another EU/EEA state carry no withholding (art. 62(2)), subject to the distinct general-government procurement regime (8% on services, with the buyer scope, EUR 150 no-contract exception and other exclusions in art. 64(2)); paid to a legal person outside the EU/EEA or to an individual, they carry 20% (arts. 62(3) and 64(1)(d)). The EUR 300 floor of art. 64(8) applies only to a Greek-resident payee. For a non-resident without a Greek permanent establishment, withholding on these fees is not the final tax (art. 64(3)); the payee may instead opt to be taxed as a resident and credit the tax withheld (art. 62(3)). For the directive exemptions, the recipient must also have a listed EU legal form, be EU tax resident without treaty residence outside the EU, and be subject to the listed tax without an option or exemption. For dividends the 10% holding covers capital, votes or profits. For interest/royalties the 25% direct link is payer to recipient, recipient to payer, or a common company to both, held for 24 months. The percentage alone does not earn exemption. If only the 24-month period is incomplete, art. 63(3) allows a bank guarantee: tax rate / (1 minus tax rate) multiplied by the amount distributed or paid. It expires on completing the holding period and is forfeited if the holding ceases. Remit ordinary withholding by the end of the second month after payment (art. 64(7)).

## Two worked examples that recompute

### Example 1: engineer moving from Germany under art. 5C

Eleni is a German-resident engineer, aged 35, with no children. She has not been Greek tax resident in the last 6 years. She starts work for a Greek company in Athens on 1 March 2026 and declares she will stay for at least 2 years. She starts on or before 2 July, so she applies for 5C in myAADE by 31 December 2026, and 2026 is her first 5C year. Her 2026 Greek employment income, after employee social contributions, is EUR 70,000.

Under 5C, half (EUR 35,000) is exempt. The other EUR 35,000 is taxed on the 2026 scale: 9% on 10,000 (900), 20% on 10,000 (2,000), 26% on 10,000 (2,600) and 34% on 5,000 (1,700). Tax before the art. 16 reduction is EUR 7,200. Without 5C, tax on EUR 70,000 would be EUR 21,100. Without 5C the art. 16 reduction is nil, because EUR 777 is fully phased out above about EUR 50,850 of taxable salary. The difference before the art. 16 reduction is EUR 13,900 in 2026 and can run for 7 tax years (2026 to 2032).

The following alternative is an arithmetic sensitivity only, not an instruction to claim EUR 6,883 as her final liability. With 5C, the art. 16 reduction depends on which salary figure the art. 16(2) phase-out uses. On the taxable EUR 35,000 it would be EUR 777 minus EUR 460 (EUR 20 x 23), so EUR 317, and tax would be EUR 6,883. If the exempt half also counts, the reduction is nil. We have not found a ruling on this. See "Not yet confirmed".

As she is aged 31 or over with no children, no reduced rate of art. 15(1)(b) to (e) applies. Subject to the exemptions and adjustments in art. 15(6), as a Greek resident she must also spend 30% of her real income (capped at EUR 20,000) by card or other electronic means, or pay 22% on the shortfall (art. 15(6)). This example assumes she meets that requirement. It does not compute her employee EFKA contributions (see `gr-employee-contributions`). There is no special solidarity contribution: it was abolished from 2023.

```oa-check
name: Art. 5C mover, Greek salary EUR 70,000, 2026 scale, before art. 16 reduction
inputs:
  salary: 70000
  exempt_share: 0.5
steps:
  - taxable: salary * (1 - exempt_share)
  - b1: min(taxable, 10000) * 0.09
  - b2: max(min(taxable, 20000) - 10000, 0) * 0.20
  - b3: max(min(taxable, 30000) - 20000, 0) * 0.26
  - b4: max(min(taxable, 40000) - 30000, 0) * 0.34
  - b5: max(min(taxable, 60000) - 40000, 0) * 0.39
  - b6: max(taxable - 60000, 0) * 0.44
  - tax_5c: b1 + b2 + b3 + b4 + b5 + b6
  - f1: min(salary, 10000) * 0.09
  - f2: max(min(salary, 20000) - 10000, 0) * 0.20
  - f3: max(min(salary, 30000) - 20000, 0) * 0.26
  - f4: max(min(salary, 40000) - 30000, 0) * 0.34
  - f5: max(min(salary, 60000) - 40000, 0) * 0.39
  - f6: max(salary - 60000, 0) * 0.44
  - tax_normal: f1 + f2 + f3 + f4 + f5 + f6
  - saving: tax_normal - tax_5c
  - red_normal: max(777 - max(salary - 12000, 0) / 1000 * 20, 0)
  - red_5c_on_half: max(777 - max(taxable - 12000, 0) / 1000 * 20, 0)
  - tax_5c_if_half: tax_5c - red_5c_on_half
expected:
  taxable: 35000
  tax_5c: 7200.00
  tax_normal: 21100.00
  saving: 13900.00
  red_normal: 0.00
  red_5c_on_half: 317.00
  tax_5c_if_half: 6883.00
```

### Example 2: non-resident with a rented flat in Athens

Klaus lives in Munich and is not Greek tax resident. He owns a flat in Athens. His 2026 taxable rental income from it, after the 5% deduction for property costs (art. 39(3)(a)), is EUR 30,000. Rent from Greek property is Greek-source income (art. 5(1)), so he files a Greek return between 15 March and 15 July 2027. The rent is taxed separately on the art. 40(4) scale for 2026: 15% on 12,000 (1,800), 25% on 12,000 (3,000) and 35% on 6,000 (2,100). Greek tax is EUR 6,900.

As a non-resident he gets the art. 16 to 19 reductions only under the art. 20 EU/EEA test. Even if he met it, the art. 16 reduction applies only to tax under the art. 15 scale (art. 16(1)), so it does not reduce this separate rental tax. The electronic spending requirement of art. 15(6) does not apply to him as a non-resident (art. 15(6)(c)(iv)). How Germany treats the rent and relieves the Greek tax depends on the Greece-Germany treaty and German law; check both before advising.

```oa-check
name: Non-resident, Greek rental income EUR 30,000, 2026 rental scale
inputs:
  rent: 30000
steps:
  - r1: min(rent, 12000) * 0.15
  - r2: max(min(rent, 24000) - 12000, 0) * 0.25
  - r3: max(min(rent, 36000) - 24000, 0) * 0.35
  - r4: max(rent - 36000, 0) * 0.45
  - tax: r1 + r2 + r3 + r4
expected:
  tax: 6900.00
```

## Ask the client first

1. Where was the person tax resident in each of the last 8 years, and on what date did they arrive in or leave Greece? This decides residence and eligibility for 5A (7 of 8 years) and 5B or 5C (5 of 6 years).
2. Which state are they moving from? Is it an EU or EEA state, or a state with an administrative cooperation agreement on tax with Greece? This decides 5B and 5C.
3. What income do they have, where does it arise, and how much? Include salary, business income, pension, rent, dividends and gains. This decides which regime, if any, saves tax.
4. For 5C: when does the job or business start (on or before, or after, 2 July), who is the employer, and will they stay at least 2 years?
5. For 5A: what Greek investment has been made or is planned, when, and through whom? Do they hold an investor residence permit?
6. For a company: where do the board meet and decide, where are the books kept, and are any assets, the residence or a permanent establishment moving abroad? For outbound payments: who is the recipient, where are they resident, what is the holding, and since when?

## Sources

| Source and actual scope read | URL | Read on |
|---|---|---|
| Ministry income-tax codification through Law 5264/2025: read for arts. 3-5C, 8-9, 15-16, 20, 39-40, 58, 62-64, 66A-67; residence, regimes, rates, withholding conditions, exit and return procedures | https://minfin.gov.gr/wp-content/uploads/2026/04/%CE%9A%CE%A9%CE%94%CE%99%CE%9A%CE%9F%CE%A0%CE%9F%CE%99%CE%97%CE%A3%CE%97-%CE%A4%CE%9F%CE%A5-%CE%9A%CE%A9%CE%94%CE%99%CE%9A%CE%91-%CE%A6%CE%9F%CE%A1%CE%9F%CE%9B%CE%9F%CE%93%CE%99%CE%91%CE%A3-%CE%95%CE%99%CE%A3%CE%9F%CE%94%CE%97%CE%9C%CE%91%CE%A4%CE%9F%CE%A3-%CE%9C%CE%95%CE%A7%CE%A1%CE%99-%CE%A4%CE%9F-%CE%9D-5264-2025.pdf | 2026-11-16 |
| AADE inbound-regime guide, sections 1-4: read for procedures, 5C cessation and regime combinations; read the sections used, not every unrelated incentive | https://aade.gr/sites/default/files/2025-11/forologika_kinitra.pdf | 2026-11-16 |
| AADE departure procedure: read for March/September documentary deadlines, year-end acceptance, channel and decision period | https://aade.gr/en/greeks-abroad-non-residents/income-taxation/transferring-tax-residency-greece-abroad | 2026-11-16 |
| AADE filing obligations: read for who files, non-resident Greek income and bond-only exception; statute controls any outdated general English summary | https://aade.gr/en/greeks-abroad-non-residents/income-taxation/fulfillment-tax-obligations | 2026-11-16 |
| AADE DTA forms: read for residence certification, foreign relief/refund form and supporting documents; no specific treaty outcome verified | https://aade.gr/en/greeks-abroad-non-residents/income-taxation/forms-application-double-taxation-agreements | 2026-11-16 |
| AADE TIN service: read for electronic application, identity verification and tax-representative documentation, not a universal before-income statutory deadline | https://aade.gr/en/greeks-abroad-non-residents/registration-tax-register/issuance-tax-identification-number-and-authentication-key-and-appointment | 2026-11-16 |
| AADE TPC consolidation through Law 5259/2025: read for arts. 52-54; interest, late-return and inaccurate-return sanctions | https://www.aade.gr/sites/default/files/2025-12/e2109_2025.pdf | 2026-11-16 |
| Law 5301/2026 art. 37: read for current art. 53 fixed fines, small-tax exceptions, minority and effective dates; later-law scope is bounded to this amendment | https://www.aade.gr/sites/default/files/2026-05/%CE%BD%205301_2026.pdf | 2026-11-16 |
| Decision A.1120/2025: read for two-year interest-rate freeze and cumulative ECB trigger, not the underlying percentage | https://www.aade.gr/sites/default/files/2025-08/a_1120_2025.pdf | 2026-11-16 |

The law, not an older AADE English summary, supplies the 2026 income bands. The old English 9/22/28/36/44% scale is not used here. The arithmetic alternatives in Example 1 do not establish which art. 16 phase-out basis applies.

Not yet confirmed: the actual percentage in decision ΔΠΕΙΣ 1198598 ΕΞ 2013; other 2026 changes to the Income Tax Code after Law 5264/2025 and to TPC arts. 52-54 beyond the Law 5301/2026 amendment read here; whether art. 16(2) phase-out for 5C uses taxable half or whole salary; the current administrative-cooperation country list; general departure-year split allocation and any individual's alleged exit-charge absence; Germany treaty relief in Example 2; current Regulation 883/2004 arts. 11-12 and Regulation 987/2009 A1 rules (EUR-Lex returned a human-verification page on 16 November). The prior one-state/normal-workplace and posted employee/self-employed up-to-24-month/no-replacement propositions are retained here only as questions to verify, not usable guidance: https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:02004R0883-20190731. Earlier broad AADE residence/tax-category pages and the ministry publication notice remain contextual links, not claimed freshly read law: https://aade.gr/en/greeks-abroad-non-residents/income-taxation/tax-residence-natural-persons-itc ; https://aade.gr/en/greeks-abroad-non-residents/income-taxation/taxation-greek-sourced-income-obtained-non-residents-pit ; https://aade.gr/en/greeks-abroad-non-residents/income-taxation/taxation-non-greek-sourced-income-obtained-greek-tax-residents-pit ; https://www.aade.gr/omogeneis-katoikoi-exoterikoy/eisodima/forologika-kinitra-proselkysis-neon-forologikon-katoikon ; https://minfin.gov.gr/koinopoiisi-kodikopoiisis-tou-kodika-forologias-eisodimatos-symfona-me-to-arthro-83-par-55-tou-n-5104-2024/.
