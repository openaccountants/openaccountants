---
name: ye-property-income-and-transfers
description: >
  Yemen property-tax research draft covering rental income, individual/company distinctions, ownership-transfer tax, selected exemptions and filing/payment requirements in Law 17/2010. Flags the separate Sana'a-issued 2020 small-landlord exemption. Two conditional examples distinguish gross transfer value from gain and individual rental tax from corporate profit tax. Current administration-specific amendments and operational procedures remain unresolved.
jurisdiction: YE
category: international
tax_year: 2026
tier: 2
last_updated: 2026-10-22
version: 0.1
verified_by: pending
sources:
  - url: "https://agoyemen.net/lib_details.php?id=198"
    title: "Public Prosecution, Law 17/2010, articles 51–61, 69–70, 81–82, 103–105 and 112"
    as_of: "2026-10-22"
  - url: "https://tax.gov.ye/8-2021/"
    title: "Tax and Customs Authority, Law 8/2020 adding article 160(c), small-property exemption"
    as_of: "2026-10-22"
---

# Yemen: rental income and property transfers

## Scope and governing administration

This draft translates selected provisions of the official reproduction of Law 17/2010. The full subsequent amendment chain and application across different administrations have not been reconciled. Establish the property's location, administering office, ownership category, transaction date and governing rules before using a computation. The Sana'a-issued 2020 amendment is identified separately below; no uniform nationwide exemption is asserted. [Law 17/2010](https://agoyemen.net/lib_details.php?id=198); [Law 8/2020](https://tax.gov.ye/8-2021/).

## Rental income: identify the taxpayer

Articles 51–52 cover annual rental income from buildings, prefabricated/mobile buildings and vacant land let for different purposes. Liability lies with the owner or the holder of the usufruct right in property leased from the State, with the legal representative responsible on behalf of the represented taxpayer. Article 53 uses valid lease contracts to establish income and permits assessment under implementing rules where rent is unknown or the contract is shown to be incorrect. [Articles 51–53](https://agoyemen.net/lib_details.php?id=198).

For **natural persons**, article 53(b) uses total annual rental income as the base and article 69 charges **one month's rent per year**. This is not a general 20% charge on rental profit after expenses. Variable rent, vacancies and part-year letting require the detailed rules before calculation. [Articles 53(b), 69](https://agoyemen.net/lib_details.php?id=198).

For **legal persons**, article 53(c) places rent within commercial/industrial profits and permits necessary related expenses under the law. Do not apply the natural-person one-month formula to a company. The company's rate, adjustments and other relief must be established separately. [Article 53(c)](https://agoyemen.net/lib_details.php?id=198).

## Rental exemptions and later small-landlord measure

Article 54(a) exempts property used by its owner. Other specified exemptions include conditional government, charitable, endowment and diplomatic cases; these are not a blanket exemption for every property owned by a public or non-profit entity. Article 55 removes the rental tax where property is destroyed, burnt or otherwise unusable and produces no income. A mere drop in rent is not that condition. [Articles 54–55](https://agoyemen.net/lib_details.php?id=198).

Law 8/2020, issued in Sana'a on 3 May 2020, adds an exemption for specified small rental taxpayers whose monthly rent does not exceed **YER50,000**, with reporting obligations and rules when the ceiling is exceeded. Its geographic application, eligibility, aggregation across properties and later measures must be established before claiming it. The example below uses rent above that ceiling and assumes no exemption; this does not certify the applicable law in any location. [Added article 160(c), especially third and fifth–sixth provisions](https://tax.gov.ye/8-2021/).

Article 81 requires notification and evidence within **30 days** of cessation or vacancy to obtain its relief, even where the event is outside the taxpayer's control. Delayed notice can extend liability for the delay, capped at one year. Do not stop reporting solely because a tenant leaves. [Article 81](https://agoyemen.net/lib_details.php?id=198).

## Transfer tax is based on property value

Articles 56 and 58 cover transfers of ownership of land and built/buildable property, in whole or part, including transfers other than ordinary sales and finance-lease arrangements. Article 70 sets **1% of total property value or price**. It is not a tax calculated only on the seller's gain. Article 58(b) allows valuation by the authority where the price is unspecified. Article 56(b) separately provides for a single tax for the specified murabaha, lease-to-own and participation arrangements; their implementation needs case-specific checking. [Articles 56, 58 and 70](https://agoyemen.net/lib_details.php?id=198).

Article 57 places the burden on the seller/transferor and makes the buyer/transferee or person benefiting from documentation/transfer jointly responsible for payment. It prevents documentation or registration of the transfer until this tax is fully paid. Multiple disposals of the same property can create multiple tax charges. A contractual cost allocation does not by itself remove statutory joint responsibility. [Article 57](https://agoyemen.net/lib_details.php?id=198).

Article 61 exempts specified transfers, including inheritance or testamentary transfer. That exemption concerns this transfer tax, not every inheritance-related duty or later rental income. Other conditional exemptions include particular charitable gifts, public endowments, agricultural-land transactions and fully State-owned transfers. Verify the relevant category and implementing conditions individually. [Article 61](https://agoyemen.net/lib_details.php?id=198).

## Returns, payment and completion evidence

Article 103 requires rental taxpayers' annual returns, with a lease copy, property description and actual monthly rent, by **30 April** for the preceding year, with payment at the same time. Apply any valid later exemption/reporting regime separately. [Article 103](https://agoyemen.net/lib_details.php?id=198).

Articles 104–105 place the property-transfer return on the seller/transferor within **four months of disposal or sale**, with payment on the day the return is submitted and no later than the statutory deadline, under article 112(a). This does not override article 57(b)'s payment-before-registration rule: completing registration earlier requires tax payment first. Article 59 also requires payment evidence for the listed registration, building-permit and document-certification steps. Operational forms, receipts, valuation disputes, holidays and current extensions remain unverified. [Articles 57, 59 and 104–105](https://agoyemen.net/lib_details.php?id=198).

Article 82 also requires notification of the sale/disposal within **30 days**, applies article 81's cessation rules, and makes the specified parties jointly responsible for taxes accrued through the transaction date. This earlier notification is separate from the transfer-tax return. A sale that also closes a business requires checking article 111's separate cessation return; the four-month transfer deadline is not a universal closing deadline. [Articles 81–82 and 111](https://agoyemen.net/lib_details.php?id=198).

## Example 1: individual with constant full-year rent

Assume a natural person rents a property for all twelve months at YER100,000 per month, the baseline article 69 rule applies, and no exemption applies. Annual rent is YER1,200,000 and rental tax is one month's rent: YER100,000. No property expenses are deducted in this illustration. Do not reuse it for a company or a part-year tenancy.

```oa-check
name: Yemen individual constant full-year rental tax
inputs:
  monthly_rent: 100000
  months_let: 12
  tax_months: 1
steps:
  - annual_rent: monthly_rent * months_let
  - rental_tax: monthly_rent * tax_months
expected:
  annual_rent: 1200000
  rental_tax: 100000
```

## Example 2: transfer value, not gain

Assume a non-exempt transfer with an independently accepted value of YER30 million and historic cost of YER20 million. At 1% of total value, transfer tax is YER300,000. Applying 1% only to the YER10 million gain would incorrectly produce YER100,000. This does not determine a separate business-income charge, registration fee or exemption.

```oa-check
name: Yemen transfer tax uses total accepted value
inputs:
  accepted_value: 30000000
  historic_cost: 20000000
  transfer_rate: 0.01
steps:
  - transfer_tax: accepted_value * transfer_rate
  - gain_for_comparison: accepted_value - historic_cost
  - incorrect_gain_only_tax: gain_for_comparison * transfer_rate
expected:
  transfer_tax: 300000
  gain_for_comparison: 10000000
  incorrect_gain_only_tax: 100000
```

## Intake and remaining work

Obtain title and ownership category, property location/use, leases and rent history, transaction documents, valuation, consideration, exemptions, transfers in the chain and payment/registration evidence. Remaining work includes administration-specific law, small-landlord eligibility, mixed/part-year use, valuation procedures, capital/business-income interaction, other duties/fees, inheritance rules beyond the transfer exemption and current filing operations. This Guide does not establish comprehensive capital/property coverage or professional attestation.

## Sources

- [Public Prosecution, Income Tax Law 17/2010](https://agoyemen.net/lib_details.php?id=198), articles cited above, retrieved 22 October 2026; Arabic controls over this research translation.
- [Tax and Customs Authority, Law 8/2020](https://tax.gov.ye/8-2021/), retrieved 22 October 2026; administration-specific application remains unresolved.

## Disclaimer

Source-cited research draft. Verify the applicable administration, law, facts and procedures before filing or completing a transfer.
