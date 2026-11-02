---
name: ba-cross-border
description: "Cross-border tax in Bosnia and Herzegovina for tax year 2026: payments to non-residents, non-residents working in BiH, and residents with income from abroad. Set out separately for the Federation of BiH (FBiH), Republika Srpska (RS) and Brčko District (BD), with VAT at state level. Covers withholding tax on dividends, interest, royalties and services (FBiH 5% and 10%, RS 10%, BD 10% with dividends exempt); treaty relief, residence certificates and forms (OP-820, POD-815 to 819, RS Form 10); the 38 treaty partners; permanent establishment tests; non-residents selling BiH property or shares; non-resident individuals; VAT on services bought from abroad (17%, reverse charge); foreign tax credits for companies and individuals. Trigger phrases: porez po odbitku nerezident, withholding tax Bosnia, ugovor o izbjegavanju dvostrukog oporezivanja, potvrda o rezidentnosti, stalno mjesto poslovanja, reverse charge BiH. Out of scope: transfer pricing (ba-transfer-pricing), profit tax (ba-corporate-income-tax), personal income tax (bosnia-income-tax), VAT returns (bosnia-vat)."
version: 0.1
jurisdiction: BA
category: international
tax_year: 2026
last_updated: 2026-10-30
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Bosnia and Herzegovina cross-border tax (2026)

Direct taxes in Bosnia and Herzegovina are set by the two entities and Brčko District, each with its own law. VAT and the treaty network are state-level.

- **FBiH:** Zakon o porezu na dobit (15/16 and 15/20) and its Pravilnik (consolidated to 39/26); Zakon o porezu na dohodak; Pravilnik o poreznoj rezidentnosti (33/22, 89/22, 21/24). Authority: Porezna uprava FBiH.
- **RS:** Zakon o porezu na dobit (94/15, 1/17, 58/19, 48/24, 114/25; the 114/25 changes apply from 1 January 2026), the Pravilnik o uslovima i načinu oporezivanja porezom po odbitku (115/17), and Zakon o porezu na dohotak (60/15 as amended). Authority: Poreska uprava RS.
- **BD:** Zakon o porezu na dobit (17/22, 38/22) and Zakon o porezu na dohodak (consolidated with 24/20, 21/22, 45/22, 5/25).
- **State:** Zakon o porezu na dodanu vrijednost (VAT), run by the Indirect Taxation Authority (UIO). Treaties are concluded by BiH and listed by the Ministry of Finance and Treasury (MFT).

The payer's seat decides which entity's withholding rules apply. Amounts are in convertible marks (KM, BAM).

## Who this applies to

- **Payers.** A company in the FBiH, RS or BD that pays a non-resident (a company with its seat and management outside BiH) must withhold tax at payment (FBiH profit tax law arts. 5(2), 38(4); RS art. 47(1) and Rulebook 115/17 art. 3(2); BD art. 28(1)). In BD, a foreign person with a permanent establishment in BD that pays a foreign company must also withhold (BD art. 28(1)).
- **Non-resident companies.** They are taxed on profit of a permanent establishment (PE), on income from real estate, and by withholding on other BiH-source income (FBiH arts. 3(3), (4), 38, 39; RS arts. 40, 43, 44; BD art. 3(c) to (e)).
- **Non-resident individuals.** They pay 10% final tax on occasional independent work (FBiH PIT law art. 30(1); RS PIT law art. 61a; BD PIT law art. 31(1)).
- **Residents with foreign income.** Resident companies and individuals are taxed on worldwide income and credit foreign tax (FBiH profit tax art. 32; RS art. 50; BD art. 27; FBiH PIT art. 25; RS PIT art. 67; BD PIT art. 26).
- **VAT.** A BiH business that buys services from a foreign supplier with no seat in BiH and no tax representative pays the VAT itself (VAT Law art. 13(1)(3)).

Between the entities and BD, the same credits apply as for foreign tax (FBiH art. 32(1); RS art. 51; BD art. 23).

## Rates, bands and thresholds

