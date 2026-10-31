---
name: bh-cross-border-tax
description: >
  Bahrain cross-border tax for the 2026 tax year. Covers what Bahrain law does
  and does not impose on cross-border income: no withholding tax on dividends,
  interest, royalties or service fees paid to non-residents; residence of
  companies under the Domestic Minimum Top-up Tax (DMTT) and the NBR 183-day
  test for individuals' certificates of residence; permanent establishment under
  the DMTT Executive Regulations; the 46% hydrocarbon income tax on foreign
  companies; how foreign taxes count as Covered Taxes in place of a foreign tax
  credit; treaty access, the certificate of residence procedure and mutual
  agreement; and DMTT deregistration on exit. Use for "withholding tax Bahrain",
  "Bahrain tax residence certificate", "permanent establishment Bahrain",
  "Bahrain double tax treaty", "paying a foreign supplier from Bahrain" and
  "leaving Bahrain tax". Out of scope: transfer pricing and CbCR
  (bh-transfer-pricing), the DMTT computation (bh-corporate-income-tax),
  individuals (bh-income-tax), VAT on imports (bahrain-vat).
jurisdiction: BH
category: international
tax_year: 2026
tier: 2
last_updated: 2026-10-29
version: 0.1
trust_label: Built by Michael Cutajar and the OpenAccountants team
---

# Bahrain cross-border tax v0.1

Tax year 2026. Bahrain taxes income through two laws only: the Income Tax Law
for hydrocarbon companies (Legislative Decree No. 22 of 1979) and the Domestic
Minimum Top-up Tax on multinational groups (Decree-Law No. 11 of 2024, in force
from 1 January 2025). Most cross-border questions in Bahrain therefore have a
short answer: there is no Bahrain tax to withhold or credit. This skill states
what exists, what does not, and the source for each. The DMTT Law and its
Executive Regulations are read in the National Bureau for Revenue's (NBR)
English translation, which it marks "unofficial"; the Arabic text governs.

## Who this applies to

- **A Bahrain business paying a non-resident** (dividends, interest, royalties,
  management or technical fees). Bahrain imposes no withholding tax on these
  payments (see the base section).
- **A non-resident company doing business in Bahrain.** It is taxed in Bahrain
  only if it is a hydrocarbon company or a member of a multinational group in
  scope of the DMTT. The Income Tax Law taxes every body corporate "wheresoever
  established or incorporated" that explores for, produces or refines
  hydrocarbons in Bahrain (Income Tax Law art. 2). The DMTT reaches a
  non-resident group member through a Bahrain permanent establishment (DMTT Law
  art. 5(D); NBR DMTT FAQ 2.5).
- **A Bahrain company or individual with foreign income** who needs a foreign
  treaty rate. The NBR issues certificates of residence (COR) to individuals,
  businesses and government entities resident in Bahrain (NBR COR page).
- **Individuals moving to or leaving Bahrain.** The Income Tax Law taxes only
  bodies corporate, establishments and companies (art. 1(a)), so a move in or
  out has no Bahrain income tax effect. Social insurance on a move is in
  bh-payroll-social.

## Rates, bands and thresholds

| Item | Rate or amount | Year | Source URL |
|---|---|---|---|
| Withholding tax on dividends, interest, royalties and service fees paid to non-residents | None: neither income tax law has a withholding provision | 2026 | https://www.lloc.gov.bh/Legislation/id/L2279 ; https://www.nbr.gov.bh/laws_regulations/dmtt |
| Hydrocarbon income tax, residents and non-residents alike | 46% | 2026 | https://www.lloc.gov.bh/Legislation/id/L2279 |
| DMTT Minimum Rate | 15% | 2026 | https://www.nbr.gov.bh/laws_regulations/dmtt |
| DMTT Revenue Test | EUR 750 million or more in 2 of the 4 preceding Fiscal Years | 2026 | https://www.nbr.gov.bh/laws_regulations/dmtt |
| COR for an individual: physical presence | At least 183 days in the year the COR covers | 2026 | https://www.nbr.gov.bh/FTR/certificate_of_tax_residence |
| Permanent establishment: building, construction, assembly or installation site | Only if it lasts more than 12 months | 2026 | https://www.nbr.gov.bh/laws_regulations/dmtt |
| Double taxation treaties in force | 51 (plus 10 information exchange agreements and 6 air transport agreements) | 2026 | https://www.nbr.gov.bh/FTR/bahrain_tax_treaties_network |
| MLI in force for Bahrain | From 1 June 2022 | 2026 | https://www.nbr.gov.bh/FTR/bahrain_tax_treaties_network |
| MAP request time limit where the treaty sets none | 3 years | 2026 | https://www.nbr.gov.bh/publications/view/Bahrains_Mutual_Agreement_Procedure_MAP_Guidance |
| DMTT deregistration application | Within 30 days of the event | 2026 | https://www.nbr.gov.bh/laws_regulations/dmtt |

