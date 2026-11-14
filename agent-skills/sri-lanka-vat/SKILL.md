---
name: sri-lanka-vat
description: "Use this skill whenever asked to prepare, review, or classify transactions for a Sri Lanka VAT return for any client, for taxable periods in 2026 and the year of assessment 2026/27. Trigger on phrases like Sri Lanka VAT, IRD VAT return, CGIR filing, VAT registration Sri Lanka, 18% VAT Sri Lanka, VAT on digital services Sri Lanka, VAT on financial services. Covers the 18% standard rate, zero rating, the Rs. 15 million per period and Rs. 60 million per year registration test, return and payment dates, input tax, the non-resident digital services regime from 1 July 2026 and the 20.5% financial services rate from 1 July 2026, under the Value Added Tax Act No. 14 of 2002 as amended up to Act No. 14 of 2026. MUST be loaded alongside vat-workflow-base v0.1 or later."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/sri-lanka-vat"
  jurisdiction: "LK"
  tax_year: "2026"
  last_updated: "2026-11-14"
---

# Sri Lanka VAT, taxable periods in 2026, v3.0

Built from the law: not yet approved by an accountant. Not tax advice.

## Scope and who this is for

| Field | Detail |
| --- | --- |
| Country | Sri Lanka (Democratic Socialist Republic of Sri Lanka) |
| Law | Value Added Tax Act No. 14 of 2002, in force from 1 August 2002, as amended, most recently by Act No. 4 of 2025 and Act No. 14 of 2026 (certified 30 June 2026) |
| Authority | Inland Revenue Department (IRD) |
| Currency | LKR |
| Taxable period | One month or three months, as the Act defines for the person |
| Return | Electronic, through the IRD system (RAMIS), by the last day of the month after the taxable period |
| Companion skill | vat-workflow-base v0.1 or later: MUST be loaded |

- **In:** registered persons and persons who must register; classifying bank-statement transactions into a VAT return; non-resident suppliers of digital services to persons in Sri Lanka.
- **Out:** BOI enterprises with bespoke terms, the Simplified VAT (SVAT) scheme, the Tourist VAT Refund Scheme, SSCL (`sri-lanka-sscl`).

## Ask the client first

1. TIN and VAT registration status; taxable period (monthly or quarterly)?
2. Taxable supplies made in Sri Lanka in the period and in the last 12 months.
3. Any exports or other zero-rated supplies?
4. Any purchases of digital services from non-resident platforms, and is the client VAT-registered?
5. Is the client a specified institution supplying financial services, or under a BOI agreement?
6. Credit brought forward from the previous period.

## The method, step by step

### Rates, bands and thresholds

| Item | Rate or threshold | Conditions | Source |
| --- | --- | --- | --- |
| Standard rate | 18% (tax fraction 9/59) | Any taxable period from 1 January 2024; section 2(1)(ix) | https://www.ird.gov.lk/en/publications/Value%20Added%20Tax_Acts/VAT_Act_No_14%5BE%5D_2002_%28Consolidation_2025%29.pdf |
| Zero rate | 0% | Direct export of goods and services listed in section 7 | https://www.ird.gov.lk/en/publications/SitePages/tax_chart_2526.aspx |
| Registration, taxable period test | Taxable supplies in Sri Lanka in the taxable period over fifteen million rupees | From 1 January 2024; section 10 | https://www.ird.gov.lk/en/publications/Value%20Added%20Tax_Acts/VAT_Act_No_14%5BE%5D_2002_%28Consolidation_2025%29.pdf |
| Registration, 12-month test | Taxable supplies in Sri Lanka in the 12 months then ending over sixty million rupees | Or reasonable grounds that the next period will exceed fifteen million rupees or the next 12 months sixty million rupees | same |
| Financial services VAT on value addition | 18% for periods from 1 January 2022 to 30 June 2026; 20.5% from 1 July 2026 | Section 25C(3)(g), (h) | https://www.ird.gov.lk/en/publications/Value%20Added%20Tax_Acts/VAT_Act_No_14-2026_E.PDF |
| Non-resident digital services: registration | Over sixty million rupees in the 12 months then ending, or over fifteen million rupees for a quarter | From 1 July 2026; new section 25L | same |
| Non-resident digital services charge | Tax under section 2(1)(c) from 1 July 2026 | Not charged where the recipient is a registered person (section 25N) | same |
| Simplified statement penalty, non-resident supplying registered persons | Up to fifty thousand rupees | Section 25N(4) | same |
| Return due | Last day of the month after the taxable period | Electronic; section 21(1)(a)(iii) | https://www.ird.gov.lk/en/publications/Value%20Added%20Tax_Acts/VAT_Act_No_14%5BE%5D_2002_%28Consolidation_2025%29.pdf |
| Payment due | 20th day of the month after the taxable period | Quarterly filers pay month 1 by the 20th of month 2, month 2 by the 20th of month 3; section 26(1) | same |

