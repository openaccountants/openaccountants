---
name: si-cross-border
description: "Hub skill for crossing the Slovenian border in tax year 2026. Covers tax residence of individuals (registered permanent residence, habitual abode or centre of interests, more than 183 days; ZDoh-2 arts. 6 and 7) and companies (seat or place of effective management; ZDDPO-2 art. 5); permanent establishment (art. 6 and 7); non-residents taxed on Slovenian-source income; 15% withholding on dividends, interest, royalties, Slovenian rent, artists' fees and listed services paid to listed jurisdictions (ZDDPO-2 art. 70); EU directive exemptions (arts. 71 and 72); treaty relief on the KIDO forms; the foreign tax credit; corporate exit tax with five-year instalments (arts. 54.a and 54.b); the 7% relief for new residents. Corporate rate 22% for 2024 to 2028. Trigger on: moving to Slovenia, leaving Slovenia, non-resident, davčni odtegljaj, KIDO, izstopna obdavčitev. Out of scope: slovenia-income-tax, si-corporate-income-tax, slovenia-payroll, slovenia-social-contributions, slovenia-vat-return."
jurisdiction: SI
category: international
tax_year: 2026
tier: 2
last_updated: 2026-10-23
version: 0.1
verified_by: pending
trust_label: Built by Michael Cutajar and the OpenAccountants team
---

# Slovenia: cross-border tax for people and companies (2026) v0.1

> **Source-cited draft.** No accountant has reviewed this skill yet. Every figure below comes from the Corporate Income Tax Act (ZDDPO-2), the Personal Income Tax Act (ZDoh-2) and the Tax Procedure Act (ZDavP-2) as consolidated on pisrs.si, and from guidance of the Financial Administration (FURS) on fu.gov.si, all read on 23 October 2026. It prepares working papers; it is not authority to file or pay.

This is the hub for the Slovenian cross-border (XB) domain. It links rather than repeats:

- Individual income tax, the annual scale and allowances: [slovenia-income-tax](slovenia-income-tax.md).
- Corporate income tax: [si-corporate-income-tax](si-corporate-income-tax.md).
- Payroll withholding: [slovenia-payroll](slovenia-payroll.md). Social contributions: [slovenia-social-contributions](slovenia-social-contributions.md).
- VAT: [slovenia-vat-return](slovenia-vat-return.md). Overview: [si-tax-overview](si-tax-overview.md). Entity choice: [si-company-formation](si-company-formation.md).

Those skills still carry 2025 figures. Where they differ from this skill on a cross-border point, this skill reflects the law as read on 23 October 2026.

Tax year: the calendar year for individuals. A company may use a business year of up to 12 months (FURS, CIT computation guidance). Currency: euro. Authority: Finančna uprava Republike Slovenije (FURS).

## Who this applies to

**Individuals.** A person is a Slovenian tax resident at any time in the tax year in which they meet any one of these tests (ZDoh-2 art. 6):

- an officially registered permanent residence (stalno prebivališče) in Slovenia;
- habitual abode, or the centre of personal and economic interests, in Slovenia;
- presence in Slovenia for more than 183 days in total in the tax year;
- certain diplomatic and EU-institution postings abroad.

A resident is taxed on worldwide income. A non-resident is taxed on Slovenian-source income only (ZDoh-2 art. 5).

Some people are non-residents even though they meet a test (ZDoh-2 art. 7(1)):

- foreign diplomats and consular staff, and staff of international organisations and EU institutions, who are not Slovenian citizens;
- a foreign expert in a shortage occupation who was not resident in the previous 5 years, owns no Slovenian property and stays less than 365 days in two consecutive tax years. FURS must confirm this status in writing (art. 7(3));
- a person in Slovenia only to study or for medical treatment.

