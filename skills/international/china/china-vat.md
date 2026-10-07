---
name: china-vat
description: Use this skill whenever asked to prepare, review, or classify transactions for a China VAT (增值税 / VAT) return, handle Golden Tax System (金税系统) compliance, classify transactions for Chinese VAT purposes, or advise on VAT registration and filing in China. Trigger on phrases like "增值税", "VAT return China", "增值税申报", "增值税专用发票", "金税系统", "一般纳税人", "小规模纳税人", or any China VAT request. ALWAYS read this skill before touching any China VAT work.
version: 2.0
jurisdiction: CN
tax_year: 2026
last_updated: 2026-09-27
authored_by: Michael Cutajar and the OpenAccountants team
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
depends_on:
  - vat-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# China VAT (增值税) for general and small-scale taxpayers, 2026: rates, the VAT Law, input credits, fapiao and filing

## Scope and the law in force ([VAT Law of the PRC](https://shanghai.chinatax.gov.cn/zcfw/zcfgk/zzs/202412/t474694.html); [VAT Law Implementation Regulations](https://shanghai.chinatax.gov.cn/zcfw/zcfgk/zzs/202601/t478908.html); [MOF/STA announcement 2026 No. 10 on VAT reliefs](https://shanghai.chinatax.gov.cn/zcfw/zcfgk/zzs/202602/t479283.html))

This Guide covers mainland China value added tax for **tax year 2026** (calendar year). It is for companies, sole traders (个体工商户) and advisers who classify transactions, prepare or review VAT returns, or answer VAT questions for general taxpayers (一般纳税人) and small-scale taxpayers (小规模纳税人).

**The law changed on 1 January 2026.** The VAT Law of the People's Republic of China (中华人民共和国增值税法) applies from that date, and the old Provisional Regulations were repealed the same day: "本法自2026年1月1日起施行。《中华人民共和国增值税暂行条例》同时废止" (Law Art. 38). The State Council's Implementation Regulations (增值税法实施条例) apply from the same date. Domestic VAT reliefs set by documents issued before 31 December 2025 stopped on 1 January 2026 unless an announcement keeps them: "在2025年12月31日前制发文件规定的国内环节增值税优惠政策同时停止执行" (No. 10). Do not rely on an old circular such as 财税〔2016〕36号 unless a 2026 source carries it forward. MOF means the Ministry of Finance and STA the State Taxation Administration.

Every rule below is stated under the law in force from 1 January 2026; 2025 periods have their own section near the end. Amounts are in renminbi (Law Art. 18).

**Not covered here:** Hong Kong, Macao and Taiwan; consumption tax; customs duty; the surcharges filed on the same return (附加税费) beyond a mention; export refund procedure beyond the basics; financial institutions, real estate developers and cross-period construction. Companion Guides: corporate income tax is in **cn-corporate-tax**, individual income tax (including tax on employees and freelancers) is in **cn-iit**, and the fuller VAT treatment of export refunds, restructurings and non-taxable receipts is in **cn-vat**.

## Ask the client first

