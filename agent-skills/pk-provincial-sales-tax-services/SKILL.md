---
name: pk-provincial-sales-tax-services
description: "Pakistan provincial sales tax on services for 2026 (financial year 2026-27), centred on the Punjab Revenue Authority (PRA) and the withholding-agent rules. Answers whether a bank, company or government payer must withhold provincial sales tax when it pays a service provider who is liable to register but is not registered, how much is withheld in Sindh (SRB) and Khyber Pakhtunkhwa (KPRA), and how withholding agents and providers file and claim credit on PRA-Iris. Gives pointers for Balochistan (BRA). Trigger on PRA, Punjab sales tax on services, withholding agent, STWH invoice, unregistered service provider, SRB withholding, KPRA withholding and BRA. Federal goods sales tax and income tax withholding are separate skills."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/pk-provincial-sales-tax-services"
  jurisdiction: "PK"
  tax_year: "2026"
  last_updated: "2026-11-15"
---

# Pakistan provincial sales tax on services: withholding agents and unregistered providers, 2026 v1.0

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

**Quick answer.** Sales tax on services is provincial: Punjab (PRA), Sindh (SRB), Khyber Pakhtunkhwa (KPRA) and Balochistan (BRA) each have their own Act, rates and withholding rules. A bank is a company, and every province read here treats companies as withholding agents. In Punjab, PRA's registration system marks the withholding-agent box automatically for every company. In Sindh and Khyber Pakhtunkhwa the law read here makes a company paying an **unregistered** provider (one liable to register but not registered) withhold the **whole** tax at the applicable rate, not the reduced share it withholds from a registered provider. The Punjab Withholding Rules 2015, which set the Punjab share, could not be opened from an official source on 15 November 2026: do not state a Punjab percentage until they are read (see Sources). Withholding by the payer does not register the provider; the provider's own registration duty under its Act stays.

**Required inputs.** Province where the service is provided or received; the payer's legal form (company, government office, bank, registered person) and registrations; whether the provider is registered and active with that province; the service and its rate; whether the invoice shows tax; the contract value and whether it is inclusive of tax.

## Scope

Who this covers: service recipients that may be withholding agents (banks and other companies, government offices, autonomous bodies, registered persons) and service providers paid by them, in Punjab, Sindh, Khyber Pakhtunkhwa and Balochistan, for services provided in financial year 2026-27 (from 1 July 2026). Amounts are in Pakistani rupees (PKR).

Out of scope here, with the owner skill: the full provincial rate schedules, place-of-supply rules and Islamabad Capital Territory services in [pk-sales-tax-services](pk-sales-tax-services.md); federal sales tax on goods in [pk-sales-tax-federal](pk-sales-tax-federal.md); income tax withholding under the Income Tax Ordinance 2001 in [pk-withholding-tax](pk-withholding-tax.md). Provincial withholding and federal income tax withholding are separate deductions from the same payment.

## Ask the client first

1. In which province is the service provided, received or consumed, and does the payer have an office or place of business there?
2. What is the payer: a company (including a bank), a government or public-sector office, or another registered person? Is it registered with that province as a service provider, as a withholding agent only, or not at all?
3. Is the provider registered with that province and on its active taxpayers list? If not, is it registered with another province or with FBR?
4. What is the service, and is it taxed at the standard rate, a reduced rate or a fixed rate?
5. Does the invoice show the sales tax, and is the agreed price inclusive or exclusive of tax?
6. When was the invoice issued and when will payment be made?

## The method, step by step

1. **Find the province that taxes the service.** Each Act taxes services provided, received or consumed in its territory; a service can touch two provinces. Settle this with [pk-sales-tax-services](pk-sales-tax-services.md) before choosing a withholding rule.
2. **Decide whether the payer is a withholding agent in that province.** Use the categories in the table below. A bank is a company. Sindh adds a residence condition: a payer outside Sindh with no place of business there is a withholding agent only if it has signed up on Form SSTW-01.
3. **Check the provider's status.** Registered and active, registered but inactive, registered only in another province, or unregistered. An unregistered person in the Sindh rules is one "liable to be registered under the Act but is actually not registered".
4. **Apply the withholding share for that status.** Unregistered or inactive providers: the whole tax (Sindh rule 3(4); KP paragraphs 5(b) and 12). Registered providers: Sindh one-fifth for most agents, four-fifths for government agents; KP 50% in cases not listed for full withholding. Punjab: not confirmed, see Sources.
5. **Work out the tax on the right base.** Where the invoice shows no tax, Sindh uses the tax fraction on the gross amount (tax inside the price). KP treats a commercial invoice value as exclusive of tax and withholds the tax from within that value. Follow the contract if it says otherwise (Sindh rules 3(3) proviso and 3(4)).
6. **Keep the evidence.** For an unregistered provider take a copy of the CNIC (individual) or NTN certificate (company or association) and report it in the next return or statement (Sindh rule 3(4) proviso; KP paragraph 12).
7. **Deposit and file by the due date** in the table below, then give the provider a withholding certificate (Sindh Form SSTW-06; KP paragraph 13 on request).
8. **Tell the provider what withholding does not do.** It does not register the provider and, in Sindh, does not absolve a registered provider of its own tax liability (rule 3(3) proviso).

