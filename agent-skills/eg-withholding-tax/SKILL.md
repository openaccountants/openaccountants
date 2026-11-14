---
name: eg-withholding-tax
description: "Use this skill whenever asked about Egyptian withholding tax for tax year 2026, both on payments abroad to non-residents (interest, royalties, services, athletes and artists, dividends) and on payments to Egyptian residents under the deduction at source system of Law 91 art. 59 (commissions, brokerage, purchases, supplies, contracting, services) with quarterly form 41, plus the advance payment alternative. Trigger on phrases like \"Egypt WHT\", \"Egypt withholding tax\", \"ضريبة الخصم تحت حساب الضريبة\", \"الخصم والتحصيل\", \"نموذج 41\", \"نموذج 11 مستقطعة\", \"dividends to non-resident Egypt\", \"royalty WHT Egypt\", \"technical services fee Egypt\", \"dividend tax Egypt\", or any payment by an Egyptian payer that may need tax withheld. ALWAYS read this skill before touching any Egypt withholding work."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/eg-withholding-tax"
  jurisdiction: "EG"
  tax_year: "2026"
  last_updated: "2026-11-14"
---

# EG Withholding Tax v0.3

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

This skill covers tax withheld by Egyptian payers for tax year 2026: the tax deducted at source on payments to non-residents (الضريبة المستقطعة من المنبع, Law 91 Book Four), dividend tax, and the deduction on account of tax on payments to residents (الخصم تحت حساب الضريبة, Law 91 Book Five) with its advance payment alternative. Reply in the user's language, English or Arabic. All amounts are in EGP. Law 151 of 2026 took effect on 29 July 2026 and replaced the dividend article and the art. 56 loan exemption; rows say which period applies.

## Who this applies to

- **Payers abroad** (Law 91 art. 56): sole proprietors, legal persons resident in Egypt, and non-resident bodies with a PE in Egypt, paying amounts to non-residents.
- **Dividend tax** (art. 56 bis as replaced by Law 151/2026): capital companies and partnerships (civil companies count as partnerships), including companies in special economic zones, distributing to non-resident individuals and to resident or non-resident legal persons. Resident individuals pay dividend tax under art. 46 bis (`eg-income-tax`).
- **Payers at home** (art. 59, first para. as replaced by Law 53/2014; the list of payers is the 2005 text): ministries, local units, public bodies, public sector and public business companies, capital companies, investment-law companies, partnerships with capital over EGP 50,000, special-law companies, free zone companies and projects, branches of foreign companies, pharmacies and import offices, cooperatives, press, schools, unions, clubs, federations, hospitals, hotels, NGOs, professional offices, foreign representative offices, cinema and theatre businesses, private insurance funds, and any other body named by ministerial decision.
- **Not withheld from:** a private sector taxpayer with regular records whom the ETA has accepted into the advance payment system (art. 60); a project in the Law 6/2025 turnover regime, which neither suffers nor applies withholding (`eg-sme-tax`).
- **Not here:** salary tax and the 10% on a non-original employer's payments (art. 72 bis): `eg-payroll`; the company's own tax: `eg-corporate-tax`; treaty residence and PE questions: `eg-cross-border`.

## Rates, bands and thresholds

