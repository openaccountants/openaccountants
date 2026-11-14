---
name: set-up-your-company-in-kenya-we-handle-it-from-abroad
description: "Setting up a company in Kenya from abroad: how I do it"
jurisdiction: KE
tax_year: 2026
last_updated: 2026-11-14
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: formation
version: 0.1
type: filing-howto
category: formation
---

# Setting up a company in Kenya from abroad (2026)

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Scope

This is the execution workflow for a foreign founder establishing a Kenyan private subsidiary or registering an existing foreign company as a branch. It preserves the distinction between incorporation, bank KYC, tax registration and permission to work. Do not promise remote completion of every step: representative authority, identity verification and any in-person bank/immigration requirement must be established first. A branch extends the parent; a subsidiary is a separate incorporated person.

Use [ke-company-formation](ke-company-formation.md) for legal-form/member/director/capital rules and registry/BO/annual-return deadlines. Use [ke-corporate-income-tax](ke-corporate-income-tax.md) for subsidiary/branch rates and repatriated-income tax; the old claim that a branch simply pays a higher ordinary rate is stale.

## Ask the client first

- New subsidiary or existing-parent branch; parent liability, future investors and tax structure.
- Sector, licences and any local-equity restriction, especially insurance, telecommunications, mining or private security.
- Directors/shareholders, nationalities, residence, beneficial owners and control.
- Whether a founder will work/live in Kenya and their immigration status.
- Names, Kenyan office/postal address, passport/address documents and any foreign company constitution/certificate.
- Authority for an agent to act, available authenticated documents, bank requirements and proposed funding.

## The method, step by step

### Execution order and government charges

| Item | Amount/condition | Official source |
|---|---|---|
| Foreign-company registry | KES 7,550; FC2,FC4,FC6, incorporation certificate, constitution, notarized memorandum/articles and local representative acceptance; certificate of compliance | https://brs.go.ke/fee-schedule-companies-registry/ |
| Published foreign/private registration processing | 3-5 days in BRS schedule; estimate, not full-launch guarantee | https://brs.go.ke/fee-schedule-companies-registry/ |
| Local representative | At least 1 for foreign-company registration, Companies Act s979, in words on the page; obtain prescribed requirements | https://brs.go.ke/wp-content/uploads/2023/03/CompaniesAct17of2015.pdf |
| Class G processing fee | KES 20,000 non-refundable; actual business/consultancy permit, not incorporation fee | https://immigration.go.ke/class-g-specific-trade-business-or-consultancy/ |
| Class G issuance | KES 250,000 per year; EAC Member States gratis as authority states | https://immigration.go.ke/class-g-specific-trade-business-or-consultancy/ |
| Class G capital evidence | At least USD 100,000 to be invested; proof of capital, not fee | https://fns.immigration.go.ke/infopack/permits/classG/ |

