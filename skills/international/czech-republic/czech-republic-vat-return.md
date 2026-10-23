---
name: czech-republic-vat-return
description: "Czech VAT (DPH) for tax year 2026 under the VAT Act (235/2004 Coll.) as in force from 1 January 2026. Covers who must register (calendar-year turnover over CZK 2,000,000 makes a payer from 1 January next year, over CZK 2,536,500 from the next day, 10 working days to apply), the 21% and 12% rates and what each covers, books exempt with credit, input VAT limits, the VAT return (přiznání k DPH), control statement (kontrolní hlášení) and EC sales list (souhrnné hlášení), monthly and quarterly periods and the 25-day deadlines, domestic and cross-border reverse charge, intra-EU supplies, unreliable payers and recipient liability, and penalties including control statement fines. Trigger on: DPH, přiznání k DPH, kontrolní hlášení, souhrnné hlášení, plátce DPH, registrace k DPH, nespolehlivý plátce, přenesení daňové povinnosti, Czech VAT. Out of scope: income tax (cz-income-tax, cz-corporate-income-tax) and non-residents generally (cz-cross-border). cz-vat-return points here."
jurisdiction: CZ
category: international
tax_year: 2026
tier: 2
last_updated: 2026-10-23
version: 2.1
verified_by: pending
trust_label: Built by Michael Cutajar and the OpenAccountants team
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Czech Republic: VAT (DPH) (2026) v2.1

> **Source-cited draft.** Built by Michael Cutajar and the OpenAccountants team. No accountant has reviewed this skill yet. Every figure comes from the VAT Act and the Tax Code as published in e-Sbírka (versions in force from 1 January 2026), the official VAT return form and the Financial Administration (Finanční správa), all read on 23 October 2026. It prepares working papers. It is not authority to file or pay.

This skill covers value added tax (daň z přidané hodnoty, DPH) under Act No. 235/2004 Coll. ("VAT Act") and the procedure rules in Act No. 280/2009 Coll. ("Tax Code"). It links to the other skills in the pack rather than repeating them:

- Self-employed income tax (VAT registration ends the flat-rate regime): [cz-income-tax](cz-income-tax.md).
- Companies: [cz-corporate-income-tax](cz-corporate-income-tax.md).
- Residence, non-residents and treaties: [cz-cross-border](cz-cross-border.md).
- Overview: [cz-tax-overview](cz-tax-overview.md).
- [cz-vat-return](cz-vat-return.md) is a pointer to this skill.

Tax period: the calendar month, or the quarter by election. Currency: Czech koruna (CZK). Authority: the Financial Administration and its tax offices (finanční úřady).

## Who this applies to

**Payers (plátci).** A taxable person with its seat in the Czech Republic becomes a payer in two ways (VAT Act § 6, as rewritten by Act 461/2024 from 1 January 2025):

- If its domestic turnover in a **calendar year** exceeds **CZK 2,000,000**, it is a payer from 1 January of the next year (§ 6(1)). It can choose to be a payer from the day after the threshold is crossed, but only by saying so in a registration application filed on time (§ 6(2)(a)).
- If its domestic turnover in the calendar year exceeds **CZK 2,536,500**, it is a payer from the **day after** that amount is crossed (§ 6(2)(b)).

Turnover (obrat v tuzemsku, § 4a) is the sum of consideration without VAT for supplies with a Czech place of supply: taxable supplies, supplies exempt with credit, and financial, insurance and property supplies exempt without credit when they are not occasional ancillary activity. Sales of the business's own long-term assets are left out unless they are part of its usual activity (§ 4a(3)). Since 2025 turnover is counted per calendar year, not over a rolling 12 months (Finanční správa, information on changes from 1 January 2025).

A person making only supplies that would give no right to deduct (financial, insurance or property supplies exempt without credit) does not become a payer under § 6(1) or (2). It becomes a payer only if it also makes a supply in its turnover that would give a right to deduct, and must apply within 10 working days of that supply (§ 6(3), § 94(2)).

