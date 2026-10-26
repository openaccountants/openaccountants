---
name: germany-vat-return
description: "German VAT for tax year 2026, centred on the monthly or quarterly advance return (Umsatzsteuer-Voranmeldung, form USt 1 A) under standard taxation. Covers the 19% and 7% rates, including the 7% rate on restaurant and catering services (drinks excluded) from 1 January 2026; the small business limits of § 19 UStG (EUR 25,000 and EUR 100,000); monthly or quarterly filing (EUR 9,000 and EUR 2,000), the 10th-day deadline, the one-month extension and the 1/11 special prepayment; the annual return deadline; reverse charge under § 13b; the recapitulative statement; e-invoices (receiving since 2025, issuing by 2027 or 2028); late filing and late payment surcharges and interest; and the 2026 box numbers. Trigger on: Umsatzsteuer-Voranmeldung, UStVA, Vorsteuer, Kennzahl, Dauerfristverlängerung, Zusammenfassende Meldung, E-Rechnung, Säumniszuschlag, German VAT return. Out of scope: the annual return in detail, § 19, § 20 cash basis, partial exemption and OSS (de-vat-annual-and-special-schemes), e-"
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/germany-vat-return"
  jurisdiction: "DE"
  tax_year: "2026"
  last_updated: "2026-10-24"
  trust_label: "Built by Michael Cutajar and the OpenAccountants team"
  review_status: "pending_review"
---

# Germany: VAT and the advance VAT return, tax year 2026

> **General reference only.** This skill is tax reference material for AI-assisted work. It has not been reviewed for any specific business's facts. Do not rely on it to file, pay or take a position without a qualified professional checking it.

This skill explains German VAT (Umsatzsteuer) for 2026 and how to fill in the advance return (Umsatzsteuer-Voranmeldung, form USt 1 A) for a business on standard taxation. It links to sibling skills rather than repeating them:

- [de-vat-annual-and-special-schemes](de-vat-annual-and-special-schemes.md): the annual return (form USt 2 A) and how it reconciles to the advance returns, the small business scheme in depth, cash accounting under § 20 UStG, partial exemption, § 15a corrections, the one-stop shop, fines.
- [germany-einvoice](germany-einvoice.md): XRechnung, ZUGFeRD, Peppol and archiving.
- [de-income-tax](de-income-tax.md) and [de-einkommensteuer-freelancer](de-einkommensteuer-freelancer.md): income tax.
- `vat-workflow-base` (the workflow for preparing any VAT return) and `eu-vat-directive` (EU rules), when working a bank statement into a return.

## Who this applies to

- **Every business (Unternehmer) making taxable supplies in Germany** charges VAT and files advance returns, unless it is a small business under § 19 UStG or the tax office has released it (see "Deadlines and filing"). A business is anyone who carries on a commercial or professional activity independently: sole traders, freelancers, partnerships, GmbHs.
- **Small businesses (Kleinunternehmer).** A business based in Germany is exempt if its total turnover was not more than EUR 25,000 in the previous calendar year and does not exceed EUR 100,000 in the current year (§ 19(1) UStG). It charges no VAT, claims no input VAT, and the filing duties of § 18(1) to (4) UStG do not apply to it. It can waive the scheme; the waiver binds it for at least five calendar years (§ 19(3) UStG). The start-up year, the receipt that crosses the limit and the EU-wide scheme are in de-vat-annual-and-special-schemes.
- **Businesses established abroad** that make taxable supplies in Germany must register and file here unless the customer owes the tax under the reverse charge (§ 13b UStG) or the supplies go through the one-stop shop. See "Cross-border points".
- **Customers who owe the tax.** A business (wherever it is established) or a legal person that receives a reverse-charge supply owes the VAT on it (§ 13b(5) UStG) and must file even if it makes no taxable supplies of its own (§ 18(4a) UStG).
- **Out of scope here:** VAT groups (Organschaft), the margin schemes (§§ 25, 25a UStG), the flat rates for farmers and foresters (§ 24 UStG), and travel agents. Refer these.

## Rates, bands and thresholds

