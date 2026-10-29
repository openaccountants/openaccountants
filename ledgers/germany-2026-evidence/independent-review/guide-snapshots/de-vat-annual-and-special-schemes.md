---
name: de-vat-annual-and-special-schemes
description: "German VAT for tax year 2026 beyond the monthly or quarterly advance return: the annual VAT return (Umsatzsteuererklärung, form USt 2 A) and who files it, its deadline (2 August 2027, or 29 February 2028 with a tax adviser), reconciling it to the advance returns and paying the balance within one month; the small business scheme under § 19 UStG (EUR 25,000 and EUR 100,000, losing it mid-year, no annual return) and the EU small business scheme run by the BZSt; cash accounting under § 20 UStG (EUR 800,000, freelancers); the one-month extension and the 1/11 special prepayment; partial exemption (§ 15(4)) and input tax correction (§ 15a); domestic reverse charge (§ 13b); the EU one-stop shop (§ 18j, EUR 10,000); penalties; and the e-invoicing timetable. Trigger on: Umsatzsteuererklärung, Jahreserklärung, Abschlusszahlung, Kleinunternehmer, Istversteuerung, Sondervorauszahlung, Vorsteueraufteilung, § 15a, OSS. Out of scope: classifying transactions and filling the advance return (germany-vat-return), e-invoice formats (germany-einvoice), income tax (de-income-tax, de-einkommensteuer-freelancer)."
version: 0.2
jurisdiction: DE
tax_year: 2026
last_updated: 2026-10-29
authored_by: Ryan Duguid
review_status: pending_review
trust_label: Accountant-authored
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Germany: the annual VAT return and the special schemes, tax year 2026

> **General reference only.** This skill is general tax reference material for AI-assisted work. It has not been reviewed for any specific business's facts. Do not rely on it to file, pay or take a position without review by a qualified professional in Germany.

**What this skill does.** [germany-vat-return](germany-vat-return.md) classifies transactions and fills in the monthly or quarterly advance return (Umsatzsteuer-Voranmeldung, form USt 1 A) under standard taxation. This skill picks up the cases that skill refuses and the year-end: the annual VAT return for 2026, the small business scheme, cash accounting, the one-month extension, partial exemption, input tax correction, reverse charge, the one-stop shop, penalties and the e-invoicing dates.

**Sibling skills.** [germany-vat-return](germany-vat-return.md) for the box-by-box advance return and the supplier library. [germany-einvoice](germany-einvoice.md) for XRechnung, ZUGFeRD and archiving. [de-income-tax](de-income-tax.md) and [de-einkommensteuer-freelancer](de-einkommensteuer-freelancer.md) for income tax, where a small business uses gross receipts and costs, while normal-scheme cash EÜR records VAT collected as a receipt and VAT remitted as an expense. [de-corporate-tax](de-corporate-tax.md) for a GmbH's profit.

## Who this applies to

**Every business (Unternehmer) taxed in Germany files an annual VAT return** for the calendar year, electronically, in which it computes the tax or the surplus itself (§ 18(3) UStG). The tax period is the calendar year (§ 16(1) UStG), or the part of it in which the business traded (§ 16(3)). The return counts as a tax assessment subject to review (§ 168 AO), so no notice follows unless the tax office departs from it. If the return lowers the tax below the prepayments or shows a refund, that effect starts only when the tax office agrees, which needs no form; the refund is then paid without a separate claim (§ 168 sentences 2 and 3 AO; USt 2 E 2026, lines 124 to 126).

**Who does not file it.**
- **A small business using § 19 UStG.** § 19(1) sentence 2 switches off the filing duties of § 18(1) to (4) UStG, which includes the annual return. This applies from tax year 2024 (§ 27(39) UStG). Two exceptions keep a return due: the tax office asks for one (§ 149(1) sentence 2 AO), or the business owes tax as a buyer, for example under reverse charge or on an intra-Community acquisition (§ 18(4a) UStG). The 2026 form instructions say the same.
- **A foreign business whose only German supplies go through the one-stop shop.** For those supplies § 18(1) to (4) does not apply (§ 18j(4) sentence 4 UStG).

