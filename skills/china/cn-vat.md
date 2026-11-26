---
name: cn-vat
description: Prepare or review mainland China VAT for 2026, including taxpayer status, rates, input tax, invoices, filing and worked cases. Refer specialist elections, refunds and historical periods.
jurisdiction: CN
tax_year: 2026
last_updated: 2026-11-26
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
version: 1.5
depends_on:
  - vat-workflow-base
category: international
tier: 2
domain: vat-gst
type: situation-rules
---

# China VAT (增值税), 2026

## Who this applies to

Use this Guide for mainland China VAT returns and transaction classification for 2026. The VAT Law and Implementation Regulations apply from 1 January 2026; the law repealed the Provisional Regulations on that date. Earlier periods are referred below. Amounts are CNY. Hong Kong, Macao, Taiwan, customs duty, consumption tax and surcharges are outside this Guide. See `cn-corporate-tax`, `cn-iit`, `cn-withholding` and `cn-cross-border` for their separate subjects. [Law Arts. 3, 38][law]; [Reg. Art. 54][reg].

Before computing, obtain the taxpayer's registration record, assigned filing period, sales ledger, contracts, invoice dates, deduction vouchers and evidence of where overseas services are actually received. If status or transaction classification is unknown, establish it before calculating.

## Rates, bands and thresholds

### Taxpayer status

- Small-scale means annual taxable sales not exceeding CNY 5,000,000. Natural persons remain small-scale. Non-enterprise units with occasional taxable transactions whose main activity is outside taxable transactions may choose small-scale treatment. [Law Art. 9][law]; [Reg. Art. 7][reg].
- Annual taxable sales are cumulative sales over up to 12 consecutive months or four quarters of operation, including periods without sales. Exclude occasional intangible and real-estate disposals; allocate later sales corrections to the period in which the liability arose. [Registration §III][registration].
- On exceeding the threshold, register by the following month's filing deadline; a sales adjustment that causes the excess requires registration within 10 working days of adjustment. General status starts on the first day of the period in which the threshold was exceeded. Correct any small-scale returns already filed from that effective date. [Registration §§V–VII][registration].
- Below the threshold, sound accounts and accurate tax information permit voluntary general registration, effective from the first day of the registration period. Once registered, a general taxpayer cannot revert to small-scale. [Registration §§II, VI][registration]; [Reg. Art. 36][reg].

### Rates

These are general-method rates before any applicable exemption or special election. Classify the actual supply first. [Law Art. 10][law].

