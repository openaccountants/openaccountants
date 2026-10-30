---
name: sm-cross-border
description: >
  San Marino cross-border tax for 2026: residence of individuals and companies, San Marino-source income of non-residents, permanent establishment (including the three-month construction test), the October 2026 identification rule for non-residents, final withholding on payments abroad (13% interest, 11% qualifying bonds, 5% dividends to individuals, 20% professional and self-employed services, 3% artistic and sports performers, 10% equipment and vehicle rentals), bank interest rates, the Finance circular 1/2026 on interest paid to foreign banks and rentals paid to foreign operators (B2B withholding and B2C self-assessment at 18% by 31 July 2027), the corporate and personal foreign tax credit, treaty priority and international advance agreements. Use for San Marino withholding tax, non-resident income, payments to Italy or other countries, PE and foreign tax credit questions. Treaty rates need the actual treaty text.
jurisdiction: SM
category: cross-border
tax_year: 2026
tier: 2
last_updated: 2026-10-30
version: 0.4
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# San Marino cross-border tax v0.4

Tax year: calendar year 2026. Currency EUR. Authority: UO Ufficio Tributario (Tax Office), Dipartimento Finanze e Bilancio.

## 1. Who this applies to

- **Resident individuals:** registered residence for most of the tax period, or actually living in San Marino for most of the period, or centre of vital interests in San Marino; taxed on worldwide income ([IGR arts 1-2, 10][igr]).
- **Resident companies:** registered office or effective management in San Marino for most of the tax period; taxed on worldwide income ([IGR art 42][igr]).
- **Non-residents:** taxed on the San Marino-source income listed in article 5, by final withholding at payment where articles 102-104 apply and otherwise by return ([IGR art 5][igr]).
- **Treaties:** the domestic rule applies where it is more favourable than the treaty ([IGR art 9][igr]). Apply a treaty rate only from the treaty text in force.

## 2. Rates, bands and thresholds

| Payment by a San Marino payer | Rate | Tax year | Source |
|---|---|---|---|
| Capital income (including interest) paid by economic operators, the State and public or private bodies to anyone other than San Marino banks, financial and management companies | 13% final | 2026 | [IGR art 103(1)][igr] |
| Interest on San Marino bonds and similar debt of 36 months or more, not repaid early | 11% final | 2026 | [IGR art 103(1)][igr] |
| Bank and financial-company interest: current and deposit accounts | 13% | 2026 | [IGR art 103(2)(a)][igr] |
| Bank and financial-company: repurchase agreements | 6% | 2026 | [IGR art 103(2)(b)][igr] |
| Bank and financial-company: certificates of deposit under 18 months / 18 months or more | 6% / 5% | 2026 | [IGR art 103(2)(c)][igr] |
| Bank and financial-company: bonds issued by authorised entities | 5% | 2026 | [IGR art 103(2)(d)][igr] |
| Dividends paid by a resident capital company to individuals | 5% final | 2026 | [IGR art 103(6)][igr] |
| Dividends paid to non-individuals | Nil, if the recipient declares it does not act for an individual | 2026 | [IGR art 103(6)][igr] |
| Self-employed and assimilated services (article 27) paid to non-residents, including when supplied by a business | 20% final | 2026 | [IGR art 102(1)][igr] |
| Artistic, cultural or sports services as defined by Tax Office circular; airport and naval services abroad for aviation or shipping operators | 3% final | 2026 | [IGR art 102(2)][igr] |
| Use of industrial, commercial or scientific equipment and vehicles situated in San Marino, including finance leases, paid to non-residents | 10% final | 2026 | [IGR art 104(5)][igr] |
| Non-resident B2C recipient (circular 1/2026 route) | 18% on the return for tax years 2026-2030; an Italian recipient applies the treaty rates of 13% (capital income) or 10% (rentals) | 2026 | [Finance circular 1/2026, pp. 2-3][circ1]; [Law 141/2025, art 54(6)][l141] |
| Construction or installation site as a permanent establishment | Only if it lasts more than three months | 2026 | [IGR art 4][igr] |