**The small business scheme (§ 19 UStG, rules in force since 1 January 2025).** A business based in Germany makes tax-free supplies if its total turnover was not above EUR 25,000 in the previous calendar year and is not above EUR 100,000 in the current year. Tax-free means no VAT on invoices and no input tax deduction. Total turnover (Gesamtumsatz, § 19(2)) is counted on receipts and leaves out sales of fixed assets and some exempt supplies. Three rules decide most cases (UStAE 19.1):
- Previous year above EUR 25,000: standard taxation from 1 January of the current year, even if the current year stays low.
- Previous year within EUR 25,000: the scheme runs until current-year turnover passes EUR 100,000. The supply that crosses the line is already taxed in full, and from then on normal invoicing, input tax and advance returns apply.
- First year of business: the limit is EUR 25,000 in the current year, not EUR 100,000. The supply that crosses EUR 25,000 is already taxed.

A small business can give up the scheme by a statement to the tax office up to the last day of February of the second year after the year concerned. The waiver binds for at least five calendar years and can then be revoked from the start of a later calendar year (§ 19(3)).

**The EU small business scheme.** A German business that wants the small business exemption in another member state joins a special reporting procedure at the Bundeszentralamt für Steuern (BZSt), which issues a small-business identification number (§ 19a(1) UStG). Its EU-wide annual turnover must not exceed EUR 100,000 in the previous or the current year. It files a quarterly turnover report with the BZSt within one month after each quarter (§ 19a(3)). It must tell the BZSt within 15 working days if EU turnover passes EUR 100,000; participation ends at that point (§ 19a(4)). A business based elsewhere in the EU can use the German exemption on the same EUR 100,000 test with a small-business number from its home state (§ 19(4)).

**Cash accounting (Istversteuerung, § 20 UStG).** The normal rule taxes supplies when they are made (Sollversteuerung, § 16(1)). On application the tax office can let a business tax receipts instead if any one of these holds: total turnover of the previous year was not more than EUR 800,000; the business is released from bookkeeping under § 148 AO; or, for those supplies only, it practises a liberal profession under § 18(1) no. 1 EStG. Input tax is not affected: it is deductible once the supply is made and the invoice is held, not when it is paid (§ 15(1) no. 1 UStG). Only VAT on a payment made before the supply waits for both the invoice and the payment.

**Out of scope here.** VAT groups (Organschaft), the margin schemes (§§ 25, 25a), the flat rate for farmers (§ 24), and the one-stop shops for non-EU businesses (§ 18i) and imports (§ 18k). Refer these.

## Rates, bands and thresholds