| Item | Rate or amount | Year | Source |
|---|---|---|---|
| FBiH withholding: dividends | 5% of gross (lower under a treaty) | 2026 | FBiH profit tax law art. 38(6), (7): https://ik.imagekit.io/9qcwbg8wl/15-16_i_15-20-zakon-o-porezu-na-dobit-precisceni_07YP9wNd9.pdf |
| FBiH withholding: interest, royalties, management, technical and training services (including market research, tax advice, audit and consulting), rent, entertainment and sport, insurance, telecoms; other services only to non-treaty countries | 10% of gross (lower under a treaty) | 2026 | FBiH art. 38(1), (7) |
| RS withholding: dividends, interest, royalties, entertainment and sport, professional, scientific, technical and educational services, insurance, telecoms, movable rent; other services only to non-treaty countries | 10% (the separate 5% dividend rate was deleted from 2017) | 2026 | RS law art. 44 and art. 45 as amended by 1/17 arts. 15, 16: https://www.poreskaupravars.org/dokumenti/zakoni/ZakonoizmdopDobit.pdf |
| BD withholding: interest, entertainment and sport, management, consulting, financial, technical and administrative services, insurance, royalties, movable rent | 10% of the gross payment; dividends exempt | 2026 | BD profit tax law arts. 29, 30: https://skupstinabd.ba/3-zakon/ba/Zakon%20o%20porezu%20na%20dobit/05B17-22%20Zakon%20o%20porezu%20na%20dobit%20-%20prec--is--eni%20tekst.pdf |
| Residence certificate for treaty relief | No older than one year | 2026 | FBiH art. 40(1); RS art. 52(1) as amended by 1/17 art. 19; FBiH Rulebook 39/26 art. 110(3) |
| Treaty partners in force | 38 states (MFT list) | 2026 | https://www.mft.gov.ba/Content/Read/sporazumi-u-primjeni |
| Example treaty: Croatia | Dividends 5% (company holding at least 25% directly) or 10%; interest 10%; royalties 10%; building site PE after 12 months | 2026 | Treaty arts. 5(3), 10, 11, 12: https://chj.mft.gov.ba/data/Fiskala/BiH-Hrvatska_-_Komb._tekst_-__bos_-_28.12..pdf |
| Example treaty: Serbia | Dividends 5% (company holding at least 25% directly) or 10%; interest 10%; royalties 10% | 2026 | Treaty arts. 10, 11, 12: https://chj.mft.gov.ba/data/Fiskalni%20sporazumi%202/fiskala%20sporazumi/BiH_-_Srbija_-_bos._verzija.pdf |
| Treaty: Austria | Dividends 5% (company, not a partnership, holding at least 25% directly) or 10%; interest 5%, nil on credit sales of industrial, commercial or scientific equipment or of goods between enterprises, and on loans granted, secured or guaranteed by a state bank or the central bank; royalties 5% | 2026 | Convention arts. 10(2), 11(2), (3), 12(2), MFT combined text with the MLI: https://chj.mft.gov.ba/data/Datoteke/PDF/Fiskala%20sporazumi/MLA%20novi/Austrija_bos.pdf |
| Treaty: Germany (1987 Yugoslavia treaty, applied with BiH) | Interest taxable only in the recipient's state (nil in BiH); royalties 10%. Article 11 limits only German tax on dividends paid to a BiH resident (15%); it sets no limit for dividends paid by a BiH company | 2026 | Agreement arts. 11(1), 12(1), 13(2): https://chj.mft.gov.ba/data/Fiskalni%20sporazumi%202/fiskala%20sporazumi/SPORAZUM_SA_NJEMA%C4%8CKOM-_engleski_jezik.pdf |
| Treaty: Italy (1982 Yugoslavia convention, applied with BiH) | Dividends 10%; interest 10%; royalties 10% | 2026 | Convention arts. 10(2), 11(2), 12(2): https://chj.mft.gov.ba/data/Fiskalni%20sporazumi%202/fiskala%20sporazumi/Italija.pdf |
| Treaty: Netherlands (1982 Yugoslavia treaty, applied with BiH) | Dividends 5% (company, not a partnership, holding at least 25% directly) or 15%; interest taxable only in the recipient's state (nil in BiH); royalties 10% | 2026 | Treaty arts. 10(2), 11(1), 12(2), MFT combined text with the MLI: https://chj.mft.gov.ba/data/Fiskalni%20sporazumi%202/BiH-Holandija_-_bos._verzija.pdf |
| Treaty: Slovenia | Dividends 5% (company holding at least 25% directly) or 10%; interest 7%, nil when paid by or to the government, a political subdivision, a local authority or the central bank, or on loans granted, guaranteed or insured by the institution authorised under domestic law to insure and finance international business transactions; royalties 5% | 2026 | Agreement arts. 10(2), 11(2), (3), 12(2), MFT combined text with the MLI: https://chj.mft.gov.ba/data/Fiskalni%20sporazumi%202/BiH_-_Slovenija_-_bos._verzija_.pdf |
| Treaty: Turkey | Dividends 5% (company, not a partnership, holding at least 25% directly) or 15%; interest 10%; royalties 10% | 2026 | Convention arts. 10(2), 11(2), 12(2): https://chj.mft.gov.ba/data/Datoteke/PDF/Fiskala%20sporazumi/Turkey_eng.pdf |
| PE: building or installation site | FBiH more than 6 months; RS more than 12 months (from 2026); BD no minimum in the law | 2026 | FBiH art. 6(3); RS art. 41(1)(2) as amended by 114/25 art. 13: https://poreskaupravars.org/wp-content/uploads/2025/12/Dobit-1.pdf; BD art. 2(p) |
| PE: services, FBiH | More than 3 months in any 12-month period on the same or connected project | 2026 | FBiH art. 6(4); Rulebook 39/26 art. 11(2)(c) |
| Non-resident individual, occasional independent work | 10% final, no allowance | 2026 | FBiH PIT art. 30(1): https://www.pufbih.ba/v1/public/upload/zakoni/d9bf6-zakon-o-porezu-na-dohodak-ispravan-tekst.pdf; RS PIT art. 61a (110/24): https://poreskaupravars.org/wp-content/uploads/2025/01/Scan29012025.pdf; BD PIT art. 31(1) |
| VAT on services from abroad | 17% paid by the BiH business customer | 2026 | VAT Law arts. 13(1)(3), 23: https://www.uino.gov.ba/portal/wp-content/uploads/PROPISI/2_Porezi/1_PDV/1_Zakon_o_PDV/B/B-1-Zakon_o_PDV-b.pdf |
| Late-payment interest | FBiH 0.04% a day; RS 0.03% a day; BD 0.03% a day capped at principal; VAT 0.04% a day | 2026 | FBiH: https://pufbih.ba/v1/public/upload/zakoni/1%20Zakon%20o%20visini%20stope%20zatezne%20kamate%20na%20javne%20prihode%20-%20PRECISCEN%20TEKST.pdf; RS ZPP art. 60; BD ZPU art. 68; VAT: https://www.uino.gov.ba/portal/wp-content/uploads/PROPISI/1_UIO/3_Zakon_o_postupku_indirektnog_oporeivanja/1_Zakon/B/B-1-1-Zakon-o-izmjenama-Zakona-o-postupku-indirektnog-oporezivanja-Sluzbeni-glasnik-BiH-broj-10013.pdf |

