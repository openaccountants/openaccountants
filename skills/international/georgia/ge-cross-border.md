---
name: ge-cross-border
description: "Cross-border tax in Georgia (the country, GE, currency GEL; not the US state) for tax year 2026, under the Tax Code of Georgia. Covers residence of individuals (183 days) and companies (place of business or management), permanent establishment including the three-month management rule, Georgian-source income, withholding on payments to non-residents (dividends, interest and royalties 5%; international telecom and transport 10%; other Georgian-source income 10%; salary 20%; 15% on interest, royalties and other income to a preferential tax country), the refund return for non-residents, treaty relief under art. 125 and residence certificates, the foreign tax credit, the Government list of preferential tax countries and its treaty rule, and VAT reverse charge at 18% on services bought from abroad. Trigger phrases: Georgia withholding tax non-resident, Georgia double tax treaty, Georgian residence certificate, permanent establishment Georgia, reverse charge Georgia, offshore payments Georgia. Out of scope: profit tax generally (ge-corporate-income-tax), transfer pricing (ge-transfer-pricing), individual income tax (georgia-income-tax), VAT generally (georgia-vat), treaty-by-treaty rate tables."
version: 0.1
jurisdiction: GE
category: international
tax_year: 2026
last_updated: 2026-10-31
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Georgia cross-border tax, 2026

This skill covers what a Georgian business or adviser needs when money or people cross the border: who is resident, when a foreign business has a permanent establishment, what is withheld from payments to non-residents, how treaty relief works, and VAT on services bought from abroad. The law is the Tax Code of Georgia, consolidated publication of 15 October 2026 on matsne.gov.ge. The tax authority is the Revenue Service (rs.ge). Amounts are in Georgian lari (GEL).

Profit tax is covered in ge-corporate-income-tax. Transfer pricing, including the preferential tax country rules for controlled transactions, is in ge-transfer-pricing. Personal income tax is in georgia-income-tax and VAT in georgia-vat.

## Who this applies to

- **Resident individual**: a person who actually stayed in Georgia for 183 days or more in any continuous 12-month period ending in the tax year, or who was abroad in Georgian public service that year (art. 34(2)). Days abroad for treatment, leisure, business trips or education count as days in Georgia (art. 34(3)). Any part of a day counts as a day (art. 34(5)). Days in Georgia as a diplomat or consular officer, as international-organisation staff or foreign public servant, in transit, or for treatment or leisure are not counted (art. 34(4)). Status is set for each tax period (art. 34(8)).
- **Georgian citizen resident nowhere**: treated as resident on application to the tax authority (art. 34(6^1)). A high net worth individual may be granted residence under the Minister of Finance's procedure (art. 34(6)), and the Minister may grant residence to other foreign individuals in set cases (art. 34(6^2)).
- **Georgian enterprise**: one whose place of business or place of management is in Georgia (art. 22(1)). Every other enterprise is foreign (art. 22(2)).
- **Non-residents** with Georgian-source income that is not attributed to a Georgian permanent establishment are taxed at source with no deductions (art. 134(1)).
- **Tax agents**: a legal person, enterprise, organisation or entrepreneur that pays Georgian-source income to a non-resident must withhold (art. 154(1)(c)).
- **VAT**: any business established in Georgia that buys a service from a supplier not established in Georgia is a tax agent for reverse charge. Non-entrepreneur individuals and Free Industrial Zone enterprises are not (art. 161(2)(a)).

## Rates, bands and thresholds

