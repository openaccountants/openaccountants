---
name: global-ad-platforms
description: "Use the 2026 advertising purchase investigation method to investigate supplied transactions, reconcile supporting documents, distinguish fees and transfers and apply the actual country rules. Historical merchant strings are lookup hints, not current tax or integration certification."
version: 1.0
jurisdiction: GLOBAL
tax_year: 2026
last_updated: 2026-11-14
category: bookkeeping
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: bookkeeping
type: cross-country-method
checked_on: 2026-11-14
---

# Advertising purchase investigation v1.0

## Scope

Use the method for the actual entity, period, accounting basis and supported documents. Checked on 2026-11-14. No merchant brand, payment currency or bank narrative establishes a tax result by itself.

## Ask the client first

Obtain the advertiser's legal entity/country, reporting period, actual service and campaign dates, invoice supplier/establishment, VAT/GST registration and recovery status, business/private use, agency or platform contract, invoice/payment currency, invoices/credits and prior postings. Distinguish ad distribution, creative production, agency management, influencer services and affiliate commissions. Ask whether a legacy pre-April 2025 Indian consideration is being corrected rather than applying a new 2026 withholding automatically.

## The method, step by step

1. Match the card/bank charge to the actual ad account and invoice. A threshold-billed charge, pre-funded wallet/top-up, deposit, refund or consolidated campaign payment is not necessarily current-period advertising expense. Link the bill and payment so the feed does not duplicate the cost. Separate agency, creative, production and affiliate services, supported by their contracts.
2. Confirm the business campaign/purpose and private element; retain performance and invoice evidence. For UK sole traders/partners, advertising, websites and qualifying marketing costs are within HMRC's expense categories, while client entertainment and other exclusions have separate rules. Do not classify every sponsorship, gift or subscription as advertising merely from its merchant. [HMRC marketing](https://www.gov.uk/expenses-if-youre-self-employed/marketing-entertainment-subscriptions).
3. Apply the accounting policy to services received and prepaid/unused credits; do not expense every wallet top-up or assume payment date equals accrual recognition. Under UK traditional records, unpaid commitments and receipts also need records. [HMRC records](https://www.gov.uk/self-employed-records/what-records-to-keep).
4. Determine tax from the actual supplier, customer establishment and supply. For UK general-rule overseas B2B services, test Notice 741A sections 3-6 and relevant use/enjoyment rules, exemption and input entitlement. VAT-number presence is one piece of evidence, not an all-country exemption. Partly exempt buyers can have an unrecovered charge; unregistered buyers must consider section 5.7. Domestic invoicing and overseas establishment can change the result. [Notice 741A](https://www.gov.uk/guidance/vat-place-of-supply-of-services-notice-741a).
5. For EU or another country, load its current place-of-supply, imported-service, withholding and digital-services-tax method. Do not apply a supplier's own DST as an automatic advertiser withholding. The old EU Article 44/59a references need the actual current law and country implementation; the consolidated text could not be reopened during EUR-Lex's outage. Do not substitute a guessed zero rate or universal reverse charge.
6. For India, do not withhold the old6% advertising equalisation levy on consideration received/receivable on or after 1 April 2025. Finance Act 2025 section 146 expressly inserted the cutoff into Finance Act 2016 sections 163 and 165. Historical withholding, remittance, Form 1 and deduction-disallowance work remains a separate legacy-period reconciliation; establish receipt/receivable timing and the law for that period before correcting it. The old heading incorrectly called the advertising levy '2.0'. No current income-tax withholding, GST or other levy exemption is inferred from abolishing this levy. [Enacted section 146](https://egazette.gov.in/WriteReadData/2025/262125.pdf).
7. Translate recognition, monetary balances and settlement under the applicable reporting/tax policies, retaining source and settlement currencies. An applicable AASB 121/IFRS-equivalent policy distinguishes initial recognition from closing and settlement dates; it is not simply 'currency conversion at payment date'. [AASB 121 paragraphs 21-23,28-29](https://standards.aasb.gov.au/sites/default/files/2025-03/AASB121_08-15_COMPoct23_01-25.pdf).
8. Produce the proposed advertising/production/agency accounts, timing and private allocations, supported tax, bill-payment links and held items. Route SaaS, cloud, productivity and processor purchases to their companion methods. Country return lines, including US Schedule C advertising and UK self-employment boxes, depend on entity/year and form; no universal EU chart or fixed box is supplied here. Deliver read-only import/postings for human approval.

## Country rule checked for 2026

| Rule | Applicable condition | Official source |
|---|---|---|
| Indian section 165 advertising levy no longer applies from 1 April 2025 | Consideration for specified service received/receivable on or after the date; legacy periods need their own analysis; Finance Act 2025 s146 | https://egazette.gov.in/WriteReadData/2025/262125.pdf |

## When to refuse or refer

Hold an unsupported supplier, campaign purpose, tax status, service period or business-use split. Do not apply a pattern's remembered country/entity/VAT rule. Route a permanent/fixed establishment, royalty, influencer withholding, related party, digital-services-tax overlay or prior-period Indian levy correction to the owning country method. Apply the repository's excluded-jurisdiction policy before undertaking the work; a historical descriptor does not authorise prohibited coverage. Retain the document and explain the exact missing fact rather than asking the client to research the law.

## Worked case

Assume a supported 2026 Indian advertising service, consideration ofINR100,000 received/receivable after the statutory cutoff, and an unrelated INR 5,000 credit. The obsolete6% calculation would withhold INR 6,000; the advertising levy under section 165 is zero on these facts. The remaining supplier consideration is INR 95,000 before any separately established GST, income-tax withholding or other charge. Do not call the end of this levy a full exemption from Indian tax.

```oa-check
name: Advertising levy cutoff, other tax not assumed
inputs:
  consideration: 100000
  credit: 5000
  obsolete_rate: 0.06
  current_levy_rate: 0
steps:
  - obsolete_levy: consideration * obsolete_rate
  - current_advertising_levy: consideration * current_levy_rate
  - supplier_consideration: consideration - credit
expected:
  obsolete_levy: 6000
  current_advertising_levy: 0
  supplier_consideration: 95000
```

## Historical recognition hints

These are search candidates from the old library, not verified current merchant identities, fees or tax rules. Confirm the invoice, account and transaction before selecting an account.
- **Google Ads**; candidate statement text `GOOGLE*ADS`, `GOOGLE *ADWORDS`, `GOOGLE IRELAND LTD`, `GOOGLE ADS DUBLIN`. Investigate the actual purpose and direction.
- **Meta / Facebook / Instagram Ads**; candidate statement text `FACEBK *`, `META PLATFORMS`, `FACEBOOK IRELAND`, `META PLATFORMS IRELAND`. Investigate the actual purpose and direction.
- **LinkedIn Ads**; candidate statement text `LINKEDIN`, `LINKEDIN CORP`, `LINKEDIN IRELAND`. Investigate the actual purpose and direction.
- **TikTok Ads / Bytedance**; candidate statement text `TIKTOK INFO TECH`, `BYTEDANCE`, `TIKTOK ADS`, `TIKTOK PTE LTD`. Investigate the actual purpose and direction.
- **X / Twitter Ads**; candidate statement text `X CORP`, `TWITTER ADS`, `X HOLDINGS`. Investigate the actual purpose and direction.
- **Microsoft Ads / Bing Ads**; candidate statement text `MICROSOFT ADS`, `MICROSOFT*ADVERTISING`, `MICROSOFT IRELAND OPS`. Investigate the actual purpose and direction.
- **Amazon Ads**; candidate statement text `AMAZON ADS`, `AMZN ADVERTISING`, `AMAZON ADS EMEA`. Investigate the actual purpose and direction.
- **Reddit Ads**; candidate statement text `REDDIT INC`, `REDDIT BUSINESS`. Investigate the actual purpose and direction.
- **Pinterest Ads**; candidate statement text `PINTEREST INC`, `PINTEREST EUROPE`. Investigate the actual purpose and direction.
- **Snap Ads**; candidate statement text `SNAP INC`, `SNAP*ADS`. Investigate the actual purpose and direction.
- **Taboola**; candidate statement text `TABOOLA INC`, `TABOOLA EUROPE`. Investigate the actual purpose and direction.
- **Outbrain**; candidate statement text `OUTBRAIN INC`, `OUTBRAIN EUROPE`. Investigate the actual purpose and direction.
- **Quora Ads**; candidate statement text `QUORA INC`. Investigate the actual purpose and direction.
- **Yahoo Ads**; candidate statement text `YAHOO INC`, `VERIZON MEDIA`, `YAHOO INC NEW`. Investigate the actual purpose and direction.
- **Yahoo Japan Ads**; candidate statement text `YAHOO JAPAN`, `LY CORP`. Investigate the actual purpose and direction.
- **Baidu Ads**; candidate statement text `BAIDU INC`. Investigate the actual purpose and direction.
- **Naver Search Advertising**; candidate statement text `NAVER CORP`, `NAVER*`. Investigate the actual purpose and direction.
- Historical Yandex Direct descriptor is outside this library's permitted coverage. Do not use this method for an excluded jurisdiction.
- **Spotify Ads / Spotify Ad Studio**; candidate statement text `SPOTIFY ADS`, `SPOTIFY AB`. Investigate the actual purpose and direction.
- **Apple Search Ads**; candidate statement text `APPLE SEARCH ADS`, `APPLE INC ADS`. Investigate the actual purpose and direction.
- **The Trade Desk**; candidate statement text `THE TRADE DESK INC`, `TTD`. Investigate the actual purpose and direction.
- **DV360 (Display & Video 360)**; candidate statement text `GOOGLE DV360`, `GOOGLE *DV360`. Investigate the actual purpose and direction.
- **Amazon DSP**; candidate statement text `AMAZON DSP`, `AMAZON ADS DSP`. Investigate the actual purpose and direction.
- **Awin**; candidate statement text `AWIN LTD`, `AWIN AG`. Investigate the actual purpose and direction.
- **Impact / Impact Tech**; candidate statement text `IMPACT TECH`, `IMPACT.COM`. Investigate the actual purpose and direction.
- **ShareASale**; candidate statement text `SHAREASALE`, `AWIN US INC`. Investigate the actual purpose and direction.
- **Refersion**; candidate statement text `REFERSION INC`. Investigate the actual purpose and direction.
- **Partnerize**; candidate statement text `PARTNERIZE LTD`. Investigate the actual purpose and direction.

## Sources

| Official source | Read on | Read scope |
|---|---|---|
| https://www.gov.uk/self-employed-records/what-records-to-keep | 2026-11-14 | Read for sales/expense proof, accurate records, distinguishing business transactions and accrual records. |
| https://www.gov.uk/expenses-if-youre-self-employed/marketing-entertainment-subscriptions | 2026-11-14 | Read for allowable marketing, entertainment restrictions and subscriptions route. |
| https://www.gov.uk/guidance/vat-place-of-supply-of-services-notice-741a | 2026-11-14 | Read for sections 2-6 and 13, actual supply, belonging, reverse-charge conditions, input-tax limits and unregistered recipients. |
| https://egazette.gov.in/WriteReadData/2025/262125.pdf | 2026-11-14 | Read for Finance Act 2025 section 146 amending Finance Act 2016 sections 163 and 165; consideration received/receivable on or after 1 April 2025 is outside section 165. |
| https://standards.aasb.gov.au/sites/default/files/2025-03/AASB121_08-15_COMPoct23_01-25.pdf | 2026-11-14 | Read for paragraphs 20-23 and 27-30, initial recognition, monetary closing balances and settlement exchange differences; Australian IFRS-equivalent financial reporting, not universal tax translation. |

Not yet confirmed: EU consolidated advertising place/use-and-enjoyment law was not reopened; the old Schedule C/UK box numbers and legacy Indian remittance/Form 1/disallowance detail were not certified as current 2026 procedures.  Current platform billing identities, prices, plans, live descriptors and automatic tax arrangements are not certified. Old row claims below are historical comparison only, not usable tax or fee guidance. No vendor source was used.

- Historical claim, not usable guidance, **Google Ads**: Default category: Advertising; VAT/GST notes: EU B2B reverse charge (Google Ireland). UK: reverse charge. India: 6% equalisation levy withholding on payments by Indian payors
- Historical claim, not usable guidance, **Meta / Facebook / Instagram Ads**: Default category: Advertising; VAT/GST notes: Same as Google Ads , EU/UK B2B reverse charge from Meta Ireland; India 6% EL
- Historical claim, not usable guidance, **LinkedIn Ads**: Default category: Advertising; VAT/GST notes: Microsoft subsidiary; LinkedIn Ireland for EU
- Historical claim, not usable guidance, **TikTok Ads / Bytedance**: Default category: Advertising; VAT/GST notes: Singapore (TikTok Pte Ltd) or UK invoicing; EU B2B reverse charge
- Historical claim, not usable guidance, **X / Twitter Ads**: Default category: Advertising; VAT/GST notes: US (X Corp); EU B2B reverse charge
- Historical claim, not usable guidance, **Microsoft Ads / Bing Ads**: Default category: Advertising; VAT/GST notes: EU B2B reverse charge (Microsoft Ireland)
- Historical claim, not usable guidance, **Amazon Ads**: Default category: Advertising; VAT/GST notes: EU B2B reverse charge (Amazon Online Sales Ireland or AMS EMEA Sarl)
- Historical claim, not usable guidance, **Reddit Ads**: Default category: Advertising; VAT/GST notes: US supplier (Reddit Inc); EU B2B reverse charge
- Historical claim, not usable guidance, **Pinterest Ads**: Default category: Advertising; VAT/GST notes: US supplier; EU operations
- Historical claim, not usable guidance, **Snap Ads**: Default category: Advertising; VAT/GST notes: US supplier
- Historical claim, not usable guidance, **Taboola**: Default category: Advertising / content discovery; VAT/GST notes: US HQ; EU operations
- Historical claim, not usable guidance, **Outbrain**: Default category: Advertising / content discovery; VAT/GST notes: US HQ; EU operations
- Historical claim, not usable guidance, **Quora Ads**: Default category: Advertising; VAT/GST notes: US supplier
- Historical claim, not usable guidance, **Yahoo Ads**: Default category: Advertising; VAT/GST notes: US supplier (post-Verizon spin-off)
- Historical claim, not usable guidance, **Yahoo Japan Ads**: Default category: Advertising; VAT/GST notes: Japan supplier (now LY Corp after LINE merger)
- Historical claim, not usable guidance, **Baidu Ads**: Default category: Advertising; VAT/GST notes: China supplier
- Historical claim, not usable guidance, **Naver Search Advertising**: Default category: Advertising; VAT/GST notes: South Korea supplier
- Historical claim, not usable guidance, **Yandex Direct**: Default category: Advertising; VAT/GST notes: Russia / Nidex (post-2024 spin-off); sanctions check
- Historical claim, not usable guidance, **Spotify Ads / Spotify Ad Studio**: Default category: Advertising / audio; VAT/GST notes: Sweden HQ
- Historical claim, not usable guidance, **Apple Search Ads**: Default category: Advertising; VAT/GST notes: Apple Inc / Apple Distribution International
- Historical claim, not usable guidance, **The Trade Desk**: Default category: Advertising / DSP; VAT/GST notes: US supplier
- Historical claim, not usable guidance, **DV360 (Display & Video 360)**: Default category: Advertising / DSP; VAT/GST notes: Same as Google Ads
- Historical claim, not usable guidance, **Amazon DSP**: Default category: Advertising / DSP; VAT/GST notes: Same as Amazon Ads
- Historical claim, not usable guidance, **Awin**: Default category: Affiliate marketing; VAT/GST notes: UK / Germany supplier
- Historical claim, not usable guidance, **Impact / Impact Tech**: Default category: Affiliate / partnership; VAT/GST notes: US supplier
- Historical claim, not usable guidance, **ShareASale**: Default category: Affiliate marketing; VAT/GST notes: Awin subsidiary
- Historical claim, not usable guidance, **Refersion**: Default category: Affiliate marketing; VAT/GST notes: US supplier
- Historical claim, not usable guidance, **Partnerize**: Default category: Affiliate / partnership; VAT/GST notes: UK supplier
