---
name: ct-sales-tax
description: "Use for Connecticut sales/use tax, economic nexus, luxury items, software and OS-114 filing."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/ct-sales-tax"
  jurisdiction: "US-CT"
  tax_year: "2026"
  last_updated: "2026-11-13"
---

# Connecticut sales and use tax

> **General reference only.** Written by Codex. Not reviewed by an accountant. Obtain qualified professional review before filing, paying or taking a tax position.

> **Circular 230 section 10.37:** Apply relevant law to the taxpayer's facts, evaluate reasonable assumptions and relevant circumstances, and obtain professional review of federal tax implications. Federal computations belong to linked federal owner skills.

**Answer first.** Connecticut generally charges 6.35%, with no local sales tax. Luxury categories have different price thresholds, computer/data services and qualifying business software have a 1% rate, and prepared meals have a 7.35% rate. The old blanket clothing exemption and luxury threshold were incorrect. [DRS sales tax information](https://portal.ct.gov/drs/sales-tax/tax-information) supports the current rates; [Chapter 219](https://www.cga.ct.gov/current/pub/chap_219.htm) supplies the remote-seller AND test and filing thresholds.

## Scope

Ordinary Connecticut retail sales, consumer use tax, remote-seller registration, exemptions and OS-114 returns. Covers 2026 transactions, with final forms and account-specific filing assignments checked before submission. `ct-income-tax` owns the individual return and its use-tax cross-reference, `ct-corporate-tax` owns corporate tax, and `ct-payroll` owns employer withholding/SUI. `us-sales-tax` supplies multistate context rather than Connecticut rates.

## Ask the client first

1. Seller locations, employees, inventory, affiliates, marketplaces and existing Connecticut permits.
2. Connecticut receipts and retail transaction counts for the twelve months ending September 30, plus marketplace collection evidence.
3. Exact item/service, selling price, delivery/user location, business/personal software use and physical media.
4. Exemption/resale certificates, manufacturing use, food or prescription classification and holiday dates.
5. Assigned filing frequency, period sales, exemptions, purchases without tax, payments and notices.

## The method, step by step

1. **Establish registration.** Physical presence and other statutory retailer categories apply independently of the economic test. For an out-of-state seller soliciting Connecticut sales, the ordinary statutory test is **at least $100,000 gross receipts AND 200 or more retail sales**, for Connecticut delivery during the twelve-month period ending September 30 immediately preceding the monthly or quarterly period. Neither limb alone establishes that particular test. Do not substitute current/prior calendar year. Marketplace-facilitator rules are separate: section 12-408e uses a $250,000 facilitated-sales threshold for the prior twelve months; distinguish facilitator and seller duties and avoid collecting twice. [Sections 12-407(a)(12)(G), (15)(A)(v) and 12-408e](https://www.cga.ct.gov/current/pub/chap_219.htm).
2. **Get a permit before taxable business starts.** Apply through myconneCT. DRS charges $100 for a Sales and Use Tax Permit; each location needs its own permit and an acquired business cannot use its predecessor's permit. [DRS registration instructions](https://portal.ct.gov/drs/sales-tax/tax-information).
3. **Classify the sale and delivery.** Connecticut delivery/use matters; a seller address alone does not establish taxability. The old blanket destination label does not decide digital goods, multi-user software, drop shipments or special sourcing. Keep invoice/delivery evidence; unresolved special sourcing is a gap below.
4. **Apply the appropriate rate to the taxable selling price**, retaining certificates for excluded sales. Luxury tax applies to the full selling price of the qualifying item, not just its excess over the threshold. Do not split one item to avoid the threshold.
5. **Accrue consumer use tax** on taxable Connecticut purchases when the vendor did not collect the proper tax, allowing only a legally available credit for tax paid elsewhere. Ordinary use tax follows the same applicable rate/classification. Do not assume an internet purchase is exempt. [DRS sales/use guidance](https://portal.ct.gov/drs/sales-tax/tax-information).
6. **File OS-114 and pay** electronically through myconneCT for the assigned period, including zero returns and nontaxable sales. The ordinary due date is the last day of the next month. Under section 12-414 the prior twelve months ending June 30 determine annual eligibility below $1,000 liability, quarterly eligibility at least $1,000 but below $4,000, otherwise monthly. DRS assignments and special weekly remittance provisions can override the ordinary schedule. Do not replace the assigned frequency without approval. [Section 12-414](https://www.cga.ct.gov/current/pub/chap_219.htm); [current DRS filing instructions](https://portal.ct.gov/drs/sales-tax/tax-information).

### Rates, bands and thresholds

| Transaction | Rate/amount and boundary | Official source |
|---|---|---|
| Ordinary taxable goods/services | 6.35%; no municipal add-on | [sales](https://portal.ct.gov/drs/sales-tax/tax-information) |
| Most motor vehicles | 7.75% when price exceeds $50,000; statutory exclusions require classification | [sales](https://portal.ct.gov/drs/sales-tax/tax-information) |
| Jewelry, real or imitation | 7.75% when price exceeds $5,000 | [sales](https://portal.ct.gov/drs/sales-tax/tax-information) |
| Clothing, footwear, handbags, luggage, umbrellas, wallets or watches | 7.75% when price exceeds $1,000, otherwise ordinarily 6.35% | [sales](https://portal.ct.gov/drs/sales-tax/tax-information) |
| Meals and certain beverages | 7.35% | [sales](https://portal.ct.gov/drs/sales-tax/tax-information) |
| Passenger motor vehicle rental, 30 days or less | 9.35%; the former 7.75% claimed maximum was incorrect | [sales](https://portal.ct.gov/drs/sales-tax/tax-information) |
| Computer/data processing services | 1%, subject to correct service classification | [service](https://portal.ct.gov/drs/sales-tax/services-subject-to-sales-and-use-taxes) |
| Electronically accessed/transferred canned software for business use, without any tangible property | 1%, with purchaser business information and retailer good faith | [softactual](https://portal.ct.gov/-/media/drs/publications/pubssn/2019/sn-2019(8).pdf) |
| Personal canned software, or software provided with tangible property | 6.35% even if the physical item merely authorizes electronic access | [softactual](https://portal.ct.gov/-/media/drs/publications/pubssn/2019/sn-2019(8).pdf) |
| Ordinary digital goods | 6.35%; specified newspapers/subscription magazines/textbooks are exceptions | [softactual](https://portal.ct.gov/-/media/drs/publications/pubssn/2019/sn-2019(8).pdf) |

**Clothing and the holiday.** Ordinary clothing under $50 is **not** generally exempt. DRS's alert on SN 2003(3) states that exemption was repealed July 1, 2011. The DRS 2026 development reports an enacted change, effective from passage, changing the annual sales-tax-free-week item threshold to **less than $300** and adding cleated shoes and backpacks; do not apply this limited holiday all year. Confirm the designated holiday dates and item definitions before using it. The old $50-$999 / $1,000+ split was wrong at the boundary: an ordinary $1,000 item does not exceed the luxury threshold. [DRS repeal alert](https://portal.ct.gov/drs/publications/special-notices/2003/sn-2003-3); [2026 developments](https://portal.ct.gov/drs/miscellaneous-taxes/other-tax-page/state-tax-developments/2026-developments).

**Exemptions are conditional.** Grocery food for human consumption is generally exempt; prepared meals are separately taxable. Prescription drugs, qualifying manufacturing machinery/equipment and purchases for resale require the precise statutory conditions and documentation, rather than a blanket exemption for every medical or factory purchase. Chapter 219 section 12-412 contains the food, prescription and manufacturing exemptions; section 12-410 governs resale. The old broad professional-service exemption cannot be used: DRS lists taxable business management/consulting, personnel training, interior design and other enumerated services. Classify the actual service. [Sections 12-410 and 12-412](https://www.cga.ct.gov/current/pub/chap_219.htm); [DRS taxable services](https://portal.ct.gov/drs/sales-tax/services-subject-to-sales-and-use-taxes).

**SaaS and digital sourcing.** A software subscription is not automatically a 1% computer service. Establish business use, delivery method, any physical property and the contract; digital content is separately classified. SN 2019(8) presumes digital goods delivered into Connecticut where the consumer/subscriber billing address is Connecticut unless contracts or other documents specifically provide otherwise. Retain business buyer name, address, orderer's name/title and business-use identification for the 1% software treatment. Resale of software requires unaltered onward sale/license/lease; digital-goods/service resale has its own integral-component conditions. [SN 2019(8), pages 1-3](https://portal.ct.gov/-/media/drs/publications/pubssn/2019/sn-2019(8).pdf).

## Worked cases

**Case 1, general sale and use tax.** A taxable $1,000 item delivered for Connecticut use incurs $63.50 tax and $1,063.50 total. If an unregistered vendor collects none and no exemption/credit applies, the purchaser accrues the same $63.50 use tax.

```oa-check
name: CT ordinary sales and use tax
inputs:
  price: 1000
  rate: 0.0635
steps:
  - tax: price * rate
  - total: price + tax
expected:
  tax: 63.5
  total: 1063.5
```

**Case 2, luxury boundaries and software.** A $1,000 coat is ordinarily taxed at 6.35% ($63.50); a $1,001 coat exceeds $1,000 and is taxed in full at 7.75% ($77.5775 before cent rounding). Qualifying electronic business software costing $1,000 incurs $10; personal software at that price incurs $63.50. No holiday applies in these facts.

```oa-check
name: CT luxury boundary and software
inputs:
  coat_at: 1000
  coat_over: 1001
  software: 1000
steps:
  - ordinary: coat_at * .0635
  - luxury: coat_over * .0775
  - business_software: software * .01
  - personal_software: software * .0635
expected:
  ordinary: 63.5
  luxury: 77.5775
  business_software: 10
  personal_software: 63.5
```

**Case 3, remote seller AND test.** A seller with no other nexus has $120,000 Connecticut receipts but 199 transactions in the statutory measuring period. This particular test fails. At $100,000 and 200 retail sales, both limbs are met. Physical presence, affiliates and marketplace obligations must still be checked separately.

## When to refuse or refer

Refer unresolved nexus, contested assessments, exemption disputes, bundled software/services, multi-user or multistate sourcing and marketplace double collection to a Connecticut tax professional. Do not apply stale values simply because a prior skill listed them.

Former agency landing URL retained: https://portal.ct.gov/DRS. The specific current publications below supply usable authority.

## Sources

| Source | Read scope | Read date |
|---|---|---|
| [DRS Sales and Use Tax Information](https://portal.ct.gov/drs/sales-tax/tax-information) | Read for current registration, rates, permits, filing and use tax. | 2026-11-13 |
| [CGA Chapter 219](https://www.cga.ct.gov/current/pub/chap_219.htm) | Read for retailer/economic nexus definitions, marketplace provisions, sections 12-410, 12-412 and 12-414 with adjacent clauses. | 2026-11-13 |
| [DRS Services Subject to Sales and Use Taxes](https://portal.ct.gov/drs/sales-tax/services-subject-to-sales-and-use-taxes) | Read for enumerated services and computer/software classification. | 2026-11-13 |
| [SN 2019(8)](https://portal.ct.gov/-/media/drs/publications/pubssn/2019/sn-2019(8).pdf) | Read for all three pages, digital goods, software use/delivery, sourcing and resale conditions. | 2026-11-13 |
| [SN 2003(3), current alert](https://portal.ct.gov/drs/publications/special-notices/2003/sn-2003-3) | Read for 2011 repeal alert, distinguishing obsolete body text. | 2026-11-13 |
| [DRS 2026 developments](https://portal.ct.gov/drs/miscellaneous-taxes/other-tax-page/state-tax-developments/2026-developments) | Read for sales-tax holiday threshold and eligible-item amendments. | 2026-11-13 |

## Not yet confirmed

- Exact designated 2026 holiday dates/item exclusions and special sales-sourcing cases were not fully read in a dedicated holiday/sourcing publication; no unconditional holiday exemption is supplied.
- Connecticut's old SST nonmember assertion has not been reverified from a Connecticut primary source; no SST membership conclusion is used.
- Special weekly remittance triggers, discounts, penalties, interest and exemption certificate-specific procedures are outside the ordinary workflow supplied here. Obtain the current official instructions for the actual account before those decisions.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-13. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `ct-sales-tax` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/ct-sales-tax. If neither is available, confirm every figure against the official source pages cited above before relying on it.