| Item | Rate or amount | Conditions | Tax year | Official URL |
|---|---|---|---|---|
| Interest paid to a non-resident | 20% of the gross, no costs | Law 91 art. 56 item 1 | 2026 | https://eta.gov.eg/sites/default/files/2024-03/law_no.91-2005.pdf |
| Royalties paid to a non-resident | 20% | Art. 56 item 2; not on amounts paid abroad for designs or know-how serving industry, in the cases the minister sets with the industry minister | 2026 | same |
| Services paid to a non-resident | 20% | Art. 56 item 3; not on a PE's share of head office administrative and supervision costs (cap 7% of PE profit, Executive Regulations art. 74) | 2026 | same |
| Athletes and artists, non-resident | 20% | Art. 56 item 4, whether paid directly or through any body | 2026 | same |
| Interest exempt: government borrowing | 0% | Loans and credit facilities obtained by the government, local units and other public legal persons from outside Egypt (art. 56 third para. as replaced by Law 30/2023) | 2026 | https://eta.gov.eg/sites/default/files/2024-03/law_no.30-2023.pdf |
| Interest exempt: infrastructure loans | 0% | Loans of at least five years from unrelated persons funding national infrastructure projects named by Prime Minister decision; the company's share at least 25% of its investments; ends when the term of the loans for carrying out the project's main works ends (art. 56 fourth para., Law 151/2026, as corrected by the Gazette erratum of 8 Aug 2026) | From 29 Jul 2026 | https://eta.gov.eg/sites/default/files/2026-08/law.no_.151.of_.2026.pdf |
| Dividends to non-resident individuals and to resident or non-resident legal persons | 10%; 5% if the securities are listed on the Egyptian Exchange | Art. 56 bis as replaced by Law 151/2026; no costs; not on bonus shares | 2026 | same |
| PE profits of a non-resident company | 10% as dividends, deemed distributed 60 days after the PE's year end | Art. 56 bis | 2026 | same |
| Dividend tax remittance | Within five working days from the start of the month after collection, to the ETA central department for deduction and collection, on the set form | Art. 56 bis | 2026 | same |
| Non-resident's gain on unlisted Egyptian shares or company interests | Seller computes and pays within 60 days of the transaction | Art. 46 bis 3 as replaced by Law 151/2026; non-resident gains on treasury bills are outside the tax | From 29 Jul 2026 | same |
| Commission or brokerage to an individual not linked to the profession | 20%, remitted within 15 days of the following month | Art. 57; form 14 (Executive Regulations art. 79) | 2026 | https://eta.gov.eg/sites/default/files/2024-03/law_no.91-2005.pdf |
| Treasury bill interest | 20%, no costs; payer remits the day after deduction | Art. 58 second para. as replaced by Law 30/2023 | 2026 | https://eta.gov.eg/sites/default/files/2024-03/law_no.30-2023.pdf |
| Remittance, art. 56 | Within the first 15 days of the month after deduction | Art. 56 last para.; form 11 مستقطعة (Executive Regulations art. 76) | 2026 | https://eta.gov.eg/sites/default/files/2024-03/law_no.91-2005.pdf |
| Deduction on account, payments to residents | A percentage set by the Minister of Finance, not over 5%, of each payment over EGP 300 for commission, brokerage, purchases, supplies, contracting or services to a private sector person; and of dividends of capital companies whatever the amount | Art. 59 first para. as replaced by Law 53/2014; insurance premiums excepted. The ministerial rate table was not read (see "Not yet confirmed") | 2026 | https://eta.gov.eg/sites/default/files/2024-03/law_no.53-2014.pdf |
| Art. 59 remittance | Quarterly on form 41 خصم وتحصيل, by the end of April, July, October and January | Art. 86 as replaced by Law 53/2014; Executive Regulations art. 82 | 2026 | same |
| Failure to withhold or remit | Fine of 25% of the amounts not paid; payer also owes the amounts and the delay charge | Art. 135 as replaced by Law 53/2014 (the 25% paragraph); art. 59 last para. | 2026 | same |
| Settlement of that offence | 12.5% of amounts not withheld, or withheld and not remitted, plus the amounts and the delay charge | Law 206/2020 art. 75 bis 1, added by Law 7/2025 | 2026 | https://eta.gov.eg/sites/default/files/2025-02/law_no.7.of_.2025.pdf |
| Delay charge | 22.50% a year in 2026 (Central Bank rate 20.50% on 1 Jan 2026 plus 2%) | Law 91 art. 110; part months and pounds dropped | 2026 | https://eta.gov.eg/sites/default/files/2026-03/Dawry.no_.1.of_.2026.pdf |
| Delay charge ceiling | 100% of the principal | Law 206/2020 art. 45 bis (Law 7/2025) | 2026 | https://eta.gov.eg/sites/default/files/2025-02/law_no.7.of_.2025.pdf |
| Advance payment alternative | 60% of the last declared tax in three equal instalments; once accepted, no art. 59 deduction | Arts. 60 to 63; ETA Services Guide 8/1 | 2026 | https://eta.gov.eg/sites/default/files/2024-03/law_no.91-2005.pdf |

## The base

**Non-residents (art. 56).**
1. Is the payee non-resident, and is the amount interest, a royalty, a service fee or an athlete's or artist's fee? Egyptian-source rules are in art. 3 (rents, licence fees and royalties borne by a resident or an Egyptian PE are Egyptian source, art. 3(ي) as replaced by Law 30/2023).
2. Apply 20% to the gross amount, no costs. If the contract makes the payer bear the tax, gross up: gross = net / 0.8.
3. Check the exemptions in the table (government loans; infrastructure loans from 29 Jul 2026). Law 30/2023 art. 6 keeps the old exemption for loans and credit facilities of public sector, public business sector and private sector companies where interest on them was paid before Law 30/2023 took effect (16 Jun 2023) (the old art. 56 required loans of at least three years, Executive Regulations art. 75).
4. Remit by the 15th of the next month on form 11; a non-resident dealing with a free zone project remits on form 12 (Executive Regulations art. 77).