## The taxable base

**Withholding base.**
- FBiH: the gross amount (art. 38(6)). Income from a building site or service project that meets the PE tests of art. 6(3), (4) also bears withholding when the non-resident has not registered as a profit taxpayer (art. 38(2)). Exempt: interest on supplier credit for production equipment, interest on government bonds, and reinsurance premiums paid by an approved reinsurer (art. 38(3)). Services performed remotely from outside BiH (internet, e-mail, phone) with nobody present in BiH are treated as performed abroad, so no withholding applies to them (Rulebook 39/26 art. 62(3)). Installation, technical support, training or advice performed in BiH does bear withholding (art. 62(2)).
- RS: the amount paid. Payments in kind are covered (art. 45(3)). From 2026 the exemptions are: repatriated PE profit after RS profit tax; interest on loans used to invest in equipment and plant under art. 26; and interest and insurance premiums on loans for projects the RS National Assembly declares of special importance (art. 46 as amended by 58/19, 48/24 and 114/25). The exemption for interest on RS government and municipal debt was deleted from 2026 (114/25 art. 14).
- BD: the gross amount, meaning what would have been paid had no tax been withheld (art. 30(2)). If a contract promises a net fee, gross it up. Exempt: repatriated PE profit where the foreign company holds 10% or more; interest on debt issued or guaranteed by BiH, BD, the entities or other listed issuers; deposit interest; dividends; interest from a PE to its head office if not deducted; interest on equipment or goods bought on credit; interest on loans from a foreign bank; interest on loans raised abroad for a BD company by an owner of at least 20% (art. 29(2)).