| Item | Rate or amount | Year | Source |
|---|---|---|---|
| Standard and reduced VAT rates | 19% and 7% | 2026 | § 12 UStG, https://www.gesetze-im-internet.de/ustg_1980/__12.html |
| Small business: total turnover, previous year, not exceeded | EUR 25,000 | 2026 (2025 turnover) | § 19(1) UStG, https://www.gesetze-im-internet.de/ustg_1980/__19.html |
| Small business: total turnover, current year, not exceeded | EUR 100,000 | 2026 | § 19(1) UStG |
| Small business: limit in the first year of business | EUR 25,000 (current year) | 2026 | UStAE 19.1(3); USt 2 A 2026 instructions, line 53 |
| Small business waiver: binds for at least | 5 calendar years | 2026 | § 19(3) UStG |
| EU small business scheme: EU-wide annual turnover, previous and current year | EUR 100,000 | 2026 | § 19a(1) no. 2 UStG, https://www.gesetze-im-internet.de/ustg_1980/__19a.html |
| EU small business scheme: report after passing EUR 100,000 | Within 15 working days | 2026 | § 19a(4) UStG |
| EU small business scheme: quarterly turnover report | Within one month after the quarter | 2026 | § 19a(3) UStG |
| Cash accounting: previous-year total turnover, not more than | EUR 800,000 | 2026 (2025 turnover) | § 20 sentence 1 no. 1 UStG, https://www.gesetze-im-internet.de/ustg_1980/__20.html |
| Advance returns monthly if previous-year VAT was more than | EUR 9,000 | 2026 | § 18(2) UStG, https://www.gesetze-im-internet.de/ustg_1980/__18.html |
| Tax office may release from advance returns if previous-year VAT was not more than | EUR 2,000 | 2026 | § 18(2) UStG |
| One-month extension (Dauerfristverlängerung) | On application, filing and payment one month later | 2026 | § 46 UStDV, https://www.gesetze-im-internet.de/ustdv_1980/__46.html |
| Special prepayment, monthly filers with the extension | 1/11 of the previous year's advance payments | 2026 | § 47(1) UStDV, https://www.gesetze-im-internet.de/ustdv_1980/__47.html |
| Input tax correction period | 5 years; 10 years for land and buildings | 2026 | § 15a(1) UStG, https://www.gesetze-im-internet.de/ustg_1980/__15a.html |
| No § 15a correction if input tax on the asset is not more than | EUR 1,000 | 2026 | § 44(1) UStDV, https://www.gesetze-im-internet.de/ustdv_1980/__44.html |
| No correction for a year if use changed by less than 10 percentage points, unless the correction exceeds | EUR 1,000 | 2026 | § 44(2) UStDV |
| Annual-return-only correction ceiling, except sales or § 3(1b) supplies covered by § 44(3) sentence 2 UStDV | EUR 6,000 | 2026 | § 44(3) UStDV |
| Reverse charge on mobile phones, tablets, consoles, chips and Annex 4 metals: fees in one transaction at least | EUR 5,000 | 2026 | § 13b(2) nos. 10 and 11 UStG, https://www.gesetze-im-internet.de/ustg_1980/__13b.html |
| Distance sales and e-services to EU consumers, EU-wide, below which German VAT applies | EUR 10,000 (previous and current year) | 2026 | § 3c(4) UStG, https://www.gesetze-im-internet.de/ustg_1980/__3c.html |
| Annual return deadline, no adviser | 7 months after the year: 31 July 2027, a Saturday, so Monday 2 August 2027 | Return for 2026 | § 149(2) AO, https://www.gesetze-im-internet.de/ao_1977/__149.html ; § 108(3) AO, https://www.gesetze-im-internet.de/ao_1977/__108.html |
| Annual return deadline, prepared by a tax adviser | Last day of February of the second year: 29 February 2028 | Return for 2026 | § 149(3) no. 4 AO |
| Balance due on the annual return | One month after the return reaches the tax office | Return for 2026 | § 18(4) UStG |
| E-invoices: paper or other format still allowed, B2B supplies made in 2026 | Until 31 December 2026, no turnover test | 2026 | § 27(38) no. 1 UStG, https://www.gesetze-im-internet.de/ustg_1980/__27.html |
| E-invoices: paper or other format still allowed, B2B supplies made in 2027 | Only if the issuer's 2026 total turnover was not more than EUR 800,000, or by EDI | 2027 | § 27(38) nos. 2 and 3 UStG |
| Late filing surcharge, annual return | 0.25% of the tax less prepayments per started month, at least EUR 25 per month, at most EUR 25,000 | 2026 | § 152(5) and (10) AO, https://www.gesetze-im-internet.de/ao_1977/__152.html |
| Late payment surcharge | 1% per started month of the overdue tax, rounded down to a multiple of EUR 50 | 2026 | § 240(1) AO, https://www.gesetze-im-internet.de/ao_1977/__240.html |
| Interest on assessed differences | 0.15% per full month, starting 15 months after the year ends | 2026 | § 233a(2) AO, https://www.gesetze-im-internet.de/ao_1977/__233a.html ; § 238(1a) AO, https://www.gesetze-im-internet.de/ao_1977/__238.html |
| Fine for not paying VAT on time (administrative offence) | Up to EUR 30,000 | 2026 | § 26a(1) and (3) UStG, https://www.gesetze-im-internet.de/ustg_1980/__26a.html |

## The taxable base