### Steps

1. Test registration on the period and 12-month figures (section 10). Supplies made in Sri Lanka only.
2. Classify each sale: 18% standard, 0% zero-rated (section 7), or exempt (First Schedule).
3. For a VAT-inclusive receipt, output tax is the gross times 9/59.
4. Input tax: valid tax invoice with TIN, business purpose, apportionment for mixed use; block personal consumption and other items the Act disallows.
5. Imports: VAT at 18% on the import value under section 6, collected at import.
6. Digital services bought from a non-resident platform: from 1 July 2026, a registered recipient is not charged VAT (section 25N); if a registered non-resident provider charged it anyway, it must refund it, or, if it has remitted it, the registered recipient may deduct it as input tax on the provider's invoice showing VAT separately. An unregistered recipient is charged VAT by the registered non-resident provider.
7. File by the last day of the following month; pay by the 20th.

### Conservative defaults

| Ambiguity | Default |
| --- | --- |
| Unknown rate on a sale | 18% |
| Unknown VAT status of a purchase | Not deductible |
| Unknown counterparty location | Domestic Sri Lanka |
| Unknown business-use proportion | 0% recovery |

## Boundary and exception table

### Sri Lanka-specific refusal catalogue

- **R-LK-1, BOI enterprise:** client under a Board of Investment agreement with tax holidays. "BOI enterprises have bespoke tax exemptions. Please escalate."
- **R-LK-2, SSCL interaction:** SSCL is a separate levy on turnover that excludes VAT; see `sri-lanka-sscl` (in force on 14 November 2026).
- **R-LK-3, Simplified VAT regime:** different filing requirements. Escalate.

### Supplier pattern library

These defaults classify bank lines; confirm each against the First Schedule exemptions before filing.

| Pattern | Treatment | Notes |
| --- | --- | --- |
| BOC, BANK OF CEYLON; PEOPLES BANK; COMMERCIAL BANK, COMBANK; HNB, HATTON NATIONAL; SAMPATH, SEYLAN, NDB, DFCC; NATIONS TRUST | Exclude bank charges from input tax | Banks account for VAT on financial services under section 25C, not on each fee |
| INTEREST, LOAN, REPAYMENT | Exclude | Out of scope of the return |
| IRD, INLAND REVENUE | Exclude | Tax payment |
| CUSTOMS, SRI LANKA CUSTOMS | Exclude duty; keep import VAT as input tax with the customs document | Duty is not VAT |
| EPF, ETF | Exclude | Employee funds |
| COMPANY REGISTRAR | Exclude | Registration fee |
| CEB, CEYLON ELECTRICITY; LECO; NWS&DB, NATIONAL WATER | Check the First Schedule | Utilities; treatment not confirmed |
| SLT, SRI LANKA TELECOM, DIALOG, MOBITEL, HUTCH, AIRTEL LK | Domestic 18% with a tax invoice | Telecoms |
| FRIMI, GENIE, IPAY | Exclude fees | Financial service |
| GOOGLE, MICROSOFT, META, AWS, ZOOM, SLACK, CANVA | Registered recipient: no VAT charged from 1 July 2026 (section 25N); unregistered recipient: VAT charged by the provider | Before 1 July 2026, check the provider's invoice |
| SALARY, WAGES; OWN TRANSFER, INTERNAL; DIVIDEND | Exclude | Outside VAT |
| CASH WITHDRAWAL | Ask; default exclude | |

### Tier 2 catalogue

| Item | Default |
| --- | --- |
| Vehicle costs | 0% recovery |
| Entertainment | Block |
| Digital services before 1 July 2026 | Check the provider's invoice and registration |
| BOI status | Flag; ask "BOI agreement in force?" |
| Cash withdrawals | Exclude |

### Worked classification lines (from the earlier version)

| Date | Counterparty | Gross | Net | VAT | Code | Field |
| --- | --- | --- | --- | --- | --- | --- |
| 05.04.2026 | COLOMBO TRADING PVT, invoice LK-041 | +1,180,000 | +1,000,000 | 180,000 | 18% | Output |
| 15.04.2026 | UK BUYER LTD, tea export | +5,000,000 | +5,000,000 | 0 | 0% | Zero-rated |
| 18.07.2026 | AWS, cloud hosting, registered recipient | -60,000 | -60,000 | 0 | none | Not charged (section 25N) |
| 30.04.2026 | BOC, monthly charge | -1,000 | n/a | n/a | n/a | Excluded |

The AWS line was earlier shown as self-assessed at 18%; the 2026 amendment instead removes the charge where the recipient is registered.

## Worked cases

### Case 1: domestic VAT-inclusive receipt