**Non-residents selling BiH assets.**
- FBiH: income from selling FBiH real estate, long-term shareholdings or industrial property rights to a resident or another non-resident is taxable unless a treaty says otherwise. Market value replaces a lower price between related parties (art. 39(1), (2)).
- RS: gains on RS real estate and on shares in a company whose assets are mostly RS real estate are taxed on an annual return (art. 43). From 2026 a company from the FBiH or BD is also taxed on selling shares in an RS resident company (art. 3(1)(3), amended by 114/25 art. 2).
- BD: rent, gains on BD real estate, gains on shares in companies whose assets are mostly BD real estate, and natural resource income are taxed on an annual return (art. 26).

**Permanent establishment.**
- FBiH (art. 6): a place of management, branch, office, factory, workshop, mine or quarry; a building or installation site lasting more than six months; services on the same or a connected project for more than three months in any twelve; a dependent agent who concludes contracts. Preparatory or auxiliary activity is not a PE. If a site becomes a PE, profit from the non-resident's other, shorter projects in the FBiH is taxed too (Rulebook 39/26 art. 11(3)).
- RS (art. 41): similar list. From 2026 a building, installation or assembly site counts only if it lasts more than 12 months (114/25 art. 13). Stock held by a local person who makes regular deliveries is a PE (art. 41(3)). A treaty definition prevails (art. 41(7)).
- BD (art. 2(p)): a fixed place of business, including a building, installation or assembly site with no minimum duration, and a dependent agent with authority to conclude contracts.
- PE profit is taxed at 10% under the profit tax rules (see ba-corporate-income-tax). In the RS, interest on loans from head office and royalties paid to head office are not deductible for the PE (art. 40(3), (4)).

**Foreign income of residents.**
- Companies: FBiH credits foreign tax and foreign withholding tax, capped at the FBiH tax on that profit (art. 32(2) to (4)). RS credits foreign tax, capped from 2026 at the RS tax on the profit earned abroad, and needs a certificate from the foreign tax office (art. 50 as amended by 1/17 and 114/25 art. 15). BD credits foreign tax capped at BD tax, or lets the company deduct it as an expense instead, with documents certified by the foreign tax office (art. 27).
- Individuals: foreign tax is credited, capped at the entity's own tax, only on documents certified by the foreign authority (FBiH PIT art. 25; RS PIT art. 67; BD PIT art. 26). An FBiH resident paid salary directly from abroad calculates and pays the monthly advance within 5 days of receiving it (FBiH PIT art. 27(10)); an RS resident within 7 days (RS PIT art. 66).

**VAT on services from abroad.** Services are supplied where the supplier is established, with exceptions (VAT Law art. 15). Licences and IP, advertising, consultancy, engineering, legal, audit, accounting, translation and data processing, financial and insurance services, staff supply, telecoms and hire of movable goods other than transport are supplied where the customer is established (art. 15(2)(4)). If such a service comes from a supplier with no seat in BiH and no tax representative, the BiH business customer is liable (art. 13(1)(3)). Services linked to BiH real estate are taxed in BiH whoever supplies them (art. 15(2)(1)). Imported goods bear 17% VAT at customs (see bosnia-vat).

## Deadlines and filing

| What | FBiH | RS | BD |
|---|---|---|---|
| Withhold | At payment (art. 38(4)) | At payment (art. 44(1); Rulebook 115/17 art. 2(2)) | At each payment (arts. 29(1), 30(1)) |
| Pay and report | Within 10 days after the month of payment, on POD-815 (dividends), POD-816 (interest), POD-817 (royalties), POD-818 (other income), POD-819 (property and rights) (art. 38(5); Rulebook 39/26 arts. 1, 111 to 115) | Annual withholding return within 30 days after the year end (art. 38(2), added by 1/17 art. 13; Rulebook 115/17 art. 14) | Annual withholding return by 31 March (arts. 22, 32) |
| Treaty exemption claim | Form OP-820 by the 20th of the month after payment, certified by the recipient and the foreign tax authority, or with a residence certificate no older than one year; electronic only from 1 January 2026 (Rulebook 39/26 art. 110) | Residence certificate no older than one year, and for a reduced rate a certified statement on Form 10, before payment; for continuous services once a year before the first payment (law art. 52; Rulebook 115/17 art. 13) | Proof of the treaty right given to the payer (art. 31(2)) |
| Non-resident sale of property or shares | Non-resident files and pays within 30 days, or the buyer or the company becomes liable (art. 39(3), (4)) | Annual return (art. 43(3)) | Annual return (art. 26(3)) |
| PE contract notice | | Resident reports a contract with a non-resident acting through a PE within 5 days (art. 42) | |
| Foreign tax credit | Form PK-814 with the profit tax return (Rulebook 39/26 art. 1) | With the profit tax return (art. 50(3)) | With the return (art. 27(4), (5)) |
| VAT on services from abroad | Paid by the 10th of the following month; value in box 21, the VAT in box 41 once paid (VAT Law art. 39; UIO instructions 47/22) | same | same |