| Item | Rate or amount | Year | Source |
|---|---|---|---|
| Standard rate | 19% | 2026 | § 12(1) UStG, https://www.gesetze-im-internet.de/ustg_1980/__12.html |
| Reduced rate (Annex 2 goods, books, water, hotel rooms, local transport and the other § 12(2) items) | 7% | 2026 | § 12(2) UStG, https://www.gesetze-im-internet.de/ustg_1980/__12.html |
| Restaurant and catering services, except the supply of drinks | 7% from 1 January 2026 | 2026 | § 12(2) no. 15 UStG, inserted by Art. 4 no. 2 of the Steueränderungsgesetz 2025 of 22 December 2025 (BGBl. 2025 I Nr. 363), in force 1 January 2026 (Art. 12(2)), https://www.recht.bund.de/bgbl/1/2025/363/VO.html ; BMF letter of 22 December 2025, https://www.bundesfinanzministerium.de/Content/DE/Downloads/BMF_Schreiben/Steuerarten/Umsatzsteuer/Umsatzsteuer-Anwendungserlass/2025-12-22-verpflegungsdienstleistungen.pdf?__blob=publicationFile&v=5 |
| Combined food and drinks price (buffet, all-inclusive): drinks share the tax office accepts | 30% of the package price | 2026 | UStAE 10.1(12), BMF letter of 22 December 2025 (same URL) |
| Solar modules and storage for systems on or near homes | 0% | 2026 | § 12(3) UStG, https://www.gesetze-im-internet.de/ustg_1980/__12.html |
| Small business: total turnover of the previous year, not exceeded | EUR 25,000 | 2026 (2025 turnover) | § 19(1) UStG, https://www.gesetze-im-internet.de/ustg_1980/__19.html |
| Small business: total turnover of the current year, not exceeded | EUR 100,000 | 2026 | § 19(1) UStG, https://www.gesetze-im-internet.de/ustg_1980/__19.html |
| Monthly advance returns if the previous year's VAT was more than | EUR 9,000 | 2026 | § 18(2) UStG, https://www.gesetze-im-internet.de/ustg_1980/__18.html |
| Tax office may release from advance returns if the previous year's VAT was not more than | EUR 2,000 | 2026 | § 18(2) UStG, https://www.gesetze-im-internet.de/ustg_1980/__18.html |
| Monthly filing may be chosen if the previous year ended with a surplus of more than | EUR 9,000 | 2026 | § 18(2a) UStG, https://www.gesetze-im-internet.de/ustg_1980/__18.html |
| Special prepayment for monthly filers with the one-month extension | 1/11 of the previous year's advance payments | 2026 | § 47(1) UStDV, https://www.gesetze-im-internet.de/ustdv_1980/__47.html |
| Reverse charge on mobile phones, tablets, games consoles, chips and Annex 4 metals: fees in one transaction at least | EUR 5,000 | 2026 | § 13b(2) nos. 10 and 11 UStG, https://www.gesetze-im-internet.de/ustg_1980/__13b.html |
| Recapitulative statement may be quarterly while intra-EU supplies of goods stay at or below this in the current and each of the four previous quarters | EUR 50,000 | 2026 | § 18a(1) UStG, https://www.gesetze-im-internet.de/ustg_1980/__18a.html |
| Distance sales and e-services to EU consumers, EU-wide, below which German VAT applies | EUR 10,000 (previous and current year) | 2026 | § 3c(4) UStG, https://www.gesetze-im-internet.de/ustg_1980/__3c.html |
| Small-amount invoice (short details allowed) | Gross total up to EUR 250 | 2026 | § 33 UStDV, https://www.gesetze-im-internet.de/ustdv_1980/__33.html |
| E-invoice relief for supplies made in 2027: issuer's previous-year total turnover not more than | EUR 800,000 | Supplies in 2027 | § 27(38) no. 2 UStG, https://www.gesetze-im-internet.de/ustg_1980/__27.html |
| Late filing surcharge, annual return | 0.25% of the tax less prepayments per started month, at least EUR 25 per month, at most EUR 25,000 | 2026 | § 152(5) and (10) AO, https://www.gesetze-im-internet.de/ao_1977/__152.html |
| Late payment surcharge | 1% per started month of the overdue tax, rounded down to a multiple of EUR 50 | 2026 | § 240(1) AO, https://www.gesetze-im-internet.de/ao_1977/__240.html |
| Grace period before the late payment surcharge (not for cash or cheque) | 3 days | 2026 | § 240(3) AO, https://www.gesetze-im-internet.de/ao_1977/__240.html |
| Interest on an assessed difference (annual assessment) | 0.15% per full month (1.8% a year) | 2026 | § 233a AO, https://www.gesetze-im-internet.de/ao_1977/__233a.html ; § 238(1a) AO, https://www.gesetze-im-internet.de/ao_1977/__238.html |

