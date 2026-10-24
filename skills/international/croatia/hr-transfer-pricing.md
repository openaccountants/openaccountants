---
name: hr-transfer-pricing
description: "Use this skill for Croatian transfer pricing (transferne cijene) in tax year 2026. It covers who counts as a related person (Profit Tax Act art. 13(2) and General Tax Act art. 49), when purely domestic deals are caught (art. 13(5): tax-privileged party or losses carried forward), the arm's length rule and the five methods (art. 13(1) and (3)), documentation and the compensating adjustment (Profit Tax Rulebook art. 40), the PD-IPO related-party form filed with the PD return and its 2026 e-invoice carve-out, the Minister of Finance interest rate for related-party loans (2.65% for 2026), thin capitalisation (art. 8), APAs (art. 14.a and the APA rulebook fees), country-by-country reporting and fines. Trigger on: transfer pricing Croatia, transferne cijene, povezane osobe, PD-IPO, kamatna stopa povezane osobe 2026, prethodni sporazum o transfernim cijenama, CbCR Croatia. Out of scope: corporate tax in general (hr-corporate-income-tax), withholding and treaties in depth, VAT (croatia-vat-return)."
version: 0.1
jurisdiction: HR
tax_year: 2026
last_updated: 2026-10-23
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Croatia: transfer pricing (2026) v0.1

> **Source-cited draft.** No accountant has reviewed this skill yet. The law comes from the consolidated texts published by the Tax Administration (Porezna uprava) and from Narodne novine, all read on 23 October 2026. It prepares working papers; it is not authority to file or pay.

This is the transfer pricing (TP) skill for the Croatian pack. It links rather than repeats:

- Corporate profit tax, rates, the base and the PD return: [hr-corporate-income-tax](hr-corporate-income-tax.md).
- VAT: [croatia-vat-return](croatia-vat-return.md). Overview: [hr-tax-overview](hr-tax-overview.md).

The law is the Profit Tax Act (Zakon o porezu na dobit, "ZPD", consolidated text in force from 1 January 2026, last amended by NN 151/25), the Profit Tax Rulebook (Pravilnik o porezu na dobit, "Rulebook", consolidated text in force from 16 April 2026, last amended by NN 39/26) and the General Tax Act (Opći porezni zakon, "OPZ", in force from 1 January 2026). Currency: euro (EUR).

## Who this applies to

**Profit taxpayers that deal with related persons.** Profit tax is paid by companies and other resident persons that carry on business, by Croatian branches of foreign businesses, and by individuals who pay profit tax instead of income tax (ZPD art. 2(1) to (4)). The TP rule applies to them.

**Related persons (povezane osobe), ZPD art. 13(2).** One person takes part, directly or indirectly, in the management, supervision or capital of the other, or the same persons take part, directly or indirectly, in the management, supervision or capital of both. The Act sets no minimum percentage for this test.

**Wider test for the PD-IPO form.** For the PD-IPO form, related persons also include those under OPZ art. 49 (Rulebook art. 47.b(1)). OPZ art. 49 covers persons that form one risk because one controls or has significant influence over the other, persons whose finances are so linked that losses, profits or solvency can pass between them, and persons that carry on business in the same premises with the same equipment. It also covers the taxpayer's spouse, relatives in the direct line, collateral relatives to the fourth degree and in-laws to the same degree, adoptive relations, guardians and people living in the same household (OPZ art. 49(1) and (2)).

**Cross-border deals are always in. Domestic deals are in only in two cases.** Art. 13 sits under the heading "tax base in dealings between related persons, resident and non-resident". It applies to two related residents only where one of them (ZPD art. 13(5)):

1. has a privileged tax status, meaning it pays profit tax at a rate below the prescribed rate or is exempt; or
2. has the right, in that tax period, to carry forward a tax loss from earlier periods.

The same two cases bring domestic related-party loans under the interest rule in art. 14 (ZPD art. 14(5); Rulebook art. 37(3)). Separately, OPZ art. 49(3) says contracts between related persons are recognised for tax only if unrelated persons would have agreed the same terms in the same or similar circumstances.

**Permanent establishments.** The profit of a non-resident's Croatian branch is the profit it would earn as a separate and independent company doing the same business, taking account of functions, assets and risks (ZPD art. 15(2); OPZ art. 50). The Tax Administration applies the OECD Authorised Approach of 2010 ([Transferne cijene page](https://porezna-uprava.gov.hr/hr/transferne-cijene/3993)).

