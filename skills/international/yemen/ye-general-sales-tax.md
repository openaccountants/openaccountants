---
name: ye-general-sales-tax
description: >
  Yemen general sales tax research draft: the 2005 amended baseline, registration, returns, input recovery and imports, with separate Sana'a 2020 exemptions and two conditional examples. Current territorial application and complete amendment history remain unresolved.
jurisdiction: YE
category: international
tax_year: 2026
tier: 2
last_updated: 2026-10-22
version: 0.1
verified_by: pending
sources:
  - url: "https://www.yemen-nic.info/db/laws_ye/detail.php?ID=19343"
    title: "National Information Centre: Law 42/2005 amending sales tax"
    as_of: "2026-10-22"
  - url: "https://www.yemen-nic.info/db/laws_ye/detail.php?ID=11733&print=Y"
    title: "National Information Centre: original Law 19/2001, read with amendments"
    as_of: "2026-10-22"
  - url: "https://taxauthority-ye.tax/wp-content/uploads/2024/08/19-re.pdf"
    title: "Finance Decision 1/2006: executive regulations, article 1"
    as_of: "2026-10-22"
  - url: "https://tax.gov.ye/7-2020/"
    title: "Sana'a administration: Law 7/2020"
    as_of: "2026-10-22"
  - url: "https://tax.gov.ye/164-2020/"
    title: "Sana'a administration: Finance Decision 164/2020"
    as_of: "2026-10-22"
---

# Yemen: general sales tax

## Scope and status

This is a historical statutory baseline with a separately identified Sana'a amendment, not a certified current nationwide schedule. The 2026 metadata identifies the research year. Establish location, administering authority, transaction date and applicable amendment chain before using it. Arabic controls over this translation. No professional attestation or comprehensive consumption-tax coverage is claimed.

## Rate, registration and returns

Under amended article 4, the general rate is **5%**; Schedule 3 special rates, Schedule 2 zero-rating and article 40/Schedule 1 exemptions require classification first. The original 2001 rate must not be used without amendment reconciliation.

Article 6 directs the minister to set a registration threshold **not below YER50 million**, counting annual taxable goods/services across activities in Yemen. That statutory floor is not proof of today's operative threshold. Application is due within the first **15 days of the month after reaching/exceeding the prescribed threshold**. Taxable imports remain chargeable regardless of registration or import size, subject to exemptions.

Amended article 13 requires monthly returns within **21 days after month-end**, including nil periods. It permits amendment within 15 days after that deadline and moves a holiday filing deadline to the next working day. Article 14 changes ordinary input deduction to tax **paid**, and the pre-registration purchase window to **one year**; other eligibility conditions remain. [Law 42/2005, amended articles 4, 6, 13–14](https://www.yemen-nic.info/db/laws_ye/detail.php?ID=19343).

The 2006 executive regulations define the registration threshold as **YER50 million** for taxable goods and services. This establishes the historical regulatory amount, not proof that no subsequent administration-specific measure changed it. [Decision 1/2006, article 1, PDF page 3](https://taxauthority-ye.tax/wp-content/uploads/2024/08/19-re.pdf).

## Recovery, payment and imported services

Article 14(b) requires invoice details and, for imports, a customs declaration plus regulatory requirements. Pre-registration inputs must remain available at registration and relate to taxable post-registration use. Article 15 allocates mixed taxable/exempt production inputs and restricts deductions for petroleum products, car purchases and club memberships, subject to regulations. Do not assume every tax-bearing purchase is recoverable.

Articles 30–31 require payment at the return deadline of output tax exceeding deductible inputs; a return remains required where nothing is payable. Article 13(e) says an extension to file does not change the payment date. Under article 34(b), imported services are taxed when their price is paid; the beneficiary or intermediary must declare, withhold and remit. Classification, place of supply and current collection procedures still need verification. [Law 19/2001, articles 13–15, 30–31 and 34(b), read with amendments](https://www.yemen-nic.info/db/laws_ye/detail.php?ID=11733&print=Y).

## Sana'a 2020 exemptions: conditional and separate

Law 7/2020 was issued in Sana'a by the President of the Supreme Political Council on **3 May 2020**, effective on issuance. It adds article 40 exemptions for specified pharmaceutical/medical production inputs, electric/solar vehicles, renewable-energy equipment and specified related manufacturing/generation inputs. Eligibility includes tariff classifications, new-condition requirements for specified equipment, registrations and approved requirements lists. This is not a blanket exemption for anything described as green or medical. Its application outside that administration is not established here. [Law 7/2020, articles 1 and 4](https://tax.gov.ye/7-2020/).

Decision 164/2020 specifies documentary and approval requirements for selected production-input and capital-goods exemptions. Spare parts and maintenance supplies are excluded from those categories. Requirements include licensed industrial status, tax documents, regular accounts, approved lists and evidence of use. Before diversion or sale, notify the authority and pay the tax required under the decision. Secure the actual approved list and product classification before claiming relief. [Decision 164/2020, amended regulation 90(b), II–IV](https://tax.gov.ye/164-2020/).

## Example 1: taxable sale with eligible recovery

Assume the applicable administration and period use the 5% general rate, the tax-exclusive statutory base is YER2,000,000, and YER30,000 paid input tax is independently established as deductible. Output tax is YER100,000; net payable is YER70,000. This example does not establish product classification or recovery eligibility.

```oa-check
name: Yemen general sales tax with eligible inputs
inputs:
  taxable_base: 2000000
  rate: 0.05
  eligible_input_tax: 30000
steps:
  - output_tax: taxable_base * rate
  - net_payable: output_tax - eligible_input_tax
expected:
  output_tax: 100000
  net_payable: 70000
```

## Example 2: no recoverable purchase tax

Assume the same taxable sale but the purchase tax is independently established to be non-deductible. The payable amount remains YER100,000. A purchase invoice alone does not establish eligibility.

```oa-check
name: Yemen sales tax with excluded input deduction
inputs:
  taxable_base: 2000000
  rate: 0.05
  eligible_input_tax: 0
steps:
  - output_tax: taxable_base * rate
  - net_payable: output_tax - eligible_input_tax
expected:
  output_tax: 100000
  net_payable: 100000
```

## Intake and outstanding coverage

Collect registration evidence, annual turnover by activity, invoices, customs declarations, payment dates, product classifications, approvals and the applicable tax-office instructions. Remaining work includes later registration-threshold changes, complete special-rate and exemption schedules, place/time/value rules, mixed supplies, refunds, export evidence, goods-import deferral, penalties, appeals, records retention, forms and later amendments for each administration. These gaps prevent a complete or current nationwide coverage claim.

## Sources

- [Law 42/2005](https://www.yemen-nic.info/db/laws_ye/detail.php?ID=19343).
- [Original Law 19/2001](https://www.yemen-nic.info/db/laws_ye/detail.php?ID=11733&print=Y), only as qualified by amendments.
- [Executive regulations, Decision 1/2006](https://taxauthority-ye.tax/wp-content/uploads/2024/08/19-re.pdf).
- [Sana'a Law 7/2020](https://tax.gov.ye/7-2020/).
- [Sana'a Finance Decision 164/2020](https://tax.gov.ye/164-2020/).

## Disclaimer

Source-cited research draft. Verify current law, territorial application and transaction facts before filing or payment.