**The annual return is a full recomputation, not a sum of the quarters.** Under § 18(3) UStG the business recomputes the year's tax from § 16(1) to (4) and § 17 UStG: output tax on the year's supplies, plus tax owed as a buyer, minus deductible input tax, plus or minus input tax corrections. The advance returns are only prepayments on it. So the annual return is where errors in the advance returns are put right, where § 15a corrections of up to EUR 6,000 are normally made (§ 44(3) UStDV; its sentence 2 requires sale/§ 3(1b) disposal corrections in the advance return for the period of disposal), and where a partial-exemption key estimated during the year is replaced with the final one.

**How the 2026 form (USt 2 A) ends.** Section K collects the totals. Line 124 (Kz 816) is the remaining tax or surplus for the year. Line 125 is the prepayment total for 2026, the "Vorauszahlungssoll", including any special prepayment. Line 126 (Kz 820) is the balance: line 124 minus line 125. A positive balance is the closing payment (Abschlusszahlung); a negative one is a refund. Line 125 is what was declared or assessed for the advance returns, not what was actually paid; late or missing payments are chased separately.

**The special prepayment in the annual figures.** A monthly filer with the one-month extension pays 1/11 of the previous year's advance payments by 10 February (§§ 47, 48(2) UStDV). It is credited in the last advance return of the year (§ 48(4) UStDV) and so it sits inside the line 125 total. A quarterly filer pays none.

**Small business: what counts.** Total turnover is the sum of taxable supplies counted on receipts, less exempt financial and insurance supplies and some others listed in § 19(2), and without sales of fixed assets. Supplies on which the customer owes the tax under § 13b count in; services the small business buys under § 13b do not (UStAE 19.2(2)). A small business still owes VAT on imports, intra-Community acquisitions and reverse-charge purchases (UStAE 19.1(1)).

**Moving into standard taxation.** When a small business moves into standard taxation, a supply made in the new year is taxed in full even if the customer paid in advance in the old year. That after-tax goes in line 39 (Kz 317) of the annual return and in line 46 (Kz 65) of the advance return for the period of the supply (USt 1 E 2026, line 46). A supply made in the small-business year stays tax-free even when it is paid later. Input tax on assets bought while exempt can come back over the § 15a period: the 2026 form lists a change of scheme under the small business rules as a change in circumstances for § 15a (USt 2 A, line 100).

**Cash accounting.** The tax arises when the fee is received. When the method changes, no supply may be taxed twice or escape tax (§ 20 sentence 3). A supply made in a cash-accounting year stays on cash accounting if it is paid after a later switch to accruals (USt 2 A 2026 instructions, line 21).

**Partial exemption (§ 15(4) UStG).** When a purchase is used for both taxable supplies and exempt supplies that bar deduction, the share linked to the exempt supplies is not deductible. Allocate directly where you can. Use a reasonable estimate otherwise. Split by turnover only if no more precise economic allocation is possible. For buildings, split by floor area unless another method is more precise. The share is fixed for the year in the annual return.

**Input tax correction (§ 15a UStG).** If the use of an asset changes within five years of first use (ten years for land and buildings), the input tax deducted on it is corrected by one fifth (or one tenth) a year for each year of change (§ 15a(1) and (5)). A sale or a private withdrawal during the period is also a change (§ 15a(8)). The UStDV simplifications are in the table: nothing below EUR 1,000 of input tax, nothing for a change under 10 points unless above EUR 1,000, and generally only in the annual return up to EUR 6,000. If the asset is sold or supplied under § 3(1b) during the correction period, § 44(3) sentence 2 instead requires the corrections for the disposal year and the remaining years in the advance return for the period of disposal, even when the amount is no more than EUR 6,000.

**Domestic reverse charge (§ 13b UStG).** The customer owes the tax for, among others, services from EU suppliers under § 3a(2), works and services from foreign suppliers, construction services to a business that itself provides construction services, building cleaning on the same basis, and mobile phones, tablets and chips from EUR 5,000. The customer declares output tax and, if entitled, deducts the same amount as input tax. A small business that receives such services owes the tax and cannot deduct it. The boxes and the supplier patterns are in [germany-vat-return](germany-vat-return.md).

## Deadlines and filing