Anyone with its seat or establishment in the Czech Republic who makes or will make supplies with a right to deduct can register voluntarily (§ 6f), unless it has been declared an unreliable person (§ 94a(1)).

**Non-established persons.** A taxable person without a Czech seat (and not in the EU small-business scheme for the Czech Republic) becomes a payer from the day of its first taxable supply with a Czech place of supply, unless the customer must account for the tax or the supply goes through the one-stop shop (§ 6c(1)). There is no turnover threshold. See Cross-border points.

**Identified persons (identifikované osoby).** A taxable person that is not a payer, or a non-taxable legal person, becomes an identified person when it makes a taxable acquisition of goods from another member state, receives a service with a Czech place of supply from a non-established person, or supplies a § 9(1) service to a business in another member state (§§ 6g to 6l). It reports and pays reverse-charge tax but does not charge Czech VAT on its own sales.

**Out of scope here:** VAT groups (§ 5a, § 95a), the special schemes (travel § 89, margin § 90, investment gold § 92), the EU cross-border small-business scheme (§§ 109bb to 109bg), one-stop shop returns (§§ 110a onward), partial exemption coefficients (§§ 75 and 76) and the capital goods adjustment (§§ 78 onward). Name them and refer the client.

## Rates, bands and thresholds

| Item | Rate or amount | Year | Source |
|---|---|---|---|
| Standard rate | 21% | 2026 | VAT Act § 47(1)(a), https://e-sbirka.gov.cz/sb/2004/235/2026-01-01 |
| Reduced rate (the only one since 2024) | 12% | 2026 | VAT Act § 47(1)(b), https://e-sbirka.gov.cz/sb/2004/235/2026-01-01 |
| Goods at 12% | Annex 3: food, animal feed and live animals (customs chapters 01-05, 07-23, 25), but drinks only the selected ones listed; drinking water; live plants; medicines and listed medical devices; newspapers and periodicals; child car seats; listed aids for disabled people | 2026 | VAT Act § 47(3), Annex 3, https://e-sbirka.gov.cz/sb/2004/235/2026-01-01 |
| Services at 12% | Annex 2: water supply and sewage; public passenger transport and ski lifts; accommodation; catering (drinks only drinking water and the selected drinks); entry to cultural events, museums, zoos and cinemas; sports entry and use of sports facilities; health and social care; home care; funeral services; saunas and steam baths | 2026 | VAT Act § 47(4), Annex 2, https://e-sbirka.gov.cz/sb/2004/235/2026-01-01 |
| Heat and cooling | 12% | 2026 | VAT Act § 47(3), https://e-sbirka.gov.cz/sb/2004/235/2026-01-01 |
| Books and e-books | Exempt with right to deduct | 2026 | VAT Act § 71i, https://e-sbirka.gov.cz/sb/2004/235/2026-01-01 |
| Registration: payer from 1 January next year | Domestic turnover over CZK 2,000,000 in a calendar year | 2026 | VAT Act § 6(1), https://e-sbirka.gov.cz/sb/2004/235/2026-01-01 |
| Registration: payer from the next day | Domestic turnover over CZK 2,536,500 in a calendar year | 2026 | VAT Act § 6(2)(b), https://e-sbirka.gov.cz/sb/2004/235/2026-01-01 |
| Registration application | Within 10 working days of crossing either amount | 2026 | VAT Act § 94(1), https://e-sbirka.gov.cz/sb/2004/235/2026-01-01 |
| Quarterly periods allowed | Prior-year domestic turnover not over CZK 15,000,000, not unreliable, not a group, notice by end of January | 2026 | VAT Act § 99a(1), https://e-sbirka.gov.cz/sb/2004/235/2026-01-01 |
| Control statement detail split | Tax documents over CZK 10,000 including VAT reported one by one (sections A.4 and B.2) | 2026 | Control Statement Guidelines, https://financnisprava.gov.cz/assets/cs/prilohy/d-seznam-dani/Control_Statement_Guidelines_20240101.pdf |
| Passenger car (M1) held as long-term asset | Input VAT counted at most CZK 420,000 | 2026 | VAT Act § 72(3), https://e-sbirka.gov.cz/sb/2004/235/2026-01-01 |
| Selected goods under temporary domestic reverse charge | Tax base over CZK 100,000 per supply (cereals and technical crops, metals, mobile phones, integrated circuits, laptops and tablets, game consoles) | 2026 | Government Regulation 361/2014 § 2(2), (3), https://e-sbirka.gov.cz/sb/2014/361 |

