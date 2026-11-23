---
name: sri-lanka-vat
description: Prepare or review Sri Lanka VAT returns for taxable periods in 2026. Covers the 18% standard rate, zero rating, registration, input tax, the 1 July 2026 digital services rules and the 20.5% VAT on financial services from that date. Load alongside vat-workflow-base v0.1 or later.
version: 3.1
jurisdiction: LK
tax_year: 2026
tax_year_notes: "Taxable periods in calendar 2026 and the year of assessment 2026/27 (2026-27)"
last_updated: 2026-11-22
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: vat-gst
type: situation-rules
---

# Sri Lanka VAT, taxable periods in 2026, v3.1

Built from the law: not yet approved by an accountant. Not tax advice.

## Scope and who this is for

| Field | Detail |
| --- | --- |
| Country | Sri Lanka (Democratic Socialist Republic of Sri Lanka) |
| Law | Value Added Tax Act No. 14 of 2002, in force from 1 August 2002, as amended, most recently by Act No. 4 of 2025 and Act No. 14 of 2026 (certified 30 June 2026) |
| Authority | Inland Revenue Department (IRD) |
| Currency | LKR |
| Taxable period | Ordinarily three months. Section 83 specifies monthly periods for eligible exporters, qualifying start-up businesses or projects during implementation and qualifying suppliers to specified projects. Check any prior written approval for quarterly filing. |
| Return | File through RAMIS by the last day of the month after the taxable period. The Commissioner-General may permit a written return in special circumstances on request. |
| Companion skill | vat-workflow-base v0.1 or later: MUST be loaded |

- **In:** registered persons and persons who must register; classifying bank-statement transactions into a VAT return; non-resident suppliers of digital services to persons in Sri Lanka.
- **Out:** BOI enterprises with bespoke terms, specialist Risk-Based Refund Scheme claims, tourist VAT refunds and SSCL (`sri-lanka-sscl`).

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
| Zero rate | 0% | Qualifying exports of goods and services listed in section 7. Verify proof of export, receipt of foreign currency and the time limit where applicable. | VAT Act, s 7 |
| Registration, taxable period test | Taxable supplies in Sri Lanka in the taxable period over fifteen million rupees | From 1 January 2024; section 10 | https://www.ird.gov.lk/en/publications/Value%20Added%20Tax_Acts/VAT_Act_No_14%5BE%5D_2002_%28Consolidation_2025%29.pdf |
| Registration, 12-month test | Taxable supplies in Sri Lanka in the 12 months then ending over sixty million rupees | Register on reasonable grounds of a likely breach in the next taxable period or next 12 months. Commercial importers and exporters of goods must register regardless of turnover. | VAT Act, s 10 |
| Financial services VAT on value addition | 18% for periods from 1 January 2022 to 30 June 2026; 20.5% from 1 July 2026 | Section 25C(3)(g), (h) | https://www.ird.gov.lk/en/publications/Value%20Added%20Tax_Acts/VAT_Act_No_14-2026_E.PDF |
| Non-resident digital services: registration | Over sixty million rupees in the 12 months then ending, or actual or likely value over fifteen million rupees for a quarter | Applies from 1 July 2026 and includes currency equivalents. Apply electronically within three months from liability or specification of the form, whichever is later. | Act No. 14 of 2026, s 8 (s 25L) |
| Non-resident digital services charge | 18% on taxable supplies under section 2(1)(c) from 1 July 2026 | Exclude supplies to VAT-registered recipients under section 25N. Check First Schedule Part III(e) for qualifying education, healthcare and services to specified organisations or diplomatic missions. | Act No. 14 of 2026, ss 2, 8 and 17 |
| Simplified statement penalty, non-resident supplying registered persons | Up to fifty thousand rupees | Section 25N(4) | same |
| Return due | Last day of the month after the taxable period | Electronic; section 21(1)(a)(iii) | https://www.ird.gov.lk/en/publications/Value%20Added%20Tax_Acts/VAT_Act_No_14%5BE%5D_2002_%28Consolidation_2025%29.pdf |
| Payment due | 20th day of the month after the taxable period | Quarterly filers pay month 1 by the 20th of month 2, month 2 by the 20th of month 3; section 26(1) | same |

### Steps