| What | When | Rule |
|---|---|---|
| Annual return 2026, no adviser | Monday 2 August 2027 (31 July 2027 is a Saturday) | § 149(2) AO; § 108(3) AO |
| Annual return 2026, prepared by a tax adviser | Tuesday 29 February 2028 | § 149(3) no. 4 AO. The tax office can call for it earlier, with four months' notice (§ 149(4)) |
| Annual return when the business stopped during 2026 | Adviser extension does not apply | § 149(5) AO |
| Closing payment | One month after the return reaches the tax office | § 18(4) UStG; USt 2 A line 22 note |
| Short tax period (business ended or office ordered it) | One month after the short period ends | § 18(3) sentence 2 UStG |
| Advance returns | 10th day after the month or quarter; one month later with the extension | § 18(1) UStG; § 46 UStDV |
| Special prepayment with the extension | By the due date of the first advance return of the year: 10 February 2026 for 2026 | § 48(2) UStDV |
| Choose monthly filing after a surplus above EUR 9,000 | File the January return by 10 February | § 18(2a) UStG |
| Small business waiver for 2026 | By 29 February 2028 | § 19(3) UStG |
| EU small business quarterly report | Within one month after each quarter, to the BZSt | § 19a(3) UStG |
| One-stop shop return and payment | End of the month after each quarter: 30 April, 31 July, 31 October, 31 January. Payment must have reached the Bundeskasse by then. A nil return is due for a quarter with no sales. For Q4 2026 the date is Sunday 31 January 2027: file and pay by Friday 29 January 2027, because no official text moves this date | § 18j(4) UStG; BZSt OSS page |

**How to file.** The annual return goes to the local tax office electronically, authenticated, through ELSTER (§ 18(3) UStG; § 87a(6) AO). Paper only with permission, to avoid hardship. Foreign businesses add Anlage UN. The one-stop shop return goes to the BZSt through the BZSt online portal.

**One-stop shop (§ 18j UStG).** A business established only in Germany that sells goods at a distance or supplies telecom, broadcasting or electronic services to consumers in other member states charges the customer's country's VAT once the EU-wide total passes EUR 10,000 (§ 3c(4)); the very sale that crosses it is the first one. Instead of registering in each country it can declare that VAT quarterly through the one-stop shop at the BZSt. The notice to take part must reach the BZSt before the quarter from which the scheme is used (§ 18j(1) sentence 3), so registration normally starts on the first day of the quarter after the application. Taking part covers all member states and all such supplies. Corrections to an OSS return within three years go in a later OSS return. Repeated late filing leads to exclusion (§ 18j(6)).

## Penalties and interest

- **Late annual return.** The tax office may set a late filing surcharge (§ 152(1) AO). It must set one if the return is not filed within 14 months after the year ends, for 2026 by 29 February 2028, unless the tax office extended the deadline or the tax is nil, negative or not above the prepayments (§ 152(2) no. 1 and (3)). The amount is 0.25% per started month of the tax less the prepayments, at least EUR 25 per started month, capped at EUR 25,000 (§ 152(5) sentence 2 and (10)). For the monthly or quarterly advance returns the amount is discretionary instead (§ 152(8)).
- **Late payment.** 1% per started month on the overdue tax rounded down to a multiple of EUR 50 (§ 240(1) AO). This runs on a late closing payment and on late advance payments.
- **Interest.** Where an assessment differs from the prepayments, the difference carries 0.15% for each full month from 1 April 2028 for tax year 2026 (§ 233a(2) AO, 15 months after the year end; § 238(1a) AO).
- **Fines.** Not paying an advance payment, a closing balance or an OSS payment in full and on time is an administrative offence with a fine up to EUR 30,000 (§ 26a(1) and (3) UStG). Deliberately or recklessly not issuing a required invoice, or not keeping invoices for eight years: up to EUR 5,000. Deliberately or recklessly not keeping, for two years, the invoices and payment records that § 14b(1) sentence 5 requires: up to EUR 1,000 (§ 26a(2) nos. 1 to 3 and (3)).
- **Correcting an error.** An error in an advance return can be corrected in the annual return, as in Example 1. Deliberate under-declaration is tax evasion and outside this skill.

## Cross-border points