What is at 21%: everything not listed in Annex 2 or 3. Since the 2024 consolidation package (Act 349/2023) merged the old 15% and 10% rates into 12%, that includes cleaning, hairdressing, small repairs, taxis (not scheduled public transport) and, in restaurants, drinks other than drinking water and the selected drinks. A restaurant bill with a meal and beer splits into a 12% line and a 21% line.

## The taxable base

**What is taxed.** Supplies of goods and services for consideration with a Czech place of supply, acquisitions of goods from other member states, imports, and services received from abroad where the Czech recipient must account for the tax (§ 108). The base is the consideration without VAT (§ 36).

**Exempt with right to deduct.** Intra-EU supplies of goods to a customer registered in another member state that gave its VAT number (§ 64), exports (§ 66), books (§ 71i) and the other items on line 26 of the return.

**Exempt without right to deduct.** Financial services, insurance, the postal universal service, health and education services, and most supplies and lettings of property (§§ 51 to 62). A business with these supplies and taxable ones needs the coefficient under §§ 75 and 76; this skill does not compute it.

**Input VAT.** A payer deducts input VAT on supplies used for its taxable or exempt-with-credit activity (§ 72(1)). It needs a tax document (§ 73(1)). The claim can be made from the period in which the conditions are met (§ 73(2)) and no later than the end of the second calendar year after the year in which the right arose (§ 73(3)). Limits:

- **Representation (entertaining)** that is not deductible for income tax gives no input VAT (§ 72(6)).
- **Passenger cars (M1)** held as long-term assets: input VAT is capped at CZK 420,000 (§ 72(3)). Private use is deducted in proportion (§ 72(9), § 75).
- **Mixed use** in general: only the business share (§ 72(9)).

**Reverse charge on services and goods received from abroad.** The payer or identified person self-assesses output tax and, where the use gives a right to deduct, claims the same amount as input tax in the same return. The net effect is zero for a fully taxable business.

**Domestic reverse charge (§ 92a onward)** between two payers: construction and assembly work under CZ-CPA 41 to 43 and supply of workers for it (§ 92e); waste and scrap in Annex 5 (§ 92c); unwrought gold of 333 thousandths or more, and investment gold the supplier has opted to tax (§ 92b); property supplies the supplier has opted to tax (§ 92d); and, under § 92f with Government Regulation 361/2014, emission allowances, electricity and gas to traders, electricity certificates, wholesale electronic communications and the selected goods over CZK 100,000. The supplier invoices without VAT and reports the sale on line 25; the customer self-assesses on lines 10 and 11 and deducts on lines 43 and 44.

**Return lines (form 25 5401, specimen no. 26).** Domestic supplies: lines 1 (21%) and 2 (12%). Intra-EU acquisitions of goods: 3 and 4. Services received from EU businesses under § 9(1): 5 and 6. Imports where the payer self-assesses (§ 23): 7 and 8. Domestic reverse charge as customer: 10 and 11. Other receipts where the recipient declares tax (§ 108), such as services from outside the EU: 12 and 13. Intra-EU supplies of goods: 20. Services to EU businesses: 21. Exports: 22. Domestic reverse charge as supplier: 25. Input VAT from domestic payers: 40 (21%) and 41 (12%); on imports through customs: 42; on lines 3 to 13: 43 and 44. Output tax: 62. Deduction: 63. Tax due: 64. Excess deduction (refund): 65.