## The taxable base

**Withholding tax.** Bahrain has no withholding tax on payments to
non-residents. The Income Tax Law has 13 articles and none provides for
withholding (Legislative Decree No. 22 of 1979, arts. 1-13). The DMTT Law and
Executive Regulations tax the Bahrain profits of in-scope groups through the
Filing Constituent Entity and contain no withholding obligation (DMTT Law
arts. 3, 18, 22). A Bahrain company pays the non-resident the gross amount, files
no withholding return and issues no withholding certificate.

**Residence of companies.** Bahrain has no general residence rule for companies
because it has no general corporate income tax. For the DMTT, an Entity is
located in the jurisdiction where it is tax resident "based on its place of
management, place of creation, or any other similar criteria", and otherwise
where it was created (DMTT Law art. 5(A)). For a COR, a business needs a valid
Commercial Registration certificate and, for regulated or professional firms,
its licence (NBR COR page).

**Residence of individuals.** No Bahrain law taxes individuals on income, so
there is no statutory residence test. For a COR the NBR requires physical
presence in Bahrain of at least 183 days in the year; the NBR checks this with
the Nationality, Passport and Residence Affairs office and calls it
"absolute" (NBR COR page). It also needs a valid Bahraini identity card,
passport and, for non-Bahrainis, residency permits for the year.

**Permanent establishment.** For the DMTT, a non-resident group member has a
permanent establishment in Bahrain if it has a fixed or permanent place of
business here, a dependent agent who habitually exercises authority to conduct
business for it, or another nexus set by Ministerial decision (Executive
Regulations, Decision No. 172 of 2024, art. 4(A)). A fixed place includes a
place of management, branch, office, factory, workshop, mine, oil or gas well
or quarry, and a building, construction, assembly or installation site lasting
more than 12 months (ER art. 4(B)). Storage, display, delivery, purchasing and
information-gathering places are excluded where the activity is preparatory or
auxiliary (ER art. 4(C)), but not where the activities of the entity and a
related person together form a cohesive business (ER art. 4(D)). A Bahraini
branch of a group member is a permanent establishment (NBR DMTT FAQ 2.4).

**Relief for foreign tax.** Bahrain law has no foreign tax credit. The
Income Tax Law lets a hydrocarbon taxpayer deduct from its tax only other taxes
paid to the Government of Bahrain (art. 3). Under the DMTT, foreign tax works
differently: Covered Taxes include taxes recorded in a Constituent Entity's
financial accounts with respect to its income or profits (DMTT Law art. 7(A)(1)).
Foreign tax on the Bahrain entity's income therefore raises its Effective Tax
Rate and lowers the top-up, which is the 15% Minimum Rate less the Effective Tax
Rate (DMTT Law art. 9(A)). The allocation rules move some taxes to another
entity: tax relating to a permanent establishment goes to the permanent
establishment, controlled foreign company tax goes to the controlled company,
and tax on a distribution goes to the entity that made it (ER art. 29(A), (C)
and (G)).

**Exit and cessation.** Bahrain has no exit tax. Under the DMTT, a Registrant
must apply to deregister within 30 days when the group no longer has Bahrain
entities (for example after liquidation), is no longer a multinational group, or
otherwise falls outside the law (ER art. 63(A)-(B)). The NBR will not approve
deregistration while any amount or obligation is outstanding (ER art. 63(C)).

## Deadlines and filing