**Residence certificates for BiH residents.** In the FBiH a company applies on Form ZCOR-103, with its last profit tax return. The certificate covers one tax period. It is issued on Form COR-104(A) for treaty relief, COR-104(B) for non-treaty countries and COR-104(C) to prove residence for other purposes. The FBiH tax office can also certify the other country's own form (Pravilnik o poreznoj rezidentnosti arts. 19, 20). The RS Tax Administration issues a foreign recipient, on request, a certificate of the RS tax withheld from it (RS law art. 49).

## Penalties and interest

- **Payer liable.** If the tax is not withheld or not paid on time, the payer owes it as its own tax (FBiH art. 40(2); RS art. 47(3)).
- **FBiH.** Not filing a withholding return, or not holding the treaty documents of art. 40: KM 3,000 to 100,000 for the company, KM 2,500 to 10,000 for the responsible person, plus 50% for repeat offences (art. 58(2)(b), (i), (3), (4)). Interest 0.04% a day.
- **RS.** Not filing a return: KM 2,000 to 6,000 for the company, KM 1,000 to 3,000 for the responsible person (Zakon o poreskom postupku art. 112). Not reporting a PE contract within 5 days: KM 5,000 to 15,000 (profit tax law art. 59). Interest 0.03% a day (ZPP art. 60).
- **BD.** Not filing a return: KM 1,000 to 5,000 for the company, KM 200 to 1,000 for the responsible person (Zakon o Poreznoj upravi art. 76). Interest 0.03% a day, capped at the principal (art. 68).
- **VAT.** VAT not charged or not paid: 50% of the amount, at least KM 100 (VAT Law art. 67(1)(2), (3)). Interest 0.04% a day (Zakon o postupku indirektnog oporezivanja art. 10, as amended by 100/13).

## Cross-border points

- **Treaties.** The MFT lists treaties in force with 38 states: Albania, Algeria, Austria, Azerbaijan, Belgium, Slovakia (old Czechoslovakia treaty), Czech Republic, Finland, France, Greece, Netherlands, Croatia, Iran, Ireland, Italy, Jordan, Qatar, China, Cyprus, Kuwait, Hungary, North Macedonia, Malaysia, Moldova, Norway, Germany, Pakistan, Poland, Romania, Slovenia, Serbia, Montenegro, Spain, Sri Lanka, Sweden, Turkey, United Arab Emirates and the United Kingdom. Several are modified by the BEPS Multilateral Instrument, and MFT publishes combined texts. A ratified treaty overrides the domestic rate (FBiH art. 38(7); RS art. 44(1), 52; BD art. 31(1)). The table above gives the rates for Croatia, Serbia, Austria, Germany, Italy, the Netherlands, Slovenia and Turkey from the MFT texts. A treaty only caps the BiH rate: where the domestic rate is lower (FBiH dividends 5%; BD dividends exempt), the domestic rate applies.
- **Services to treaty residents.** FBiH and RS charge withholding on "other services" only when the recipient is in a non-treaty country (FBiH art. 38(1)(i); RS art. 45(2)). The listed services (management, consulting, technical, audit, legal and so on) are taxed whatever the country, unless the treaty gives the right to tax only to the other state. Then the payer needs the residence certificate (and in the FBiH, Form OP-820).
- **Beneficial owner.** FBiH relief needs the recipient's statement that it is the beneficial owner (art. 40(1)).
- **Between entities.** A payment from an FBiH company to an RS company is not withholding territory; profit is taxed where the branch or company is, with credits (FBiH art. 32(1); RS art. 51; BD art. 23).
- **Transfer pricing.** Payments to foreign related parties must be at arm's length (ba-transfer-pricing).

## Worked examples

### Example 1: RS company paying a Croatian parent and a Croatian consultant (2026)

A Banja Luka company is 100% owned by a Zagreb company. In 2026 it pays the parent a dividend of KM 200,000 and interest of KM 50,000. It also pays a Zagreb consultancy KM 30,000 for advice given remotely. The consultancy has no PE or tax representative in BiH. The company is registered for VAT. All recipients give a Croatian residence certificate dated this year, and the parent signs Form 10 for the reduced dividend rate.