## Deadlines and filing

| Obligation | Deadline | Source |
|---|---|---|
| Registration application (turnover) | 10 working days after crossing CZK 2,000,000 or CZK 2,536,500 | VAT Act § 94(1) |
| Tax period | Calendar month; quarter by election | VAT Act §§ 99, 99a |
| Quarterly election | Notice by end of January; not for the year of registration or the next year, unless the tax office allows the next year on a request filed by the end of October of the registration year; not for unreliable payers or groups | VAT Act § 99a(1), (3), (4) |
| VAT return | 25 days after the end of the period; cannot be extended | Tax Code § 136(4); VAT Act § 101(2) |
| Payment | Same day as the return deadline | Tax Code § 135(3) |
| Nil return | Still required for an established payer | VAT Act § 101(3) |
| Control statement, legal persons | Monthly, 25 days after each month, even if the return is quarterly | VAT Act § 101e(1) |
| Control statement, natural persons | With the VAT return (monthly or quarterly) | VAT Act § 101e(2) |
| Correcting control statement after the deadline (následné) | Within 5 working days of finding the error | VAT Act § 101f(2) |
| Reply to a tax office call about a missing control statement | 5 days from notice of the call | VAT Act § 101g(1) |
| EC sales list (souhrnné hlášení) | Monthly, 25 days after the month; with the return if the payer only supplies § 9(1) services | VAT Act § 102(5), (6) |

A deadline on a Saturday, Sunday or public holiday moves to the next working day (Tax Code § 33(4)).

**Electronic filing only.** The return, the control statement, the EC sales list and the registration application must be filed electronically in the published format. An e-mail is not a valid filing, and a filing in the wrong format or structure has no effect (VAT Act § 101a). In practice that means the EPO portal or a data box (datová schránka).

**Who files a control statement.** A payer that made or received domestic taxable supplies, self-assessed under domestic reverse charge, or declared tax on an acquisition or a service from a non-established supplier (§ 101c, § 108(2) and (3)). Domestic reverse charge goes in A.1 and B.1, acquisitions and services from abroad in A.2, other documents over CZK 10,000 including VAT one by one in A.4 and B.2, and the rest in totals in A.5 and B.3 (Control Statement Guidelines). A payer with nothing under § 101c in a period does not file one, but must still answer a tax office call within 5 days (§ 101g(1)).

## Penalties and interest

**Control statement fines (VAT Act § 101h), fixed amounts:**

| Situation | Fine | Halved |
|---|---|---|
| Filed late without being called | CZK 1,000 | not halved |
| Filed in the replacement period after a call | CZK 10,000 | CZK 5,000 |
| Not filed after a call to change, add or confirm data | CZK 30,000 | CZK 15,000 |
| Not filed at all after a call under § 101g(1) | CZK 50,000 | CZK 25,000 |
| Not correcting data after a call | Up to CZK 50,000, discretionary | |
| Seriously obstructing VAT administration | Up to CZK 500,000, discretionary | |

The CZK 10,000, 30,000 and 50,000 fines are halved if the payer is a natural person, files quarterly, or is a single-member s.r.o. whose member is a natural person (§ 101h(2)). The first delay in a calendar year under the CZK 1,000 rule, and the first under the CZK 10,000 rule, carry no fine (§ 101j). A payer can ask for the CZK 10,000 to 50,000 fines to be waived within 3 months if the reason is justifiable (§ 101k). Fines are due 15 days after the decision becomes final (§ 101h(6)).

**Late VAT return (Tax Code § 250).** If the delay is more than 5 working days: 0.05% of the tax for each day of delay, at most 5%; or 0.05% of the excess deduction, at most 5%. Below CZK 1,000 it is not charged. The cap is CZK 300,000. A return never filed costs at least CZK 500. The fine is halved if the return is filed within 30 days of the deadline and no other late filing was found that calendar year (§ 250(7)).