## Rates, bands and thresholds

| Item | Rate or amount | Year | Source URL |
|---|---|---|---|
| Profit tax rate, revenue up to EUR 1,000,000 in the period | 10% | 2026 | https://porezna-uprava.gov.hr/hr_propisi/_layouts/15/in2.vuk2019.sp.propisi.intranet/propisi.aspx#id=pro19 (ZPD art. 28) |
| Profit tax rate, revenue above EUR 1,000,000 in the period | 18% | 2026 | https://porezna-uprava.gov.hr/hr_propisi/_layouts/15/in2.vuk2019.sp.propisi.intranet/propisi.aspx#id=pro19 (ZPD art. 28) |
| Interest rate on loans between related persons (minimum on loans given, maximum on loans received) | 2.65% | 2026 | https://narodne-novine.nn.hr/clanci/sluzbeni/2025_12_150_2236.html |
| How that rate is set | average of the ECB main refinancing rate published by the Croatian National Bank in the current year, published before the tax period | 2026 | https://porezna-uprava.gov.hr/hr_propisi/_layouts/15/in2.vuk2019.sp.propisi.intranet/propisi.aspx#id=pro23 (Rulebook art. 37(1) and (2)) |
| Thin capitalisation: shareholder holding | at least 25% of shares, capital or votes | 2026 | https://porezna-uprava.gov.hr/hr_propisi/_layouts/15/in2.vuk2019.sp.propisi.intranet/propisi.aspx#id=pro19 (ZPD art. 8(1)) |
| Thin capitalisation: loans above which interest is not deductible | 4 times the shareholder's share of capital (paid-in capital, retained earnings and reserves, monthly average) | 2026 | https://porezna-uprava.gov.hr/hr_propisi/_layouts/15/in2.vuk2019.sp.propisi.intranet/propisi.aspx#id=pro19 (ZPD art. 8(1) and (3)) |
| Interest limitation on exceeding borrowing costs | 30% of tax EBITDA or EUR 3,000,000, whichever is higher | 2026 | https://porezna-uprava.gov.hr/hr_propisi/_layouts/15/in2.vuk2019.sp.propisi.intranet/propisi.aspx#id=pro19 (ZPD art. 30.a(1)) |
| PD-IPO: small loans to one related person at one rate may be shown as one total | up to EUR 20,000 in the period | 2026 | https://porezna-uprava.gov.hr/hr_propisi/_layouts/15/in2.vuk2019.sp.propisi.intranet/propisi.aspx#id=pro23 (Rulebook art. 47.b(4)) |
| APA fee, unilateral: revenue on the last return up to EUR 398,168.43, or a business started in the current period | EUR 1,990.84 | 2026 | https://porezna-uprava.gov.hr/hr_propisi/_layouts/15/in2.vuk2019.sp.propisi.intranet/propisi.aspx#id=pro1721 (APA Rulebook art. 15(2)) |
| APA fee, unilateral: revenue EUR 398,168.43 to EUR 2,654,456.17 | EUR 3,981.68 | 2026 | https://porezna-uprava.gov.hr/hr_propisi/_layouts/15/in2.vuk2019.sp.propisi.intranet/propisi.aspx#id=pro1721 (APA Rulebook art. 15(2)) |
| APA fee, unilateral: revenue above EUR 2,654,456.17 | EUR 6,636.14 | 2026 | https://porezna-uprava.gov.hr/hr_propisi/_layouts/15/in2.vuk2019.sp.propisi.intranet/propisi.aspx#id=pro1721 (APA Rulebook art. 15(2)) |
| APA fee add-on: bilateral / multilateral | plus EUR 6,636.14 / plus EUR 13,272.28 | 2026 | https://porezna-uprava.gov.hr/hr_propisi/_layouts/15/in2.vuk2019.sp.propisi.intranet/propisi.aspx#id=pro1721 (APA Rulebook art. 15(3) and (4)) |
| APA term | up to 5 years | 2026 | https://porezna-uprava.gov.hr/hr_propisi/_layouts/15/in2.vuk2019.sp.propisi.intranet/propisi.aspx#id=pro1721 (APA Rulebook art. 12(1)) |
| Country-by-country report: group consolidated revenue in the prior year | more than EUR 750,000,000 | 2026 | https://porezna-uprava.gov.hr/Propisi (Administrative Cooperation Act art. 35(1)) |
| Fine: failing to determine the tax base under the Act (legal person) | EUR 260 to EUR 26,540 (responsible person EUR 260 to EUR 2,650) | 2026 | https://porezna-uprava.gov.hr/hr_propisi/_layouts/15/in2.vuk2019.sp.propisi.intranet/propisi.aspx#id=pro19 (ZPD art. 38(1)(1) and (2)) |
| Fine: not attaching required documents to the return, or not giving data or documents on request (legal person) | EUR 660 to EUR 39,810 | 2026 | https://porezna-uprava.gov.hr/Propisi (OPZ art. 193(1)(10), (14), (16)) |
| Fine: not presenting books and records on request, or refusing a tax audit (legal person) | EUR 2,650 to EUR 66,360 | 2026 | https://porezna-uprava.gov.hr/Propisi (OPZ art. 192(1)(10), (12)) |
| Fine: CbC report or notice not filed, late, incomplete or wrong (legal person) | EUR 260 to EUR 26,540 | 2026 | https://porezna-uprava.gov.hr/Propisi (Administrative Cooperation Act art. 66(1)(2)) |
| Time limit to assess tax | 6 years from the end of the year the liability arose | 2026 | https://porezna-uprava.gov.hr/Propisi (OPZ art. 108(1) and (2)) |