Documented travel, board and lodging reimbursements and costs incurred in the client's name are not subject to the 20% withholding ([IGR art 102(3)][igr]). Withholding on interest paid to resident companies is on account, not final ([IGR art 103(8)][igr]).

## 3. The base

**Source.** Article 5 lists San Marino-source income: land and buildings in San Marino; capital income paid by the State, residents or San Marino permanent establishments; employment paid by residents; professional work; business through a permanent establishment; and other listed categories ([IGR art 5][igr]).

**Capital income carve-outs (from 2026).** Interest and similar income from current accounts, deposits, certificates of deposit, repos and San Marino-issued bonds paid by authorised entities under Law 165/2005 are not San Marino-source. Capital income is also not San Marino-source where the payer is non-resident, or where the payer is a San Marino bank or financial company and the recipient is a foreign bank, a foreign entity doing equivalent reserved activities for its own account, or a foreign collective investment undertaking ([IGR art 5(1)(b), replaced by DD 156/2026, art 2(1)][dd156]). Interest paid by an ordinary San Marino business to a foreign bank is San Marino-source and taxed at 13%.

**Identification of non-residents.** Non-resident individuals and economic operators not subject to final withholding are identified by an ISS code or an economic-operator code (COE) from ASE-CC. A non-resident operator can instead appoint a San Marino tax representative, jointly liable for compliance and record-keeping, who requests the COE. Identification does not of itself create a permanent establishment ([IGR art 5(4-bis), added by DD 156/2026, art 2(2)][dd156]).

**Permanent establishment.** A fixed place of business with the listed examples; a construction, assembly or installation site (with connected supervision) only beyond three months; habitual contract-concluding agents; preparatory and auxiliary activities excluded; common control alone does not create a permanent establishment ([IGR art 4][igr]).

**Foreign-bank interest and foreign rentals (Finance circular 1/2026 of 5 August 2026).**

The circular covers interest paid by San Marino residents (businesses and private persons, not financial operators) to foreign banks, and rent paid to foreign operators for equipment, goods and vehicles under article 104(5) ([Finance circular 1/2026, p. 1][circ1]). Overdraft interest and interest on advances from foreign banks are covered.

1. **B2B.** A San Marino economic operator paying interest to a foreign bank, or rent for equipment or vehicles to a foreign operator without a San Marino permanent establishment, withholds 13% (interest) or 10% (rental) and remits it in the two-month period after payment ([Finance circular 1/2026, pp. 1-2][circ1]). Default interest follows the character of the underlying obligation.
2. **B2C.** Where the payer is a private resident, the foreign recipient files its own San Marino return for 2026 income by 31 July 2027 and pays the IGR due in one payment by the same date, at 18% unless a treaty applies; there are no advances. The return system is due in April 2027 and an operating manual in early 2027 ([Finance circular 1/2026, pp. 2-3][circ1]).
3. Income is taxed when paid: a 2026 payment of income accrued in 2025 is taxed in full; income accrued but unpaid because the San Marino debtor is insolvent is not taxed ([Finance circular 1/2026, p. 3][circ1]).
4. If the payer neither withholds nor remits, the recipient is jointly liable once the payer is entered on the roll. If the payer withheld correctly but did not remit, the foreign bank or operator is not liable ([IGR art 131][igr]; [Finance circular 1/2026, p. 3][circ1]).

## 4. Deadlines and filing

| Obligation | Deadline | Source |
|---|---|---|
| Remit tax withheld | By the end of the two-month period after the month of payment | [IGR art 125(1)][igr] |
| Financial-institution payers | 50% advance on prior-year withholding by 31 July; balance in the first two months of the following year | [IGR art 125(2)][igr] |
| Non-resident return (where no final withholding) | 31 July following the tax year | [IGR art 93(1)][igr] |
| B2C non-resident return and payment for 2026 income (circular 1/2026 route) | 31 July 2027 | [Finance circular 1/2026, p. 3][circ1] |