**Dividends (art. 56 bis).** 10% (5% listed) on the distribution, no costs, withheld by the body executing the transaction and remitted within five working days of the next month. Resident companies exclude dividends received from other resident companies from their profits base, and the law also excludes from the dividend tax base "the distributions a company resident in Egypt received from distributions made by another resident company" (Law 151/2026). How far that second exclusion reaches is not settled (see "Not yet confirmed").

**Residents (art. 59).**
1. Is the payer one of the bodies listed in art. 59, and the payee a private sector person not in the advance payment system or the Law 6/2025 regime?
2. Is the single payment over EGP 300 and for commission, brokerage, purchases, supplies, contracting or services (or a dividend of a capital company)?
3. Deduct at the ministerial rate for the activity, keep the records of every transaction and person dealt with and the amount collected (art. 86), and remit quarterly on form 41. The form records registration number, national ID, name, address, tax office, date, nature, gross value, deduction type, net value, rate and tax withheld.
4. The payee credits the amount against its annual tax (`eg-corporate-tax`, `eg-income-tax`).
5. During an exemption period of the payee, no deduction or collection applies, except the reporting duties of arts. 59 to 59 bis 2 (art. 73 as replaced by Law 53/2014).
6. **Reporting duties, not a deduction** (arts. 59 bis to 59 bis 2 as replaced by Law 53/2014): art. 59 item 1 bodies that sell or distribute goods, industrial products or farm crops to private sector persons for trading or manufacturing, and art. 59 items 1 and 2 bodies that let premises they own for trading, manufacturing, services or food and drink, must send the ETA statements of the transactions and amounts or rents collected, by the end of April, July, October and January for the previous three months. The goods, activities and rents covered are set by ministerial decree.

**Advance payments instead of deduction (arts. 60 to 63).** Apply on the form (1 دفعات مقدمة) at least 60 days before the tax period; ETA answers within 60 days and silence is refusal (art. 62; Executive Regulations arts. 83, 84). Acceptance works as a certificate to all payers for that period (art. 84). Pay 60% of the last declared tax, or of an estimate where there is no prior return or the prior period was a loss (art. 61), in three equal instalments by 30 June, 30 September and 31 December (art. 63); the third can be cut or skipped if profit will fall. Instalments earn a yield at the Central Bank rate. ETA moves the taxpayer back to deduction after two consecutive loss periods, a change of legal form, or a difference over 20% between declared and estimated profit (ETA Services Guide 8/1).

## Deadlines and filing

| Payment type | Form | Deadline | Source |
|---|---|---|---|
| Interest, royalties, services, athletes to non-residents | Form 11 مستقطعة | First 15 days of the following month | Law 91 art. 56; Executive Regulations art. 76 |
| Dividends and deemed PE distributions | ETA form for dividend tax | Five working days from the start of the following month | Art. 56 bis |
| Commission to unconnected individuals | Form 14 مستقطعة | First 15 days of the following month | Art. 57; Executive Regulations art. 79 |
| Treasury bill interest | ETA form | Day after deduction | Art. 58 |
| Art. 59 deductions from residents | Form 41 خصم وتحصيل | End of April, July, October, January for the previous quarter | Art. 86; Executive Regulations art. 82 |
| Salaries | Payroll forms | `eg-payroll` | Law 206/2020 art. 31(b) |