1. **Choose structure before filing.** Establish business substance, legal liability, intended investors, distribution plans and tax/treaty facts. Do not choose a subsidiary merely by comparing the old ordinary-rate figures; the current branch treatment includes repatriated-income tax.
2. **Use BRS/eCitizen and the correct application.** Private incorporation uses the forms in [ke-company-formation](ke-company-formation.md). Foreign-company registration uses the BRS foreign row above. Verify proposed names against BRS restrictions, including similarity and restricted names; do not assume the old separate KES 150 reservation charge survives the live flow.
3. **Collect and authenticate the right documents.** For a branch BRS expressly lists notarized memorandum/articles. Obtain clear foreign passport/identity, addresses, corporate records and agent authority appropriate to the live application. Do not treat a general power of attorney as proof every bank/registry/immigration step can be completed without the founder. Foreign-language immigration documents need authorised English translation per eFNS.
4. **Confirm the local representative.** A foreign company needs the representative under s979 and prescribed foreign-company regulations. Under s981, the representative answers for compliance and is personally liable to a company penalty only if the court is satisfied they should be liable; it is not automatic liability for every parent debt. Subsidiary director requirements are ss128-129; do not sell an unnecessary resident nominee as a universal legal requirement. Check bank/PIN practical requirements separately.
5. **Submit, pay and verify registration.** Review the live government invoice, authenticate/sign required forms, pay, retain submission/payment acknowledgements, obtain the correct certificate, and reconcile registered shareholders, directors, office and beneficial owners. A certificate of incorporation and a foreign certificate of compliance are different outcomes.
6. **Prepare and lodge beneficial ownership.** Use the sourced preparation/amendment deadlines in [ke-company-formation](ke-company-formation.md). The old wording measured the first deadline from incorporation and treated every ownership change as the filing event; the Act read measures completion/preparation and making amendments. Obtain the current form and regulations for this structure.
7. **Verify KRA PINs and obligations.** Confirm company and relevant individual/director PIN requirements and links through iTax (https://itax.kra.go.ke), retaining certificates and authorised representation. Do not assume the current BRS integration or a separate manual application without inspecting what has actually issued.
8. **Obtain bank acceptance.** Assemble the incorporation/compliance certificate, CR12/registered ownership information, directors' identity/PINs, office, beneficial ownership and source-of-funds evidence requested by the bank. The bank makes its own decision and may require attendance; do not promise the old 2-week completion estimate.
9. **Obtain immigration permission where needed.** Class G covers a person intending a specific trade, business, consultancy or profession other than a prescribed profession. Use the current Directorate/eFNS checklist: Form25, signed cover letter, passport, immigration status, photo, capital evidence, registration documents, PIN/CR12 and Form27. Company TCC applies for new cases; renewal requires company/individual TCCs and additional accounts/employment evidence. Log in via eCitizen single sign-on, choose Permit Issuance/Renewal, complete, submit, use the generated invoice, retain receipts and monitor official notifications. Do not work without the requisite permit/pass.
10. **Calendar continuing compliance.** Set annual registry return, beneficial-owner updates, tax return/balance payment and any VAT/payroll obligations. The old automatic strike-off claim after 5 unfiled years is not what s894 says: it sets an inquiry, notice and Gazette procedure where the Registrar reasonably believes the company is inactive. Treat missing returns seriously without inventing an automatic timer.

## Boundary and exception table

| Situation | Response |
|---|---|
| Branch/local representative | Establish prescribed eligibility and scope of court-determined penalty liability |
| Subsidiary/resident nominee proposed | Separate legal director requirement from bank/PIN practice; refer nominees |
| Class G investment evidence | Capital proof is distinct from government fees; employment may require a different permit, not automatic waiver of Class G capital |
| EAC nationality | Check the Directorate's gratis treatment and correct permit route |
| Regulated/foreign ownership or layered controls | Specialist licence, equity and beneficial-ownership review before promises |

## Worked cases

Permit budget: on a hypothetical approved Class G case for 1 year, published processing KES 20,000 plus issuance KES 250,000 totals KES 270,000, before other actual fees. USD 100,000 capital evidence is not added to KES fees or treated as a payment to government.

```oa-check
name: Class G government fee distinction
inputs:
  processing: 20000
  annual_issuance: 250000
  years: 1
steps:
  - fees: processing + annual_issuance * years
expected:
  fees: 270000
```

Registry decision: BRS publishes KES 10,650 for a private company and KES 7,550 for a foreign registration. Difference KES 3,100 does not decide the structure: a branch retains parent liability and requires a local representative, and tax/bank/permit costs are separate. Use the legal/tax analysis before selecting the application.

```oa-check
name: Registry fees do not decide structure
inputs:
  private_fee: 10650
  foreign_fee: 7550
steps:
  - difference: private_fee - foreign_fee
expected:
  difference: 3100
```

## When to refuse or refer

Refer sector equity/licensing, nominee directors, remote identity/authority uncertainty, layered ownership, tax treaties, parent guarantees and immigration-category doubts. Never promise full foreign ownership across all sectors, bank acceptance or a permit merely from registration.

## Filing and payment

BRS/eCitizen registration, KRA tax obligations, bank KYC and eFNS immigration are separate tracks. Keep each invoice, receipt, acknowledgement and final approval in the handover file. Follow the issued immigration instructions on presenting printouts/endorsement; do not assume the founder can remain abroad throughout.

## Completion checklist

Reconcile intended structure to certificate and registered details; beneficial owners to control evidence; tax/PIN obligations to issued certificates; agent authority to each action; bank approval to its conditions; permit to intended activity; calendars to the relevant legal dates.

## Sources

| Source and passages actually read | Official URL | Read on |
|---|---|---|
| Read for BRS private/foreign registration fee, forms, certificates and processing rows | https://brs.go.ke/fee-schedule-companies-registry/ | 2026-11-14 |
| Read for Companies Act BRS 2021 revision ss13-19,93A,128-129,243,705,894,979-981, legal distinction and representative liability | https://brs.go.ke/wp-content/uploads/2023/03/CompaniesAct17of2015.pdf | 2026-11-14 |
| Read for Directorate Class G requirements, fees, EAC gratis treatment and renewal evidence | https://immigration.go.ke/class-g-specific-trade-business-or-consultancy/ | 2026-11-14 |
| Read for eFNS Class G application steps, translation, investment evidence, TCC distinction and presentation instructions | https://fns.immigration.go.ke/infopack/permits/classG/ | 2026-11-14 |
| Read for TPA ss8-13 taxpayer/PIN requirements | https://www.kra.go.ke/images/publications/Tax-Procedures-Act--2026.pdf | 2026-11-14 |

Not yet confirmed: Post-2021 changes to cited company-law passages and current foreign-company regulations/local-representative residence requirements. The old KES 150/30-day name-reservation combination, universal passport/address notarisation and address age under 3 months, 5-10-day foreign completion, 2-week banking, guaranteed power-of-attorney remote completion, compulsory resident subsidiary director/secretary for bank/PIN linking and automatic strike-off after 5 years are not established by the official texts opened. The claim that Class G capital proof disappears merely because a Kenyan company employs the applicant is unsupported; determine the correct employment permit. Nominal-capital stamp duty and current BOF1 requirements need the live filing rules.

> Contributed by Julian Njoroge Maina, 25241.