1. Test past and expected taxable supplies in Sri Lanka for the period and 12 months. Apply the commercial goods importer and exporter rule separately. Section 10 normally allows 15 days to apply after registration liability arises.
2. Classify each sale: 18% standard, 0% zero-rated (section 7), or exempt (First Schedule).
3. For a VAT-inclusive receipt, output tax is the gross times 9/59.
4. Claim input tax attributable to taxable supplies, apportioning mixed purchases. Check the valid tax invoice or Customs evidence and the section 22 limits. File the relevant return within 12 months of the local invoice or 24 months of the Customs declaration. Use the applicable tax invoice specification from 1 October 2026.
5. Apply 18% to taxable imported goods on the section 6 value and check exemptions and deferments. VAT is collected at import under section 2.
6. From 1 July 2026, a non-resident digital supplier excludes a VAT-registered recipient under section 25N. If a registered provider charged the tax anyway, it refunds it. If remittance to the Commissioner-General prevents a refund, the recipient may claim the separately invoiced tax to the extent allowed under section 22. Charge an unregistered recipient on taxable supplies after checking the First Schedule exemptions.
7. File by the last day of the month after the period. Pay monthly by the 20th of the following month. For quarterly filers, pay the first two months by the 20th of the next month and the quarter balance by the 20th of the month after the quarter.

### Conservative defaults

| Ambiguity | Default |
| --- | --- |
| Unknown rate on a sale | Obtain the supply facts before filing. |
| Unknown VAT status of a purchase | Not deductible |
| Unknown counterparty location | Verify the place of supply and any export conditions. |
| Unknown business-use proportion | 0% recovery |

## Boundary and exception table

### Sri Lanka-specific refusal catalogue

- **R-LK-1, BOI enterprise:** client under a Board of Investment agreement with tax holidays. "BOI enterprises have bespoke tax exemptions. Please escalate."
- **R-LK-2, SSCL interaction:** SSCL is a separate levy on turnover that excludes VAT; see `sri-lanka-sscl` (in force on 14 November 2026).
- **R-LK-3, legacy SVAT:** the scheme ended on 1 October 2025. Use the ordinary regime for current filings. Refer legacy disputes and specialist Risk-Based Refund Scheme claims.

### Supplier pattern library

These defaults classify bank lines; confirm each against the First Schedule exemptions before filing.

| Pattern | Treatment | Notes |
| --- | --- | --- |
| Bank or payment provider charge | Check the service and invoice | Exclude ordinary exempt account charges and segregate VAT on financial services. Check any separately invoiced taxable service. |
| INTEREST, LOAN, REPAYMENT | Exclude ordinary loan principal and check interest or fees by service | Specified financial-services suppliers use Chapter IIIA where applicable. |
| IRD, INLAND REVENUE | Exclude | Tax payment |
| CUSTOMS, SRI LANKA CUSTOMS | Exclude duty; keep import VAT as input tax with the customs document | Duty is not VAT |
| EPF, ETF | Exclude | Employee funds |
| COMPANY REGISTRAR | Exclude | Registration fee |
| Electricity, including distribution | Exempt | First Schedule Part III(b)(iii). Check separately supplied services. |
| Water bill | Check the charge and tax invoice | Distinguish the supply from deposits and other charges. |
| SLT, SRI LANKA TELECOM, DIALOG, MOBITEL, HUTCH, AIRTEL LK | Domestic 18% with a tax invoice | Telecoms |
| Digital platform invoice | From 1 July 2026 check supplier and recipient status, the actual service and any First Schedule exemption. | In a covered supply to a VAT-registered recipient apply section 25N. For earlier periods check the applicable law and invoice. |
| SALARY, WAGES; OWN TRANSFER, INTERNAL; DIVIDEND | Exclude | Outside VAT |
| CASH WITHDRAWAL | Ask; default exclude | |

### Tier 2 catalogue

| Item | Default |
| --- | --- |
| Vehicle costs | Apply section 22(6)(i). Check exceptions, including qualifying goods transport, hiring cars, stock-in-trade and specified employee transport. |
| Entertainment | Check attribution to taxable activity and supporting invoice. Exclude private and non-attributable costs. |
| Digital services before 1 July 2026 | Check the provider's invoice and registration |
| BOI status | Flag; ask "BOI agreement in force?" |
| Cash withdrawals | Exclude |

### Worked classification lines (from the earlier version)

| Date | Counterparty | Gross | Net | VAT | Code | Field |
| --- | --- | --- | --- | --- | --- | --- |
| 05.04.2026 | COLOMBO TRADING PVT, invoice LK-041 | +1,180,000 | +1,000,000 | 180,000 | 18% | Output |
| 15.04.2026 | UK BUYER LTD, tea exported by supplier, payment qualifies under section 7 | +5,000,000 | +5,000,000 | 0 | 0% | Zero-rated |
| 18.07.2026 | AWS, cloud hosting, registered recipient | -60,000 | -60,000 | 0 | none | Not charged (section 25N) |
| 30.04.2026 | BOC, exempt monthly account charge | -1,000 | n/a | n/a | n/a | Excluded |

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