- **Foreign businesses with German VAT duties** file the annual return like a German business, with Anlage UN and, from 2026, a foreign address for notices (BMF letter of 29 December 2025 on the 2026 form, para. 4). The tax office for each country is in the pack README.
- **EU businesses using the German small business exemption** need the small-business number from their home state and EU turnover within EUR 100,000 (§ 19(4)). They waive it in their home state, not in Germany (§ 19(5)).
- **German businesses using another state's small business exemption** go through the BZSt procedure in § 19a, with the quarterly report and the 15-working-day notice above.
- **One-stop shop.** Sales declared through the OSS are taxed in the customer's state and are not part of the German output tax.
- **Reverse charge on services from abroad** applies to a small business too, which then must file an advance return for that period and an annual return for the year (§ 18(4a)).

## Worked examples

### Example 1: A GmbH's 2026 annual return with one correction

Muster GmbH is a quarterly filer on accruals, with no extension. Its four 2026 advance returns declared output tax of EUR 38,000 and input tax of EUR 29,750, so prepayments of EUR 8,250 (Q1 2,550, Q2 1,900, Q3 2,200, Q4 1,600). Preparing the annual return, the accountant finds a December 2026 sale of EUR 10,000 net, invoiced but booked in January 2027. It belongs to 2026. Output tax for the year is 38,000 + 1,900 = EUR 39,900. Line 124 (Kz 816) is 39,900 - 29,750 = EUR 10,150. Line 125 is EUR 8,250. Line 126 (Kz 820) is a closing payment of EUR 1,900.

The GmbH files itself on Friday 14 May 2027, so the balance is due one month later, Monday 14 June 2027. If it paid two months late, the late payment surcharge would be 1% x 1,900 x 2 = EUR 38. If it had instead filed on 15 October 2027, three months started after the 2 August deadline. Should the tax office set a surcharge, 0.25% of 1,900 is EUR 4.75 a month, below the EUR 25 minimum, so 3 x 25 = EUR 75.

```oa-check
name: Muster GmbH, 2026 annual VAT return reconciling four quarters with a missed invoice
inputs:
  q_output_vat: 38000
  q_input_vat: 29750
  missed_invoice_net: 10000
  rate: 0.19
  months_paid_late: 2
  months_filed_late: 3
steps:
  - prepayments_line_125: q_output_vat - q_input_vat
  - annual_output_vat: q_output_vat + missed_invoice_net * rate
  - kz816_line_124: annual_output_vat - q_input_vat
  - kz820_line_126: kz816_line_124 - prepayments_line_125
  - overdue_rounded: floor(kz820_line_126 / 50) * 50
  - late_payment_surcharge: overdue_rounded * 0.01 * months_paid_late
  - filing_surcharge_per_month: max(kz820_line_126 * 0.0025, 25)
  - late_filing_surcharge: filing_surcharge_per_month * months_filed_late
expected:
  prepayments_line_125: 8250
  annual_output_vat: 39900
  kz816_line_124: 10150
  kz820_line_126: 1900
  overdue_rounded: 1900
  late_payment_surcharge: 38
  filing_surcharge_per_month: 25
  late_filing_surcharge: 75
```

### Example 2: A translator leaves the small business scheme and uses cash accounting

Lena is a self-employed translator, a liberal profession under § 18(1) no. 1 EStG. Her 2024 total turnover was within EUR 25,000, so in 2025 she used § 19. Her total turnover for 2025 was EUR 31,200, counted on receipts and including the advance below (UStAE 19.2(1)). That is above EUR 25,000 but below EUR 100,000, so 2025 stayed tax-free and she filed no VAT return for it. Because 2025 passed EUR 25,000, every supply she makes from 1 January 2026 is taxed at 19%. Her 2025 turnover is far below EUR 800,000, and she is a liberal professional, so the tax office can let her tax receipts (§ 20 nos. 1 and 3); she applies for it.