A registered trader receives Rs. 1,180,000 including VAT. Output tax is 9/59 of the gross.

```oa-check
name: VAT-inclusive domestic receipt at 18%
inputs:
  gross: 1180000
steps:
  - vat: round(gross * 9 / 59, 2)
  - net: gross - vat
expected:
  vat: 180000
  net: 1000000
```

### Case 2: decision, must a growing business register?

A business has taxable supplies of Rs. 4,000,000 a month: Rs. 12,000,000 a quarter and Rs. 48,000,000 over 12 months, so it is under both tests. A new contract adds Rs. 1,500,000 a month. On a three-month period that is Rs. 16,500,000, over Rs. 15,000,000, so it must register even though its 12-month total (Rs. 66,000,000 projected) is what crosses the annual test later.

```oa-check
name: Registration test, quarter and 12 months
inputs:
  monthly_now: 4000000
  monthly_extra: 1500000
steps:
  - quarter_now: monthly_now * 3
  - year_now: monthly_now * 12
  - quarter_new: (monthly_now + monthly_extra) * 3
  - year_new: (monthly_now + monthly_extra) * 12
  - quarter_excess: quarter_new - 15000000
expected:
  quarter_now: 12000000
  year_now: 48000000
  quarter_new: 16500000
  year_new: 66000000
  quarter_excess: 1500000
```

## When to refuse or refer

- BOI enterprises, SVAT scheme, Tourist VAT Refund Scheme: escalate.
- Specified institutions computing VAT on financial services value addition (section 25C): escalate; the rate rises to 20.5% from 1 July 2026.
- Non-resident digital service providers registering under Chapter IIIC: escalate the registration and simplified statement.
- Transitional periods around 1 January 2024 (15% to 18%) and 1 July 2026: verify the period dates.

## Filing and payment

| Step | Detail |
| --- | --- |
| Return | Electronically through the IRD system by the last day of the month after the taxable period; an acknowledgement is issued (section 21) |
| Schedules | In the form the Commissioner-General specifies by Gazette Order |
| Payment | By the 20th day of the month after the taxable period (section 26) |
| Working paper | Per vat-workflow-base Section 3, with Sri Lanka fields: Output 18%, Zero-rated, Exempt, Input domestic, Input imports, Net VAT |
| Bank statements | BOC, People's Bank, Commercial Bank export CSV or PDF; LKR primary; Sinhala or Tamil descriptions possible; internal transfers excluded; convert foreign currency at the CBSL rate |
| Onboarding questions | TIN; filing period; industry; exports; BOI status; credit brought forward (always ask) |

## Completion checklist

- [ ] Registration tested on the period and on 12 months
- [ ] Each sale classified 18%, 0% or exempt
- [ ] Input tax only with valid tax invoices, apportioned
- [ ] Digital services from 1 July 2026 treated under sections 25L to 25P
- [ ] Return by the last day of the following month, payment by the 20th

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| Read for sections 2(1) (rates and the section 2(1)(c) digital services charge), 10 (registration), 21 (returns), 26 (payment) and the taxable period definition in section 83 of the IRD consolidated VAT Act | https://www.ird.gov.lk/en/publications/Value%20Added%20Tax_Acts/VAT_Act_No_14%5BE%5D_2002_%28Consolidation_2025%29.pdf | 2026-11-14 |
| Read for sections 2 (digital services date moved to 1 July 2026), 4, 5, 7 (section 25C 20.5% rate) and 8 (new Chapter IIIC, sections 25L to 25P) of the VAT (Amendment) Act No. 14 of 2026 | https://www.ird.gov.lk/en/publications/Value%20Added%20Tax_Acts/VAT_Act_No_14-2026_E.PDF | 2026-11-14 |
| Read for the VAT section (registration test, standard and zero rates, financial services rows) of the IRD tax chart, the latest on the site | https://www.ird.gov.lk/en/publications/SitePages/tax_chart_2526.aspx | 2026-11-14 |
| Read for the list of VAT amending Acts on the IRD VAT page | https://www.ird.gov.lk/en/Type%20of%20Taxes/SitePages/Value%20Added%20Tax%20%28VAT%29.aspx?menuid=1204 | 2026-11-14 |

Not yet confirmed: the First Schedule exemption lists (the earlier version listed healthcare, education, residential rent and unprocessed agriculture, and financial services as exempt; financial services are in fact taxed on value addition under section 25C); utilities treatment; the blocked input tax list (personal consumption, entertainment, passenger vehicles in the earlier version); which persons file monthly and which quarterly under the section 83 definition; whether a reverse charge applies to other imported services; the SVAT scheme rules.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-14. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `sri-lanka-vat` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/sri-lanka-vat. If neither is available, confirm every figure against the official source pages cited above before relying on it.