| Obligation | Deadline | Where | Source |
|---|---|---|---|
| Withholding tax return or payment | None: no withholding tax | n/a | Income Tax Law arts. 1-13; DMTT Law |
| Certificate of residence | No fixed deadline. The timeframe depends on how complete the request is | Foreign Tax Relations Directorate, NBR, by mail, e-fax or email to FTR@nbr.gov.bh, in Arabic or English | NBR COR page |
| MAP request | Within the time limit in the treaty; 3 years where the treaty sets none | NBR competent authority, Competent.Authority@nbr.gov.bh | NBR MAP Guidance |
| DMTT registration by the Filing Constituent Entity, incl. for a Bahrain permanent establishment | 120 days from the first day of the Transition Year | NBR | ER art. 62(A) |
| DMTT deregistration on exit | 30 days from the event | NBR | ER art. 63(B) |
| Hydrocarbon estimated income tax declaration | 15th day of the third month of the taxable year | Minister of Finance and National Economy | Income Tax Law art. 8 |

**COR request contents.** The applicant sends a request letter that states the
purpose and cites the treaty articles or foreign law relied on, supported by an
opinion of independent legal counsel or another independent qualified expert.
Documents are certified by an independent lawyer, notary or auditor, or shown in
original to NBR officials. The request also includes a justification from the
body asking for the COR (for example the foreign tax authority), that body's
contact details, the agent's letter of engagement if an agent applies, and,
if the foreign authority asks, evidence of withholding tax paid (NBR COR page).

## Penalties and interest

There is no withholding tax, so there are no withholding penalties.

For a non-resident group member with a Bahrain permanent establishment in scope
of the DMTT, the DMTT fines apply: failing to register on time or registering
with incorrect information, up to BHD 100,000; late or missing return, up to
30% of the tax that should have been declared; late payment, 1% of the unpaid
tax for each month or part of a month, capped at 70% (DMTT Law art. 28(A)(1)-(3)).
For a hydrocarbon company, late filing or payment adds 1% for each 30 days or
part of 30 days (Income Tax Law art. 8).

## Cross-border points

- **Treaty rates for payments out of Bahrain.** A non-resident does not need a
  treaty to reduce Bahrain withholding, because there is none. A treaty matters
  to a non-resident in Bahrain mainly for the permanent establishment definition
  and for MAP.
- **Treaty rates for payments into Bahrain.** A Bahrain resident claims the
  reduced rate in the payer's country with a Bahrain COR (NBR COR page). The
  payer country's own forms and rules apply there.
- **Treaty network.** 51 double taxation treaties, 10 tax information exchange
  agreements and 6 air transport agreements are in force (NBR Tax Treaties
  Network page). Under Bahrain law a treaty in force overrides all other
  domestic law except the Constitution (NBR MAP Guidance).
- **MLI.** Bahrain signed the Multilateral Instrument on 27 November 2020; it
  entered into force for Bahrain on 1 June 2022 (NBR Tax Treaties Network page).
- **Disputes.** Every Bahrain treaty has a MAP article; MAP covers transfer
  pricing cases, anti-abuse claims and multi-year cases (NBR MAP Guidance).
- **Transfer pricing and CbCR** are in bh-transfer-pricing.

## Worked examples

### 1. Bahrain company paying three foreign suppliers

A Bahrain trading company pays a UK parent a dividend of BHD 300,000, a Dutch
lender interest of BHD 50,000 and a US software owner a royalty of BHD 100,000.
Bahrain has no withholding tax, so the company withholds nothing and pays the
full BHD 450,000 (Income Tax Law arts. 1-13; DMTT Law). No Bahrain withholding
return is due. Each recipient's own country decides how it taxes the income.

```oa-check
name: Bahrain payments to non-residents, no withholding tax
inputs:
  dividend: 300000
  interest: 50000
  royalty: 100000
  bahrain_wht_rate: 0
steps:
  gross_paid: dividend + interest + royalty
  wht: gross_paid * bahrain_wht_rate
  net_received: gross_paid - wht
expected:
  gross_paid: 450000
  wht: 0
  net_received: 450000
```

### 2. Foreign tax on royalty income of a Bahrain DMTT entity