## The taxable base

**What is taxed.** Supplies of goods and services made in Germany for consideration by a business, intra-EU acquisitions of goods, imports, and private use of business assets (§ 3(1b) and (9a) UStG). The base is everything the customer pays, without the VAT itself.

**Place of supply first, then the rate.** A service to a business is taxed where the customer is established (§ 3a(2) UStG). So a German consultant's service to a French company is not taxable in Germany, and a foreign supplier's service to a German business is taxed in Germany with the German customer owing the tax.

**Restaurant meals from 2026.** Food served in a restaurant or by a caterer is at 7% from 1 January 2026. Drinks stay at 19%. A bill must split the two. Where one price covers food and drinks (a buffet or all-inclusive deal), the tax office accepts 30% of the package price as the drinks share (UStAE 10.1(12)). For services in the night of 31 December 2025 to 1 January 2026, applying 19% is not challenged (BMF letter of 22 December 2025, no. 3).

**Input VAT (Vorsteuer).** A business deducts VAT charged by other businesses on an invoice that meets § 14 UStG, VAT on intra-EU acquisitions, import VAT that has arisen, and VAT it owes under the reverse charge (§ 15(1) UStG). No deduction for:
- costs linked to exempt supplies without input deduction, such as residential letting, insurance or financial services (§ 15(2) UStG). Mixed use needs apportionment: see de-vat-annual-and-special-schemes;
- an item used less than 10% for business (§ 15(1) sentence 2 UStG);
- costs blocked by § 15(1a) UStG: gifts above the § 4(5) no. 1 EStG limit, hunting, yachts, private living costs. Reasonable, evidenced business entertainment is NOT blocked for VAT;
- an invoice that is missing required details.

**The 2026 boxes (Kennzahlen, Kz) on form USt 1 A.** Tax bases go in whole euros; tax amounts include cents. Source: BMF letter of 29 December 2025 with the 2026 form and instructions.

| Line | Kz | What goes in it |
|---|---|---|
| 13 | 81 | Taxable supplies at 19%, net base |
| 14 | 86 | Taxable supplies at 7%, net base (including restaurant food from 2026) |
| 15 | 87 | Supplies at 0% (solar, § 12(3) UStG) |
| 19 | 41 | Tax-free intra-EU supplies of goods to a customer with a VAT ID |
| 22 | 43 | Other tax-free supplies with input deduction, such as exports |
| 23 | 48 | Tax-free supplies without input deduction (§ 4 nos. 8 to 29 UStG) and a small business's supplies |
| 25, 26 | 89, 93 | Intra-EU acquisitions at 19% and 7%, net base |
| 30 | 46 (base), 47 (tax) | Reverse charge on § 3a(2) services from a business in another EU state (§ 13b(1) UStG) |
| 31 | 73, 74 | Reverse charge on supplies under the real estate transfer tax act |
| 32 | 84 (base), 85 (tax) | Reverse charge, everything else: services and works supplies from a business established outside Germany that do not belong in line 30 (so non-EU suppliers), and the domestic categories (§ 13b(2) nos. 1, 2 and 4 to 12 UStG) |
| 34 | 60 | Your own supplies on which the customer owes the tax under § 13b(5) UStG |
| 35 | 21 | Your § 3a(2) services to businesses in other EU states (also go in the recapitulative statement) |
| 36 | 45 | Other supplies whose place of supply is not in Germany |
| 38 | 66 | Input VAT from other businesses' invoices |
| 39 | 61 | Input VAT on intra-EU acquisitions |
| 40 | 62 | Import VAT that has arisen |
| 41 | 67 | Input VAT on reverse-charge supplies |
| 44 | 64 | Input VAT correction under § 15a UStG |
| 46 | 65 | Tax from a change of taxation method, and extra tax on taxed prepayments after a rate change |
| 47 | 69 | Tax shown wrongly on an invoice (§ 14c UStG) |
| 49 | 39 | Special prepayment credit, normally only in the last return of the year |
| 50 | 83 | The amount to pay, or the surplus with a minus sign. Always filled in |

