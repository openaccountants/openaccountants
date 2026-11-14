---
name: global-marketplaces-banking-fees
description: "Use the 2026 marketplace and banking-fee reconciliation method to investigate supplied transactions, reconcile supporting documents, distinguish fees and transfers and apply the actual country rules. Historical merchant strings are lookup hints, not current tax or integration certification."
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

# Marketplace and banking-fee reconciliation v1.0

## Scope

Use the method for the actual entity, period, accounting basis and supported documents. Checked on 2026-11-14. No merchant brand, payment currency or bank narrative establishes a tax result by itself.

## Ask the client first

Identify seller/buyer role, legal entity/country, reporting period, platform contract and actual supplying establishment; product/service, inventory/dispatch and customer locations; registrations and customer business status; gross orders, refunds, taxes, fees, reserves, payouts, bank balances, fee invoices and information returns. Distinguish creator/ad-share/subscription income, professional services, used personal goods and purchases. Obtain source transaction IDs and all currencies. Determine the financial-reporting framework and cash/accrual tax basis before reconstruction.

## The method, step by step

1. Match the candidate descriptor to its actual account and commercial documents. A net deposit may combine several periods, tax collections, refunds, reserves and fees. Reconcile opening platform balance plus signed movements to closing balance and link the payout to the bank; do not treat payout alone as sales or add its transfer as a second sale.
2. Reconstruct orders/invoices and line components without double-counting repeated order totals or processor/marketplace feeds. Separate customer refunds, seller promotions, shipping consideration, stock reimbursements, fee refunds and platform charges. Fees and chargebacks need actual invoices/statements, not remembered public pricing. Determine principal/agent and actual supplier/customer contracts; a merchant-of-record label is not a universal 'net revenue/no VAT' rule. Under an applicable AASB 15 policy, paragraphs 47 and B34-B38 test third-party collections and control of each specified supply. [AASB 15](https://standards.aasb.gov.au/sites/default/files/2026-11/AASB 15_12-14_COMPdec22_07-26.pdf).
3. Test marketplace collection separately from the seller's registration, filing, income-tax and own sales obligations. Under the UK goods rules, distinguish goods outside GB, imports to Northern Ireland, stock already in the UK and VAT-registered business customers. The marketplace rule is not a blanket exemption for the seller. See the sourced values and exceptions below. EU IOSS/OSS and deemed-supplier rules require current law and product/customer/establishment facts; they are not interchangeable with the UK rule. US state collection/registration rules need that state's method, not a blanket100,000/200-transaction threshold or claim that sellers never register. [HMRC overseas goods](https://www.gov.uk/guidance/vat-and-overseas-goods-sold-to-customers-in-the-uk-using-online-marketplaces).
4. Reconcile information returns to underlying sales/receipts, including personal/non-income transfers, refunds, duplicated processor reports, fees and timing. A federal1099-K reporting threshold is not a taxable-income exemption. Apply the actual reporting entity/transaction type and state/backup-withholding exceptions below. EU DAC7 and UK platform reporting remain separate obligations: distinguish payment-only/advertisement functions from an operator arranging reportable activity and use current country rules. Do not infer DAC7 coverage merely because a platform transfers money.
5. For banking charges, preserve wire/outgoing/incoming SWIFT, foreign transaction, explicit conversion, ATM, monthly account, overdraft/NSF, returned cheque, inactivity, card replacement and verification fees as separate candidates. Determine actual business/private purpose and bank-versus-processor role. A narrative percentage is not a verified rate or a basis to estimate a fee. For UK sole traders/partners, eligible business financial charges are different from loan/overdraft principal repayments; private costs and fines are not automatically deductible. [HMRC financial costs](https://www.gov.uk/expenses-if-youre-self-employed/legal-financial).
6. Separate actual fees from exchange differences. Under an applicable AASB 121 policy, initial recognition and monetary closing/settlement rates have different jobs. An observed difference from a mid-market quote does not automatically establish a separately invoiced fee; preserve the contractual pricing and reporting policy. Do not certify a US GAAP mapping or all-country tax deduction from this conditional financial-reporting source. [AASB 121 paragraphs 21-23,27-30](https://standards.aasb.gov.au/sites/default/files/2025-03/AASB 121_08-15_COMPoct23_01-25.pdf).
7. Determine VAT/GST on each actual service. Financial services, advisory, software and payment-related services are not all the same supply. The old 'most bank fees exempt' reference to an unrelatedIRC provision is not a worldwide rule. Obtain the fee document and current local exemption/input-tax law; overseas general B2B services to a UK buyer require Notice 741A's conditions and recovery restrictions. [Notice 741A](https://www.gov.uk/guidance/vat-place-of-supply-of-services-notice-741a).
8. Deliver gross-to-net and per-currency reconciliations, proposed revenue/fees/tax/clearing/FX postings, return/report bridges, out-of-period items and exact unresolved facts. Review unusual descriptions and negative settlements. Check duplicate IDs and previous imports, then provide read-only postings/import for human approval.

## Country values and conditions

| Rule | 2026 value and conditions | Official source |
|---|---|---|
| US federal TPSO information reporting | Gross reportable payments exceed USD 20,000 AND transactions exceed200; no tax-free allowance; state lower thresholds, voluntary forms and backup withholding can produce a form below this | https://www.irs.gov/newsroom/form-1099-k-faqs-general-information |
| US payment-card information reporting | No TPSO de-minimis threshold for payment-card transactions; do not apply the above test to card payments | https://www.irs.gov/newsroom/form-1099-k-faqs-general-information |
| UK overseas consignment goods through marketplace | GBP 135 or less intrinsic value for the total consignment, not each item; GB overseas goods point-of-sale rule; Northern Ireland imports from outside UK/EU have separate import VAT mechanics; excise/noncommercial and stated Channel Island scheme exceptions | https://www.gov.uk/guidance/vat-and-overseas-goods-sold-to-customers-in-the-uk-using-online-marketplaces |
| UK VAT-number business-customer exception | For covered imported consignments, the marketplace does not charge VAT when the customer gives a valid UK VAT number; GB customer reverse charges, Northern Ireland follows import VAT rules; normal input recovery conditions apply | https://www.gov.uk/guidance/vat-and-overseas-goods-sold-to-customers-in-the-uk-using-online-marketplaces |

For goods above the consignment limit, normal import rules apply. For goods already in the UK sold by an overseas seller, marketplace collection and the seller's deemed supply/registration/import liabilities depend on the precise case; sales to a UK VAT-number business can remain the seller's responsibility. A seller making only zero-rated deemed supplies can consider registration or exemption from registration under HMRC's conditions. These UK rules do not certify the old EUR 150 EU threshold/OSS scope, whose consolidated law was not readable today.

## When to refuse or refer

Stop at missing platform statements, fee invoices, tax role, product/location facts or an unresolved payout difference. Do not invent gross revenue from a percentage fee, waive registration merely because a platform collected tax, or classify all FX spread as a bank expense. Route state sales tax, EU/UK platform-reporting scope, marketplace deemed supply, cross-border inventory, mixed-use borrowing, exempt financial services and treaty/withholding issues to the owning method.

## Worked case

Assume a supplied principal-seller report with USD 12,000 customer consideration, USD 1,000 tax collected for the authority, USD 500 customer refunds, USD 600 actual fees and USD 400 retained reserve. Supported net payout is USD 9,500; after the tax/refund amounts, sales consideration is USD 10,500 on these stipulated facts. The reserve remains a balance, not a fee. This example does not calculate a country's tax or prove a platform fee rate.

```oa-check
name: Marketplace gross to net and held reserve
inputs:
  gross: 12000
  collected_tax: 1000
  refunds: 500
  fees: 600
  reserve: 400
steps:
  - net_sales_consideration: gross - collected_tax - refunds
  - payout: gross - collected_tax - refunds - fees - reserve
  - clearing_control: payout + collected_tax + refunds + fees + reserve
expected:
  net_sales_consideration: 10500
  payout: 9500
  clearing_control: 12000
```

## Historical recognition hints

These are search candidates from the old library, not verified current merchant identities, fees or tax rules. Confirm the invoice, account and transaction before selecting an account.
- **Etsy**; candidate statement text `ETSY.COM`, `ETSY*PMT`, `ETSY IRELAND`. Investigate the actual purpose and direction.
- **eBay**; candidate statement text `EBAY INC`, `EBAY COMM PMT`, `EBAY EUROPE`. Investigate the actual purpose and direction.
- **Amazon Seller**; candidate statement text `AMAZON SELLER`, `AMAZON PAYMENTS`, `AMAZON SERVICES EUROPE`, `AMAZON MKTPLACE PMTS`. Investigate the actual purpose and direction.
- **AliExpress**; candidate statement text `ALIEXPRESS.COM`, `ALIBABA.COM`. Investigate the actual purpose and direction.
- **Mercari**; candidate statement text `MERCARI.COM`. Investigate the actual purpose and direction.
- **Depop**; candidate statement text `DEPOP LTD`. Investigate the actual purpose and direction.
- **Vinted**; candidate statement text `VINTED UAB`, `VINTED LTD`. Investigate the actual purpose and direction.
- **Fiverr**; candidate statement text `FIVERR INTERNATIONAL`, `FIVERR.COM`. Investigate the actual purpose and direction.
- **Upwork**; candidate statement text `UPWORK INC`, `UPWORK GLOBAL`. Investigate the actual purpose and direction.
- **Toptal**; candidate statement text `TOPTAL LLC`. Investigate the actual purpose and direction.
- **Catalant**; candidate statement text `CATALANT TECH`. Investigate the actual purpose and direction.
- **Patreon**; candidate statement text `PATREON INC`, `PATREON*`. Investigate the actual purpose and direction.
- **Substack**; candidate statement text `SUBSTACK INC`. Investigate the actual purpose and direction.
- **Gumroad**; candidate statement text `GUMROAD INC`. Investigate the actual purpose and direction.
- **Lemon Squeezy**; candidate statement text `LEMON SQUEEZY`, `LEMONSQUEEZY`. Investigate the actual purpose and direction.
- **Beehiiv**; candidate statement text `BEEHIIV INC`. Investigate the actual purpose and direction.
- **Whop**; candidate statement text `WHOP INC`. Investigate the actual purpose and direction.
- **OnlyFans**; candidate statement text `OF*ONLYFANS`, `FENIX INTL LTD`. Investigate the actual purpose and direction.
- **Twitch**; candidate statement text `TWITCH INTERACTIVE`. Investigate the actual purpose and direction.
- **YouTube Creator**; candidate statement text `GOOGLE *YOUTUBE`, `GOOGLE PAYMENTS`. Investigate the actual purpose and direction.
- **Wire fee**; candidate statement text `WIRE FEE`, `OUTGOING WIRE`, `INTERNATIONAL WIRE`. Investigate the actual purpose and direction.
- **Currency conversion fee**; candidate statement text `FX FEE`, `FOREIGN EXCH FEE`, `CURRENCY CONVERSION`, `0.5% INTL FEE`. Investigate the actual purpose and direction.
- **ATM fee**; candidate statement text `ATM FEE`, `OUT-OF-NETWORK ATM`, `INTERAC FEE`. Investigate the actual purpose and direction.
- **Monthly account fee**; candidate statement text `MONTHLY FEE`, `ACCT MAINT FEE`, `BANK ACCOUNT FEE`. Investigate the actual purpose and direction.
- **Overdraft fee**; candidate statement text `OVERDRAFT FEE`, `NSF FEE`, `INSUFFICIENT FUNDS`. Investigate the actual purpose and direction.
- **Returned cheque fee**; candidate statement text `RETURNED CHK FEE`, `RETURNED ITEM FEE`. Investigate the actual purpose and direction.
- **PayPal sending fee**; candidate statement text `PAYPAL *FEE`, `PYPL FEE`. Investigate the actual purpose and direction.
- **Stripe transaction fee**; candidate statement text `STRIPE FEE`, `STRIPE *PROCESSING`. Investigate the actual purpose and direction.
- **Card swap / replacement**; candidate statement text `CARD REPLACEMENT`, `NEW CARD FEE`. Investigate the actual purpose and direction.
- **Wire receive fee**; candidate statement text `WIRE RECEIVED FEE`, `INTL WIRE IN FEE`. Investigate the actual purpose and direction.
- **Inactivity fee**; candidate statement text `INACTIVITY FEE`, `DORMANT ACCOUNT FEE`. Investigate the actual purpose and direction.
- **Foreign transaction fee (card)**; candidate statement text `FOREIGN TRANSACTION FEE`, `3% FX`. Investigate the actual purpose and direction.
- **SWIFT fee**; candidate statement text `SWIFT FEE`, `SWIFT MSG FEE`. Investigate the actual purpose and direction.
- **Verified by Visa**; candidate statement text `VBV FEE`. Investigate the actual purpose and direction.

## Sources

| Official source | Read on | Read scope |
|---|---|---|
| https://www.gov.uk/self-employed-records/what-records-to-keep | 2026-11-14 | Read for sales/expense proof, accurate records, distinguishing business transactions and accrual records. |
| https://www.gov.uk/guidance/vat-and-overseas-goods-sold-to-customers-in-the-uk-using-online-marketplaces | 2026-11-14 | Read for overview, intrinsic consignment value, exceptions, B2B VAT-number treatment, over 135 imports, goods already in UK, seller registration and Northern Ireland distinctions. |
| https://www.irs.gov/newsroom/form-1099-k-faqs-general-information | 2026-11-14 | Read for general FAQs1-8 and current OBBBA notice for TPSO over 20000 AND over 200 transactions, payment-card distinction, backup withholding, state thresholds and taxable income. |
| https://www.gov.uk/expenses-if-youre-self-employed/legal-financial | 2026-11-14 | Read for eligible UK business financial charges, non-deductible loan principal and bad-debt distinction by accounting basis. |
| https://www.gov.uk/guidance/vat-place-of-supply-of-services-notice-741a | 2026-11-14 | Read for sections 2-6 and 13, actual supply, belonging, reverse-charge conditions, input-tax limits and unregistered recipients. |
| https://standards.aasb.gov.au/sites/default/files/2026-11/AASB 15_12-14_COMPdec22_07-26.pdf | 2026-11-14 | Read for paragraphs 47,105-108,B34-B38,B44-B47 for third-party collections, contracts, principal-agent control and unexercised rights; conditional reporting scope. |
| https://standards.aasb.gov.au/sites/default/files/2025-03/AASB 121_08-15_COMPoct23_01-25.pdf | 2026-11-14 | Read for paragraphs 20-23 and 27-30, initial recognition, monetary closing balances and settlement exchange differences; Australian IFRS-equivalent financial reporting, not universal tax translation. |

Not yet confirmed: EU consolidated VAT deemed-supplier/IOSS/OSS and DAC7 text could not be reopened. Current EU and UK platform-reporting operational dates/filing specifications, US state thresholds and universal bank-fee exemptions are not certified by this global file.  Current platform billing identities, prices, plans, live descriptors and automatic tax arrangements are not certified. Old row claims below are historical comparison only, not usable tax or fee guidance. No vendor source was used.

- Historical claim, not usable guidance, **Etsy**: Fee structure: Listing fee + 6.5% transaction + 3% + USD 0.25 payment processing; VAT/GST notes: Etsy Ireland for EU; collects EU OSS VAT on B2C
- Historical claim, not usable guidance, **eBay**: Fee structure: 12.9% + USD 0.30 (FVF); plus optional store subscription; VAT/GST notes: EU marketplace deemed-supplier rules; collects VAT on imported goods ≤ EUR 150 (IOSS)
- Historical claim, not usable guidance, **Amazon Seller**: Fee structure: Referral fee 6-45% by category; FBA fees; ad fees; VAT/GST notes: Amazon collects "marketplace tax" in US states; EU/UK deemed-supplier for imports ≤ EUR/£150
- Historical claim, not usable guidance, **AliExpress**: Fee structure: n/a (buyer-side); VAT/GST notes: Buyer-side patterns mostly
- Historical claim, not usable guidance, **Mercari**: Fee structure: 10% selling fee + payment processing; VAT/GST notes: US / Japan operations
- Historical claim, not usable guidance, **Depop**: Fee structure: 10% + payment fee; VAT/GST notes: Etsy subsidiary
- Historical claim, not usable guidance, **Vinted**: Fee structure: Buyer-side fee (no seller fee); shipping fee; VAT/GST notes: Lithuania HQ; EU marketplace
- Historical claim, not usable guidance, **Fiverr**: Fee structure: 20% Fiverr commission (5% of gig + 15% withhold); VAT/GST notes: Israel HQ
- Historical claim, not usable guidance, **Upwork**: Fee structure: 10% client fee + freelancer membership tiers; VAT/GST notes: US HQ
- Historical claim, not usable guidance, **Toptal**: Fee structure: Variable commission; VAT/GST notes: US HQ
- Historical claim, not usable guidance, **Catalant**: Fee structure: Commission; VAT/GST notes: US HQ
- Historical claim, not usable guidance, **Patreon**: Fee structure: 8-12% by tier + 2.9% + USD 0.30 payment processing; VAT/GST notes: US HQ
- Historical claim, not usable guidance, **Substack**: Fee structure: 10% + Stripe processing; VAT/GST notes: US HQ
- Historical claim, not usable guidance, **Gumroad**: Fee structure: 10% + Stripe processing; VAT/GST notes: US HQ
- Historical claim, not usable guidance, **Lemon Squeezy**: Fee structure: 5% + USD 0.50 + Stripe; collects sales tax for sellers; VAT/GST notes: Acquired by Stripe 2024
- Historical claim, not usable guidance, **Beehiiv**: Fee structure: Tiered subscription + ad share; VAT/GST notes: US HQ
- Historical claim, not usable guidance, **Whop**: Fee structure: Commission on digital products; VAT/GST notes: US HQ
- Historical claim, not usable guidance, **OnlyFans**: Fee structure: 20% platform fee; VAT/GST notes: UK HQ (Fenix International)
- Historical claim, not usable guidance, **Twitch**: Fee structure: Revenue share with Amazon; VAT/GST notes: Amazon subsidiary
- Historical claim, not usable guidance, **YouTube Creator**: Fee structure: Ad share + Super Chat etc.; VAT/GST notes: Google Ireland for EU
- Historical claim, not usable guidance, **Wire fee**: Default category: Bank charges / Other expenses
- Historical claim, not usable guidance, **Currency conversion fee**: Default category: Bank charges / Currency loss
- Historical claim, not usable guidance, **ATM fee**: Default category: Bank charges
- Historical claim, not usable guidance, **Monthly account fee**: Default category: Bank charges
- Historical claim, not usable guidance, **Overdraft fee**: Default category: Bank charges (note: deductibility may be restricted by purpose)
- Historical claim, not usable guidance, **Returned cheque fee**: Default category: Bank charges
- Historical claim, not usable guidance, **PayPal sending fee**: Default category: Bank charges / Payment processing
- Historical claim, not usable guidance, **Stripe transaction fee**: Default category: Bank charges / Payment processing
- Historical claim, not usable guidance, **Card swap / replacement**: Default category: Bank charges
- Historical claim, not usable guidance, **Wire receive fee**: Default category: Bank charges
- Historical claim, not usable guidance, **Inactivity fee**: Default category: Bank charges
- Historical claim, not usable guidance, **Foreign transaction fee (card)**: Default category: Bank charges / Currency loss
- Historical claim, not usable guidance, **SWIFT fee**: Default category: Bank charges
- Historical claim, not usable guidance, **Verified by Visa**: Default category: Bank charges