**Steps:**
1. Download the current form templates from the ETA withholding forms page (https://www.eta.gov.eg/ar/content/nmadhj-aqrarat-alkhsm-walthsyl: forms 11 (V3), 14, 41, 42 to 44, 43, 45, 46, 47).
2. Fill one line per transaction, then upload and pay through the ETA tax system (https://workspace.eta.gov.eg/workspace/dashboard for merged offices) or the channels in Executive Regulations art. 82 (bank transfer, smart card, approved banks or post).
3. Keep the receipt and give the payee its details so it can credit the tax.

**Treaty relief.** The ETA Services Guide (service 5/1) describes treaty relief on interest, royalties, services and dividends as a refund to the non-resident of the excess over the treaty rate: simplified registration, form 1 ضريبة مستقطعة من المنبع, an original certified residence certificate for each year, a beneficial owner certificate stating the income is not linked to an Egyptian PE, the contracts in Arabic, forms 11 and payment receipts. ETA decides within 45 days of a complete file, otherwise it owes a delay charge at the Central Bank rate plus 2%. Treaty rates themselves are not in this pack: read the treaty on ETA's list (see `eg-cross-border`).

## Penalties and interest

| Failure | Consequence | Source |
|---|---|---|
| Not withholding, collecting or remitting on time | Fine 25% of the amounts not paid, plus the amounts and the delay charge; settlement at 12.5% instead | Law 91 arts. 59, 135 (Law 53/2014); Law 206/2020 art. 75 bis 1 (Law 7/2025) |
| Late payment of tax withheld | Delay charge 22.50% a year in 2026, whole months, capped at 100% of the principal | Law 91 art. 110; ETA circular 1/2026; Law 206/2020 art. 45 bis |
| Late or missing returns and forms | Fines under Law 206/2020 arts. 69 and 70 (EGP 3,000 to 50,000; EGP 5,000 to 200,000 over 60 days) | Law 206/2020; `eg-corporate-tax` |
| Managers | The partner, manager or board member in charge is liable for evasion within their knowledge | Law 206/2020 art. 73 |

## Cross-border points

- The 20% art. 56 rate and the 10% or 5% dividend rate are the domestic rates. Residence certificates, beneficial ownership, PE status and the ETA treaty list are covered in `eg-cross-border`; treaty rates are not in this pack, so read the treaty itself; relief runs through the ETA refund procedure above.
- A non-resident company's Egyptian PE pays 22.5% on its profit (`eg-corporate-tax`) and 10% on the deemed distribution 60 days after its year end; there is no separate branch remittance tax beyond that.
- A non-resident selling unlisted Egyptian shares pays its own tax within 60 days; the Egyptian buyer does not withhold under art. 46 bis 3.
- VAT on imported services is separate: `egypt-vat`.

## Two worked examples that recompute

**Case 1. Royalty and dividend to a foreign parent, no treaty claim.** An Egyptian unlisted company pays a royalty of EGP 1,000,000 and a dividend of EGP 5,000,000 to its non-resident parent in March 2026. Royalty: 20% = 200,000, remitted on form 11 by 15 April. Dividend: 10% = 500,000, remitted within five working days of April. The parent receives 800,000 and 4,500,000. If the shares were listed, the dividend tax would be 250,000.

```oa-check
name: Royalty and dividend to non-resident parent 2026
inputs:
  royalty: 1000000
  dividend: 5000000
steps:
  - royalty_tax: royalty * 0.20
  - dividend_tax: dividend * 0.10
  - net_paid: royalty + dividend - royalty_tax - dividend_tax
  - dividend_tax_listed: dividend * 0.05
expected:
  royalty_tax: 200000.00
  dividend_tax: 500000.00
  net_paid: 5300000.00
  dividend_tax_listed: 250000.00
```

**Case 2. Decision: settle a missed remittance or wait for the fine.** A company withheld 200,000 on a service fee to a non-resident in January 2026 and has not remitted it five whole months later. Delay charge at 22.50%: 200,000 x 22.5% x 5/12 = 18,750. Settling under Law 206 art. 75 bis 1 costs 12.5% = 25,000 on top, total 243,750. Left to the art. 135 fine of 25% (50,000), the total is 268,750, and prosecution stays open. Settling saves 25,000.

```oa-check
name: Missed remittance, settlement against fine
inputs:
  withheld: 200000
  months: 5
steps:
  - delay: withheld * 0.225 * months / 12
  - settle_total: withheld + delay + withheld * 0.125
  - fine_total: withheld + delay + withheld * 0.25
  - saving: fine_total - settle_total
expected:
  delay: 18750.00
  settle_total: 243750.00
  fine_total: 268750.00
  saving: 25000.00
```

## Ask the client first

1. Who is paid: resident or non-resident, individual or company, and does the payee have an Egyptian PE?
2. What is paid: interest, royalty, service, dividend, commission, goods, contracting? Gross amount and payment date?
3. For dividends: listed or unlisted shares, and is the shareholder a resident company?
4. Is the payee in the advance payment system or the Law 6/2025 regime?
5. Does a treaty apply, and does the payee hold a residence certificate and beneficial owner certificate?
6. Does the contract make the payer bear the tax (gross-up)?

Do not help disguise payments to avoid withholding. Do not present output as a filed form or a professional sign-off.

## Sources

| Source | URL | Read on |
|---|---|---|
| Income Tax Law 91 of 2005, original Gazette text: arts. 47 to 63 (page images read) | https://eta.gov.eg/sites/default/files/2024-03/law_no.91-2005.pdf | 2026-11-02 |
| Executive Regulations, MoF decree 991 of 2005: arts. 74 to 84 (page images read) | https://eta.gov.eg/sites/default/files/2024-03/law_no.991-2005.pdf | 2026-11-02 |
| Law 53 of 2014, art. 1: arts. 59 first para., 59 bis to 59 bis 2, 72, 73, 86, 135, 138 (page images read) | https://eta.gov.eg/sites/default/files/2024-03/law_no.53-2014.pdf | 2026-11-02 |
| Law 30 of 2023, whole text: arts. 3, 56, 56 bis, 58, 72 bis and transitional art. 6 (text layer read) | https://eta.gov.eg/sites/default/files/2024-03/law_no.30-2023.pdf | 2026-11-02 |
| Law 151 of 2026, whole text; Gazette 30 bis (a), 28 Jul 2026 (text layer read) | https://eta.gov.eg/sites/default/files/2026-08/law.no_.151.of_.2026.pdf | 2026-11-02 |
| Law 7 of 2025, whole text: arts. 45 bis, 75 bis, 75 bis 1 of Law 206 | https://eta.gov.eg/sites/default/files/2025-02/law_no.7.of_.2025.pdf | 2026-11-02 |
| Unified Tax Procedures Law 206 of 2020: arts. 29 to 33, 53, 69 to 75 (page images read) | https://eta.gov.eg/sites/default/files/2024-03/law_no.206-2020.pdf | 2026-11-02 |
| ETA circular 1 of 2026 (Central Bank rates; page image read) | https://eta.gov.eg/sites/default/files/2026-03/Dawry.no_.1.of_.2026.pdf | 2026-11-02 |
| ETA Services Guide, 2nd edition: services 5/1 (treaty refund), 8/1 (advance payments), settlement of withholding offences (text layer read) | https://eta.gov.eg/sites/default/files/2025-08/guide.of_.the_.egyptian.tax_.authority.services.second%20edition.pdf | 2026-11-02 |
| ETA withholding forms page and form 41 template (column headings read) | https://www.eta.gov.eg/ar/content/nmadhj-aqrarat-alkhsm-walthsyl | 2026-11-02 |
| Gazette erratum to Laws 149, 150 and 151 of 2026, Gazette 32 bis, 8 Aug 2026 (read for the correction to arts. 52 and 56 on infrastructure loans; via the independent review) | https://eta.gov.eg/sites/default/files/2026-08/law.no_.149.150.151.of_.2026.retractation.pdf | 2026-11-02 |

Not yet confirmed: the art. 59 rate table (MoF decree 537 of 2005 as amended by decrees 301 of 2013 and 380 of 2018, and any later decree); secondary sources give 1% on supplies and contracting, 3% on services and 5% on commissions, but no ETA or Gazette copy was found, so do not apply those figures without the decree. Whether the EGP 300 floor in art. 59 has since been changed. The ministerial decree listing the goods, activities and rents covered by the arts. 59 bis to 59 bis 2 reporting duties (MoF decree 310 of 2013 per secondary sources) was not found; the law text sets reporting, not a collection rate. The reach of the art. 56 bis exclusion of dividends a resident company received from another resident company (whether it frees all resident company to resident company dividends from the 10% or only the part of a distribution funded by such dividends). Whether ETA accepts treaty rates at source with a residence certificate instead of the refund route; refund time limits. Whether rents paid to non-residents fall under art. 56 (the old skill said 20%; art. 56 lists only interest, royalties, services and athletes or artists). The rate at which a non-resident pays on unlisted share gains, and whether non-resident gains on listed shares are covered by the art. 50 item 7 or art. 31 item 7 exemption. The old skill's software classification rule, record retention period, timing at the earlier of payment, credit or invoice, and annual reconciliation with the corporate return had no official source. Treaty rates by country (the old skill's table): not re-read from the treaties, so dropped; no skill in the pack states them yet.

> Originally contributed by Ahmed Hassan; rebuilt against the law by the OpenAccountants team.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-14. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `eg-withholding-tax` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/eg-withholding-tax. If neither is available, confirm every figure against the official source pages cited above before relying on it.