Her 2025 tax was nil, so she files quarterly (§ 18(2)). In Q1 2026 she receives EUR 8,925 for 2026 work (EUR 7,500 net plus EUR 1,425 VAT) and EUR 1,800 for a December 2025 job. The December job was supplied while she was exempt, so it carries no VAT. A client paid her EUR 2,000 in November 2025 as an advance for a job she delivered in February 2026. The supply is in 2026, so the advance is taxed in the period of the supply (USt 1 E 2026, line 46; USt 2 E 2026, line 39): 2,000 x 19 / 119 = EUR 319.33, in Kz 65 of the advance return and line 39 (Kz 317) of the annual return. Her input tax on 2026 invoices for the quarter is EUR 380. Q1 payment: 1,425 + 319.33 - 380 = EUR 1,364.33, due Friday 10 April 2026. She must already be able to receive e-invoices. For 2026 supplies she may still send paper invoices, or PDF invoices with the client's consent, to German business clients until 31 December 2026 (§ 27(38) no. 1); for 2027 supplies the relief continues to 31 December 2027 as long as her 2026 total turnover stays within EUR 800,000 (no. 2).

```oa-check
name: Translator, out of § 19 from 2026 after EUR 31,200 in 2025, cash accounting, Q1 2026
inputs:
  turnover_2025: 31200
  small_business_prev_limit: 25000
  cash_accounting_limit: 800000
  q1_receipts_2026_work_gross: 8925
  q1_receipts_2025_work: 1800
  advance_received_2025: 2000
  q1_input_vat: 380
  rate: 0.19
steps:
  - excess_over_25000: max(turnover_2025 - small_business_prev_limit, 0)
  - headroom_under_800000: cash_accounting_limit - turnover_2025
  - q1_net_taxable: q1_receipts_2026_work_gross / (1 + rate)
  - q1_output_vat: q1_net_taxable * rate
  - vat_on_2025_work: q1_receipts_2025_work * 0
  - after_tax_on_advance_kz65: advance_received_2025 * rate / (1 + rate)
  - q1_advance_payment: q1_output_vat + vat_on_2025_work + after_tax_on_advance_kz65 - q1_input_vat
expected:
  excess_over_25000: 6200
  headroom_under_800000: 768800
  q1_net_taxable: 7500
  q1_output_vat: 1425
  vat_on_2025_work: 0
  after_tax_on_advance_kz65: 319.33
  q1_advance_payment: 1364.33
```

## Ask the client first

1. Total turnover (on receipts, without fixed-asset sales) for 2025 and 2026 to date, and the year the business started. This decides § 19 and § 20.
2. Accruals or cash accounting, and the tax office's letter allowing cash accounting.
3. Monthly or quarterly filer, whether the one-month extension is in place, and the special prepayment paid in February.
4. Any exempt supplies (rent, finance, medical, education) alongside taxable ones, and how input tax was split during the year.
5. Assets bought in the last five years (ten for buildings) whose use changed, that were sold, or that came from a small-business year.
6. Sales to consumers in other EU states, and whether the business is registered for the one-stop shop or the EU small business scheme.

## Sources

