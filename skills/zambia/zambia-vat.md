---
name: zambia-vat
description: "Use this skill to prepare, review or classify transactions for a Zambia VAT return for 2026: 16% rate, K800,000 registration threshold, Smart Invoice input tax rule, reverse VAT, blocked input tax, monthly return by the 18th. Trigger on Zambia VAT, ZRA VAT return, reverse VAT Zambia, input tax claim, withholding VAT agent. Covers registered suppliers and businesses deciding whether to register. Not for mining refund disputes or MFEZ certificates, which are referred."
jurisdiction: ZM
category: international
tax_year: 2026
last_updated: 2026-11-01
version: 2.1
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Zambia VAT Return Skill v2.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

Charge year 2026. Authority: Zambia Revenue Authority (ZRA). Law: Value Added Tax Act, Cap. 331. Currency: Kwacha (ZMW, K).

## Who this applies to

Anyone making taxable supplies of goods or services in Zambia in the course of business. Suppliers dealing only in exempt supplies cannot register. Mining and MFEZ cases are escalated (see Ask the client first).

## Rates, bands and thresholds

| Item | Amount | Tax year | Official URL |
|---|---|---|---|
| Standard rate | 16% | 2026 | https://www.zra.org.zm/wp-content/uploads/2026/06/Introduction-to-VAT.pdf |
| Zero rate | 0%: exports with evidence, goods imported by diplomats with reciprocal privileges, supplies to donors for official purposes, cement, roofing sheets, bricks and blocks to approved public benefit organisations | 2026 | same |
| Mandatory registration | Annual taxable supplies above K800,000 (leaflet also says K200,000 per quarter) | 2026 | same |
| Voluntary registration | Turnover above K400,000 but below the threshold; renew 30 days before the new charge year | 2026 | same |
| Input tax time limit | 90 days from invoice date to submitting the return | 2026 | https://www.zra.org.zm/wp-content/uploads/2026/06/Claiming-input-tax.pdf |
| Diesel input tax cap | Mining, processing, exploration 70%; other suppliers 90%; diesel resellers 100% | 2026 | same |
| Electricity input tax cap | Mining and mineral processing 80% | 2026 | same |
| Business gifts or samples | Taxable above K100 per year | 2026 | https://www.zra.org.zm/wp-content/uploads/2026/06/Introduction-to-VAT.pdf |

Any supply not listed in the Exemption or Zero-Rating Orders is standard rated. Example exempt supplies per ZRA: health and medical services, education, funeral services.

## The base

**Output tax.** Tax point is the earliest of payment received, invoice issued, goods or services delivered, goods supplied.

**Input tax.** Output less input. From 1 January 2025 only Smart Invoice invoices are claimable; a non-smart invoice gives no claim. Imports need form CE 20, receipt and Release Order. Late registrants assessed by ZRA cannot claim input tax incurred before registration.

**Blocked input tax (ZRA leaflet).** Telephone and internet (with carrier and hotel resale exceptions); motor vehicles with side windows or a rear seat (dealers, lessors and hire businesses excepted; repairs claimable if business use, apportioned if mixed); business entertainment; food, drink, transport, hospitality or housing for directors, staff or customers; staff dwelling houses unless built for sale; goods lost in the business must have input tax refunded. Partially exempt businesses claim only the taxable share by an approved method.

**Reverse VAT (VAT Act s. 8(5) and (6)).** Applies to imported services performed, used or enjoyed in Zambia from a non-resident with no appointed tax agent. The recipient raises a tax invoice, charges 16% and declares output VAT. ZRA says this "cannot be claimed as input tax", so it is a cost, not net zero. Outside scope: exempt services, and persons not eligible or below the threshold.

**Withholding VAT.** The 2026 leaflet lists withholding VAT agents due by the 16th and marks it "currently suspended". While suspended, do not assume a customer withholds.

**Bank statement patterns.**

| Pattern | Treatment | Notes |
|---|---|---|
| ZANACO | EXCLUDE | Exempt financial |
| STANBIC ZM, STANBIC ZAMBIA | EXCLUDE | Same |
| STANDARD CHARTERED ZM | EXCLUDE | Same |
| FNB ZAMBIA, ABSA ZM | EXCLUDE | Same |
| ZRA, ZAMBIA REVENUE | EXCLUDE | Tax payment |
| CUSTOMS | Check for import VAT | |
| NAPSA | EXCLUDE | Social security |
| ZESCO | Domestic 16% | Electricity |
| LWSC, SWSC | Domestic 16% | Water |
| MTN ZM, AIRTEL ZM, ZAMTEL | Domestic 16% | Telecoms; input tax blocked except carrier and hotel resale |
| GOOGLE, MICROSOFT, AWS | Reverse charge 16% | Non-resident |

## Deadlines and filing

Monthly return and payment on or before the 18th of the following month; nil returns are required. Oil marketing companies: 10-day periods due on the 15th, 25th and 5th.

**How to register.** Log in to the portal, click the registration module, Tax Type Amendment, answer YES to "Are you dealing in taxable goods & services for VAT purposes?", complete the form and submit. Have three months of bank statements, a business plan and a 12-month cash flow.