**Penalty on additional assessment (Tax Code § 251).** 20% of tax increased by the tax office, or of an excess deduction reduced. No penalty arises on tax the payer declares itself in an additional return (§ 251(4)).

**Late payment interest (Tax Code § 252; Government Regulation 351/2013 § 2).** From the fourth day after the due date: the Czech National Bank repo rate on the first day of the relevant half-year plus 8 percentage points a year (Tax Code § 251a(5)). Not charged if the total is CZK 1,000 or less for one period (§ 251a(2)).

**Other duties.** Failing a registration or reporting duty, including the EC sales list: fine up to CZK 500,000 (Tax Code § 247a(1)).

**Unreliable payer (nespolehlivý plátce, VAT Act § 106a).** The tax office declares a payer unreliable for a serious breach of its duties, and the status is published in the VAT register. Consequences:

- The payer files monthly. A quarterly payer switches to monthly from the next quarter (§ 99a(4)).
- A customer that receives a supply from a payer published as unreliable is presumed to have known the tax would not be paid and so is **liable for the supplier's unpaid VAT** unless it rebuts that presumption (§ 109(1), (2)(a)). The same presumption applies if the customer pays to a bank account the tax office has not published for that supplier (§ 109(2)(c)(2)), pays in a virtual asset, pays a price obviously out of line with the market without economic reason, or pays cash above the cash-payment limit.
- The customer can protect itself by paying the VAT part of the invoice directly to the supplier's tax office (§ 109a).
- A person declared unreliable cannot register voluntarily (§ 94a(1)).

Check each supplier in the VAT register (Registr DPH) on the day of payment.

## Cross-border points

- **Intra-EU supply of goods.** Exempt with credit if the customer is registered in another member state, gave its VAT number, and the goods leave the Czech Republic (§ 64(1)). Report on line 20 and in the EC sales list.
- **Services to EU businesses (§ 9(1) general rule).** No Czech VAT; the customer reverse-charges. Report on line 21 and in the EC sales list (§ 102(1)(d)).
- **Services received from abroad.** A Czech payer or identified person accounts for the tax (§ 108(3)(a)). From EU suppliers: lines 5 and 6. From outside the EU: lines 12 and 13. Deduct on lines 43 and 44.
- **Intra-EU acquisitions of goods.** Self-assessed on lines 3 and 4, deducted on lines 43 and 44 (§ 108(2)).
- **Non-established suppliers.** A business with no Czech seat becomes a payer from its first Czech taxable supply that the customer does not reverse-charge (§ 6c), and must apply within 10 working days (§ 94(4)). It files returns only for periods with something to declare (§ 101(4)) and must give an e-mail address in its application (§ 96(3)).
- **Distance sales to consumers and digital services.** Through the one-stop shop (§§ 110a onward). Not covered here.
- **EU small-business scheme.** From 2025 a Czech business can use the small-business exemption in other member states, and EU businesses can use it in the Czech Republic (§§ 109bb onward). Not covered here.

## Worked examples

### Example 1: s.r.o., monthly return for May 2026

A Czech s.r.o., a monthly payer, has these figures for May 2026, all without VAT:

1. Domestic sales of services at 21%: CZK 500,000. Output tax CZK 105,000 (line 1).
2. Domestic sales of food at 12%: CZK 100,000. Output tax CZK 12,000 (line 2).
3. Advertising bought from an Irish company, reverse charge: CZK 40,000. Self-assessed tax at 21%: CZK 8,400 (line 5).
4. Output tax (line 62): 105,000 + 12,000 + 8,400 = CZK 125,400.
5. Domestic purchases at 21% from payers: CZK 200,000. Input tax CZK 42,000 (line 40).
6. Input tax on the reverse-charge service: CZK 8,400 (line 43).
7. Deduction (line 63): 42,000 + 8,400 = CZK 50,400.
8. Tax due (line 64): 125,400 less 50,400 = CZK 75,000.