### Rates, bands and thresholds

| Item and conditions, financial year 2026-27 | Figure or rule | Official source |
|---|---|---|
| Sindh standard rate on taxable services; Second Schedule services carry their own rates | 15% (fifteen per cent of value) | [Sindh STS Act 2011 s.8(1), updated to Finance Act 2026](https://www.srb.gos.pk/srb/wp-content/uploads/2026/08/SSTOS_Act2011.pdf) |
| Khyber Pakhtunkhwa standard rate; Second Schedule services carry their own rates | 15% (fifteen per cent, standard or general rate) | [KP STS Act 2022 s.9(1), updated to Finance Act 2026](https://kpra.gov.pk/wp-content/uploads/2026/09/KPSTSA-2022-Updated-Finance-act-2026.pdf) |
| Balochistan standard rate; Third Schedule rates revised from 1 July 2026 | 15% (fifteen percent of value) | [BSTS Act 2015 s.10(1), amended by Finance Act 2026](https://ebra.com.pk/storage/uploads/downloads/1785387363.pdf); [BRA circular 10 July 2026](https://ebra.com.pk/storage/uploads/downloads/1784709123.pdf) |
| Sindh withholding agents | Government offices; autonomous bodies, state-owned enterprises and regulators not incorporated under the Companies Act; budget-funded organisations; companies; specified recipients of advertisement and other listed services; SRB-registered persons buying from unregistered or inactive persons | [Sindh Withholding Rules 2014 r.1(2)](https://www.srb.gos.pk/srb/wp-content/uploads/2026/08/SSTOS_withholdingrules2014.pdf) |
| Sindh, payer outside Sindh | Withholding agent only if resident in Sindh or with a place of business there, or signed up on Form SSTW-01 | same |
| Sindh, registered provider, most agents | Withhold one-fifth of the tax shown on the invoice; illustration: tax 150 on value 1,000, withhold 30 | same, r.3(3) |
| Sindh, registered provider, government and public-body agents in r.1(2)(a)-(b) | Withhold four-fifths of the tax shown on the invoice | same, r.3(4A) |
| Sindh, unregistered or inactive provider | Withhold the tax at the applicable rate from the amount billed, on gross value by the tax fraction unless the contract says otherwise | same, r.3(4) |
| Sindh, services where the provider must collect the tax itself | No withholding on telecom, electric power transmission, banking company, financial institution, insurance (other than re-insurance), port, airport, terminal and airport ground services invoiced by an SRB-registered provider | same, r.3(1) proviso |
| Khyber Pakhtunkhwa withholding agents | Federal and provincial government offices, public-sector bodies, companies (including those registered with another tax authority), specified construction procurers, and others notified | [KP Withholding Regulation 2024 para 3(1)](https://kpra.gov.pk/wp-content/uploads/2025/01/KP-withholding-regulations-2024.pdf) |
| Khyber Pakhtunkhwa, full withholding | Advertisement; unregistered or inactive providers; services to government; unregistered out-of-province providers; reduced-rate services | same, para 5 |
| Khyber Pakhtunkhwa, other cases | 50% of the leviable tax | same, para 6 |
| Khyber Pakhtunkhwa, not withheld | Telecom, banking and courier services (except between such companies) | same, para 4 |
| Punjab, company as withholding agent | PRA-Iris registration marks the "Withholding Agent" box automatically and it cannot be edited for a company user | [PRA registration manual](https://e.pra.punjab.gov.pk/templates/PRA-Taxpayers-End-Registration-User-Manual-V0.1.pdf) |

### Deadlines and filing

| Item | Rule | Official source |
|---|---|---|
| Sindh, agent registered with SRB as a service provider | Deposit by the due date of the month in which it claims the input tax, or the payment date, whichever is earlier; if no credit is claimed within four months, by the payment date or within four months of the invoice | [Sindh Withholding Rules 2014 r.3(7)(i)](https://www.srb.gos.pk/srb/wp-content/uploads/2026/08/SSTOS_withholdingrules2014.pdf) |
| Sindh, other agents | Deposit by the 15th day of the second month after the invoice month, or the payment date, whichever is earlier; return SSTW-03 if not SRB-registered | same, r.3(7)(iii) and 3(8) |
| Sindh, government accounting offices | Intimation to SRB by the 15th of the following month; DDO return SSTW-03 by the 18th | same, r.3(6) |
| Khyber Pakhtunkhwa, agents registered with KPRA or FBR | Deposit by the 15th of the month after withholding, or the payment date, whichever is earlier | [KP Withholding Regulation 2024 para 8](https://kpra.gov.pk/wp-content/uploads/2025/01/KP-withholding-regulations-2024.pdf) |
| Khyber Pakhtunkhwa, other agents | Deposit by the 15th of the month after payment; monthly statement by the 18th, nil statement if no withholding | same, paras 8(3) and 11 |
| Punjab, agent not registered as a service provider | Files a monthly Sales Tax Withholding Statement on PRA-Iris, nil if nothing withheld, within the due date in the law and rules | [PRA-Iris FAQ 36, 37, 56](https://e.pra.punjab.gov.pk/templates/PRA_Iris_Sales_Tax_Return_FAQs.pdf) |
| Punjab, registered provider | Monthly return is mandatory even with no sales (nil return through Annexures C1 and C) | same, FAQ 48 |

### Who is liable when tax is not withheld or not deposited

- **Sindh.** A withholding agent that pays late owes default surcharge under s.44 of the Act (rule 3(9)). A provider that lets a non-agent withhold remains liable for the tax and surcharge (rule 4(4)).
- **Balochistan.** A person required to withhold that fails to withhold or deposit is personally liable for the tax (s.14(3)).
- **Khyber Pakhtunkhwa.** The provider cannot claim credit for withheld tax until the agent declares and deposits it (paragraph 7(3)). Failure to withhold or deposit is assessed by show cause notice under s.27 with penalty and default surcharge; a missed monthly statement counts as a missed return (paragraph 14).
- **Punjab.** A provider gets credit only for an STWH invoice the withholding agent verifies. If the agent is not registered as a service provider the credit is provisional, and if the agent does not deposit within the statutory period PRA-Iris raises a liability on the provider at line 7a of its next return; the return cannot be submitted until it is paid, and the amount comes back at 7b once the agent deposits (PRA-Iris FAQ 52, 53, 57; user manual 3.15).

### Balochistan pointer

Balochistan's standard rate is 15% (s.10(1)) and the Third Schedule reduced rates were revised from 1 July 2026 (BRA circular of 10 July 2026). A registered person acting as a withholding agent deducts the whole tax on a service received from a provider in another province under s.4(2), and s.14(2) lets the Authority require any person, registered or not, to withhold all or part of the tax. The withholding agents and shares are in the Balochistan Sales Tax Special Procedure (Withholding) Rules 2018; only its February 2026 amendment notification was read here, so the shares are on the "Not yet confirmed:" line.

## Boundary and exception table

| Situation | Treatment |
|---|---|
| Bank pays a Sindh provider that is liable to register but is not registered | Bank (a company) withholds the whole tax at the applicable rate, by the tax fraction on the gross bill, and keeps the CNIC or NTN copy (r.1(2)(e), r.3(4)) |
| Bank pays a registered, active Sindh provider whose invoice shows tax | Withholds one-fifth of the tax shown and pays the rest to the provider (r.3(3)) |
| Bank is itself the provider (Sindh) | Its customers do not withhold on banking services it invoices as an SRB-registered provider (r.3(1) proviso) |
| Company pays an unregistered KP provider on a commercial invoice | Value treated as exclusive of tax; 100% of the tax withheld from within the invoice value (paras 2(1)(v) proviso, 5(b), 12) |
| KP provider registered only in Sindh or Punjab, not with KPRA | Full withholding (para 5 clarification) |
| Punjab provider, unregistered, paid by a company | Company is a PRA withholding agent; the share and base are in the Punjab Withholding Rules 2015, not confirmed here. Do not apply the Sindh or KP rule to Punjab by analogy |
| Payer outside Sindh with no Sindh place of business | Not a Sindh withholding agent unless signed up on Form SSTW-01 (r.1(2) second proviso) |
| Withholding agent claims input tax on the withheld amount before deposit (Punjab) | Not allowed until deposited in the Punjab treasury (PRA-Iris FAQ 54) |

## Worked cases

### 1. Sindh: bank pays an unregistered consultant

A bank in Karachi pays PKR 1,000,000 to a consultant who provides a standard-rate Sindh service, is liable to register with SRB, but has no SNTN. The bill shows no tax and the contract is silent. The bank is a withholding agent (company, r.1(2)(e)). It withholds the whole tax by the tax fraction on the gross amount: 1,000,000 × 15/115 = PKR 130,434.78, pays the consultant PKR 869,565.22, deposits the tax by the r.3(7) date and keeps a copy of the consultant's CNIC. The consultant still has to register under s.24(1).

```oa-check
name: Sindh bank withholds whole tax from unregistered provider, tax fraction
inputs:
  gross_bill: 1000000
  rate: 0.15
steps:
  - tax_withheld: round(gross_bill * rate / (1 + rate), 2)
  - net_paid: gross_bill - tax_withheld
expected:
  tax_withheld: 130434.78
  net_paid: 869565.22
```

### 2. Khyber Pakhtunkhwa decision: register or stay unregistered

A Peshawar company buys a standard-rate service worth PKR 500,000. Two ways the provider can be paid:

- **Provider registered and active, tax invoice:** tax PKR 75,000 shown on top; the company withholds 50% (para 6), PKR 37,500, and pays the provider 500,000 + 75,000 − 37,500 = PKR 537,500. The provider declares the tax and takes credit for the PKR 37,500 once deposited.
- **Provider unregistered, commercial invoice of PKR 500,000:** the value is treated as exclusive of tax, so the tax is PKR 75,000, withheld in full from within the invoice value (paras 2(1)(v) proviso, 5(b), 12). The provider receives PKR 425,000.

The difference to the provider on the same invoice value is PKR 112,500, before the registered provider's own input tax credit and compliance cost.

```oa-check
name: KP registered versus unregistered provider, same PKR 500,000 value
inputs:
  value: 500000
  rate: 0.15
steps:
  - tax: value * rate
  - registered_withheld: tax * 0.5
  - registered_received: value + tax - registered_withheld
  - unregistered_received: value - tax
  - difference: registered_received - unregistered_received
expected:
  tax: 75000
  registered_withheld: 37500
  registered_received: 537500
  unregistered_received: 425000
  difference: 112500
```

## When to refuse or refer

- A Punjab question that turns on the share withheld, the Punjab rate for the service or a Punjab deadline: give the method and the PRA-Iris steps, say the Punjab figure is not confirmed here, and ask for the current Punjab Withholding Rules 2015 and the Punjab Act schedule.
- A service taxed by two provinces, or a provider registered in one province and paid in another: refer for place-of-supply analysis under each Act.
- A show cause notice, assessment or penalty for failure to withhold: refer to a Pakistani tax practitioner.
- Balochistan withholding shares: refer until the full 2018 Rules are read.

## Filing and payment

**Punjab, PRA-Iris (https://e.pra.punjab.gov.pk/public/txplogin.xhtml):**

1. Withholding agent not registered as a service provider: Withholding menu, then "Sales Tax Withholding Agent", select the tax period, load the STWH invoices where it is the buyer (Statement of Records), add Annex G data if any, attach the CPR in the Payment tab, verify with the PIN and submit. With no withholding, submit a nil statement.
2. Withholding agent registered as a provider: verify or reject each STWH invoice from the provider in real time; reject and de-link from Annex C any wrong one, so the provider can file.
3. Provider: enter the sale in Invoice Management, then enter the same invoice again with type STWH and the withheld amount; in the return use "Load STWH" and "Claim" in Annexure C. Sales to unregistered buyers use NTN 9999997 or the buyer's name and CNIC.
4. Return: Sales Tax menu, "35 (Monthly Sales Tax Return filed voluntarily)", select the period, load sales and purchases, add the CPR, verify with the PIN, save and submit. The submitted return appears in Completed Tasks. Extensions use "35 (Application for extension of filing of sales tax return)"; a revised return needs the Commissioner's approval through "35 (6)".
5. Banks collecting for PRA file the "Monthly Return for Collecting Agent" and add each collection under the Collecting Agent tab (user manual 7.1).

**Sindh:** an agent not registered with SRB signs up on Form SSTW-01, deposits on Form SSTW-04 to head of account B-02384 and files SSTW-03; an SRB-registered agent includes the withheld tax in its own SST-03 return (r.3(2), 3(8)).

**Khyber Pakhtunkhwa:** deposit to head of account B-02386 and file the monthly withholding statement by the 18th, nil if needed (paras 2(1)(ii), 11).

## Completion checklist

- Province and service settled; payer confirmed as a withholding agent in that province.
- Provider's registration and active status checked on the province's list.
- Share and base applied (whole tax for unregistered providers in Sindh and KP; Punjab share confirmed from the Rules before use).
- CNIC or NTN copy kept for an unregistered provider.
- Tax deposited, statement or return filed, certificate issued to the provider.

## Sources

| Source | URL | Read on |
|---|---|---|
| Read for withholding agents, unregistered-person definition, shares, deposit dates, returns, certificates and liability: Sindh Sales Tax Special Procedure (Withholding) Rules 2014, rr.1-5, as amended to the notification of 30 June 2026 | https://www.srb.gos.pk/srb/wp-content/uploads/2026/08/SSTOS_withholdingrules2014.pdf | 2026-11-15 |
| Read for the standard rate (s.8(1)), person liable (s.9) and registration (s.24(1)): Sindh Sales Tax on Services Act 2011, updated to the Sindh Finance Act 2026 | https://www.srb.gos.pk/srb/wp-content/uploads/2026/08/SSTOS_Act2011.pdf | 2026-11-15 |
| Read for withholding agents, full and 50% withholding, input tax, deposit dates, statements, unregistered providers and adjudication: KP Sales Tax on Services Special Procedure (Withholding) Regulation 2024, paras 1-14 | https://kpra.gov.pk/wp-content/uploads/2025/01/KP-withholding-regulations-2024.pdf | 2026-11-15 |
| Read for the standard rate (s.9(1)) and withholding power (s.14): KP Sales Tax on Services Act 2022, updated to the KP Finance Act 2026 | https://kpra.gov.pk/wp-content/uploads/2026/09/KPSTSA-2022-Updated-Finance-act-2026.pdf | 2026-11-15 |
| Read for the standard rate (s.10(1)), reverse charge on out-of-province services (s.4(2)) and withholding liability (s.14): Balochistan Sales Tax on Services Act 2015, amended by the Finance Act 2026 | https://ebra.com.pk/storage/uploads/downloads/1785387363.pdf | 2026-11-15 |
| Read for the revised Third Schedule rates from 1 July 2026 (scanned, read by OCR): BRA circular of 10 July 2026 | https://ebra.com.pk/storage/uploads/downloads/1784709123.pdf | 2026-11-15 |
| Read for the February 2026 amendments only (scanned, read by OCR): Balochistan Withholding Rules 2018 amendment notification | https://ebra.com.pk/storage/uploads/downloads/1772518454.pdf | 2026-11-15 |
| Read for withholding statements, STWH invoices, provisional credit, 7a liability, unregistered buyers, nil returns and collecting agents: PRA-Iris Sales Tax Return FAQs (2024), FAQs 20-57 | https://e.pra.punjab.gov.pk/templates/PRA_Iris_Sales_Tax_Return_FAQs.pdf | 2026-11-15 |
| Read for the 7a/7b/7c liability, revised return, extension, withholding statement and collecting agent steps: PRA-Iris Sales Tax Return User Manual v4 (2024), sections 3.15 and 4 to 7 | https://e.pra.punjab.gov.pk/templates/PRA_Iris_User_Manual_Version4.pdf | 2026-11-15 |
| Read for the automatic withholding-agent flag for companies: PRA Registration Module user manual v0.1 (January 2024), section 2.1 | https://e.pra.punjab.gov.pk/templates/PRA-Taxpayers-End-Registration-User-Manual-V0.1.pdf | 2026-11-15 |

Not yet confirmed: the Punjab standard rate and schedules for 2026-27 (Punjab Finance Act 2026); the Punjab Sales Tax on Services (Withholding) Rules 2015 as amended (withholding agents, the share withheld from registered and from unregistered providers, the base, deposit and statement due dates); the Punjab registration duty and threshold, return due dates and penalties for failing to withhold or register; whether a Punjab bank withholds the whole tax from an unregistered provider (the Sindh and KP rules say yes for their provinces; Punjab is not assumed); the Balochistan Withholding Rules 2018 base text (agents and shares); Sindh and KP penalty amounts for failing to withhold. The Punjab Act (http://punjablaws.gov.pk/laws/2506.html) and the PRA rules page (http://pra.punjab.gov.pk/SalesTax/Index) refused every connection on 15 November 2026, so neither was read; read them in a normal browser before adding any Punjab figure.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-15. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `pk-provincial-sales-tax-services` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/pk-provincial-sales-tax-services. If neither is available, confirm every figure against the official source pages cited above before relying on it.