The payer's withholding return frees the recipient from filing for income under final withholding ([IGR art 125(3)][igr]). Keep certificates of tax withheld, stamped by the Tax Office, for the recipient's foreign credit claim ([Finance circular 1/2026][circ1]).

## 5. Penalties and interest

Late remittance of withholding carries interest at the legal rate plus 2 points ([IGR art 128][igr]). Failure to withhold, failure to remit and late or omitted returns carry the penalties in articles 138-139 ([IGR arts 138-139][igr]). A late return within 30 days of the deadline costs 200 (400 after), and is null after 30 days for refund purposes ([IGR arts 93, 139(1)(d), replaced by DD 156/2026, art 16][dd156]). Paying an assessment within 60 days halves the penalties ([IGR art 129][igr]).

## 6. Cross-border points

**Corporate foreign tax credit.** Final, non-refundable foreign tax on foreign income included in the base is credited up to the share of net San Marino tax that the foreign income bears to total income, State by State ([IGR art 44(1)-(3)][igr]). For income not earned through a foreign permanent establishment, foreign income for the fraction is total income x foreign gross receipts / total receipts ([IGR art 44(8)][igr]). No credit if the foreign income was not declared ([IGR art 44(5)][igr]). Foreign tax paid and not recovered can, under the conditions of article 44(7), be deducted in the following period; this is a deduction, not a carried-forward credit ([IGR art 44(7)][igr]).

**Personal foreign tax credit.** Same limit for individuals; business and self-employed income uses the receipts fraction ([IGR art 18][igr]). See `sm-income-tax`.

**International advance agreements.** Delegated Decree 116/2026 covers transfer pricing, entry and exit values, treaty PE status and profit attribution, and the application of rules on dividends, interest and royalties paid to or received from non-residents ([DD 116/2026, art 1][dd116]). See `sm-transfer-pricing`.

**Italy.** For the B2C return, circular 1/2026 states that under the Italy-San Marino treaty an Italian recipient applies the treaty rates of 13% on capital income and 10% on rentals instead of 18% ([Finance circular 1/2026, p. 2][circ1]). Confirm the recipient is an Italian treaty resident.

## 7. Two worked examples that recompute

### Example 1: B2B interest to a foreign bank and equipment rental

A San Marino company pays 10,000 of loan interest to a foreign bank (no San Marino permanent establishment) and 12,000 of rent for machinery located in San Marino to a foreign leasing company. Withholding: 1,300 on interest and 1,200 on rent, total 2,500, remitted by the end of the following two-month period.

```oa-check
name: San Marino 2026 B2B withholding on foreign-bank interest and equipment rent
inputs:
  interest_paid: 10000
  rent_paid: 12000
  interest_rate: 0.13
  rental_rate: 0.10
steps:
  interest_withholding: interest_paid * interest_rate
  rental_withholding: rent_paid * rental_rate
  total_withholding: interest_withholding + rental_withholding
  bank_receives: interest_paid - interest_withholding
  lessor_receives: rent_paid - rental_withholding
expected:
  interest_withholding: 1300
  rental_withholding: 1200
  total_withholding: 2500
  bank_receives: 8700
  lessor_receives: 10800
```

If the payer were a private resident, there would be no withholding; the foreign recipient would self-assess 18% on its 2026 return (1,800 on 10,000 of covered income) by 31 July 2027.

### Example 2: corporate foreign credit, no foreign PE (edge case)

A San Marino company has taxable income of 100,000 and net IGR before credits of 18,000. Total gross receipts are 200,000, of which 40,000 come from one foreign State, which charged 5,000 of final tax. Foreign income for the fraction: 100,000 x 40,000 / 200,000 = 20,000. Credit limit 18,000 x 20,000 / 100,000 = 3,600. Credit 3,600; 1,400 is not credited (check article 44(7) for a deduction next year).

