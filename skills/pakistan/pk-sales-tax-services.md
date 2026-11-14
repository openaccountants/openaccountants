---
name: pk-sales-tax-services
description: Use for pakistan provincial and ict services sales tax. Read the stated period, eligibility conditions, evidence requirements, owner skills and unresolved boundaries before calculating or preparing a return.
jurisdiction: PK
tax_year: 2026
last_updated: 2026-11-14
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: vat-gst
version: 1.1
type: computation
---

# Pakistan provincial and ICT services sales tax v 1.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Scope

Service suppliers/recipients working across Sindh SRB, Punjab PRA, Khyber Pakhtunkhwa KPRA, Balochistan BRA and Islamabad Capital Territory FBR. This 2026 skill uses specifically identified 2025-2026 cycle provisions below; later 2026 amendments and actual period extensions must be checked before a later return. Federal goods sales tax is owned by `pk-sales-tax-federal`; income withholding by `pk-withholding-tax`. FBR administering ICT services does not turn those services into federal goods.

Quick answer: determine service category, locations, supplier/recipient liability and actual exemption/rate conditions separately for each authority. An office province or PSEB certificate alone does not settle jurisdiction or export relief.

## Ask the client first

Obtain supplier legal identity/NTN and each registration; service description/CPC/tariff code, contracts and taxable value; supplier establishments and performance/recipient/consumption locations; period/payment/invoice dates; B 2 B/B 2 C facts; invoice-by-invoice province/country split; recipient status/withholding role; actual input invoices/payment evidence and barred-input conditions; any election/notification; foreign delivery/bank-business-account/SBP export reporting and encashment evidence. Obtain existing notices/assessments and any actual inter-authority understanding. Turnover alone is not proof of a general registration threshold. PSEB matters for federal export income tax but is not universally a services-tax export condition.

## Rates, bands and thresholds