| Source | URL | Read on |
|---|---|---|
| UStG § 3c (distance sales, EUR 10,000) | https://www.gesetze-im-internet.de/ustg_1980/__3c.html | 2026-10-23 |
| UStG § 13b (reverse charge) | https://www.gesetze-im-internet.de/ustg_1980/__13b.html | 2026-10-23 |
| UStG § 14 (invoices, e-invoice duty) | https://www.gesetze-im-internet.de/ustg_1980/__14.html | 2026-10-23 |
| UStG § 15 (input tax, partial exemption) | https://www.gesetze-im-internet.de/ustg_1980/__15.html | 2026-10-23 |
| UStG § 15a (input tax correction) | https://www.gesetze-im-internet.de/ustg_1980/__15a.html | 2026-10-23 |
| UStG § 16 (tax period, computation) | https://www.gesetze-im-internet.de/ustg_1980/__16.html | 2026-10-23 |
| UStG § 18 (advance and annual returns, closing payment) | https://www.gesetze-im-internet.de/ustg_1980/__18.html | 2026-10-23 |
| UStG § 18j (one-stop shop, EU scheme) | https://www.gesetze-im-internet.de/ustg_1980/__18j.html | 2026-10-23 |
| UStG § 19 (small businesses) | https://www.gesetze-im-internet.de/ustg_1980/__19.html | 2026-10-23 |
| UStG § 19a (EU small business procedure) | https://www.gesetze-im-internet.de/ustg_1980/__19a.html | 2026-10-23 |
| UStG § 20 (cash accounting) | https://www.gesetze-im-internet.de/ustg_1980/__20.html | 2026-10-23 |
| UStG § 26a (fines) | https://www.gesetze-im-internet.de/ustg_1980/__26a.html | 2026-10-23 |
| UStG § 27(38) and (39) (e-invoice transition; small business filing from 2024) | https://www.gesetze-im-internet.de/ustg_1980/__27.html | 2026-10-23 |
| UStDV §§ 44, 46, 47, 48 | https://www.gesetze-im-internet.de/ustdv_1980/__44.html | 2026-10-23 |
| AO § 168 (return as an assessment; refunds need consent) | https://www.gesetze-im-internet.de/ao_1977/__168.html | 2026-10-23 |
| AO § 108 (deadline on a weekend) | https://www.gesetze-im-internet.de/ao_1977/__108.html | 2026-10-23 |
| AO § 149 (filing deadlines) | https://www.gesetze-im-internet.de/ao_1977/__149.html | 2026-10-23 |
| AO § 152 (late filing surcharge) | https://www.gesetze-im-internet.de/ao_1977/__152.html | 2026-10-23 |
| AO § 233a (interest period) | https://www.gesetze-im-internet.de/ao_1977/__233a.html | 2026-10-23 |
| AO § 238 (interest rate) | https://www.gesetze-im-internet.de/ao_1977/__238.html | 2026-10-23 |
| EGAO Art. 97 § 36 (extended deadlines end with tax year 2024) | https://www.gesetze-im-internet.de/aoeg_1977/art_97__36.html | 2026-10-23 |
| AO § 240 (late payment surcharge) | https://www.gesetze-im-internet.de/ao_1977/__240.html | 2026-10-23 |
| BMF letter of 29 December 2025, 2026 annual VAT return form USt 2 A and instructions USt 2 E | https://www.bundesfinanzministerium.de/Content/DE/Downloads/BMF_Schreiben/Steuerarten/Umsatzsteuer/2025-12-29-muster-USt-erklaerung-2026.pdf?__blob=publicationFile&v=5 | 2026-10-23 |
| BMF letter of 29 December 2025, 2026 advance return form USt 1 A and instructions USt 1 E (line 46, Kz 65) | https://www.bundesfinanzministerium.de/Content/DE/Downloads/BMF_Schreiben/Steuerarten/Umsatzsteuer/2025-12-29-vordruckmuster-USt-voranmeldung-2026.pdf?__blob=publicationFile&v=2 | 2026-10-23 |
| VAT Application Decree (UStAE) as at 31 December 2025, sections 19.1, 19.2 and 19.7 | https://www.bundesfinanzministerium.de/Content/DE/Downloads/BMF_Schreiben/Steuerarten/Umsatzsteuer/Umsatzsteuer-Anwendungserlass/Umsatzsteuer-Anwendungserlass-31-12-2025.pdf?__blob=publicationFile&v=2 | 2026-10-23 |
| BMF FAQ on e-invoicing (receiving from 1 January 2025) | https://www.bundesfinanzministerium.de/Content/DE/FAQ/e-rechnung.html | 2026-10-23 |
| BZSt, One-Stop-Shop EU scheme (deadlines, payment, nil returns) | https://www.bzst.de/DE/Unternehmen/Umsatzsteuer/One-Stop-Shop_EU/one_stop_shop_eu_node.html | 2026-10-23 |
| ELSTER, the filing portal | https://www.elster.de | 2026-10-23 |

Not yet confirmed: whether the one-stop shop deadline for Q4 2026 (Sunday 31 January 2027) moves to the next working day under § 108(3) AO; neither § 18j UStG, UStAE 18j.1 nor the BZSt page says so, so the skill tells the reader to file and pay by Friday 29 January 2027.

> Contributed by Ryan Duguid.

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