| Rate | General-method scope | Official source |
|---|---|---|
| 13% | goods, processing/repair/replacement services, movable-property leasing and imports, except the statutory reduced or zero-rate categories. | [Official provision](https://shanghai.chinatax.gov.cn/zcfw/zcfgk/zzs/202412/t474694.html) |
| 9% | transport, postal, basic telecom, construction, real-estate leasing and sales, land-use rights; the listed farm products, edible oil/salt, utilities and household fuels, publications, feed, fertiliser, pesticides, agricultural machinery and film. The statutory goods list and scope notes determine eligibility. [Law Art. 10(2)][law]; [No. 9 annexes][scope]. | [Official provision](https://shanghai.chinatax.gov.cn/zcfw/zcfgk/zzs/202412/t474694.html) |
| 6% | other services and intangibles, except the statutory 13%, 9% or zero-rate categories. Ordinary consulting, market research, IT services and qualifying courier collection/delivery are illustrated below. [Law Art. 10(3)][law]; [No. 9 Annex 2][categories]. | [Official provision](https://shanghai.chinatax.gov.cn/zcfw/zcfgk/zzs/202412/t474694.html) |
| 0% | goods exports subject to State Council exceptions; the specified cross-border services/intangibles. For design, software and information-systems services sold to overseas entities, consumption must be entirely abroad. The actual recipient must be abroad and the service unrelated to domestic goods, real estate or natural resources. A foreign customer alone is insufficient. [Law Art. 10(4)–(5)][law]; [Reg. Art. 9][reg]; [No. 11 §I(2)][exports]. Refund/exemption claim preparation is referred below. | [Official provision](https://shanghai.chinatax.gov.cn/zcfw/zcfgk/zzs/202601/t478908.html) |

### Small-scale sales

For 1 January 2026–31 December 2027, the exemption thresholds are VAT-exclusive sales of CNY 100,000 per month, CNY 300,000 per quarter, or CNY 1,000 per transaction/day (aggregate multiple transactions in one day). Below the applicable threshold, sales are exempt; **on reaching it, the whole amount is taxable**. Where a statutory margin deduction applies, use the permitted VAT-exclusive net amount for this test. [No. 10 §I][relief]; [Law Art. 23][law].

The statutory simplified levy is 3%, without input credit. From 1 January 2026–31 December 2027, eligible small-scale sales otherwise at 3% use 1%; sales/leases of real estate and transfers of land-use rights are excluded from that reduction. [Law Arts. 11, 14][law]; [No. 10 §III(3)(6)][relief].

Invoice sales benefiting from the reduction at 1%. A small-scale taxpayer can waive the reduction for all or some sales and issue special invoices at 3%; if below the exemption threshold, also waive exemption for those sales. The general 36-month lockout after waiving a relief excludes small-scale taxpayers. [STA No. 4 §§I, IV][small]; [Law Art. 27][law].

## The base

- **Compute:** general-method VAT payable = current output VAT minus creditable input VAT. Simplified-method VAT = VAT-exclusive sales × applicable levy, with no input credit. [Law Art. 14][law].
- **VAT-inclusive price:** divide by 1 + applicable VAT rate/levy to obtain the VAT-exclusive base. [Reg. Art. 16][reg].
- **Foreign currency:** convert to CNY using the central parity rate on the transaction day or the first day of that month; retain the chosen conversion basis for 12 months. [Reg. Art. 17][reg].
- **Separate transactions at different rates:** account separately or use the highest rate. Missing classification facts alone do not trigger this rule. [Law Art. 12][law].
- **One transaction with principal and ancillary elements:** apply its principal business rate where the elements have the required principal/ancillary relationship. Specialist bundled supplies are referred below. [Law Art. 13][law]; [Reg. Art. 10][reg].
- **Outside taxable transactions:** employment wages, administrative fees/government funds, legally required expropriation compensation and deposit interest. Other non-taxable income is referred below. [Law Art. 6][law].
- **Deemed sales:** a unit/sole trader uses self-produced or commissioned goods for welfare/personal consumption, or gives goods away; a unit/individual gives away intangibles, real estate or financial products. Use market value. [Law Arts. 5, 19][law].
- **Tax point:** payment during/after the transaction or the contractual right to payment; an earlier invoice advances the tax point. Without a written payment date use completion (goods dispatched, service finished or transfer completed). Deemed sales use completion and imports the customs declaration day. Earlier export declaration advances the export tax point. Prepaid services and other special tax points are referred below. [Law Art. 28][law]; [Reg. Arts. 39–41][reg].

### Input VAT and fapiao

A general taxpayer needs a lawful deduction voucher and eligible taxable use: special VAT invoice, customs import VAT certificate, withholding tax-payment certificate, qualifying farm-product invoice or another prescribed credit voucher. The last two categories' detailed calculations are referred below. Special-invoice and import credits use the VAT shown. [Law Art. 16][law]; [Reg. Arts. 11–12][reg].

Confirm eligible invoices' deduction use through the tax digital account or VAT invoice platform before claiming. A missing or unconfirmed voucher cannot support a current claim. [STA explanation, Q12][digital].

Block inputs for simplified or exempt activities, abnormal losses, staff welfare/personal consumption, and directly consumed catering, daily-life and entertainment services. Client entertainment is personal consumption. Loan interest and loan-related advisory/handling/consulting fees paid to the lender also have blocked input. Mixed use, reversals and other non-taxable activities are referred below. [Law Art. 22][law]; [Reg. Arts. 19–21][reg].

If input exceeds output, carry the excess forward or seek a refund where State Council rules permit; refund preparation is referred below. [Law Art. 21][law].

Issue invoices for taxable transactions. Special invoices show sales and VAT separately; do not issue them to natural-person purchasers, for exempt sales or in other prohibited cases. Paper and electronic invoices have equal legal effect. [Reg. Arts. 5, 37][reg]; [Law Art. 34][law].

For errors, discounts, cancellation or returns after a special invoice, follow the void/red-letter procedure before reducing output tax or sales. [Reg. Art. 38][reg].

## Deadlines and filing

The tax office assigns the filing period. Monthly/quarterly returns and payment are due within 15 days after period end. Small-scale taxpayers may use quarters. Ten-/15-day filers declare within 15 days from the first day of the next month and prepay within five days after each short period. [Law Arts. 30–31][law]; [Reg. Art. 43][reg].

For natural persons taxed per transaction, VAT can be collected when the authority issues an invoice or through withholding. Other reached-threshold transactions with VAT still unpaid must be self-declared by 30 June of the following year. Monthly-threshold exceptions and domestic withholding arrangements are referred below. [Reg. Art. 44][reg]; [STA No. 4 §§II–III][small].

Nil-tax and exempt periods still require returns. [Tax collection implementation rules, Art. 32][collection]. If the last day is a statutory holiday, the deadline moves to the day after it; three or more consecutive statutory holidays within the period extend it by those holiday days. Use the official filing calendar. [Art. 109][collection].

Fixed-place businesses file where established/resident. Without a fixed place, file where the transaction occurs. Natural-person property sales/leases, natural-resource rights and construction file at the property/resource/work location; imports follow customs filing locations. Branch consolidation and withholding locations are referred below. [Law Art. 29][law].

## Penalties and interest

Late payment, late returns, false tax bases, evasion, underpayment and any criminal exposure: Check this point with one of our partner accountants.

## Cross-border points

A foreign seller's service sold to a domestic buyer is consumed in China except on-site consumption abroad; a direct connection with domestic goods, real estate or natural resources also establishes domestic consumption. For a taxable Chinese supply by a foreign seller, the buyer withholds VAT unless a domestic agent files under the applicable State Council rules. VAT withheld = VAT-exclusive sales × rate. [Law Arts. 4, 15][law]; [Reg. Art. 4][reg].

General consulting is not automatically zero-rated. Qualifying consulting supplied to an overseas entity and consumed entirely abroad can instead be exempt: actual recipient abroad, no connection to domestic goods, real estate or natural resources, required written contract and income obtained, no disqualifying circumstance or waiver, and timely exemption declaration. Related input is blocked. Establish those conditions rather than assuming either exemption or 6% solely from the customer's address. [No. 11 §§I, VI, VII, IX][exports]; [Law Art. 22][law].

## Two worked examples that recompute

### Worked cases

All input-credit examples assume a general taxpayer, lawful vouchers confirmed for deduction, eligible taxable business use and no blocked input, except where explicitly stated. Amounts retain the original case inputs.

1. **IT consulting:** a Shanghai general taxpayer receives CNY 530,000 VAT-inclusive from a Beijing company for March 2026 consulting. Base = 530,000 ÷ 1.06 = **500,000**; output = **30,000**. Its special e-invoice shows base and VAT separately. [Law Art. 10][law]; [Reg. Arts. 5, 16][reg].
2. **Laptops:** CNY 113,000 VAT-inclusive with a special e-invoice gives base **100,000**, input **13,000**. Laptops purchased for staff welfare instead give **no credit**. Cases 1–2 alone produce net VAT **17,000**. [Law Arts. 14, 22][law]; [Reg. Arts. 12, 16][reg].
3. **Quarterly small-scale trader:** eligible goods sales, no exemption/reduction waiver, no real-estate sales. Q1 2026 VAT-exclusive CNY **280,000** is below 300,000 and exempt. Q2 **320,000** is taxed in full at 1% = **3,200**, rather than taxing only the **20,000** excess. [Law Art. 23][law]; [No. 10 §§I, III][relief].
4. **Singapore market research:** CNY **100,000** VAT-exclusive, consumed in China, foreign supplier without a domestic filing agent. Buyer withholds **6,000**. The eligible general-taxpayer buyer needs the tax-payment certificate, written contract, payment proof and foreign supplier's statement/invoice for credit; a small-scale buyer has no input credit. [Law Arts. 14–16][law]; [Reg. Art. 12][reg]; [No. 13 §I(5)][input].
5. **Business travel and dinner:** an employee's domestic business-coach ticket bearing their identity, CNY **1,030**, gives input 1,030 ÷ 1.03 × 3% = **30**. A client dinner invoice of **1,060** at 6% includes **60** VAT, which is blocked. [No. 13 §I(2)][input]; [Law Art. 22][law]; [Reg. Art. 20][reg].
6. **German packaging design:** a Shenzhen general-taxpayer studio sells design used entirely in Germany to a German company; assume the actual recipient abroad and no domestic property/goods/resource connection. The service qualifies for 0% and requires a refund/exemption declaration. Separate brand consulting is evaluated under the exemption conditions above, not automatically 0% or 6%. Claim preparation is referred below. [Reg. Art. 9][reg]; [Law Art. 33][law]; [No. 11 §§I, VI–VII][exports].
7. **Registration:** monthly-filer cumulative eligible sales reach CNY **5,200,000** in the 12 months to May 2026. Register by June's filing deadline; status starts **1 May 2026**, and correct May if already filed small-scale. If the company instead files quarterly and crosses the threshold in Q2, status starts **1 April 2026**. [Registration §§III, V–VII][registration].
8. **US client:** Shanghai general taxpayer receives CNY **700,000** VAT-exclusive. Qualifying software/information-systems services consumed entirely abroad yield **zero output** at 0%; claim preparation is referred below. Qualifying management consulting satisfying the exemption conditions above also yields **zero output**, but its related input is blocked. Otherwise taxable consulting without relief gives 700,000 × 6% = **42,000**. [Reg. Art. 9][reg]; [Law Arts. 10, 22, 33][law]; [No. 11 §§I, VI–VII, IX][exports].
9. **Courier:** CNY **9,540** inclusive for qualifying 收派服务 on a special invoice at 6% gives base **9,000**, input **540**. This assumes collection/delivery service, rather than transport-only service. [No. 9 Annex 2, p. 12][categories]; [Law Art. 10][law]; [Reg. Arts. 12, 16][reg].
10. **Cloud hosting:** domestic information-systems hosting, CNY **10,600** inclusive on a special invoice at 6%, gives base **10,000**, input **600**. [No. 9 Annex 2, p. 9][categories]; [Law Art. 10][law]; [Reg. Arts. 12, 16][reg].
11. **Payroll:** CNY **850,000** salaries for employees' services to the employer are outside taxable VAT transactions; leave them off the VAT return. [Law Art. 6][law].
12. **Special invoice:** small-scale goods sale **50,000** VAT-exclusive to a general taxpayer. Waive the 1% reduction and, if applicable, threshold exemption for this sale. VAT at 3% = **1,500**, invoiced separately; the eligible general-taxpayer buyer claims **1,500** subject to the input tests above. [STA No. 4 §§I, IV][small]; [Law Arts. 11, 14][law]; [Reg. Art. 12][reg].

### Executable checks for the preserved worked cases

```oa-check
name: China2026 general VAT output and eligible laptop input
inputs:
  consulting_vat_inclusive: 530000
  laptops_vat_inclusive: 113000
steps:
  consulting_sales: consulting_vat_inclusive / 1.06
  output_vat: consulting_sales * 0.06
  laptop_base: laptops_vat_inclusive / 1.13
  eligible_input: laptop_base * 0.13
  net_vat: output_vat - eligible_input
expected:
  consulting_sales: 500000
  output_vat: 30000
  laptop_base: 100000
  eligible_input: 13000
  net_vat: 17000
```

```oa-check
name: China2026 small-scale whole sales taxed above quarterly exemption
inputs:
  vat_exclusive_quarter_sales: 320000
steps:
  tax_on_whole_sales: vat_exclusive_quarter_sales * 0.01
expected:
  tax_on_whole_sales: 3200
```

```oa-check
name: China2026 courier input and small-scale sale at 3 percent
inputs:
  courier_vat_inclusive: 9540
  small_scale_sale: 50000
steps:
  courier_base: courier_vat_inclusive / 1.06
  courier_input: courier_base * 0.06
  small_scale_vat: small_scale_sale * 0.03
expected:
  courier_base: 9000
  courier_input: 540
  small_scale_vat: 1500
```

## When to refer

Each topic below remains within the Guide's intake, but no rate, election, credit or deadline is established by these referrals.

- **Simplified elections:** general-taxpayer 3%/5% choices, old construction/property projects, fixed-asset/second-hand goods reductions, housing rental, used cars, project-wide elections and lock-ins. Check this point with one of our partner accountants.
- **Other non-taxable and financial items:** free services, equity/dividends/futures, insurance payouts, donations, subsidies, lender income, bank/platform fees and non-domestic sales with blocked input. Check this point with one of our partner accountants.
- **Special input vouchers:** farm products/cooperatives, motor vehicles, rail/air tickets, road/bridge/lock tolls, ordinary-invoice exceptions and old invoice confirmation deadlines. Check this point with one of our partner accountants.
- **Input adjustments:** abnormal-loss classification, apportionment and annual true-up, long-term mixed-use assets, reversals and loan-fee classification. Check this point with one of our partner accountants.
- **Special tax points and prepayments:** advances, prepaid services, long-production goods, instalments, real-estate completion, bundled software/goods/telecom, abnormal prices, cross-area construction/property/oil-gas and branch prepayments. Check this point with one of our partner accountants.
- **Export procedures:** goods/deemed-export eligibility, international/space transport, overseas repairs, R&D, energy management, film/TV, circuit design/testing, business-process management, outsourcing and technology transfers; refund/exemption registration, product-specific rates (including photovoltaic/battery changes), collection/deemed collection, initial/final claim windows, bonded-zone dates, agency exports, waivers, returns and missing evidence. A missed initial window alone does not establish domestic taxation. Check this point with one of our partner accountants.
- **Exemptions and carried-forward reliefs:** agriculture, medical services, used personal goods/books, scientific/aid/disability imports, care, marriage/funerals, education/student services, cultural/religious admission, software refunds and other sector reliefs; separate accounting and waiver consequences. Check this point with one of our partner accountants.
- **Forms and historical periods:** return-box completion, prepayment forms, Shanghai pilot eligibility, 2025 returns and transition/late registration. Check this point with one of our partner accountants.
- **Domestic natural persons:** monthly-threshold exceptions, rent/interest allocation, platforms, domestic-service withholding from November 2026, declarations without withholding, and payer filing locations. Check this point with one of our partner accountants.
- **Special structures or disputes:** banks/insurers/securities firms, real-estate developers, consolidated filing, contracting/affiliation, asset-management products, restructuring, unreasonable arrangements, suspected false invoices, audits and risk reviews. Check this point with one of our partner accountants.

## Ask the client first

Collect any missing registration, sales, invoice, use, contract, payment and export evidence before deciding. Reconcile with existing records first. Identify the relevant referral above whenever it prevents a supported answer.

Before completion, reconcile sales, output VAT, eligible input and withholding to the ledger; check dates and the official filing calendar; retain evidence for every exemption/zero rate; use the correct assigned form; obtain professional review before filing or paying.

## Sources

Official texts below were read on **2026-11-26**. Article/section references above identify the operative passages. Referral topics do not establish the detailed law.

Not yet confirmed: taxpayer-specific facts and the specialist outcomes listed under When to refer. Those outcomes require the partner-accountant referral before use.

[law]: https://shanghai.chinatax.gov.cn/zcfw/zcfgk/zzs/202412/t474694.html
[reg]: https://shanghai.chinatax.gov.cn/zcfw/zcfgk/zzs/202601/t478908.html
[registration]: https://shanghai.chinatax.gov.cn/zcfw/zcfgk/zzs/202601/t478913.html
[relief]: https://shanghai.chinatax.gov.cn/zcfw/zcfgk/zzs/202602/t479283.html
[small]: https://shanghai.chinatax.gov.cn/zcfw/zcfgk/zzs/202602/t479286.html
[input]: https://shanghai.chinatax.gov.cn/zcfw/zcfgk/zzs/202602/t479292.html
[exports]: https://guangdong.chinatax.gov.cn/gdsw/zjfg/2026-02/02/content_a761ec677dbb47bda83ce41928d9ff1f.shtml
[scope]: https://shanghai.chinatax.gov.cn/zcfw/zcfgk/zzs/202602/t479282.html
[categories]: https://shanghai.chinatax.gov.cn/zcfw/zcfgk/zzs/202602/P020260202532248327615.pdf
[digital]: https://shanghai.chinatax.gov.cn/zcfw/zcjd/202411/t474124.html
[collection]: https://shanghai.chinatax.gov.cn/zcfw/zcfgk/swzsgl/200402/t284445.html

> **General reference only.** This Guide is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status or local procedures. A qualified professional in the relevant jurisdiction must review the work before filing, paying or taking a tax position.