Domestic RS withholding would be 10% on all three, KM 28,000 (arts. 44, 45). Under the BiH–Croatia treaty: dividends to a company holding at least 25% directly are capped at 5% (art. 10), so KM 10,000; interest stays at 10% (art. 11), so KM 5,000; consultancy fees are business profits taxable only in Croatia without a PE (art. 7), so nothing is withheld once the certificate is held (RS law art. 52(1)). Total withholding is KM 15,000, a saving of KM 13,000. The annual withholding return is due by 30 January 2027 (art. 38(2)). For VAT, consultancy is supplied where the customer is (VAT Law art. 15(2)(4)), so the company pays 17% on KM 30,000, KM 5,100, by the 10th of the following month and deducts it in box 41 once paid.

```oa-check
name: RS payments to Croatian residents with treaty relief (2026)
inputs:
  dividend: 200000
  interest: 50000
  consulting: 30000
steps:
  - wht_domestic: (dividend + interest + consulting) * 0.10
  - wht_dividend_treaty: dividend * 0.05
  - wht_interest_treaty: interest * 0.10
  - wht_consulting_treaty: consulting * 0
  - wht_treaty_total: wht_dividend_treaty + wht_interest_treaty + wht_consulting_treaty
  - saving: wht_domestic - wht_treaty_total
  - vat_reverse_charge: consulting * 0.17
expected:
  wht_domestic: 28000
  wht_dividend_treaty: 10000
  wht_interest_treaty: 5000
  wht_consulting_treaty: 0
  wht_treaty_total: 15000
  saving: 13000
  vat_reverse_charge: 5100
```

### Example 2: FBiH company with a Serbian royalty and a capped credit (2026)

A Sarajevo software company licenses software to a Serbian customer for KM 100,000 in 2026. Serbia withholds 10%, the treaty maximum for royalties (BiH–Serbia treaty art. 12), so KM 10,000. Costs directly linked to that income are KM 40,000.

The royalty is part of the company's worldwide profit (FBiH art. 3(1)). Profit on it is KM 60,000, and FBiH tax on that at 10% is KM 6,000. The credit for Serbian tax cannot exceed the FBiH tax on that profit (art. 32(3), (4)), so it is KM 6,000 and FBiH tax on this income falls to nil. The other KM 4,000 of Serbian tax is not relieved in the FBiH. The company claims the credit on Form PK-814 with its return and keeps the Serbian proof of tax paid.

```oa-check
name: FBiH foreign tax credit capped at FBiH tax (2026)
inputs:
  royalty: 100000
  related_costs: 40000
steps:
  - serbian_wht: royalty * 0.10
  - profit_on_royalty: royalty - related_costs
  - fbih_tax_on_royalty: profit_on_royalty * 0.10
  - credit: min(serbian_wht, fbih_tax_on_royalty)
  - fbih_tax_after_credit: fbih_tax_on_royalty - credit
  - unrelieved: serbian_wht - credit
expected:
  serbian_wht: 10000
  profit_on_royalty: 60000
  fbih_tax_on_royalty: 6000
  credit: 6000
  fbih_tax_after_credit: 0
  unrelieved: 4000
```

## Ask the client first

1. Where is the paying company seated: FBiH, RS or BD? That sets the rate list, exemptions and deadlines.
2. What exactly is paid (dividend, interest, royalty, which service), and is the service performed in BiH or remotely?
3. Where is the recipient resident, does it hold a current residence certificate, and is it the beneficial owner? For dividends, what share does it hold directly?
4. Does the contract fix a net fee? BD requires grossing up, and in all three the payer owes tax it failed to withhold.
5. Does a foreign business have people, a site or an agent in BiH, and for how long? This decides whether there is a PE.
6. For foreign income: what tax was paid abroad, and is there a certificate from the foreign tax office?

## Sources