**Corrections and credit notes.** A later change to the price (a discount, a cancellation, a credit note) is corrected in the period in which the change happens, not in the original period, by entering the change in the same box with a minus sign where it reduces the base (§ 17(1) UStG). Only where the fee has become uncollectible (§ 17(2) no. 1 UStG) is the reduction also shown in Kz 50 (line 51), or for input VAT in Kz 37 (line 52) (2026 form USt 1 A).

**Common bank-statement lines.**

| Counterparty type | Treatment |
|---|---|
| Bank fees, interest, loans, insurance premiums | Exempt or outside scope: no input VAT |
| Tax office, customs duty, chambers (IHK, HWK), broadcasting levy, statutory insurance, payroll and social contributions | Not a supply: leave out. Import VAT on a customs notice goes in Kz 62 |
| German utilities, telecoms, rent of business premises with VAT shown | Input VAT in Kz 66 |
| Software or advertising billed by an EU entity (e.g. an Irish subsidiary) | Kz 46 and 47, input in Kz 67 |
| Software or services billed by a non-EU entity | Kz 84 and 85, input in Kz 67 |
| Goods bought from another EU state and shipped to Germany | Kz 89 or 93, input in Kz 61 |
| Owner's transfers, transfers between own accounts | Leave out |

## Deadlines and filing