| Item | Rate or amount | Year | Source URL |
|---|---|---|---|
| Residence test for individuals | 183 days or more in any continuous 12 calendar months ending in the tax year | 2026 | Tax Code art. 34(2), https://matsne.gov.ge/en/document/view/1043717?publication=247 |
| Permanent establishment through management by another person | over 3 months | 2026 | art. 29(4), same URL |
| Dividends paid to a non-resident | 5% at source | 2026 | arts. 130(1), 134(1)(a), same URL |
| Dividends from profit of banks, credit unions, microfinance organisations and loan providers earned in 2023 or later | not taxed at source | 2026 | art. 130(8), same URL |
| Interest paid to a non-resident without a PE | 5% at source | 2026 | arts. 131(1), 134(1)(b), same URL |
| Interest from a Georgian licensed financial institution | not taxed at source | 2026 | art. 131(5), same URL |
| Interest on debt securities of a Georgian enterprise listed on a recognised foreign exchange | not taxed at source | 2026 | art. 131(8), same URL |
| Royalties paid to a non-resident | 5% at source | 2026 | art. 134(1)(b^1), same URL |
| International telecom and international transport services | 10% at source | 2026 | art. 134(1)(c), same URL |
| Non-resident oil and gas subcontractors | 4% at source | 2026 | art. 134(1)(d), same URL |
| Other Georgian-source income of a non-resident | 10% at source | 2026 | art. 134(1)(e), same URL |
| Salary of a non-resident | 20% at source | 2026 | arts. 81(1), 134(1)(f), same URL |
| Interest, royalties and other income to a person registered in a preferential tax country | 15% at source | 2026 | art. 134(1^1), same URL |
| Preferential tax country test | profit tax exemption, no profit tax, or a rate not over 1/3 of the Georgian rate | 2026 | art. 98^2(5), (6), same URL |
| Preferential tax country list | Part 1: 15 jurisdictions; Part 2: 49 countries | 2026 | Government Ordinance No 615 of 29 December 2016, https://matsne.gov.ge/ka/document/view/3523434 |
| VAT on services bought from a non-established supplier (reverse charge) | 18% of the amount paid | 2026 | arts. 161(1)(a), (3)(a), 166, same Tax Code URL |
| Penalty interest on late tax, including tax not withheld | 0.05% of the unpaid tax per day | 2026 | art. 272(4), same Tax Code URL |

## The taxable base

**Georgian-source income** (art. 104(1)). The place where the money is received does not matter (art. 104(2)). For a non-resident the main items are:

- employment in Georgia;
- supplies of goods in Georgia;
- services delivered in Georgia, which means actually rendered in Georgia, or tied to property in Georgia, or to securities of a Georgian resident;
- dividends from a resident company, and gains on its shares;
- interest and royalties paid by a Georgian resident, or charged to a Georgian permanent establishment;
- rent for movable property used in Georgia, and income from immovable property in Georgia;
- gains on shares in an enterprise more than 50% of whose assets come from Georgian immovable property;
- management, financial and insurance services paid for by a resident enterprise or a Georgian permanent establishment, wherever they are performed (art. 104(1)(n));
- international transport and telecom services between Georgia and abroad.

A service a non-resident performs entirely abroad is not Georgian-source, unless it falls in one of these listed cases. So no Georgian income tax is withheld from it.

**Withholding is on the gross amount**, with no deductions (art. 134(1)). The tax agent withholds when it pays (art. 154(3)(a)).

**The refund return.** A non-resident taxed at source on items (c) to (e) of art. 134(1) may file a return before 1 April of the next year. It is then taxed on Georgian-source gross income less deductions, and its tax cannot exceed what was withheld (art. 134(3), (4)).

**Sales of Georgian property by non-residents** are not taxed at source. A non-resident enterprise without a permanent establishment is taxed on gross Georgian-source income from the sale for the calendar year, less related deductions (art. 97(5), (6)). A non-resident individual is taxed the same way (art. 80(4), (5)).

**Permanent establishment** (art. 29):

- It is a fixed place of business through which a foreign enterprise or non-resident individual carries on business in Georgia, in whole or in part, including through an authorised agent (art. 29(1)).
- These count as a PE (art. 29(2)): construction sites and installation projects; drilling rigs; a fixed base of a non-resident individual; a place of management, branch, representative office, office or workshop.
- Management of a foreign enterprise by another person, on its behalf or in its interest, for more than three months is a PE (art. 29(4)).
- These are not a PE on their own (art. 29(5) to (9), (12)):
  - an independent intermediary that cannot negotiate or sign;
  - owning Georgian shares or property;
  - seconded staff under the host's control;
  - controlling a Georgian company;
  - storage, display, purchasing, information gathering, preparatory or ancillary work, or preparing and signing loan, supply or technical service agreements for the foreign enterprise;
  - leasing property, unless the owner systematically services and supervises it.
- The tax authority registers PEs (art. 29(11)).
- A PE pays profit tax like a Georgian company on distributed profit. Profit sent to the head office counts as distributed (arts. 97(3), 98^1(3)); see ge-corporate-income-tax.