The return, the payment and the control statement are all due on Thursday 25 June 2026. The Irish service goes in section A.2 of the control statement. It is a purchase, so it is not in the EC sales list. Before paying the CZK 200,000 of domestic suppliers, check that none is published as unreliable and that each account paid is the one published in the VAT register.

```oa-check
name: s.r.o. monthly return, May 2026
inputs:
  sales_21: 500000
  sales_12: 100000
  eu_service_in: 40000
  purchases_21: 200000
steps:
  - out_21: sales_21 * 0.21
  - out_12: sales_12 * 0.12
  - out_rc: eu_service_in * 0.21
  - line_62: out_21 + out_12 + out_rc
  - in_21: purchases_21 * 0.21
  - line_63: in_21 + out_rc
  - line_64: line_62 - line_63
expected:
  out_21: 105000
  out_12: 12000
  out_rc: 8400
  line_62: 125400
  line_63: 50400
  line_64: 75000
```

### Example 2: OSVČ crosses both thresholds in 2026

A Czech sole trader (OSVČ), not yet a payer, has domestic turnover of CZK 1,950,000 from 1 January to 31 August 2026.

1. On 10 September 2026 she invoices CZK 300,000. Turnover is now CZK 2,250,000: over CZK 2,000,000 by CZK 250,000 and under CZK 2,536,500. She must apply within 10 working days, by Thursday 24 September 2026. Unless she elects otherwise in that application, she would be a payer from 1 January 2027 (§ 6(1)).
2. On 15 October 2026 she invoices CZK 400,000. Turnover is now CZK 2,650,000, over CZK 2,536,500 by CZK 113,500. She becomes a payer on 16 October 2026 (§ 6(2)(b)). She must file a new application within 10 working days of 15 October, even though she already applied (Finanční správa, 2025 information note).
3. The 15 October invoice itself carries no VAT: she was not yet a payer when she made it.
4. In November she invoices CZK 100,000 for services at 21%: VAT CZK 21,000.
5. She files monthly. She cannot choose quarters for 2026, nor for 2027 unless she asks the tax office by 31 October 2026 and it agrees for reasons deserving special consideration (§ 99a(3)). Her first return (16 to 31 October) and control statement are due on Wednesday 25 November 2026.
6. If the tax office later calls her for a missing control statement and she files it in the replacement period, the first such delay in the calendar year carries no fine (§ 101j). A second one costs CZK 10,000, halved to CZK 5,000 because she is a natural person (§ 101h(2)(a)).

Registration also ends the flat-rate income tax regime; see [cz-income-tax](cz-income-tax.md).

```oa-check
name: OSVČ crosses CZK 2,000,000 and CZK 2,536,500 in 2026
inputs:
  turnover_to_aug: 1950000
  sept_invoice: 300000
  oct_invoice: 400000
  nov_invoice: 100000
  kh_fine_full: 10000
steps:
  - after_sept: turnover_to_aug + sept_invoice
  - over_first: max(0, after_sept - 2000000)
  - over_second_sept: max(0, after_sept - 2536500)
  - after_oct: after_sept + oct_invoice
  - over_second: max(0, after_oct - 2536500)
  - nov_vat: nov_invoice * 0.21
  - kh_fine_second: kh_fine_full * 0.5
expected:
  after_sept: 2250000
  over_first: 250000
  over_second_sept: 0
  after_oct: 2650000
  over_second: 113500
  nov_vat: 21000
  kh_fine_second: 5000
```

## Ask the client first