A business on quarterly periods has taxable supplies of Rs. 4,000,000 a month. Its quarter is Rs. 12,000,000 and its 12-month total is Rs. 48,000,000. A new contract that is expected to run throughout the next 12 months adds Rs. 1,500,000 a month. The projected quarter is Rs. 16,500,000 and the projected 12 months are Rs. 66,000,000. The reasonable-grounds test is met on either projection, so apply when the obligation arises.

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

- Refer bespoke BOI terms, legacy SVAT disputes, the Risk-Based Refund Scheme and the Tourist VAT Refund Scheme.
- Specified institutions computing VAT on financial services value addition (section 25C): escalate; the rate rises to 20.5% from 1 July 2026.
- Non-resident digital service providers registering under Chapter IIIC: escalate the registration and simplified statement.
- Transitional periods around 1 January 2024 (15% to 18%) and 1 July 2026: verify the period dates.

## Filing and payment

| Step | Detail |
| --- | --- |
| Return | Electronically through the IRD system by the last day of the month after the taxable period; an acknowledgement is issued (section 21) |
| Schedules | In the form the Commissioner-General specifies by Gazette Order |
| Payment | By the 20th of the next month, including the first two instalments and final balance for a quarterly period under section 26. |
| Working paper | Per vat-workflow-base Section 3, with Sri Lanka fields: Output 18%, Zero-rated, Exempt, Input domestic, Input imports, Net VAT |
| Bank statements | Use the available CSV or PDF and reconcile internal transfers. Keep the supporting exchange-rate record for foreign currency transactions. Use the Customs valuation and its applicable exchange rate for import VAT. |
| Onboarding questions | TIN; filing period; industry; exports; BOI status; credit brought forward (always ask) |

## Completion checklist

- [ ] Registration tested on the period and on 12 months
- [ ] Each sale classified 18%, 0% or exempt
- [ ] Input tax only with valid tax invoices, apportioned
- [ ] Digital services from 1 July 2026 checked under Chapter IIIC and First Schedule Part III(e)
- [ ] Return by the last day of the following month, payment by the 20th

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| Read for sections 2(1) (rates and the section 2(1)(c) digital services charge), 10 (registration), 21 (returns), 26 (payment) and the taxable period definition in section 83 of the IRD consolidated VAT Act | https://www.ird.gov.lk/en/publications/Value%20Added%20Tax_Acts/VAT_Act_No_14%5BE%5D_2002_%28Consolidation_2025%29.pdf | 2026-11-14 |
| Read for sections 2 (digital services date moved to 1 July 2026), 4, 5, 7 (section 25C 20.5% rate) and 8 (new Chapter IIIC, sections 25L to 25P) of the VAT (Amendment) Act No. 14 of 2026 | https://www.ird.gov.lk/en/publications/Value%20Added%20Tax_Acts/VAT_Act_No_14-2026_E.PDF | 2026-11-14 |
| Read for the VAT section (registration test, standard and zero rates, financial services rows) of the IRD tax chart, the latest on the site | https://www.ird.gov.lk/en/publications/SitePages/tax_chart_2526.aspx | 2026-11-14 |
| Read for the list of VAT amending Acts on the IRD VAT page | https://www.ird.gov.lk/en/Type%20of%20Taxes/SitePages/Value%20Added%20Tax%20%28VAT%29.aspx?menuid=1204 | 2026-11-14 |
| Gazette 2481/22, tax invoice specification | https://www.ird.gov.lk/en/publications/Gazette_Documents/2026_2481-22_E.pdf | 2026-11-24 |
| Gazette 2500/106, 1 October 2026 tax invoice start date | https://www.ird.gov.lk/en/publications/Gazette_Documents/2026_2500_106_E.pdf | 2026-11-24 |
| Gazette 2456/02, replacement of SVAT and Risk-Based Refund Scheme | https://www.ird.gov.lk/en/publications/Gazette_Documents/2025_2456-02_E.pdf | 2026-11-24 |
| IRD November notice, due dates and input credit filing limits | https://www.ird.gov.lk/en/Lists/Latest%20News%20%20Notices/Attachments/826/VAT_03112026_26410_E.pdf | 2026-11-24 |
| Sri Lanka Customs exchange rates for customs valuation | https://www.customs.gov.lk/exchange-rates/ | 2026-11-24 |

Not yet confirmed: whether a particular water, bank, telecom or platform fee qualifies on the actual invoice, and whether an imported service outside the electronic-platform regime is taxable under the facts and place-of-supply rules.