Sources: [VAT Law](https://shanghai.chinatax.gov.cn/zcfw/zcfgk/zzs/202412/t474694.html); [Implementation Regulations](https://shanghai.chinatax.gov.cn/zcfw/zcfgk/zzs/202601/t478908.html); [STA announcement on general taxpayer registration](https://shanghai.chinatax.gov.cn/zcfw/zcfgk/zzs/202601/t478913.html).

- **Status.** General taxpayer (一般纳税人) or small-scale (小规模纳税人) on the tax office record? Taxable sales over the last 12 months (or four quarters)?
- **Who you are.** Company, sole trader (个体工商户), non-business unit or natural person?
- **Filing period.** Which period has the tax office set: 1 month, 1 quarter, 10 days or 15 days? Or do you file per transaction?
- **What you sell.** Goods, services, intangibles or real estate? Anything that could be exempt, at a different rate, or under a simplified-method election?
- **Foreign customers.** Do you export goods, or sell services or technology to overseas entities? Do you hold customs declarations, contracts and proof that the service is used abroad?
- **Foreign suppliers.** Do you buy services or intangibles from companies outside China? The Chinese buyer must withhold the VAT.
- **Purchases.** For each input you want to credit, do you hold a deduction voucher (special VAT invoice 增值税专用发票, customs import certificate, tax payment certificate 完税凭证), confirmed for use (用途确认) in the e-tax bureau?
- **Blocked uses.** Were any purchases used for staff welfare, client entertainment, meals, loans, or for exempt or simplified-method sales?
- **Free transfers.** Did you give goods away, or transfer intangibles, real estate or financial products free of charge?
- **Timing.** Did any invoice go out before you were paid? Were you paid in advance?
- **Small-scale only.** Did you invoice any sales at 3% (to issue special invoices) instead of the reduced 1% ([STA announcement 2026 No. 4](https://shanghai.chinatax.gov.cn/zcfw/zcfgk/zzs/202602/t479286.html))?

## The method, step by step

1. **Is it a taxable transaction in China?** ([VAT Law](https://shanghai.chinatax.gov.cn/zcfw/zcfgk/zzs/202412/t474694.html) Art. 3–4; [Implementation Regulations](https://shanghai.chinatax.gov.cn/zcfw/zcfgk/zzs/202601/t478908.html) Art. 4.) A paid sale of goods, services, intangibles or real estate, or an import. Goods: dispatched from or located in China. Real estate and natural resource rights: located in China. Other services and intangibles: consumed in China or sold by a domestic seller. A foreign seller's service is consumed in China when sold to a domestic buyer (unless consumed on site abroad) or when it relates directly to goods, real estate or natural resources in China.
2. **Take out what is not taxable** (Law Art. 6): wages and salaries, administrative fees and government funds collected, compensation for expropriation, and deposit interest ("取得存款利息收入"). Dividends and loan principal are not sales either. Some non-taxable receipts block related input; see **cn-vat**.
3. **Add deemed sales** (Law Art. 5, 19). Only three cases: a unit or 个体工商户 uses its own or commissioned goods for collective welfare or personal consumption; a unit or 个体工商户 gives goods away; a unit or individual transfers intangibles, real estate or financial products free of charge. Value them at market price. Free services are not deemed sales.
4. **Fix the calculation method from the status.** A general taxpayer uses the general method: output tax minus creditable input tax (Law Art. 14). A small-scale taxpayer uses the simplified method: sales × levy rate, with no input credit. Some general taxpayer activities may elect the simplified method (see the rates section).
5. **Pick the rate for each sale** (Law Art. 10–13) from the rates section. Mixed-rate sales not accounted for separately take the highest rate ("未分别核算的，从高适用税率", Art. 12).
6. **Work out the taxable amount** (Law Art. 17; Reg. Art. 15–17): the whole consideration excluding VAT; from a VAT-inclusive price, divide by (1 + rate) or (1 + levy rate). Foreign currency: central parity rate on the day of sale or the 1st of the month, fixed for 12 months once chosen.
7. **Date the liability** (Law Art. 28; Reg. Art. 39–41): the day payment is received (during or after the transaction) or the right to payment arises (the contract payment date, or else completion of the sale). An invoice issued first sets the date. Deemed sales: on completion. Imports: customs declaration date. Exports: the export declaration date if earlier.
8. **Compute output tax** or tax payable, then **test each input** (Law Art. 16, 22): credit only amounts on a lawful voucher and not blocked; apportion shared input.
9. **Carry forward excess input** or claim a refund where State Council rules allow (Law Art. 21).
10. **Apply small-scale relief** if the client is small-scale ([MOF/STA announcement 2026 No. 10](https://shanghai.chinatax.gov.cn/zcfw/zcfgk/zzs/202602/t479283.html)): test the monthly or quarterly threshold, then apply the reduced 1% where it applies.
11. **Invoice, file and pay within 15 days of the period end** (Law Art. 30); true up apportioned input in the January return (Reg. Art. 23).

## Rates and levy rates for tax year 2026 ([VAT Law Art. 10–13](https://shanghai.chinatax.gov.cn/zcfw/zcfgk/zzs/202412/t474694.html); [Implementation Regulations Art. 8–10](https://shanghai.chinatax.gov.cn/zcfw/zcfgk/zzs/202601/t478908.html); [MOF/STA announcement 2026 No. 9, scope notes](https://shanghai.chinatax.gov.cn/zcfw/zcfgk/zzs/202602/t479282.html); [MOF/STA announcement 2026 No. 10](https://shanghai.chinatax.gov.cn/zcfw/zcfgk/zzs/202602/t479283.html); [Shanghai Tax Bureau Q&A on the new law](https://shanghai.chinatax.gov.cn/tax/zcfw/rdwd/202603/t479704.html))

| Rate | What it covers (Law Art. 10) |
|---|---|
| 13% | Sales of goods, processing, repair and replacement services, leasing of tangible movable property, and imports of goods, other than those listed at 9% or 0% |
| 9% | Transport, postal, basic telecom, construction and real estate leasing services; sales of real estate; transfers of land use rights. Sales or imports of: farm products, edible vegetable oil and edible salt; tap water, heating, cooling, hot water, gas, LPG, natural gas, dimethyl ether, biogas and household coal products; books, newspapers, magazines, audio-visual products and e-publications; feed, fertiliser, pesticides, farm machinery and agricultural film |
| 6% | Sales of services and intangibles not listed at 13%, 9% or 0%: for example financial services, value-added telecom, IT, consulting, R&D, design, advertising, catering, accommodation and other consumer services |
| 0% | Exports of goods (unless the State Council provides otherwise); cross-border sales of the services and intangibles listed in Reg. Art. 9 |
| 3% levy rate | Simplified method (Law Art. 11: "征收率为百分之三") |

The law writes the rates in words ("税率为百分之十三"); the Shanghai Tax Bureau Q&A gives them in digits ("同时经营销售13%税率的货物和6%税率的服务"). The detailed scope of the 9% goods and of each service category is in the annexes to MOF/STA announcement 2026 No. 9 (from 1 January 2026), including the "适用9%增值税税率货物范围注释".

**Which services are zero-rated (Reg. Art. 9).** Only these:
- sold **to an overseas entity** and **consumed entirely outside China**: R&D, energy performance contracting, design, film and TV production and distribution, software, circuit design and testing, information systems, business process management, and offshore service outsourcing;
- technology transferred to an overseas entity and used entirely outside China;
- international transport, space transport, and repair services for overseas parties (对外修理修配).

A service that is not on this list, such as general management consulting or marketing for a foreign client, is **not** zero-rated. Exported goods means goods declared to customs, physically leaving China and sold to an overseas entity or individual, plus goods the State Council deems exported (Reg. Art. 8). Zero-rated sales are declared for refund or exemption (退（免）税) (Law Art. 33); the refund procedure is in **cn-vat**.

**Mixed and composite sales.** Separate transactions at different rates must be accounted for separately, or the highest rate applies (Law Art. 12). One transaction with a main and an ancillary part takes the main part's rate (Law Art. 13; Reg. Art. 10).

### Simplified-method elections for general taxpayers, 2026 to 2027 ([MOF/STA announcement 2026 No. 10](https://shanghai.chinatax.gov.cn/zcfw/zcfgk/zzs/202602/t479283.html))

From 1 January 2026 to 31 December 2027, a general taxpayer **may choose** the simplified method at the **3%** levy rate for listed activities, including: selling tap water; small hydropower units selling their own electricity; consignment stores; public transport (buses, metro, taxis, long-distance coaches); labour-only construction (清包工) and construction for old projects (contract start before 30 April 2016); R&D, IT and consulting services by non-enterprise units; film screening, warehousing, loading and unloading, and pick-up and delivery (收派) services; non-degree education and education support services; and some others ("可以选择适用简易计税方法，按照3%的规定征收率计算缴纳增值税"). In the same period it may choose the **5%** levy rate for listed old real estate items, such as leasing or selling real estate acquired before 30 April 2016 ("按照5%的规定征收率计算缴纳增值税"). The choice covers all taxable transactions of the same simplified-method project (construction and own-developed real estate are chosen project by project): "一般纳税人应当就同一简易计税方法项目的全部应税交易一并选择适用简易计税方法". **Lock-in:** once chosen, it cannot be changed for 36 months, and after switching back to the general method it cannot choose the simplified method again for another 36 months ("36个月内不得变更", No. 10 三（四）2). If it elects, it cannot credit the input for those items (Law Art. 22).

Also under No. 10, from 1 January 2026, these taxpayers **may choose** the simplified method ("可以选择适用简易计税方法"): a general taxpayer selling a used fixed asset whose input was blocked and not credited, a small-scale taxpayer (not a natural person) selling its own used fixed asset, and anyone selling second-hand goods (旧货), at 3% reduced to 2% ("依照3%征收率减按2%计算缴纳增值税"). Individuals (not 个体工商户 registered as general taxpayers) renting out housing may choose 3% reduced to 1.5% ("依照3%征收率减按1.5%计算缴纳增值税").

## Small-scale taxpayers in 2026 ([VAT Law Art. 9, 11, 14, 23, 27](https://shanghai.chinatax.gov.cn/zcfw/zcfgk/zzs/202412/t474694.html); [MOF/STA announcement 2026 No. 10](https://shanghai.chinatax.gov.cn/zcfw/zcfgk/zzs/202602/t479283.html); [STA announcement 2026 No. 4 on small-scale collection](https://shanghai.chinatax.gov.cn/zcfw/zcfgk/zzs/202602/t479286.html); [Implementation Regulations Art. 7, 37, 43](https://shanghai.chinatax.gov.cn/zcfw/zcfgk/zzs/202601/t478908.html))

| Item | Figure and period | Source wording |
|---|---|---|
| Who is small-scale | Annual taxable sales **not over** 500万元 (five million yuan) | "年应征增值税销售额未超过五百万元" (Law Art. 9) |
| Statutory levy rate | 3% | Law Art. 11 |
| Reduced levy rate, 1 January 2026 to 31 December 2027 | 1% on all taxable transactions **except** selling or leasing real estate and transferring land use rights | "依照3%征收率减按1%征收率征收增值税" (No. 10) |
| Prepaid items in the same period | Prepay at 1% once the total at the prepayment location reaches the threshold | "减按1%预征率预缴增值税" (No. 10) |
| Sales threshold, monthly filer, 2026 to 2027 | 10万元 (one hundred thousand yuan) of monthly sales | "起征点为月销售额10万元" (No. 10) |
| Sales threshold, quarterly filer, 2026 to 2027 | 30万元 (three hundred thousand yuan) of quarterly sales | "起征点为季度销售额30万元" (No. 10) |
| Sales threshold, per-transaction filer, 2026 to 2027 | 1,000 yuan per transaction; several transactions in one day are tested per day | "起征点为每次（日）销售额1000元" (No. 10) |

**How the threshold works (Law Art. 23).** If sales do **not reach** the threshold, they are exempt. Once sales **reach** it, VAT is charged on the **whole** amount, not just the excess: "达到起征点的，依照本法规定全额计算缴纳增值税". Where a small-scale taxpayer is allowed to deduct certain costs from its sales, the threshold is tested on the net VAT-exclusive amount (No. 10).

**Other small-scale rules:**
- No input credit. Tax payable = sales × levy rate (Law Art. 14).
- Natural persons are always small-scale. A non-business unit that has only occasional taxable sales **and** whose main business is not a taxable transaction may choose small-scale treatment ("不经常发生应税交易且主要业务不属于应税交易范围的非企业单位", Reg. Art. 7).
- **Natural persons with bond interest, rent of real estate or platform work income** test the monthly threshold on the month's total sales; a lump sum of interest or rent is spread evenly over the months it covers ("应当以当月发生全部应税交易的销售额", STA announcement 2026 No. 4, item 二).
- Small-scale taxpayers may use a quarterly period (Reg. Art. 43).
- **Invoicing at 1%.** Sales under the 1% cut must be invoiced at 1% ("应当按照1%征收率开具增值税发票"). A small-scale taxpayer may give up the cut for all or some sales in order to issue special VAT invoices ("可以选择全部或者部分应税交易放弃减税并开具增值税专用发票"); those sales are then taxed and invoiced at 3% (STA announcement 2026 No. 4, item 四).
- **Below the threshold.** A small-scale taxpayer whose sales are below the threshold may give up the exemption for all or some sales and issue special invoices ("可以选择全部或者部分应税交易放弃免税并开具增值税专用发票", STA announcement 2026 No. 4, item 一).
- No special invoice may be issued to a natural person buyer or for an exempt sale (Reg. Art. 37).
- The rule that a waived relief cannot be used again for 36 months does **not** apply to small-scale taxpayers ("小规模纳税人除外", Law Art. 27).
- A small-scale taxpayer with sound accounts may register as a general taxpayer voluntarily (Law Art. 9). Once registered, it cannot go back.

## Becoming a general taxpayer ([STA announcement 2026 No. 2 on general taxpayer registration](https://shanghai.chinatax.gov.cn/zcfw/zcfgk/zzs/202601/t478913.html); [Implementation Regulations Art. 36](https://shanghai.chinatax.gov.cn/zcfw/zcfgk/zzs/202601/t478908.html))

- **Who must register.** A taxpayer whose annual taxable sales **exceed** 500万元 (five million yuan). Two exceptions: natural persons, and non-business units with occasional taxable sales that choose small-scale treatment.
- **Annual sales.** Cumulative taxable sales over a running period of up to 12 months or four quarters of business ("连续不超过12个月或四个季度的经营期内累计应征增值税销售额"), counting months with no sales. Occasional sales of intangibles or real estate are left out. Sales adjusted later (self-correction, risk review, audit) count in the period in which the liability arose.
- **Deadline.** Register within the filing deadline of the month after the threshold is exceeded. If the threshold is exceeded because sales were adjusted, register within 10 working days of the adjustment.
- **Effective date.** The 1st day of the period in which the threshold was exceeded ("超过规定标准的当期1日"). For voluntary registration, the 1st day of the period in which the taxpayer registers. Returns already filed as small-scale from the effective date must be corrected period by period.
- **Missed deadline.** From 5 working days after the deadline, the taxpayer is managed as a general taxpayer anyway.
- **One way only.** "纳税人登记为一般纳税人后，不得转为小规模纳税人" (Reg. Art. 36).
- **Transition.** If the 2025 Q4 or December small-scale return shows the threshold exceeded, status starts on 1 January 2026. A taxpayer that before 2026 computed tax at the VAT rates without input credit also becomes a general taxpayer on 1 January 2026 ("一般纳税人生效之日为2026年1月1日", item 十一).
- **Counselling period ended.** The probationary counselling regime (纳税辅导期) for new general taxpayers stopped on 1 January 2026.

## Input tax credits (general taxpayers) ([VAT Law Art. 16, 21, 22](https://shanghai.chinatax.gov.cn/zcfw/zcfgk/zzs/202412/t474694.html); [Implementation Regulations Art. 11–12, 19–25](https://shanghai.chinatax.gov.cn/zcfw/zcfgk/zzs/202601/t478908.html); [MOF/STA announcement 2026 No. 13 on input tax](https://shanghai.chinatax.gov.cn/zcfw/zcfgk/zzs/202602/t479292.html); [MOF/STA announcement 2026 No. 10](https://shanghai.chinatax.gov.cn/zcfw/zcfgk/zzs/202602/t479283.html); [STA announcement 2019 No. 45](https://shanghai.chinatax.gov.cn/zcfw/zcfgk/zzs/202001/t451787.html))

**Deduction vouchers (Reg. Art. 11–12).** Input tax is credited only against a lawful voucher:
- the VAT shown on a special VAT invoice (增值税专用发票) from the seller, including the fully digitalised e-invoice (special invoice);
- the VAT shown on a customs import VAT payment certificate (海关进口增值税专用缴款书);
- the VAT shown on a tax payment certificate (完税凭证) for services, intangibles or domestic real estate bought from a foreign seller. The buyer must also hold a written contract, proof of payment and the foreign party's statement or invoice, or the credit is refused (No. 13, 一（五）);
- farm-product purchase or sales invoices, at a computed amount;
- other vouchers with a deduction function, shown below.

| Voucher (No. 13) | Creditable input |
|---|---|
| Unified motor vehicle sales invoice | VAT shown on it |
| Rail e-ticket or air e-ticket itinerary for domestic passenger transport | VAT shown or included on it |
| Road, waterway and other passenger tickets showing the traveller's identity | Face amount ÷ (1 + 3%) × 3% |
| Toll-road e-invoice, or e-invoice (ordinary) marked 通行费 | VAT shown on it |
| Bridge and lock toll invoices | Amount ÷ (1 + 5%) × 5% |

Apart from these, an ordinary invoice (普通发票) gives no credit.

**Farm products (No. 10, from 1 January 2026).** With a special invoice or customs certificate from a general taxpayer, credit the VAT shown. With a special invoice from a small-scale taxpayer taxed at 3%, credit the invoice amount × 9% ("以增值税专用发票上注明的金额和9%的扣除率计算进项税额"). With a farm-product sales or purchase invoice, credit the purchase price × 9%.

**Never creditable (Law Art. 22):**
1. input for items under the simplified method;
2. input for exempt items;
3. input for abnormal losses: goods stolen, lost or spoiled through poor management, or goods or real estate confiscated, destroyed or demolished for breaking the law (Reg. Art. 19);
4. purchases used for collective welfare or personal consumption. Client entertainment (交际应酬消费) counts as personal consumption (Reg. Art. 20);
5. catering, daily-life services (居民日常服务) and entertainment bought and consumed directly ("购进并直接用于消费的餐饮服务、居民日常服务和娱乐服务");
6. other items the State Council specifies. At present: loan interest, and advisory, handling and consulting fees paid to the lender that relate directly to the loan (Reg. Art. 21).

Input tied to certain non-taxable receipts (for example equity sales other than securities, and dividends) is also blocked (Reg. Art. 22); see **cn-vat**.

**Apportionment (Reg. Art. 23).** If goods (other than fixed assets) or services serve both creditable sales and simplified, exempt or blocked non-taxable items, and the input cannot be split, compute the blocked share each period by the ratio of sales or income. True it up for the whole year in the January return of the next year.

**Long-term assets in mixed use (Reg. Art. 25).** For a fixed asset, intangible or real estate with an original value **not over** 500万元 (five million yuan), all input is creditable. Above that, credit it in full on purchase and then adjust each year for the blocked use (see **cn-vat** for the method).

**Reversal (Reg. Art. 24).** If goods (other than fixed assets) or services whose input was credited later suffer an abnormal loss, or are used for welfare, personal consumption or directly consumed catering, daily-life or entertainment services, reverse (转出) the input in that period; if the input cannot be identified, use the current actual cost.

**No deadline for confirming vouchers.** The old 360-day certification window is gone. For special invoices, customs certificates, motor vehicle invoices and toll e-invoices issued from 1 January 2017, "取消认证确认、稽核比对、申报抵扣的期限". The taxpayer confirms each voucher's use (用途确认) in the e-tax bureau when filing (STA announcement 2019 No. 45, item 一). The STA policy library lists that announcement as partly in force. Check it has not been repealed before relying on it.

**Excess input (Law Art. 21).** Carry it forward, or apply for a refund (留抵退税) under State Council rules. A refund claim is a referral.

## Invoicing: fapiao and the fully digitalised e-invoice ([VAT Law Art. 34](https://shanghai.chinatax.gov.cn/zcfw/zcfgk/zzs/202412/t474694.html); [Implementation Regulations Art. 5, 37, 38](https://shanghai.chinatax.gov.cn/zcfw/zcfgk/zzs/202601/t478908.html); [STA: nationwide digital e-invoice](https://www.chinatax.gov.cn/chinatax/n810219/n810780/c5236090/content.html); [Shanghai Tax Bureau explanation](https://shanghai.chinatax.gov.cn/zcfw/zcjd/202411/t474124.html); [STA announcement 2026 No. 4](https://shanghai.chinatax.gov.cn/zcfw/zcfgk/zzs/202602/t479286.html))

- A taxpayer must issue an invoice to the buyer for each taxable transaction (Reg. Art. 37). A special VAT invoice shows the sales amount and the VAT separately (Reg. Art. 5).
- **No special invoice** may be issued where the buyer is a natural person, where the sale is exempt, or in other cases MOF and the STA specify (Reg. Art. 37). Issue an ordinary invoice instead.
- If a special invoice is wrong, or the sale is discounted, suspended or returned, void it or issue a red-letter special invoice (红字增值税专用发票). Otherwise output tax or sales cannot be reduced (Reg. Art. 38).
- Paper and electronic invoices have the same legal effect, and the state promotes electronic invoices (Law Art. 34).
- **Fully digitalised e-invoices (数电发票)** have been in nationwide use since 1 December 2024 ("自2024年12月1日起，在全国正式推广应用全面数字化电子发票"). They come as an e-invoice (special invoice) and an e-invoice (ordinary invoice). Numbers are assigned nationally, the invoicing limit (发票总额度) is granted automatically, and issuing, delivery, checking and use confirmation (用途勾选) all happen in the national e-tax bureau. Taxpayers no longer need to obtain a dedicated tax-control device first ("不再需要预先领取专用税控设备").
- For a purchase invoice, the practical check is whether it is in the client's tax digital account (税务数字账户) and has been confirmed for use, not whether it went through the old Golden Tax device process.

## Exemptions in 2026 ([VAT Law Art. 24–27](https://shanghai.chinatax.gov.cn/zcfw/zcfgk/zzs/202412/t474694.html); [Implementation Regulations Art. 26–31](https://shanghai.chinatax.gov.cn/zcfw/zcfgk/zzs/202601/t478908.html); [MOF/STA announcement 2026 No. 10](https://shanghai.chinatax.gov.cn/zcfw/zcfgk/zzs/202602/t479283.html))

Statutory exemptions (Law Art. 24):
1. Farm producers selling their own primary farm products; ploughing, irrigation, pest control, plant protection, agricultural insurance and related training; breeding and disease control for poultry, livestock and aquatic animals. Selling purchased primary farm products, or primary products made from purchased farm products, does **not** qualify ("纳税人销售外购的初级农产品...不属于本项目免征增值税的范围", No. 10 二（一）1).
2. Medical services by medical institutions. For-profit cosmetic medical institutions are excluded (Reg. Art. 27).
3. Antique and old books; used personal goods sold by natural persons.
4. Imported instruments and equipment used directly for scientific research, experiments and teaching.
5. Imported materials and equipment given free by foreign governments and international organisations.
6. Articles for disabled people imported directly by organisations of disabled people; services provided by disabled individuals.
7. Care services of nurseries, kindergartens (only fees within the approved fee standard: "有关收费标准规定以内的保育费、保育教育费", Reg. Art. 29), elderly-care institutions and disability-service institutions; marriage introduction; funeral services.
8. Degree education provided by schools; work-study services by students.
9. First-gate admission income of memorial halls, museums, cultural centres, heritage sites, art galleries, exhibition halls, painting academies and libraries for cultural events, and of religious sites for cultural or religious events.

Other reliefs exist only as the State Council provides (Law Art. 25). No. 10 carries many forward, several only from 1 January 2026 to 31 December 2027. If a relief is not in Law Art. 24 or a 2026 announcement, do not assume it survived. Residential rent is **not** exempt (see the 1.5% election in the rates section).

Using an exemption:
- Account for exempt sales separately, or the exemption is lost (Law Art. 26).
- A taxpayer may waive an exemption, but then cannot use it again for 36 months; small-scale taxpayers are not locked in (Law Art. 27).
- Input for exempt items is not creditable (Law Art. 22), and no special invoice may be issued for an exempt sale (Reg. Art. 37).

## Boundary and exception table ([VAT Law](https://shanghai.chinatax.gov.cn/zcfw/zcfgk/zzs/202412/t474694.html); [Implementation Regulations](https://shanghai.chinatax.gov.cn/zcfw/zcfgk/zzs/202601/t478908.html); [MOF/STA announcement 2026 No. 13](https://shanghai.chinatax.gov.cn/zcfw/zcfgk/zzs/202602/t479292.html); [MOF/STA announcement 2026 No. 10](https://shanghai.chinatax.gov.cn/zcfw/zcfgk/zzs/202602/t479283.html))

| Situation | Treatment | Basis |
|---|---|---|
| Deposit interest received | Not taxable | Law Art. 6 |
| Loan interest received by a lender | Taxable financial service at 6% | Law Art. 10 |
| Bank charges and payment-platform fees paid | Taxable; creditable on a special invoice unless directly related to a loan | Law Art. 10; Reg. Art. 21 |
| Loan interest paid, and loan-related fees paid to the lender | Input not creditable | Reg. Art. 21 |
| Deposit or advance received before the transaction starts (no invoice issued) | Not yet "payment received", which means money received during or after the transaction. Exceptions: services paid in advance (see below) and invoices issued early | Law Art. 28; Reg. Art. 39 |
| Express courier services (收派服务) | A logistics support service within modern services, taxed at 6%, not transport at 9% ("快递企业提供快递服务取得的收入，按照收派服务缴纳", [No. 9 Annex 2](https://shanghai.chinatax.gov.cn/zcfw/zcfgk/zzs/202602/P020260202532248327615.pdf)). A general taxpayer courier may elect the simplified 3%; credit what the special invoice shows | Law Art. 10; No. 9 Annex 2; No. 10 |
| Staff meals, client dinners, entertainment, food delivery for staff | Input not creditable | Law Art. 22; Reg. Art. 20 |
| Software sold with installation, maintenance or training | Software product rate on the whole | No. 13 三 |
| Machinery or steel structures sold with installation | Goods rate on the whole | No. 13 三 |
| Service paid in advance and delivered over time | Tax point is the earlier of the day the service actually starts and the contract date, on the whole amount received | No. 13 四（二） |
| Foreign company sells a service to a Chinese business | Buyer withholds VAT at the applicable rate, unless a domestic agent files | Law Art. 15 |
| Price unusually low or high without good reason | Tax office may assess the value (cost-plus uses a 10% profit margin) | Law Art. 20; Reg. Art. 18 |

## Worked cases (tax year 2026) ([VAT Law](https://shanghai.chinatax.gov.cn/zcfw/zcfgk/zzs/202412/t474694.html); [Implementation Regulations](https://shanghai.chinatax.gov.cn/zcfw/zcfgk/zzs/202601/t478908.html); [MOF/STA announcement 2026 No. 10](https://shanghai.chinatax.gov.cn/zcfw/zcfgk/zzs/202602/t479283.html); [STA announcement 2026 No. 4](https://shanghai.chinatax.gov.cn/zcfw/zcfgk/zzs/202602/t479286.html))

Cases 1 to 6: a Shanghai IT consulting company, general taxpayer, monthly filer, April 2026 bank statement.

**Case 1: domestic consulting income at 6%.** It receives 530,000 yuan including VAT from a Beijing company for IT consulting. Sales = 530,000 ÷ 1.06 = 500,000. Output VAT = 500,000 × 6% = 30,000. It issues a special e-invoice showing both amounts.

**Case 2: laptops at 13%.** It pays Lenovo 113,000 yuan including VAT for ten laptops and receives a special e-invoice. Sales amount = 113,000 ÷ 1.13 = 100,000. Input VAT = 100,000 × 13% = 13,000, creditable once confirmed for use. With only an ordinary invoice, no credit. If the laptops were given to staff as welfare, the 13,000 would not be creditable (Law Art. 22).

**Case 3: services for a US client.** It receives 700,000 yuan (VAT-exclusive price) from a US company. If the work is software development or information systems services for the US company and is consumed entirely outside China, it is zero-rated (Reg. Art. 9): output VAT nil, and the company declares refund or exemption. If it is general management advice, it is not on the list: output VAT = 700,000 × 6% = 42,000. Until the contract and evidence of use abroad are in hand, book the 42,000.

**Case 4: courier fees.** It pays SF Express 9,540 yuan for March deliveries and receives a special invoice for 收派服务 at 6%. Sales amount = 9,540 ÷ 1.06 = 9,000. Input VAT = 540. (The old version of this example used 9%. Courier income is taxed as 收派服务, not transport.)

**Case 5: cloud hosting.** Alibaba Cloud charges 10,600 yuan including VAT at 6%. Sales amount = 10,000. Input VAT = 600, creditable with the special invoice.

**Case 6: payroll.** Salaries of 850,000 yuan paid. Not a taxable transaction (Law Art. 6). Leave it off the VAT return.

**Case 7: small-scale quarterly filer and the threshold.** A small-scale trading company files quarterly, sells no real estate, invoices at 1% and has not given up the cut. Q1 2026 VAT-exclusive sales: 280,000 yuan. Below 30万元 (three hundred thousand yuan), so exempt. Q2 2026 sales: 320,000 yuan. The threshold is reached, so the whole amount is taxed: 320,000 × 1% = 3,200, not 1% of the 20,000 excess.

**Case 8: small-scale sale with a special invoice.** The same company sells goods for 50,000 yuan (VAT-exclusive) to a general taxpayer that wants a special invoice. It gives up the 1% cut for that sale: VAT = 50,000 × 3% = 1,500, shown on a special invoice. The buyer credits 1,500.

**Case 9: buying a service from abroad.** A Chinese company buys market research from a Singapore company with no Chinese agent, for 100,000 yuan (VAT-exclusive), used in China. The buyer withholds 100,000 × 6% = 6,000 and remits it. It may credit the 6,000 with the tax payment certificate, the written contract, proof of payment and the Singapore company's statement or invoice.

**Case 10: crossing 500万元.** A small-scale company filing monthly reaches cumulative sales of 5,200,000 yuan for the 12 months to May 2026. That exceeds 500万元 (five million yuan). It must register by the June filing deadline. General taxpayer status takes effect on 1 May 2026, and the May return filed as small-scale must be corrected. For a quarterly filer the period is the quarter, so status would start on 1 April 2026.

### Conservative defaults when facts are missing ([VAT Law](https://shanghai.chinatax.gov.cn/zcfw/zcfgk/zzs/202412/t474694.html))

- Rate unknown, or mixed-rate sales not accounted for separately: use the higher rate (Law Art. 12).
- Voucher missing or not confirmed: credit nothing until it is held and confirmed.
- Export or foreign-use evidence missing: treat the sale as domestic and taxable.
- Status unknown: confirm it from the tax office record before computing anything.

## When to refuse or refer

Sources: [VAT Law](https://shanghai.chinatax.gov.cn/zcfw/zcfgk/zzs/202412/t474694.html); [Implementation Regulations](https://shanghai.chinatax.gov.cn/zcfw/zcfgk/zzs/202601/t478908.html).

Refer to a Chinese certified tax agent (税务师) or CPA (注册会计师) when:
- an export refund or exemption claim, or a refund of excess input (留抵退税), has to be prepared;
- the client is a bank, insurer, securities firm or other financial institution, or sells financial products;
- the client develops or sells real estate, or has construction or property work needing prepayment (Reg. Art. 45);
- the client files on a consolidated head-office basis (Law Art. 29; Reg. Art. 42), or is restructuring (merger, division, sale of a business);
- a long-term asset over 500万元 (five million yuan) is in mixed use (Reg. Art. 25);
- the client relies on a relief not found in Law Art. 24 or a 2026 announcement;
- there is any sign of false invoicing (虚开发票), which can be a crime, or the tax office has opened an audit or risk review.

Refuse to:
- claim input tax for a small-scale taxpayer;
- zero-rate a service not on the Reg. Art. 9 list, or without proof of use abroad;
- issue a special invoice to an individual consumer or for an exempt sale;
- present a computation as final without a professional check.

## Filing and payment ([VAT Law Art. 29–32](https://shanghai.chinatax.gov.cn/zcfw/zcfgk/zzs/202412/t474694.html); [Implementation Regulations Art. 43–45](https://shanghai.chinatax.gov.cn/zcfw/zcfgk/zzs/202601/t478908.html); [STA announcement 2026 No. 6 on returns](https://shanghai.chinatax.gov.cn/zcfw/zcfgk/zzs/202602/t479295.html); [Shanghai Tax Bureau announcement 2026 No. 1](https://shanghai.chinatax.gov.cn/zcfw/zcfgk/zzs/202606/t480523.html); [Tax Collection Administration Law](https://shanghai.chinatax.gov.cn/zcfw/zcfgk/swzsgl/200609/t284229.html); [its Implementation Rules](https://shanghai.chinatax.gov.cn/zcfw/zcfgk/swzsgl/200402/t284445.html))

| Period | Who | Return and payment due |
|---|---|---|
| 1 month | Most general taxpayers | Within 15 days after the month ends |
| 1 quarter | Small-scale taxpayers; banks, finance companies, trust companies and credit cooperatives; others the STA designates (Reg. Art. 43) | Within 15 days after the quarter ends |
| 10 or 15 days | As the tax office sets | Prepay within 5 days after each period; file within 15 days from the 1st of the next month (Law Art. 30–31) |
| Per transaction | Taxpayers without regular taxable sales | If sales reach the threshold, by 30 June of the next year (Reg. Art. 44) |

- The tax office sets each taxpayer's period by the amount of tax (Law Art. 30). The old 1-day, 3-day and 5-day periods are gone.
- There is **no annual VAT return**. The only annual step is the January true-up of apportioned input (Reg. Art. 23).
- Nil returns are still required: "纳税人在纳税期内没有应纳税款的，也应当按照规定办理纳税申报" (Implementation Rules Art. 32). This applies during an exemption too.
- If the last day falls on a public holiday, the deadline moves to the day after the holiday, and three or more consecutive holidays inside the period extend it (Implementation Rules Art. 109). Use the tax office's published filing calendar for the month.
- **Where:** where the business is registered or the taxpayer lives. Branches in another county file separately unless consolidated filing is approved. Import VAT is collected by customs (Law Art. 29, 32).
- **Forms:** the 增值税及附加税费申报表 (general taxpayer and small-scale versions), filed in the national e-tax bureau, with some fill-in rules changed from 1 February 2026 (STA announcement 2026 No. 6). Some Shanghai taxpayers picked by the Shanghai Tax Bureau have piloted a revised form since 5 June 2026; use it only if the tax office has told the client it is in the pilot. The surcharges (city maintenance and construction tax and education surcharges) go on the same return.

**Penalties (Tax Collection Administration Law):**

| Failure | Consequence | Article |
|---|---|---|
| Late payment | Surcharge of 0.05% of the unpaid tax per day ("按日加收滞纳税款万分之五的滞纳金") | 32 |
| Late filing | Fine of up to two thousand yuan ("二千元以下"); in serious cases two thousand to ten thousand yuan ("二千元以上一万元以下") | 62 |
| Tax evasion (false books, hidden income, false returns) | Tax and surcharge recovered, plus a fine of half to five times the tax ("百分之五十以上五倍以下"); criminal liability if it is a crime | 63 |
| Not filing, so tax goes unpaid | Tax and surcharge recovered, plus a fine of half to five times the tax | 64 |
| Fabricating a false tax base | Fine of up to fifty thousand yuan ("五万元以下") | 64 |

## Returns for 2025 periods ([VAT Law Art. 38](https://shanghai.chinatax.gov.cn/zcfw/zcfgk/zzs/202412/t474694.html); [STA announcement 2026 No. 2](https://shanghai.chinatax.gov.cn/zcfw/zcfgk/zzs/202601/t478913.html))

Periods up to 31 December 2025 stay under the Provisional Regulations and the policies in force then. Do not apply the new law's deemed-sale, blocked-input or tax-point rules to 2025 transactions. If the 2025 Q4 or December small-scale return shows the threshold exceeded, general taxpayer status starts on 1 January 2026, not earlier; later adjustments to 2025 sales cannot make it start before that date. For a 2025 period, check the rule in force at the time before using this Guide.

## Completion checklist ([VAT Law](https://shanghai.chinatax.gov.cn/zcfw/zcfgk/zzs/202412/t474694.html); [MOF/STA announcement 2026 No. 10](https://shanghai.chinatax.gov.cn/zcfw/zcfgk/zzs/202602/t479283.html))

- [ ] Status confirmed from the tax office record; 12-month sales tested against 500万元 (five million yuan).
- [ ] Filing period confirmed.
- [ ] Non-taxable items removed (wages, deposit interest, dividends, loan principal).
- [ ] Deemed sales added at market value.
- [ ] Each sale at the right rate (13%, 9%, 6%, 0%) or levy rate, with separate accounting for mixed rates.
- [ ] Small-scale: threshold tested (10万元 a month or 30万元 a quarter); 1% applied, or 3% where the cut was given up for special invoices.
- [ ] Tax points checked for advances, early invoices and exports.
- [ ] Every credited input has a lawful voucher confirmed for use.
- [ ] Blocked input removed: welfare, entertainment, catering, loan interest, exempt and simplified items; shared input apportioned.
- [ ] Foreign-seller purchases: VAT withheld and remitted; certificate, contract, payment proof and statement held.
- [ ] Zero-rated services matched to the Reg. Art. 9 list, with evidence.
- [ ] Wrong or returned special invoices voided or reversed (red-letter).
- [ ] Return filed and tax paid within 15 days of the period end.

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