1. Is the seat or an establishment in the Czech Republic? A non-established business has no threshold.
2. What is domestic turnover so far this calendar year, and on what dates were the large invoices issued? That fixes the day it becomes a payer.
3. Legal person or natural person? For an s.r.o., is there a single member who is a natural person? That sets the control statement deadline and halves the fines.
4. Monthly or quarterly, and what was prior-year turnover? Quarterly needs CZK 15,000,000 or less and no unreliable status.
5. Any exempt supplies (financial, insurance, property lettings)? If so, partial exemption applies and this skill stops.
6. Who are the main suppliers and how are they paid? Check the VAT register for unreliable status and published accounts.

## Sources

| Source | URL | Read on |
|---|---|---|
| Act No. 235/2004 Coll., VAT Act, version in force 1 January to 31 December 2026: §§ 4a, 6, 6c, 6f to 6l, 47, 64, 71i, 72, 73, 92a to 92f, 94, 94a, 96, 99, 99a, 101, 101a, 101c to 101k, 102, 106a, 108, 109, 109a; Annexes 2, 3, 5, 6 | https://e-sbirka.gov.cz/sb/2004/235/2026-01-01 | 2026-10-23 |
| Act No. 280/2009 Coll., Tax Code, version in force from 1 January 2026: §§ 33, 135, 136, 247a, 250, 251, 251a, 252 | https://e-sbirka.gov.cz/sb/2009/280/2026-01-01 | 2026-10-23 |
| Act No. 349/2023 Coll., public budget consolidation, Part on the VAT Act, point 5 (§ 47(1)(b): reduced rate 12% from 2024) | https://e-sbirka.gov.cz/sb/2023/349 | 2026-10-23 |
| Government Regulation No. 361/2014 Coll., temporary domestic reverse charge | https://e-sbirka.gov.cz/sb/2014/361 | 2026-10-23 |
| Government Regulation No. 351/2013 Coll., § 2 (late payment interest: repo plus 8 points) | https://e-sbirka.gov.cz/sb/2013/351 | 2026-10-23 |
| Finanční správa, Změny v plátcovství a registračním řízení DPH od 1. 1. 2025 (information note 11977/25) | https://financnisprava.gov.cz/assets/cs/prilohy/d-seznam-dani/11977_25_Informace_ke_zmenam_v_platcovstv2025.pdf | 2026-10-23 |
| Finanční správa, VAT return form 25 5401, specimen no. 26 (English) | https://financnisprava.gov.cz/assets/tiskopisy/5401-A_26.pdf | 2026-10-23 |
| Finanční správa, Control Statement Guidelines, valid from 1 January 2024 | https://financnisprava.gov.cz/assets/cs/prilohy/d-seznam-dani/Control_Statement_Guidelines_20240101.pdf | 2026-10-23 |
| Finanční správa, Kontrolní hlášení DPH | https://financnisprava.gov.cz/cs/dane/dane/dan-z-pridane-hodnoty/kontrolni-hlaseni-dph | 2026-10-23 |
| Finanční správa, Registr DPH (unreliable payers and published accounts) | https://adisspr.mfcr.cz/dpr/DphReg | 2026-10-23 |

Not yet confirmed:
- The control statement guidelines read are the version valid from 1 January 2024; no later version was listed on the Financial Administration page on 23 October 2026. The CZK 10,000 split comes from those guidelines, not from the Act.
- Whether the temporary domestic reverse charge under § 92f and Regulation 361/2014 continues after 31 December 2026. Czech law sets no end date (§ 92f and Regulation 361/2014 as in force on 23 October 2026 contain none), but its EU basis, Article 199a of the VAT Directive, is reported to run to 31 December 2026 under Directive (EU) 2022/890, with a Commission proposal of 1 October 2026 to extend it to 30 June 2030; both were seen only in secondary reports, as EUR-Lex could not be read. It does not affect tax year 2026.
- The cash-payment limit that triggers recipient liability under § 109(2)(c)(4) is set in a separate act, which was not read.
- The current Czech National Bank repo rate was not read; take it from the CNB for each half-year when computing interest.