| Source | URL | Read on |
|---|---|---|
| FBiH Zakon o porezu na dobit, 15/16 and 15/20, consolidated: arts. 3, 5, 6, 32, 38 to 40, 58 | https://ik.imagekit.io/9qcwbg8wl/15-16_i_15-20-zakon-o-porezu-na-dobit-precisceni_07YP9wNd9.pdf | 2026-10-30 |
| FBiH Pravilnik o primjeni Zakona o porezu na dobit, consolidated to 39/26: arts. 1, 11 (PE), 62, 63, 110, 111 to 115 | https://pufbih.ba/v1/public/upload/zakoni/03062026%20Pravilnik%20o%20primjeni%20Zakona%20o%20porezu%20na%20dobit%2039-26.pdf | 2026-10-30 |
| FBiH Pravilnik o poreznoj rezidentnosti, 33/22, 89/22, 21/24: arts. 1, 19, 20 | https://www.pufbih.ba/v1/public/upload/zakoni/1587d-b4848-7b55c-pravilnik-o-poreznoj-rezidentnosti-precisceni-3322-8922-i-2124-.pdf | 2026-10-30 |
| FBiH Zakon o porezu na dohodak, consolidated: arts. 25, 27(10), 30 | https://www.pufbih.ba/v1/public/upload/zakoni/d9bf6-zakon-o-porezu-na-dohodak-ispravan-tekst.pdf | 2026-10-30 |
| FBiH Zakon o visini stope zatezne kamate na javne prihode: art. 2 | https://pufbih.ba/v1/public/upload/zakoni/1%20Zakon%20o%20visini%20stope%20zatezne%20kamate%20na%20javne%20prihode%20-%20PRECISCEN%20TEKST.pdf | 2026-10-30 |
| RS Zakon o porezu na dobit, 94/15: arts. 38, 40 to 52, 59 | https://www.poreskaupravars.org/dokumenti/zakoni/Zakon%20o%20porezu%20na%20dobit%20od%2001_01_2016.pdf | 2026-10-30 |
| RS amendment 1/17: arts. 13 to 19 | https://www.poreskaupravars.org/dokumenti/zakoni/ZakonoizmdopDobit.pdf | 2026-10-30 |
| RS amendment 58/19: art. 10 (art. 46) | https://www.poreskaupravars.org/dokumenti/zakoni/Zakon%20o%20porezu%20na%20dobit%20SG%202019.pdf | 2026-10-30 |
| RS amendment 48/24: art. 1 (art. 46) | https://poreskaupravars.org/wp-content/uploads/2024/06/Zakon.pdf | 2026-10-30 |
| RS amendment 114/25, in force 1 January 2026: arts. 2, 12 to 16 | https://poreskaupravars.org/wp-content/uploads/2025/12/Dobit-1.pdf | 2026-10-30 |
| RS Pravilnik o uslovima i načinu oporezivanja porezom po odbitku, 115/17: arts. 2 to 4, 13, 14, Form 10 | https://www.poreskaupravars.org/dokumenti/pravilnici/Pravilnik-%D0%BE-uslovima-nacinu-oporezivanja-porezom-po-odbitku-SLGL-115_17.pdf | 2026-10-30 |
| RS Zakon o porezu na dohodak 60/15: arts. 66, 67 | https://www.poreskaupravars.org/dokumenti/zakoni/zakonoporezunadohodak6015.pdf | 2026-10-30 |
| RS amendment to the income tax law 110/24: art. 61a | https://poreskaupravars.org/wp-content/uploads/2025/01/Scan29012025.pdf | 2026-10-30 |
| RS Zakon o poreskom postupku 78/20: arts. 60, 112 | https://poreskaupravars.org/wp-content/uploads/2020/11/Zakon-o-poreskom-postupku.pdf | 2026-10-30 |
| BD Zakon o porezu na dobit, consolidated 17/22: arts. 2(p), 3, 22 to 32 | https://skupstinabd.ba/3-zakon/ba/Zakon%20o%20porezu%20na%20dobit/05B17-22%20Zakon%20o%20porezu%20na%20dobit%20-%20prec--is--eni%20tekst.pdf | 2026-10-30 |
| BD Zakon o porezu na dohodak, unofficial consolidated text: arts. 3, 26, 31 | https://skupstinabd.ba/3-zakon/ba/Zakon%20o%20porezu%20na%20dohodak/Nesluz--bena%20prec--is--c-ena%20verzija%20Zakona%20o%20porezu%20na%20dohodak%20B.pdf | 2026-10-30 |
| BD Zakon o Poreznoj upravi 11/20: arts. 68, 76 | https://skupstinabd.ba/3-zakon/ba/Zakon%20o%20Poreznoj%20upravi%20Brc--ko%20Distrikta%20BiH/011B11-20%20Zakon%20%20o%20poreznoj%20upravi%20Brcko%20distrikta%20BiH.pdf | 2026-10-30 |
| BiH Zakon o PDV (9/05): arts. 13, 15, 23, 39, 67 | https://www.uino.gov.ba/portal/wp-content/uploads/PROPISI/2_Porezi/1_PDV/1_Zakon_o_PDV/B/B-1-Zakon_o_PDV-b.pdf | 2026-10-30 |
| UIO Uputstvo o popunjavanju PDV prijave, 47/22 (boxes 21, 41) | https://www.uino.gov.ba/portal/wp-content/uploads/PROPISI/2_Porezi/1_PDV/2_Pravilnici/B/B-1-2-Uputstvo-o-popunjavanju-PDV-prijave-Sglasnik-47-22-19-07-22.pdf | 2026-10-30 |
| Zakon o izmjenama Zakona o postupku indirektnog oporezivanja 100/13 (0.04%) | https://www.uino.gov.ba/portal/wp-content/uploads/PROPISI/1_UIO/3_Zakon_o_postupku_indirektnog_oporeivanja/1_Zakon/B/B-1-1-Zakon-o-izmjenama-Zakona-o-postupku-indirektnog-oporezivanja-Sluzbeni-glasnik-BiH-broj-10013.pdf | 2026-10-30 |
| BiH–Austria convention, MFT combined text with the MLI: arts. 10 to 12 | https://chj.mft.gov.ba/data/Datoteke/PDF/Fiskala%20sporazumi/MLA%20novi/Austrija_bos.pdf | 2026-10-30 |
| Yugoslavia–Germany agreement 1987, English text published by MFT: arts. 11 to 13 | https://chj.mft.gov.ba/data/Fiskalni%20sporazumi%202/fiskala%20sporazumi/SPORAZUM_SA_NJEMA%C4%8CKOM-_engleski_jezik.pdf | 2026-10-30 |
| Yugoslavia–Italy convention 1982, English text published by MFT: arts. 10 to 12 | https://chj.mft.gov.ba/data/Fiskalni%20sporazumi%202/fiskala%20sporazumi/Italija.pdf | 2026-10-30 |
| Yugoslavia–Netherlands treaty 1982, MFT combined text with the MLI: arts. 10 to 12 | https://chj.mft.gov.ba/data/Fiskalni%20sporazumi%202/BiH-Holandija_-_bos._verzija.pdf | 2026-10-30 |
| BiH–Slovenia agreement 2006, MFT combined text with the MLI: arts. 10 to 12 | https://chj.mft.gov.ba/data/Fiskalni%20sporazumi%202/BiH_-_Slovenija_-_bos._verzija_.pdf | 2026-10-30 |
| BiH–Turkey convention, English text published by MFT: arts. 10 to 12 | https://chj.mft.gov.ba/data/Datoteke/PDF/Fiskala%20sporazumi/Turkey_eng.pdf | 2026-10-30 |
| MFT, double tax treaties in force | https://www.mft.gov.ba/Content/Read/sporazumi-u-primjeni | 2026-10-30 |
| BiH–Croatia treaty, MFT combined text with the MLI: arts. 5, 7, 10 to 12 | https://chj.mft.gov.ba/data/Fiskala/BiH-Hrvatska_-_Komb._tekst_-__bos_-_28.12..pdf | 2026-10-30 |
| BiH–Serbia treaty, MFT combined text with the MLI: arts. 10 to 12 | https://chj.mft.gov.ba/data/Fiskalni%20sporazumi%202/fiskala%20sporazumi/BiH_-_Srbija_-_bos._verzija.pdf | 2026-10-30 |

Not yet confirmed: treaty rates for the other 30 treaty partners (only the Croatia, Serbia, Austria, Germany, Italy, Netherlands, Slovenia and Turkey texts were read); the BiH rate on dividends paid by a BiH company to a German resident (the 1987 treaty's dividend article covers only German dividends, and the other-income article was not read); whether the Italy and Turkey treaties are modified by the MLI (MFT publishes no combined text for them); whether treaties signed after the MFT list page date (23 November 2020) are in force; the RS rules for issuing residence certificates to RS companies; the RS deadline for paying withheld tax to the budget beyond "at payment" (Rulebook 115/17 does not set a monthly date); the BD form and procedure for treaty relief; whether the FBiH 4:1 and RS interest rules restrict interest paid abroad beyond withholding (see ba-corporate-income-tax); VAT refunds to foreign businesses on Form PDV SL 1 (conditions not read; see bosnia-vat); Brčko withholding exemption list as amended after 17/22 (none found). The RS law texts were read from OCR of the official gazette scans published by Poreska uprava RS.

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