**Foreign tax credit.** A Georgian enterprise may set off profit tax paid abroad on income that is not Georgian-source. A company on the distributed-profit model sets it off when it pays tax on a dividend. The credit is capped at the Georgian tax on that profit (art. 124). A resident individual pays no Georgian tax on foreign-source income (art. 82(1)(u)); see georgia-income-tax.

**Preferential tax countries.**

- The list (Government Ordinance No 615) has 15 jurisdictions in Part 1: Anguilla, Bahamas, Bahrain, Bermuda, British Virgin Islands, Guernsey, Vanuatu, Cayman Islands, Curaçao, Isle of Man, Marshall Islands, Micronesia, Palau, Sark, Turks and Caicos Islands.
- Part 2 has 49 countries where a regime for some legal persons meets the test (art. 98^2(6)). Examples are Andorra, the United Arab Emirates, Cyprus, Hong Kong, Jersey, Liechtenstein, Luxembourg, Malaysia, Panama and Seychelles.
- **The treaty rule.** Under note 3 of the list, a listed country that has a ratified tax treaty in force with Georgia is preferential only for art. 98^1(2)(e) and art. 98^2(3)(a) to (e). So the 15% withholding in art. 134(1^1) does not apply to a person in a treaty country on the list.

**Treaty relief.** The procedure for using a treaty privilege, and for refunds of Georgian tax to a non-resident, is set by order of the Minister of Finance (art. 125). Treaties are published on matsne.gov.ge. Read the treaty with the payee's country for the rate and the beneficial-owner condition before applying it. For example, under the Georgia–Cyprus agreement (in force 4 January 2016), dividends and interest paid to a Cyprus resident, and royalties whose beneficial owner is a Cyprus resident, are taxable only in Cyprus (arts. 10(1), 11(1), 12(1)). This does not apply where the payee has a Georgian PE the income is linked to (arts. 10(3), 11(3), 12(3)).

**Residence certificates.** The Revenue Service issues certificates of Georgian tax residence. Anyone can check one on rs.ge/residence using the certificate ID and barcode.

**VAT on services bought from abroad.**

- For a business customer, the place of supply of a service is where the customer is established, unless a special rule applies (art. 162^1(3)(a)).
- A service supplied in Georgia by a person not established there, to a tax agent, is reverse charged (art. 161(1)(a)). The agent charges VAT on the amount paid (art. 161(3)(a)).
- A VAT-registered agent declares it in its monthly return and may deduct it under the normal rules (arts. 168(1), 175(1)(d)).
- An agent that is not VAT-registered pays it by the 15th of the next month (art. 168(4)). It has no deduction, because deduction is for registered taxable persons.
- Exempt services are not reverse charged (art. 161(6)(a)).
- Non-resident suppliers of electronic and similar services to Georgian consumers must account for VAT themselves (arts. 162^1(14), 165^2(2)(e)); see georgia-vat.

## Deadlines and filing

| What | When | Source |
|---|---|---|
| Pay tax withheld from a non-resident | when the payment is made; for payments in kind, on the last day of the month | art. 154(3)(a) |
| Withholding return on payments made | by the 15th of the month after the reporting period | art. 154(4) |
| Notice of income paid and tax withheld, per recipient | by the 15th of the month after the month of withholding | art. 154(3)(c.a) |
| Non-resident refund return for art. 134(1)(c) to (e) income | before 1 April of the following year | art. 134(3) |
| Reverse-charge VAT, VAT-registered agent | in the monthly VAT return, by the 15th of the next month | art. 168(1) |
| Reverse-charge VAT, agent not VAT-registered | by the 15th of the next month | art. 168(4) |
| Permanent establishment existence | from registration, grant of powers or start of representative activity | art. 29(10) |

## Penalties and interest

| Offence | Penalty | Source |
|---|---|---|
| Failure to withhold | the payer pays the tax not withheld on the amount actually paid, plus the related penalties | art. 154(2)(b) |
| Late payment | penalty interest of 0.05% of the unpaid tax per day, including the day of payment | art. 272(4) |
| Penalty interest time limit | not charged once 3 years have passed from the day the obligation to charge it arose | art. 272(2^1) |
| Late return, up to 2 months | 5% of the tax due on the return (Georgian text of art. 274(1); the English translation still shows an older wording of 5% a month capped at 30%) | art. 274(1) |
| Late return, over 2 months | 10% of the tax due | art. 274(2) |
| Late return showing no tax | no fine | art. 274(3) |
| Understatement, up to 5% of the tax declared | 10% of the understated tax | art. 275(2^1) |
| Understatement, over 5% and up to 20% | 25% of the understated tax | art. 275(2^2) |
| Understatement, other cases | 50% of the understated tax | art. 275(2) |
| Understatement over GEL 100,000 | large-scale tax evasion under criminal law | art. 275(4) |