**How to file.** Log in at the ZRA portal (www.zra.org.zm, tax portal) with TPIN, password and captcha, enter the one-time password sent to email and phone, then choose Returns, File a return. Enter tax type Value Added Tax, account name and return period. Click Next. Answer YES or NO to the transaction questions; these decide which schedules open (for example Schedules 1 and 2 for standard-rated output). Complete the schedules, verify summary Schedules A, B and C, click Next, verify VAT payable or repayable in Schedule D, click Submit. The return reference number is generated automatically. A filed return cannot be amended on the portal: write to ZRA. Refunds are due within 30 days of the repayment return, and ZRA can offset other tax owed.

The manual return form opens with Section A: Sales, line 8 standard rated local sales, line 9 sales at minimum taxable value, line 10 disposal of capital assets, line 11 total standard rated outputs.

## Penalties and interest

Late return: K400 or 0.5% of tax payable per day, whichever is greater; applies to nil and repayment returns too. Late payment: 0.5% per day plus interest at the Bank of Zambia discount rate plus 2%. (ZRA Introduction to VAT leaflet, 2026.) Remission conditions changed from 1 January 2026 (Act 19 of 2025).

## Cross-border points

Exports are zero rated with evidence. A non-resident supplying a VAT-registered person appoints an independent VAT-registered tax agent: agent logs in to TaxOnline, Registration, Applications, Application for Reverse VAT, completes the form, uploads the appointment letter, submits. The agent files by the 18th. Agency fees carry 16% and are not claimable on that return; the non-resident stays jointly liable.

## Two worked examples that recompute

**Simple.** Sales K348 including VAT, purchases K232 including VAT (ZRA's example).

```oa-check
name: Output less input
inputs:
  output: 48
  input: 32
steps:
  - vat: output - input
expected:
  vat: 16.00
```

**Decision: pay a non-resident with or without a tax agent.** A VAT-registered firm buys K200,000 of consultancy. With no tax agent it self-accounts K32,000 with no input claim. If the supplier appoints an agent, the agent charges K32,000 on a Smart Invoice, claimable as ordinary input tax if not otherwise blocked. Agent route net cost K0 against K32,000, before any fee passed on.

```oa-check
name: Reverse VAT cost with and without agent
inputs:
  fee: 200000
  rate: 0.16
steps:
  - no_agent_cost: fee * rate
  - agent_cost: 0
  - saving: no_agent_cost - agent_cost
expected:
  no_agent_cost: 32000.00
  saving: 32000.00
```

## Ask the client first

- Registered, and from what date? Annual taxable supplies?
- Are any supplies exempt?
- Is every purchase invoice a Smart Invoice, and dated within 90 days?
- Any imported services, and does the supplier have a Zambian tax agent?
- Mining or mineral processing? Message: "Mining has specific provisions and development agreements. Escalate."
- MFEZ? Message: "Multi-Facility Economic Zone operators require certificate verification. Escalate."
Minimum input: a bank statement.

## Sources

| Source | URL | Read on |
|---|---|---|
| VAT (Amendment) Act No. 19 of 2025, whole Act; read for the figures cited | https://www.parliament.gov.zm/sites/default/files/documents/acts/Act%20No.%2019%20of%202025%20The%20Value%20Added%20Tax%20%28Amendment%29%20Act.pdf | 2026-11-01 |
| ZRA leaflet Introduction to VAT (2026), OCR read; read for the figures cited | https://www.zra.org.zm/wp-content/uploads/2026/06/Introduction-to-VAT.pdf | 2026-11-01 |
| ZRA leaflet Claiming Input Tax (2026), OCR read; read for the figures cited | https://www.zra.org.zm/wp-content/uploads/2026/06/Claiming-input-tax.pdf | 2026-11-01 |
| ZRA leaflet Reverse VAT (2026), OCR read; read for the figures cited | https://www.zra.org.zm/wp-content/uploads/2026/06/Reverse-VAT.pdf | 2026-11-01 |
| ZRA Guide to Filing Tax Returns (2026), OCR read; read for the figures cited | https://www.zra.org.zm/wp-content/uploads/2026/06/Guide-to-Filing-Tax-Returns.pdf | 2026-11-01 |
| ZRA leaflet Post-Registration Requirements (2026), OCR read; read for the figures cited | https://www.zra.org.zm/wp-content/uploads/2026/06/Post-Registration-Requirements.pdf | 2026-11-01 |
| ZRA Smart Invoice FAQs (2026), scope questions; read for the figures cited | https://www.zra.org.zm/wp-content/uploads/2026/08/Smart-Invoice-FAQs.pdf | 2026-11-01 |

Not yet confirmed: the VAT Act and the Exemption and Zero-Rating Orders themselves were not opened; ZRA leaflets stand in, so old claims that basic foodstuffs, agricultural inputs, medical equipment and domestic electricity are zero rated, and that financial, residential rental, public transport, postal and domestic water supplies are exempt, are unconfirmed; bad debt relief after 12 months; old blocked items club subscriptions and invoices without TPIN; refund after 4 months of excess credits; old box numbers 1 to 20 (replaced, only lines 8 to 11 read here); whether the K800,000 annual and K200,000 quarterly tests apply together; withholding VAT at 100% of VAT with a return credit, and the date of suspension; old filing penalty of 1,000 units; 5% a month late payment charge (the old file figure conflicts with the leaflet).

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