The `propisi.aspx#id=pro` links are the Tax Administration's own links to its consolidated texts: pro19 is the ZPD, pro23 the Rulebook and pro1721 the APA Rulebook. The OPZ (under "Porezni postupak") and the Administrative Cooperation Act (under "Administrativna suradnja") are in the same register at https://porezna-uprava.gov.hr/Propisi.

## The taxable base

**The adjustment.** If related persons agree prices or other terms that differ from what unrelated persons would agree, the taxpayer adjusts its base to the profit it would have made between unrelated persons (ZPD art. 13(1)). The adjustment then bears tax at the taxpayer's normal rate: 10% or 18% depending on revenue (art. 28). An upward adjustment does not add to revenue, so it does not by itself move a company from 10% to 18%.

**Methods (ZPD art. 13(3); Rulebook art. 40(1) to (4)).**

- Traditional transaction methods: comparable uncontrolled price, resale price, cost plus.
- Transactional profit methods: profit split, transactional net margin.
- Pick the most appropriate method for the case. Weigh each method's strengths and weaknesses, the functional analysis, the data available and how comparable the transactions are.
- Where a traditional method and a profit method are equally reliable, use the traditional method. Where CUP and another method are equally reliable, use CUP.
- Another method is allowed only if the five do not fit the facts, and the file must say why.
- The OECD Transfer Pricing Guidelines are used to interpret the Croatian rules (Rulebook art. 40(12)).

**Interest on related-party loans (ZPD art. 14; Rulebook art. 37).**