The recipient may pay the tax and penalties on behalf of the payer (art. 154(2)(c)).

## Cross-border points

- **Moving management into Georgia.** A foreign company that moves its place of management to Georgia becomes a Georgian enterprise (art. 22(1)). Passing on dividends it received before the move is not distributed profit (art. 98^1(2)(f)).
- **Foreign dividends passed on.** A dividend a Georgian company receives from a foreign enterprise and pays on is not distributed profit. This does not apply if the foreign enterprise is in a preferential tax country; for this rule, treaty countries on the list are caught too (art. 98^1(2)(e); Ordinance No 615, note 3).
- **Payments to preferential tax countries that are taxed as profit.** Loans, advances, fines, debt securities and lost claims involving a person registered in a preferential tax country are taxed when made. Capital contributions to any non-resident are taxed too. Credits follow when the money comes back (art. 98^2(3), (7), (8)). See ge-corporate-income-tax.
- **Moving an offshore company's assets to Georgia.** All assets of a foreign enterprise registered in a preferential tax country may move to a Georgian enterprise before 1 January 2028, if the same individuals own 100% of both (art. 309(146)). The reliefs are no profit or income tax on Georgian-source income from that activity, no import tax on the assets, and no property tax on them until 1 January 2030.
- **Transfer pricing.** Transactions with foreign related parties, and any transaction with a resident of a non-treaty preferential tax country, must be at arm's length (art. 127); see ge-transfer-pricing.
- **Non-resident employees.** Salary of a non-resident is taxed at source at 20% (art. 134(1)(f)). A non-resident employer that has no Georgian PE does not withhold; the employee may account for the tax instead (art. 154(1)(a.b), (5)).

## Worked examples

### Example 1: services bought from abroad by a Georgian company

A VAT-registered Tbilisi LLC makes two payments in April 2026. It pays GEL 20,000 to a foreign software firm for development work done entirely abroad. It also pays GEL 50,000 to its foreign parent as a management fee. The client confirms that no tax treaty applies to the parent, that neither payee is in a preferential tax country, and that neither has a Georgian PE.

The software work is not Georgian-source, because it was not rendered in Georgia and is not one of the listed services (art. 104(1)(c)). So nothing is withheld. A management fee paid by a resident enterprise is Georgian-source wherever the work is done (art. 104(1)(n)). It is withheld at 10%, GEL 5,000 (art. 134(1)(e)), and paid when the fee is paid (art. 154(3)(a)).

Both services are supplied in Georgia for VAT, because the customer is established there (art. 162^1(3)(a)). Both are reverse charged at 18% on the amount paid: GEL 3,600 and GEL 9,000 (arts. 161(3)(a), 166). The LLC declares GEL 12,600 output VAT in its April return by 15 May 2026, and deducts the same amount if the services are used for taxable supplies (art. 175(1)(d)). The withholding return is also due by 15 May 2026 (art. 154(4)).

```oa-check
name: Georgian LLC buys a software service and a management fee from abroad, April 2026
inputs:
  software_fee: 20000
  management_fee: 50000
steps:
  - wht_software: software_fee * 0
  - wht_management: management_fee * 0.10
  - vat_software: software_fee * 0.18
  - vat_management: management_fee * 0.18
  - reverse_charge_output: vat_software + vat_management
  - reverse_charge_input: reverse_charge_output
  - net_vat: reverse_charge_output - reverse_charge_input
  - cash_to_parent: management_fee - wht_management
expected:
  wht_management: 5000.00
  vat_software: 3600.00
  vat_management: 9000.00
  reverse_charge_output: 12600.00
  net_vat: 0.00
  cash_to_parent: 45000.00
```

### Example 2: interest to a Cyprus parent and a royalty to a British Virgin Islands company

