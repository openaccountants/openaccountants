---
name: ca-911-988-surcharges
description: >
  California 911 and 988 surcharges under the Emergency Telephone Users
  Surcharge Act (R&TC 41001 and following), administered by CDTFA, with the
  2026 rates and the rates effective 1 January 2027. Covers the flat
  per-access-line surcharges that telecommunication service suppliers collect
  each month on wireline, postpaid wireless and VoIP lines, the same flat
  amounts that sellers of prepaid mobile telephony services collect on each
  retail transaction, the statutory caps, exempt lines and transactions, the
  place-of-primary-use rule, combined "911/988 Surcharge" billing, the monthly
  service supplier return and the quarterly prepaid seller return, electronic
  funds transfer, the 10% penalties, interest, the refusal-to-pay list and
  records. Not the prepaid MTS local charges, sales tax, or CPUC fees. Trigger
  on "California 911 surcharge", "988 surcharge", "911/988 surcharge",
  "Emergency Telephone Users Surcharge return", "prepaid MTS 911 surcharge",
  "CDTFA L-1051", "2027 911 surcharge rate".
version: 0.1
jurisdiction: US-CA
category: state-tax
tax_year: 2026
tax_year_notes: "2026-27"
last_updated: 2026-11-22
tier: 2
domain: tax
type: computation
---

# California 911 and 988 surcharges, 2026 and 2027 rates v0.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

> **Source-cited draft.** Built from the Emergency Telephone Users Surcharge Act, Revenue and Taxation Code (R&TC) sections 41001 to 41099, as published in the CDTFA Business Taxes Law Guide (Revision 2026); CDTFA special notices L-1051 (November 2026) and L-1012 (November 2025); and the CDTFA Tax Guide for Sellers of Prepaid Mobile Telephony Services (MTS) and Telecommunication Service Suppliers. All were read on 2026-11-22. No accountant has reviewed it.

**Answer first.** California imposes two separate flat surcharges, a **911 surcharge** and a **988 surcharge**:

- **Service suppliers:** collected each month on every access line (wireline, postpaid wireless or VoIP) that a service user subscribes to in California, for each month or part of a month (R&TC 41020(a)(1), 41050(a)).
- **Prepaid mobile telephony services (MTS) sellers:** the same flat amounts are collected on each retail transaction in California (R&TC 41020(a)(2), 41028(a), 41030(f)(2)).
- **The rates:**
  - **2026:** USD 0.41 (911) and USD 0.05 (988), together USD 0.46 per line per month ([CDTFA L-1012](https://cdtfa.ca.gov/formspubs/L1012.pdf)).
  - **2027, 1 January to 31 December:** USD 0.59 (911) and USD 0.11 (988), together USD 0.70 per line per month ([CDTFA L-1051](https://www.cdtfa.ca.gov/formspubs/L1051.pdf)).
- **Who sets them:** the Office of Emergency Services (Cal OES), each year by 1 October, for the next calendar year. The caps are USD 0.80 a month for 911 and USD 0.30 a month for 988 (R&TC 41030, 41031).
- **Returns:**
  - **Service suppliers:** an electronic return each month, due the last day of the second month after the month the surcharges were collected (R&TC 41051, 41052).
  - **Prepaid MTS sellers that are not service suppliers:** a quarterly return, due the last day of the month after the quarter (R&TC 41053.1).
- **Late payment or filing:** 10% plus interest (R&TC 41095).

**Tax year.** Tax year label 2026-27. The 2026 rates apply to access lines and prepaid transactions from 1 January to 31 December 2026, and the 2027 rates from 1 January to 31 December 2027 ([CDTFA L-1012](https://cdtfa.ca.gov/formspubs/L1012.pdf); [CDTFA L-1051](https://www.cdtfa.ca.gov/formspubs/L1051.pdf)). The rates follow the month of service or the retail transaction (R&TC 41031).

**Circular 230 disclosure.** This material is general information, not written advice on a specific transaction under 31 CFR 10.37. It is not intended to be used, and cannot be used, to avoid penalties.

## Scope and who this is for

In scope:

- **Service suppliers**, meaning persons supplying an access line to a service user in California ([R&TC 41007](https://cdtfa.ca.gov/lawguides/vol4/etusl/etusl-ch1-all.html)).
- **Sellers of prepaid MTS** in retail transactions ([R&TC 41007.5](https://cdtfa.ca.gov/lawguides/vol4/etusl/etusl-ch1-all.html)).
- **The service users and prepaid consumers** who owe the surcharges until they are paid to a registered supplier or seller ([R&TC 41024, 41028(c)](https://cdtfa.ca.gov/lawguides/vol4/etusl/etusl-ch2-all.html)).

The job: register, decide which lines or transactions carry the surcharges, apply the right year's flat amounts, bill or receipt them, file and pay, and handle refusals, exemptions, credits and penalties.

Out of scope, and where it goes:

| Topic | Skill |
| --- | --- |
| Prepaid MTS local charges (percentage of the price, city or county rates) and the 2% seller reimbursement on them | refer; CDTFA local charge rate tables |
| Sales and use tax on phones, SIM cards and other goods sold with prepaid service | `california-sales-tax` |
| CPUC public purpose program surcharges and CPUC registration | refer to the California Public Utilities Commission |
| Federal Universal Service Fund and federal excise taxes on telephone service | refer |
| City utility users taxes on telephone service | refer (local) |

## Ask the client first

- Is the business a service supplier (provides wireline, postpaid wireless or VoIP access lines), a seller of prepaid MTS, or both?
- How many access lines did it bill in California for each month (by category: wireline, wireless, VoIP, prepaid), and how many are exempt (Lifeline, public telephones, no charge billed, place of primary use outside California, constitutional exemptions)?
- For prepaid sales: how many retail transactions occurred in California in the quarter (in-store, known California address, or a California mobile number), and how many were Lifeline-exempt?
- Is it registered with CDTFA for an Emergency Telephone Users Surcharge account or a prepaid MTS account, and does CDTFA require it to pay by electronic funds transfer?
- Which months or quarters are being filed, and are any late or unpaid?
- Have any customers refused to pay surcharges totaling USD 3 or more?

## The method, step by step

### Rates, bands and thresholds

| Item | Figure | Conditions | Source |
| --- | --- | --- | --- |
| 911 surcharge, 2027 | USD 0.59 per access line per month, or per prepaid retail transaction | "January 1, 2027, through December 31, 2027" | [CDTFA L-1051](https://www.cdtfa.ca.gov/formspubs/L1051.pdf) |
| 988 surcharge, 2027 | USD 0.11 per access line per month, or per prepaid retail transaction | same | same |
| 911 surcharge, 2026 | USD 0.41 | "January 1, 2026, through December 31, 2026" | [CDTFA L-1012](https://cdtfa.ca.gov/formspubs/L1012.pdf) |
| 988 surcharge, 2026 | USD 0.05 | same | same |
| 911 surcharge cap | USD 0.80 per access line per month | "in no event shall the surcharge amount in any month be greater than eighty cents ($0.80) per access line per month" | [R&TC 41030(b)(1)](https://cdtfa.ca.gov/lawguides/vol4/etusl/etusl-ch2-all.html) |
| 988 surcharge cap | USD 0.30 per access line per month | "in no event shall the surcharge amount in any month be greater than thirty cents ($0.30) per access line per month" | [R&TC 41030(b)(3)](https://cdtfa.ca.gov/lawguides/vol4/etusl/etusl-ch2-all.html) |
| Prepaid MTS surcharge | equal to the per-line amounts, per retail transaction | "equal to the amount set forth in subdivision (b) for each retail transaction in this state" | [R&TC 41030(f)(2)](https://cdtfa.ca.gov/lawguides/vol4/etusl/etusl-ch2-all.html) |
| Rate setting | by 1 October, effective 1 January of the next calendar year | Cal OES determines both amounts and notifies CDTFA | [R&TC 41030(a), 41031](https://cdtfa.ca.gov/lawguides/vol4/etusl/etusl-ch2-all.html) |
| Service supplier return and payment | last day of the second month after the month collected | Monthly, filed electronically | [R&TC 41051, 41052(a)](https://cdtfa.ca.gov/lawguides/vol4/etusl/etusl-ch4-all.html) |
| Prepaid seller (not a service supplier) return and payment | last day of the month after each calendar quarter | Filed electronically | [R&TC 41053.1](https://cdtfa.ca.gov/lawguides/vol4/etusl/etusl-ch4-all.html) |
| Electronic funds transfer required | estimated liability averaging USD 20,000 or more per month | Service suppliers, as determined by CDTFA | [R&TC 41060(a)](https://cdtfa.ca.gov/lawguides/vol4/etusl/etusl-ch4-all.html) |
| Late payment penalty | 10% of the surcharge | Plus interest at the modified adjusted rate under R&TC 6591.5 | [R&TC 41095(a)](https://cdtfa.ca.gov/lawguides/vol4/etusl/etusl-ch4-all.html) |
| Late return penalty | 10% of the surcharge for the period | Penalties under 41095 capped at 10% of the surcharge for any one return | [R&TC 41095(b), (c)](https://cdtfa.ca.gov/lawguides/vol4/etusl/etusl-ch4-all.html) |
| Deficiency: negligence; fraud | 10%; 25% of the determination | Negligence or intentional disregard; fraud or intent to evade | [R&TC 41073, 41074](https://cdtfa.ca.gov/lawguides/vol4/etusl/etusl-ch4-all.html) |
| Refusal-to-pay list | USD 3 or more, cumulative, per service user | Names, addresses and reasons, with each return | [R&TC 41024, 41052(b)](https://cdtfa.ca.gov/lawguides/vol4/etusl/etusl-ch4-all.html) |
| Records | 4 years from when the surcharge is due | Service suppliers and sellers | [R&TC 41056](https://cdtfa.ca.gov/lawguides/vol4/etusl/etusl-ch4-all.html) |
| Credit for refunded overcollections | claimed on a return dated within 3 years of the overpayment | After refunding the customer | [R&TC 41023; 41028(b)(2)](https://cdtfa.ca.gov/lawguides/vol4/etusl/etusl-ch2-all.html) |

### Steps

1. **Register.**
   - Every service supplier or seller registers with CDTFA (R&TC 41040). Use CDTFA Online Services, "Register a New Business Activity", for an Emergency Telephone Users Surcharge account ([CDTFA, Telecommunication Service Suppliers](https://cdtfa.ca.gov/industry/sellers-of-prepaid-mobile-telephony-services-and-telecommunication-service-suppliers/telecommunication-service-suppliers.htm)).
   - Prepaid MTS sellers need a prepaid MTS account and a California seller's permit ([CDTFA, Sellers](https://cdtfa.ca.gov/industry/sellers-of-prepaid-mobile-telephony-services-and-telecommunication-service-suppliers/sellers.htm)).
2. **Count the access lines (service suppliers).**
   - An access line is a wireline communications service line, a wireless communications service line or a VoIP service line ([R&TC 41007.1](https://cdtfa.ca.gov/lawguides/vol4/etusl/etusl-ch1-all.html)).
   - A line is "in this state" when it is associated with a California billing address ([R&TC 41010](https://cdtfa.ca.gov/lawguides/vol4/etusl/etusl-ch1-all.html)).
   - Not more than one 911 surcharge and one 988 surcharge apply per wireless line number ([R&TC 41007.3(b)](https://cdtfa.ca.gov/lawguides/vol4/etusl/etusl-ch1-all.html)).
   - Each line subscribed in a month owes a full month's surcharges, even for part of a month ([R&TC 41050(a)](https://cdtfa.ca.gov/lawguides/vol4/etusl/etusl-ch4-all.html)).
3. **Take out exempt lines.**
   - **Lifeline, public telephones and no-charge lines:** lines supplying Lifeline service, lines connected to public telephones, and lines for which no charges are billed ([R&TC 41046](https://cdtfa.ca.gov/lawguides/vol4/etusl/etusl-ch3-all.html)).
   - **Out-of-state customers:** mobile or VoIP charges for a customer whose place of primary use is outside California ([R&TC 41020(b)](https://cdtfa.ca.gov/lawguides/vol4/etusl/etusl-ch2-all.html)).
   - **Constitutional and federal exemptions:** lines where the surcharge would breach the US Constitution, federal law or state law (R&TC 41027). CDTFA lists these under that rule ([CDTFA, Industry Topics](https://cdtfa.ca.gov/industry/sellers-of-prepaid-mobile-telephony-services-and-telecommunication-service-suppliers/industry-topics.htm)):
     - the United States, its unincorporated agencies and instrumentalities, and any state;
     - wholly owned federal corporations;
     - the American Red Cross;
     - banks in California;
     - enrolled American Indians subscribing from within a reservation;
     - federal credit unions;
     - nonprofit hospitals and nonprofit education organizations;
     - insurers paying the gross premiums tax.
4. **Apply the year's amounts.** Multiply the taxable lines for the month by the 911 amount and, separately, by the 988 amount for that calendar year (rates table).
5. **Bill them.**
   - Collect the surcharges with the regular bill (R&TC 41021(a), 41045), each stated separately ([R&TC 41022(a)](https://cdtfa.ca.gov/lawguides/vol4/etusl/etusl-ch2-all.html)).
   - A supplier may combine them as one line labeled "911/988 Surcharge", but must still remit them as separate amounts ([R&TC 41022(b)](https://cdtfa.ca.gov/lawguides/vol4/etusl/etusl-ch2-all.html)).
   - Where several suppliers' lines are used, the supplier that bills the customer collects ([R&TC 41021(a)](https://cdtfa.ca.gov/lawguides/vol4/etusl/etusl-ch2-all.html)).
6. **Prepaid MTS sellers.**
   - **Collect:** the flat 911 and 988 amounts are collected on each retail transaction in California, not per minute or per dollar. They are separately stated on the receipt or disclosed electronically, or combined as "911/988 Surcharge" ([R&TC 41028(a)](https://cdtfa.ca.gov/lawguides/vol4/etusl/etusl-ch2-all.html)).
   - **Where the transaction occurs:** a sale is in California if it is made in person at a California business location. Failing that, it is in California if the consumer's known address is in California (shipped to or picked up in California, in the seller's records, or given at the sale). Failing that too, it is in California if the mobile number is associated with California ([R&TC 41028(e)](https://cdtfa.ca.gov/lawguides/vol4/etusl/etusl-ch2-all.html)).
   - **Lifeline exemption:** a retail transaction is exempt only if the consumer is certified for the state or federal Lifeline program **and** the seller is authorized to provide Lifeline service ([R&TC 41028(h)](https://cdtfa.ca.gov/lawguides/vol4/etusl/etusl-ch2-all.html)).
   - **Mixed sales:** a transaction that mixes exempt items with a nonexempt prepaid MTS sale still carries both surcharges ([CDTFA, rates page](https://cdtfa.ca.gov/industry/sellers-of-prepaid-mobile-telephony-services-and-telecommunication-service-suppliers/911-surcharge-988-surcharge-and-local-charge-rates.htm)).
7. **File and pay** by the due date for the business type. See Filing and payment.

## Boundary and exception table

| Situation | Treatment | Source |
| --- | --- | --- |
| Line connected for 10 days in a month | Full month's 911 and 988 surcharges | [R&TC 41050(a)](https://cdtfa.ca.gov/lawguides/vol4/etusl/etusl-ch4-all.html); [CDTFA, Industry Topics](https://cdtfa.ca.gov/industry/sellers-of-prepaid-mobile-telephony-services-and-telecommunication-service-suppliers/industry-topics.htm) |
| Customer switches supplier mid-month | Each supplier's line carries the surcharges for that month | [R&TC 41050(b)](https://cdtfa.ca.gov/lawguides/vol4/etusl/etusl-ch4-all.html) |
| Business PBX with 40 extensions but 8 concurrent outbound call paths | CDTFA: lines subject to the surcharges do not exceed the number of concurrent outbound calls that can be placed to 911 or 988 | [CDTFA, Industry Topics](https://cdtfa.ca.gov/industry/sellers-of-prepaid-mobile-telephony-services-and-telecommunication-service-suppliers/industry-topics.htm) |
| Mobile customer whose place of primary use is in another state | Exempt (Mobile Telecommunications Sourcing Act) | [R&TC 41020(b)(1)](https://cdtfa.ca.gov/lawguides/vol4/etusl/etusl-ch2-all.html) |
| Prepaid calling card used by dialing an 800 number or PIN-less calling | CDTFA: not subject to the 911 or 988 surcharges | [CDTFA, Industry Topics](https://cdtfa.ca.gov/industry/sellers-of-prepaid-mobile-telephony-services-and-telecommunication-service-suppliers/industry-topics.htm) |
| Prepaid wireless top-up card, data plan usable for calls, or SIM card with airtime | Subject to the 911 and 988 surcharges per transaction | same |
| Medical alert devices and inmate call systems | CDTFA: usually not subject, because they generally do not reach 911 or 988 | same |
| Service supplier that also sells prepaid MTS | Reports the prepaid surcharges on its service supplier return | [CDTFA, Telecommunication Service Suppliers](https://cdtfa.ca.gov/industry/sellers-of-prepaid-mobile-telephony-services-and-telecommunication-service-suppliers/telecommunication-service-suppliers.htm) |
| Customer refuses to pay | Supplier need not sue; lists users with USD 3 or more uncollected (cumulative) with the return | [R&TC 41024, 41052(b)](https://cdtfa.ca.gov/lawguides/vol4/etusl/etusl-ch4-all.html) |
| Prepaid seller writes off a worthless account | Relieved of collection on that base; deduct on the return; report later recoveries | [R&TC 41028(d)](https://cdtfa.ca.gov/lawguides/vol4/etusl/etusl-ch2-all.html) |
| Prepaid consumer paid another state's surcharge on the purchase | Credit against, but not above, the California surcharges | [R&TC 41028(c)(2)](https://cdtfa.ca.gov/lawguides/vol4/etusl/etusl-ch2-all.html) |
| Disputed exemption claim | Supplier, seller or user may ask CDTFA for a ruling (due within 30 days); no collection from the claimant while pending | [R&TC 41049](https://cdtfa.ca.gov/lawguides/vol4/etusl/etusl-ch3-all.html) |
| The 2% seller reimbursement | Applies to local charges only, not to the 911 or 988 surcharges | [CDTFA, Sellers](https://cdtfa.ca.gov/industry/sellers-of-prepaid-mobile-telephony-services-and-telecommunication-service-suppliers/sellers.htm) |

## Worked cases

Both cases are made up for illustration. The rates come from CDTFA L-1051 and L-1012.

**Case 1: VoIP and wireline supplier, January 2027 return, and the change from 2026.**

- **Lines:** a service supplier bills 12,000 access lines with California billing addresses for January 2027. Of these:
  - 150 are Lifeline lines (exempt under 41046);
  - 50 are VoIP lines for customers whose place of primary use is outside California (exempt under 41020(b)(2)).
- **Taxable lines:** 12,000 - 150 - 50 = 11,800.
- **911 surcharge:** 11,800 x USD 0.59 = USD 6,962.00.
- **988 surcharge:** 11,800 x USD 0.11 = USD 1,298.00.
- **Total:** USD 8,260.00, reported as two separate amounts. The return and payment are due Wednesday 31 March 2027 (the last day of the second month after January).
- **At the 2026 rates:** the same lines would have owed 11,800 x USD 0.46 = USD 5,428.00, so January 2027 costs USD 2,832.00 more.
- **EFT:** at about USD 8,260 a month, the supplier is under the USD 20,000 average monthly threshold for mandatory electronic funds transfer, unless CDTFA determines otherwise.

```oa-check
name: Service supplier January 2027 911 and 988 surcharges, and change from 2026
inputs:
  lines_billed: 12000
  lifeline_lines: 150
  out_of_state_primary_use: 50
  rate_911_2027: 0.59
  rate_988_2027: 0.11
  rate_911_2026: 0.41
  rate_988_2026: 0.05
steps:
  - taxable_lines: lines_billed - lifeline_lines - out_of_state_primary_use
  - surcharge_911: taxable_lines * rate_911_2027
  - surcharge_988: taxable_lines * rate_988_2027
  - total_2027: surcharge_911 + surcharge_988
  - total_2026_rates: taxable_lines * (rate_911_2026 + rate_988_2026)
  - increase: total_2027 - total_2026_rates
expected:
  taxable_lines: 11800
  surcharge_911: 6962.00
  surcharge_988: 1298.00
  total_2027: 8260.00
  total_2026_rates: 5428.00
  increase: 2832.00
```

**Case 2: convenience-store prepaid MTS seller, first quarter of 2027, paid late.**

- **Transactions:** a retail store (not a service supplier) makes 3,000 in-store retail sales of prepaid wireless top-ups between 1 January and 31 March 2027.
- **Exempt:** 40 are sold to consumers certified for Lifeline, and the store is authorized to provide Lifeline service. Under R&TC 41028(h) both conditions must hold.
- **Taxable transactions:** 3,000 - 40 = 2,960. Each carries the flat USD 0.59 plus USD 0.11, whatever the top-up's price.
- **911 surcharge:** 2,960 x USD 0.59 = USD 1,746.40.
- **988 surcharge:** 2,960 x USD 0.11 = USD 325.60.
- **Total:** USD 2,072.00, due with the electronic return by Friday 30 April 2027 (the last day of the month after the quarter).
- **Late payment:** the store pays on 20 May 2027. The penalty is 10% x USD 2,072.00 = USD 207.20, plus interest at the modified adjusted rate (the rate was not stated on the pages read). Penalties for one return under R&TC 41095 are capped at 10%, so a late return adds nothing further.

```oa-check
name: Prepaid MTS seller Q1 2027 surcharges per transaction, with late-payment penalty
inputs:
  transactions: 3000
  lifeline_exempt: 40
  rate_911_2027: 0.59
  rate_988_2027: 0.11
  penalty_rate: 0.10
steps:
  - taxable_transactions: transactions - lifeline_exempt
  - surcharge_911: taxable_transactions * rate_911_2027
  - surcharge_988: taxable_transactions * rate_988_2027
  - total_due: surcharge_911 + surcharge_988
  - late_penalty: total_due * penalty_rate
  - total_with_penalty: total_due + late_penalty
expected:
  taxable_transactions: 2960
  surcharge_911: 1746.40
  surcharge_988: 325.60
  total_due: 2072.00
  late_penalty: 207.20
  total_with_penalty: 2279.20
```

## When to refuse or refer

- **Local charges:** prepaid MTS local charges and their rates and reimbursement. Refer.
- **Disputed exemptions:** whether a service is an "access line", a VoIP service line or prepaid MTS, or whether a constitutional exemption applies. Ask CDTFA for a ruling under R&TC 41049, or refer.
- **Old periods or disputes:** unfiled or audited periods, deficiency determinations, petitions for redetermination and relief requests. Refer to a California practitioner.
- **Rate questions:** how Cal OES computed the amounts. Refer to Cal OES.
- **Two stale exemptions:** CDTFA's industry page still lists toll lines used to gather and disseminate news for the public press, and wide-area telephone service lines used by common carriers. Those words were deleted from R&TC 41027 in 2022 (law guide History note, Stats. 2021, Ch. 432). Do not apply them without confirming with CDTFA.

## Filing and payment

- **Service suppliers:**
  - **When:** monthly, by the last day of the second month after the month collected. For example, January's return is due 31 March ([R&TC 41051, 41052](https://cdtfa.ca.gov/lawguides/vol4/etusl/etusl-ch4-all.html)).
  - **How:** through CDTFA Online Services ("File a Return"), with the Refusal to Pay Schedule when it applies.
  - **Every period:** a return is due even if nothing is owed. A due date on a weekend or state holiday moves to the next business day ([CDTFA, Telecommunication Service Suppliers](https://cdtfa.ca.gov/industry/sellers-of-prepaid-mobile-telephony-services-and-telecommunication-service-suppliers/telecommunication-service-suppliers.htm)).
  - **Billing aggregators:** may file for several suppliers through a CDTFA bulk template (same page).
- **Prepaid MTS sellers that are not service suppliers:** a quarterly electronic return, by the last day of the month after each calendar quarter ([R&TC 41053.1](https://cdtfa.ca.gov/lawguides/vol4/etusl/etusl-ch4-all.html)). CDTFA requires the prepaid MTS return to be filed separately from other returns ([CDTFA, Sellers](https://cdtfa.ca.gov/industry/sellers-of-prepaid-mobile-telephony-services-and-telecommunication-service-suppliers/sellers.htm)).
- **Electronic funds transfer:**
  - **Service suppliers:** required when the estimated liability averages USD 20,000 or more a month ([R&TC 41060(a)](https://cdtfa.ca.gov/lawguides/vol4/etusl/etusl-ch4-all.html)).
  - **Prepaid sellers:** a seller (not a service supplier) that pays sales tax by EFT also pays these surcharges by EFT ([R&TC 41028(g)](https://cdtfa.ca.gov/lawguides/vol4/etusl/etusl-ch2-all.html)).
- **Extensions:** CDTFA may extend a return or payment by up to one month for good cause, or up to three months after a disaster, if asked before the period ends ([R&TC 41054](https://cdtfa.ca.gov/lawguides/vol4/etusl/etusl-ch4-all.html)).
- **Penalties and interest:**
  - **Late:** 10% for late payment and 10% for a late return, capped at 10% per return, plus interest ([R&TC 41095](https://cdtfa.ca.gov/lawguides/vol4/etusl/etusl-ch4-all.html)).
  - **EFT payers:** 41060 applies instead of 41095: 10% for a late return, 10% for paying by other than EFT, and 10% for late payment, together capped at 10% of the surcharges for any one return ([R&TC 41060(d), (e), (f), (h)](https://cdtfa.ca.gov/lawguides/vol4/etusl/etusl-ch4-all.html)).
  - **Deficiencies:** 10% for negligence and 25% for fraud ([R&TC 41073, 41074](https://cdtfa.ca.gov/lawguides/vol4/etusl/etusl-ch4-all.html)).

## Completion checklist

- [ ] Registered with CDTFA (Emergency Telephone Users Surcharge account, or prepaid MTS account plus seller's permit).
- [ ] Access lines counted per month with a California billing address, one 911 and one 988 per wireless number, full amount for partial months.
- [ ] Exempt lines or transactions removed, each with its basis (41046, 41020(b), 41027, 41028(h)).
- [ ] Rates for the right calendar year applied: 2026 USD 0.41 and USD 0.05; 2027 USD 0.59 and USD 0.11.
- [ ] Surcharges stated separately, or combined as "911/988 Surcharge", and remitted as separate amounts.
- [ ] Return filed electronically by its due date (monthly supplier, quarterly prepaid seller), even with nothing owed.
- [ ] Refusal-to-pay list attached where a user owes USD 3 or more.
- [ ] Records kept 4 years.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| CDTFA Special Notice L-1051, 2027 Emergency Telephone Users Surcharge Rates (911 and 988 Surcharges), November 2026. Read in full: 911 USD 0.59 and 988 USD 0.11 per access line, 1 January to 31 December 2027; Cal OES sets the amounts by 1 October (citing R&TC 41030). | https://www.cdtfa.ca.gov/formspubs/L1051.pdf | 2026-11-22 |
| CDTFA Special Notice L-1012, 2026 Emergency Telephone Users Surcharge Rates, November 2025. Read in full: 911 USD 0.41 and 988 USD 0.05 for 2026 (988 down from USD 0.08). | https://cdtfa.ca.gov/formspubs/L1012.pdf | 2026-11-22 |
| CDTFA Business Taxes Law Guide (Revision 2026), Emergency Telephone Users Surcharge Act, Chapter 1 (entire chapter). Read for R&TC 41007 (service supplier), 41007.1 (access line), 41007.2, 41007.3 (wireless line, one surcharge per number), 41007.5 (prepaid definitions), 41008, 41009, 41010 and 41013. | https://cdtfa.ca.gov/lawguides/vol4/etusl/etusl-ch1-all.html | 2026-11-22 |
| Same, Chapter 2 (entire chapter). Read the texts operative from 29 September 2022 of R&TC 41020 (imposition, primary-use exclusion), 41021 to 41024, 41027, 41028 (prepaid), 41030 (amounts and caps, as amended by Stats. 2026, Ch. 252), 41031, 41032, 41040 and 41041, with their History notes. | https://cdtfa.ca.gov/lawguides/vol4/etusl/etusl-ch2-all.html | 2026-11-22 |
| Same, Chapter 3 (entire chapter). Read for R&TC 41045, 41046 (exempt lines) and 41049 (rulings). | https://cdtfa.ca.gov/lawguides/vol4/etusl/etusl-ch3-all.html | 2026-11-22 |
| Same, Chapter 4 (entire chapter). Read for R&TC 41050 to 41056 (due dates, returns, seller quarterly return, extensions, records), 41060 (EFT), 41071, 41073, 41074 and 41095 (interest and penalties). | https://cdtfa.ca.gov/lawguides/vol4/etusl/etusl-ch4-all.html | 2026-11-22 |
| CDTFA Tax Guide for Sellers of Prepaid MTS and Telecommunication Service Suppliers, 911 Surcharge, 988 Surcharge, and Local Charge Rates. Read for flat rates and caps, per-transaction collection, mixed transactions and known-address rules. | https://cdtfa.ca.gov/industry/sellers-of-prepaid-mobile-telephony-services-and-telecommunication-service-suppliers/911-surcharge-988-surcharge-and-local-charge-rates.htm | 2026-11-22 |
| Same guide, Industry Topics. Read for prepaid product examples, exempt access lines, partial months, combined billing, own lines, multiple suppliers and PBX. | https://cdtfa.ca.gov/industry/sellers-of-prepaid-mobile-telephony-services-and-telecommunication-service-suppliers/industry-topics.htm | 2026-11-22 |
| Same guide, Telecommunication Service Suppliers. Read for registration, monthly electronic return, due-date example, weekend rule, bulk filing, EFT and refunds. | https://cdtfa.ca.gov/industry/sellers-of-prepaid-mobile-telephony-services-and-telecommunication-service-suppliers/telecommunication-service-suppliers.htm | 2026-11-22 |
| Same guide, Sellers. Read for prepaid MTS account and seller's permit, separate electronic return, and the 2% reimbursement (local charges only). | https://cdtfa.ca.gov/industry/sellers-of-prepaid-mobile-telephony-services-and-telecommunication-service-suppliers/sellers.htm | 2026-11-22 |

Not yet confirmed: the current modified adjusted interest rate under R&TC 6591.5 (not read); whether the weekend and holiday due-date rule on CDTFA's service supplier page also applies to the quarterly prepaid seller return (the seller page read does not say); the two exemptions CDTFA's industry page still lists (news-gathering toll lines and common carriers' wide-area telephone service lines), which the 2022 amendment deleted from R&TC 41027; the statutory basis for CDTFA's PBX concurrent-call rule (stated on the CDTFA page, not found in the sections read); Cal OES's 2027 rate calculation summary (not read); the text of the Mobile Telecommunications Sourcing Act (Public Law 106-252), referenced but not read.

**Disclaimer.** This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon. The most up-to-date version of this skill is maintained at [openaccountants.com](https://www.openaccountants.com).