**Treaty override.** A person who is resident under art. 6 but is resident only of the other state under a Slovenian tax treaty is a non-resident for that period (ZDoh-2 art. 7(2)). FURS applies the treaty tie-breaker when the person files a residence questionnaire with a certificate of residence from the other state ([FURS, Tax obligations on leaving Slovenia](https://www.fu.gov.si/fileadmin/Internet/Davki_in_druge_dajatve/Podrocja/Mednarodno_obdavcenje/Opis/Davcne_obveznosti_Slovencev_ob_odhodu_iz_Slovenije.docx)).

**Part year.** In the year a person becomes or stops being resident, the allowances and the annual scale apply in proportion to the period of residence (ZDoh-2 art. 121).

**Companies.** A company is resident if it has its seat in Slovenia or its place of effective management there. The place of effective management is where the key management and commercial decisions are taken (ZDDPO-2 art. 5). A resident is taxed on worldwide income; a non-resident on Slovenian-source income only (art. 4). A foreign partnership without legal personality that is not taxed under ZDoh-2 is also a corporate taxpayer (art. 3(2)).

**Permanent establishment (poslovna enota).** A non-resident has a Slovenian PE where it carries on business in or through a place in Slovenia (ZDDPO-2 art. 6). It includes:

- an office, branch, factory, workshop, mine or quarry;
- a building site or construction, assembly or installation project, or supervision of one, lasting **more than 6 months**. It is a PE from the first day, preparatory work included (art. 6(2) and (5));
- a dependent agent who habitually concludes contracts, or plays the principal role in concluding contracts routinely signed without material change (art. 6(3));
- an agent acting in its own name exclusively or almost exclusively for closely related non-residents (art. 6(4)).

Storage, display, delivery, purchasing and information gathering are not a PE if they are preparatory or auxiliary. The exemption does not apply where closely related persons split a cohesive business between places (art. 7). "Closely related" includes more than 50% ownership (art. 7(4)).

A foreign company that does business in Slovenia must register for tax on form DR-04 before it starts. A foreign sole trader uses DR-03 ([FURS, Permanent establishment of a non-resident, March 2026](https://www.fu.gov.si/fileadmin/Internet/Davki_in_druge_dajatve/Podrocja/Mednarodno_obdavcenje/Opis/Stalna_poslovna_enota_nerezidenta.docx)).

## Rates, bands and thresholds

| Item | Rate or amount | Year | Source |
|---|---|---|---|
| Corporate income tax, general rate (also on PE profits and on exit gains) | 22% (ZDDPO-2 art. 60 says 19%; ZORZFS art. 64 overrides it for 2024 to 2028) | 2024 to 2028 | [ZDDPO-2 art. 60 with note](https://pisrs.si/pregledPredpisa?id=ZAKO4687); [FURS letter 0920-542/2024-2](https://www.fu.gov.si/fileadmin/Internet/Davki_in_druge_dajatve/Poslovanje_z_nami/Novodila_in_pojasnila/2024/0920-542_2024-2_Odgovor_na_vase_vprasanje_-_sprememba_davcne_stopnje_DDPO.docx) |
| Business year straddling a rate change | Weighted by months in each calendar year | 2024 onward | FURS letter 0920-542/2024-2 |
| Withholding tax on Slovenian-source payments under art. 70 (see the list below) | 15% of each payment | 2026 | [ZDDPO-2 art. 70(1)](https://pisrs.si/pregledPredpisa?id=ZAKO4687) |
| Services caught by withholding | Consulting, marketing, market research, recruitment, administration, IT and legal services, only when paid to a person seated or managed in a listed jurisdiction | 2026 | ZDDPO-2 art. 70(1)(6), art. 8.a(2) |
| Listed jurisdictions, first list (non-EU states with a corporate rate below 12.5%) | Bahamas, Barbados, Belize, Brunei, Costa Rica, Dominican Republic, Liberia, Liechtenstein, Maldives, Marshall Islands, Mauritius, Oman, Panama, Saint Kitts and Nevis, Saint Vincent and the Grenadines, Samoa, Seychelles, Uruguay, Vanuatu | Order of 28 February 2022, as published by FURS | [FURS, list under art. 8.a](https://www.fu.gov.si/fileadmin/Internet/Davki_in_druge_dajatve/Podrocja/Mednarodno_obdavcenje/Zakonodaja/Seznam_drzav_v_katerih_je_splosna_oziroma_povprecna_nominalna_stopnja_obdavcitve_dobicka_druzb_nizja_od_12_5_pri_tem_pa_to_niso_drzave_clanice_EU.pdf) |
| Listed jurisdictions, second list | The EU list of non-cooperative jurisdictions, as published in the Official Journal | as amended | ZDDPO-2 art. 8.a(2) |
| EU parent-subsidiary exemption from dividend withholding | Holding at least 10%, held at least 24 months (a bank guarantee covers the gap until month 24) | 2026 | ZDDPO-2 art. 71(1) and (3) |
| EU interest and royalties exemption | Direct holding at least 25% (either way, or a common parent), held at least 24 months, needs a FURS permit | 2026 | ZDDPO-2 art. 72(1) and (10) |
| Exit tax instalments | Up to 5 equal annual instalments for moves to the EU or to an EEA state with a recovery-assistance agreement | 2026 | ZDDPO-2 art. 54.b |
| Interest on deferred exit tax (company) | 2% a year, or the European Commission reference rate for state aid if higher on the decision date | 2026 | [ZDavP-2 arts. 370.a(2) and 104(2)](https://pisrs.si/pregledPredpisa?id=ZAKO4703) |
| Individuals: capital income (dividends, interest, capital gains) | 25% final; capital gains fall to 20% after 5 years and 15% after 10 years of holding; exempt after 15 years | 2026 | [ZDoh-2 arts. 132 and 96(1)](https://pisrs.si/pregledPredpisa?id=ZAKO4697) |
| Individuals: rental income | 25% final | 2026 | ZDoh-2 art. 135.č |
| Individuals: annual scale (before indexation) | 16% to 50% in five bands, top band over EUR 72,000; amounts indexed each year by ministerial notice | statutory | ZDoh-2 art. 122 |
| Relief for new residents | 7% of salary off the income tax, for up to 5 consecutive tax years | tax years from 2025 | ZDoh-2 art. 113.a |
| Allowances for EU and EEA residents | General, family and other allowances if Slovenian income is at least 90% of total taxable income | tax years from 2025 | ZDoh-2 art. 116 |
| Treaty claim decided by FURS (form lodged before payment) | Within 15 days | 2026 | ZDavP-2 art. 260(3) |
| Treaty refund claim (KIDO 9 to 11) | Within 5 years of the payment | 2026 | [FURS, Dividends, interest and royalties](https://www.fu.gov.si/fileadmin/Internet/Davki_in_druge_dajatve/Podrocja/Mednarodno_obdavcenje/Opis/Dividende_obresti_in_premozenjske_pravice.docx) |

**What art. 70 catches.** The 15% applies to Slovenian-source payments of the following (ZDDPO-2 art. 70(1)):

- dividends and dividend-like income (art. 74, which includes liquidation surpluses and hidden profit distributions to a 25% shareholder);
- interest. Exceptions include Slovenian government debt and interest paid by banks, but bank interest paid to a listed jurisdiction is caught;
- royalties, including software and know-how;
- rent for real estate in Slovenia;
- fees for artists' and sportsmen's services that accrue to another person;
- the listed services above, when paid to a listed jurisdiction.

No withholding applies to payments to the state, municipalities or the Bank of Slovenia. None applies to a resident, or to a Slovenian PE of a non-resident, that gives the payer its tax number (art. 70(2)).

**Withholding on dividends inside the EU and EEA, without the 10% test.** No tax is withheld on dividends to a company resident in another EU or EEA state if it cannot credit the Slovenian tax at home, for example because it exempts the dividend, and the transaction is not avoidance (art. 70(3)). Exempt EU and EEA pension funds, investment funds and insurers get similar relief on dividends and interest (art. 70(5)). Neither rule applies to states with no exchange of information (art. 70(7)).

## The taxable base

**Companies: residents.** Worldwide profit, worked out from the income statement as adjusted by ZDDPO-2 (arts. 12 and following). Corporate detail is in [si-corporate-income-tax](si-corporate-income-tax.md). Two cross-border rules sit in the base:

- **Dividends received** are excluded from the base if the payer is a Slovenian taxpayer, an EU company covered by the parent-subsidiary directive, or a company subject to comparable tax that is not resident in a listed jurisdiction (art. 24(1)). The exclusion is lost to the extent the payer deducted the payment (art. 24(4)).
- **Controlled foreign companies.** A foreign entity is a CFC where the Slovenian taxpayer, alone or with related persons, holds more than 50% of votes, capital or profit, and the entity actually paid less than half the Slovenian tax on its profit (art. 67.h). Its income is then taxed in Slovenia under arts. 67.i and 67.j.

**Companies: non-residents.**

- Profit of a Slovenian PE is taxed on a CIT return like a resident's (arts. 12 and 68(3)).
- Other Slovenian-source income is taxed only through withholding under art. 70 (art. 11).
- Source rules are in art. 8. Gains on Slovenian real estate are Slovenian-source. So are gains on shares of a company where more than half the value came from Slovenian real estate at any time in the 365 days before the sale (art. 8(10) and (14)).
- Services are Slovenian-source if performed in Slovenia or charged to a Slovenian resident or PE (art. 8(13)). Only the listed services paid to listed jurisdictions bear withholding.

The base for withholding is each gross payment (FURS, CIT computation guidance, section 3.0). A resident or PE that suffers withholding includes the gross income in its base and credits the tax withheld (art. 75).

**Individuals: residents.** Worldwide income, under the rules in [slovenia-income-tax](slovenia-income-tax.md). There is no remittance basis.

**Individuals: non-residents.** Slovenian-source income only (ZDoh-2 art. 5(2)):

- employment and services performed in Slovenia (art. 9);
- income paid by a Slovenian resident or PE, including dividends, interest, rent and royalties (art. 10);
- Slovenian real estate;
- securities and shares issued by Slovenian entities (art. 13).

A non-resident pays no Slovenian tax on (ZDoh-2 art. 33):

- capital gains on Slovenian shares, unless the holding was at least 10% at any time in the past 5 years;
- business income where there is no PE and less than 183 days' presence in any 12 months. Artists and sportsmen are excluded, and so is income under withholding;
- interest on Slovenian government bonds and on listed corporate bonds.

Tax paid by a non-resident during the year is final. There is no annual reconciliation as for residents ([FURS, International taxation of individuals, June 2025](https://www.fu.gov.si/fileadmin/Internet/Davki_in_druge_dajatve/Podrocja/Mednarodno_obdavcenje/Opis/Brosura_Mednarodna_obdavcitev_posameznikov.docx), section 2.5).

**Arriving: relief for new residents.** From tax year 2025, an employee gets a reduction of income tax equal to 7% of salary for up to 5 consecutive tax years. All of these must hold (ZDoh-2 art. 113.a):

- they are resident in Slovenia;
- they were not resident in the two tax years before starting work in Slovenia, and had no Slovenian employment or business income in that period;
- the employment contract guarantees salary of at least 2 times the latest average annual salary published by the Statistical Office, converted to a month;
- the employer is resident, or a non-resident with a Slovenian PE or branch that deducts the salary;
- they are under 40 on the start date;
- the employer test counts as met in a tax year if they are employed in Slovenia for at least 10 months of it.

**Leaving: individuals.** ZDoh-2 has no exit charge on individuals. A person who leaves for good becomes a non-resident when they cut all significant ties: they deregister permanent residence, move habitual abode and the centre of interests abroad, and spend no more than 183 days in Slovenia. They then regularise their status with FURS on the questionnaire "Ugotovitev rezidentskega statusa - odhod iz Republike Slovenije" (FURS, Tax obligations on leaving Slovenia, June 2025). Slovenian-source income stays taxable.

**Leaving: companies (exit tax, izstopna obdavčitev).** A company must disclose hidden reserves and add them to its base when (ZDDPO-2 art. 54.a(1)):

- it moves assets from Slovenia to its foreign PE and Slovenia loses the right to tax them;
- it moves assets from its Slovenian PE to its head office or to another PE abroad, with the same result;
- it moves its tax residence abroad. Assets that stay connected with a Slovenian PE are not caught;
- it moves the business of its Slovenian PE abroad.

The other rules in art. 54.a:

- Hidden reserves are fair value minus tax value at the time of transfer. A negative difference counts as nil (art. 54.a(2)).
- Short-term assets are not counted (art. 54.a(8)).
- Assets returning within 12 months are excluded if they were moved for securities financing, as collateral, or for prudential capital or liquidity (art. 54.a(9)).
- Assets arriving from another EU or EEA state take the value set by that state, unless that value is not arm's length (art. 54.a(10)).

## Deadlines and filing

- **CIT return (DDPO) for a resident or a non-resident's PE.** Filed on eDavki within 3 months after the end of the tax period: 31 March for a calendar year. Any balance is due within 30 days of filing. Advance payments (akontacije) are paid monthly if the annual advance exceeds EUR 400, otherwise quarterly. Each instalment falls due on the last day of its period and must be paid within 20 days ([FURS, CIT computation and payment, April 2026](https://www.fu.gov.si/fileadmin/Internet/Davki_in_druge_dajatve/Podrocja/Davek_od_dohodkov_pravnih_oseb/Opis/Obracunavanje_in_placevanje_davka_od_dohodkov_pravnih_oseb.docx)). A new taxpayer files a provisional computation within 8 days of registration.
- **Withholding tax.** The payer computes and withholds at the time of payment. It pays the tax and files the withholding return no later than **5 days after the payment**, and gives the recipient the same data (ZDavP-2 art. 374). FURS names the form ODO-1 (CIT computation guidance, section 3.0).
- **Treaty relief before payment.** The recipient gives the payer the claim form before the income is paid. The payer sends it to FURS, which decides within 15 days. The payer may apply the treaty rate only once FURS approves (ZDavP-2 art. 260). Each payment needs a new claim, but FURS may approve regular payments for a longer period (art. 260(5) and (6)). The forms are:
  - KIDO 1 for dividends;
  - KIDO 2 for interest;
  - KIDO 3 for royalties;
  - KIDO 5 for employment income;
  - other KIDO forms for other income types.
- **Treaty refund after payment.** The recipient claims the excess from FURS within 5 years of the payment (ZDavP-2 art. 262; FURS, Dividends, interest and royalties). The forms are:
  - KIDO 9 for dividends;
  - KIDO 10 for interest;
  - KIDO 11 for royalties.

  Evidence includes a register extract, proof of ownership and the loan or licence contract. Where an MLI-modified treaty has a 365-day holding test, the claim must include a statement that the test is met on the payment date.
- **EU directive relief.** The parent-subsidiary procedure is in ZDavP-2 art. 375. The interest and royalties exemption needs a FURS permit under art. 377. The art. 70(3) and (5) relief needs a declaration with a residence certificate. The payer keeps it for 10 years. The payer claims a refund within 5 years of paying the tax (ZDavP-2 art. 383.a).
- **Exit tax.** The hidden reserves are disclosed in the CIT return for the period of the move. If the company chooses instalments, it states the number, amounts, due dates and interest in that return. The first instalment is due 30 days after filing the return, and each later one a year after the previous one (ZDavP-2 art. 370.a(1) and (3)). FURS may require security (art. 370.a(4)). All remaining instalments fall due at once in these cases (art. 370.a(5)):
  - the assets or the PE business are sold;
  - they move again, or the residence moves, to a state outside the art. 54.b list;
  - the company goes bankrupt or stops trading;
  - an instalment is more than 12 months overdue.
- **Foreign tax credit evidence.** A company claims the credit in the CIT return on Annex 10 of the CIT return rules, with evidence from the foreign tax authority that the tax was paid ([FURS, Claiming credit or refund of foreign tax](https://www.fu.gov.si/fileadmin/Internet/Davki_in_druge_dajatve/Podrocja/Mednarodno_obdavcenje/Opis/Uveljavljanje_odbitka_oziroma_vracila_tujega_davka_pravnih_oseb_in_fizicnih_oseb_ki_opravljajo_dejavnost.docx)).

## Penalties and interest

- **Late payment interest (zamudne obresti).** Charged on tax not paid on time, at the rate set by the law on statutory default interest (ZDavP-2 art. 96(1)). A return or correction filed late carries interest from the payment due date (art. 95.a).
- **Failure to file or withhold (companies and sole traders).** These fines apply where a taxpayer fails to file a tax return or a withholding return on time and in the prescribed way. They also apply where a payer fails to compute, withhold or pay withholding tax (ZDavP-2 art. 397(1), points 1, 2 and 6):

  | Who | Fine |
  |---|---|
  | Legal person | EUR 1,200 to 15,000 |
  | Medium or large company | EUR 3,200 to 30,000 |
  | Sole trader | EUR 800 to 10,000 |
  | Responsible person of a legal person | EUR 600 to 4,000 (EUR 800 to 4,000 for a medium or large company) (art. 397(3)) |

- **Especially serious cases.** These are cases where unpaid tax could exceed EUR 10,000 for a legal person, or EUR 25,000 for a medium or large company (art. 398(1) and (4)):

  | Who | Fine |
  |---|---|
  | Legal person | EUR 4,500 to 100,000 |
  | Medium or large company | EUR 10,500 to 150,000 |

- **Individuals.** EUR 250 to 400 for not filing a tax declaration on time (ZDavP-2 art. 394).
- **Directive and treaty relief refused.** Arts. 24 and 71 do not apply to abusive arrangements whose main purpose is a tax advantage (ZDDPO-2 arts. 24(6) and 71(6)). Treaties modified by the MLI also carry a principal purpose test (FURS, Applying double tax treaties, September 2023).

## Cross-border points

- **Treaty network.** FURS publishes the list of treaties applied in 2026, with combined MLI texts ([FURS, list of treaties in force](https://www.fu.gov.si/fileadmin/Internet/Davki_in_druge_dajatve/Podrocja/Mednarodno_obdavcenje/Zakonodaja/Seznam_veljavnih_MP.docx)). The treaties with Australia (MP 13/24), New Zealand (MP 8/25) and Egypt (MP 16/10) are ratified but not yet applied. Read the treaty itself for the reduced rate; the domestic 15% applies until FURS approves the claim.
- **Foreign tax credit, companies.** A resident deducts foreign tax on foreign income included in its base (ZDDPO-2 art. 62). The credit is limited to the lower of two amounts, worked out country by country (art. 63):
  - the foreign tax finally and actually paid. For a treaty state this is capped at the treaty rate;
  - the Slovenian tax on that income.

  Excess credit cannot be carried to other countries or other years (arts. 66 and 67). Foreign tax paid in an earlier year on income already in the base can be refunded under the same limits (art. 62(2)).
- **Foreign tax credit, individuals.** The same lower-of rule applies, with the treaty rate as the cap (ZDoh-2 arts. 136 and 137). Excess credit is lost. Where the treaty gives the taxing right only to Slovenia (for example most capital gains, pensions and other income), no credit is given. The person reclaims the foreign tax from the foreign authority (FURS, Applying double tax treaties).
- **Withholding inside the EU.** Dividends to an EU parent are exempt at 10% for 24 months (ZDDPO-2 art. 71). Interest and royalties to an associated EU company are exempt at 25% for 24 months, with a FURS permit (art. 72). The same procedures apply to Swiss recipients under the EU-Switzerland agreement (FURS, Dividends, interest and royalties).
- **Payments through a PE.** Art. 70(1) excludes from withholding dividends and dividend-like income paid through a non-resident's Slovenian PE.
- **Social security.** Contributions for people working across borders are in [slovenia-social-contributions](slovenia-social-contributions.md); this skill does not cover them.

## Worked examples

### Example 1: a Ljubljana company pays a Panama consultant and lender

A Slovenian d.o.o. pays EUR 40,000 for consulting services to a company seated in Panama. It also pays EUR 10,000 of interest on a loan from that company. Panama is on the art. 8.a list, and Slovenia has no treaty with Panama in the FURS list for 2026.

1. Consulting paid to a listed jurisdiction is caught by art. 70(1)(6). If the consultant were seated in a non-listed state, no withholding would apply.
2. Interest charged to a Slovenian resident is Slovenian-source (art. 8(7)) and caught by art. 70(1)(2). The bank exception does not help, because the lender is not a bank.
3. Withholding at 15% of each gross payment: EUR 6,000 on the fee and EUR 1,500 on the interest, EUR 7,500 in total.
4. The Panama company receives EUR 42,500 net.
5. The d.o.o. pays the tax and files the withholding return no later than 5 days after each payment (ZDavP-2 art. 374).

There is no treaty, so no KIDO claim is possible. The d.o.o. should also check whether the consulting fee is deductible: related-party and low-tax rules sit in [si-corporate-income-tax](si-corporate-income-tax.md).

```oa-check
name: Payments to a listed jurisdiction, 15% withholding (2026)
inputs:
  fee: 40000
  interest: 10000
steps:
  - wht_fee: fee * 0.15
  - wht_interest: interest * 0.15
  - wht_total: wht_fee + wht_interest
  - net_paid: fee + interest - wht_total
expected:
  wht_fee: 6000
  wht_interest: 1500
  wht_total: 7500
  net_paid: 42500
```

### Example 2: a d.o.o. moves its effective management to Vienna in 2026

The board of a Slovenian company moves to Vienna. From 1 July 2026 all key decisions are taken there, and the company becomes resident in Austria only. It keeps no Slovenian PE. At that date:

- its long-term assets (equipment and a trademark) have a fair value of EUR 1,200,000 and a tax value of EUR 700,000;
- its inventory has a fair value of EUR 300,000 and a tax value of EUR 250,000.

1. A transfer of tax residence abroad triggers exit tax on assets not left with a Slovenian PE (ZDDPO-2 art. 54.a(1)(3)).
2. Hidden reserves on the long-term assets are EUR 500,000.
3. The inventory is a short-term asset and is left out (art. 54.a(8)).
4. The EUR 500,000 goes into the base for the period of the move, taxed at 22%: EUR 110,000.
5. Austria is an EU state, so the company may pay in 5 equal annual instalments of EUR 22,000 (art. 54.b). The first falls due 30 days after the return is filed. Interest at 2% a year, or the EC reference rate if higher, runs on the deferred amount (ZDavP-2 arts. 370.a and 104(2)). It is not computed here.
6. If the company sells the trademark during the instalment period, every remaining instalment falls due at once (art. 370.a(5)(1)).

```oa-check
name: Corporate exit tax on residence transfer to Austria (2026)
inputs:
  fv_long: 1200000
  tv_long: 700000
  fv_stock: 300000
  tv_stock: 250000
  years: 5
steps:
  - reserves: max(fv_long - tv_long, 0)
  - excluded_stock_gain: fv_stock - tv_stock
  - exit_tax: reserves * 0.22
  - instalment: exit_tax / years
expected:
  reserves: 500000
  excluded_stock_gain: 50000
  exit_tax: 110000
  instalment: 22000
```

## Ask the client first

1. For an individual: is permanent residence registered in Slovenia? Where do the family live, and where is the person's work? How many days are spent in Slovenia in the calendar year? What are the exact arrival or departure dates?
2. Does another state also treat the person or company as resident, and is there a Slovenian treaty with it in the FURS 2026 list? Can they get a certificate of residence from that state?
3. For a payment abroad: who receives it? Where is the recipient seated and where is it managed? Is that place on either art. 8.a list? Is the recipient the beneficial owner? What is the holding percentage, and since when has it been held?
4. For a foreign company working in Slovenia: what activities, where, for how long (the 6-month site test), and who signs contracts in Slovenia?
5. For a company moving out: which assets move, to which state, and at what fair and tax values? Does any business stay behind as a Slovenian PE?
6. For a new employee arriving: what are their age on the start date, their salary, and their residence and Slovenian income in the two prior tax years? These decide the 7% relief.

## Sources

| Source | URL | Read on |
|---|---|---|
| Corporate Income Tax Act (ZDDPO-2), consolidated text NPB23 (up to ZDDPO-2V, Uradni list RS 85/25): arts. 3 to 8, 8.a, 11, 12, 24, 54.a, 54.b, 60 with the ZORZFS art. 64 note, 62 to 67, 67.h, 68, 70 to 72, 74, 75 | https://pisrs.si/pregledPredpisa?id=ZAKO4687 | 2026-10-23 |
| Personal Income Tax Act (ZDoh-2), consolidated text NPB36 (up to ZDoh-2AB, Uradni list RS 104/24): arts. 5 to 10, 33, 96, 113.a, 116, 121, 122, 132, 135.č, 136, 137 | https://pisrs.si/pregledPredpisa?id=ZAKO4697 | 2026-10-23 |
| Tax Procedure Act (ZDavP-2), consolidated text NPB32: arts. 60, 95.a, 96, 104, 260, 262, 370.a, 373 to 377, 383.a, 394, 397, 398 | https://pisrs.si/pregledPredpisa?id=ZAKO4703 | 2026-10-23 |
| FURS, Obračunavanje in plačevanje DDPO (CIT computation and payment), 4th edition April 2026 | https://www.fu.gov.si/fileadmin/Internet/Davki_in_druge_dajatve/Podrocja/Davek_od_dohodkov_pravnih_oseb/Opis/Obracunavanje_in_placevanje_davka_od_dohodkov_pravnih_oseb.docx | 2026-10-23 |
| FURS, letter 0920-542/2024-2 on the 22% rate (ZORZFS art. 64) | https://www.fu.gov.si/fileadmin/Internet/Davki_in_druge_dajatve/Poslovanje_z_nami/Novodila_in_pojasnila/2024/0920-542_2024-2_Odgovor_na_vase_vprasanje_-_sprememba_davcne_stopnje_DDPO.docx | 2026-10-23 |
| FURS, order listing states under art. 8.a (corporate rate below 12.5%) | https://www.fu.gov.si/fileadmin/Internet/Davki_in_druge_dajatve/Podrocja/Mednarodno_obdavcenje/Zakonodaja/Seznam_drzav_v_katerih_je_splosna_oziroma_povprecna_nominalna_stopnja_obdavcitve_dobicka_druzb_nizja_od_12_5_pri_tem_pa_to_niso_drzave_clanice_EU.pdf | 2026-10-23 |
| FURS, Dividende, obresti in premoženjske pravice (KIDO forms, 5-year refund, EU directives) | https://www.fu.gov.si/fileadmin/Internet/Davki_in_druge_dajatve/Podrocja/Mednarodno_obdavcenje/Opis/Dividende_obresti_in_premozenjske_pravice.docx | 2026-10-23 |
| FURS, Izvajanje mednarodnih pogodb (applying tax treaties and the MLI), September 2023 | https://www.fu.gov.si/fileadmin/Internet/Davki_in_druge_dajatve/Podrocja/Mednarodno_obdavcenje/Opis/Izvajanje_mednarodnih_pogodb_o_izogibanju_dvojnega_obdavcevanja_dohodka_in_premozenja.docx | 2026-10-23 |
| FURS, list of tax treaties applied in 2026 | https://www.fu.gov.si/fileadmin/Internet/Davki_in_druge_dajatve/Podrocja/Mednarodno_obdavcenje/Zakonodaja/Seznam_veljavnih_MP.docx | 2026-10-23 |
| FURS, Stalna poslovna enota nerezidenta (permanent establishment), 3rd edition March 2026 | https://www.fu.gov.si/fileadmin/Internet/Davki_in_druge_dajatve/Podrocja/Mednarodno_obdavcenje/Opis/Stalna_poslovna_enota_nerezidenta.docx | 2026-10-23 |
| FURS, Davčne obveznosti Slovencev ob odhodu iz Slovenije (leaving Slovenia), 5th edition June 2025 | https://www.fu.gov.si/fileadmin/Internet/Davki_in_druge_dajatve/Podrocja/Mednarodno_obdavcenje/Opis/Davcne_obveznosti_Slovencev_ob_odhodu_iz_Slovenije.docx | 2026-10-23 |
| FURS, Mednarodna obdavčitev posameznikov (international taxation of individuals), 7th edition June 2025 | https://www.fu.gov.si/fileadmin/Internet/Davki_in_druge_dajatve/Podrocja/Mednarodno_obdavcenje/Opis/Brosura_Mednarodna_obdavcitev_posameznikov.docx | 2026-10-23 |
| FURS, Uveljavljanje odbitka oziroma vračila tujega davka (foreign tax credit and refund), September 2021 | https://www.fu.gov.si/fileadmin/Internet/Davki_in_druge_dajatve/Podrocja/Mednarodno_obdavcenje/Opis/Uveljavljanje_odbitka_oziroma_vracila_tujega_davka_pravnih_oseb_in_fizicnih_oseb_ki_opravljajo_dejavnost.docx | 2026-10-23 |

Not yet confirmed: the late payment interest rate for 2026 (ZDavP-2 art. 96 points to the statutory default interest law, not read); the EC reference rate that may lift exit-tax deferral interest above 2%; whether the art. 8.a order of 28 February 2022 has been amended since (FURS still publishes it as the current list); the average annual salary figure behind the 7% new-resident relief and the 2026 indexed income tax bands; whether ZDoh-2 was amended after Uradni list RS 104/24 (the pisrs consolidated text NPB36 ends there); the ministerial lists of company forms and taxes for arts. 71 and 72; individual treaty rates and tie-breakers; the withholding mechanics for non-resident individuals (REK forms), which belong to the payroll and income tax skills.