**Advance returns.** Filed electronically through ELSTER (https://www.elster.de) by the 10th day after the end of each period; the payment is due the same day (§ 18(1) UStG). Paper only with the tax office's permission to avoid hardship. A deadline on a Saturday, Sunday or public holiday moves to the next working day (§ 108(3) AO).

**Monthly or quarterly.**
- Quarterly is the default (§ 18(2) UStG).
- Monthly if the previous year's VAT was more than EUR 9,000.
- The tax office may release a business from advance returns if the previous year's VAT was not more than EUR 2,000. The annual return is still due.
- A business with a surplus of more than EUR 9,000 in the previous year may choose monthly by filing the January return by 10 February; the choice binds for the year (§ 18(2a) UStG).
- New businesses: for tax years 2021 to 2026, a business that traded for only part of the previous year has that year's tax converted to a full-year figure, and a business starting in the current year uses its expected tax for this year (§ 18(2) last sentence UStG). The general rule of monthly filing in the first two years is set aside for these years. Shelf companies and bought dormant companies file monthly in the current and following year (§ 18(2) sentence 5 UStG).

**One-month extension (Dauerfristverlängerung).** On application the tax office must extend the filing and payment deadline by one month, unless the tax looks at risk (§ 46 UStDV). Apply on form USt 1 H through ELSTER by the date the first affected return is due (§ 48(1) UStDV). A monthly filer must pay a special prepayment (Sondervorauszahlung) of 1/11 of the previous year's advance payments, by the due date of the first advance return of the year, 10 February (§ 47(1), § 48(2) UStDV). The base is the sum of the previous year's Kz 83 amounts plus the previous year's special prepayment credited in Kz 39 (2026 form instructions, lines 8 and 9). It is credited in Kz 39 of the last return of the year (§ 48(4) UStDV). A quarterly filer pays no special prepayment.

**Annual return.** Every business on standard taxation files an annual return for the calendar year (§ 18(3) UStG). For 2026 it is due 31 July 2027 (§ 149(2) AO), which is a Saturday, so Monday 2 August 2027 (§ 108(3) AO); if a tax adviser prepares it, by 29 February 2028 (§ 149(3) no. 4 AO). Any balance is due one month after the return is filed (§ 18(4) UStG). Detail: de-vat-annual-and-special-schemes.

**Recapitulative statement (Zusammenfassende Meldung).** Sent to the Bundeszentralamt für Steuern (https://www.bzst.de) by the 25th day after each month in which intra-EU supplies of goods were made; quarterly while those supplies stay at or below EUR 50,000 in the current and each of the four previous quarters (§ 18a(1) UStG). § 3a(2) services to EU businesses are reported by the 25th day after each quarter (§ 18a(2) UStG).

**E-invoices.**
- Receiving: since 1 January 2025 every business in Germany must be able to receive an e-invoice (a structured format such as XRechnung or ZUGFeRD), small businesses included. Receiving by e-mail needs no separate inbox (UStAE 14.1(5), BMF letter of 15 October 2025).
- Issuing: an invoice for a supply to another business must be an e-invoice where both are established in Germany (§ 14(2) sentence 2 no. 1 UStG). Transition (§ 27(38) UStG): for supplies made in 2025 and 2026, paper or another electronic format (with the customer's consent) is allowed until 31 December 2026; for supplies made in 2027, only if the issuer's 2026 total turnover was not more than EUR 800,000, or by EDI. For supplies from 1 January 2028 there is no relief.
- Small-amount invoices up to EUR 250, travel tickets and small businesses' invoices may always be issued as ordinary invoices (BMF letter of 15 October 2025, no. 22).

## Penalties and interest

- **Late advance return.** The tax office may set a late filing surcharge (§ 152(1) AO). The 0.25% formula does not apply to monthly or quarterly returns or to the special prepayment; the amount is set by judgement, looking at how late, how often and how much tax (§ 152(8) AO). The cap is EUR 25,000 (§ 152(10) AO).
- **Late annual return.** 0.25% of the assessed tax less prepayments for each started month late, at least EUR 25 a month, rounded down to whole euros, at most EUR 25,000 (§ 152(5) and (10) AO). The surcharge is compulsory if the return is not filed within 14 months after the year ends (for 2026, by 29 February 2028, which is also the tax-adviser deadline), unless the deadline was extended, the tax is nil or negative, or the tax does not exceed the prepayments (§ 152(2) and (3) AO).
- **Late payment (Säumniszuschlag).** 1% for each started month on the overdue tax rounded down to a multiple of EUR 50 (§ 240(1) AO). No surcharge if the payment is no more than 3 days late, except for payment in cash or by cheque (§ 240(3) AO with § 224(2) no. 1 AO). A bank transfer counts on the day the tax office's account is credited (§ 224(2) no. 2 AO). It runs on advance payments, the special prepayment and the annual balance.
- **Interest (§ 233a AO).** Where the annual assessment differs from the prepayments, the difference carries interest of 0.15% per full month, from 15 months after the year ends (for 2026, from 1 April 2028) until the assessment takes effect (§ 233a(2) AO, § 238(1a) AO). The amount is rounded down to a multiple of EUR 50 (§ 238(2) AO). Advance payments themselves carry no § 233a interest (§ 233a(1) sentence 2 AO).
- **Fines** for VAT not paid on time (§ 26a UStG) are covered in de-vat-annual-and-special-schemes.

## Cross-border points

- **Services received from abroad.** A § 3a(2) service from an EU business: base Kz 46, tax Kz 47, input Kz 67; the tax arises at the end of the period in which the service was performed (§ 13b(1) UStG). Other services and works supplies from a business established abroad (including non-EU): Kz 84 and 85; the tax arises when the invoice is issued, at the latest at the end of the month after the supply (§ 13b(2) no. 1 UStG). A fully taxable business pays and deducts the same amount.
- **Services supplied abroad.** A § 3a(2) service to a business in another EU state is not taxable in Germany: Kz 21, the recapitulative statement, and an invoice noting that the customer owes the tax. To a business outside the EU: Kz 45.
- **Goods.** Intra-EU supplies to a customer with a valid VAT ID are tax-free with input deduction (Kz 41), with transport evidence; exports outside the EU go in Kz 43. Acquisitions from EU suppliers are self-assessed (Kz 89 or 93, input Kz 61). Import VAT is charged by customs and deducted in Kz 62.
- **Domestic reverse charge.** Construction services (where the customer itself regularly supplies construction services), building cleaning, scrap metal, gold, mobile phones, tablets, consoles, chips and Annex 4 metals at EUR 5,000 or more per transaction, and the other categories listed in § 13b(2) UStG: the business customer owes the tax (§ 13b(2) and (5) UStG). The supplier reports the sale in Kz 60.
- **Distance sales to EU consumers.** Up to EUR 10,000 a year EU-wide (goods and electronic services together, previous and current year), German VAT applies; above it, the customer's country's VAT, usually through the one-stop shop (§ 3c(4) UStG). See de-vat-annual-and-special-schemes.
- **Foreign businesses.** A business established abroad that makes taxable supplies in Germany not covered by the reverse charge registers and files like a German business. A foreign business with no German filing duty recovers German input VAT through the refund procedure (§ 18(9) UStG).

## Worked examples

### Example 1: An IT consultant's monthly return, with a late payment

Anna is a freelance IT consultant in Berlin on standard taxation. Her 2025 VAT was above EUR 9,000, so she files monthly in 2026 without an extension. For March 2026 she has:
- fees from German clients of EUR 20,000 net, at 19%: EUR 3,800 VAT, Kz 81;
- fees from a French company of EUR 5,000 for consulting: not taxable in Germany, Kz 21 and the recapitulative statement, no VAT;
- German purchase invoices showing EUR 1,140 VAT: Kz 66;
- a US software subscription of EUR 200 billed by the US entity: Kz 84 EUR 200, Kz 85 EUR 38;
- online advertising of EUR 1,000 billed by an Irish company: Kz 46 EUR 1,000, Kz 47 EUR 190.

The reverse-charge tax of EUR 228 is also her input VAT in Kz 67. Output VAT is EUR 4,028, input VAT EUR 1,368, so Kz 83 is EUR 2,660. The return and payment are due Friday 10 April 2026. Her transfer reaches the tax office on Tuesday 14 April, 4 days late, past the 3-day grace period. The surcharge is 1% of EUR 2,650 (EUR 2,660 rounded down to a multiple of 50) for one started month: EUR 26.50.

```oa-check
name: IT consultant, March 2026 advance return with reverse charge and a late payment
inputs:
  domestic_net: 20000
  eu_service_sale: 5000
  domestic_input_vat: 1140
  non_eu_software: 200
  eu_advertising: 1000
  standard_rate: 19
  months_late: 1
steps:
  - kz81_tax: pct(domestic_net, standard_rate)
  - kz85_tax: pct(non_eu_software, standard_rate)
  - kz47_tax: pct(eu_advertising, standard_rate)
  - output_vat_line37: kz81_tax + kz85_tax + kz47_tax
  - kz67_input: kz85_tax + kz47_tax
  - input_vat_total: domestic_input_vat + kz67_input
  - kz83: output_vat_line37 - input_vat_total
  - overdue_rounded: floor(kz83 / 50) * 50
  - late_payment_surcharge: pct(overdue_rounded, 1) * months_late
expected:
  kz81_tax: 3800
  kz85_tax: 38
  kz47_tax: 190
  output_vat_line37: 4028
  kz67_input: 228
  input_vat_total: 1368
  kz83: 2660
  overdue_rounded: 2650
  late_payment_surcharge: 26.50
```

### Example 2: A restaurant's December return, buffet at two rates and the special prepayment

A restaurant GmbH files monthly with the one-month extension. Its 2025 advance returns showed Kz 83 amounts of EUR 61,000 in total, and its 2025 special prepayment of EUR 5,000 was credited in December 2025. The base for 2026 is EUR 66,000, so the 2026 special prepayment is EUR 6,000, declared on form USt 1 H and paid by 10 February 2026.

In December 2026 it sells only buffet packages, food and drinks for one price, for EUR 127,330 gross. Using the 30% drinks share (UStAE 10.1(12)), EUR 38,199 is drinks at 19% (net EUR 32,100, VAT EUR 6,099, Kz 81) and EUR 89,131 is food at 7% (net EUR 83,300, VAT EUR 5,831, Kz 86). Output VAT is EUR 11,930. Input VAT on invoices is EUR 4,200 (Kz 66), leaving EUR 7,730 in line 48. December is the last period, so the EUR 6,000 special prepayment is credited in Kz 39, and Kz 83 is EUR 1,730. With the extension it is due 10 February 2027. Had the whole price been taxed at 19%, as before 2026, output VAT would have been EUR 20,330.

```oa-check
name: Restaurant, December 2026 return with a 30% drinks share and the special prepayment credit
inputs:
  kz83_2025_total: 61000
  svz_2025: 5000
  package_gross: 127330
  drinks_share_pct: 30
  input_vat: 4200
steps:
  - svz_base: kz83_2025_total + svz_2025
  - svz_2026: svz_base / 11
  - drinks_gross: pct(package_gross, drinks_share_pct)
  - food_gross: package_gross - drinks_gross
  - drinks_net_kz81: drinks_gross * 100 / 119
  - food_net_kz86: food_gross * 100 / 107
  - drinks_vat: drinks_gross - drinks_net_kz81
  - food_vat: food_gross - food_net_kz86
  - output_vat: drinks_vat + food_vat
  - line48: output_vat - input_vat
  - kz83_december: line48 - svz_2026
  - output_vat_all_at_19: package_gross * 19 / 119
expected:
  svz_base: 66000
  svz_2026: 6000
  drinks_gross: 38199
  food_gross: 89131
  drinks_net_kz81: 32100
  food_net_kz86: 83300
  drinks_vat: 6099
  food_vat: 5831
  output_vat: 11930
  line48: 7730
  kz83_december: 1730
  output_vat_all_at_19: 20330
```

## Ask the client first

1. Is the business on standard taxation, or a small business under § 19 UStG? What was total turnover in 2025, and what is it so far in 2026?
2. Monthly or quarterly, and is there a one-month extension? If monthly with the extension, was the 2026 special prepayment declared and paid, and is this the last return of the year?
3. For each foreign supplier: which legal entity issued the invoice, and where is it established? This decides Kz 46 and 47 against Kz 84 and 85.
4. For each EU customer: is there a valid VAT ID, and was it checked with the Bundeszentralamt für Steuern?
5. Any exempt income (residential rent, medical, education, insurance, financial services)? If so, input VAT needs apportioning.
6. For restaurants and caterers: do the till and invoices split food from drinks, and are there package prices?

## Sources

| Source | URL | Read on |
|---|---|---|
| UStG § 12 (rates, including § 12(2) no. 15 restaurant services) | https://www.gesetze-im-internet.de/ustg_1980/__12.html | 2026-10-24 |
| UStG § 13b (reverse charge) | https://www.gesetze-im-internet.de/ustg_1980/__13b.html | 2026-10-24 |
| UStG § 14 (invoices, e-invoice duty) | https://www.gesetze-im-internet.de/ustg_1980/__14.html | 2026-10-24 |
| UStG § 15 (input VAT) | https://www.gesetze-im-internet.de/ustg_1980/__15.html | 2026-10-24 |
| UStG § 17 (corrections to the tax base) | https://www.gesetze-im-internet.de/ustg_1980/__17.html | 2026-10-24 |
| UStG § 18 (advance returns, annual return, filing rhythm) | https://www.gesetze-im-internet.de/ustg_1980/__18.html | 2026-10-24 |
| UStG § 18a (recapitulative statement) | https://www.gesetze-im-internet.de/ustg_1980/__18a.html | 2026-10-24 |
| UStG § 19 (small businesses) | https://www.gesetze-im-internet.de/ustg_1980/__19.html | 2026-10-24 |
| UStG § 3a (place of supply of services) | https://www.gesetze-im-internet.de/ustg_1980/__3a.html | 2026-10-24 |
| UStG § 3c (distance sales) | https://www.gesetze-im-internet.de/ustg_1980/__3c.html | 2026-10-24 |
| UStG § 27(38) (e-invoice transition) | https://www.gesetze-im-internet.de/ustg_1980/__27.html | 2026-10-24 |
| UStG, consolidated text, last amended by Art. 5 of the law of 29 June 2026 | https://www.gesetze-im-internet.de/ustg_1980/BJNR119530979.html | 2026-10-24 |
| Steueränderungsgesetz 2025 of 22 December 2025, BGBl. 2025 I Nr. 363, Art. 4 no. 2 (§ 12(2) no. 15 UStG) and Art. 12(2) (in force 1 January 2026) | https://www.recht.bund.de/bgbl/1/2025/363/VO.html | 2026-10-24 |
| UStDV § 33 (small-amount invoices) | https://www.gesetze-im-internet.de/ustdv_1980/__33.html | 2026-10-24 |
| UStDV § 46 (one-month extension) | https://www.gesetze-im-internet.de/ustdv_1980/__46.html | 2026-10-24 |
| UStDV § 47 (special prepayment) | https://www.gesetze-im-internet.de/ustdv_1980/__47.html | 2026-10-24 |
| UStDV § 48 (procedure, credit in the last return) | https://www.gesetze-im-internet.de/ustdv_1980/__48.html | 2026-10-24 |
| AO § 108 (deadline on a weekend or holiday) | https://www.gesetze-im-internet.de/ao_1977/__108.html | 2026-10-24 |
| AO § 149 (filing deadlines) | https://www.gesetze-im-internet.de/ao_1977/__149.html | 2026-10-24 |
| AO § 152 (late filing surcharge) | https://www.gesetze-im-internet.de/ao_1977/__152.html | 2026-10-24 |
| AO § 224 (date of payment) | https://www.gesetze-im-internet.de/ao_1977/__224.html | 2026-10-24 |
| AO § 233a (interest period) | https://www.gesetze-im-internet.de/ao_1977/__233a.html | 2026-10-24 |
| AO § 238 (interest rate and rounding) | https://www.gesetze-im-internet.de/ao_1977/__238.html | 2026-10-24 |
| AO § 240 (late payment surcharge) | https://www.gesetze-im-internet.de/ao_1977/__240.html | 2026-10-24 |
| BMF letter of 22 December 2025, 7% on restaurant and catering services from 1 January 2026 (UStAE 10.1(12), 12.16(12)) | https://www.bundesfinanzministerium.de/Content/DE/Downloads/BMF_Schreiben/Steuerarten/Umsatzsteuer/Umsatzsteuer-Anwendungserlass/2025-12-22-verpflegungsdienstleistungen.pdf?__blob=publicationFile&v=5 | 2026-10-24 |
| BMF letter of 15 October 2025, mandatory e-invoices between domestic businesses (UStAE 14.1) | https://www.bundesfinanzministerium.de/Content/DE/Downloads/BMF_Schreiben/Steuerarten/Umsatzsteuer/Umsatzsteuer-Anwendungserlass/2025-10-15-einfuehrung-obligatorische-e-rechnung.pdf?__blob=publicationFile&v=5 | 2026-10-24 |
| BMF letter of 29 December 2025, 2026 advance return form USt 1 A, form USt 1 H and instructions | https://www.bundesfinanzministerium.de/Content/DE/Downloads/BMF_Schreiben/Steuerarten/Umsatzsteuer/2025-12-29-vordruckmuster-USt-voranmeldung-2026.pdf?__blob=publicationFile&v=2 | 2026-10-24 |
| ELSTER, the filing portal | https://www.elster.de | 2026-10-24 |
| Bundeszentralamt für Steuern (VAT IDs, recapitulative statement) | https://www.bzst.de | 2026-10-24 |

Not yet confirmed: which tax office handles a foreign business, by country (the Umsatzsteuerzuständigkeitsverordnung was not read for this version); the rounding rule for whole-euro tax bases on the advance return (the 2026 instructions say whole euros but not whether to round or cut off the cents).

> Contributed by OpenAccountants.

> Contributed by Michael Cutajar.

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

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-10-24. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `germany-vat-return` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/germany-vat-return. If neither is available, confirm every figure against the official source pages cited above before relying on it.