```oa-check
name: San Marino 2026 corporate foreign tax credit using the receipts fraction
inputs:
  total_taxable_income: 100000
  net_igr_before_credit: 18000
  total_receipts: 200000
  foreign_receipts: 40000
  foreign_tax_paid: 5000
steps:
  foreign_income_for_credit: total_taxable_income * foreign_receipts / total_receipts
  credit_limit: net_igr_before_credit * foreign_income_for_credit / total_taxable_income
  credit_allowed: min(foreign_tax_paid, credit_limit)
  foreign_tax_not_credited: foreign_tax_paid - credit_allowed
expected:
  foreign_income_for_credit: 20000
  credit_limit: 3600
  credit_allowed: 3600
  foreign_tax_not_credited: 1400
```

## 8. Ask the client first

1. Payer and recipient: residence, whether a business, bank or private person, and any San Marino permanent establishment.
2. Nature of each payment (interest, dividend, service fee, rent, royalty) and the contract.
3. Payment dates and amounts in 2026.
4. Treaty State of the recipient and residence certificate.
5. For San Marino recipients of foreign income: foreign tax paid, final assessment and receipts split by State.

## Sources

| Source | URL | Read on |
|---|---|---|
| Law 166/2013 (IGR), official coordinated text updated to 22 December 2025: arts 1-5, 9-10, 18, 42-44, 93, 102-104, 125, 128-131, 138-139 | https://www.consigliograndeegenerale.sm/on-line/documento17086436.html | 2026-10-30 |
| Delegated Decree 156/2026 of 12 October 2026, arts 2, 16, 19 | https://www.bollettinoufficiale.sm/on-line/RicercaBU?operation=getDocBU&id=9c3a0dfeb72a7aeab52d1c5c0440879b4cf2ad33 | 2026-10-30 |
| Law 141/2025 of 12 November 2025, art 54(6) | https://www.consigliograndeegenerale.sm/on-line/home/archivio-leggi-decreti-e-regolamenti/documento17155359.html | 2026-10-30 |
| Finance department circular 1/2026 of 5 August 2026 (articles 5, 103 and 104 IGR), pp. 1-3 | https://www.finanze.sm/pub2/dam/jcr%3Ac7b6c29b-5894-4a96-914b-00785958a63a/Circolare%20n.1-2026.pdf | 2026-10-30 |
| Delegated Decree 116/2026 (international advance agreements), art 1 | https://www.bollettinoufficiale.sm/on-line/RicercaBU?operation=getDocBU&id=26a68bf4326bc216b251bc3af7fd385bc9f7c7a0 | 2026-10-30 |

Not yet confirmed: a separate withholding rate for royalties (the earlier version's 20% royalty rate; article 102 covers article 27 self-employed income, and whether a given royalty falls in article 27 depends on its character); the list of San Marino tax treaties in force and their rates; the conditions of the article 44(7) deduction; exit taxation of companies.

[igr]: https://www.consigliograndeegenerale.sm/on-line/documento17086436.html
[l141]: https://www.consigliograndeegenerale.sm/on-line/home/archivio-leggi-decreti-e-regolamenti/documento17155359.html
[dd156]: https://www.bollettinoufficiale.sm/on-line/RicercaBU?operation=getDocBU&id=9c3a0dfeb72a7aeab52d1c5c0440879b4cf2ad33
[dd116]: https://www.bollettinoufficiale.sm/on-line/RicercaBU?operation=getDocBU&id=26a68bf4326bc216b251bc3af7fd385bc9f7c7a0
[circ1]: https://www.finanze.sm/pub2/dam/jcr%3Ac7b6c29b-5894-4a96-914b-00785958a63a/Circolare%20n.1-2026.pdf

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