| Jurisdiction/category and material conditions | Read cycle rule | Official source |
|---|---|---|
| Sindh ordinary taxable service |15% standard, subject to Second Schedule rates/conditions and notified variations | [Act s.8](https://www.srb.gos.pk/srb/wp-content/uploads/2026/01/Sindh-Sales-Tax-Act-2011-25-26-2.pdf) |
| Sindh specified software/IT-system consultant services | Rule 42 I standard 15%;3% electronic Form Soption with timing/continuation conditions below; Second Scheduleitem 20 excludes CPC 83159 from its 3% row | [Second Schedule 20](https://www.srb.gos.pk/srb/wp-content/uploads/2026/01/Sindh-Sales-Tax-Act-2011-25-26-2.pdf); [r 42 I](https://www.srb.gos.pk/srb/wp-content/uploads/2025/11/Sindh-Sales-Tax-Rules-2011-25-26-1.pdf) |
| Sindh IT export, CPC 7331/8313/8314/8315/8316 | Exempt only if exported **and delivered outside Pakistan**, FX through banking into exporting registered person's business account **and SBP reporting**; PSEB is not a printed condition in this row | [First Schedule 14](https://www.srb.gos.pk/srb/wp-content/uploads/2026/01/Sindh-Sales-Tax-Act-2011-25-26-2.pdf) |
| Balochistan ordinary taxable service |15%; First Scheduleexempt, Second Schedulehigher, Third Schedulelower without input adjustment and notifications/thresholds can modify | [Act s.10](https://ebra.com.pk/public/storage/uploads/downloads/1755574443.pdf) |
| Balochistan hosting/IT infrastructure, telecom/internet and specified electronic security/communications installation |19.50% in specified higher-rate list; not a blanket IT exemption | [Second Schedule](https://ebra.com.pk/public/storage/uploads/downloads/1759148712.pdf) |
| KP after Finance Act 2025 changes |15% general negative-list regime except exempt/Second Scheduleconditions; use 2022 Act as amended, not 2013 Act alone | [FA 2025 s.10](https://kpra.gov.pk/wp-content/uploads/2025/07/kp-finance-act-2025.pdf) |
| KP digital/IT-based services, Second Schedule 12 |5%**without input adjustment**; includes software/web/app/cloud/digital marketing; no blanket export exemption established by this row | [FA 2025 Second Schedule 12](https://kpra.gov.pk/wp-content/uploads/2025/07/kp-finance-act-2025.pdf) |
| ICT IT/IT-enabled services generally |15% Table 1 item 11, subject to applicable Table 2 classification | [ICTSchedule](https://download1.fbr.gov.pk/Docs/2025711172945966ICTOUpdatedupto30.06.2025.pdf) |
| ICT software/IT-system-development consultants |5%**no input adjustment or refund**, Table 2 item 11 | [ICTSchedule Table 2](https://download1.fbr.gov.pk/Docs/2025711172945966ICTOUpdatedupto30.06.2025.pdf) |
| ICT exports of services |0% under s.3(1 A), after export character and actual operative rules established | [ICTs.3](https://download1.fbr.gov.pk/Docs/2025711172945966ICTOUpdatedupto30.06.2025.pdf) |

### Sindh IT option and export distinction

Rule 42 I requires registration and uses gross amount charged. Its 3% option requires electronic Form Swithin 21 days from financial-year commencement, or at least 14 days before first economic activity for new providers. Once exercised it continues for that year and subsequent years until withdrawal submitted at least 21 days before the financial year of revocation. Read the Act's actual category/exclusion with the rule; do not assume every service labelled “IT” qualifies or retrospectively elect after the deadline. Second Schedule Part IIgeneral condition(1)bars input deduction at the reduced rate; condition(2)requires the prescribed election for item 20. CPC 83159 collocation hosting instead carries 19.50% under Part I; broad rule 42 I wording does not erase that exclusion. [r 42 I](https://www.srb.gos.pk/srb/wp-content/uploads/2025/11/Sindh-Sales-Tax-Rules-2011-25-26-1.pdf); [Second Schedule 20](https://www.srb.gos.pk/srb/wp-content/uploads/2026/01/Sindh-Sales-Tax-Act-2011-25-26-2.pdf).

Exemption and zero-rating differ. Sindh First Schedule 14 is **exemption**, not federal 154 Afinal income tax or automatic refundable zero-rating. Keep delivery, qualifying code, registered business account, banking FX and SBP reporting conditions together. A non-PSEB exporter is not automatically taxable in Sindh merely for missing PSEB; missing export/delivery/banking conditions is a different failure. Do not extend this Sindh row to Punjab/KP/Balochistan or all creative/digital services. [First Schedule 14](https://www.srb.gos.pk/srb/wp-content/uploads/2026/01/Sindh-Sales-Tax-Act-2011-25-26-2.pdf).

## The method, step by step

1. Classify the service and actual period. Sindh s.3 covers economic activity from its office/business, including nonresident customers, and inbound nonresident-to-resident service with recipient liability under s.9(2). Exemptions/particular place rules must still be tested. Do not copy a foreign VAT reverse-charge rule as “100% withholding across all provinces”. [ss.3/9](https://www.srb.gos.pk/srb/wp-content/uploads/2026/01/Sindh-Sales-Tax-Act-2011-25-26-2.pdf).
2. Apply service-specific place rules to all touched jurisdictions. Sindh 2023 rules cover advertising/media/agents, insurance/agents, franchise/IP, transport and power transmission, with residual services returning to the Act/general rules. Rule 7 franchise/IP generally uses resident recipient location, with untaxed-province exception. Rule 8 corporate road/pipeline goods transport shares the value 50/50 origin/destination but retains same-province, untaxed endpoint, oil-tanker and noncompany booking-office branches. **No universal origin-only or B 2 Bdestination/B 2 Cprovider rule is supplied.** [rr 3-11](https://www.srb.gos.pk/srb/wp-content/uploads/2025/11/07-Sindh-Place-of-Provision-of-Services-Rules-2023.pdf).
3. Map Punjab/KP/Balochistan/ICT jurisdiction independently before charging or registering. A single tax payment is not proof that another authority has no claim. Obtain actual apportionment/credit/MOU provisions; do not pay twice as a default or promise an inter-provincial committee remedy without its operative route.
4. Establish registration, taxable value, correct rate/election/exemption, input entitlement/apportionment and invoice requirements in that authority. No general 4,000,000 or other common registration threshold is cleared; no ordinary bank-account province establishes place of supply. Prepare separate authority registers, returns and payments, with unresolved lines held for specialist review.
5. Reconcile service invoices, customer payments/withholding, input evidence, export receipts, ledgers and actual submitted returns/CPRs. Do not net provincial tax against income tax or assume federal/provincial input cross-credit. Unclear input entitlement stays provisional, not a fabricated zero liability.

## Deadlines, filing and records

| Authority and boundary | Read rule | Source |
|---|---|---|
| Sindh ordinary payment/return | Unless otherwise specified, payment 15 thfollowing month; electronic return within 3 days of payment due date; relevant service-specific variations still apply | [r 14](https://www.srb.gos.pk/srb/wp-content/uploads/2025/11/Sindh-Sales-Tax-Rules-2011-25-26-1.pdf) |
| Balochistan ordinary payment/return | Unless otherwise specified, payment 15 thfollowing month; return within 3 days after due date under r 15; particular service rules can differ | [rr 15/17](https://ebra.com.pk/public/storage/uploads/downloads/1715239876.pdf) |
| KP | s.39 permits prescribed/other periodic returns; Finance Act 2025 changes revised-return window to 120 days. No universal no-quarterly/annual-option claim | [2022 Act](https://kpra.gov.pk/wp-content/uploads/2024/07/KP-STS-ACT-2022-Updated-2024.pdf); [FA 2025 s.10](https://kpra.gov.pk/wp-content/uploads/2025/07/kp-finance-act-2025.pdf) |
| Punjab/ICT | Obtain actual current applicable rule/form/payment/return/extension before scheduling; do not infer a universal 15/18 calendar from another authority | Pending operational source boundary |
| Sindh records | For periods through 30 June 2025:10 years after tax period; from 1 July 2025:6 years from financial-year end; proceedings final decision if later | [s.27](https://www.srb.gos.pk/srb/wp-content/uploads/2026/01/Sindh-Sales-Tax-Act-2011-25-26-2.pdf) |
| Balochistan records |10 years after period for July 2023 onward; refund documents 10 years from refund-year end; final proceedings if later | [s.32](https://ebra.com.pk/public/storage/uploads/downloads/1755574443.pdf) |
| KP records, read base Act |5 years after period or final decision if later; check later amendments for current period | [s.36](https://kpra.gov.pk/wp-content/uploads/2024/07/KP-STS-ACT-2022-Updated-2024.pdf) |

Use actual SRB/PRA/KPRA/BRA/IRIS authority registration and return portals, rather than send every service to FBR. Sindh rule 42 I references its particular SST-G 3 form; old SST-03/PST/BST-03 labels are not proof of every current portal form. Generate the authority's payment instruction and retain actual bank acknowledgment/CPR and submitted return. Reconcile nil/activity periods under actual rules. The earlier blanket 5 year retention instruction is replaced by the authority-specific distinctions above.

## Penalties and interest

Sindh s.43 item 2 uses 100 per day of late-return default; the former 5,000/10,000 and 15 day bands are superseded. Sindh s.44 ordinary surcharge is interbank+3% yearly, fraud 2% monthly, calculated from day after due date to day before actual payment, tax due excluding penalty. [ss.43/44](https://www.srb.gos.pk/srb/wp-content/uploads/2026/01/Sindh-Sales-Tax-Act-2011-25-26-2.pdf).

Balochistan s.48 item 2 states 10,000 late-return penalty and 200 per default day if not filed within 15 days; preserve the exact assessment/default facts. Its s.49 ordinary surcharge is 12% yearly, fraud 2% monthly, with day-after-due to day-before-payment window and penalty excluded. The oldinterbank+3% statement was superseded. [ss.48/49](https://ebra.com.pk/public/storage/uploads/downloads/1755574443.pdf). Punjab/KP/ICT penalty summaries and actual default-date amendments remain pending; do not invent a common minimum.

## Worked cases

### Ali's original software-client facts retained

Ali is a freelance software developer with sole-proprietor/home-office PE in Karachi, not yet registered with any PRA. Client Ais Karachi fintech paying 800,000 monthly; Client Bis Lahore marketing agency paying 400,000; Client Cis US SaaS company paying USD 5,000 monthly through banking into his Karachi account; Ali holds PSEB registration. PSEB alone does not settle any sales-tax leg.

For Client A, assume confirmed software-development category, exclusive-of-tax 800,000 value, supply in the read cycle and all necessary registration/election conditions. Show the real election difference rather than assume an unverified rate:

```oa-check
name: Ali ClientA ordinary15percent branch
inputs:
  tax_exclusive_service_value: 800000
steps:
  - output_tax: tax_exclusive_service_value * 0.15
  - gross_invoice: tax_exclusive_service_value + output_tax
expected:
  output_tax: 120000
  gross_invoice: 920000
```

```oa-check
name: Ali ClientA evidenced3percent option branch
inputs:
  tax_exclusive_service_value: 800000
steps:
  - output_tax: tax_exclusive_service_value * 0.03
  - gross_invoice: tax_exclusive_service_value + output_tax
  - difference_from_standard: tax_exclusive_service_value * 0.15 - output_tax
expected:
  output_tax: 24000
  gross_invoice: 824000
  difference_from_standard: 96000
```

Client B 400,000 is a **jurisdiction hold** until the relevant Sindh/Punjab law, service-specific rule and recipient/withholding facts are reconciled. The former automatic 60,000 Sindh charge and register-only-SRB answer are not cleared. Document performance/client location and obtain actual dispute route before finalising.

Client CUSD 5,000 requires qualifying code, export **and overseas delivery**, FX bank-business-account and SBP reporting for Sindh First Schedule 14. If all met, report under the proper exempt category; otherwise determine the actual outcome rather than call missing PSEB decisive. Do not invent a PKR exchange rate or combine its turnover with income-tax 154 Awithout reconciliation. Ali's FBR income registration/return remains separate.

## Boundary and exception table

| Old topic retained | Supported treatment or specific pending boundary |
|---|---|
| Diplomatic/international organisations | Actual authority's exemption and recipient certificate required; no universal exemption |
| Education/health/cosmetic services | Specific schedule/category/recognition conditions, with KP taxed categories and actual exemptions checked; no blanket sector exclusion |
| Government-to-government | Actual notification required |
| Call centres/IT/digital marketplaces | Actual category/election/place/export law; oldhistorical 3/5/8 rates cannot travel between authorities |
| Imported digital/foreign supplier | Recipient-liability/registration/withholding under actual authority plus income-tax analysis; specialist finalisation |
| Refund/cross-credit/apportionment | Evidence and authority-specific rule before claim; no automatic federal credit or cash refund |
| Cross-province dispute/notice | Preserve all claims and actual contractual/place facts; refer for jurisdiction/relief route, no default origin remittance |

## When to refuse or refer

Keep all 9 referral groups: provincial refunds; competing cross-province claims/notices; withholding-agent obligations; imported-service reverse-charge/self-billing; AML/suspicious-transaction duties; audits/appeals; federal goods; residual FED; and capital-value/infrastructure-cess/professional-tax regimes. Missing category/location/period/election/export evidence prevents a final computation. Do not register automatically merely to seem cautious, apply an assumed standard rate or bank-account-location default, or label every foreign receipt exempt. Obtain the needed source and state the pending item.

## Sources

| Source and actual portions read | Official URL | Read on |
|---|---|---|
| Read for Sindh Act ss.3/8/9/27/43/44, First Schedule 14 and Second Schedule 20 with neighboring conditions | https://www.srb.gos.pk/srb/wp-content/uploads/2026/01/Sindh-Sales-Tax-Act-2011-25-26-2.pdf |2026-11-14|
| Read for Sindh Rules 14 and 42 Iincluding election/continuation/forms | https://www.srb.gos.pk/srb/wp-content/uploads/2025/11/Sindh-Sales-Tax-Rules-2011-25-26-1.pdf |2026-11-14|
| Read for Sindh Place Rules 3-11, particular service allocation/residual provisions | https://www.srb.gos.pk/srb/wp-content/uploads/2025/11/07-Sindh-Place-of-Provision-of-Services-Rules-2023.pdf |2026-11-14|
| Read for Balochistan Act ss.10/32/48/49 and higher-rate list; ordinary payment rule 17 withreturnrule 15 | https://ebra.com.pk/public/storage/uploads/downloads/1755574443.pdf; https://ebra.com.pk/public/storage/uploads/downloads/1759148712.pdf; https://ebra.com.pk/public/storage/uploads/downloads/1715239876.pdf |2026-11-14|
| Read for KPFinance Act 2025 s.10 amendments, general rate and Second Schedule 12; base Act ss.36/39 | https://kpra.gov.pk/wp-content/uploads/2025/07/kp-finance-act-2025.pdf; https://kpra.gov.pk/wp-content/uploads/2024/07/KP-STS-ACT-2022-Updated-2024.pdf |2026-11-14|
| Read for ICTOrdinances.3,Table 1 item 11 and Table 2 item 11 including no-input/refund condition | https://download1.fbr.gov.pk/Docs/2025711172945966ICTOUpdatedupto30.06.2025.pdf |2026-11-14|

Not yet confirmed: Punjabcurrent 2025-2026 schedule/rate/IT/export/penalty/deadline conditions; ordinaryweb and browser attempts to officialpunjablaws 2506 failed/timedout, and old 2012 PRAchapters are insufficient to clear later rates. KP 2026 Finance Act/Maynotification recovery remains incomplete. All actual later 2026 changes/extension calendars, particular input-credit/election restrictions, export definitions/procedures beyond the read rows, each current registration/portal/form, withholding/marketplace/refund/cross-credit/treaty/notice route require targeted confirmation. These boundaries preserve the old topics and keep unsupported figures outside usable instructions.