A Bahrain company in a group that meets the EUR 750 million DMTT Revenue Test
licenses software to a customer abroad and earns a royalty of BHD 1,000,000.
The customer's country withholds 10% under its treaty with Bahrain, after the
company shows a Bahrain COR; **10% is an assumed foreign rate for this example,
not a Bahrain figure**. The BHD 100,000 is recorded in the company's accounts
as tax on its income, so it is a Covered Tax (DMTT Law art. 7(A)(1)). The tax
expense is added back in computing Constituent Entity Income (ER art. 12(A)(1),
Net Taxes Expense). Assume the royalty is the group's only Bahrain income, with
no costs, no other adjustments and no Substance-based Income Exclusion, so
Constituent Entity Income is BHD 1,000,000. The Effective Tax Rate is 10%, the
top-up rate is 5% and the
DMTT is BHD 50,000 (DMTT Law art. 9). Without the foreign tax the DMTT would be
BHD 150,000, so the foreign tax reduces it by BHD 100,000. Bahrain gives no
refund or credit beyond that.

```oa-check
name: Bahrain DMTT with foreign withholding as Covered Tax
inputs:
  royalty: 1000000
  assumed_foreign_wht_rate: 0.10
  minimum_rate: 0.15
  sbie: 0
steps:
  covered_taxes: royalty * assumed_foreign_wht_rate
  etr: covered_taxes / royalty
  top_up_rate: max(0, minimum_rate - etr)
  taxable_income: max(0, royalty - sbie)
  dmtt: top_up_rate * taxable_income
  dmtt_without_foreign_tax: minimum_rate * taxable_income
  reduction: dmtt_without_foreign_tax - dmtt
expected:
  covered_taxes: 100000
  etr: 0.10
  top_up_rate: 0.05
  dmtt: 50000
  dmtt_without_foreign_tax: 150000
  reduction: 100000
```

## Ask the client first

- Who is paying whom, from which country, and for what (dividend, interest,
  royalty, services)?
- Is the Bahrain company, or the foreign company working in Bahrain, part of a
  group with revenue of EUR 750 million or more in two of the last four years?
- Does any group company explore for, produce or refine hydrocarbons in
  Bahrain?
- Does the foreign company have an office, branch, site lasting over 12 months
  or a dependent agent in Bahrain?
- For a COR: which year, which treaty and article, and (for an individual) how
  many days were spent in Bahrain that year?
- Is the group leaving Bahrain, and are any NBR amounts or filings outstanding?

## Sources

| Source | URL | Read on |
|---|---|---|
| Legislative Decree No. 22 of 1979, Income Tax Law, arts. 1-13 (LLOC English) | https://www.lloc.gov.bh/Legislation/id/L2279 | 2026-10-29 |
| Decree-Law No. 11 of 2024 (DMTT Law), arts. 1, 3, 5, 7, 9, 18, 22, 28, 44 (NBR unofficial English) | https://www.nbr.gov.bh/laws_regulations/dmtt | 2026-10-29 |
| Decision No. 172 of 2024, DMTT Executive Regulations, arts. 4, 29, 62, 63 (NBR unofficial English) | https://www.nbr.gov.bh/laws_regulations/dmtt | 2026-10-29 |
| NBR DMTT FAQs 2.4 and 2.5 | https://www.nbr.gov.bh/dmtt_faqs/2 | 2026-10-29 |
| NBR, Certificate of Residence for Tax Purposes | https://www.nbr.gov.bh/FTR/certificate_of_tax_residence | 2026-10-29 |
| NBR, Tax Treaties Network | https://www.nbr.gov.bh/FTR/bahrain_tax_treaties_network | 2026-10-29 |
| NBR, Guidance on Mutual Agreement Procedure, version 1.1 | https://www.nbr.gov.bh/publications/view/Bahrains_Mutual_Agreement_Procedure_MAP_Guidance | 2026-10-29 |

Not yet confirmed: an NBR or Ministry statement in terms that Bahrain has no
withholding tax (the rule above rests on reading both income tax laws in full,
which contain none); any fee for a certificate of residence and the time the
NBR takes to issue one; whether any Ministerial decision under ER art. 4(A)(3)
has set an extra permanent establishment nexus; Bahrain's MLI positions and
which treaties the MLI modifies; the withholding rates in each treaty partner's
law and treaty, which the paying country applies.