- On a loan **given** to a related person, the lender books interest at least at the arm's length rate when the loan was granted (art. 14(1)).
- On a loan **received** from a related person, interest is deductible only up to that rate (art. 14(2)).
- The Minister of Finance publishes the rate before the tax period (art. 14(3)). For 2026 it is **2.65%** (NN 150/2025).
- A taxpayer may instead set the rate under art. 13 (a benchmarked arm's length rate), but only if it does so for all its loan contracts (art. 14(4); Rulebook art. 37(4)).
- If withholding tax is paid on the interest, the non-deductible interest is reduced in proportion to the withholding tax paid (Rulebook art. 37(5)).
- The interest add-back goes on line 16 of the PD return ("interest between related persons"); thin capitalisation interest goes on line 15 (Rulebook art. 47(3)).

**Thin capitalisation (ZPD art. 8; Rulebook art. 32).** Interest on loans from a shareholder holding at least 25% of shares, capital or votes is not deductible on the part of the loans that at any time in the period exceeds 4 times that shareholder's share of capital. Loans from third parties guaranteed by the shareholder and loans from related persons count as shareholder loans (art. 8(2)). Loans from banks and other financial organisations do not (art. 8(1); Rulebook art. 32(4)). The shareholder's share of capital is measured on the last day of each month the loan is used (Rulebook art. 32(2)). No add-back arises where the interest is charged by a domestic profit taxpayer, or where income tax on capital is paid on the interest (Rulebook art. 32(5) and (6)). In practice the rule bites on loans from foreign shareholders and their related persons.

**Default interest between related persons** is never deductible (ZPD art. 7(1)(8); Rulebook art. 29), whoever charged it.

**Order of the interest rules.** Interest the taxpayer already added back under art. 8 or art. 14 reduces the amount it must add back under the 30% EBITDA limit (ZPD art. 30.a(11)).

**Compensating adjustment (Rulebook art. 40(8) to (11)).**

- Before or at the time of the transaction, the taxpayer must document reasonable efforts to set an arm's length price on the information it then had (art. 40(8)).
- If at the end of the period the price turns out not to be arm's length, the taxpayer must make a compensating adjustment (art. 40(9)).
- It must be made before the return is filed, and the taxpayer must explain with the return why the original price missed (art. 40(10)).
- A self-adjustment does not stop the Tax Administration adjusting again in an audit, and does not affect a mutual agreement procedure (art. 40(11)).

## Deadlines and filing

**PD return.** Filed electronically within 4 months after the end of the tax period, so by 30 April 2027 for calendar 2026. Tax shown as due is payable by the same date (ZPD art. 35(1) to (3)).

**PD-IPO form (Izvješće o poslovnim događajima s povezanim osobama).** It is filed with the PD return (Rulebook art. 46(2)) whenever the books record business events with related persons in the period (art. 47.b(1)). It has four parts (art. 47.b(2)):

- I.1 liabilities to related persons from loans and credits received;
- I.2 receivables from related persons from loans and credits given;
- II.1 liabilities to related persons from purchases of goods and services;
- II.2 receivables from related persons from supplies of goods and services.

Each row names the related person, its OIB (or VAT ID or tax number), seat and country. It is marked **P** where either party has privileged tax status and **G** where either party may carry forward a loss (art. 13(5)). The loan parts also show the holding in capital and votes, the other basis of the relationship, balances, the interest rate, interest above the published rate (art. 14) and interest on loans above 4 times capital (art. 8). Amounts are in euros and cents (art. 47.b(6)).

**New for 2026 returns: e-invoice carve-out.** A taxpayer within the e-invoice fiscalisation regime does not report in parts II.1 and II.2 the business events shown in e-invoices with domestic related persons that are also within that regime (Rulebook art. 47.b(5), added by NN 39/26). It applies to tax periods starting on or after 1 January 2026 that do not end before 31 December 2026, and it does not apply to a taxpayer that, in its period starting on or after 1 January 2026, is not both an issuer and a recipient of e-invoices (NN 39/26 art. 11(4) and (5)). Loans (parts I.1 and I.2) and foreign related persons are still reported.

**Documentation.** It is not filed with the return. The taxpayer must hold it and hand it over when the Tax Administration asks ([Transferne cijene page](https://porezna-uprava.gov.hr/hr/transferne-cijene/3993)). Related-party dealings are recognised only if the taxpayer holds, and on request provides, data on the related persons, the dealings, the methods used, why they were chosen and how the adjustment was made (ZPD art. 13(4)). The content follows the OECD master file and local file (Rulebook art. 40(6)):

- **Group (master file):** ownership and organisation; business and main activities, supply chain, the 5 main products or services and any other above 5% of revenue, intra-group service contracts, markets, a short functional analysis, restructurings; intangibles and the TP policy for them; group financing and its TP policy; consolidated accounts and existing APAs.
- **Local company (local file):** management structure, business and strategy, local market position; each material controlled transaction with amounts by category and by country, and the list of related companies dealt with; intra-group contracts; comparability and functional analysis; the method per category with all calculations and the comparables used; the annual accounts (other than the balance sheet and profit and loss account already filed with FINA).

Documentation from earlier years that is relied on must be updated for material changes (art. 40(7)). The Act and the Rulebook set no revenue or transaction-value threshold below which documentation is not needed, and no deadline for producing it after a request.

**Advance pricing agreement (prethodni sporazum o transfernim cijenama), ZPD art. 14.a and the APA Rulebook (NN 42/17, 156/22).**

- Unilateral, bilateral or multilateral, with the Tax Administration and, for bilateral and multilateral, the other states' authorities (art. 14.a(1)).
- It covers transactions before they start, and, where commercially justified, transactions already under way. It binds both the taxpayer and the Tax Administration for its term (art. 14.a(1) and (2)).
- Start with an initial written statement sent to sporazum.tc@porezna-uprava.hr ([APA page](https://porezna-uprava.gov.hr/hr/prethodni-sporazum-o-transfernim-cijenama/3971)). Send it at least 6 months before the transaction starts (APA Rulebook art. 5(1) and (3)).
- If the Tax Administration sees merit, it holds a preliminary meeting. After a positive assessment the taxpayer files the formal statement of intent with the full documents (APA Rulebook arts. 6, 7(3) and 8).
- A person not yet registered for profit tax can apply, if it registers by the date the APA is signed (art. 5(2)).
- The fee is paid when the formal statement of intent under art. 8 is filed, not with the initial statement. The revenue band is read from the last profit tax return. Half of the fee is refunded if the taxpayer withdraws after filing, and a renewal costs half (art. 15(1), (2), (7), (8)). Fees are in the table above.
- Term up to 5 years; a renewal application may be filed 6 months before expiry (art. 12(1) and (4)). An annual report on how the APA was applied is due by the PD return deadline (art. 11(3)).

**Country-by-country reporting (Administrative Cooperation Act art. 35; Rulebook on automatic exchange art. 107).**

- Applies to groups with consolidated revenue above EUR 750 million in the prior year.
- The CbC report (form MNP-CbCr) is due within 12 months after the end of the reporting year (art. 35(1)).
- Every Croatian constituent entity notifies the Tax Administration whether it is the ultimate parent, surrogate parent or another constituent entity, and who files the report. The notice is due within 4 months after the end of the profit tax period (art. 35(2) and (3); [CbCr page](https://porezna-uprava.gov.hr/hr/izvjesca-po-drzavama-cbcr/4522)).

## Penalties and interest

- **Extra tax.** An audit adjustment raises the base, and tax follows at 10% or 18% (ZPD art. 13(1), art. 28). The Croatian rules read set no percentage surcharge on TP adjustments.
- **Late payment interest.** Where an audit finds more tax due, interest runs from the day the taxpayer should have paid it (OPZ art. 130(7)), so from the original PD due date. The rate is set by a separate law (OPZ art. 130(1)); see "Not yet confirmed".
- **Misdemeanour fines.** These are ranges a court or the Tax Administration sets case by case:
  - Not determining the tax base as the Act requires: EUR 260 to EUR 26,540 for the company and EUR 260 to EUR 2,650 for the responsible person. A repeat offence costs EUR 390 to EUR 39,810 and EUR 390 to EUR 3,980 (ZPD art. 38(1) to (3)).
  - Not attaching the documents the tax rules require to the return (for example, PD-IPO), or not giving data or documents on request: EUR 660 to EUR 39,810 for the company and EUR 390 to EUR 3,980 for the responsible person (OPZ art. 193(1)(10), (14), (16) and (4)).
  - Not presenting books, records and business documents on request, or not allowing an audit: EUR 2,650 to EUR 66,360 for the company and EUR 660 to EUR 5,300 for the responsible person (OPZ art. 192(1)(10), (12) and (4)).
  - CbC report or notice not filed, late, incomplete or wrong: EUR 260 to EUR 26,540 for the company and EUR 260 to EUR 2,650 for the responsible person (Administrative Cooperation Act art. 66(1)(2) and (2)).
- **Time limits.** The right to assess tax and interest lapses 6 years after the year-end in which the liability arose (OPZ art. 108(1) and (2)). An audit normally must start within 3 years of that date. Audits of related persons, cross-border transactions and transfer prices may start at any time before the 6-year period ends (OPZ art. 117(2) and (3)(5)).

## Cross-border points

- **Treaties and double taxation.** Croatia makes a corresponding adjustment where it accepts that the adjusted profit is arm's length, whether or not the treaty has Article 9(2) of the OECD Model. MAP requests on TP or branch profit go to map-hr@porezna-uprava.hr ([Transferne cijene page](https://porezna-uprava.gov.hr/hr/transferne-cijene/3993)).
- **Withholding on interest.** Interest paid to a foreign legal person bears 15% withholding tax, unless it is on a trade credit for goods, a loan from a foreign bank or financial institution, or bonds (ZPD art. 31(4) to (6)). It is 25% where the recipient is in an EU-listed non-cooperative jurisdiction with no treaty (art. 31(12)). The TP interest add-back is reduced in proportion to the withholding tax paid (Rulebook art. 37(5)). Treaty and EU directive relief is outside this skill.
- **Who triggers PD-IPO.** Any related person, domestic or foreign. Foreign related persons are always reported in full. The 2026 e-invoice carve-out covers only domestic related persons inside the e-invoice regime.
- **Branches.** Profit attribution follows ZPD art. 15 and OPZ art. 50, using the OECD Authorised Approach.

## Worked examples

### Example 1: interest-free loan to a foreign subsidiary

A Croatian d.o.o. with 2026 revenue of EUR 3,000,000 lends EUR 400,000 to its Slovenian subsidiary on 1 January 2026, interest free, outstanding all year. It does not benchmark loans under art. 13, so the published rate applies.

1. Minimum interest it must book for tax: 2.65% of EUR 400,000 = EUR 10,600 (ZPD art. 14(1); NN 150/2025).
2. It booked nothing, so the base rises by EUR 10,600.
3. Revenue is above EUR 1,000,000, so the rate is 18% (art. 28). Extra tax: EUR 1,908.
4. The loan goes in part I.2 of PD-IPO, with the base increase for interest under art. 14 (Rulebook art. 47.b(2)). The Slovenian company is foreign, so the e-invoice carve-out does not apply.

```oa-check
name: Interest-free loan EUR 400,000 to a foreign subsidiary (2026 rate 2.65%)
inputs:
  loan: 400000
  rate_pct: 2.65
  booked_interest: 0
  cit_rate: 18
steps:
  - minimum_interest: loan * rate_pct / 100
  - base_increase: minimum_interest - booked_interest
  - extra_tax: base_increase * cit_rate / 100
expected:
  minimum_interest: 10600
  base_increase: 10600
  extra_tax: 1908
```

### Example 2: domestic service fee caught because the supplier has losses

Company A, a Croatian d.o.o. with 2026 revenue of EUR 800,000, buys management services from its Croatian sister company B for EUR 120,000. B has tax losses from earlier years that it may carry forward in 2026. Both are domestic, but art. 13 applies because one party can carry forward a loss (ZPD art. 13(5)(2)). In an audit the Tax Administration shows, using cost plus, that the arm's length fee is EUR 70,000.

1. Adjustment to A's base: EUR 120,000 minus EUR 70,000 = EUR 50,000 (art. 13(1)).
2. A's revenue is EUR 800,000, up to EUR 1,000,000, so the rate is 10% (art. 28). The adjustment does not change revenue. Extra tax: EUR 5,000.
3. Late payment interest on EUR 5,000 runs from the original 2026 PD due date, 30 April 2027 (OPZ art. 130(7)). The rate is not computed here.
4. A fine of EUR 260 to EUR 26,540 may follow for not determining the base as the Act requires (ZPD art. 38(1)(1)).
5. Had A made the cut itself as a compensating adjustment before filing, with the explanation the Rulebook requires, the extra tax would be the same, but no audit finding would arise (Rulebook art. 40(9) and (10)).
6. PD-IPO: A reports B in part II.1, marked G (B may carry forward a loss). If both A and B are in the e-invoice regime and the fee was invoiced by e-invoice, part II.1 leaves this purchase out (Rulebook art. 47.b(5)). Art. 13 still applies.

```oa-check
name: Domestic management fee cut from EUR 120,000 to EUR 70,000 (supplier has losses, 10% rate)
inputs:
  fee_paid: 120000
  arm_length_fee: 70000
  revenue: 800000
  rate_threshold: 1000000
  cit_rate: 10
steps:
  - adjustment: fee_paid - arm_length_fee
  - headroom_below_threshold: rate_threshold - revenue
  - extra_tax: adjustment * cit_rate / 100
expected:
  adjustment: 50000
  headroom_below_threshold: 200000
  extra_tax: 5000
```

## Ask the client first

1. Who the related persons are: the ownership chain (direct and indirect), shared managers or supervisory board members, and any family links under OPZ art. 49.
2. Whether each related person is Croatian or foreign, and for domestic ones, whether either party pays tax below the normal rate, is exempt, or may carry forward a loss in 2026.
3. Each related-party transaction in 2026 by type and amount: goods, services, royalties, loans (balances, rates, dates granted) and guarantees.
4. Whether loans are priced at the published 2.65% or benchmarked under art. 13, and the shareholder's capital, retained earnings and reserves for the 4 times test.
5. Whether the company and its domestic related persons are in the e-invoice fiscalisation regime and invoice each other by e-invoice.
6. Whether a master file or local file exists, whether the group's consolidated revenue exceeds EUR 750 million, and whether an APA, MAP or tax audit is open.

## Sources

| Source | URL | Read on |
|---|---|---|
| Zakon o porezu na dobit, consolidated text in force from 1 January 2026 (NN 177/04 to 151/25), arts. 2, 7, 8, 13, 14, 14.a, 15, 28, 30.a, 31, 35, 38 | https://porezna-uprava.gov.hr/hr_propisi/_layouts/15/in2.vuk2019.sp.propisi.intranet/propisi.aspx#id=pro19 | 2026-10-23 |
| Pravilnik o porezu na dobit, consolidated text in force from 16 April 2026 (NN 95/05 to 39/26), arts. 29, 32, 37, 40, 46, 47, 47.b | https://porezna-uprava.gov.hr/hr_propisi/_layouts/15/in2.vuk2019.sp.propisi.intranet/propisi.aspx#id=pro23 | 2026-10-23 |
| Pravilnik o izmjenama i dopunama Pravilnika o porezu na dobit, NN 39/2026 (art. 47.b(5) and application from 2026 returns) | https://narodne-novine.nn.hr/clanci/sluzbeni/2026_04_39_469.html | 2026-10-23 |
| Odluka o objavi kamatne stope na zajmove između povezanih osoba, NN 150/2025 (2.65% for 2026) | https://narodne-novine.nn.hr/clanci/sluzbeni/2025_12_150_2236.html | 2026-10-23 |
| Pravilnik o postupku sklapanja prethodnog sporazuma o transfernim cijenama, consolidated (NN 42/17, 156/22), arts. 5, 11, 12, 15 | https://porezna-uprava.gov.hr/hr_propisi/_layouts/15/in2.vuk2019.sp.propisi.intranet/propisi.aspx#id=pro1721 | 2026-10-23 |
| Opći porezni zakon, consolidated text in force from 1 January 2026 (NN 115/16 to 151/25), arts. 49, 50, 108, 117, 130, 192, 193 | https://porezna-uprava.gov.hr/Propisi | 2026-10-23 |
| Hrvatska narodna banka, ECB main refinancing rate in force on 1 July 2026 (2.40%), NN 68/2026 | https://narodne-novine.nn.hr/clanci/sluzbeni/2026_06_68_826.html | 2026-10-23 |
| Zakon o administrativnoj suradnji u području poreza, consolidated (NN 115/16 to 146/25), arts. 34, 35, 66 | https://porezna-uprava.gov.hr/Propisi | 2026-10-23 |
| Porezna uprava, Transferne cijene (methods, documentation on request, MAP, AOA) | https://porezna-uprava.gov.hr/hr/transferne-cijene/3993 | 2026-10-23 |
| Porezna uprava, Prethodni sporazum o transfernim cijenama | https://porezna-uprava.gov.hr/hr/prethodni-sporazum-o-transfernim-cijenama/3971 | 2026-10-23 |
| Porezna uprava, Izvješća po državama (CbCr) | https://porezna-uprava.gov.hr/hr/izvjesca-po-drzavama-cbcr/4522 | 2026-10-23 |

Not yet confirmed: the late payment interest rate on tax debts for 2026. OPZ art. 130(1) points to a separate law. The Tax Administration's register lists the Zakon o kamatama (NN 94/04, kept in force by the Obligations Act art. 1164), which treats taxes as money obligations (art. 1(2)), and the Croatian National Bank published, under Obligations Act art. 29(9), an ECB rate of 2.40% in force on 1 July 2026 (NN 68/2026). The provision that sets the margin over that rate for tax debts was not read, so no rate is given; whether the Tax Administration expects a corresponding downward adjustment by the domestic counterparty in a case like Example 2; how Rulebook art. 37(5) computes the proportional reduction for withholding tax; any time limit for producing documentation after a request; and the content of the Tax Administration's TP audit manual (Priručnik za nadzor transfernih cijena), which was not read.

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