In June 2026 the same LLC pays GEL 60,000 of interest to its parent, a Cyprus resident company. It also pays a GEL 40,000 royalty to a company registered in the British Virgin Islands. The parent gives a Cyprus certificate of residence and is the beneficial owner. The client confirms that no Georgian tax treaty covers the BVI company, and that neither payee has a Georgian PE.

Both Cyprus and the BVI are on the Government list. Cyprus has a treaty with Georgia, so under note 3 it is not a preferential tax country for withholding. The domestic rate on the interest is therefore 5%, GEL 3,000 (arts. 131(1), 134(1)(b)). Under the treaty, interest paid to a Cyprus resident beneficial owner is taxable only in Cyprus (Georgia–Cyprus agreement, art. 11(1)), so the Georgian tax after relief is nil. The relief is given through the art. 125 procedure.

The BVI is in Part 1 with no treaty, so the royalty bears 15%, GEL 6,000 (art. 134(1^1)). Reverse-charge VAT on the royalty is left out of this example.

```oa-check
name: Interest to a Cyprus parent with treaty relief and a royalty to a BVI company, June 2026
inputs:
  interest_to_cyprus: 60000
  royalty_to_bvi: 40000
steps:
  - domestic_wht_interest: interest_to_cyprus * 0.05
  - treaty_wht_interest: interest_to_cyprus * 0
  - wht_royalty: royalty_to_bvi * 0.15
  - total_domestic_wht: domestic_wht_interest + wht_royalty
  - total_after_treaty: treaty_wht_interest + wht_royalty
  - treaty_saving: total_domestic_wht - total_after_treaty
expected:
  domestic_wht_interest: 3000.00
  treaty_wht_interest: 0.00
  wht_royalty: 6000.00
  total_domestic_wht: 9000.00
  total_after_treaty: 6000.00
  treaty_saving: 3000.00
```

## Ask the client first

1. Where is each payee resident, and does it have a certificate of residence from that country? Is it the beneficial owner?
2. Is any payee registered in a jurisdiction on the Government list, and does Georgia have a tax treaty in force with that country?
3. What exactly is being paid for (dividend, interest, royalty, management, other services), and where is the work done?
4. Does the foreign party have staff, an office, a site or a manager acting for it in Georgia, and for how long? That decides whether there is a PE.
5. Is the Georgian payer VAT-registered?
6. For individuals: how many days did the person spend in Georgia in any 12-month period ending in 2026?

## Sources

| Source | URL | Read on |
|---|---|---|
| Tax Code of Georgia, consolidated English text, publication of 15 October 2026 (arts. 22, 29, 34, 80, 81, 82, 97, 98^1, 98^2, 104, 124, 125, 130 to 132, 134, 154, 161, 162^1, 165^2, 166, 168, 175, 272, 274, 275, 309(146)) | https://matsne.gov.ge/en/document/view/1043717?publication=247 | 2026-10-31 |
| Tax Code of Georgia, Georgian original, same publication (arts. 125, 134) | https://matsne.gov.ge/ka/document/view/1043717?publication=247 | 2026-10-31 |
| Government of Georgia Ordinance No 615 of 29 December 2016, list of countries with preferential tax treatment | https://matsne.gov.ge/ka/document/view/3523434 | 2026-10-31 |
| Agreement between Georgia and Cyprus on the avoidance of double taxation (signed 13 May 2015, in force 4 January 2016), arts. 10 to 12 | https://matsne.gov.ge/ka/document/view/3161306 | 2026-10-31 |
| Revenue Service, resident certificate check | https://www.rs.ge/residence | 2026-10-31 |

Not yet confirmed: the Minister of Finance order under art. 125 (whether treaty relief is given at source or only by refund, the form, and what documents a non-resident must give); the list of Georgia's treaties in force (the Ministry of Finance and Revenue Service treaty pages did not load as text, so treaty rates other than Cyprus are left out); whether the Cyprus agreement has been amended by protocol or by the Multilateral Instrument; how a Georgian resident applies for a certificate of residence (the rs.ge page read only checks one); the Minister of Finance rules for non-resident suppliers of services to consumers (art. 165^2(2)(e)) and for reverse-charge reporting (art. 161(4)); the procedure for granting residence to foreign individuals under art. 34(6^2); whether a royalty for a licence counts as a service for reverse charge in every case.
